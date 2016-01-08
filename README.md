## Statistical Topology with Applications in Reticulate Evolution
## Kevin Emmett
## PhD Thesis

### Notes

Things to cover...

* genomics
* population genetics
* evolution
* horizontal gene transfer
* phylogenetic networks

* topology: properties under continuous transformation
* algebraic topology
* topological data analysis
* persistent homology

* statistics
* dimensionality reudction: PCA, MDS

* statistics for PH [many]
* random complexes and PH [Kahle etc]

### Introduction

* Open with Darwin's Tree of Life
* Recapitulate the Doolittle story and run through some history.
* Darwin -> Zuckerkandl/Pauling -> Woese -> Modern Genomics
* Doolittle; evidence for nonvertical evolution; new models

* Propose topological data analysis as a possible framework
* Describe the basic idea behind TDA
* Give a simple picture for how TDA is applied to sequence data
* Thesis Organization

### Background

* Major section: survey of evolutionary biology, population genetics and phylogenetics.
* Sequence alignment. Coalescent simulation.
* Discuss Darwin, Zuckerkandl and Pauling, Woese, Doolittle.
* LUCA. Universal Tree of Life. Powerful image!
* But evidence that evolution is not as linear as Darwin thought.
* Discuss the coalescent with recombination. Biological mechanisms of recombination and horizontal gene transfer
* Discuss phylogenetics and phylogenetic networks.
* Detailed information can be put in later sections
* Infinite sites assumption


* Major section: Applied topology
* Discuss group theory, equivalence classes, homology.
* Mapper
* Persistent Homology
* Discuss developments in statistical TDA.

* M

### Theory Section

* Random Processes that Generate Distributions on the Barcode Diagram
* Quantifying Homology 
* Statistical topological data analysis
* Statistical learning
* Recombination Complexes

### Applications: Viruses and Prokaryotes

* Bacteriophage
* Influenza
* Tree of Life

### Applications: Humans

### Books

#### Population Genetics

* Gene Genealogies, Variation and Evolution [Hein, Schierup, Wiuf]
* Coalescent Theory [Wakeley]
* Phylogenetics [Felsenstein]
* Phylogenetic Networks [Huson]
* ReCombinatorics [Gusfield]
* Basic Phylogenetic Combinatorics [Dress, Huber, Koolen, Moulton, Spillner]

#### Topological Data Analysis

* Topology [Munkres]
* Algebraic Topology [Hatcher]
* Geometry, Topology and Physics [Nakahara]
* Elementary Applied Topology [Ghrist]
* Topology for Computing [Zomorodian]
* Computational Topology: An Introduction [Edelsbrunner, Harer]

## Précis

In the theory* section, we describe two approaches for extracting useful information from topological constructions.

Stochastic Process Inference.

In the first chapter, we show how the information in the persistence diagram can be used in parameteric models for statistical inference. We will illustrate this with a number of simple examples, and then demonstrate statistical inference in a more complex model drawn from population genetics.

We illustrate our approach with an initial application to inference in a Gaussian Random Field model.
This model will be used in later chapters when applied to real data. This approach of making statistical statements about the persistence diagram differs from that of previous approaches for statistical information

## Other

Innovation. Topological data analysis is a new mathematical framework to capture global structural properties of large data sets. This framework can capture properties that are invisible to traditional statistical techniques, as shown by its ability, for example, to identify a previously uncharacterized subgroup of breast tumors with a unique survival profile20. Persistent homology, a type of topological data analysis, has recently been proposed as a multi-purpose framework for analyzing many types of data21,22, but remains untapped by biologists. Our group is pioneering the use of this framework to analyze genomic sequence data. We have found the approach of persistent homology to be uniquely suited for succinctly characterizing these large, high-dimensional datasets6. We therefore believe that as the density of genomic data continues to explode, persistent homology will mature into a useful framework for extracting and understanding nontrivial structure present in the data.

The philosophy of analyzing evolution with persistent homology differs from that of established phylogenetic methods. In the field of phylogenetics, the objects of interest are trees that describe patterns of uniparental ancestry. The null model is that of no horizontal evolution. A specific reticulate event can be introduced as a correction to the tree by addition of a reticulate branch connecting two nodes23. Reticulate surfaces involving genetic exchange among three or more parental strains are never studied. In contrast, the objects of interest in persistent homology are topological spaces that describe general relationships, which may include complex, multi-parental reticulate events. Horizontal evolution is an intrinsic feature of this framework, rather than a deviation from a null model. Persistent homology therefore provides a fresh depiction of evolutionary relationships that challenges the dominant tree-centered paradigm. The utility of this new approach became evident to us when investigating the recent H7N9 influenza outbreak, for which it could identify the emerging reassortant.

This proposal seeks to develop new methods in persistent homology, motivated by the specific needs of evolutionary biology. While topology traditionally focuses on immutable objects, evolution is a dynamic process. We are not content merely to describe genomic data, but seek to explain the evolutionary mechanisms that gave rise to it. To this end, we develop (Aim 1.1) techniques for statistical inference using persistent homology-based methods. In Aim 1.3, we will improve on these techniques by explicitly incorporating time as a dimension in the persistent homology calculations; this goal will require substantial theoretical advance in computational topology7,8.

----------------------------------

