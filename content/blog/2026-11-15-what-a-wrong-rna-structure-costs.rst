What a wrong RNA structure costs
################################

:date: 2026-11-15
:tags: ViennaRNA; RNA structure prediction
:category: background
:section: essays
:bridge: rna
:slug: what-a-wrong-rna-structure-costs
:feedback: guide
:title: What a wrong RNA structure costs
:summary: Computing an RNA secondary structure takes a second. Deciding what to do with the result is where a project's money goes. Seven ways a prediction gets used for something it did not say, what each one costs a project in months and experiments at Austrian public funding rates, and the check that would have caught it. Written for the person who signs the timesheet, with the central number computed on the first 400 nucleotides of a real viral genome.
:description: Seven ways an RNA structure prediction is acted on wrongly, what each costs a lab in months and experiments, and the check that prevents it.

.. role:: link-flat(link)
  :class: m-flat m-text

.. container:: series-note

   Background to :link-flat:`ViennaRNA in practice <{filename}/rna-structure-prediction.rst>`, a series of tutorials. :link-flat:`RNAfold tutorial <{filename}/blog/2026-10-28-rnafold-in-practice.rst>` · :link-flat:`SHAPE and chemical probing data <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>` · :link-flat:`RNAplfold and accessibility <{filename}/blog/2026-11-07-rnaplfold-accessibility.rst>` · :link-flat:`ViennaRNA 2.8.0 release note <{filename}/blog/2026-11-12-viennarna-2-8-0.rst>`

Computing a secondary structure is the cheapest step in RNA biology. What is done with
the result is among the most consequential. ``RNAfold`` on a few hundred nucleotides
finishes in well under a second on a laptop, and the output looks finished too: one line
of brackets, one energy. Nothing about it says that this is the most probable of many
structures the molecule adopts, not the structure it has.

The money is spent afterwards, when the line of brackets becomes a mutant series, a
synthesis order, or a panel in a grant application. This is a list of the ways I have
seen that step go wrong, in courses, in the issue tracker and in manuscripts I have
reviewed, with the cost of each worked out at current rates. None of them is a flaw in
the method. Each is the method answering a question that was not the one being asked.

Three unit prices
-----------------

The arithmetic below uses three numbers, stated once here so the multiplication is yours
to check. The salary figure is an Austrian public funding rate, so the sums are what a
project here would pay. Rates elsewhere in Europe differ, the order of magnitude does not.

- **A doctoral month.** The `FWF standard personnel cost rate <https://www.fwf.ac.at/en/funding/steps-to-your-fwf-project/further-information/personnel-costs>`_
  for a doctoral candidate at 30 hours a week is EUR 50,220 a year for applications from
  January 2026, employer contributions included. Six months of a doctoral student cost
  half of that, EUR 25,110.
- **A probing experiment.** SHAPE-MaP or DMS-MaPseq on one RNA costs a few thousand euros
  in reagents and sequencing and two to four weeks of somebody's time, before any
  analysis.
- **A synthesis round.** A handful of oligonucleotides is a few hundred euros. A series
  of modified mRNA constructs for an expression assay runs to four or five figures.

Delay has a price of its own that none of these capture. A manuscript revision is three
to six months. A grant deadline missed is a year.

1. The minimum free energy structure, taken as *the* structure
---------------------------------------------------------------

**What it looks like.** A figure with one structure in it. A mutant designed to disrupt
"the helix at positions 120 to 135". A sentence in a manuscript saying the 5' UTR forms a
stem-loop, singular.

**Why the model produces it.** The MFE structure is the single most stable one, and for
an RNA of a few hundred nucleotides that is a weak distinction. Here are the first 400
nucleotides of the SARS-CoV-2 genome (NC_045512.2), the 5' UTR and the start of ORF1ab,
one of the best-studied RNA structures of the decade:

.. code:: bash

   RNAfold -p --noPS < sars2_1-400.fa

