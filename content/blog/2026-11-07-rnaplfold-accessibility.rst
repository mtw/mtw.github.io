RNAplfold tutorial: accessibility and opening energy on long RNAs
#################################################################

:date: 2026-11-07
:tags: ViennaRNA; RNA structure prediction; flavivirus; tools
:category: howto
:section: guides
:bridge: rna
:slug: rnaplfold-accessibility
:feedback: guide
:title: RNAplfold tutorial: accessibility in long RNAs
:summary: How to compute the accessibility of a region with RNAplfold in the ViennaRNA Package, i.e. the probability that a stretch of nucleotides is unpaired, how to read the _lunp file, how to choose the right maximum base pair span and the window size, and how far the accessibility of a region changes when it is cut out of its sequence context. Worked example with the Zika virus genome, all commands included.
:description: How to compute RNA accessibility with RNAplfold: unpaired probabilities, the _lunp file, choosing span and window, and the border effect at sequence ends.
:social_image: {static}/static/og-rnaplfold-accessibility-1200x630.png

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   :link-flat:`ViennaRNA in practice <{filename}/rna-structure-prediction.rst>`, a series of tutorials. :link-flat:`RNAfold tutorial <{filename}/blog/2026-10-28-rnafold-in-practice.rst>` · :link-flat:`SHAPE and chemical probing data <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>` · RNAplfold and accessibility (this post)

Whenever an oligonucleotide has to find its target in a longer RNA, whether it is an
siRNA, an antisense oligo, a probe or a miRNA seed match, the sequence of the target site
is only half of the question. The other half is whether the site is accessible, because a
region that is locked inside a helix most of the time cannot be bound without opening that
helix first, and the energy for that has to come from somewhere.
:link-flat:`RNAplfold <https://viennarna.readthedocs.io/en/latest/man/RNAplfold.html>` in
the :link-flat:`ViennaRNA Package <{filename}/glossary.rst#viennarna>` addresses this question.
It reports, for every position and for every stretch up to a chosen length, the probability
that the region is unpaired. This quantity is typically called accessibility.

The two earlier tutorials in this series fold a tRNA, because they are about what a program
returns when a sequence is folded as a whole. RNAplfold is for the opposite case, it can be
used on a long RNA sequence such as a transcript, a viral genome, or a chromosome. On a short non-coding RNA there is
nothing for the program to average over, the whole molecule lies within one window, and
what comes back is a global folding with artefacts at both ends. The example used in this tutorial is
therefore a real genome. Every command was run with ViennaRNA 2.7.2, and
every number quoted comes from that run.

The example sequence
--------------------

The Zika virus reference genome, 10,794 nucleotides, with one open reading frame from 107
to 10,366 and therefore a 3' untranslated region from 10,367 to the end. That region
carries the
:link-flat:`exoribonuclease-resistant structures and the other functional elements of a flavivirus 3' UTR <{filename}/flavivirus-rna-structures.rst>`,
which makes it a reasonable place to ask where an oligo could bind.

.. code-block:: bash

   efetch -db nuccore -id NC_012532.1 -format fasta > zika.fa

Any other route to the same accession does as well. What matters is that the sequence is
complete, without truncations on either end.

What RNAplfold computes, and the two options that decide it
-----------------------------------------------------------

RNAfold folds the whole sequence at once. RNAplfold slides a window along the sequence,
folds each window, and averages the result over all windows that contain a given pair or
region. Two options control this, and both have to be set deliberately:

- ``-L`` (``--span``) is the largest separation a base pair may have.
- ``-W`` (``--winsize``) is the size of the averaging window, 70 by default. When ``-L`` is
  not given it takes the value of ``-W``, which is worth knowing, because a plain
  ``-W 70`` silently forbids every pair spanning more than 70 nucleotides.

