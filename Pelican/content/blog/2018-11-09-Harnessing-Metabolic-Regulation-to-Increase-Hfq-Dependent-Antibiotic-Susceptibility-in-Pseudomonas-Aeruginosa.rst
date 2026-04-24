Harnessing Metabolic Regulation to Increase Hfq-Dependent Antibiotic Susceptibility in Pseudomonas Aeruginosa
#############################################################################################################

:date: 2018-11-09
:modified: 2026-04-24
:tags: bacteria; One Health
:category: publications
:slug: Harnessing-Metabolic-Regulation-to-Increase-Hfq-Dependent-Antibiotic-Susceptibility-in-Pseudomonas-Aeruginosa
:author: mtw
:summary: This paper asks whether the Hfq/Crc/CrcZ metabolic control system can be used to make Pseudomonas aeruginosa more sensitive to antibiotics, and shows that the answer is yes.
:title: Metabolic control of Hfq-dependent antibiotic susceptibility in Pseudomonas aeruginosa
:description: A study linking Hfq, CrcZ, carbon source, c-di-GMP, and antibiotic susceptibility in Pseudomonas aeruginosa, with an eye toward metabolic re-sensitization.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Pusic-2018.001small.webp
          :alt: Increased CrcZ levels correlate with increased gentamicin susceptibility in Pseudomonas aeruginosa
          :figclass: m-figure m-flat

This paper takes the Hfq story in *Pseudomonas aeruginosa* one step further. Instead of asking only which genes are controlled by Hfq, it asks whether that regulatory layer can be exploited to make the bacterium more susceptible to antibiotics. That is a more intervention-oriented question, and it gives the work a slightly different flavor from the mechanistic porin paper that followed later. The central idea is that Hfq is not just another global regulator. Because it sits at the intersection of carbon catabolite repression, RNA-mediated control, membrane physiology, and stress adaptation, changing Hfq availability could shift several antibiotic-relevant traits at once.

The starting point is the observation that deletion of `hfq` increases susceptibility of *P. aeruginosa* to multiple classes of clinically relevant antibiotics. The paper then asks why that happens and whether the same effect can be reproduced in a less drastic and more physiologically meaningful way. That second question is where `CrcZ` becomes important. `CrcZ` is an RNA decoy that sequesters Hfq and thereby counteracts Hfq/Crc-mediated repression. If higher `CrcZ` levels reduce effective Hfq activity, then metabolic conditions that induce `CrcZ`, or artificial overexpression of `CrcZ`, might sensitize cells to antibiotics without deleting a global regulator outright.

Methodologically, the study combines several layers of evidence. It compares antibiotic susceptibility of wild-type and `hfq` deletion strains in both PAO1 and PA14 backgrounds, uses RNA-seq to identify antibiotic-relevant processes influenced by Hfq, and then links those transcriptomic changes to physiological phenotypes including membrane potential, `c-di-GMP` levels, and biofilm formation. In parallel, the paper tests whether raising `CrcZ` levels by plasmid overexpression or by growth on non-preferred carbon sources can reproduce the sensitizing effect. That combination is important because it turns the paper from a descriptive regulatory study into a proof-of-principle for metabolic re-sensitization.

The result is not a single neat pathway but a broader systems picture. Loss of Hfq affects multiple determinants of antibiotic susceptibility at once: uptake and efflux functions, membrane and LPS-related traits, energy metabolism, and signaling pathways connected to `c-di-GMP`. The paper therefore argues that the increased susceptibility of the `hfq` mutant is a composite phenotype rather than the consequence of one master resistance gene. That makes the biology messier, but also more realistic. Antibiotic response in *Pseudomonas* is typically shaped by overlapping physiological layers rather than by a single switch.

What makes the paper especially interesting is that the `CrcZ` experiments point toward a controllable lever. Overproducing `CrcZ` increases sensitivity to gentamicin, and growth on oxaloacetate, a non-preferred carbon source that induces `CrcZ`, shifts susceptibility in the same direction. In complex synthetic cystic fibrosis sputum medium, adding oxaloacetate also lowers the MIC for gentamicin and cefepime. That gives the paper its practical angle: metabolic context can be used to bias the regulatory state of the bacterium toward a more antibiotic-sensitive phenotype.

