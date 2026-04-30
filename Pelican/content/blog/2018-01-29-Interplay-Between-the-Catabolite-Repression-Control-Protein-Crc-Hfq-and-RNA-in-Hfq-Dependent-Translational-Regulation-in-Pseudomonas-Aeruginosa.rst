Interplay Between the Catabolite Repression Control Protein Crc, Hfq and RNA in Hfq-Dependent Translational Regulation in Pseudomonas Aeruginosa
#######################################################################################################################################################################

:date: 2018-01-29
:modified: 2026-04-29
:tags: bacteria; non-coding RNA
:category: publications
:slug: Interplay-Between-the-Catabolite-Repression-Control-Protein-Crc-Hfq-and-RNA-in-Hfq-Dependent-Translational-Regulation-in-Pseudomonas-Aeruginosa
:author: mtw
:summary: This paper explains how the catabolite repression protein Crc modulates Hfq-dependent translational control in Pseudomonas aeruginosa by stabilizing Hfq/RNA assemblies and competing with sRNA access to Hfq.
:title: How Crc modulates Hfq-dependent RNA regulation in Pseudomonas aeruginosa
:description: A mechanistic study of the Hfq/Crc/RNA complex during carbon catabolite repression in Pseudomonas aeruginosa.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Sonnleitner-2018.001small.webp
          :alt: Crc stabilizes Hfq/RNA complexes in vitro
          :figclass: m-figure m-flat

This paper is the mechanistic centerpiece of the *Pseudomonas aeruginosa* Hfq/Crc/CrcZ story. Earlier work had already made it clear that carbon catabolite repression in *Pseudomonas* does not work like the textbook `cAMP`-CRP systems familiar from enteric bacteria. Instead, it operates largely at the post-transcriptional level and depends on the RNA chaperone `Hfq`, the catabolite repression control protein `Crc`, and the regulatory RNA `CrcZ`. What had remained unclear was how `Crc` actually contributes to Hfq-dependent repression. This paper addresses exactly that point.

The key result is that `Crc` is not simply another independent regulator acting in parallel to `Hfq`. Rather, it enhances `Hfq`-mediated translational repression by forming higher-order assemblies with `Hfq` and A-rich target RNAs. The study shows that `Crc` does not bind productively to `Hfq` alone, nor to RNA alone, under the relevant conditions. Instead, RNA bound to the distal side of `Hfq` provides the context in which `Crc` can engage. In that configuration, `Crc` stabilizes the `Hfq/RNA` complex and thereby strengthens translational silencing of catabolic mRNAs.

That finding matters because it changes the conceptual picture of carbon catabolite repression in *Pseudomonas*. Hfq is the primary RNA-binding repressor, but `Crc` acts as a proteinaceous modulator that increases the lifetime and effectiveness of the repressive complex. This is more interesting than a simple cofactor model, because it shows how an RNA-binding protein can be tuned by another protein through assembly on a shared RNA substrate. In that sense, the paper is not just about *Pseudomonas* physiology. It is also about a general principle of post-transcriptional control.

Methodologically, the paper is unusually rich. It combines RNA-seq with bacterial two-hybrid assays, co-immunoprecipitation, microscale thermophoresis, electrophoretic mobility shift assays, UV and chemical cross-linking, and structural interpretation of the interaction surfaces. That breadth is important because the claim is mechanistic and multi-part: `Crc` and `Hfq` associate in vivo, the association depends on the right RNA context, `Crc` contacts both `Hfq` and RNA in the complex, and the resulting assembly is more stable than the `Hfq/RNA` complex alone. No single technique would have been enough to make that case convincingly.

Another important aspect of the paper is that `Crc` does not just strengthen one branch of Hfq activity. It also interferes with access of at least one regulatory sRNA to the proximal side of `Hfq`. In the experiments shown here, the presence of `Crc` reduces effective binding of the sRNA `PrrF2` to `Hfq`, and corresponding in vivo data suggest that this can affect sRNA-mediated riboregulation. That point gives the paper broader significance: `Crc` is not merely a helper for catabolic repression, it can also bias how `Hfq` is allocated between carbon-source prioritization and other RNA-regulatory tasks.

This is where the physiological interpretation becomes especially useful. The authors propose a working model in which `Crc` helps prioritize `Hfq` function toward the utilization of favored carbon sources during carbon catabolite repression. In other words, when the cell grows on a preferred substrate, `Crc` helps keep `Hfq` focused on shutting down unnecessary catabolic programs. When `CrcZ` accumulates after relief of CCR, `Hfq` is sequestered away from these target mRNAs and repression is lifted. That logic is exactly what later papers on antibiotic susceptibility and porin regulation build on.

