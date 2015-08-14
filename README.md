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

* Recapitulate the Doolittle story and run through some history.
* Darwin -> Zuckerkandl/Pauling -> Woese -> Modern Genomics
* Doolittle
* Some evidence for nonvertical evolution.
* Propose topological data analysis as a possible framework
* Describe the basic idea behind TDA

### Background

* Major section: survey of evolutionaru biology, population genetics and phylogenetics.
* Discuss Darwin, Zuckerkandl and Pauling, Woese, Doolittle.
* LUCA. Universal Tree of Life. Powerful image!
* But evidence that evolution is not as linear as Darwin thought.
* Discuss the coalescent with recombination. Biological mechanisms of recombination and horizontal gene transfer
* Discuss phylogenetics and phylogenetic networks.
* Detailed information can be put in later sections
* Infinite sites assumption

* Major section: Applied topology
* Discuss group theory, equivalence classes, homology.
* Lead up to persistent homology.
* Discuss developments in statistical TDA.

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
