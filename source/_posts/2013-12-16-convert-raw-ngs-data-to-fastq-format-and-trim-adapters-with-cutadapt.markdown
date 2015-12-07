---
layout: post
title: "Convert raw NGS data to fastq format and trim adapters with cutadapt"
date: 2013-12-16 22:46:06 +0100
comments: true
categories: rna-seq
---
Raw next-generation-sequencing (NGS) data is often shipped in unaligned BAM format, whereas most mappers expect input data in FASTQ format. I've written a little bash script that does the preprocessing job for paired-end data: Convert raw reads to FASTQ with [bam2fastq](http://www.hudsonalpha.org/gsl/information/software/bam2fastq), trim adapters with [cutadapt](http://code.google.com/p/cutadapt/) and perform quality control checks with [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/).

{% gist 7989028 bam2fastq_cutadapt.sh %}
