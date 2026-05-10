Why kinetic folding matters in RNA design
#########################################

:date: 2025-01-20
:modified: 2026-04-30
:tags: RNA design; RNA folding kinetics; co-transcriptional RNA folding; synthetic biology
:category: outreach
:slug: Why-Kinetic-Folding-Matters-in-RNA-Design
:author: mtw
:summary: RNA design is incomplete when equilibrium structure is treated as the sole criterion. Folding kinetics becomes essential whenever pathway, timing, or metastable intermediates contribute to function.
:title: Why kinetic folding matters in RNA design
:description: A practical perspective on RNA design problems in which folding pathways, cotranscriptional effects, and kinetic accessibility are as important as the equilibrium structure.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

RNA design is frequently formulated as a problem of specifying a target
structure and identifying sequences that adopt this structure with high
thermodynamic stability. In many cases, this is a useful and necessary
starting point. However, it is not a complete description of function.
Many RNAs are not defined only by their equilibrium structure, but by the
pathway through which this structure is reached. Both the time at which a
functional conformation becomes available, and the persistence of
metastable states can become integral determinants of RNA stability.

Kinetic folding therefore becomes important whenever the route (often referred to as folding path) to a
structure contributes to the mechanism. Equilibrium thermodynamics
describes the relative stability of states. It does not, by itself,
describe whether a transcript can reach a productive state within the
relevant time frame, whether a competing structure blocks this route,
or whether cotranscriptional folding traps the molecule before the
intended conformation becomes accessible.

This distinction has been central to several earlier studies. The post
:link-flat:`Folding kinetics of large RNAs <{filename}/blog/2008-06-01-Folding-Kinetics-of-Large-RNAs.rst>` discusses why pathway information becomes increasingly important for RNA systems that extend beyond small model examples. Likewise,
:link-flat:`BarMap: RNA folding on dynamic energy landscapes <{filename}/blog/2010-07-01-BarMap-RNA-Folding-on-Dynamic-Energy-Landscapes.rst>` emphasizes that the folding landscape is not fixed during transcription, but changes as the nascent RNA chain grows. This becomes particularly relevant in
:link-flat:`Efficient computation of cotranscriptional RNA-ligand interaction dynamics <{filename}/blog/2018-07-01-Efficient_Computation_of_Cotranscriptional_RNA-Ligand_Interaction_Dynamics.rst>`, where ligand binding must be considered together with the transient formation of binding-competent intermediates.

For synthetic RNA design, these issues are especially relevant for
switches, aptamer-coupled systems, regulatory elements, and other
constructs in which timing is part of the functional mechanism. A
candidate sequence may satisfy all static structural constraints and
nevertheless fail experimentally. The active conformation may form
too late, a competing helix may sequester essential nucleotides, or the
ligand-binding state may exist only outside the relevant temporal
window. In such cases, the design has not failed because the target
structure was incorrectly specified, but because the design objective did
not sufficiently represent the mechanism.

The same principle applies from the design perspective in
:link-flat:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>`. A meaningful objective function must encode the intended functional logic, not merely a desired endpoint structure. Once this objective is formulated in mechanistic terms, kinetic information becomes a design criterion rather than a post hoc explanation for failure.

Recent work on :link-flat:`KinPFN: Bayesian Approximation of RNA Folding Kinetics <{filename}/blog/2025-01-01-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst>` and :link-flat:`Bayesian Approximation of RNA Folding Times <{filename}/blog/2025-01-01-Bayesian-Approximation-of-RNA-Folding-Times.rst>` addresses a practical limitation that has long constrained this area. Detailed kinetic simulations can be highly informative, but their computational cost limits their routine use in large design spaces. Approximation methods are valuable because they allow folding-time information to be incorporated earlier in the design process, where many alternative sequences still have to be compared.

The central methodological risk is therefore clear. RNA design can
optimize the wrong criterion. If function depends on pathway behaviour,
then a convincing equilibrium fold may still be insufficient. Kinetic
reasoning does not replace thermodynamic design, comparative analysis,
or experimental validation. Instead, it adds a necessary layer of
interpretation whenever timing, accessibility, or transient states are
part of the mechanism.

This becomes particularly important when candidate designs have to be
prioritized before experimental resources are committed. At this stage,
a project may already have plausible sequences, an assay strategy, and a
mechanistic hypothesis, but still lack a clear distinction between a
folding-pathway problem, a sequence-design problem, and a measurement
problem. A structured review can help clarify this distinction and
identify which candidates are most informative to test next. My
:link-flat:`services page <{filename}/services.rst>` describes how I approach design reviews and advisory work for teams facing this type of decision.
