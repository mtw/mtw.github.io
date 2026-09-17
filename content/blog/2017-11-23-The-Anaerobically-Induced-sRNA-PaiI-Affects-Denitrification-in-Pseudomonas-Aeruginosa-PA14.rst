The Anaerobically Induced sRNA PaiI Affects Denitrification in Pseudomonas Aeruginosa PA14
###########################################################################################

:date: 2017-11-23
:modified: 2026-04-29
:tags: bacteria; non-coding RNA
:category: publications
:slug: The-Anaerobically-Induced-sRNA-PaiI-Affects-Denitrification-in-Pseudomonas-Aeruginosa-PA14
:author: mtw
:summary: This paper identifies the small RNA PaiI as an anaerobically induced regulator in Pseudomonas aeruginosa PA14 and shows that it is needed for efficient denitrification under nitrate-respiring conditions.
:title: PaiI links anaerobic small-RNA regulation to denitrification in Pseudomonas aeruginosa
:description: A study of the nitrate-induced sRNA PaiI in Pseudomonas aeruginosa PA14, its NarXL-dependent expression, and its role in nitrite reduction and anaerobic growth.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Tata-2017.001small.webp
          :alt: PaiI deletion causes transient nitrite accumulation and reduced nitrite reductase activity during anaerobic growth
          :figclass: m-figure m-flat

This paper continues the anaerobic *Pseudomonas aeruginosa* story, but from a more focused regulatory angle. Instead of asking how the whole transcriptome changes during oxygen limitation, it asks whether a specific small RNA helps the bacterium adapt to nitrate-respiring growth. That is an important question because chronic *Pseudomonas* infections in cystic fibrosis lungs often involve oxygen-poor, biofilm-associated conditions where denitrification becomes physiologically relevant. If there are dedicated anaerobiosis-induced sRNAs in this setting, they are likely to be part of the fine-tuning layer that sits on top of the classical transcriptional denitrification cascade.

The main result is the identification and first characterization of `PaiI`, a small RNA that is strongly induced under anaerobic conditions in the presence of nitrate. Its expression depends on the `NarXL` two-component system, which immediately places it inside the nitrate-responsive regulatory network rather than as a generic stress transcript. The paper then shows that `PaiI` is not just a marker of anaerobiosis. A `paiI` deletion mutant displays a clear physiological phenotype under denitrifying conditions, particularly when glucose is used as the carbon source.

Methodologically, the paper grows out of earlier RNA-seq work on PA14 under anoxic conditions. Candidate sRNAs were identified from the anaerobic transcriptome data and then followed up experimentally by Northern blotting, promoter analysis, mutant construction, and physiological assays. That progression matters: the study starts with a transcriptomics observation, but it does not stop there. It moves quickly into targeted genetics and phenotype measurements, which is what makes `PaiI` credible as a functional regulator rather than just another induced RNA band on a blot.

The key phenotype is a defect in efficient denitrification. In the absence of `PaiI`, the cultures accumulate more nitrite and show reduced nitrite reductase activity, indicating a problem in the conversion of nitrite to nitric oxide. The deletion strain is also impaired in anaerobic growth on glucose, and that phenotype can be reconciled with reduced glucose uptake under these conditions. In other words, the paper ties a small RNA to a very concrete physiological bottleneck within nitrate respiration rather than to an abstract stress response.

An interesting aspect of the study is that the effect appears to be indirect. The transcriptome data did not reveal major changes in the abundance of the canonical `nir` transcripts, and the nitrite reductase protein itself was not simply lost in the mutant. Overexpression of `dnr` could complement the deletion phenotype, which places `PaiI` functionally close to the denitrification control circuitry without reducing it to a trivial one-step mechanism. That makes the biology more subtle, but also more realistic: many small RNAs in bacteria shape pathway output through network effects rather than by acting as on/off switches for one obvious target.

The in vivo angle strengthens the paper further. The `paiI` deletion strain was impaired in colonizing murine tumors, a model that contains hypoxic or anaerobic regions and therefore stresses the same nitrate-respiring physiology that the in vitro assays probe. That does not turn `PaiI` into a classical virulence factor paper, but it does show that the anaerobic-growth phenotype is not just a laboratory curiosity. The small RNA matters under host-relevant low-oxygen conditions.

