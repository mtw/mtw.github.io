Pan-flavivirus analysis reveals sfRNA-independent 3' UTR-biased siRNA production from an insect-specific flavivirus
###################################################################################################################

:date: 2024-10-15
:modified: 2024-10-31
:tags: virus bioinformatics; xrRNA; flavivirus; virology
:category: publications
:slug: pan-flavivirus-sirna-production-in-insect-specific-flavivirus
:author: mtw
:summary: A comparative analysis of vsiRNA profiles across insect-specific flaviviruses reveals unusually strong 3' UTR-biased siRNA production that is independent of sfRNA formation.
:title: 3' UTR-biased siRNA production in an insect-specific flavivirus
:description: This study uncovers a distinctive siRNA response in Kamiti River virus, an insect-specific flavivirus that has a particularly long structured 3'UTR

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

  .. figure:: {static}/files/papers/preview/Preview__Besson-2024.001small.webp
    :alt: 3UTR of KRV, CFAV, and CxFV
    :figclass: m-figure m-flat

Mosquito antiviral immunity is dominated by RNA interference, so the distribution of viral siRNAs can be read as a footprint of how the host sees and processes viral RNA. In many flaviviruses, that footprint is fairly diffuse across the genome. This paper starts from the question of whether that is a general rule or whether different flavivirus groups leave different small-RNA signatures in mosquito cells. The answer is that most flaviviruses do behave broadly as expected, but classical insect-specific flaviviruses stand out sharply, and Kamiti River virus stands out even within that subset.

The main comparative result is the unusually strong 3' UTR bias of vsiRNA production in KRV. More than 95% of KRV-derived vsiRNAs map to the 3' UTR, which is remarkable both because of the scale of the enrichment and because KRV carries an unusually long, highly structured 3' UTR of roughly 1.2 kb. That immediately suggests that the structured non-coding end of the genome is not just a passive repository of regulatory motifs. It appears to dominate how the mosquito RNAi machinery encounters the virus.

That would already be interesting on its own, but the paper becomes much more compelling when it asks whether the obvious candidate explanation is actually correct. Because flavivirus 3' UTRs produce sfRNAs through XRN1 stalling at structured xrRNA elements, it would be easy to assume that the strong vsiRNA signal simply reflects abundant sfRNA production. In other words, one might expect the siRNAs to be coming from the same structured decay intermediates that are already familiar from flavivirus RNA biology.

The experiments show that this explanation is incomplete. For KRV, two major sfRNAs were mapped to predicted XRN1-resistant elements in the 3' UTR, and both species were abundant enough to be clear candidates for shaping the small-RNA profile. But when sfRNA production was reduced in Pacman-deficient mosquito cells, the 3' UTR-biased siRNA pattern did not collapse accordingly. That is the key result of the paper. The striking siRNA enrichment and the presence of sfRNAs coincide in the same region, yet the former does not depend on the latter in any simple causal way.

Methodologically, that is an important distinction. It means the 3' UTR signal cannot be explained away as a trivial by-product of one already known pathway. Biologically, it suggests that KRV or related classical insect-specific flaviviruses generate another RNA species, or another structural context, that is especially accessible to the mosquito RNAi machinery. The 3' UTR may therefore act less like a conventional protected fragment and more like a structured decoy or processing hotspot that redirects the antiviral response.

This fits well with a broader line of work on conserved RNA elements in flavivirus untranslated regions. The paper naturally connects to :link-flat:`the comparative analysis of flavivirus 3' UTR architectures <{filename}/blog/2019-03-24-Functional_RNA_Structures_in_the_3UTR_of_Tick-Borne_Insect-Specific_and_No_Known_Vector_Flaviviruses.rst>`, to the later :link-flat:`mosquito-borne flavivirus 3' UTR synthesis <{filename}/blog/2021-09-06-Functional-RNA-structures-in-the-3UTR-of-MBFV.rst>`, and to studies such as :link-flat:`the Zambia insect-specific flavivirus xrRNA paper <{filename}/blog/2020-09-14-Discoveries-of-Exoribonuclease-Resistant-Structures-of-Insect-Specific-Flaviviruses-Isolated-in-Zambia.rst>`. Those papers established that structured 3' UTRs are central to flavivirus evolution and host interaction. This study adds a new layer by showing that the same region can also dominate mosquito siRNA production in a way that is not simply reducible to sfRNA biogenesis.

For insect-specific flaviviruses, that makes the result especially valuable. These viruses offer a setting in which mosquito-virus interactions can be studied without the vertebrate half of the arbovirus cycle complicating the picture. KRV therefore becomes more than an odd small-RNA outlier. It becomes a model for asking how structured viral RNAs shape, divert, or absorb antiviral RNAi in arthropod hosts.

..
.. frame:: Abstract

  RNA interference (RNAi) plays an essential role in mosquito antiviral immunity, but it is not known whether viral small interfering RNA (siRNA) profiles differ between mosquito-borne and mosquito-specific viruses. A pan-Orthoflavivirus analysisin Aedes albopictus cells revealed that viral siRNAs were evenly distributed across the viral genome of most representatives of the Flavivirus genus. In contrast, siRNA production was biased toward the 3' untranslated region (UTR) of the genomes of classical insect-specific flaviviruses (cISF), which was most pronounced for Kamiti River virus (KRV), a virus with a unique, 1.2 kb long 3' UTR. KRV-derived siRNAs were produced in high quantities and almost exclusively mapped to the 3' UTR. We mapped the 5' end of KRV subgenomic flavivirus RNAs (sfRNAs), products of the 5'−3' exoribonuclease XRN1/Pacman stalling on secondary RNA structures in the 3' UTR of the viral genome. We found that KRV produces high copy numbers of a long, 1,017 nt sfRNA1 and a short, 421 nt sfRNA2, corresponding to two predicted XRN1-resistant elements. Expression of both sfRNA1 and sfRNA2 was reduced in Pacman-deficient Aedes albopictus cells; however, this did not correlate with a shift in viral siRNA profiles. We suggest that cISFs, particularly KRV, developed a unique mechanism to produce high amounts of siRNAs as a decoy for the antiviral RNAi response in an sfRNA-independent manner.

Citation
========

  | :link-flat-strong:`Pan-flavivirus analysis reveals sfRNA-independent, 3’UTR-biased siRNA production from an Insect-Specific Flavivirus <{filename}/blog/2024-10-15-Pan-flavivirus-analysis-reveals-sfRNA-independent-3-UTR-biased-siRNA-production-from-an-insect-specific-flavivirus.rst>`
  | Benoit Besson, Gijs J. Overheul, :ul:`Michael T. Wolfinger`, Sandra Junglen, Ronald P. van Rij
  | *J. Virol.* e01215-24 (2024) | :doi:`doi:10.1128/jvi.01215-24 <https://doi.org/10.1128/jvi.01215-24>` | :link-flat:`Preprint PDF <{static}/files/papers/Besson-2024__PREPRINT.pdf>`
