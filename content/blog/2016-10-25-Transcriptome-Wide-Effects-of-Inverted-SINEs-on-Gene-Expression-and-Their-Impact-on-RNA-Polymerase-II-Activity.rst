Transcriptome-Wide Effects of Inverted SINEs on Gene Expression and Their Impact on RNA Polymerase II Activity
################################################################################################################

:date: 2016-10-25
:modified: 2026-04-29
:tags: non-coding RNA; RNA structure conservation
:category: publications
:frontpage: no
:slug: Transcriptome-Wide-Effects-of-Inverted-SINEs-on-Gene-Expression-and-Their-Impact-on-RNA-Polymerase-II-Activity
:author: mtw
:summary: This paper shows that nearby inverted SINEs, especially Alu pairs in 3'UTRs, are associated with reduced gene expression and can repress transcripts by impairing RNA polymerase II elongation.
:title: How inverted SINEs repress gene expression
:description: A transcriptome-wide and mechanistic study of inverted Alu/SINE pairs and their effect on RNA abundance, reporter expression, and RNA polymerase II progression.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Tajaddod-2016.001small.webp
          :alt: Reporter constructs showing that inverted SINE pairs reduce luciferase output and RNA levels
          :figclass: m-figure m-flat

This paper takes a familiar genome-annotation object, the short interspersed element, and asks a sharper regulatory question: what happens when nearby SINEs occur in inverted orientation within transcripts? In primates, the most prominent examples are Alu elements. They are abundant, often located in introns or untranslated regions, and are well known to form double-stranded RNA structures when inverted copies appear close enough to base pair. The interesting point is that such structures had already been linked to several possible outcomes, including RNA editing, nuclear retention, and translational control, but it was still unclear what their dominant transcriptome-wide effect actually is.

The first part of the paper therefore looks at the genome and transcriptome at scale. Using human annotation data and ENCODE RNA-seq profiles, the study shows two related patterns. First, closely spaced inverted Alu pairs are less common than tandemly arranged pairs, suggesting that they are disfavored over evolutionary time. Second, transcripts carrying inverted SINE arrangements are expressed at lower levels than comparable transcripts with tandem or single SINEs. That matters because it turns a collection of anecdotal locus-specific observations into a broader statistical signal.

The paper then does the more important thing and tests mechanism directly. Reporter constructs carrying natural or engineered SINE arrangements in their 3'UTRs were compared in cell culture. These experiments show that inverted SINEs reduce both reporter protein output and RNA abundance, whereas tandem arrangements have a weaker effect. The repression also scales with the quality of the double-stranded structure: constructs that can form more perfect intramolecular duplexes show stronger loss of expression. So the phenomenon is not simply “having an Alu” but having an arrangement that favors structured pairing within the transcript.

What makes the paper especially interesting is where it ends up mechanistically. The authors explicitly tested several obvious double-stranded-RNA explanations and found that they do not account for the effect. The repression was not explained by ADAR-mediated editing, not by STAUFEN binding, and not by the classical cytoplasmic dsRNA sensors one might first suspect. Instead, the evidence pointed toward a different mechanism: transcriptional elongation by RNA polymerase II becomes less efficient across constructs carrying inverted SINEs, leading to reduced transcript output. That is a stronger and more surprising conclusion than simply saying that dsRNA structures destabilize mature RNA.

In other words, the paper moves the problem upstream. The crucial effect of inverted SINEs is not only on the fate of an already completed transcript, but on the process of making that transcript in the first place. If the polymerase is slowed or impaired by the sequence and structural context associated with inverted repeats, then the cell pays a transcriptional cost for placing too much intramolecular pairing potential into transcribed regions. That provides a plausible mechanistic reason why such arrangements are comparatively underrepresented in the genome.

This is also why the paper remains interesting beyond transposon biology. It connects RNA structure, repetitive-sequence organization, and transcriptional control in one framework. Genome evolution is usually discussed in terms of sequence composition and selection on coding potential, but here the selective pressure may also act through the physical behavior of the resulting RNA and its impact on Pol II. That is a genuinely integrative idea.

From the perspective of the rest of the site, this study belongs to the broader non-coding RNA and RNA-structure theme, even though the biological setting is very different from viral UTRs or bacterial sRNAs. The common thread is that RNA structure is not passive. Whether in regulatory RNAs, untranslated regions, or repetitive elements, it can feed back onto gene expression in concrete mechanistic ways. In this case, inverted SINEs are a large-scale example of that principle in mammalian transcriptomes.

.. frame:: Abstract

  Short interspersed elements (SINEs), especially primate Alu elements, are abundant within transcribed regions of mammalian genomes and can form intramolecular double-stranded structures when nearby insertions occur in inverted orientation. This study shows that such inverted SINE pairs are underrepresented relative to tandem pairs and that transcripts harboring them are expressed at lower levels across multiple human cell lines. Reporter assays demonstrate that inverted SINEs reduce both protein output and RNA abundance, with stronger repression when the potential duplex is more perfect. The effect is not explained by known dsRNA sensors or RNA editing, but instead points to impaired RNA polymerase II elongation as a major mechanism.


Citation
========

  | :link-flat-strong:`Transcriptome-Wide Effects of Inverted SINEs on Gene Expression and Their Impact on RNA Polymerase II Activity <https://doi.org/10.1186/s13059-016-1083-0>`
  | Mansoureh Tajaddod, Andrea Tanzer, Konstantin Licht, :ul:`Michael T. Wolfinger`, Stefan Badelt, Florian Huber, Oliver Pusch, Sandy Schopoff, Michael Janisiw, Ivo Hofacker, Michael F. Jantsch
  | *Genome Biol.* 17:220 (2016) | :doi:`doi:10.1186/s13059-016-1083-0 <https://doi.org/10.1186/s13059-016-1083-0>` | :link-flat:`PDF <{static}/files/papers/Tajaddod-2016.pdf>`
