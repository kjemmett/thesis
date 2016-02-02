## Background

### Biology

btw papers
----------
1. icml paper [FA]
2. warsaw paper [FA]
3. bict paper 1 [FA]
4. bict paper 2 [FA]
5. microbes article [FA]
6. ebola paper [FA]
7. mendelian paper
8. (ip) human recomb paper
9. (ip) flu paper [cFA]
10. stochseq paper [FA]
11. biofilm paper
12. dream paper

[anything else?]


-----------------------------------------------------

(infinite sites model and binary sequences)

In the majority of our cases, we will work under the so called \emph{infinite sites model}.
The model assumes no double mutations occur.
The justification for the model is that because the probability of a double mutation goes as $1/L^2$ where $L$ is the length of the genome, double mutations will be extremely rare over time scales we are interested in.
A consequence of this model is that we can safely assume binary sequence data, where `0' implies unmutated and `1' implies mutated.
If two organisms share a mutation, we know they shared a common ancestor with that mutation at some point in the past.
While this may seem like a strong assumption, it holds quite well for 

------------------------------------------------------

(Where is this going?)
We give a concrete example on four leaves.
We consider only segregating sites.
Consider the set of four sequences S = {00000, 11000, 10110, 10101}.
One possible unrooted tree topology representing the data is shown in Figure XX.

A few things are worth noting in this example.
One, each segregating site is associated with an edge in the 


------------------------------------------------------------------


## MAPPER NOTES

# NEW NOTES:

The field of exploratory data analysis is vast.
\emph{Mapper} is an algorithm for the representation of high-dimensional datasets as a network.
The \emph{Mapper} algorithm belongs to the class of algorithms designed for \emph{condensed representation} and \emph{exploratory data analysis}.

In contrast to persistent homology, which summarizes high-dimensional data 

Mapper allows for qualitative analysis of high-dimensional data through direct visualization.
In this sense it belongs within the larger category of dimensionality reduction techniques such as multidimensional scaling (MDS) and their nonlinear extensions, including Isomap and t-SNE.
However, mapper has certain advantages over these approaches, as we will see.

Taking an explicitly topological approach has three key advantages: coordinate freeness, invariance to deformation, and compressed representation of shape.

(1) Coordinate free
(2) Invariance to deformation - robustness to noise
(3) Compressed representation - ability to handle large datasets.

Compressed representation: if our dataset is large, a network analysis may be difficult to .
Mapper allows us to control the resolution at which we explore the data.
* multiresolution


In this way, mapper is well suited for interactive analysis and visualization.

The \emph{Mapper} algorithm was developed by Gurjeet Singh and Gunnar Carlsson in \cite{Singh:2007ve}.

High-dimensional data to graph/network representation.


Mapper was first applied to problems in RNA folding in \cite{Bowman:2008esa} and breast cancer subtype identification in \cite{Nicolau:2011}.
One of the earliest applications of mapper can be found in \cite{Nicolau:2011}, wher


In our work we use the commercial implementation of Mapper developed by Ayasdi \cite{AyasdiIris:2015}.
An open-source implementation of Mapper is available in the Python Mapper package \cite{Mullner:2013}.


Mapper: a mathematical tool that builds a simple geometric representation of data along preassigned guiding functions called filters. Mapper provides both a method for mathematical data analysis and a visualization tool; the filter functions introduced through Mapper define a framework for supervised analysis. Approximates a collapse of the data into a simple, low dimensional shape, and the filter functions act as guides along which the collapse is done


Mapper is coordinate free and depends only on the similarity of points as measured by the distance function.
Further exposition can be found in \cite{Lum:2013cz}.



Steps:
(1) Project using filter function.
(2) Create overlapping bins
(3) Cluster in the projected space.
(3) Connect pairs of bins with shared points


# Older Notes

Condensed Representations.
Exploratory data analysis seeks to represent high-dimensional datasets in .

\begin{figure}
\begin{tikzpicture}[node/.style={minimum height=.8cm,minimum width=2cm,draw}]
\draw (0,0) node[node, align=center] (dr) {Dimensionality\\Reduction};
\draw (3,1) node[node] (linear) {Linear};
\draw (3,-1) node[node] (nonlinear) {Nonlinear};
\draw (6,1) node[node] (pca) {PCA};
\draw (6, -.5) node[node] (geometry) {Geometry};
\draw (6, -1.5) node[node] (topology) {Topology};
\draw (9, -.5) node[node,align=left] (manifold_learning) {Manifold\\Learning};
\draw (9, -1.5) node[node] (mapper) {Mapper};
\draw (12, -.5) node[node,align=center] (mds) {MDS\\PCA\\Isomap};


\myline{dr}{linear};
\myline{dr}{nonlinear};
\draw[-latex] (linear) -- (pca);
\myline{nonlinear}{geometry};
\myline{nonlinear}{topology};
\draw[-latex] (topology) -- (mapper);
\draw[-latex] (geometry) -- (manifold_learning);
\draw[-latex] (manifold_learning) -- (mds);

\end{tikzpicture}
\caption[Dimensionality Reduction for EDA]{Dimensionality Reduction for EDA}
\label{background:fig:eda}
\end{figure}

Mapper algorithm was first developed in \cite{Singh:2007ve}.
Mapper is coordinate free and depends onnly on the similarity of points as measured by the distance function.
Further exposition can be found in \cite{Lum:2013cz}.
Used in biology example in \cite{Nicolau:2011} top classify breast cancer subtypes.
In our work we use the commercial Mapper implementation Ayasdi \cite{AyasdiIris:2015}.
An open-source implementation of the Mapper algorithm is available in the Python Mapper package \cite{Mullner:2013}.

Steps:
(1) Project using filter function.
(2) Create overlapping bins
(3) Cluster in the projected space.
(3) Connect pairs of bins with shared points
