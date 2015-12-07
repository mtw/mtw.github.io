---
layout: post
title: "How to compute normalized RNA-seq expression from multicov files"
date: 2014-04-15 00:29:51 +0200
comments: true
categories: [rna-seq, ViennaNGS]
---

Whenever it comes to analyzing RNA-seq experiments, there is a need for
comparing expression data at a quantitative level. Consider a scenario
where samples were taken from different conditions and subjected to
Illumina sequencing. Whether those samples were multiplexed or sequenced on
a single lane each, one generally gets a different number of raw reads from
each sample, refelcting experimental and technical biases inherent in the
RNA-seq protocols. Various measures for normalization of RNA-seq samples
have been proposed, the most widely used being RPKM (reads per kilobase per
million). While RPKM tries to account for different sequencing depth by
normalizing by the number of reads sequenced in a specific sample, divided
by 10^6, this very step causes a systematic bias, as has been shown
recently (see [Wagner et al.,Theory Biosci
(2012);131(4):281-5.](http://dx.doi.org/10.1007/s12064-012-0162-3) and [Li
et al.,Bioinformatics
(2010);26(4):493-500](http://dx.doi.org/10.1093/bioinformatics/btp692)).

The central point of these papers is to work out an alternative measure for
RNA-seq expression abundance that resembles as closely as possible the
*relative molar concentraction* (rmc) of each RNA species present in a
sample. It is easy to see that the average rmc across genes has to be a
constant that only depends on the number of genes mapped in an RNA-seq
experiment.

One example of measures that fulfills the invariant average criterion is
*Transcript per million* (TPM), being defined as
 {% img center /images/TPM_1.png %}
where t_g is a proxy for the number of transcripts that can be explained by
a certain number of mapped reads and T is the sum of all t_g over all
genes. If one is interested in mRNA abundance, the  average TPM - and thus
the average rmc is inversely proportional to the number of features
present in a reference annotation.

Practically, TPM values for individual genes can be computed from read
count tables, ie. tables that give the number of reads overlapping a
specific gene. Typical programs for obtaining read count tables are
[htseq-count](http://www-huber.embl.de/users/anders/HTSeq/doc/count.html)
or
[multiBamCov](http://bedtools.readthedocs.org/en/latest/content/tools/multicov.html)
([bedtools](http://bedtools.readthedocs.org/en/latest/index.html)
multicov).

I have recently implemented
[normalize_multicov.pl](https://github.com/mtw/ViennaNGS/blob/master/scripts/normalize_multicov.pl),
a tool for computing normalized RNA-seq expression in terms of TPM from
multicov files. It is part of the
[ViennaNGS](https://github.com/mtw/ViennaNGS) Perl Modules for NGS analysis
and very easy to use: Just provide it the output of a bedtols multicov run
on your data as well as the read length used for sequencing your samples
and get back a normalized multicov file of your samples in terms of
TPM. That's all ...
