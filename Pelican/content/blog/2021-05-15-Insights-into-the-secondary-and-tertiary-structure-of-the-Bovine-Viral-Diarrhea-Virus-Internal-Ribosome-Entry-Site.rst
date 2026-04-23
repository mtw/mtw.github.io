Insights into the secondary and tertiary structure of the BVDV Internal Ribosome Entry Site
##################################################################################################################

:date: 2021-05-15
:modified: 2026-04-23
:tags: 3D; SHAPE; virus bioinformatics; non-coding RNA; flavivirus; virology
:category: publications
:slug: Insights-into-the-secondary-and-tertiary-structure-of-the-Bovine-Viral-Diarrhea-Virus-Internal-Ribosome-Entry-Site
:author: mtw
:description: Characterization of a pseudoknot in the 5'UTR Internal Ribosome Entry Site (IRES) of Bovine Viral Diarrhea Virus (BVDV)
:title: Secondary and tertiary structure of the BVDV IRES
:summary: This post summarizes what SHAPE-guided modeling and 3D analysis reveal about a pseudoknot in the BVDV internal ribosome entry site and why that matters for IRES function.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Gosavi-2022.001small.webp
          :alt: 3D structure prediction of the BVDV IRES region
          :figclass: m-figure m-flat



Bovine viral diarrhea virus (BVDV) relies on an internal ribosome entry site (IRES) in its 5' untranslated region to drive cap-independent translation. For systems like this, function depends on RNA architecture rather than sequence alone, which makes the structural organization of the IRES worth analyzing in detail.

This study combined SHAPE-MaP probing with secondary-structure analysis and tertiary modeling to ask a specific question: how is the BVDV IRES organized in solution, and what evidence supports the proposed pseudoknot in domain III? That is the central structural feature of the post, because pseudoknot architecture is likely to be directly relevant to how the IRES maintains a translation-competent state.

The resulting model supports a modular IRES architecture with three major domains. Much of the secondary structure agrees with earlier work, but the analysis also points to flexibility in domain II and a comparatively stable arrangement in domain III. That contrast is useful: it suggests that not all parts of the IRES contribute in the same way, and that local structural stability may be concentrated in the regions most critical for tertiary organization.

The most important result concerns domain III, where the data support an H-type pseudoknot and a specific local arrangement of helices. The tertiary modeling suggests quasi-coaxial stacking between motifs associated with the pseudoknot, which provides a structural explanation for why this region appears unusually stable. Comparative analysis across Pestivirus genomes further supports the idea that the pseudoknot is not an isolated feature of a single strain, but part of a conserved functional architecture.

That does not mean the computational model alone proves mechanism. What it does provide is a more concrete structural hypothesis for how the BVDV IRES is arranged and why certain elements are likely to matter for translation. In other words, the work narrows the space of plausible architectures and gives experimentalists a clearer basis for targeted perturbation.

This is also where the comparison to related IRES systems becomes useful. BVDV and hepatitis C virus share broad organizational similarities, but the real value of that comparison is not to imply immediate transfer of therapeutic strategy. It is to show that conserved structural logic can emerge across related viral translation elements, making careful cross-system comparison worthwhile.

For RNA virology, this is a good example of where structure probing and computational modeling complement each other well. Probing constrains the plausible secondary structures, comparative analysis highlights conserved base pairs, and tertiary modeling translates those constraints into a geometric hypothesis that can be tested further.

I also work with groups that need help interpreting RNA structure models in viral systems and other structured RNAs. If that is relevant to your work, you can find more detail on my :link-flat:`services page <{filename}/services.rst>`.

.. raw:: html

  <object data="{static}/files/papers/Gosavi-2022.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Gosavi-2022.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame :: Abstract

    The Internal Ribosome Entry Site (IRES) RNA of Bovine viral diarrhea virus (BVDV), an economically significant Pestivirus, is required for the cap-independent translation of viral genomic RNA. Thus, it is essential for viral replication and pathogenesis. We applied a combination of high-throughput biochemical RNA structure probing (SHAPE-MaP) and in silico modeling approaches to gain insight into the secondary and tertiary structures of BVDV IRES RNA. Our study demonstrated that BVDV IRES RNA forms in solution a modular architecture composed of three distinct structural domains (I-III). Two regions within domain III are engaged in tertiary interactions to form an H-type pseudoknot. Computational modeling of the pseudoknot motif provided a fine-grained picture of the tertiary structure and local arrangement of helices in the BVDV IRES. Furthermore, comparative genomics and consensus structure predictions revealed that the pseudoknot is evolutionarily conserved among many Pestivirus species. These studies provide detailed insight into the structural arrangement of BVDV IRES RNA H-type pseudoknot and encompassing motifs that likely contribute to the optimal functionality of viral cap-independent translation element.

Figures and Data
================

.. image-grid::

  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.001.png

  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.002.png
  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.003.png

  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.004.png
  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.005.png

  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.006.png
  {static}/files/QuickSlide/QuickSlide__Gosavi-2022/QuickSlide__Gosavi-2022.007.png

Citation
========

  | :link-flat-strong:`Insights into the secondary and tertiary structure of the Bovine Viral Diarrhea Virus Internal Ribosome Entry Site <https://doi.org/10.1080/15476286.2022.2058818>`
  | Devadatta Gosavi, Iwona Wower, Irene K Beckmann, Ivo L Hofacker, Jacek Wower, :ul:`Michael T Wolfinger`, Joanna Sztuba-Solinska
  | *RNA Biol.* 19(1) 496-506 (2022) | :doi:`doi:10.1080/15476286.2022.2058818 <https://doi.org/10.1080/15476286.2022.2058818>` | :link-flat:`PDF <{static}/files/papers/Gosavi-2022.pdf>`