`Lange et al. <https://doi.org/10.1093/nar/gks181>`_ (*Nucleic Acids Res.* 40:5215–26,
2012) tested these parameters against transcriptome-wide enzymatic probing data and a
curated set of regulatory elements. Local folding came out more accurate than global
folding, with a span of 150 balancing the number of correctly predicted pairs versus the damage
done by spurious long-range pairs. The error at sequence ends shrank when the window
was set clearly larger than the span, which gives a defensible starting point:

.. code-block:: bash

   RNAplfold -W 300 -L 150 -u 10 < zika.fa

``-u`` is the longest stretch for which the unpaired probability is computed, with
a default value of 31. This includes all shorter stretches, which are computed for free.
The run takes about twenty seconds for this genome and writes ``zika_dp.ps``, a dot plot of the local pair
probabilities, and ``zika_lunp``, which holds the accessibility.

Reading the _lunp file
----------------------

.. code-block:: text

   #unpaired probabilities
    #i$	l=1	2	3	4	5	6	7	8	9	10
   1	0.9836767	NA	NA	NA	NA	NA	NA	NA	NA	NA
   2	0.9864437	0.9701079	NA	NA	NA	NA	NA	NA	NA	NA
   3	0.9464304	0.9372792	0.9278591	NA	NA	NA	NA	NA	NA	NA

One row per position, one column per length. The entry in row ``i`` and column ``l`` is the
probability that the stretch of ``l`` nucleotides **ending** at position ``i`` is completely
unpaired. Row 1 is therefore ``NA`` beyond ``l=1``, since no stretch of two can end at the
first nucleotide, and those ``NA`` values form the triangle at the top.

The first rows above are also the first warning. Position 1 of this genome is reported as
unpaired with probability 0.98, and the three nucleotides ending at position 3 as unpaired
together with 0.93, which is not a statement about the 5' end of a flavivirus genome but
about the fact that nothing lies upstream of it in the file.

The border effect, and why context is not optional
--------------------------------------------------

The 3' UTR of this genome is 428 nucleotides, short enough to tempt one into folding it on
its own. Doing so changes the answer. Below is the probability that a nucleotide is
unpaired for the same nucleotides, computed once inside the whole genome and once with the
UTR as its own sequence, both with ``-W 300 -L 150``:

.. code-block:: text

   genome pos   in fragment   full genome   UTR alone   difference
       10367             1          0.150       0.949       +0.799
       10370             4          0.118       0.988       +0.870
       10380            14          0.173       0.101       -0.072
       10400            34          0.601       0.613       +0.013
       10450            84          0.015       0.014       -0.001
       10600           234          0.887       0.894       +0.007
       10794           428          0.187       0.187        0.000

The first nucleotides of the fragment have no upstream partners left to pair with, so the
program reports them as nearly free: 0.95 against 0.15 in the genome. An oligo designed
against that site on the strength of the fragment calculation would be aimed at the part of
the answer that is an artefact of the cut.

Looking at the numbers tells us how far the effect reaches. Mean absolute difference between the
two calculations, by distance from the cut:

.. code-block:: text

   first 25 nt of the fragment   0.208   (largest single difference 0.881)
   26 to 75                      0.057   (0.227)
   76 to 150                     0.095   (0.461)
   151 to 250                    0.047   (0.266)
   251 to 428                    0.005   (0.106)

At the 3' end the two calculations agree to three decimal places, because there the context
is the same in both. At the 5' cut they disagree completely, and single positions still
differ by 0.46 at 150 nucleotides from the cut. The practical rule follows from the shape
of that table, and this is exactly what I tell students in practical courses: give a region
a reasonable sequence context, ideally a few hundred nucleotides of real flanking sequence
on each side, and read no accessibility from the first or last window of whatever was
handed to the program. Where the ends cannot be avoided, LocalFold from the paper above was
built to remove the effect.

The same reasoning applies to a transcript. An mRNA cut at its annotated transcription
start site has a real end, and the border is biology. An mRNA fragment cut at an arbitrary
coordinate has an artificial end, and the border is an artefact.