Seen together with the 2016 PA14 anoxic-transcriptome study, this work is a nice example of how broad RNA-seq surveys can lead to more focused mechanistic follow-up. The earlier paper mapped the large-scale physiological shift into long-term anaerobic growth. This one takes one candidate from that landscape and asks what it actually does. The answer is that `PaiI` helps the cell execute denitrification efficiently, especially at the nitrite-reduction step, and thereby supports anaerobic adaptation.

For readers interested in bacterial RNA biology, the paper is also a reminder that *Pseudomonas* sRNA research is not limited to Hfq-dependent envelope or carbon-catabolite regulation. Under anaerobic conditions, small RNAs can also intersect directly with respiration-linked physiology. That makes `PaiI` a useful addition to the site’s broader non-coding RNA theme, even though the biological setting is very different from the viral and structural RNA work elsewhere on the page.

.. frame:: Abstract

  *Pseudomonas aeruginosa* can thrive under anaerobic conditions by using nitrate as terminal electron acceptor, a trait relevant to chronic infection settings such as cystic fibrosis lungs. This study identifies the small RNA `PaiI` in strain PA14 as a nitrate- and anaerobiosis-induced RNA whose expression depends on `NarXL`. Deletion of `paiI` impairs anaerobic growth on glucose, causes transient accumulation of nitrite, and reduces nitrite reductase activity, indicating a defect in efficient denitrification. The mutant is also impaired in growth within murine tumors, underscoring the importance of `PaiI` for adaptation to hypoxic or anaerobic environments.


Citation
========

  | :link-flat-strong:`The Anaerobically Induced sRNA PaiI Affects Denitrification in Pseudomonas aeruginosa PA14 <https://doi.org/10.3389/fmicb.2017.02312>`
  | Muralidhar Tata, Fabian Amman, Vinay Pawar, :ul:`Michael T. Wolfinger`, Siegfried Weiss, Susanne Haussler, Udo Blasi
  | *Front. Microbiol.* 8:2312 (2017) | :doi:`doi:10.3389/fmicb.2017.02312 <https://doi.org/10.3389/fmicb.2017.02312>` | :link-flat:`PDF <{static}/files/papers/Tata-2017.pdf>`


See Also
========

  | :link-flat-strong:`RNA-Seq Based Transcriptional Profiling of Pseudomonas Aeruginosa Pa14 After Short- and Long-Term Anoxic Cultivation in Synthetic Cystic Fibrosis Sputum Medium <{filename}/blog/2016-01-28-RNA-Seq-Based-Transcriptional-Profiling-of-Pseudomonas-Aeruginosa-Pa14-After-Short-and-Long-Term-Anoxic-Cultivation-in-Synthetic-Cystic-Fibrosis-Sputum-Medium.rst>`
  | Muralidhar Tata, :ul:`Michael T. Wolfinger`, Fabian Amman, Nicole Roschanski, Andreas Dotsch, Elisabeth Sonnleitner, Susanne Haussler, Udo Blasi
  | *PLoS ONE* 11:e0147811 (2016) | :doi:`doi:10.1371/journal.pone.0147811 <https://doi.org/10.1371/journal.pone.0147811>` | :link-flat:`PDF <{static}/files/papers/Tata-2016.pdf>`

  | :link-flat-strong:`How Pseudomonas aeruginosa responds to colistin and tobramycin <{filename}/blog/2021-04-30-Gene-Expression-Profiling-of-Pseudomonas-Aeruginosa-Upon-Exposure-to-Colistin-and-Tobramycin.rst>`
  | Anastasia Cianciulli Sesso, Branislav Lilic, Fabian Amman, :ul:`Michael T. Wolfinger`, Elisabeth Sonnleitner, Udo Blasi
  | *Front. Microbiol.* 12:626715 (2021) | :doi:`doi:10.3389/fmicb.2021.626715 <https://doi.org/10.3389/fmicb.2021.626715>` | :link-flat:`PDF <{static}/files/papers/Sesso-2021.pdf>`
