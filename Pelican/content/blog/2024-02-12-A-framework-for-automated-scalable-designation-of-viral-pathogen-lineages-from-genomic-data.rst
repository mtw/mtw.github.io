A framework for automated scalable designation of viral pathogen lineages from genomic data
###########################################################################################

:date: 2024-02-12
:modified: 2024-04-21
:tags: virus bioinformatics; molecular epidemiology; One Health
:category: publications
:slug:
:author: mtw
:summary: Keeping pace with ever-changing viruses is a challenge. This study unveils an automated system for classifying viral lineages based on genetics, offering a faster and more objective approach
:title: Beyond Pango: The future of virus lineage classification

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

Tracking and categorizing viruses like SARS-CoV-2 effectively is crucial for scientific research and public health initiatives. Traditionally, scientists used naming conventions based on geographical locations or specific characteristics to identify variants. However, given the rapid mutations in viruses, even a single mutation can create a new lineage, complicating classification. Additionally, the vast amount of genomic data associated with viruses like SARS-CoV-2 presents challenges for existing classification methods, which often involve manual curation and crowd-sourced proposals, leading to time-consuming processes and potential biases.

To overcome these challenges, we introduce Autolin, an automated system that utilizes genetic data to classify viral lineages. This approach proves to be efficient even with extensive datasets, offering a much quicker and more objective method compared to manual curation. The prospect of analyzing and classifying rapidly evolving viruses in real-time represents a significant advancement in our ability to monitor and comprehend these pathogens.

Autolin provides several benefits over current methods. Its speed allows researchers to keep up with the fast-paced evolution of viruses, while its reliance on genetic data helps eliminate biases inherent in manual curation or crowd-sourced approaches. This objectivity is crucial for ensuring clear and consistent communication regarding viral threats. Moreover, Autolin is highly scalable and can be applied to any virus, not just SARS-CoV-2, making it invaluable for addressing future public health challenges. Additionally, Autolin offers flexibility by allowing users to integrate information about the significance of specific mutations, leading to classifications that are more relevant from an epidemiological perspective.

Although Autolin is not without limitations and requires continuous updates as new data emerges, it represents a significant advancement in our ability to monitor and understand viruses. As genomic sequencing becomes more widespread globally, automated tools like Autolin will be indispensable for effectively managing future public health crises. With faster, more impartial, and scalable virus classification, researchers and public health officials will be better equipped to confront emerging pathogens and protect public health.

.. button-primary:: {static}/files/papers/McBroome-2024.pdf

    Download PDF

.. frame:: Abstract

  Pathogen lineage nomenclature systems are a key component of effective communication and collaboration for researchers and public health workers. Since February 2021, the Pango dynamic lineage nomenclature for SARS-CoV-2 has been sustained by crowdsourced lineage proposals as new isolates were sequenced. This approach is vulnerable to time-critical delays as well as regional and personal bias. Here we developed a simple heuristic approach for dividing phylogenetic trees into lineages, including the prioritization of key mutations or genes. Our implementation is efficient on extremely large phylogenetic trees consisting of millions of sequences and produces similar results to existing manually curated lineage designations when applied to SARS-CoV-2 and other viruses including chikungunya virus, Venezuelan equine encephalitis virus complex and Zika virus. This method offers a simple, automated and consistent approach to pathogen nomenclature that can assist researchers in developing and maintaining phylogeny-based classifications in the face of ever-increasing genomic datasets.



Citation
========

  | :link-flat-strong:`A framework for automated scalable designation of viral pathogen lineages from genomic data <https://doi.org/doi:10.1038/s41564-023-01587-5>`
  | Jakob McBroome, Adriano de Bernardi Schneider, Cornelius Roemer, :ul:`Michael T. Wolfinger`, Angie S. Hinrichs, Aine N. O’Toole, Chris Ruis, Yatish Turakhia, Andrew Rambaut, and Russell Corbett-Detig
  | *Nature Microbiol.*  9:550–560 (2024) | :doi:`doi:10.1038/s41564-023-01587-5 <https://doi.org/doi:10.1038/s41564-023-01587-5>` | :link-flat:`PDF <{static}/files/papers/McBroome-2024.pdf>`
