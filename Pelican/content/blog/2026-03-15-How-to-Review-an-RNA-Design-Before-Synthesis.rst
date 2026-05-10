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

RNA designs often look most convincing before they are examined in
detail. The intended fold is easy to sketch, the mechanism sounds
plausible, and the sequence appears to satisfy the formal constraints.
The problems usually emerge later. The productive state may not be
populated strongly enough, an alternative conformation may compete more
effectively than expected, or the design may depend on a folding
pathway that has not been analysed. A review before synthesis therefore
asks whether the design logic is already coherent enough to justify the
next experiment.

The objective has to be stated clearly enough to evaluate candidates at
all. Sometimes that simply means a single dominant fold. In more
interesting systems, the criterion is narrower. One conformation should
remain accessible, another should be suppressed under defined
conditions, or a binding-competent state should appear within a useful
time window. Designs fail surprisingly often because the actual
objective was never stated sharply enough to rank candidates
consistently.

:link-flat:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>` addresses exactly that point. The design objective is made
explicit, and once the mechanism has been translated into structural and
kinetic criteria, candidate selection becomes more defensible.

The structural case also has to be strong enough. A predicted fold may
look attractive and still rest on a very shallow margin over competing
alternatives. For that reason, I prefer to examine ensembles rather
than a single minimum free energy structure whenever possible. A
construct that looks tidy in one representative fold can become much
less convincing if the ensemble remains diffuse or if small
perturbations reshuffle the ranking of alternatives.

Equilibrium may also be the wrong lens. If the design depends on
transcriptional timing, ligand capture, switching order, or metastable
intermediates, static structure alone may be an inadequate screening
criterion. I discuss that broader point in :link-flat:`Why kinetic folding matters in RNA design <{filename}/blog/2025-01-20-Why-Kinetic-Folding-Matters-in-RNA-Design.rst>`. Many disappointing RNA constructs are not structurally
impossible. They are simply mistimed.

Not every project requires a full kinetic analysis. Some features,
however, should trigger closer scrutiny. Competing local helices,
long-range interactions that require transcript completion, and
mechanisms that depend on narrow binding windows all suggest that
endpoint prediction is not enough. In those cases, the design has to be
examined against the folding pathway as part of the mechanism itself.

The sequence should also be stress-tested against nearby variants. Small
synonymous or compensatory changes can be informative even before any
experiment is run. If the intended mechanism collapses under minimal
perturbation, the design is probably too brittle. If sensible variants
preserve the desired behaviour, confidence improves even without any
claim of certainty.

Computational prediction enters here as the first mechanistic model of
the construct. The relevant issue is which assumptions are robust, which
are weakly supported, and which have not yet been tested. That is close
in spirit to :link-flat:`When to trust RNA structure prediction for experimental decisions <{filename}/blog/2026-03-01-When-to-Trust-RNA-Structure-Prediction-for-Experimental-Decisions.rst>`, where the same question appears from the experimental
side.

Before synthesis, the design should at least have a clear mechanistic
objective, a structural analysis that goes beyond a single favourite
fold, an explicit judgment about whether kinetics matters, and a
realistic view of the main failure modes. None of that guarantees
success, but it reduces the chance of spending time and money on a
construct whose weaknesses were visible from the start.

I also offer :link-flat:`design reviews and advisory support </services>`
for teams working at exactly that stage. The main requirement is often a
structured examination of which assumptions behind a candidate design
are well supported, which remain doubtful, and what should be checked
before synthesis begins.
