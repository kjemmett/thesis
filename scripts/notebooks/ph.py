import glob
import pandas as pd
import numpy as np
from Bio import SeqIO
from dionysus import Simplex, Filtration, StaticPersistence, \
                        vertex_cmp, data_cmp, data_dim_cmp, DynamicPersistenceChains, \
                        ExplicitDistances, Rips
        
from scipy.spatial.distance import squareform
from itertools import combinations

import matplotlib.pyplot as plt
import seaborn as sns

class Distances:
    """Distances Class
    Takes a numpy array as input
    """
    def __init__(self, d):
        self.d = d
        self.n = len(d)

    def __len__(self):
        return self.n

    def __call__(self, i, j):
        return self.d[i][j]
    

def compute_persistence_rips(dmat, max_dim=2, max_filt=None, verbose=False):

    num_points = dmat.shape[0]
    if verbose:
        print 'building complex'

    if not max_filt:
        max_filt = np.max(dmat)+1

    distances = ExplicitDistances(Distances(dmat))
    rips = Rips(distances)

    simplices = Filtration()
    rips.generate(max_dim, max_filt, simplices.append)

    for s in simplices: s.data = rips.eval(s)
    simplices.sort(data_dim_cmp)
    
    pp = StaticPersistence(simplices)
    if verbose:
        print "Persistence initialized"

    pp.pair_simplices()
    if verbose:
        print "Simplices paired"

    smap = pp.make_simplex_map(simplices)
    if verbose:
        print "Number of unpaired simplices:", len([i for i in pp if i.unpaired()])
        print "Number of paired simplices:", len([i for i in pp if not i.unpaired()])

    bars = {dim:[] for dim in range(max_dim)}
    
    for i in pp:
        if i.sign():
            b = smap[i]

            if b.dimension() >= max_dim:
                continue

            if i.unpaired():
                if verbose:
                    print b.dimension(), b.data, "inf"
                bars[b.dimension()].append((b.data, 'inf'))
                continue

            d = smap[i.pair()]


            if d.data > b.data:
                if verbose:
                    print b.dimension(), b.data, d.data
                bars[b.dimension()].append((b.data, d.data))
                #for ii in i.chain: print smap[ii]
                #for ii in i.pair().cycle: print smap[ii]

    return bars


def gen_random_dmat(loc=0, scale=1, size=(1,1)):
    A = np.random.normal(loc=loc, scale=scale, size=size)
    A[np.diag_indices_from(A)] = 0
    A = (A + A.T)/2.0
    
    return A


def get_birth_and_deaths(bars):
    births = [bar[0] for bar in bars[1]]
    deaths = [bar[1] for bar in bars[1]]
    return births, deaths


def seqpdist(seq1, seq2):
    d = sum(i != j for (i,j) in zip(str(seq1), str(seq2)))

    return d


def make_gene_dmat(seqs):
    seqids = seqs.keys()
    dmat = pd.DataFrame(index=seqids, columns=seqids)

    for i in seqids:
        for j in seqids:
            dmat[i][j] = seqpdist(seqs[i], seqs[j])
            dmat[j][i] = dmat[i][j]

    return dmat


def make_seq_dmat(df, gdmat):
    genes = gdmat.keys() 
    num_seqs = df.shape[0]
    dmat = np.zeros((num_seqs, num_seqs))
    
    for i in range(num_seqs):
        for j in range(i, num_seqs):
            d = 0
            for gene in genes:
                d = d + g_dmat[gene][df.iloc[i][gene]-1, df.iloc[j][gene]-1]
            dmat[i, j] = d
            dmat[j, i] = d

    return dmat


def analyze_strain(datpath, strain):
    df = pd.read_csv('{0}/{1}/{1}.txt'.format(datpath, strain), sep='\t', index_col=0)
    genes = [col for col in df.columns if ('clonal_complex' not in col)]

    # parse df to 
    print genes
    gdmat = {}
    seqs = {}
    for gene in genes:
        seqs[gene] = SeqIO.to_dict(SeqIO.parse('{0}/{1}/{2}.tfa'.format(datpath, strain, gene),
                                     format='fasta'))
    
    # need to make sure all sequences are there for each sample.
    to_drop = []
    for st in df.index:
        for gene in genes:
            g = '{0}_{1}'.format(gene, df[gene][st])
            if g not in seqs[gene]:
                to_drop.append(st)
                continue
    print to_drop
    df = df.drop(to_drop)

    for gene in genes:
        gdmat[gene] = make_gene_dmat(seqs[gene])
    return df, gdmat


def make_st_dmat(df, gdmat):

    n = df.shape[0]
    genes = [col for col in df.columns if ('clonal_complex' not in col)]
    dmat = pd.DataFrame(np.zeros((n,n)), index=df.index, columns=df.index)

    for (i, j) in combinations(df.index, 2):
        for gene in genes:
            g1 = '{0}_{1}'.format(gene, df[gene][i])
            g2 = '{0}_{1}'.format(gene, df[gene][j])
            dmat[i][j] += gdmat[gene][g1][g2]
        dmat[j][i] = dmat[i][j]

    return dmat



# define a nice barcode plotting function
def plot_barcode(bars, plot_dist=True, figsize=(12,8)):
    if plot_dist:
        nrows = 3
    else:
        nrows = 2
        
    fig, ax = plt.subplots(nrows=nrows, ncols=1, sharex=True, figsize=figsize)
    fig.subplots_adjust(hspace=0.05)

    for i in range(2):
        if i == 0:
            s1 = sorted(bars[i], key=lambda tup: tup[1])[::-1]
        if i == 1:
            s1 = sorted(bars[i], key=lambda tup: tup[0])[::-1]
        for bidx, b in enumerate(s1):
            try:
                ax[i].plot([b[0], b[1]], [bidx+1, bidx+1], c=sns.color_palette()[0], lw=1.0)
            except:
                pass
        ax[i].set_yticklabels('')
        ax[i].set_ylim((0, len(s1)+1))
        
    ax[0].set_ylabel('H0', rotation=0, va='center', fontsize=12)
    ax[1].set_ylabel('H1', rotation=0, va='center', fontsize=12)

    births, deaths = get_birth_and_deaths(bars)
    
    if plot_dist:
        try:
            sns.kdeplot(np.array(births), label='births')
            sns.kdeplot(np.array(deaths), label='deaths')
        except:
            pass
        ax[2].set_yticklabels('')
        ax[2].set_xlabel('Distance')
    #     ax[2].set_xlim((0, 600))
        ax[2].legend()
    
    plt.close()
    return fig
