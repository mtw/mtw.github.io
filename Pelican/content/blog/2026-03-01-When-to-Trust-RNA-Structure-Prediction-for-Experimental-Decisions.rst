When to trust RNA structure prediction for experimental decisions
#################################################################

:date: 2026-03-01
:modified: 2026-05-01
:tags: RNA structure prediction; ViennaRNA; SHAPE; AI; RNA design
:category: outreach
:slug: When-to-trust-RNA-structure-prediction-for-experimental-decisions
:author: mtw
:summary: RNA structure prediction is most useful when it narrows the experimental space, exposes uncertainty clearly, and helps determine when the available structural evidence is sufficient for the next step.
:title: When to trust RNA structure prediction for experimental decisions
:description: A practical guide to when RNA secondary structure prediction is reliable enough to support experimental choices, and when additional probing, comparative evidence, or more careful modeling is needed.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

RNA structure prediction is the natural starting point for mechanistic
work on RNA, because it is a cheap and efficient way to obtain an
explicit structural hypothesis. For experimental work, the relevant
question is whether the current prediction is already sufficient to
explain the mechanism at issue, or whether the interpretation still
depends on additional constraints. The usual performance measures are
informative, but they do not answer that question directly.

Classical thermodynamic prediction is often enough to establish a useful
mechanistic picture. Compact RNAs, shorter motifs, and systems with one
dominant conformational regime can often be analysed productively in
that framework. Even then, the ensemble is usually more informative
than a single minimum free energy structure, because the mechanistically
relevant issue is often whether a helix, junction, or competing
alternative is stable enough to matter.

The situation changes once the mechanism depends strongly on context.
Ligand binding, protein occupancy, co-transcriptional folding,
long-range interactions, and metastable states are difficult to
represent in a static secondary structure model. :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>` is still an important reference precisely because it does not obscure that
point. Thermodynamic folding gains substantially from experimental
constraints, but the additional data do not eliminate the need for
interpretation.

The same applies to probing-guided analyses. :link-flat:`SHAPE directed RNA folding with the ViennaRNA Package <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>` is relevant here because SHAPE reactivities do not yield a
secondary structure directly. They alter the set of structures that
remain plausible once nucleotide flexibility has been taken into
account. When sequence-based folding and probing data support the same
structural features, the resulting inference becomes much stronger.

The current machine-learning literature changes the tooling but not the
underlying problem. As discussed in :link-flat:`Caveats in deep learning for RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>`, strong benchmark performance is not equivalent to robust
structural inference. Sequence-only neural models therefore require the
same caution as any other predictor when the sequence class is unusual,
when the mechanism depends on context, or when the experimental cost of
an incorrect inference is high.

What matters experimentally is whether the prediction explains the
relevant structural feature in a stable way, whether competing
structures remain close enough in free energy to alter the
interpretation, and whether independent evidence supports the same
conclusion. The required level of support depends on cost. A partly
resolved prediction may be acceptable before a cheap follow-up
experiment. The same level of uncertainty is often inadequate before a
costly design cycle or a stronger mechanistic claim.

This is also the point at which kinetics enters. A construct may look
convincing at equilibrium and still fail once the folding pathway
becomes mechanistically relevant. I discuss that in more detail in
:link-flat:`Why kinetic folding matters in RNA design <{filename}/blog/2025-01-20-Why-Kinetic-Folding-Matters-in-RNA-Design.rst>`. Some experimental decisions depend on features that a single
static structure cannot represent adequately.

The practical difficulty is usually not the software itself. It is the
judgment of whether a given prediction already explains the mechanism
well enough, or whether the interpretation still depends on additional
evidence. That is the type of question I address in
:link-flat:`design reviews and advisory work </services>`.