Seen from the perspective of the later work on `oprD`, `opdP`, `Crc`, and carbon catabolite repression, this study is an important bridge. It establishes the broader principle that Hfq-dependent post-transcriptional regulation is tied to antibiotic susceptibility in a metabolically responsive way. The later papers then dissect individual branches of that logic in more detail. Here, the emphasis is still on the network level: Hfq availability, modulated by `CrcZ`, changes how the cell handles drugs across several mechanistic layers.

The paper is also a good example of why bacterial RNA regulation matters beyond classical sRNA target maps. Regulatory RNAs such as `CrcZ` can have indirect but clinically meaningful effects because they redistribute the activity of central RNA-binding proteins. In this case, a carbon-source-sensitive decoy RNA becomes part of a strategy for shifting susceptibility to aminoglycosides and beta-lactams. That is a strong illustration of how metabolism and antimicrobial response are coupled in opportunistic pathogens.

.. frame:: Abstract

  The opportunistic pathogen *Pseudomonas aeruginosa* is highly resistant to many antibiotics. This study shows that deletion of the RNA chaperone `hfq` increases susceptibility to multiple antibiotic classes and that Hfq affects several resistance-related traits, including import and efflux functions, energy metabolism, cell-envelope properties, and `c-di-GMP` levels. Importantly, the Hfq-sequestering regulatory RNA `CrcZ`, when overproduced or induced by non-preferred carbon sources, also enhances antibiotic sensitivity. These findings suggest that controlled induction of `CrcZ` can be used to re-sensitize *P. aeruginosa* through metabolic control of Hfq-dependent regulation.


Citation
========

  | :link-flat-strong:`Harnessing Metabolic Regulation to Increase Hfq-Dependent Antibiotic Susceptibility in Pseudomonas aeruginosa <https://doi.org/10.3389/fmicb.2018.02709>`
  | Petra Pusic, Elisabeth Sonnleitner, Beatrice Krennmayr, Dorothea Agnes Heitzinger, :ul:`Michael T. Wolfinger`, Armin Resch, Udo Blasi
  | *Front. Microbiol.* 9:2709 (2018) | :doi:`doi:10.3389/fmicb.2018.02709 <https://doi.org/10.3389/fmicb.2018.02709>` | :link-flat:`PDF <{static}/files/papers/Pusic-2018.pdf>`


See Also
========

  | :link-flat-strong:`Distinctive Regulation of Carbapenem Susceptibility in Pseudomonas aeruginosa by Hfq <{filename}/blog/2020-05-26-Distinctive-Regulation-of-Carbapenem-Susceptibility-in-Pseudomonas-Aeruginosa-by-Hfq.rst>`
  | Elisabeth Sonnleitner, Petra Pusic, :ul:`Michael T. Wolfinger`, Udo Blasi
  | *Front. Microbiol.* 11:1001 (2020) | :doi:`doi:10.3389/fmicb.2020.01001 <https://doi.org/10.3389/fmicb.2020.01001>` | :link-flat:`PDF <{static}/files/papers/Sonnleitner-2020.pdf>`

  | :link-flat-strong:`Rewiring of Gene Expression in Pseudomonas aeruginosa During Diauxic Growth Reveals an Indirect Regulation of the MexGHI-OpmD Efflux Pump by Hfq <{filename}/blog/2022-06-23-Rewiring-of-Gene-Expression-in-Pseudomonas-aeruginosa-During-Diauxic-Growth-Reveals-an-Indirect-Regulation-of-the-MexGHI-OpmD-Efflux-Pump-by-Hfq.rst>`
  | Marlena Rozner, Ella Nukarinen, :ul:`Michael T. Wolfinger`, Fabian Amman, Wolfram Weckwerth, Udo Blaesi, Elisabeth Sonnleitner
  | *Front. Microbiol.* 13:919539 (2022) | :doi:`doi:10.3389/fmicb.2022.919539 <https://doi.org/10.3389/fmicb.2022.919539>` | :link-flat:`PDF <{static}/files/papers/Rozner-2022.pdf>`
