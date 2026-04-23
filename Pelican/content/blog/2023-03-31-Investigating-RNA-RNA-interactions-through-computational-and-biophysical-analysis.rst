RNA–RNA interaction analysis of Japanese encephalitis virus
###########################################################

:date: 2023-03-31
:modified: 2026-04-23
:tags: RNA-RNA interaction; non-coding RNA; virus bioinformatics; 3D; flavivirus
:category: publications
:slug: Investigating-RNA-RNA-interactions-through-computational-and-biophysical-analysis
:author: mtw
:summary: This study combines computational and biophysical analysis to characterize a long-range RNA-RNA interaction in Japanese encephalitis virus and to test the role of the conserved cyclization sequence.
:description: A combined computational and biophysical analysis of long-range RNA-RNA interactions in Japanese encephalitis virus.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

  .. figure:: {static}/files/papers/preview/Preview__Mrozowich-2023.001small.webp
        :alt: Graphical abstract of doi:10.1093/nar/gkad223
        :figclass: m-figure m-flat


Long-range RNA-RNA interactions are central to the replication cycle of many flaviviruses, but they are not always easy to characterize directly. In Japanese encephalitis virus (JEV), the 5' and 3' terminal regions are expected to interact through conserved cyclization elements, yet the strength, stoichiometry, and structural behavior of that interaction still needed to be tested experimentally.

This study approaches the problem from both sides. Computational analysis was used to identify the most plausible interaction site and to evaluate whether the conserved cyclization sequence is kinetically favored over competing alternatives such as homodimer formation. The predicted interaction was then tested biophysically using SEC-MALS, analytical ultracentrifugation, microscale thermophoresis, and SAXS.

The result is a stronger case for the long-range interaction than computation alone could provide. The 5' and 3' terminal regions interact directly with nanomolar affinity and a 1:1 stoichiometry, and that interaction weakens substantially when the conserved cyclization sequence is disrupted. That is a useful mechanistic result because it ties the predicted long-range pairing to an experimentally measurable binding event.

Just as importantly, the kinetic analysis supports the idea that the cyclization sequence is not merely one possible pairing among many. It appears to be the dominant interaction pathway under the conditions examined, with an advantage over competing self-association states. For flavivirus biology, that matters because genome cyclization is closely tied to replication, and the computational ranking of alternative structures becomes much more informative once it is backed by binding measurements.

The SAXS-based structural model adds another piece of the picture. It does not deliver atomic resolution, but it does suggest that the complex is flexible while still maintaining a stable overall association in solution. That kind of low-resolution structural information is valuable when interpreting long viral RNAs, where conformational heterogeneity is often part of the biology rather than a nuisance to be averaged away.

More broadly, this paper is a good example of how RNA-RNA interaction studies should be done. Sequence analysis alone is too weak, and biophysical characterization without a clear computational hypothesis is inefficient. The combination is what makes the result persuasive: comparative and thermodynamic reasoning narrow the search space, and orthogonal biophysical methods test whether the predicted interaction actually exists and behaves as expected.

For teams working on viral RNA architecture, long-range RNA interactions, or structure-guided mechanistic questions, I also offer focused technical review and advisory support through my :link-flat:`services page <{filename}/services.rst>`.

.. raw:: html

  <object data="{static}/files/papers/Mrozowich-2023.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Mrozowich-2023.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

    Numerous viruses utilize essential long-range RNA–RNA genome interactions, specifically flaviviruses. Using Japanese encephalitis virus (JEV) as a model system, we computationally predicted and then biophysically validated and characterized its long-range RNA–RNA genomic interaction. Using multiple RNA computation assessment programs, we determine the primary RNA–RNA interacting site among JEV isolates and numerous related viruses. Following in vitro transcription of RNA, we provide, for the first time, characterization of an RNA–RNA interaction using size-exclusion chromatography coupled with multi-angle light scattering and analytical ultracentrifugation. Next, we demonstrate that the 5′ and 3′ terminal regions of JEV interact with nM affinity using microscale thermophoresis, and this affinity is significantly reduced when the conserved cyclization sequence is not present. Furthermore, we perform computational kinetic analyses validating the cyclization sequence as the primary driver of this RNA–RNA interaction. Finally, we examined the 3D structure of the interaction using small-angle X-ray scattering, revealing a flexible yet stable interaction. This pathway can be adapted and utilized to study various viral and human long-non-coding RNA–RNA interactions and determine their binding affinities, a critical pharmacological property of designing potential therapeutics.

Figures and Data
================

.. image-grid::

  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.001.png

  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.002.png
  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.003.png

  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.004.png
  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.005.png

  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.006.png
  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.007.png

  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.008.png
  {static}/files/QuickSlide/QuickSlide__Mrozowich-2023/QuickSlide__Mrozowich-2023.009.png

Citation
========

  | :link-flat-strong:`Investigating RNA-RNA interactions through computational and biophysical analysis <https://doi.org/10.1093/nar/gkad223>`
  | Tyler Mrozowich, Sean Park, Maria Waldl, Amy Henrickson, Scott Tersteeg, Corey R. Nelson, Anneke De Klerk, Borries Demeler, Ivo L. Hofacker, :ul:`Michael T. Wolfinger`, Trushar R. Patel
  | *Nucleic Acids Res.* gkad223 (2023) | :doi:`doi:10.1093/nar/gkad223 <https://doi.org/10.1093/nar/gkad223>` | :link-flat:`PDF <{static}/files/papers/Mrozowich-2023.pdf>` |  :link-flat:`Supplement <{static}/files/papers/Mrozowich-2023__SUPPLEMENT.pdf>`
