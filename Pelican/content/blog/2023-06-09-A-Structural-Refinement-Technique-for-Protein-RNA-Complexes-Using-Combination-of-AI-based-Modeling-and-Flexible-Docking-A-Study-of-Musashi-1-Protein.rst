RNA-Protein Complex Refinement using AI Modeling and Docking
############################################################

:date: 2023-06-09
:modified: 2023-06-1
:tags: new method; 3D; RNA-Protein interaction; AI
:category: publications
:slug:
:author: mtw
:summary: This study presents an efficient technique for refining protein-RNA complexes using artifilial intelligence (AI) based modeling and flexible docking. The method, utilizing parallel cascade selection molecular dynamics (PaCS-MD), accelerates conformational sampling of flexible RNA regions and produces high-quality complex models. Experimental validation demonstrates its superiority over template-based modeling, suggesting its potential for constructing complexes with non-canonical RNA-protein interactions
:description: Enhance protein-RNA complex modeling with AI-based techniques and PaCS-MD for faster conformational sampling and improved quality
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


Understanding the interactions between proteins and RNA is essential for unraveling the mysteries of cellular functions. In a recent study, we proposed an innovative and efficient technique to accurately model the interactions between proteins and RNA, leading to insights that have the potential to advance the fields of structural biology and drug design.

When a protein interacts with RNA, it forms what is known as a protein-RNA complex. Constructing accurate models of these complexes is a formidable challenge. Traditional methods, such as template-based modeling, involve creating the overall conformation and then manually connecting RNA with a protein’s RNA-binding domains (RBDs). However, this doesn't always lead to biologically plausible complexes, highlighting the urgent need for improved methodologies to simulate protein-RNA association complexes.

As we were particularly interested in the RNA-binding protein Musashi-1 (MSI1) and its interaction with RNA through RNA-binding domains (MSI1-RBDs), we proposed a two-step approach: first, we utilized the AI-based modeling technique Alphafold2 to predict a 3D structure of the MSI1-RBDs based on the amino-acid sequences in humans. Following this, we used a flexible docking technique called PaCS-MD to construct the protein-RNA complexes. Unlike traditional methods that manually ligate RNA to the protein, PaCS-MD automatically constructs the complexes, providing a more natural interaction.

To ensure the validity of the constructed complexes, we evaluated their structural stability using the SIE (Solvation Interaction Energy) method. The results confirmed previous studies, showing that a core set of three nucleotides in MSI1-RBDs plays a significant role in the interaction with the target RNA. Moreover, we identified crucial residues for RNA-binding that aligned well with previous findings.

Our method offers a significant advantage over conventional techniques. Unlike traditional homology modeling methods, such as Phyre2, our technique captures the essential transitions required for forming protein-RNA complexes. However, we acknowledge that the technique relies on having initial structural information from NMR (Nuclear Magnetic Resonance) coordinates. Without this data, achieving accurate flexible docking can be challenging.

The study provides a compelling demonstration of constructing plausible protein-RNA complexes using a combination of AI-based modeling and flexible docking. This research takes us one step closer to deciphering the complex interactions between proteins and RNA, paving the way for advancements in personalized medicine and drug discovery.


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