What the window changes
-----------------------

Inside the genome, where there are no border issues, the two parameter sets still disagree
by factors of two to ten:

.. code-block:: text

        pos    W=70 L=70   W=300 L=150
      10400        0.746         0.601
      10450        0.032         0.015
      10500        0.077         0.012
      10600        0.807         0.887
      10700        0.010         0.001

A shorter span raises accessibility, because pairs reaching further than the span are
excluded and a nucleotide has fewer partners available. Accessibility is thus a property of
the sequence and the parameters. Pick the base pair span from what is plausible for the molecule,
keep the window clearly larger, and report both, because an accessibility can only be reproduced by someone who has
those two numbers.

Asking the design question
--------------------------

With the parameters fixed, the file answers directly where a ten-mer could bind. In the
3' UTR of this genome, in full genomic context:

.. code-block:: text

   most accessible     10624-10633   p(all 10 unpaired) = 0.399
                       10533-10542   p(all 10 unpaired) = 0.268

   least accessible    10765-10774   p(all 10 unpaired) = 5.1e-12
                       10770-10779   p(all 10 unpaired) = 1.3e-11

Eleven orders of magnitude between the best and the worst site inside one 428-nucleotide
region. The closed end is where the stable structures of the UTR sit. A reagent aimed
there has to pay for opening them, while one aimed at 10,624 does not. The ranking is what this
program is for: it puts the sites a sequence allows in order of preference, which is what
a design decision needs.

Opening energies
----------------

For design the cost of opening a region is often more convenient than its probability.
``-O`` switches the output to the logarithm of the probabilities, in kcal/mol, written to
``zika_openen``:

.. code-block:: bash

   RNAplfold -W 300 -L 150 -u 10 -O < zika.fa

These numbers go into an energy budget: what an oligo gains from hybridising has to cover
the opening cost of its site. That calculation is what RNAup performs in one step.

Practical notes
---------------

- Output file names come from the FASTA header, so a batch of sequences in one file
  overwrites nothing as long as the headers differ. ``--auto-id`` numbers them instead.
- The complexity in the manual, ``O(n+L*L)`` memory and ``O(n*L*L)`` time, uses ``L`` for
  the window size and not for the span that the command line calls ``-L``.
- ``-u`` should be at least the length of the probe.
- ``-c`` sets the cutoff below which pair probabilities are omitted from the dot plot, 0.01
  by default. This has no effect on the ``_lunp`` file.
- Reactivities from a probing experiment can be folded in with ``--shape``, in the same
  input format and with the same three methods as in the
  :link-flat:`SHAPE tutorial <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>`.
  When both are available it is worth reporting accessibility with and without the data.
- ``-T`` rescales the energy parameters. An accessibility computed at 37 °C says little
  about a hybridisation carried out on ice.

Further reading
---------------

The windowed algorithm behind RNAplfold is described in
`Bernhart, Hofacker and Stadler, Local RNA base pairing probabilities in large sequences <https://doi.org/10.1093/bioinformatics/btk014>`_
(*Bioinformatics* 22:614–5, 2006). The choice of span and window, the border effect and a
remedy for it are the subject of
`Lange et al., Global or local? Predicting secondary structure and accessibility in mRNAs <https://doi.org/10.1093/nar/gks181>`_
(*Nucleic Acids Res.* 40:5215–26, 2012). How an opening cost is combined with the energy of
hybridisation is worked out in
`Mückstein et al., Thermodynamics of RNA–RNA binding <https://doi.org/10.1093/bioinformatics/btl024>`_
(*Bioinformatics* 22:1177–82, 2006), the paper behind RNAup. The
:link-flat:`glossary <{filename}/glossary.rst>` defines the terms used above, and the
:link-flat:`series page <{filename}/rna-structure-prediction.rst>` lists the tutorials in
reading order.
