---
layout: post 
title: "SHAPE directed RNA folding" 
date: 2015-09-02 15:13:03 
categories: [RNA structure, publications] 
--- 

With the advent of efficient strategies for experimental RNA structure
validation, especially combination of chemical probing with next-generation
sequencing technologies, came demand to couple experimental data,
e.g. SHAPE reactivities, with in silico RNA structure prediction tools. In
this line, the computational structure prediction is guided by in vitro or
even in vivo probing data.

We have recently implemented three previously published methods for
incorporation of SHAPE probing data into the *Vienna RNA Package* and
benchmarked prediction results with a set of RNAs with known reference
structures.

Don't miss the [Supplementary
Data](http://bioinformatics.oxfordjournals.org/content/early/2015/09/23/bioinformatics.btv523/suppl/DC1)
since it contains extensive coverage of the applied benchmark strategies
and lots of background information.

[__SHAPE directed RNA folding__](http://bioinformatics.oxfordjournals.org/content/early/2015/09/23/bioinformatics.btv523.abstract)  
*Ronny Lorenz, Dominik Luntzer, Ivo L. Hofacker, Peter F. Stadler, Michael T. Wolfinger*   
Bioinformatics 2015 btv523  
[DOI: 10.1093/bioinformatics/btv523](http://dx.doi.org/10.1093/bioinformatics/btv523)

## Abstract

> Summary: Chemical mapping experiments allow for nucleotide resolution
  assessment of RNA structure. We demonstrate that different strategies of
  integrating probing data with thermodynamics-based RNA secondary
  structure prediction algorithms can be implemented by means of soft
  constraints. This amounts to incorporating suitable pseudo-energies into
  the standard energy model for RNA secondary structures. As a showcase
  application for this new feature of the ViennaRNA Package we compare
  three distinct, previously published strategies to utilize SHAPE
  reactivities for structure prediction. The new tool is benchmarked on a
  set of RNAs with known reference structure.

> Availability and implementation: The capability for SHAPE directed RNA
  folding is part of the upcoming release of the ViennaRNA Package 2.2, for
  which a preliminary release is already freely available at
  [http://www.tbi.univie.ac.at/RNA](http://www.tbi.univie.ac.at/RNA).
