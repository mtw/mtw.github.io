Rewiring of Gene Expression in Pseudomonas aeruginosa During Diauxic Growth Reveals an Indirect Regulation of the MexGHI-OpmD Efflux Pump by Hfq
################################################################################################################################################

:date: 2022-06-23
:modified: 2022-10-14
:tags: bacteria; NGS; One Health
:category: publications
:slug: Rewiring-of-Gene-Expression-in-Pseudomonas-aeruginosa
:author: mtw
:summary: This study examines carbon catabolite repression and its indirect effects on antibiotic susceptibility in Pseudomonas aeruginosa.
:title: Hfq, Crc, and antibiotic resistance in P. aeruginosa
:description: Here we study carbon catabolite repression and its impact on antibiotic susceptibility in the opportunistic pathogen Pseudomonas aeruginosa

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Rozner-2022.001small.webp
          :alt: Schematic of the mexGHI-opmD operon downregulation by Hfq during carbon catabolite repression
          :figclass: m-figure m-flat


This paper extends the `Hfq/Crc/CrcZ` story in *Pseudomonas aeruginosa* from single regulons to a dynamic physiological transition. The biological setting is diauxic growth: the bacterium first consumes a preferred carbon source and then rewires its metabolism once that source is depleted. In *Pseudomonas*, that transition is controlled in large part by carbon catabolite repression (`CCR`), with `Hfq` and `Crc` repressing many transcripts during growth on preferred substrates and the regulatory RNA `CrcZ` relieving that repression once the cell shifts to alternative nutrients.

The paper asks what that transition looks like globally and whether it has consequences beyond nutrient utilization. To answer that, the study measures the transcriptome, translatome, and proteome in parallel during and after relief of `CCR`. That multi-omics design is the real strength of the work. It allows the authors to distinguish changes that occur at RNA abundance, translational efficiency, and protein output, rather than treating "gene expression" as a single layer.

The main mechanistic result is that the `mexGHI-opmD` operon is upregulated after `CCR` is relieved, which in turn lowers susceptibility to norfloxacin. This is important because the operon encodes an efflux system with direct consequences for antibiotic response. The paper therefore shows that the shift from preferred to non-preferred carbon sources does not just alter metabolism. It also changes the antimicrobial phenotype of the cell.

That observation fits naturally into a broader line of work on how `Hfq`, `Crc`, and `CrcZ` link metabolism to RNA control in *Pseudomonas*. The mechanistic basis is laid out in :link-flat:`Interplay Between the Catabolite Repression Control Protein Crc, Hfq and RNA in Hfq-Dependent Translational Regulation in Pseudomonas aeruginosa <{filename}/blog/2018-01-29-Interplay-Between-the-Catabolite-Repression-Control-Protein-Crc-Hfq-and-RNA-in-Hfq-Dependent-Translational-Regulation-in-Pseudomonas-Aeruginosa.rst>`, and the link to carbapenem uptake is developed further in :link-flat:`Distinctive Regulation of Carbapenem Susceptibility in Pseudomonas aeruginosa by Hfq <{filename}/blog/2020-05-26-Distinctive-Regulation-of-Carbapenem-Susceptibility-in-Pseudomonas-Aeruginosa-by-Hfq.rst>`. This paper pushes that logic one step further by showing how the same network indirectly reshapes resistance-relevant output during diauxic growth. Nutrient-state sensing and antibiotic susceptibility are tightly coupled through the same RNA-centered regulatory architecture.

The word "indirect" in the title matters. The study does not claim that `Hfq` binds the `mexGHI-opmD` operon in a simple one-step regulatory interaction. Instead, the data support a more distributed model in which relief of `CCR` changes the allocation and activity of `Hfq`-dependent control, and the effect on the efflux pump emerges from that broader rewiring. That makes the paper more interesting than a straightforward target-identification study, because it emphasizes network-level consequences of post-transcriptional regulation.

From a practical perspective, the result is also useful because it reminds us that antibiotic susceptibility can depend strongly on physiological state. The same bacterium can present a different drug-response profile depending on which nutrients it has consumed and which regulatory program it has entered. That is exactly the kind of context dependence that often complicates antimicrobial treatment and laboratory interpretation.

Methodologically, the paper is a good example of how multi-omics becomes genuinely informative when tied to a clear transition state. Sampling during and after relief of `CCR` gives the authors a biologically meaningful perturbation, and the combined transcriptome-translatome-proteome view makes it possible to see which responses are broad and which are more specifically post-transcriptional. For readers interested in bacterial RNA regulation, that is a major part of the value.

Taken together with the 2018 and 2020 studies, this paper makes the connection between metabolism, RNA control, and resistance phenotypes especially clear. It shows how the same regulatory machinery is deployed during a physiological growth transition and how that deployment feeds into efflux-mediated drug response.

.. frame:: Abstract

    In Pseudomonas aeruginosa, the RNA chaperone Hfq and the catabolite repression protein Crc act in concert to regulate numerous genes during carbon catabolite repression (CCR). After alleviation of CCR, the RNA CrcZ sequesters Hfq/Crc, which leads to a rewiring of gene expression to ensure the consumption of less preferred carbon and nitrogen sources. Here, we performed a multiomics approach by assessing the transcriptome, translatome, and proteome in parallel in P. aeruginosa strain O1 during and after relief of CCR. As Hfq function is impeded by the RNA CrcZ upon relief of CCR, and Hfq is known to impact antibiotic susceptibility in P. aeruginosa, emphasis was laid on links between CCR and antibiotic susceptibility. To this end, we show that the mexGHI-opmD operon encoding an efflux pump for the antibiotic norfloxacin and the virulence factor 5-Methyl-phenazine is upregulated after alleviation of CCR, resulting in a decreased susceptibility to the antibiotic norfloxacin. A model for indirect regulation of the mexGHI-opmD operon by Hfq is presented.

Citation
========

  | :link-flat-strong:`Rewiring of Gene Expression in Pseudomonas aeruginosa During Diauxic Growth Reveals an Indirect Regulation of the MexGHI-OpmD Efflux Pump by Hfq <https://doi.org/10.3389/fmicb.2022.919539>`
  | Marlena Rozner, Ella Nukarinen, :ul:`Michael T. Wolfinger`, Fabian Amman, Wolfram Weckwerth, Udo Blaesi, Elisabeth Sonnleitner
  | *Front. Microbiol.* (2022) 13:919539 | :doi:`doi:10.3389/fmicb.2022.919539 <https://doi.org/10.3389/fmicb.2022.919539>` | :link-flat:`PDF <{static}/files/papers/Rozner-2022.pdf>`
