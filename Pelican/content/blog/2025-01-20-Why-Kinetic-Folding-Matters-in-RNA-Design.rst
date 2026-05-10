Why kinetic folding matters in RNA design
#########################################

:date: 2025-01-20
:modified: 2026-04-30
:tags: RNA design; RNA folding kinetics; co-transcriptional RNA folding; synthetic biology
:category: outreach
:slug: Why-Kinetic-Folding-Matters-in-RNA-Design
:author: mtw
:summary: RNA design fails surprisingly often when equilibrium structure is treated as the whole story. Folding kinetics matters whenever pathway, timing, or metastable intermediates shape function.
:title: Why kinetic folding matters in RNA design
:description: A practical guide to when RNA design problems depend on folding pathways and not only on equilibrium structure.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

RNA is often designed as if the minimum free energy structure were the
whole target. That can work in simple cases, but many RNAs function
because they reach a state at the right time, avoid a competing state
for long enough, or switch between states under conditions in which
transcription, ligand binding, and cotranscriptional trapping matter.

Kinetic folding becomes relevant whenever the route matters as much as
the endpoint. Equilibrium thermodynamics is often the right starting
point, but it does not cover every design objective.

This point appears already in :link-flat:`Folding kinetics of large RNAs <{filename}/blog/2008-06-01-Folding-Kinetics-of-Large-RNAs.rst>`, which lays out why pathway information becomes essential once RNA systems grow beyond the simplest toy cases. It appears again in :link-flat:`BarMap: RNA folding on dynamic energy landscapes <{filename}/blog/2010-07-01-BarMap-RNA-Folding-on-Dynamic-Energy-Landscapes.rst>`, which makes it explicit that the landscape itself changes during transcription. It becomes especially concrete in :link-flat:`Efficient computation of cotranscriptional RNA-ligand interaction dynamics <{filename}/blog/2018-07-01-Efficient_Computation_of_Cotranscriptional_RNA-Ligand_Interaction_Dynamics.rst>`, where ligand binding has to be understood together with the emergence of binding-competent intermediates.

For synthetic design, this matters most in switches, aptamer-coupled
systems, and related constructs in which timing is part of the
mechanism. A sequence can satisfy all static constraints and still fail
because the productive conformation appears too late, a competing helix
traps the transcript, or the ligand-binding window is too narrow.

:link-flat:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>` makes the same point from the design side. A credible
objective function has to encode the intended mechanism, not just a
target fold. Once the objective is stated properly, kinetics becomes a
design filter rather than an afterthought.

More recent work on :link-flat:`KinPFN: Bayesian Approximation of RNA Folding Kinetics <{filename}/blog/2025-01-01-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>` and :link-flat:`Bayesian Approximation of RNA Folding Times <{filename}/blog/2025-01-01-Bayesian-Approximation-of-RNA-Folding-Times.rst>` points in the same direction. The practical obstacle has often been
cost. Full kinetic simulations are informative, but they are slow.
Approximation methods matter because they allow many more candidates to
be compared without abandoning the mechanistic question.

The methodological problem is straightforward. In RNA design, one can
optimize the wrong criterion. If the system depends on pathway
behaviour, a convincing equilibrium fold may still be irrelevant.
Kinetic reasoning does not replace design intuition, but it can prevent
attention from drifting away from the mechanism that determines
function.

That same problem appears whenever one has to decide which candidate
designs deserve to move forward at all.

Projects often become expensive at exactly that point. A team may
already have sequences, assays, and a plausible mechanistic story, but
no clear answer to whether the design has a folding-pathway problem or a
measurement problem. In that situation, a structured review can save
time. My :link-flat:`services page <{filename}/services.rst>` describes how I handle design reviews and advisory work for teams
facing that kind of decision.