.. code:: text

   AUUAAAGGUUUAUACCUUCCCAGGUAACAAACCAACCAACUUUCGAUCUCUUGUAGAUCUGUUCUCUAAACGAACUUUAAAAUCUGUGUGGCUGUCACUCGGCUGCAUGCUUAGUGCACUCACGCAGUAUAAUUAAUAACUAAUUACUGUCGUUGACAGGACACGAGUAACUCGUCUAUCUUCUGCAGGCUGCUUACGGUUUCGUCCGUGUUGCAGCCGAUCAUCAGCACAUCUAGGUUUCGUCCGGGUGUGACCGAAAGGUAAGAUGGAGAGCCUUGUCCCUGGUUUCAACGAGAAAACACACGUCCAACUCAGUUUGCCUGUUUUACAGGUUCGCGACGUGCUCGUACGUGGCUUUGGAGACUCCGUGGAGGAGGUCUUAUCAGAGGCACGUCAACAU
   ......(((((.(((((....)))))..))))).......(((((((((.....))))).((((.......))))........((((((((.((.((((.(((.....))).)))))).))))))))..((((((.....))))))...(((((((((((..(((((...(((.((((((((.....((((((.(((((......)))))..)))))).........(((((((.((......)))))))))(((....)))))))))))))).))))).))))...)))))))))))...((((((.......((..((((((...))))))..))))))))...(.(((((.(((((((((((((.....))).)))))..))))).))))))..... (-132.70)
   ......(((((.(((((....)))))..))))).........,.(((((.....))))).((((.......))))........((((((((.((.((((.(((.....))).)))))).))))))))..{(((((.....)))))}.{.(((((((((((..(((((...(((.((((((((.,,..((((((.(((((......)))))..))))))......,..(((((((.((......)))))))))(((....)))))))))))))).))))).))))...))))))),).....((((((.......((..((((((...))))))..))))))))...|}(((((.(((((((((((((.....)))}})))}.,))))).)))))...... [-138.14]
   ......(((((.(((((....)))))..)))))...........(((((.....))))).((((.......))))........((((((((.((.((((.(((.....))).)))))).))))))))..((((((.....))))))...(((((((((((..(((((...(((.((((((((.....((((((.(((((......)))))..)))))).........(((((((.((......)))))))))(((....)))))))))))))).))))).))))...))))))).......((((((.......((..((((((...))))))..)))))))).....(((((.(((((((((((((.....))).)))))..))))).)))))...... {-130.40 d=21.45}
    frequency of mfe structure in ensemble 0.000147239; ensemble diversity 35.27 

.. code:: bash

   RNAsubopt -e 1 < sars2_1-400.fa | tail -n +3 | wc -l
   # 104

The MFE structure has a free energy of −132.7 kcal/mol and a probability of **0.015
percent** in the ensemble it was drawn from, i.e. about one molecule in seven thousand.
There are 104 structures within 1 kcal/mol of it, 1,641 within 2 and more than 17,000
within 3. The ensemble diversity, i.e. the expected number of base pairs by which two
structures drawn from the population differ, is 35.

This does not mean the prediction is bad, and the literature lets us check. Probing and
conservation studies agree on five stem-loops in this region, SL1 to SL5, with SL5
spanning positions 150 to 294 and ending with a three-way junction (Rangan et al. 2020,
Manfredonia et al. 2020, Huston et al. 2021). They sit one after the other on an otherwise
unpaired backbone. All five are in the MFE structure above (the third arm of the SL5
junction, SL5c, is the one piece the model does not place), and the base pairs that form
them have mean probabilities of 0.90 (SL1), 0.95 (SL2), 0.81 (SL3), 0.97 (SL4) and 0.93
(SL5) in the ensemble. The helices are well supported.

