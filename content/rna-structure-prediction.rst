RNA structure prediction
########################
:slug: rna-structure-prediction
:title: RNA structure prediction with ViennaRNA: tutorials and background | Michael T. Wolfinger
:summary: The tutorials on this site on RNA secondary structure prediction with the ViennaRNA Package, in reading order: reading RNAfold output, folding with SHAPE and chemical probing data, what deep learning predictors learn, and the background papers.
:description: Tutorials on RNA secondary structure prediction with ViennaRNA in reading order: RNAfold output, SHAPE and probing data, deep learning predictors, glossary.
:hero_eyebrow: Guides
:hero_title: RNA structure prediction with ViennaRNA
:date: 2026-10-31
:modified: 2026-10-31

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

This page collects the posts on this site that explain how to predict the secondary
structure of an RNA with the :link-flat:`ViennaRNA Package <https://www.tbi.univie.ac.at/RNA/>`
and how far such a prediction can be trusted, in the order in which I would read them.
They are written for researchers who use structure predictions in their own work, i.e.
for experimentalists and computational biologists alike, and each tutorial works through
a complete example with all commands included, so that the results can be reproduced on
any computer with ViennaRNA installed.

Tutorials
=========

1. :link-flat-strong:`RNAfold tutorial: MFE, pair probabilities and ensemble output <{filename}/blog/2026-10-28-rnafold-in-practice.rst>`.
   What RNAfold writes to the terminal and to its output files, i.e. the minimum free
   energy (MFE) structure, the pair probabilities and the dot plot, the centroid and
   MEA structures, and the suboptimal structures from RNAsubopt. The example is yeast
   tRNA-Phe, and the question throughout is how to tell whether the MFE structure is a
   robust prediction or one of many that the sequence could form.
2. :link-flat-strong:`SHAPE and chemical probing tutorial: folding with reactivities in RNAfold <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>`.
   How SHAPE reactivities go into RNAfold, the input format, what the three methods in
   ViennaRNA (Deigan, Zarringhalam and Washietl) do with the data, and what probing data
   change in a prediction and what they do not. Same tRNA, so the two tutorials can be
   read side by side.

Background
==========

- :link-flat-strong:`AI for RNA structure prediction: what deep learning models learn <{filename}/blog/2026-10-28-deep-learning-rna-secondary-structure-prediction.rst>`.
  What neural networks trained on known structures compute, why the usual benchmarks
  overstate their accuracy, what a test on synthetic data revealed about their outputs,
  and what has changed since 2022.
- :link-flat-strong:`Caveats to deep learning approaches to RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`
  (Flamm et al., *Front Bioinform* 2022). The paper behind the explainer, with the
  synthetic data experiments.
- :link-flat-strong:`Predicting RNA secondary structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`
  (Lorenz et al., *Methods* 2016). The methods paper for the probing data support in
  ViennaRNA that the SHAPE tutorial uses.
- :link-flat-strong:`SHAPE directed RNA folding <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>`
  (Lorenz et al., *Bioinformatics* 2016). The comparison of the three methods on a set of
  RNAs with known structures.

Reference
=========

The :link-flat-strong:`glossary <{filename}/glossary.rst>` defines the terms used in the
tutorials, e.g. :link-flat:`MFE <{filename}/glossary.rst#mfe>`,
:link-flat:`partition function <{filename}/glossary.rst#partition-function>`,
:link-flat:`dot-bracket notation <{filename}/glossary.rst#dot-bracket>` and
:link-flat:`soft constraints <{filename}/glossary.rst#soft-constraints>`. Every entry has
its own address and can be linked directly.

Questions and further tutorials
===============================

Each tutorial ends with a short form for questions that the text left open; these
questions decide what gets written next. Further tutorials are in preparation on reading
dot plots and dot-bracket strings, on accessibility with RNAplfold, on consensus
structures from alignments with RNAalifold, and on comparing predicted structures. A
series of hands-on :link-flat:`ViennaRNA training modules and workshops <{filename}/blog/2026-10-28-viennarna-training-workshops-2027.rst>`
is planned for 2027.

Questions about RNA structure prediction, or about working together?
:link-flat-strong:`Write to me <{filename}/contact.rst#write>`.
