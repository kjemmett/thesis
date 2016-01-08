### Topological Data Analysis

Note: We want to rearrange this section so it flows better.
To that end we will do the following.
Move the more preliminary mathematical definitions into an appendix.
Use the background section to work through the full TDA pipeline using a simple example.
Then work through a simple example using sequence-like data.

One subsection on Persistent Homology.
One subsection on Mapper.

-----------------------------------------------------------------------

(How about we move all of this into the appendix section?)

Topology is the branch of mathematics that aims to characterize objects and spaces up to deformations.
For example, if we take a tree, as in the previous section, and change the lengths of the branches, the tree remains a tree. 
Likewise, if we take a circle, and compress it along one axis into an ellipse, we recognize that while some properties of the shape have changed, such as skew, others have not, such as the fact that the ellipse still encloses a single hole.
Topology is concerned with these holes.

How can we address if two spaces have the same topology?

* Footnote: In the tree literature, a distinction between different tree topologies is drawn. This refers to different possible branching patterns on the same set of leaves. While this is an appropriate usage of the term topology, it is not the usage we pursue.

---------------------------------------------------------------------------

Topology is the branch of mathematics that aims to characterize objects and spaces up to deformations.
Algebraic topology formalizes our qualitative notions of shape into sets of numerical invariants that can be manipulated using tools from abstract algebra.
Topological data analysis (TDA) is an emerging framework that has been developed over the last 15 yhears to provide algorithms for computing topological invariants from finite data.
TDA encompasses numerous efforts and can now be considered a branch of applied mathematics in its own right.
It has emerged from substantial interdisciplinary effort between mathematicians, computer scientists, and domain specific scientists.

This thesis uses methods from TDA to study the biological problems that were outlined in the previous section.
Our two main methods will be \emph{persistent homology} and \emph{mapper}.



In this section, we provide an overview of these methods from the perspective of an end-user.
We think of each method as a pipeline that takes data as input, and outputs some summary information about the topology of the input.
While technical terms will be defined as they are introduced, our primary aim will be developing a working understanding of the main aspects of each method as they are used in practice, and not on a rigorous mathematical formalism.

Need only an understanding of homology.
A more thorough reference for the mathematical ideas underpinning these methods can be found in Appendix XX.
Development of the ideas leading to homology in Appendix XX.

\subsection{Peristent Homology}

In this section we introduce persistent homology, a way of summarizing the topological properties of point cloud data.

Persistent homology summarizes the topological properties of point cloud data.
Homology refers to quantitative notions of shape.
The adjective \emph{persistent} indicates that we analyze homology over multiple scales and provide an assessment of which invariants last over longer scales.


Shape information is indexed by dimension.

\subsection{Mapper}

The Mapper algorithm was developed by Gurjeet Singh in \cite{Singh:2007ve}.

----------------------------------------------------------------------------------------------


Topology is the branch of mathematics that aims to characterize spaces up deformation.
If we start
Algebraic topology assigns algebraic quantities to these invariants.

Topological Data Analysis (TDA) refers to a set of tools that have been developed over the past decade aimed at computing topological invariants from data.
These tools have been developed extensively through collaborations between mathematicians and computer scientists.


The two main computational tools which we will employ in this thesis are \emph{peristent homology} and \emph{mapper}.
In this section we describe both of these tools.
We take a pipeline approach, where the input to each method is the data, and the output is some topological summary of the data.
Each step of the pipline involves some type of transformation of the data.
We describe each step of the pipeline in turn.