The MFE structure also contains one thing the literature does not have. Nucleotides 41 to
44 pair with 295 to 298, four base pairs that close SL2 to SL5 into a multiloop. Those four
pairs have probabilities between 0.23 and 0.30. The centroid structure, the third line
of the output above, leaves them out, and so does the maximum expected accuracy structure
(``RNAfold --MEA``). The one element of the prediction that the probing data reject is the one element the dot plot
marks as weak, and the line of brackets gives no hint of it. The question to ask is
therefore about a helix, never about a structure.

**What it costs.** A mutant series designed against a helix with a base pair probability
of 0.3 tests a helix that is absent in seven out of ten molecules. Design, cloning, the assay and the months
before anyone notices that nothing is consistent come to about a quarter of a doctoral
year, i.e. about EUR 12,500, plus reagents.

**What prevents it.** ``RNAfold -p``, and the dot plot read before anything is ordered.
The :link-flat:`RNAfold tutorial <{filename}/blog/2026-10-28-rnafold-in-practice.rst>`
in this series exists for this.

2. A fragment folded out of its context
----------------------------------------

**What it looks like.** A 3' UTR cut out of the transcript and folded alone. A target site
for an siRNA or an antisense oligonucleotide judged on the fold of the 50 nucleotides
around it.

**Why the model produces it.** Base pairs do not respect the boundaries you draw. A
nucleotide near the edge of a fragment has lost half of its possible partners, so the
prediction for that region describes a molecule that does not exist.

The same RNA shows it. The annotated 5' UTR ends at position 265, and folding exactly
those 265 nucleotides, as a reasonable person would, gives a structure in which SL2 is
missing (its nucleotides pair elsewhere, the best pair inside the element has a
probability of 0.20) and SL5 is cut through the middle, because SL5 runs to position 294
and the boundary of the fragment is inside it. With 400 nucleotides both are back, SL2
with pair probabilities of 0.95. Nothing about the sequence changed. The boundary moved
a conserved hairpin out of the prediction.

The accessibility question is more sensitive still, and here the mistake deserves to be
shown as a mistake. The first of these two commands is the one a person makes who has the
UTR in a file and wants to know how accessible an eight-nucleotide window is:

.. code:: bash

   RNAplfold -W 240 -L 160 -u 8 < sars2_5utr.fa    # the mistake: the UTR by itself
   RNAplfold -W 240 -L 160 -u 8 < sars2_1-600.fa   # the UTR in its context

The sequence in the first file is 265 nucleotides and the window is 240, so there is no
position in that file that lies more than one window from a cut. The
:link-flat:`RNAplfold tutorial <{filename}/blog/2026-11-07-rnaplfold-accessibility.rst#the-border-effect-and-why-context-is-not-optional>`
measures how far the border effect reaches and ends with the rule to read no accessibility
from the first or last window of whatever was handed to the program. By that rule the first
command yields nothing that may be read at all. It still prints numbers, and they look like
every other number the program prints:

=========  =====================  =====================
position   UTR alone              UTR within 600 nt
=========  =====================  =====================
215        5.8 × 10\ :sup:`-8`    4.7 × 10\ :sup:`-4`
230        0.070                  0.011
265        0.035                  0.00097
=========  =====================  =====================

At the 3' end of the fragment the number is 36 times too high. Fifty nucleotides upstream
it is four orders of magnitude too low. Near a boundary the result is not an approximation
of the right number, it has no relation to it, and nothing in the output says so.

**What it costs.** A synthesis round aimed at a site chosen on the wrong number, and the
weeks of testing that follow. For oligonucleotides the reagents are cheap and the time is
not. For a series of modified mRNAs neither is.

**What prevents it.** Fold the whole molecule, or compute the local quantity with the
fragment inside its context, which is what ``RNAplfold`` is for. The
:link-flat:`RNAplfold tutorial <{filename}/blog/2026-11-07-rnaplfold-accessibility.rst>`
works through the choice of window and span.

3. Modified nucleotides folded as unmodified ones
-------------------------------------------------

