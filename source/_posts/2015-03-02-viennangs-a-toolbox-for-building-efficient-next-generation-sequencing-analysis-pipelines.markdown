---
layout: post
title: "ViennaNGS: A toolbox for building efficient next-generation sequencing analysis pipelines"
date: 2015-03-02 21:58:01 +0100
comments: true
categories: [rna-seq, ViennaNGS]
---
__ViennaNGS__  is a Perl distribution for building efficient NGS data and
analysis pipelines, integrating high-level routines and wrapper functions for
common NGS processing tasks. While ViennaNGS is not an established pipeline per
se, it provides tools and functionality for the development of custom NGS
pipelines in Perl. ViennaNGS comes with a set of utility scripts that serve as
reference implementation for most library functions and can readily be applied
for specific tasks or integrated as-is into custom pipelines.

ViennaNGS covers a broad range of NGS data processing tasks, including
functionality for extracting and converting features from common NGS file
formats, computation and evaluation of read mapping statistics, quantification
and normalization of read count data, identification and characterization of
splice junctions from RNA-seq data, parsing and condensing sequence motif data,
automated construction of Assembly and Track Hubs for the UCSC genome browser
and wrapper routines for a set of commonly used NGS command line tools.


We have recently published the __ViennaNGS__ paper at F1000Research:

[__ViennaNGS: A toolbox for building efficient next-generation sequencing
analysis pipelines__](http://f1000research.com/articles/4-50)  
*Michael T. Wolfinger, Jörg Fallmann, Florian Eggenhofer, Fabian Amman*  
F1000Research 2015,4:50  
[DOI: 10.12688/f1000research.6157.1](http://dx.doi.org/10.12688/f1000research.6157.1)

The ViennaNGS suite is available through Github
(https://github.com/mtw/Bio-ViennaNGS) and CPAN
(http://search.cpan.org/dist/Bio-ViennaNGS). 
