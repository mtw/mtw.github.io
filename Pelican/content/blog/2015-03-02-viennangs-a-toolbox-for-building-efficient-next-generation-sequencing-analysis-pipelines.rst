ViennaNGS: A toolbox for building efficient next-generation sequencing analysis pipelines
#########################################################################################

:date: 2015-03-02
:modified: 2026-04-24
:tags: NGS; tools
:category: publications
:slug: ViennaNGS-a-toolbox-for-building-efficient-next-generation-sequencing-analysis-pipelines
:author: mtw
:title: Building efficient NGS analysis pipelines with ViennaNGS
:summary: ViennaNGS is a modular toolbox for building reproducible NGS analysis workflows, combining Perl library code, utility scripts, and browser-oriented data-export components for early high-throughput genomics pipelines.
:description: A modular Perl toolbox for next-generation sequencing analysis, designed to make custom NGS pipelines easier to build, reuse, and reproduce.

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

.. container:: m-col-t-10 m-center-t m-col-s-10 m-center-s m-col-m-6 m-right-m

   .. figure:: {static}/files/papers/preview/Preview__Wolfinger-2015.001small.webp
          :alt: Representative ViennaNGS utilities and tutorial resource requirements from the paper
          :figclass: m-figure m-flat

In the early years of NGS bioinformatics, many analyses were still held together by ad hoc lab scripts. That worked for one project at a time, but it did not scale well: code was hard to reuse, pipelines were difficult to document, and routine file-format handling often had to be reimplemented over and over again. ViennaNGS grew out of that environment. The goal was not to offer yet another one-click analysis suite, but to provide reusable building blocks for people who needed to assemble their own workflows.

That distinction matters. ViennaNGS is not a fixed pipeline in the narrow sense. It is a toolbox: a collection of Perl modules and utility scripts intended to support the development of custom next-generation sequencing workflows. In practical terms, that meant exposing common operations as reusable library code while also shipping command-line utilities that served as both reference implementations and ready-to-use helpers for everyday tasks.

The scope of the package reflects the pain points of early NGS data analysis. ViennaNGS included support for feature extraction and format conversion across common genomics file types, mapping statistics, expression quantification and normalization, splice-junction analysis, motif-data handling, and the automated construction of Assembly and Track Hubs for the UCSC genome browser. It also wrapped widely used command-line tools, which helped make larger pipelines less repetitive and easier to script consistently.

What I still like about this paper is that it treats software architecture as a scientific problem rather than an afterthought. The key issue was not only whether one could write a script for a given analysis step, but whether that step could be turned into a reusable, composable module that fit into a larger workflow. That is a very different mindset from publishing a single-purpose utility. It is closer to infrastructure design, and that is why the project remained useful after specific assays or preferred file formats evolved.

The paper also pays attention to usability in a way that was easy to overlook at the time. ViennaNGS was distributed through familiar community channels, including GitHub and CPAN, and it came with tutorials that demonstrated real pipeline construction rather than isolated API calls. That may sound mundane, but it was important. For many academic bioinformatics tools, the bottleneck is not raw capability; it is whether anyone besides the original author can actually deploy the software in a real analysis environment.

From a present-day perspective, ViennaNGS belongs to an earlier generation of workflow engineering, before systems like Snakemake or Nextflow became default answers for many users. But that does not make the underlying ideas obsolete. The need for modularity, explicit file-format handling, reusable wrappers, and browser-ready outputs has not gone away. If anything, the paper reads as a snapshot of a period when the field was still learning how much of NGS bioinformatics depended on software organization rather than on any one algorithm.

The project was especially useful in research settings where workflows had to remain flexible. Not every NGS problem fits a canned pipeline, and many biologically interesting questions still require custom combinations of standard processing steps. ViennaNGS tried to make that custom work less brittle by packaging recurring operations into a coherent toolbox. That is the reason I think it still deserves attention: it addressed the engineering layer of genomics analysis at a time when that layer was often neglected.

The ViennaNGS suite is available through :link-flat:`GitHub <https://github.com/mtw/Bio-ViennaNGS>` and :link-flat:`CPAN <https://metacpan.org/dist/Bio-ViennaNGS>`.

.. frame:: Abstract

  Recent achievements in next-generation sequencing (NGS) technologies lead to a high demand for reuseable software components to easily compile customized analysis workflows for big genomics data. We present ViennaNGS, an integrated collection of Perl modules focused on building efficient pipelines for NGS data processing. It comes with functionality for extracting and converting features from common NGS file formats, computation and evaluation of read mapping statistics, as well as normalization of RNA abundance. Moreover, ViennaNGS provides software components for identification and characterization of splice junctions from RNA-seq data, parsing and condensing sequence motif data, automated construction of Assembly and Track Hubs for the UCSC genome browser, as well as wrapper routines for a set of commonly used NGS command line tools.

Citation
========

  | :link-flat-strong:`ViennaNGS: A toolbox for building efficient next-generation sequencing analysis pipelines <https://doi.org/10.12688/f1000research.6157.2>`
  | Michael T. Wolfinger, Jörg Fallmann, Florian Eggenhofer, Fabian Amman
  | *F1000Research* 4:50 (2015) | :doi:`doi: 10.12688/f1000research.6157.2 <https://doi.org/10.12688/f1000research.6157.2>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2015.pdf>`