**What it looks like.** A therapeutic mRNA in which every uridine has been replaced by
N1-methylpseudouridine, folded with the default parameters, i.e. as if it were made of
uridine.

**Why the model produces it.** The default energy parameters describe the four standard
nucleotides. Modified bases pair and stack differently. Before ViennaRNA 2.8.0 the
parameter files for them had to be found and loaded separately, so most people did not.

**What it costs.** For a therapeutics group this is the most expensive item on the list.
Construct design, a synthesis series and an expression assay, all resting on a calculation
for the unmodified sequence, while the molecule that leaves the synthesiser carries the
modified base at every uridine position. A single synthesis series of modified mRNAs can reach
five figures before the first measurement.

**What prevents it.** Since ViennaRNA 2.8.0 the parameter files for pseudouridine and
N1-methylpseudouridine ship inside the library, so the fix is one option on the command
line. The :link-flat:`2.8.0 release note <{filename}/blog/2026-11-12-viennarna-2-8-0.rst>`
has the details.

4. Probing data that constrained nothing
-----------------------------------------

**What it looks like.** A SHAPE-MaP dataset, generated at real expense, shown as a bar
chart beside the predicted structure and never put into the prediction. Or put in with
the default method, no thought about normalisation, and read afterwards as a per-nucleotide
verdict of paired or unpaired.

**Why the model produces it.** A reactivity is a continuous, noisy measure of nucleotide
flexibility. It is not a pairing state. It enters the model as a pseudo energy, and the
three methods for doing so give different structures from the same data, which is why the
method and its parameters have to be chosen and then reported.

**What it costs.** The experiment itself, a few thousand euros and several weeks, is the
smaller part. The larger part is a figure that looks like validation and is not. A reviewer usually
finds this before the authors do.

**What prevents it.** ``--shape`` with a method chosen on purpose, and the constrained
prediction reported next to the unconstrained one. The
:link-flat:`probing-data tutorial <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>`
covers the three methods and what to report.

5. A structure claim with nothing behind it
--------------------------------------------

**What it looks like.** One dot-bracket string in a figure legend. No base pair
probabilities, no ensemble diversity, no alternative structure, no statement of what was
checked.

**Why the model produces it.** ``RNAfold`` prints one structure by default, and one
structure is what gets pasted into the figure.

**What it costs.** Reviewers ask now, more often than not, how well supported the structure is.
Answering takes an afternoon if the ensemble was computed at the time and a revision cycle
if it was not: three to six months for a manuscript. In a grant application there is no
revision cycle, only the next deadline, a year away.

**What prevents it.** Show the dot plot or the base pair probabilities, report the
ensemble diversity, and say in the methods which quantities were examined. This is a
few minutes of work when the ensemble was computed in the first place.

6. What the model leaves out, assumed to be in it
-------------------------------------------------

**What it looks like.** A secondary structure reported for an RNA whose fold is decided by
something the calculation does not contain. tRNA is the usual example. For yeast
tRNA-Phe with default parameters the MFE structure is the cloverleaf, with a probability
of six percent. The centroid of the ensemble keeps only the acceptor stem, and at 25 °C a
different structure becomes the MFE, with alternative D and anticodon arms. What holds the
real molecule in its shape is a network of tertiary contacts and magnesium ions, neither
of which is in the model.

**Why the model produces it.** The nearest neighbour model contains stacking energies,
loop penalties and the standard base pairs at 37 °C in 1 M NaCl. It does not contain
pseudoknots, divalent ions, proteins, modified bases unless asked, or tertiary contacts.
Where those decide the fold, the ensemble says what the sequence would do on its own in a
test tube of salt water. Everything beyond that has to come from somewhere else, e.g. from
probing data, from a homologue with a solved structure, or from an experiment.

**What it costs.** Months spent on a question the method cannot answer, and a claim that
no better parameter set can rescue. This is the error that most often becomes a correction
rather than a revision.

