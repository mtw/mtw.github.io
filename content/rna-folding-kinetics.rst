RNA folding kinetics and energy landscapes
##########################################
:slug: rna-folding-kinetics
:title: RNA folding kinetics and energy landscapes: barrier trees, co-transcriptional folding | Michael T. Wolfinger
:summary: Why an RNA molecule does not simply adopt its lowest-energy structure, how energy landscapes are summarised by barrier trees, how folding is computed on a landscape that changes during transcription, and how fast a structure is reached.
:description: RNA folding kinetics: energy landscapes and barrier trees, coarse-grained dynamics, co-transcriptional folding, riboswitches, and folding time distributions.
:hero_eyebrow: Topic
:hero_title: RNA folding kinetics and energy landscapes
:date: 2026-10-31
:modified: 2026-10-31

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

An RNA molecule does not fall into its lowest-energy structure. It moves through a space
of alternative structures, one base pair at a time, and it can get stuck on the way. In
the cell it starts to fold while it is still being made, so the first part of the chain
has already chosen a structure before the rest exists. For a riboswitch, for a designed
switch and for many regulatory RNAs this is not a detail. The structure that matters is
the one reached in time, not the one that is most stable.

This page collects the work on this site on that question, from the formal description of
an energy landscape in 2002 to learned folding time distributions in 2025.

The landscape and its barrier tree
==================================

An :link-flat:`energy landscape <{filename}/glossary.rst#energy-landscape>` is the set of
all secondary structures of a sequence with their free energies, connected by elementary
moves. Its :link-flat:`local minima <{filename}/glossary.rst#local-minimum>` are the
structures a molecule can rest in, the :link-flat:`saddle points <{filename}/glossary.rst#saddle-point>`
between them set the barriers, and a :link-flat:`barrier tree <{filename}/glossary.rst#barrier-tree>`
summarises this in one diagram: leaves are the minima, internal nodes the lowest saddle
connecting two basins, branch lengths the barrier heights.

:link-flat-strong:`Barrier trees of degenerate landscapes <{filename}/blog/2002-07-01-Barrier_Trees_of_Degenerate_Landscapes.rst>`
(*Zeitschrift für Physikalische Chemie* 2002) makes this precise for the degenerate case,
in which many structures share the same energy, and implements it in the ``barriers``
program. The input is deliberately general, i.e. a finite set of states, a neighbourhood
relation and an energy for each state, which is why the same tool applies to lattice
proteins and spin systems as well as to RNA.

The point of the tree is what comes after it. Once the landscape is partitioned into
basins connected by barriers, the basins can be treated as
:link-flat:`macrostates <{filename}/glossary.rst#macrostate>` and the folding process as a
Markov process between them.

Folding as motion between basins
================================

:link-flat-strong:`Efficient computation of RNA folding dynamics <{filename}/blog/2004-04-14-Efficient-Computation-of-RNA-Folding-Dynamics.rst>`
(*Journal of Physics A* 2004) does exactly that. Instead of simulating many stochastic
trajectories through the full structure space, it integrates the flow of population
between barrier-separated basins. Bistable molecules and switches become computable on
timescales that direct simulation does not reach, and the results agree with the
stochastic simulations where both can be run.

Getting the landscape in the first place is its own problem, since enumerating all
structures is impossible beyond small sequences.
:link-flat-strong:`Exploring the lower part of discrete polymer model energy landscapes <{filename}/blog/2006-04-14-Exploring-the-Lower-Part-of-Discrete-Polymer-Model-Energy-Landscapes.rst>`
(*Europhysics Letters* 2006) floods the landscape upward from the optimal and near-optimal
structures, so that only the part relevant for the basin structure is expanded. The
examples are lattice proteins, the algorithm is not specific to them, and
:link-flat-strong:`Memory-efficient exploration of RNA energy landscapes <{filename}/blog/2014-06-12-memory-efficient-RNA-energy-landscape-exploration.rst>`
(*Bioinformatics* 2014) brings the approach back to RNA with a local variant that keeps
the macrostate model exact while fitting into memory. That paper also compares the exact
transition model with two barrier-based approximations and shows where the approximations
mislead.

A related question is how to look at all this. :link-flat-strong:`Visualization of lattice-based protein folding simulations <{filename}/blog/2006-06-01-Visualization-of-Lattice-Based-Protein-Folding-Simulations.rst>`
(IV 2006) treats trajectories and transitions as something to be inspected rather than
summarised, which matters once the state space is too large to read as a table.

Folding while the chain grows
=============================

