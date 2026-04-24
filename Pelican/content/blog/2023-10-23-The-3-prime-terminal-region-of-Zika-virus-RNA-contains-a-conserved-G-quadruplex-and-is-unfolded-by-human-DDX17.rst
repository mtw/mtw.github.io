The 3′ terminal region of Zika virus RNA contains a conserved G-quadruplex
################################################################################

:date: 2023-10-23
:modified: 2026-04-23
:tags: virus bioinformatics; RNA-Protein interaction; non-coding RNA; flavivirus; virology
:category: publications
:slug: zika-virus-g-quadruplex-ddx17
:author: mtw
:summary: This study examines evidence for a conserved G-quadruplex in the Zika virus 3' terminal region and discusses what the observed DDX17 interaction does, and does not, imply.
:description: A closer look at G-quadruplex formation in Zika virus RNA, host helicase interaction, and the limits of therapeutic interpretation.
:title: A conserved G-quadruplex in the Zika virus 3' terminal region

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Gemmill-2024.001small.webp
          :alt: G-Quadruplex in the terminal region of the Zika virus genome
          :figclass: m-figure m-flat

Zika virus (ZIKV) is a positive-strand flavivirus whose untranslated terminal regions contain structured RNA elements with likely regulatory roles. In this study, we focused on a G-rich segment in the 3' terminal region and asked two fairly specific questions: is there convincing evidence that this segment forms a conserved G-quadruplex, and how does that element interact with host helicases?

G-quadruplexes are structurally distinct RNA elements formed by stacked guanine quartets. In viral RNAs they are interesting because they may compete with alternative conformations, alter accessibility, or modulate how host factors engage a structured region. That does not make every predicted G4 biologically relevant, but it does make them worth testing when the underlying sequence signal is conserved.

The central result is that the candidate ZIKV G4 is not just a short-oligo artifact. Across available ZIKV isolates, the G-rich segment is conserved, and biochemical assays support G4 formation in the context of a larger 3' terminal region transcript. Pyridostatin and BG4 binding provided experimental support for that interpretation. This moves the discussion from sequence speculation to a more defensible structural observation.

The second important result is that human DEAD-box helicases interact with this region. Both DDX3X132-607 and DDX17135-555 bind the 3' terminal region, and the DDX17 construct used in the study unfolds the G4. Mechanistically, that is interesting because it suggests the local RNA ensemble is not static. Host proteins may reshape this part of the viral RNA, potentially shifting the balance between alternative conformations or affecting downstream processes that depend on terminal-region architecture.

What the study does not show, however, is just as important. It does not establish that the G4 is required for viral replication in cells, nor does it show that DDX17 binding or unwinding is directly druggable in a useful therapeutic sense. Those are hypotheses that may follow from the data, but they are not conclusions supported by the present experiments. For a system like this, the right next steps are functional perturbation, context-specific virology, and direct tests of how the structured region behaves during infection.

This distinction matters because structured viral RNAs are easy to oversell. A conserved element plus a host-factor interaction is already a meaningful result. It tells us there is a plausible structured RNA feature in the ZIKV 3' terminal region and that at least one host helicase can remodel it. That is strong mechanistic groundwork, even before any translational claims enter the picture.

For RNA virology more broadly, this is exactly where computational and biochemical analysis work well together. Comparative sequence analysis identifies conserved candidates, structural assays test whether those candidates persist in larger transcript contexts, and protein-binding experiments begin to reveal how host factors may shape the RNA landscape. That combined view is much more informative than any one layer on its own.

For teams evaluating viral RNA structure hypotheses or RNA-protein interaction models, I also offer focused technical review and advisory support through my :link-flat:`services page <{filename}/services.rst>`.

.. raw:: html

  <object data="{static}/files/papers/Gemmill-2024.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Gemmill-2024.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

   Zika virus (ZIKV) infection remains a worldwide concern, and currently no effective treatments or vaccines are available. Novel therapeutics are an avenue of interest that could probe viral RNA-human protein communication to stop viral replication. One specific RNA structure, G-quadruplexes (G4s), possess various roles in viruses and all domains of life, including transcription and translation regulation and genome stability, and serves as nucleation points for RNA liquid-liquid phase separation. Previous G4 studies on ZIKV using a quadruplex forming G-rich sequences Mapper located a potential G-quadruplex sequence in the 3′ terminal region (TR) and was validated structurally using a 25-mer oligo. It is currently unknown if this structure is conserved and maintained in a large ZIKV RNA transcript and its specific roles in viral replication. Using bioinformatic analysis and biochemical assays, we demonstrate that the ZIKV 3′ TR G4 is conserved across all ZIKV isolates and maintains its structure in a 3′ TR full-length transcript. We further established the G4 formation using pyridostatin and the BG4 G4-recognizing antibody binding assays. Our study also demonstrates that the human DEAD-box helicases, DDX3X132-607 and DDX17135-555, bind to the 3′ TR and that DDX17135-555 unfolds the G4 present in the 3′ TR. These findings provide a path forward in potential therapeutic targeting of DDX3X or DDX17’s binding to the 3′ TR G4 region for novel treatments against ZIKV.

Citation
========

  | :link-flat-strong:`The 3’ terminal region of Zika virus RNA contains a conserved G-quadruplex and is unfolded by human DDX17 <{filename}/blog/2023-10-23-The-3-prime-terminal-region-of-Zika-virus-RNA-contains-a-conserved-G-quadruplex-and-is-unfolded-by-human-DDX17.rst>`
  | Danielle L. Gemmill, Corey R. Nelson, Maulik D. Badmalia, Higor S. Pereira, :ul:`Michael T. Wolfinger`, and Trushar Patel
  | *Biochem. Cell Biol.* 102(1):96–105 (2024) | :doi:`doi:10.1139/bcb-2023-0036 <https://doi.org/10.1139/bcb-2023-0036>` | :link-flat:`PDF <{static}/files/papers/Gemmill-2024.pdf>`