**What prevents it.** Knowing the list of what is not in the model before starting, and
asking whether the RNA at hand is on it. The closing section of the
:link-flat:`RNAfold tutorial <{filename}/blog/2026-10-28-rnafold-in-practice.rst#practical-consequences>`
spells the list out.

7. Numbers compared across parameter sets or versions
------------------------------------------------------

**What it looks like.** A free energy computed in 2019 set beside one computed with ViennaRNA 2.8.0.
Pseudo energies from a probing-constrained fold compared with unconstrained ones. Results
from two versions of the package pooled into one table.

**Why the model produces it.** Energies are only comparable within one parameter set and
one method. ViennaRNA 2.8.0, released on 6 November 2026, corrected the units of the
G-quadruplex parameters, three corrections for modified bases, Wuchty-style suboptimal
folding for two dangle settings, and the loop decomposition used by ``RNAeval``. A number
from before and a number from after are not the same quantity.

**What it costs.** A resubmission when the numbers do not reproduce, or, if nobody
checks, a difference between two versions of the software interpreted as biology and
published.

**What prevents it.** The package version and the parameter file in the methods section
of every paper, and a recomputation when upgrading. The
:link-flat:`2.8.0 release note <{filename}/blog/2026-11-12-viennarna-2-8-0.rst>` lists
which results moved.

What the arithmetic says
------------------------

Each item above costs more than the check that would have caught it, usually by a factor
of a hundred or more. The check is a second command, or a second look at output that
already exists. Done deliberately, before anything is ordered, that check has a name, an
:link-flat:`RNA structure review <{filename}/glossary.rst#structure-review>`, and it costs
a small fraction of any item above. The expensive mistakes in RNA structure work happen when the most probable of
many structures is read as the structure the molecule has, and an order form is signed
on that reading.

Sources: FWF `standard personnel costs <https://www.fwf.ac.at/en/funding/steps-to-your-fwf-project/further-information/personnel-costs>`_,
rates for applications from January 2026 ·
`NC_045512.2 <https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2>`_, SARS-CoV-2 isolate
Wuhan-Hu-1, positions 1 to 265, 1 to 400 and 1 to 600 ·
Rangan R, Zheludev IN, Hagey RJ, Pham EA, Wayment-Steele HK, Glenn JS, Das R. RNA genome
conservation and secondary structure in SARS-CoV-2 and SARS-related viruses. *RNA*
26:937–959 (2020). `doi:10.1261/rna.076141.120 <https://doi.org/10.1261/rna.076141.120>`_ ·
Manfredonia I, Nithin C, Ponce-Salvatierra A, Ghosh P, Wirecki TK, Marinus T, Ogando NS,
Snijder EJ, van Hemert MJ, Bujnicki JM, Incarnato D. Genome-wide mapping of SARS-CoV-2 RNA
structures identifies therapeutically-relevant elements. *Nucleic Acids Res* 48:12436–12452
(2020). `doi:10.1093/nar/gkaa1053 <https://doi.org/10.1093/nar/gkaa1053>`_ ·
Huston NC, Wan H, Strine MS, de Cesaris Araujo Tavares R, Wilen CB, Pyle AM. Comprehensive
in vivo secondary structure of the SARS-CoV-2 genome reveals novel regulatory motifs and
mechanisms. *Mol Cell* 81:584–598.e5 (2021). `doi:10.1016/j.molcel.2020.12.041 <https://doi.org/10.1016/j.molcel.2020.12.041>`_ · ViennaRNA 2.8.0,
`RNAfold <https://viennarna.readthedocs.io/latest/usage/man/RNAfold.html>`_,
`RNAsubopt <https://viennarna.readthedocs.io/latest/usage/man/RNAsubopt.html>`_ and
`RNAplfold <https://viennarna.readthedocs.io/latest/usage/man/RNAplfold.html>`_ man pages ·
`ViennaRNA 2.8.0 release notes <https://github.com/ViennaRNA/ViennaRNA/releases/tag/v2.8.0>`_.