During transcription the landscape itself changes: every added nucleotide opens
structures that did not exist a moment earlier.
:link-flat-strong:`BarMap and RNA folding on dynamic energy landscapes <{filename}/blog/2010-07-01-BarMap-RNA-Folding-on-Dynamic-Energy-Landscapes.rst>`
(*RNA* 2010) handles this by computing a barrier tree for each transcript length and
mapping the macrostates of one onto those of the next, so that the population can be
carried forward rather than recomputed. The same construction covers temperature changes
and refolding after cleavage.

For long molecules even that is expensive.
:link-flat-strong:`Folding kinetics of large RNAs <{filename}/blog/2008-06-01-Folding-Kinetics-of-Large-RNAs.rst>`
(*Journal of Molecular Biology* 2008) takes the heuristic route with Kinwalker, which
assembles a folding trajectory from locally optimal substructures and interleaves folding
with transcription, up to roughly 1500 nucleotides. It reproduces experimentally studied
cases such as the delayed cloverleaf formation in bacteriophage RNA and the Hok system.

Riboswitches: where timing is the mechanism
===========================================

A riboswitch decides between two structures depending on whether a small molecule is
bound, and for many of them the decision is made during transcription.
:link-flat-strong:`Co-transcriptional folding and metastable states in riboswitch function <{filename}/blog/2017-01-31-NMR-Structural-Profiling-of-Transcriptional-Intermediates-Reveals-Riboswitch-Regulation-by-Metastable-RNA-Conformations.rst>`
(*Journal of the American Chemical Society* 2017) resolves every transcription
intermediate of the 2′dG riboswitch from *Mesoplasma florum* by NMR at single-nucleotide
resolution. Ligand responsiveness depends on the transcript length: certain intermediates
expose a binding-competent arrangement, slightly longer ones already offer competing
folds. The switch works within a narrow kinetic window.

:link-flat-strong:`Co-transcriptional riboswitch modeling with ViennaRNA <{filename}/blog/2018-07-01-Efficient_Computation_of_Cotranscriptional_RNA-Ligand_Interaction_Dynamics.rst>`
(*Methods* 2018) models the same system computationally by adding ligand binding to the
mapped-landscape framework, with binding treated as all-or-none for a defined competent
structure and a concentration-dependent rate. The model reproduces the mechanism: an
early competent state captures the ligand and thereby steers the molecule away from the
conformation that would otherwise take over.

The design side follows directly.
:link-flat-strong:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>`
(*Methods* 2018) makes the design objective explicit and includes folding kinetics in the
evaluation, because a candidate that satisfies the structural constraints can still fail
if its switching path is slow or passes through the wrong intermediate.

How long does it take?
======================

A compact way to state folding kinetics is the distribution of
:link-flat:`first passage times <{filename}/glossary.rst#folding-time>`, i.e. how long a
molecule needs to reach a target structure for the first time. Obtaining that distribution
requires many simulation runs.
:link-flat-strong:`KinPFN <{filename}/blog/2025-01-22-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>`
(ICLR 2025) approximates the whole distribution from a handful of example folding times
with a prior-data fitted network trained on synthetic multi-modal priors. It does not
replace the simulator. It sits on top of it, reports the cumulative distribution in one
forward pass, and saves most of the simulation effort, which makes it possible to compare
many candidates rather than a few. The
:link-flat:`workshop paper <{filename}/blog/2025-03-05-Bayesian-Approximation-of-RNA-Folding-Times.rst>`
states the same idea in shorter form.

Where this connects
===================

Folding kinetics is the reason why a predicted equilibrium structure is not the end of the
story. How such a prediction is computed, and how far it can be trusted, is the subject of
the tutorials on :link-flat-strong:`RNA structure prediction with ViennaRNA <{filename}/rna-structure-prediction.rst>`;
probing data, which constrain the structures a molecule actually populates, are described
in :link-flat-strong:`Predicting RNA structures from sequence and probing data <{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst>`
(*Methods* 2016). The terms used here are defined in the
:link-flat-strong:`glossary <{filename}/glossary.rst>`, e.g.
:link-flat:`metastable state <{filename}/glossary.rst#metastable-state>`,
:link-flat:`co-transcriptional folding <{filename}/glossary.rst#cotranscriptional-folding>`
and :link-flat:`BarMap <{filename}/glossary.rst#barmap>`. The posts are also collected on
the topic pages :link-flat:`RNA folding kinetics </blog/tag/rna-folding-kinetics.html>`,
:link-flat:`energy landscapes </blog/tag/energy-landscapes.html>` and
:link-flat:`co-transcriptional RNA folding </blog/tag/co-transcriptional-rna-folding.html>`.
