Gene Expression Profiling of Pseudomonas Aeruginosa Upon Exposure to Colistin and Tobramycin
############################################################################################

:date: 2021-04-30
:modified: 2026-04-29
:tags: bacteria; NGS
:category: publications
:slug: Gene-Expression-Profiling-of-Pseudomonas-Aeruginosa-Upon-Exposure-to-Colistin-and-Tobramycin
:author: mtw
:summary: This study combines RNA-seq and ribosome profiling to show how Pseudomonas aeruginosa rewires both transcription and translation when challenged with the last-resort antibiotics colistin and tobramycin.
:title: How Pseudomonas aeruginosa responds to colistin and tobramycin
:description: Parallel transcriptome and translatome profiling in cystic-fibrosis-like medium reveals distinct regulatory responses of Pseudomonas aeruginosa to colistin and tobramycin.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Sesso-2021.001small.webp
          :alt: Pathways and functions dysregulated in Pseudomonas aeruginosa upon colistin treatment
          :figclass: m-figure m-flat

This paper looks at a clinically important problem from a systems-biology angle. In cystic fibrosis infections, *Pseudomonas aeruginosa* is often treated with colistin or tobramycin once many other antibiotics have become ineffective. Both are last-resort drugs, but they stress the cell in very different ways. Colistin primarily targets the envelope, whereas tobramycin disrupts translation after energy-dependent uptake into the cytoplasm. The question behind the paper is therefore not just which resistance genes are already known, but how the bacterium reorganizes its physiology when it is actually exposed to these two drugs under a host-relevant growth condition.

The experimental design is what makes the study particularly useful. PA14 was grown in synthetic cystic fibrosis sputum medium and then challenged with inhibitory concentrations of colistin or tobramycin. Instead of measuring transcript levels alone, the paper combined RNA-seq with ribosome profiling in parallel. That matters because antibiotic stress often perturbs translation directly, and a transcriptome alone can miss the distinction between genes that are transcribed more strongly and genes that are actually being translated more efficiently. In that sense, the study moves one level closer to the physiological response of the cell.

The two antibiotics trigger markedly different expression programs. Colistin elicits a response centered on envelope and oxidative-stress adaptation, including well-known pathways connected to lipid A modification and polymyxin resistance, but also broader changes involving the MexT and AlgU regulons. Tobramycin, by contrast, produces a response that is much more tied to translational stress and metabolic rewiring. The cells alter amino-acid catabolism, lower-TCA-cycle genes, secretion systems, and functions linked to motility and attachment, while at the same time increasing expression of systems involved in stalled-ribosome rescue, tRNA methylation, and toxin-antitoxin modules.

One of the strengths of the paper is that it shows these are not merely generic stress signatures. The colistin and tobramycin responses diverge in ways that reflect the underlying drug mechanisms. Colistin mainly drives a membrane-protective and anti-oxidative program, while tobramycin pushes the bacterium into a state that appears designed to reduce uptake, manage translational damage, and compensate for ribosome disruption. That distinction makes the dataset more than a catalog of differentially expressed genes. It provides a mechanistic map of how *Pseudomonas* senses and reacts to two antibiotic classes that remain highly relevant in the clinic.

The ribosome-profiling component is especially valuable in the tobramycin case. Since aminoglycosides act on the ribosome, direct translatome information helps reveal the countermeasures used by the cell to keep protein synthesis viable enough for survival. The upregulation of rescue factors, methylation-associated functions, and toxin-antitoxin systems reads as a translational damage-control program. That is precisely the kind of biology that would be harder to infer confidently from mRNA levels alone.

This study fits naturally beside the earlier anoxic CF-sputum transcriptomics work, which asked how the infection-like environment reshapes physiology over time. The 2021 paper starts from that already adapted state and asks what happens when the cells are hit with last-resort antibiotics. The later Hfq/Crc/CrcZ papers approach related questions from a regulatory angle and ask how metabolic and post-transcriptional control feed into drug susceptibility. Read together, these studies make it clear that antibiotic response in *Pseudomonas* is tightly interwoven with metabolism, envelope state, and translational control.

