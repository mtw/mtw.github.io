How to interpret SHAPE and chemical probing data for RNA structure decisions
############################################################################

:date: 2026-05-09
:modified: 2026-05-09
:tags: SHAPE; chemical probing; DMS; RNA structure prediction; ViennaRNA
:category: outreach
:slug: How-to-Interpret-SHAPE-and-Chemical-Probing-Data-for-RNA-Structure-Decisions
:author: mtw
:summary: SHAPE, DMS, and related probing experiments can sharpen RNA structure analysis substantially, but only if the data are interpreted as evidence with limits rather than as a direct readout of base pairing.
:title: How to interpret SHAPE and chemical probing data for RNA structure decisions
:description: A practical guide to what SHAPE, DMS, and related probing data can support in RNA structure analysis, and where the interpretation still remains underdetermined.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

SHAPE and related chemical probing assays are often described as if they
directly reveal RNA structure. That is too simple. What these
experiments provide is evidence about local nucleotide behaviour under a
particular condition. Used well, that evidence can change a structural
decision substantially. Used carelessly, it can make a weak structural
story look more certain than it really is.

The first point is that probing data are not a direct list of base
pairs. A reactive nucleotide is not automatically unpaired, and a
protected nucleotide is not automatically locked into one specific
helix. Tertiary contacts, protein binding, ligand occupancy, local
stacking, and conformational mixtures can all alter the signal. That is
why the practical question is usually not "what is the structure", but
"which structural explanations remain plausible once these data are
taken seriously."

This distinction matters most when the computational model is already
near a decision boundary. If several secondary-structure candidates are
close in free energy, probing data can suppress weak alternatives and
make the analysis much more useful. If the real uncertainty lies
elsewhere, for example in kinetics, long-range interactions, or a
protein-bound state, the same data may still be informative, but they
will not rescue an incomplete model.

That is one reason :link-flat:`SHAPE directed RNA folding with the ViennaRNA Package <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>` has remained relevant. The methodological contribution was not merely to
let ViennaRNA ingest SHAPE values. The more important point was that
reactivities can be translated into folding constraints in different
ways, and those choices alter the conclusion. The same probing profile
can push a model harder or more gently depending on how the data are
encoded.

The broader framework is discussed in :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`.
Thermodynamic folding remains useful because it keeps the alternatives
explicit. Probing remains useful because it shifts the balance of those
alternatives toward what the molecule appears to be doing under the
measured condition. The gain comes from combining them without treating
either one as final.

That is also why I would separate two different questions that often get
collapsed. One is whether probing data improves a structure prediction at
all. I discuss that directly in :link-flat:`When SHAPE data actually improves RNA structure prediction <{filename}/blog/2022-10-20-When-SHAPE-Data-Actually-Improves-RNA-Structure-Prediction.rst>`.
The other is what the data allow you to conclude once they exist. That
second question is often the more important one in practice, because it
is the one that determines whether a construct should be synthesized, a
mutational series should be designed, or a biological claim is still too
weak.

DMS, SHAPE-MaP, DMS-MaPseq, and related workflows differ in chemistry
and readout, but the interpretive issue is similar. They are best used
to ask whether a proposed structural explanation remains credible once
measured accessibility enters the argument. They are less useful when
treated as if they convert a difficult inference problem into a solved
picture.

This is especially relevant now that RNA structure predictions are often
combined with machine learning or benchmark-driven workflows. A good
score on a structural benchmark does not remove the need to interpret
probing data carefully, just as probing data do not remove the need to
ask whether the computational model is missing the relevant mechanism.
The real question is still whether the current combination of evidence
is strong enough for the next decision.

In practice, I find probing data most helpful when three things line up:
the structural question is well posed, the experiment was done under a
condition that actually matches that question, and the computational
interpretation stays honest about what remains underdetermined. Once any
of those three slips, the danger is not that the analysis becomes
useless, but that it starts looking more definitive than it is.

That is often the stage where groups benefit from a technical review or
a focused training session. The issue is usually not whether SHAPE or
DMS is useful in principle. It is whether the current design, probing
setup, and computational interpretation are coherent enough to support
the next experimental decision. That is exactly the kind of question I
take up in :link-flat:`design reviews, workshops, and advisory work </services>`.
