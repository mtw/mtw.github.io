Cross-Regulation by CrcZ RNA Controls Anoxic Biofilm Formation in Pseudomonas Aeruginosa
########################################################################################

:date: 2016-12-21
:modified: 2026-04-29
:tags: bacteria; non-coding RNA
:category: publications
:slug: Cross-Regulation-by-CrcZ-RNA-Controls-Anoxic-Biofilm-Formation-in-Pseudomonas-Aeruginosa
:author: mtw
:summary: This paper shows that the Hfq-binding RNA CrcZ is highly abundant in anoxic Pseudomonas aeruginosa biofilms and that competition for Hfq by CrcZ limits anaerobic biofilm formation.
:title: CrcZ cross-regulates anoxic biofilm formation in Pseudomonas aeruginosa
:description: A study of how the decoy RNA CrcZ links carbon catabolite repression to Hfq-dependent biofilm physiology under anoxic conditions.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Pusic-2016.001small.webp
          :alt: CrcZ levels modulate viable biomass in anoxic Pseudomonas aeruginosa biofilms
          :figclass: m-figure m-flat

This paper is the point where the `CrcZ` story starts to expand beyond carbon metabolism. `CrcZ` was already known as the decoy RNA that sequesters `Hfq` when carbon catabolite repression is relieved, thereby allowing expression of genes needed for the use of less preferred carbon sources. What this study asks is whether that same competition for `Hfq` can spill over into a completely different physiological process: formation of anaerobic biofilms by *Pseudomonas aeruginosa* under cystic-fibrosis-like conditions.

That question turns out to be well chosen. The paper shows that `CrcZ` is by far the most abundant `Hfq`-bound regulatory RNA in PA14 anoxic biofilms grown in synthetic cystic fibrosis sputum medium. Since `Hfq` itself proves to be important for anaerobic biofilm formation, this immediately suggests a potential cross-regulatory mechanism. If `CrcZ` soaks up a substantial fraction of `Hfq` under these conditions, then it may indirectly reshape a broad set of `Hfq`-dependent processes that have nothing to do with carbon uptake in the narrow sense.

The main biological result is that this is exactly what happens. Deleting `crcZ` increases anoxic biofilm formation, while overproducing `CrcZ` reduces it to a level comparable with the `hfq` deletion mutant. Confocal microscopy and biomass quantification further show that `CrcZ` levels influence the balance between viable and dead cells in these biofilms. In other words, `CrcZ` is not just a marker of altered metabolic state. It actively constrains the development of anaerobic biofilms by competing for `Hfq`.

Methodologically, the study combines RNA-centric and physiology-centric approaches in a useful way. Hfq-bound RNAs were identified by co-immunoprecipitation and RNA-seq, which established the strong enrichment of `CrcZ` in the bound fraction. This was then followed by targeted analysis of `crcZ`, `hfq`, and combined mutant or overexpression strains under anoxic biofilm conditions. The authors also used transcriptome analysis of the `hfq` mutant and physiological readouts such as metabolic activity, redox balance, crystal-violet assays, and confocal imaging. That range is important because the claim is inherently indirect: `CrcZ` does not form biofilms itself, it changes the availability of a global RNA chaperone that then alters multiple downstream pathways.

The broader implication is that regulatory decoy RNAs can cross-regulate functions outside the pathways for which they were first discovered. Here, `CrcZ` couples the nutritional state of the cell to anaerobic biofilm formation by redistributing `Hfq`. That is a conceptually strong result, because it shows how one abundant RNA can bias the use of a central post-transcriptional regulator toward one physiological program and away from another.

This paper also provides the bridge to several later `Pseudomonas` studies on the site. The 2018 NAR paper explains at the molecular level how `Crc`, `Hfq`, and RNA assemble into repressive complexes during carbon catabolite repression. The 2018 metabolic-sensitization paper then exploits `CrcZ`-mediated Hfq sequestration to alter antibiotic susceptibility. And the 2020 porin paper dissects how `Hfq` and `Crc` regulate specific antibiotic entry pathways. This 2016 study is where the physiological reach of `CrcZ` first becomes obvious.