This paper provides the molecular explanation for several phenotypes that can otherwise look disconnected. :link-flat:`Harnessing Metabolic Regulation to Increase Hfq-Dependent Antibiotic Susceptibility in Pseudomonas aeruginosa <{filename}/blog/2018-11-09-Harnessing-Metabolic-Regulation-to-Increase-Hfq-Dependent-Antibiotic-Susceptibility-in-Pseudomonas-Aeruginosa.rst>` uses `CrcZ` to shift Hfq-dependent antibiotic susceptibility. :link-flat:`Distinctive Regulation of Carbapenem Susceptibility in Pseudomonas aeruginosa by Hfq <{filename}/blog/2020-05-26-Distinctive-Regulation-of-Carbapenem-Susceptibility-in-Pseudomonas-Aeruginosa-by-Hfq.rst>` shows that `opdP` is controlled through an `Hfq/Crc` complex while `oprD` follows a different Hfq/sRNA route. :link-flat:`Rewiring of Gene Expression in Pseudomonas aeruginosa During Diauxic Growth Reveals an Indirect Regulation of the MexGHI-OpmD Efflux Pump by Hfq <{filename}/blog/2022-06-23-Rewiring-of-Gene-Expression-in-Pseudomonas-aeruginosa-During-Diauxic-Growth-Reveals-an-Indirect-Regulation-of-the-MexGHI-OpmD-Efflux-Pump-by-Hfq.rst>` expands that logic to broader transcriptome rewiring. This 2018 NAR paper lays out the physical and biochemical basis of that regulatory architecture.

For readers interested in bacterial RNA biology more generally, the study is also notable because it gives one of the clearest examples of how an RNA chaperone can be functionally redirected by another protein. `Hfq` is often discussed mainly in the context of sRNA-mediated regulation. Here, the emphasis shifts to a different side of its biology: target-specific translational repression shaped by an interacting partner and by the availability of competing RNAs. That makes the paper both mechanistically satisfying and central to the broader `Pseudomonas` cluster.

.. frame:: Abstract

  In *Pseudomonas aeruginosa*, carbon catabolite repression depends on the RNA chaperone `Hfq`, the catabolite repression control protein `Crc`, and the regulatory RNA `CrcZ`. This study shows that `Crc` is required for full-fledged Hfq-mediated translational repression because it forms assemblies with `Hfq` and A-rich target RNAs, contacting both binding partners and stabilizing the resulting complex. The work further shows that `Crc` can interfere with sRNA binding to `Hfq`, suggesting a mechanism by which `Crc` prioritizes Hfq function toward carbon-source control during CCR.


Citation
========

  | :link-flat-strong:`Interplay Between the Catabolite Repression Control Protein Crc, Hfq and RNA in Hfq-Dependent Translational Regulation in Pseudomonas aeruginosa <https://doi.org/10.1093/nar/gkx1245>`
  | Elisabeth Sonnleitner, Alexander Wulf, Sebastien Campagne, Xue-Yuan Pei, :ul:`Michael T. Wolfinger`, Giada Forlani, Konstantin Prindl, Laetitia Abdou, Armin Resch, Frederic Allain, Ben Luisi, Henning Urlaub, Udo Blasi
  | *Nucleic Acids Res.* 46:1470-1485 (2018) | :doi:`doi:10.1093/nar/gkx1245 <https://doi.org/10.1093/nar/gkx1245>` | :link-flat:`PDF <{static}/files/papers/Sonnleitner-2018.pdf>`


See Also
========

  | :link-flat-strong:`Harnessing Metabolic Regulation to Increase Hfq-Dependent Antibiotic Susceptibility in Pseudomonas aeruginosa <{filename}/blog/2018-11-09-Harnessing-Metabolic-Regulation-to-Increase-Hfq-Dependent-Antibiotic-Susceptibility-in-Pseudomonas-Aeruginosa.rst>`
  | Petra Pusic, Elisabeth Sonnleitner, Beatrice Krennmayr, Dorothea Agnes Heitzinger, :ul:`Michael T. Wolfinger`, Armin Resch, Udo Blasi
  | *Front. Microbiol.* 9:2709 (2018) | :doi:`doi:10.3389/fmicb.2018.02709 <https://doi.org/10.3389/fmicb.2018.02709>` | :link-flat:`PDF <{static}/files/papers/Pusic-2018.pdf>`

  | :link-flat-strong:`Distinctive Regulation of Carbapenem Susceptibility in Pseudomonas aeruginosa by Hfq <{filename}/blog/2020-05-26-Distinctive-Regulation-of-Carbapenem-Susceptibility-in-Pseudomonas-Aeruginosa-by-Hfq.rst>`
  | Elisabeth Sonnleitner, Petra Pusic, :ul:`Michael T. Wolfinger`, Udo Blasi
  | *Front. Microbiol.* 11:1001 (2020) | :doi:`doi:10.3389/fmicb.2020.01001 <https://doi.org/10.3389/fmicb.2020.01001>` | :link-flat:`PDF <{static}/files/papers/Sonnleitner-2020.pdf>`

  | :link-flat-strong:`Rewiring of Gene Expression in Pseudomonas aeruginosa During Diauxic Growth Reveals an Indirect Regulation of the MexGHI-OpmD Efflux Pump by Hfq <{filename}/blog/2022-06-23-Rewiring-of-Gene-Expression-in-Pseudomonas-aeruginosa-During-Diauxic-Growth-Reveals-an-Indirect-Regulation-of-the-MexGHI-OpmD-Efflux-Pump-by-Hfq.rst>`
  | Marlena Rozner, Ella Nukarinen, :ul:`Michael T. Wolfinger`, Fabian Amman, Wolfram Weckwerth, Udo Blaesi, Elisabeth Sonnleitner
  | *Front. Microbiol.* 13:919539 (2022) | :doi:`doi:10.3389/fmicb.2022.919539 <https://doi.org/10.3389/fmicb.2022.919539>` | :link-flat:`PDF <{static}/files/papers/Rozner-2022.pdf>`
