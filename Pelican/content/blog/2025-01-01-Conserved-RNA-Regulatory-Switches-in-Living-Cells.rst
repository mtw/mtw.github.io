Identification of Conserved RNA Regulatory Switches in Living Cells
###################################################################

:date: 2025-01-01
:modified: 2026-04-24
:tags: RNA structure prediction; RNA structure conservation
:category: publications
:slug: conserved-rna-regulatory-switches-in-living-cells
:author: mtw
:summary: Transcriptome-scale ensemble mapping combined with covariation analysis reveals conserved RNA thermometers in bacteria and regulatory 5' UTR switches in human cells.
:title: Conserved RNA regulatory switches in living cells
:description: Transcriptome-wide mapping of RNA structural ensembles in living cells reveals conserved bacterial RNA thermometers and regulatory 5' UTR switches in human cells.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Most transcriptome-wide RNA structure studies still summarize each RNA with a single consensus structure. This paper tackles the more difficult and more realistic problem: many RNAs populate ensembles of alternative conformations, and some of those alternative states act as regulatory switches in living cells. The key question is how to recover such ensembles at transcriptome scale and distinguish functional structural heterogeneity from background noise.

The study combines two ingredients. First, transcriptome-wide MaP-based structure probing data are deconvolved with the DRACO algorithm to infer RNA secondary structure ensembles rather than single structures. Second, the resulting conformations are filtered with an automated conservation framework, DeConStruct, which uses covariation and comparative analysis to prioritize candidate regulatory structures. This combination makes it possible to move from transcriptome-wide structural profiling to the systematic discovery of conserved RNA switches.

In bacteria, the approach identified a substantial set of regions that populate two or more conformations in vivo and recovered known regulatory elements, confirming that the method can detect genuine structural switching behavior. More importantly, it uncovered several previously uncharacterized RNA thermometers in the 5' UTRs of *cspG*, *cspI*, *cpxP*, and *lpxP*, and then followed these candidates mechanistically during cold adaptation. In this context, the work also resolved a role for the CspE chaperone in regulating *lpxP*, making the paper a strong example of how ensemble mapping can lead to concrete functional hypotheses.

The eukaryotic part is equally notable. By introducing a dedicated 5'UTR-MaP strategy, the paper extends ensemble-scale RNA structure mapping into human 5' UTRs and identifies structural switches connected to differential open reading frame usage in transcripts such as *CKS2* and *TXNL4A*. This is a useful reminder that RNA structure prediction becomes more powerful when it is treated as an ensemble problem rather than a single-structure problem, especially in regulatory regions where alternative conformations can alter translation behavior.

For computational RNA biology, this is an important paper because it connects three layers that are often treated separately: transcriptome-scale probing, ensemble deconvolution, and evolutionary support. It therefore sits squarely in the `RNA structure prediction` space, but in a way that moves beyond static secondary-structure models and toward experimentally anchored maps of regulatory structure dynamics in living cells.

.. raw:: html

  <object data="{static}/files/papers/Borovska-2025.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs.
     <a href="{static}/files/papers/Borovska-2025.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

   RNA molecules can populate ensembles of alternative structural conformations; however, comprehensively mapping RNA conformational landscapes within living cells presents notable challenges and has, as such, so far remained elusive. Here, we generate transcriptome-scale maps of RNA secondary structure ensembles in both Escherichia coli and human cells, uncovering features of structurally heterogeneous regions. By combining ensemble deconvolution and covariation analyses, we report the discovery of several bacterial RNA thermometers in the 5′ untranslated regions (UTRs) of the cspG, cspI, cpxP and lpxP mRNAs of Escherichia coli. We mechanistically characterize how these thermometers switch structure in response to cold shock and reveal the CspE chaperone-mediated regulation of lpxP. Furthermore, we introduce a method for the transcriptome-scale mapping of 5′ UTR structures in eukaryotes and leverage it to uncover RNA structural switches regulating the differential usage of open reading frames in the 5′ UTRs of the CKS2 and TXNL4A mRNAs in HEK293 cells. Collectively, this work reveals the complexity of RNA structural dynamics in living cells and provides a resource to accelerate the discovery of regulatory RNA switches.

Citation
========

  | :link-flat-strong:`Identification of conserved RNA regulatory switches in living cells using RNA secondary structure ensemble mapping and covariation analysis <{filename}/blog/2025-01-01-Conserved-RNA-Regulatory-Switches-in-Living-Cells.rst>`
  | Ivana Borovská, Chundan Zhang, Sarah-Luisa J. Dülk, Edoardo Morandi, Marta F. S. Cardoso, Billal M. Bourkia, Daphne A. L. van den Homberg, :ul:`Michael T. Wolfinger`, Willem A. Velema, Danny Incarnato
  | *Nat. Biotechnol.* (2025) | :doi:`doi:10.1038/s41587-025-02739-0 <https://doi.org/10.1038/s41587-025-02739-0>` | :link-flat:`PDF <{static}/files/papers/Borovska-2025.pdf>`
