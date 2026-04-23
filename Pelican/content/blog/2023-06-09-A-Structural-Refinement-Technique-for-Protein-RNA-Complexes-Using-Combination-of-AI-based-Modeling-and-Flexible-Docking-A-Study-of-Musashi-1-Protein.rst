RNA-Protein Complex Refinement using AI Modeling and Docking
############################################################

:date: 2023-06-09
:modified: 2026-04-23
:tags: new method; 3D; RNA-Protein interaction; AI
:category: publications
:slug:
:author: mtw
:summary: This article explains a workflow for refining protein-RNA complexes by combining AI-based structural models with flexible docking and enhanced sampling.
:description: A method-focused overview of AI-assisted protein-RNA complex refinement using flexible docking and PaCS-MD.
:title: RNA-protein complex refinement using AI modeling and docking


.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

  .. figure:: {static}/files/papers/preview/Preview__Darai-2023.001small.webp
        :alt: Association complex of Musashi RBD1 and RBD with a target RNA
        :figclass: m-figure m-flat


Modeling protein-RNA complexes remains difficult even when reasonably good structures for the individual components are available. The hardest part is often not generating a starting model, but refining the interface in a way that captures flexible RNA segments and produces a biologically plausible binding geometry.

This study addresses that problem with a two-step workflow. First, AlphaFold2 was used to generate a structural model for the RNA-binding domains of the human Musashi-1 (MSI1) protein. Second, the resulting model was refined in the presence of RNA using flexible docking based on parallel cascade selection molecular dynamics (PaCS-MD). The point of the method is not simply to place RNA near a protein surface, but to sample interface rearrangements that matter for complex formation.

Musashi-1 is a useful test case because its RNA recognition has been studied experimentally, which means the resulting models can be checked against known interaction patterns. In the refined complexes, the analysis recovered a core set of residues and nucleotides that are consistent with previous work on MSI1-RNA recognition. That matters more than raw structural novelty: a refinement method is only useful if it recovers contacts that make biochemical sense.

Compared with a more standard template-based workflow built around Phyre2, the PaCS-MD approach produced better-supported association complexes in this system. The main reason is that enhanced sampling gives flexible RNA regions more room to explore realistic conformations during docking, instead of forcing the final model to depend too heavily on manual assembly or rigid starting assumptions.

The method still has clear limits. It depends on having useful initial structural information, and the quality of the final complex remains tied to the quality of both the starting model and the sampling protocol. This is not a general solution to protein-RNA structure prediction from sequence alone. It is a refinement strategy that becomes valuable when there is already enough structural context to make flexible docking meaningful.

That makes the study best understood as a methods contribution. It shows that AI-derived protein models can be combined with enhanced-sampling docking to improve protein-RNA complex refinement, at least for systems like MSI1 where independent evidence exists for the binding interface. For researchers working on RNA-binding proteins, this is a more realistic and useful claim than broad promises about drug discovery.

If your lab or company needs an external review of an RNA-protein modeling workflow, a structure-guided design problem, or a docking strategy, I also offer focused advisory support through my :link-flat:`services page <{filename}/services.rst>`.


.. raw:: html

  <object data="{static}/files/papers/Darai-2023.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Darai-2023.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

   An efficient structural refinement technique for protein-RNA complexes is proposed based on a combination of AI-based modeling and flexible docking. Specifically, an enhanced sampling method called parallel cascade selection molecular dynamics (PaCS-MD) was extended to include flexible docking to construct protein-RNA complexes from those obtained by AI-based modeling (AlphaFold2). With the present technique, the conformational sampling of flexible RNA regions is accelerated by PaCS-MD, enabling one to construct plausible models for protein-RNA complexes. For demonstration, PaCS-MD constructed several protein-RNA complexes of the RNA-binding Musashi-1 (MSI1) family of proteins, which were validated by comparing a group of crucial residues for RNA-binding with experimental complexes. Our analyses suggest that PaCS-MD improves the quality of complex modeling compared to the standard protocol based on template-based modeling (Phyre2). Furthermore, PaCS-MD could also be a beneficial technique for constructing complexes of non-native RNA-binding to proteins.

Citation
========

  | :link-flat-strong:`A Structural Refinement Technique for Protein-RNA Complexes Using a Combination of AI-based Modeling and Flexible Docking: A Study of Musashi-1 Protein <https://doi.org/10.1246/bcsj.20230092>`
  | Nitchakan Darai, Kowit Hengphasatporn, Peter Wolschann, :ul:`Michael T. Wolfinger`, Yasuteru Shigeta, Thanyada Rungrotmongkol, Ryuhei Harada
  | *B. Chem. Soc. Jpn.* (2023)

See Also
========

  | :link-flat-strong:`Theoretical studies on RNA recognition by Musashi 1 RNA–binding protein <{filename}/blog/2022-07-26-Theoretical-studies-on-RNA-recognition-by-Musashi1-RNA-binding-protein.rst>`
  | Nitchakan Darai, Panupong Mahalapbutr, Peter Wolschann, Vannajan Sanghiran Lee, :ul:`Michael T. Wolﬁnger`, Thanyada Rungrotmongkol
  | *Sci. Rep.* 12:12137 (2022) | :doi:`doi:10.1038/s41598-022-16252-w <https://doi.org/10.1038/s41598-022-16252-w>` | :link-flat:`PDF <{static}/files/papers/Darai-2022.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__Darai-2022.pdf>`

  | :link-flat-strong:`Musashi Binding Elements in Zika and Related Flavivirus 3’UTRs: A Comparative Study in Silico <{filename}/blog/2019-05-06-Musashi-Binding-Elements-in-Zika-and-Related-Flavivirus-3UTRs-A-Comparative-Study-in-Silico.rst>`
  | Adriano de Bernardi Schneider, :ul:`Michael T. Wolfinger`
  | *Sci. Rep.* 9(1):6911 (2019) | :doi:`doi:10.1038/s41598-019-43390-5 <https://doi.org/10.1038/s41598-019-43390-5>` | :link-flat:`PDF <{static}/files/papers/deBernardiSchneider-2019a.pdf>` | :link-flat:`Figures <{static}/files/QuickSlide/QuickSlide__deBernardiSchneider-2019a.pdf>`