It is also worth noting that the setting here is highly relevant to chronic infection biology. The experiments were done in a medium designed to mimic cystic fibrosis sputum and under oxygen-limited conditions that approximate the microenvironments in established infections. That makes the work more than a basic-regulation paper. It shows that carbon-responsive RNA control is wired into a host-relevant persistence phenotype.

.. frame:: Abstract

  *Pseudomonas aeruginosa* can grow in anaerobic biofilms in cystic fibrosis lungs, and this study identifies the Hfq-binding RNA `CrcZ` as a major regulator of that state. `CrcZ` is highly abundant in PA14 anoxic biofilms and represents the most enriched regulatory RNA in the Hfq-bound fraction. Because `Hfq` is required for efficient anoxic biofilm formation, the data support a model in which `CrcZ` limits biofilm development by sequestering `Hfq`. Deletion of `crcZ` enhances anoxic biofilm formation, whereas `CrcZ` overproduction mirrors the `hfq` mutant phenotype, demonstrating cross-regulation of an Hfq-dependent physiological process unrelated to carbon metabolism in the narrow sense.


Citation
========

  | :link-flat-strong:`Cross-Regulation by CrcZ RNA Controls Anoxic Biofilm Formation in Pseudomonas aeruginosa <https://doi.org/10.1038/srep39621>`
  | Petra Pusic, Muralidhar Tata, :ul:`Michael T. Wolfinger`, Elisabeth Sonnleitner, Susanne Haussler, Udo Blasi
  | *Sci. Rep.* 6:39621 (2016) | :doi:`doi:10.1038/srep39621 <https://doi.org/10.1038/srep39621>` | :link-flat:`PDF <{static}/files/papers/Pusic-2016.pdf>`


See Also
========

  | :link-flat-strong:`How Crc modulates Hfq-dependent RNA regulation in Pseudomonas aeruginosa <{filename}/blog/2018-01-29-Interplay-Between-the-Catabolite-Repression-Control-Protein-Crc-Hfq-and-RNA-in-Hfq-Dependent-Translational-Regulation-in-Pseudomonas-Aeruginosa.rst>`
  | Elisabeth Sonnleitner, Alexander Wulf, Sebastien Campagne, Xue-Yuan Pei, :ul:`Michael T. Wolfinger`, Giada Forlani, Konstantin Prindl, Laetitia Abdou, Armin Resch, Frederic Allain, Ben Luisi, Henning Urlaub, Udo Blasi
  | *Nucleic Acids Res.* 46:1470-1485 (2018) | :doi:`doi:10.1093/nar/gkx1245 <https://doi.org/10.1093/nar/gkx1245>` | :link-flat:`PDF <{static}/files/papers/Sonnleitner-2018.pdf>`

  | :link-flat-strong:`Harnessing Metabolic Regulation to Increase Hfq-Dependent Antibiotic Susceptibility in Pseudomonas aeruginosa <{filename}/blog/2018-11-09-Harnessing-Metabolic-Regulation-to-Increase-Hfq-Dependent-Antibiotic-Susceptibility-in-Pseudomonas-Aeruginosa.rst>`
  | Petra Pusic, Elisabeth Sonnleitner, Beatrice Krennmayr, Dorothea Agnes Heitzinger, :ul:`Michael T. Wolfinger`, Armin Resch, Udo Blasi
  | *Front. Microbiol.* 9:2709 (2018) | :doi:`doi:10.3389/fmicb.2018.02709 <https://doi.org/10.3389/fmicb.2018.02709>` | :link-flat:`PDF <{static}/files/papers/Pusic-2018.pdf>`

  | :link-flat-strong:`PaiI links anaerobic small-RNA regulation to denitrification in Pseudomonas aeruginosa <{filename}/blog/2017-11-23-The-Anaerobically-Induced-sRNA-PaiI-Affects-Denitrification-in-Pseudomonas-Aeruginosa-PA14.rst>`
  | Muralidhar Tata, Fabian Amman, Vinay Pawar, :ul:`Michael T. Wolfinger`, Siegfried Weiss, Susanne Haussler, Udo Blasi
  | *Front. Microbiol.* 8:2312 (2017) | :doi:`doi:10.3389/fmicb.2017.02312 <https://doi.org/10.3389/fmicb.2017.02312>` | :link-flat:`PDF <{static}/files/papers/Tata-2017.pdf>`
