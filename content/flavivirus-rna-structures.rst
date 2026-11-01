Structured RNAs in flavivirus genomes
#####################################
:slug: flavivirus-rna-structures
:title: Structured RNAs in flavivirus genomes: xrRNAs, dumbbells, cyclization | Michael T. Wolfinger
:summary: What is structured in the untranslated regions of flavivirus genomes, how exoribonuclease-resistant RNAs stall Xrn1, how these elements are distributed across mosquito-borne, tick-borne and insect-specific lineages, and how they can be designed from scratch.
:description: Structured RNA elements in flavivirus genomes: xrRNAs that stall Xrn1, dumbbells and stem-loops, cyclization, and the design of mechanically active RNAs.
:hero_eyebrow: Topic
:hero_title: Structured RNAs in flavivirus genomes
:date: 2026-10-31
:modified: 2026-10-31

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

The genome of a flavivirus is a single positive-strand RNA of about eleven kilobases
with one long open reading frame and two untranslated regions. The untranslated regions
are not spacers: they carry structured elements that the virus depends on, i.e. elements
that resist a host enzyme, that bring the two ends of the genome together, or that bind
host proteins, and most of them are conserved as a fold rather than as a sequence. This
page collects the work on this site on these elements, from comparative analyses across
virus lineages to the design of such a fold from scratch. Each paper is linked here by a
short description of what it does, and the post behind the link gives its title, the full
citation and the DOI.

How an RNA stops an enzyme
==========================

The clearest case is the :link-flat:`exoribonuclease-resistant RNA <{filename}/glossary.rst#xrrna>`
(xrRNA). The host exoribonuclease Xrn1 degrades RNA from the 5′ end. In a flavivirus the
enzyme stalls at a defined position in the 3′ untranslated region, and the RNA downstream
of that position survives as :link-flat:`subgenomic flaviviral RNA <{filename}/glossary.rst#sfrna>`
(sfRNA), which interferes with the antiviral response of the host.

The resistance is mechanical rather than chemical: the element folds into a ring whose
closure is held by a pseudoknot, the 5′ end of the element is threaded through that ring, and the
construction holds against the enzyme pulling on it. Sequence identity matters only where
it maintains this topology, which is why xrRNAs are hard to find by sequence comparison
alone and why they were found by looking for the fold.

What is conserved across the lineages
=====================================

Mosquito-borne flaviviruses such as dengue, Zika, West Nile, Japanese encephalitis and
yellow fever virus build their 3′ untranslated regions from a small set of recurring
modules: one or more xrRNAs, dumbbell elements and a terminal stem-loop. The number of
copies and their arrangement differ between lineages, the vocabulary does not. A book
chapter on :link-flat-strong:`the structured modules of mosquito-borne flavivirus 3′UTRs <{filename}/blog/2021-09-02-Functional-RNA-structures-in-the-3UTR-of-MBFV.rst>`
(*Virus Bioinformatics* 2021) describes that vocabulary for the group.

A :link-flat-strong:`comparative analysis of flavivirus 3′ UTR structures <{filename}/blog/2019-03-25-Functional_RNA_Structures_in_the_3UTR_of_Tick-Borne_Insect-Specific_and_No_Known_Vector_Flaviviruses.rst>`
(*Viruses* 2019) extends the question to tick-borne, insect-specific and no-known-vector
flaviviruses. It found xrRNA-like elements distributed far more widely than the
lineage-specific view had suggested, and a repeated, cascaded organisation of duplicated
elements in insect-specific viruses. Within one virus species the same logic applies: a
study of :link-flat-strong:`structure conservation and molecular epidemiology in tick-borne encephalitis virus <{filename}/blog/2021-12-17-Evolutionary-traits-of-Tick-borne-encephalitis-virus-Pervasive-non-coding-RNA-structure-conservation-and-molecular-epidemiology.rst>`
(*Virus Evolution* 2022) shows a strongly conserved core domain near the 3′ end of the
genome and a variable region upstream of it that is still built from the same modules,
combined with a phylogeny of the virus in space and time.

New viruses, same toolkit
=========================

Several of the papers here start in the field rather than at the computer, with a virus
isolated from mosquitoes or ticks, and then ask whether the new genome carries the known
elements.

- A :link-flat-strong:`survey of insect-specific flaviviruses from Zambia <{filename}/blog/2020-09-14-Discoveries-of-Exoribonuclease-Resistant-Structures-of-Insect-Specific-Flaviviruses-Isolated-in-Zambia.rst>`
  (*Viruses* 2020) describes two viruses from *Culex* mosquitoes that replicate in mosquito
  cells but not in mammalian or avian cells. Their 3′ untranslated regions carry xrRNA-like
  folds, dumbbells and a terminal stem-loop, and the predicted xrRNAs stall Xrn1 in vitro.
- The :link-flat-strong:`description of Mpulungu virus, a novel African tick flavivirus <{filename}/blog/2021-03-01-An_African_Tick_Flavivirus_Forming_an_Independent_Clade_Exhibits_Unique_Exoribonuclease-Resistant_RNA_Structures_in_the_Genomic_three_prime-Untranslated_Region.rst>`
  (*Scientific Reports* 2021) reports a virus from a *Rhipicephalus* tick in Zambia that
  groups with Ngoye virus outside the established tick-borne flaviviruses. Two xrRNA
  elements sit in its 3′ untranslated region, both confirmed biochemically.
- The :link-flat-strong:`report on Xinyang flavivirus and a likely tick-only clade <{filename}/blog/2024-05-29-Xinyang-flavivirus-from-Haemaphysalis-flava-ticks-defines-a-basal-likely-tick-only-Orthoflavivirus-clade.rst>`
  (*Journal of General Virology* 2024) adds a virus from ticks in Henan Province, China,
  that joins the same branch. Its dinucleotide composition and a missing furin cleavage
  site in prM argue for a lineage without a vertebrate host, yet the 3′ untranslated
  region keeps the usual architecture of pseudoknot-containing stem-loops and a dumbbell.

