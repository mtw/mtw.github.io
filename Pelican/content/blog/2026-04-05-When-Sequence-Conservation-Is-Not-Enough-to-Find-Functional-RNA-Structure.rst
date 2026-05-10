When sequence conservation is not enough to find functional RNA structure
#########################################################################

:date: 2026-04-05
:modified: 2026-05-01
:tags: RNA structure conservation; virus bioinformatics; xrRNA; flavivirus; non-coding RNA
:category: outreach
:slug: When-sequence-conservation-is-not-enough-to-find-functional-RNA-structure
:author: mtw
:summary: Functional RNA structures are often preserved long after primary sequence similarity becomes weak or misleading. In those cases, comparative analysis has to look for conserved architecture, compensatory change, and shared structural logic rather than sequence identity alone.
:title: When sequence conservation is not enough to find functional RNA structure
:description: Why functional RNA elements are often better tracked through conserved architecture than through primary sequence alone, especially in viral untranslated regions.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

  .. figure:: {static}/files/figures/blog_img_01.webp
        :alt: RNA multiple sequence alignment and secondary structure
        :figclass: m-figure m-flat

Sequence conservation is a useful starting point in comparative
biology, but it can be a poor guide to functional RNA structure.
Structured RNAs may remain under selection at the level of base
pairing, topology, or higher-order organization even while their
primary sequence drifts. A sequence-only view will miss part of that
signal.

The point becomes especially clear in viral untranslated regions. In
many RNA viruses, the non-coding parts of the genome do not merely
separate coding segments or stabilize transcript ends. They carry
structured elements that influence replication, cyclization, nuclease
resistance, host adaptation, and regulatory timing. Those functions can
remain conserved even when the underlying sequence has changed
substantially.

Comparative RNA analysis therefore has to ask a different question.
Instead of following sequence identity alone, it has to examine whether
the same architecture has been preserved. Compensatory substitutions,
recurring motif arrangements, and conserved mechanistic roles become
more informative than local sequence similarity by itself.

The flavivirus `3'UTR` provides a particularly good example. In :link-flat:`Comparative genomics of flavivirus 3' UTR RNA structures <{filename}/blog/2019-03-24-Functional_RNA_Structures_in_the_3UTR_of_Tick-Borne_Insect-Specific_and_No_Known_Vector_Flaviviruses.rst>`, the point is not simply that these viruses contain structured RNA. The deeper result is that lineages with very different sequence histories can still preserve exoribonuclease-resistant RNAs and other functional modules through shared structural organization. What is conserved is often the mechanism, not the exact wording of the sequence.

The same logic becomes even clearer in the mosquito-borne branch. :link-flat:`Functional RNA structures in the 3'UTR of Mosquito-Borne Flaviviruses <{filename}/blog/2021-09-06-Functional-RNA-structures-in-the-3UTR-of-MBFV.rst>` shows that these genomes are built from a recurring structural vocabulary, including xrRNAs, dumbbells, and terminal stem-loops, yet the number, arrangement, and detailed realization of those elements vary across groups. A sequence-based comparison alone would flatten that picture. Structural comparison reveals the lineage-specific architecture.

Functional RNA elements are not always portable as
simple motifs. An xrRNA is not defined by a short consensus sequence. It
is defined by a fold that creates a physical barrier to exonuclease
progression. The same is true more broadly for many structured elements
in viral genomes, whose activity depends on geometry and context.

Tick-borne flaviviruses offer a useful intermediate case. In :link-flat:`RNA structure conservation and molecular epidemiology of TBEV <{filename}/blog/2021-12-17-Evolutionary-traits-of-Tick-borne-encephalitis-virus-Pervasive-non-coding-RNA-structure-conservation-and-molecular-epidemiology.rst>`, the central observation is that the `3'UTR` varies, but not arbitrarily. The variable region still draws from a limited structural vocabulary. That means lineage diversification is better understood as a remodeling of architecture than as unconstrained sequence drift.

The same principle also explains why newly discovered lineages can be so informative. In :link-flat:`Mpulungu virus and unique xrRNAs in a novel African tick flavivirus <{filename}/blog/2021-03-01-An_African_Tick_Flavivirus_Forming_an_Independent_Clade_Exhibits_Unique_Exoribonuclease-Resistant_RNA_Structures_in_the_Genomic_three_prime-Untranslated_Region.rst>` and the later :link-flat:`Xinyang flavivirus clade paper <{filename}/blog/2024-05-29-Xingyang-flavivirus-from-Haemaphysalis-flava-ticks-defines-a-basal-likely-tick-only-Orthoflavivirus-clade.rst>`, the genomes look unusual at the sequence level, yet the untranslated regions still preserve recognizable structured-RNA strategies. That kind of result would be very hard to see if one were only searching for clean sequence conservation.

This is one of the more important conceptual shifts in RNA virology. It
changes what counts as homology, what counts as divergence, and what
kinds of questions can be asked about function. Sequence divergence
does not imply that structure has been lost. In many cases, the
function has been re-encoded in a different sequence realization.

When the biology depends on structured RNA, sequence alignment is
usually the beginning of the analysis rather than the end.
Interpretation becomes much stronger once covariation, consensus
folding, experimental validation, and comparative architecture are
considered together.