From a practical perspective, the paper is a reminder that resistance and susceptibility are not static traits. Even when a strain carries known resistance determinants, the acute regulatory response to treatment can still expose weak points or compensatory pathways. That is why datasets like this are useful: they help identify which circuits are activated under drug pressure and which of them might be worth targeting in combination therapies.

.. frame:: Abstract

  *Pseudomonas aeruginosa* has become resistant to most antibiotics, leaving polymyxins and aminoglycosides among the last therapeutic options. This study profiled gene expression and ribosome occupancy in parallel in strain PA14 grown in synthetic cystic fibrosis sputum medium after exposure to colistin or tobramycin. Colistin primarily induced anti-oxidative and envelope-associated responses together with deregulation of the MexT and AlgU regulons, whereas tobramycin caused strong changes in amino-acid catabolism, lower TCA-cycle functions, secretion systems, motility- and attachment-related genes, and pathways involved in stalled-ribosome rescue, tRNA methylation, and toxin-antitoxin systems. The combined RNA-seq/Ribo-seq approach therefore captures both the transcriptional and translational layers of the antibiotic stress response.


Citation
========

  | :link-flat-strong:`Gene Expression Profiling of Pseudomonas aeruginosa Upon Exposure to Colistin and Tobramycin <https://doi.org/10.3389/fmicb.2021.626715>`
  | Anastasia Cianciulli Sesso, Branislav Lilic, Fabian Amman, :ul:`Michael T. Wolfinger`, Elisabeth Sonnleitner, Udo Blasi
  | *Front. Microbiol.* 12:626715 (2021) | :doi:`doi:10.3389/fmicb.2021.626715 <https://doi.org/10.3389/fmicb.2021.626715>` | :link-flat:`PDF <{static}/files/papers/Sesso-2021.pdf>`


See Also
========

  | :link-flat-strong:`RNA-Seq Based Transcriptional Profiling of Pseudomonas Aeruginosa Pa14 After Short- and Long-Term Anoxic Cultivation in Synthetic Cystic Fibrosis Sputum Medium <{filename}/blog/2016-01-28-RNA-Seq-Based-Transcriptional-Profiling-of-Pseudomonas-Aeruginosa-Pa14-After-Short-and-Long-Term-Anoxic-Cultivation-in-Synthetic-Cystic-Fibrosis-Sputum-Medium.rst>`
  | Muralidhar Tata, :ul:`Michael T. Wolfinger`, Fabian Amman, Nicole Roschanski, Andreas Dotsch, Elisabeth Sonnleitner, Susanne Haussler, Udo Blasi
  | *PLoS ONE* 11:e0147811 (2016) | :doi:`doi:10.1371/journal.pone.0147811 <https://doi.org/10.1371/journal.pone.0147811>` | :link-flat:`PDF <{static}/files/papers/Tata-2016.pdf>`

  | :link-flat-strong:`Harnessing Metabolic Regulation to Increase Hfq-Dependent Antibiotic Susceptibility in Pseudomonas aeruginosa <{filename}/blog/2018-11-09-Harnessing-Metabolic-Regulation-to-Increase-Hfq-Dependent-Antibiotic-Susceptibility-in-Pseudomonas-Aeruginosa.rst>`
  | Petra Pusic, Elisabeth Sonnleitner, Beatrice Krennmayr, Dorothea Agnes Heitzinger, :ul:`Michael T. Wolfinger`, Armin Resch, Udo Blasi
  | *Front. Microbiol.* 9:2709 (2018) | :doi:`doi:10.3389/fmicb.2018.02709 <https://doi.org/10.3389/fmicb.2018.02709>` | :link-flat:`PDF <{static}/files/papers/Pusic-2018.pdf>`
