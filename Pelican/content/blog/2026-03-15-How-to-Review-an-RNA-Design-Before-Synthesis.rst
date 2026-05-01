How to review an RNA design before synthesis
############################################

:date: 2026-03-15
:modified: 2026-05-01
:tags: RNA design; RNA structure prediction; RNA folding kinetics; synthetic biology; ViennaRNA
:category: outreach
:slug: How-to-review-an-RNA-design-before-synthesis
:author: mtw
:summary: Many RNA designs fail for reasons that are visible long before the first synthesis order is placed. A careful review can expose mismatched objectives, weak structural assumptions, and overlooked kinetic failure modes before they become expensive.
:title: How to review an RNA design before synthesis
:description: A practical guide to evaluating RNA constructs before synthesis, with attention to structure prediction, folding kinetics, mechanism, and candidate prioritization.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

An RNA design often looks most convincing at the moment it is drawn on a slide. The intended fold is clear, the mechanistic story seems plausible, and the sequence appears to satisfy the formal constraints. Problems usually emerge later. The productive structure is not populated strongly enough, an alternative conformation competes more effectively than expected, or the whole construct depends on a kinetic pathway that was never examined in the first place.

That is why a review before synthesis is worth doing. The point is not to prove that a design will work. Very few serious RNA projects offer that kind of certainty. The point is to decide whether the design logic is strong enough that the next experiment is worth its cost.

The first question is whether the objective is stated clearly enough. In simple cases, that may mean a single dominant fold. In more interesting systems, it often means something more specific: one conformation should remain accessible, another should be disfavored under defined conditions, or a binding-competent state should appear within a useful time window. Designs fail surprisingly often because the real objective was never formalized well enough to rank candidates consistently.

That issue sits at the center of :link-flat:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>`. The paper is useful not only because it proposes a workflow, but because it makes the design objective explicit. Once the mechanism is translated into structural and kinetic criteria, candidate selection becomes much more disciplined.

The second question is whether the structural evidence is actually strong enough. A predicted fold may look attractive, yet still rest on a very shallow margin over competing alternatives. That is one reason I find it useful to review designs in terms of ensembles rather than a single minimum-free-energy structure wherever possible. A construct that looks clean in one representative fold can become much less convincing if the ensemble remains diffuse or if small perturbations immediately reshuffle the ranking of alternatives.

The third question is whether equilibrium is even the right lens. If the design depends on transcriptional timing, ligand capture, switching order, or metastable intermediates, then static structure alone may be the wrong screening criterion. I discuss that broader point in :link-flat:`Why kinetic folding matters in RNA design <{filename}/blog/2025-01-20-Why-Kinetic-Folding-Matters-in-RNA-Design.rst>`. In practice, many disappointing RNA constructs are not structurally impossible. They are kinetically mistimed.

That does not mean every project needs a full kinetic analysis. It does mean that some signs should trigger extra scrutiny. Competing local helices, long-range interactions that require transcript completion, or mechanisms that depend on narrow binding windows all suggest that endpoint prediction is not enough. In those cases, a design review should ask whether the mechanism still makes sense once the folding pathway is taken seriously.

Another useful check is whether the sequence has been stress-tested against nearby variants. Small synonymous or compensatory changes can be informative even before any experiment is run. If the intended mechanism collapses under minimal perturbation, that is often a warning that the design is too brittle. If the design survives sensible variants and still preserves the desired behavior, confidence improves even without any claim of certainty.

This is also where computational prediction can be used honestly. The goal is not to make the construct look impressive. The goal is to identify which assumptions are robust, which ones are weakly supported, and which ones remain untested. That is close in spirit to :link-flat:`When to trust RNA structure prediction for experimental decisions <{filename}/blog/2026-03-01-When-to-Trust-RNA-Structure-Prediction-for-Experimental-Decisions.rst>`. Both questions come down to the same practical standard: is the evidence strong enough for the next step to be a rational one.

Before synthesis, I would therefore want at least four things on the table: a clear mechanistic objective, a structural analysis that goes beyond a single favorite fold, a judgment about whether kinetics matters, and a realistic view of the main failure modes. None of that guarantees success. It does, however, reduce the chance of spending time and money on a construct whose weaknesses were visible from the start.

For teams working through exactly that stage, I also offer :link-flat:`design reviews and advisory support </services>`. The value is usually not another layer of generic enthusiasm. It is a structured attempt to identify which assumptions behind a candidate design are solid, which are questionable, and what should be checked before synthesis begins.
