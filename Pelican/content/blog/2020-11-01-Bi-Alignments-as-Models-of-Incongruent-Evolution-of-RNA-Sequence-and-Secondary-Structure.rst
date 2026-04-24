Bi-Alignments as Models of Incongruent Evolution of RNA Sequence and Secondary Structure
########################################################################################

:date: 2020-11-01
:modified: 2026-04-24
:tags: non-coding RNA; new method; RNA structure conservation
:category: publications
:slug: Bi-Alignments-as-Models-of-Incongruent-Evolution-of-RNA-Sequence-and-Secondary-Structure
:author: mtw
:summary: This paper introduces bi-alignments, a formal framework for cases where RNA sequence homology and RNA structural homology cannot be captured by the same alignment.
:title: Bi-alignments for incongruent RNA sequence and structure evolution
:description: A methods paper on how to model structured RNAs when conserved sequence and conserved base-pairing patterns have shifted relative to each other.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

This paper addresses a subtle but important problem in comparative RNA analysis. Many RNA alignment methods assume that sequence evolution and secondary-structure evolution are congruent, meaning that homologous nucleotides also remain in corresponding structural roles. That assumption is often useful, and for many classical RNA families it works well enough to support consensus-structure prediction, covariance modeling, and structure-aware multiple alignment. But biology is not always that tidy.

The motivating observation here is that structured RNAs can preserve a recognizable fold even when the exact pairing register has shifted relative to the underlying sequence. In that situation, analogous base pairs are no longer formed by homologous nucleotides, and a single alignment cannot simultaneously do justice to both sequence similarity and structural correspondence. If one insists on aligning the homologous sequence blocks, the structural match degrades. If one instead aligns the analogous stem or loop positions, the sequence alignment begins to look wrong. That is the kind of incongruence this paper sets out to model explicitly.

The methodological contribution is the idea of a bi-alignment. Instead of forcing sequence homology and structural homology into one common alignment, the paper represents them as two coupled alignments: one for sequence, one for structure. A third alignment then relates these two views to each other and accounts for the relative shifts between them. Formally, this turns the problem into a constrained four-way alignment, but the conceptual point is simpler than the formalism may suggest. The method acknowledges that sequence and structure can both be conserved, yet conserved in slightly different coordinate systems.

That framing is useful because it captures evolutionary scenarios that standard consensus models tend to flatten away. One example discussed in the paper is stem sliding, where a stem can effectively move by losing a pair at one end while gaining a new one at the other. The overall hairpin remains recognizable and functionally similar, but the base pairs are no longer anchored to the same homologous nucleotides. A conventional structure-aware alignment tends to overcommit to one notion of correspondence or the other. Bi-alignments provide a way to represent the mismatch between those two notions directly instead of treating it as noise.

The paper is also interesting as a reminder that comparative RNA bioinformatics depends on modeling assumptions that are easy to forget once they become standard. Tools based on the Sankoff idea, consensus folding, or covariance models have been extremely successful, but they are built around the expectation that conserved structure and conserved sequence can be reconciled in one coherent alignment. Bi-alignments are valuable not because that assumption is usually wrong, but because they define what to do in the cases where it is not quite right.

Methodologically, this was a deliberately formal paper. It does not present a flashy biological case study so much as it tries to sharpen the mathematical language for a real comparative-genomics phenomenon. The discussion of miRNA precursors and the exploratory scan through Rfam are there to show that incongruent evolution is not just a pathological corner case. Structured RNAs can drift in ways that preserve shape better than position, and once that happens, the distinction between homology and structural analogy becomes computationally relevant.

Seen from the broader arc of RNA bioinformatics, this work fits into a longer effort to make our models better reflect how RNAs actually evolve. Some papers focus on thermodynamics, some on kinetics, some on experimental constraints, and others on machine learning. This one is about representation: what exactly are we aligning when we compare two structured RNAs? That is a foundational question, and although the paper is mathematically flavored, it speaks to a very biological issue.

For readers interested in RNA methods, the value of the paper is therefore twofold. First, it introduces a concrete framework for handling sequence-structure incongruence. Second, it sharpens the intuition that "RNA structure conservation" is not always equivalent to "the same nucleotides occupy the same structural roles". That distinction matters whenever we try to infer evolutionary relationships from structured non-coding RNAs, especially in families where local motifs can shift while the overall fold remains recognizable.

.. frame:: Abstract

  RNA molecules may be subject to independent selection pressures on sequence and structure. This can preserve structural features without maintaining their exact positions on the conserved sequence, so that analogous base pairs are no longer formed by homologous nucleotides. We model this phenomenon with bi-alignments, defined as a pair of alignments, one for sequence homology and one for structural homology, together with an alignment of the two that captures relative shifts between conserved sequence and conserved structure. In this way, bi-alignments provide a formal model for incongruent evolution of RNA sequence and secondary structure.


Citation
========

  | :link-flat-strong:`Bi-Alignments as Models of Incongruent Evolution of RNA Sequence and Secondary Structure <https://doi.org/10.1007/978-3-030-63061-4_15>`
  | Maria Waldl, Sebastian Will, :ul:`Michael T. Wolfinger`, Ivo L. Hofacker, Peter F. Stadler
  | In *Computational Intelligence Methods for Bioinformatics and Biostatistics*, pp159-170. Springer International Publishing (2020) | :doi:`doi:10.1007/978-3-030-63061-4_15 <https://doi.org/10.1007/978-3-030-63061-4_15>` | :link-flat:`Preprint PDF <{static}/files/papers/Waldl-2020__PREPRINT.pdf>`


See Also
========

  | :link-flat-strong:`Predicting RNA Structures from Sequence and Probing Data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`
  | Ronny Lorenz, :ul:`Michael T. Wolfinger`, Andrea Tanzer, Ivo L. Hofacker
  | *Methods* 103:86-98 (2016) | :doi:`doi:10.1016/j.ymeth.2016.04.004 <https://doi.org/10.1016/j.ymeth.2016.04.004>` | :link-flat:`PDF <{static}/files/papers/Lorenz-2016.pdf>`

  | :link-flat-strong:`Caveats to Deep Learning Approaches to RNA Secondary Structure Prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`
  | Christoph Flamm, Julia Wielach, :ul:`Michael T. Wolfinger`, Stefan Badelt, Ronny Lorenz, Ivo L. Hofacker
  | *Front. Bioinform.* 2:835422 (2022) | :doi:`doi:10.3389/fbinf.2022.835422 <https://doi.org/10.3389/fbinf.2022.835422>` | :link-flat:`PDF <{static}/files/papers/Flamm-2022.pdf>`
