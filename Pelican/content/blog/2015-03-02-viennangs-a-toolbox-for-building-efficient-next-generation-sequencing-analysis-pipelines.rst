ViennaNGS: A toolbox for building efficient next-generation sequencing analysis pipelines
#########################################################################################

:date: 2015-03-02
:modified: 2022-10-14
:tags: NGS; tools
:category: publications
:slug: ViennaNGS-a-toolbox-for-building-efficient-next-generation-sequencing-analysis-pipelines
:author: mtw
:title: Building efficient NGS analysis pipelines with ViennaNGS
:summary: ViennaNGS is a workflow system for building efficient NGS data analysis pipelines, integrating high-level routines and wrapper functions for common NGS processing tasks
:description: ViennaNGS is collection of utilities and Perl modules for next-generation sequencing (NGS) data analysis

.. role:: link-flat-strong(link)
  :class: m-flat m-text m-strong

.. role:: link-flat(link)
  :class: m-flat m-text

.. role:: ul
  :class: m-text m-ul

.. role:: doi(link)
  :class: doi

While *ViennaNGS* is not an established pipeline per
se, it provides tools and functionality for the development of custom NGS
pipelines in Perl. *ViennaNGS* comes with a set of utility scripts that serve as
reference implementation for most library functions and can readily be applied
for specific tasks or integrated as-is into custom pipelines.

*ViennaNGS* covers a broad range of NGS data processing tasks, including
functionality for extracting and converting features from common NGS file
formats, computation and evaluation of read mapping statistics, quantification
and normalization of read count data, identification and characterization of
splice junctions from RNA-seq data, parsing and condensing sequence motif data,
automated construction of Assembly and Track Hubs for the UCSC genome browser
and wrapper routines for a set of commonly used NGS command line tools.

The ViennaNGS suite is available through :link-flat:`Github <https://github.com/mtw/Bio-ViennaNGS>` and :link-flat:`CPAN <https://metacpan.org/dist/Bio-ViennaNGS>`.

.. raw:: html

  <object data="{static}/files/papers/Wolfinger-2015.pdf" type="application/pdf" width="100%" height="1050px">
  <p>Your browser does not support PDFs. 
     <a href="{static}/files/papers/Wolfinger-2015.pdf">Download the PDF</a>
  </p>
  </object> <br/><br/>

.. frame:: Abstract

  Recent achievements in next-generation sequencing (NGS) technologies lead to a high demand for reuseable software components to easily compile customized analysis workflows for big genomics data. We present ViennaNGS, an integrated collection of Perl modules focused on building efficient pipelines for NGS data processing. It comes with functionality for extracting and converting features from common NGS file formats, computation and evaluation of read mapping statistics, as well as normalization of RNA abundance. Moreover, ViennaNGS provides software components for identification and characterization of splice junctions from RNA-seq data, parsing and condensing sequence motif data, automated construction of Assembly and Track Hubs for the UCSC genome browser, as well as wrapper routines for a set of commonly used NGS command line tools.

Citation
========

  | :link-flat-strong:`ViennaNGS: A toolbox for building efficient next-generation sequencing analysis pipelines <https://doi.org/10.12688/f1000research.6157.2>`
  | Michael T. Wolfinger, Jörg Fallmann, Florian Eggenhofer, Fabian Amman
  | *F1000Research* 4:50 (2015) | :doi:`doi: 10.12688/f1000research.6157.2 <https://doi.org/10.12688/f1000research.6157.2>` | :link-flat:`PDF <{static}/files/papers/Wolfinger-2015.pdf>`
