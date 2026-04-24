NMR Structural Profiling of Transcriptional Intermediates Reveals Riboswitch Regulation by Metastable RNA Conformations
#######################################################################################################################

:date: 2017-01-31
:modified: 2026-04-24
:tags: bacteria; energy landscapes; synthetic biology; co-transcriptional RNA folding
:category: publications
:slug: co-transcriptional-riboswitch-metastable-states
:author: mtw
:summary: This paper uses NMR spectroscopy to resolve transcription intermediates of the 2'dG riboswitch at single-nucleotide resolution, showing how transcript length and metastable states govern ligand-controlled switching.
:title: Co-transcriptional folding and metastable states in riboswitch function
:description: NMR and computational analysis of transcription intermediates in a 2'dG-sensing riboswitch.


.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Riboswitches regulate gene expression by changing conformation in response to ligand binding, but the decisive structural events often happen while the RNA is still being transcribed. This study focuses on the type I-A 2'dG-sensing riboswitch from *Mesoplasma florum* and asks how transcript length, ligand binding, and metastable intermediates interact during that process.

What makes this paper stand out is the experimental resolution of that question. Rather than inferring intermediates only indirectly, the study used NMR spectroscopy to characterize all relevant transcription intermediates of the riboswitch at single-nucleotide resolution. That provides a rare view of how the accessible conformational space changes as the RNA grows, and it shows very clearly that riboswitch function cannot be understood from the final full-length structure alone.

The methodological approach is worth emphasizing because it differs from many purely computational studies. The RNA was analyzed as a series of length-defined transcription intermediates, allowing the authors to ask, step by step, which helices and alternative folds become available at each stage of transcription. In effect, the work turns cotranscriptional folding into an experimentally accessible sequence of structural snapshots. That is exactly the kind of information that is usually missing when one tries to explain riboswitch behavior from equilibrium models alone.

The main finding is that ligand responsiveness is tightly coupled to transcript length and to the presence of metastable conformations. Certain intermediates transiently expose a binding-competent arrangement, while slightly longer transcripts can already open competing structural options that redirect the switch. In other words, the riboswitch operates within a narrow kinetic window. The regulatory outcome depends on whether ligand binding happens at the right moment, before alternative folds become dominant.

That point matters well beyond this one riboswitch. The paper makes a broader argument that metastable RNA states are not just folding noise on the way to the “real” structure. They can be the mechanistically decisive states. For transcriptional riboswitches in particular, regulation emerges from the coupling of synthesis, folding, and binding, not from equilibrium thermodynamics alone. This is one of the clearest experimental demonstrations of that idea.

For readers interested in RNA design or synthetic biology, this is also the real lesson of the paper. If a regulatory RNA works by passing through a specific sequence of transient states, then designing only for the final minimum-free-energy structure is not enough. One has to think in terms of folding pathways and timing. That perspective became the basis for later computational work on the same 2'dG riboswitch system, including the follow-up landscape-based analysis linked below.




.. frame:: Abstract

  Gene repression induced by the formation of transcriptional terminators represents a prime example for the coupling of RNA synthesis, folding, and regulation. In this context, mapping the changes in available conformational space of transcription intermediates during RNA synthesis is important to understand riboswitch function. A majority of riboswitches, an important class of small metabolite-sensing regulatory RNAs, act as transcriptional regulators, but the dependence of ligand binding and the subsequent allosteric conformational switch on mRNA transcript length has not yet been investigated. We show a strict fine-tuning of binding and sequence-dependent alterations of conformational space by structural analysis of all relevant transcription intermediates at single-nucleotide resolution for the I-A type 2′dG-sensing riboswitch from Mesoplasma f lorum by NMR spectroscopy. Our results provide a general framework to dissect the coupling of synthesis and folding essential for riboswitch function, revealing the importance of metastable states for RNA-based gene regulation.



Citation
========

  | :link-flat-strong:`NMR Structural Profiling of Transcriptional Intermediates Reveals Riboswitch Regulation by Metastable RNA Conformations <https://doi.org/10.1021/jacs.6b10429>`
  | Christina Helmling, Anna Wacker, :ul:`Michael T. Wolfinger`, Ivo L. Hofacker, Martin Hengsbach, Boris Fürtig, Harald Schwalbe
  | *J. Am. Chem. Soc.* 139 (7):2647–56 (2017) | :doi:`doi:10.1021/jacs.6b10429 <https://doi.org/10.1021/jacs.6b10429>`


See also
========

  | :link-flat-strong:`Efficient Computation of Cotranscriptional RNA-Ligand Interaction Dynamics <{filename}/blog/2018-07-01-Efficient_Computation_of_Cotranscriptional_RNA-Ligand_Interaction_Dynamics.rst>`
  | :ul:`Michael T. Wolfinger`, Christoph Flamm, Ivo L. Hofacker
  | *Methods* 143:70–76 (2018) | :doi:`doi:10.1016/j.ymeth.2018.04.036 <https://doi.org/10.1016/j.ymeth.2018.04.036>` | :link-flat:`Preprint PDF <{static}/files/papers/Wolfinger-2018__PREPRINT.pdf>`

  | :link-flat-strong:`In silico design of ligand-triggered RNA switches <{filename}/blog/2018-07-01-In-Silico-Design-of-Ligand-Triggered-RNA-Switches.rst>`
  | Sven Findeiß, Stefan Hammer, :ul:`Michael T. Wolfinger`, Felix Kühnl, Christoph Flamm, Ivo L. Hofacker
  | *Methods* 143:90–101 (2018) | :doi:`doi:10.1016/j.ymeth.2018.04.003 <https://doi.org/10.1016/j.ymeth.2018.04.003>` | :link-flat:`Preprint PDF <{static}/files/papers/Findeiss-2018__PREPRINT.pdf>`
