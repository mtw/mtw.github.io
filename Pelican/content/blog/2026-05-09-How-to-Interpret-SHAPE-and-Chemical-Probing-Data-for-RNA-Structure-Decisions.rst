How to interpret SHAPE and chemical probing data for RNA structure decisions
############################################################################

:status: hidden
:date: 2026-05-09
:modified: 2026-05-09
:tags: SHAPE; RNA structure prediction; ViennaRNA
:category: outreach
:slug: How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions
:author: mtw
:summary: SHAPE, DMS, and related probing experiments can sharpen RNA structure analysis substantially, but only if the data are interpreted as evidence with limits rather than as a direct readout of base pairing.
:title: How to interpret SHAPE and chemical probing data for RNA structure decisions
:description: A practical guide to where SHAPE, DMS, and related probing techniques can support RNA structure analysis, and where the interpretation still remains underdetermined.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

SHAPE and related chemical probing assays are often described as if they
directly reveal RNA structure. That is too simple. These experiments
measure nucleotide flexibility under a defined condition, and the
structural interpretation remains indirect.

A reactive nucleotide is not automatically unpaired, and an unreactive
nucleotide is not automatically base-paired in a particular helix.
Tertiary contacts, protein binding, ligand occupancy, local stacking,
and co-existing conformations can all affect the signal. The relevant
question is therefore which structural interpretations remain plausible
once the probing data are taken into account.

This distinction becomes most important when the computational model is
ambiguous. If sequence-based folding yields several candidate structures
within a narrow free-energy range, probing data can suppress weak
alternatives and sharpen the analysis substantially. If the relevant
uncertainty lies elsewhere, for example in folding kinetics, long-range
interactions, or a protein-bound state, the same data may still be
informative, but they will not repair an incomplete model.


:link-flat:`SHAPE directed RNA folding with the ViennaRNA Package <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>`
has remained relevant for exactly that reason. Reactivities can be
translated into folding constraints in different ways, and the choice
affects the result.

The same probing profile can influence a structure prediction more
strongly or more weakly, depending on how the data are processed and
which parameters are used. The Deigan et al. method is probably the most
widely used approach for converting probing data into pseudo-energies,
but its performance depends on the chosen parameters. Those parameters
are not universal.

We discussed this broader framework in :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`.
Thermodynamic RNA folding keeps the alternative structures explicit.
Probing data can then shift the balance between those alternatives
toward what the molecule appears to do under the measured condition.

Two questions are often mixed together. One is whether probing data
improve a structure prediction at all. I discuss that question in
:link-flat:`When SHAPE data actually improves RNA structure prediction <{filename}/blog/2022-10-20-When-SHAPE-Data-Actually-Improves-RNA-Structure-Prediction.rst>`.
The other is what those data allow one to conclude. The second question
is often the more important one because it determines how far the
analysis can be taken.

DMS, SHAPE-MaP, DMS-MaPseq, and related workflows differ in chemistry
and readout, but the interpretive issue is similar. They are most useful
when they are used to test whether a proposed structural explanation
remains credible once measured nucleotide flexibility is taken into
account.

This becomes particularly relevant when RNA structure predictions are
combined with automated pipelines, large benchmarks, and more complex
prediction workflows. A good score on a benchmark does not remove the
need to interpret probing data carefully. Conversely, probing data do
not remove the need to ask whether the computational model misses the
relevant mechanism.

Probing data are most helpful when the structural question is well
posed, the experiment matches that question, and the computational
interpretation remains conservative about what is still unresolved.
Otherwise the analysis can start to look more definitive than it is.

At that stage, groups often benefit from a technical review or a focused
training session. The issue is usually whether the current design,
probing setup, and computational interpretation are coherent enough to
support the next experimental decision. That is the kind of question I
take up in :link-flat:`design reviews, workshops, and advisory work </services>`.
