A framework for automated scalable designation of viral pathogen lineages from genomic data
###########################################################################################

:date: 2024-02-12
:modified: 2026-04-23
:tags: virus bioinformatics; new method; tools; molecular epidemiology; One Health
:category: publications
:slug:
:author: mtw
:summary: This study describes an automated framework for lineage designation from phylogenetic and genomic data, designed to scale to very large viral datasets while remaining consistent and interpretable.
:title: Automated lineage designation from viral genomic data
:description: A scalable framework for automated viral lineage designation from genomic and phylogenetic data.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

  .. figure:: {static}/files/papers/preview/Preview__McBroome-2024.001small.webp
        :alt: Automated lineage designation of Venezuelan Equine Encephalitis complex viruses
        :figclass: m-figure m-flat

Lineage designation is partly a biological question and partly an information-management problem. Once viral sequencing reaches very large scale, as it did for SARS-CoV-2, manual or community-curated naming systems become increasingly difficult to maintain. Delays accumulate, criteria become harder to apply consistently, and the workload grows faster than the nomenclature process can keep up.

This study presents Autolin, a heuristic framework for automated lineage designation from phylogenetic and genomic data. The main contribution is not a claim that expert curation should disappear, but that a simple and explicit rule-based system can produce lineage assignments at a scale that is difficult to sustain manually.

That matters because lineage systems are only useful when they are both interpretable and sustainable. An automated framework can evaluate very large trees, apply the same criteria repeatedly, and generate designations without depending on ad hoc proposal cycles. In practice, that means faster turnaround and more consistent behavior across datasets with millions of sequences.

Another useful feature of the framework is that it allows prioritization of particular mutations or genes. That makes the method flexible enough to reflect biological or epidemiological priorities rather than treating all sequence variation as equally informative. In other words, the system is not just scalable; it can also be tuned to highlight the parts of a genome that matter most for a given pathogen or surveillance context.

The paper is careful about scope. Automated lineage designation is not the same thing as biological interpretation, and no heuristic can remove the need for expert judgment altogether. What it can do is provide a consistent baseline classification system that remains usable as genomic datasets continue to grow. The fact that the method produces lineage partitions similar to existing curated systems across multiple viruses makes that claim much more credible.

For genomic epidemiology, this is the real value of the framework. It gives researchers a practical way to maintain phylogeny-based nomenclature under conditions where purely manual designation becomes increasingly fragile. That is useful not only for SARS-CoV-2, but also for other rapidly sampled viral systems where scale has already become the defining constraint.

.. raw:: html

  <object data="{static}/files/papers/McBroome-2024.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/McBroome-2024.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

  Pathogen lineage nomenclature systems are a key component of effective communication and collaboration for researchers and public health workers. Since February 2021, the Pango dynamic lineage nomenclature for SARS-CoV-2 has been sustained by crowdsourced lineage proposals as new isolates were sequenced. This approach is vulnerable to time-critical delays as well as regional and personal bias. Here we developed a simple heuristic approach for dividing phylogenetic trees into lineages, including the prioritization of key mutations or genes. Our implementation is efficient on extremely large phylogenetic trees consisting of millions of sequences and produces similar results to existing manually curated lineage designations when applied to SARS-CoV-2 and other viruses including chikungunya virus, Venezuelan equine encephalitis virus complex and Zika virus. This method offers a simple, automated and consistent approach to pathogen nomenclature that can assist researchers in developing and maintaining phylogeny-based classifications in the face of ever-increasing genomic datasets.

Citation
========

  | :link-flat-strong:`A framework for automated scalable designation of viral pathogen lineages from genomic data <https://doi.org/10.1038/s41564-023-01587-5>`
  | Jakob McBroome, Adriano de Bernardi Schneider, Cornelius Roemer, :ul:`Michael T. Wolfinger`, Angie S. Hinrichs, Aine N. O’Toole, Chris Ruis, Yatish Turakhia, Andrew Rambaut, and Russell Corbett-Detig
  | *Nature Microbiol.*  9:550–560 (2024) | :doi:`doi:10.1038/s41564-023-01587-5 <https://doi.org/10.1038/s41564-023-01587-5>` | :link-flat:`PDF <{static}/files/papers/McBroome-2024.pdf>`
