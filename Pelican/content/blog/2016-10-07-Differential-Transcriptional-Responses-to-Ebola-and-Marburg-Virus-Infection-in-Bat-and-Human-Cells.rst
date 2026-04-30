Why bats and humans respond differently to filovirus infection
##############################################################

:date: 2016-10-07
:modified: 2026-04-30
:tags: virology; virus bioinformatics
:category: publications
:slug: Differential-Transcriptional-Responses-to-Ebola-and-Marburg-Virus-Infection-in-Bat-and-Human-Cells
:author: mtw
:summary: This paper compares Ebola and Marburg virus infection in bat and human cells and shows that the transcriptional response, pathway activation, and replication dynamics differ substantially between the natural host and a susceptible human system.
:title: Why bats and humans respond differently to filovirus infection
:description: A comparative transcriptomics study of Ebola and Marburg virus infection in bat and human cells, focusing on replication kinetics, host-response pathways, and candidate determinants of tolerance.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

This paper addresses one of the most important biological contrasts in filovirus research. Ebola and Marburg viruses cause severe, often fatal disease in humans, yet bats are thought to serve as natural hosts without showing the same destructive pathology. That difference is not just an ecological curiosity. It points to a host-response problem: what do bat cells do differently, and what does the human cell response look like when infection becomes damaging instead of tolerated?

The study approaches that question through comparative transcriptomics. Human `HuH7` cells and bat `R06E-J` cells were infected with either Ebola virus or Marburg virus, and RNA-seq profiles were collected across several time points representing early, intermediate, and later phases of the infection cycle. That design matters because host response is dynamic. A single endpoint would blur together primary responses, downstream stress programs, and viral amplification effects. By sampling the time course, the paper can distinguish faster from slower trajectories and compare how two related filoviruses reshape host transcription in two very different cellular backgrounds.

One of the clearest results is kinetic. Filovirus replication proceeds more rapidly in the human cells than in the bat cells. That observation already hints at a mechanistic difference in permissiveness or control. The transcriptomic analysis then shows that the infected cells do not simply differ in the magnitude of a common response. They differ in which genes, motifs, and pathways become most strongly engaged. Among the most prominent regulated classes are chemokine ligands and transcription factors, indicating that immune signaling and regulatory rewiring are central features of the infection response.

The pathway-level results are especially useful. The paper reports strong activation of the `JAK/STAT` axis, induction of several dual-specificity phosphatases (`DUSP` genes) linked to MAP kinase regulation, and upregulation of `PPP1R15A`, a marker connected to endoplasmic-reticulum stress and stress-induced cell-death programs. That combination is informative because it suggests that the host response is not only antiviral in a narrow sense. It also involves broader stress adaptation and signaling-control modules that may shape whether infection remains contained or progresses toward pathology.

Another important contribution is infrastructural rather than purely biological. At the time, the transcriptional response of bat cells to filovirus infection had not been characterized in comparable depth, and even the human-cell picture was incomplete. The study therefore had to do more than differential-expression testing alone. It also established a transcriptomic resource, including de novo assembly work for the bat system, to make cross-species comparison possible. That resource-building aspect is easy to miss, but it is a major reason why the paper has remained useful.

What makes the study compelling is that it treats the bat-human contrast as a systems-level problem. The question is not reduced to one receptor, one interferon gene, or one viral antagonist. Instead, the authors look at coordinated host programs: transcription factors, activity motifs, pathways, and infection-stage-dependent responses. That is the right scale for a problem where tolerance likely emerges from network behavior rather than a single switch.

Seen from today’s perspective, the paper also illustrates an approach that has only become more important: using comparative host transcriptomics to identify candidate cellular states associated with tolerance, resilience, or severe disease. In that sense, this is not just a filovirus paper. It is part of a broader shift toward understanding infection through host regulatory landscapes rather than viral replication alone.

The article stands apart from structure-centered virology because it shows a different register of virus bioinformatics: large-scale RNA-seq analysis, de novo transcriptome reconstruction, pathway interpretation, and cross-species comparison. That broader systems perspective matters because host response, viral evolution, and structured RNA biology often end up informing one another even when the immediate question is different.

.. frame:: Abstract

  This study compares the transcriptional responses of bat and human cells infected with Ebola virus or Marburg virus across multiple time points. It shows that filovirus replication is faster in human cells and identifies strong regulation of chemokine ligands, transcription factors, the `JAK/STAT` pathway, MAP kinase inhibitors such as the `DUSP` genes, and the stress-associated factor `PPP1R15A`. By combining comparative RNA-seq with bat transcriptome reconstruction, the work provides a resource for understanding how natural host cells may tolerate filovirus infection while human cells progress toward a more pathogenic response.


Citation
========

  | :link-flat-strong:`Differential Transcriptional Responses to Ebola and Marburg Virus Infection in Bat and Human Cells <https://doi.org/10.1038/srep34589>`
  | Martin Hölzer, Verena Krähling, Fabian Amman, Emanuel Barth, Stephan H. Bernhart, Victor Carmelo, Maximilian Collatz, Gero Doose, Florian Eggenhofer, Jan Ewald, Jörg Fallmann, Lasse M. Feldhahn, Markus Fricke, Juliane Gebauer, Andreas J. Gruber, Franziska Hufsky, Henrike Indrischek, Sabina Kanton, Jörg Linde, Nelly Mostajo, Roman Ochsenreiter, Konstantin Riege, Lorena Rivarola-Duarte, Abdullah H. Sahyoun, Sita J. Saunders, Stefan E. Seemann, Andrea Tanzer, Bertram Vogel, Stefanie Wehner, :ul:`Michael T. Wolfinger`, Rolf Backofen, Jan Gorodkin, Ivo Grosse, Ivo L. Hofacker, Steve Hoffmann, Christoph Kaleta, Peter F. Stadler, Stephan Becker, Manja Marz
  | *Sci. Rep.* 6:34589 (2016) | :doi:`doi:10.1038/srep34589 <https://doi.org/10.1038/srep34589>` | :link-flat:`PDF <{static}/files/papers/Holzer-2016.pdf>`
