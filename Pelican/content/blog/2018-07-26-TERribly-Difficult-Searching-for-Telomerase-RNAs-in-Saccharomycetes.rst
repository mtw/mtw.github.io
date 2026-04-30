TERribly Difficult: Searching for Telomerase RNAs in Saccharomycetes
####################################################################

:date: 2018-07-26
:modified: 2022-10-14
:tags: non-coding RNA
:category: publications
:slug: TERribly-Difficult-Searching-for-Telomerase-RNAs-in-Saccharomycetes
:author: mtw
:summary: Telomerase RNAs are difficult to detect by homology search alone; this study reports an annotation strategy for Saccharomycetaceae using ViennaRNA-based methods.
:title: Searching for Telomerase RNAs in Saccharomycetes is TERribly difficult
:description: Finding and annotating Telomerase RNAs in phylogenetically related subgroups of yeasts is TERribly difficult

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Telomerase RNA is a frustrating target for computational annotation. Functionally, it is essential: without it, telomerase cannot maintain chromosome ends. But unlike many better-behaved non-coding RNAs, telomerase RNAs often evolve rapidly in primary sequence, vary strongly in length, and tolerate substantial structural reorganization. That makes them precisely the kind of molecule that defeats simple homology search.

This paper focuses on that problem in Saccharomycete yeasts. The central question is not whether telomerase RNAs exist in these genomes, but how one can find them when neither sequence conservation nor a single fixed structural model is strong enough to carry the search on its own. The title is not rhetorical. The paper is genuinely about why this annotation problem is difficult, and what a realistic computational strategy looks like when the target family is both fast-evolving and structurally plastic.

The study combines multiple approaches rather than relying on one decisive signal. Sequence similarity, comparative context, and ViennaRNA-supported structural reasoning are used together to build and refine search models across subgroups. That point is important because it captures a recurring lesson in non-coding RNA bioinformatics: when the biology is heterogeneous, the right answer is often not a more aggressive version of a single method, but a carefully staged combination of several weak but complementary signals.

Even with that broader strategy, the outcome is only partially complete, and that is one of the strengths of the paper. Instead of overstating success, it documents the limits of the current search space. The authors identify 27 new telomerase RNAs, but only within the subgroup Saccharomycetaceae, and even there different phylogenetic subgroups require different search models. More distant branches of Saccharomycotina remain unresolved. In other words, the paper is as much about the boundaries of current annotation methodology as it is about the annotations themselves.

That honesty makes the paper more useful than a narrower success story would have been. Telomerase RNAs are a classic example of a family where absence of annotation is not evidence of absence. They are simply hard to find. By spelling out which features help, which ones fail, and where the search breaks down, the paper becomes a methodological reference for anyone working on difficult structured RNAs that have retained function while drifting in sequence and architecture.

The broader significance is easy to miss if one focuses only on yeast telomeres. This is really a paper about ncRNA discoverability. Many computational pipelines work best on families with strong covariation support, stable consensus motifs, or relatively conserved lengths. Telomerase RNA violates those expectations. As a result, the paper becomes a useful case study in how to adapt comparative RNA annotation strategies when the target family sits at the edge of what standard homology models can capture.

The same underlying issue appears repeatedly across RNA biology: biologically important RNAs are not always easy to recognize from sequence alone, and structure-aware comparative methods become essential precisely where simple pipelines fail. Telomerase RNA in yeasts is one of the clearest examples of that problem.

.. frame:: Abstract

  The telomerase RNA in yeasts is large, usually >1000 nt, and contains functional elements that have been extensively studied experimentally in several disparate species. Nevertheless, they are very difficult to detect by homology-based methods and so far have escaped annotation in the majority of the genomes of Saccharomycotina. This is a consequence of sequences that evolve rapidly at nucleotide level, are subject to large variations in size, and are highly plastic with respect to their secondary structures. Here, we report on a survey that was aimed at closing this gap in RNA annotation. Despite considerable efforts and the combination of a variety of different methods, it was only partially successful. While 27 new telomerase RNAs were identified, we had to restrict our efforts to the subgroup Saccharomycetacea because even this narrow subgroup was diverse enough to require different search models for different phylogenetic subgroups. More distant branches of the Saccharomycotina remain without annotated telomerase RNA.

Citation
========

  | :link-flat-strong:`TERribly Difficult: Searching for Telomerase RNAs in Saccharomycetes <https://doi.org/10.3390/genes9080372>`
  | Maria Waldl, Bernhard C. Thiel, Roman Ochsenreiter, Alexander Holzenleiter, João Victor de Araujo Oliveira, Maria Emília M.T. Walter, Michael T. Wolfinger, Peter F. Stadler
  | *Genes* 9(8),372 (2018) | :doi:`doi: 10.3390/genes9080372 <https://doi.org/10.3390/genes9080372>` | :link-flat:`PDF <{static}/files/papers/Waldl-2018.pdf>`