Taken together these three viruses say something that no single genome could: the
structured 3′ untranslated region belongs to the core of the flavivirus genome, not to
the part of it that tracks the vertebrate host.

Other elements, other hosts
===========================

Not every structure in these genomes is an xrRNA.

- An :link-flat-strong:`analysis of RNA–RNA interactions in Japanese encephalitis virus <{filename}/blog/2023-03-31-Investigating-RNA-RNA-interactions-through-computational-and-biophysical-analysis.rst>`
  (*Nucleic Acids Research* 2023) measures the long-range interaction that
  :link-flat:`cyclizes <{filename}/glossary.rst#cyclization>` the genome. The two terminal
  regions bind with nanomolar affinity in a one-to-one complex, and the affinity drops
  when the conserved cyclization sequence is disrupted.
- A :link-flat-strong:`study of the Zika virus 3′ terminal region <{filename}/blog/2023-10-23-The-3-prime-terminal-region-of-Zika-virus-RNA-contains-a-conserved-G-quadruplex-and-is-unfolded-by-human-DDX17.rst>`
  (*Biochemistry and Cell Biology* 2024) shows that a conserved G-rich segment forms a
  quadruplex in the context of a longer transcript and that the human helicase DDX17
  unfolds it.
- A :link-flat-strong:`comparison of Musashi binding elements in flavivirus 3′UTRs <{filename}/blog/2019-05-06-Musashi-Binding-Elements-in-Zika-and-Related-Flavivirus-3UTRs-A-Comparative-Study-in-Silico.rst>`
  (*Scientific Reports* 2019) asks where the binding motif of the host protein
  :link-flat:`Musashi-1 <{filename}/glossary.rst#musashi>` is accessible rather than
  merely present, using opening energies against shuffled controls.
- A :link-flat-strong:`pan-flavivirus analysis of small interfering RNA production <{filename}/blog/2024-10-15-Pan-flavivirus-analysis-reveals-sfRNA-independent-3-UTR-biased-siRNA-production-from-an-insect-specific-flavivirus.rst>`
  (*Journal of Virology* 2024) finds that more than 95 % of the small interfering RNAs
  derived from Kamiti River virus map to its long 3′ untranslated region, and that this
  bias does not disappear when sfRNA production is reduced. The region dominates the
  antiviral RNA interference response for a reason that sfRNA biogenesis does not explain.

A related element outside the 3′ untranslated region is the internal ribosome entry site
of bovine viral diarrhea virus, a pestivirus. A :link-flat-strong:`structural study of the BVDV IRES <{filename}/blog/2021-05-15-Insights-into-the-secondary-and-tertiary-structure-of-the-Bovine-Viral-Diarrhea-Virus-Internal-Ribosome-Entry-Site.rst>`
(*RNA Biology* 2022) combines :link-flat:`SHAPE <{filename}/glossary.rst#shape>` probing
with structure modelling and supports a pseudoknot in its domain III.

From comparison to design
=========================

If the function of an xrRNA follows from its topology, the fold should be designable.
The :link-flat-strong:`de novo design of mechanically active RNAs <{filename}/blog/2026-05-12-Rational-design-of-mechanically-active-RNAs-in-Nucleic-Acids-Research.rst>`
(*Nucleic Acids Research* 2026) reduces natural mosquito-borne xrRNAs to a symbolic
description that keeps the three-way junction, the two pseudoknots and the length
constraints between them, generates sequences under those constraints, and filters the
candidates by three-dimensional modelling and molecular dynamics. Of the two pseudoknots
the second decides the mechanical resistance. The third construct in the series stalls
Xrn1 as efficiently as the natural element while most of the recognisable sequence signal
is gone. The earlier :link-flat:`preprint note <{filename}/blog/2026-01-08-Rational-design-of-mechanically-active-RNAs.rst>`
records how the project was framed, and the German mini-review
:link-flat:`Strukturierte RNAs in Viren <{filename}/blog/2023-03-23-Strukturierte-RNAs-in-Viren.rst>`
summarises the idea for a broader audience.

Methods and further reading
===========================

The structures on this page were found with comparative genomics and thermodynamic
structure prediction. Some were then tested in the laboratory, e.g. the xrRNA candidates
of the Zambian isolates and of Mpulungu virus, which were shown to stall Xrn1 in vitro,
and the designed elements of the 2026 design paper. Others, e.g. the elements of Xinyang
virus and the conserved architectures of the comparative studies, rest on prediction and
comparison alone, and the posts say which is which. The methods behind the
predictions are described in the tutorials on
:link-flat-strong:`RNA structure prediction with ViennaRNA <{filename}/rna-structure-prediction.rst>`,
and the terms used here, e.g. :link-flat:`3′ UTR <{filename}/glossary.rst#utr3>`,
:link-flat:`stem-loop <{filename}/glossary.rst#stem-loop>`,
:link-flat:`dumbbell <{filename}/glossary.rst#dumbbell>` and
:link-flat:`pseudoknot <{filename}/glossary.rst#pseudoknot>`, are defined in the
:link-flat-strong:`glossary <{filename}/glossary.rst>`. All posts on this subject are
collected on the topic pages :link-flat:`flavivirus </blog/tag/flavivirus.html>` and
:link-flat:`xrRNA </blog/tag/xrrna.html>`. I was guest editor of a *Viruses* special issue on
:link-flat:`functional RNAs in virology <{filename}/blog/2025-07-29-Functional-RNAs-in-Virology.rst>`
on the same subject.
