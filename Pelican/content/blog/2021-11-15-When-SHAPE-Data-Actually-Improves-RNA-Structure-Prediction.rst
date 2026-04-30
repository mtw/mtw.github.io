When SHAPE data actually improves RNA structure prediction
##########################################################

:date: 2021-11-15
:modified: 2026-04-30
:tags: SHAPE; RNA structure prediction; ViennaRNA
:category: outreach
:slug: When-SHAPE-Data-Actually-Improves-RNA-Structure-Prediction
:author: mtw
:summary: SHAPE data can improve RNA structure prediction substantially, but only when the experiment, the model, and the biological question line up in the right way.
:title: When SHAPE data actually improves RNA structure prediction
:description: A practical guide to when SHAPE probing strengthens RNA structure prediction, and where it still leaves uncertainty.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

People often talk about SHAPE-guided folding as if adding experimental data automatically solves RNA structure prediction. It does not. What SHAPE does provide is a strong extra layer of evidence about local nucleotide flexibility. In the right setting, that is enough to disambiguate near-optimal structures and to make the prediction much more useful. In the wrong setting, it can still leave the hard part unresolved.

The first question is whether the biological problem is actually one of local secondary structure. If the main uncertainty lies in competing helices within a compact structural domain, SHAPE data can be extremely informative. If the molecule is dominated by tertiary contacts, protein binding, ligand effects, or changing cellular context, the reactivities may still be helpful, but they will not rescue a model that is missing the relevant physics.

The second question is whether the probing data are being integrated through a sensible model. This is where :link-flat:`SHAPE directed RNA folding <{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst>` still matters. The central point of that paper is not simply that ViennaRNA can read SHAPE values. It is that there are different ways to translate reactivities into folding constraints, and those choices affect the result. Soft constraints and pseudo-energies work precisely because they let the thermodynamic model and the experiment inform one another instead of pretending that either one is perfect on its own.

That broader logic is laid out in :link-flat:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`. Thermodynamic folding remains useful because it gives an explicit model of structural alternatives and energetic tradeoffs. Probing data remain useful because they move the prediction toward what the molecule is doing under the measured condition. The practical gain comes from the combination.

Where people still get misled is in the interpretation of success. A cleaner fold on a figure is not the same as a solved biological question. SHAPE can improve ranking among secondary-structure candidates. It can sharpen ensemble interpretation. It can reveal where a sequence-only model is systematically wrong. It usually cannot tell you, on its own, whether a regulatory switch depends on kinetics, protein occupancy, or an alternative conformation outside the measured state.

That point becomes even more important now that AI models are routinely evaluated against RNA structure benchmarks. The critique in :link-flat:`Caveats to deep learning approaches to RNA secondary structure prediction <{filename}/blog/2021-12-16-Caveats-to-deep-learning-approaches-to-RNA-secondary-structure-prediction.rst>` is relevant here. Better benchmark scores do not remove the need for careful inference. If a model generalizes poorly, or if the training data do not reflect the biological regime of interest, experimental constraints can still be more informative than a confident-looking prediction.

In practice, SHAPE helps most when three things line up. The construct has a well-defined structural question. The experiment is done under a condition that actually matches that question. The computational interpretation respects the fact that the data are informative but incomplete. That is a narrower claim than the usual marketing language around “data-driven structure prediction,” but it is closer to how good results are actually obtained.

This is also where many teams hit a decision point. Sometimes the issue is not whether SHAPE is useful in principle, but whether the current construct, probing design, and analysis setup are coherent enough to justify the next experiment. That is often the stage where an external technical review or a focused training session becomes useful, especially if the group is deciding between a quick sequence-only analysis and a more serious structure-guided workflow. My :link-flat:`services page <{filename}/services.rst>` outlines the formats I use for that kind of design review and workshop support.
