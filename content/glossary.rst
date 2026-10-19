Glossary
########
:title: Glossary of RNA structure, folding kinetics and viral RNA terms | Michael T. Wolfinger
:summary: Short definitions of the terms used on this site: RNA secondary structure and the thermodynamic model, folding kinetics and barrier trees, chemical probing data, the structured RNA elements of flavivirus genomes, and the software I have written or co-developed.
:description: Definitions of the terms used on this site: MFE and ensemble, barrier tree and BarMap, SHAPE and soft constraints, xrRNA, sfRNA, dumbbell element, ViennaRNA.
:hero_eyebrow: Glossary
:hero_title: Terms used on this site
:date: 2026-10-19
:modified: 2026-10-19

.. Layout note: the definitions are raw-HTML <dl> blocks so that every term gets an
   id and can be linked as /glossary/#term. Pelican expands the {filename} links inside
   raw HTML, and _ldjson.html reads the <dt>/<dd> pairs for the DefinedTermSet.

.. raw:: html

   <p class="page-intro">The posts on this site use a vocabulary that is standard in the field but not outside it. This page collects the terms, each with a short definition and a link to the post where the concept matters most. Every entry has its own address, for example <code>/glossary/#barrier-tree</code>, so a definition can be linked directly.</p>

RNA secondary structure and the thermodynamic model
===================================================

.. raw:: html

   <dl class="glossary">
   <dt id="secondary-structure">RNA secondary structure</dt>
   <dd>The set of base pairs an RNA molecule forms: Watson-Crick pairs GC and AU, and the GU wobble pair. In the standard definition the pairs are nested, i.e. no two pairs cross, which excludes pseudoknots. This is the level of description at which the ViennaRNA algorithms work, and the level at which most of the structures on this site are drawn.</dd>

   <dt id="dot-bracket">Dot-bracket notation</dt>
   <dd>A string with one character per nucleotide. A dot marks an unpaired position, a pair of matching parentheses a base pair. <code>(((((((..((((........)))).(((((.......))))).....(((((.......)))))))))))).... </code> is the cloverleaf of yeast tRNA-Phe. All ViennaRNA programs read and write this notation.</dd>

   <dt id="nearest-neighbor-model">Nearest-neighbor energy model</dt>
   <dd>The free energy of a secondary structure is written as a sum over its loops: stacked pairs, hairpin loops, bulges, interior loops and multiloops, each with a tabulated contribution. The parameters (Turner 2004) were measured by optical melting of small RNAs at 37 °C in 1 M NaCl. Every prediction in ViennaRNA rests on this model, and every limitation of the predictions starts here.</dd>

   <dt id="mfe">Minimum free energy (MFE) structure</dt>
   <dd>The secondary structure with the lowest free energy under the nearest-neighbor model, computed by dynamic programming (Zuker and Stiegler 1981) in <code>RNAfold</code>. It is one structure out of an astronomically large set, and its weight in the ensemble can be a few percent. How much to trust it is the question the <a href="{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst">SHAPE tutorial</a> works through on a tRNA.</dd>

   <dt id="partition-function">Partition function and Boltzmann ensemble</dt>
   <dd>The sum over all secondary structures of exp(−E/RT), computed by McCaskill's algorithm (1990), <code>RNAfold -p</code>. Dividing a structure's Boltzmann factor by the partition function gives its probability, and summing over structures gives the probability of each base pair. The ensemble, rather than a single structure, is what the energy model actually predicts.</dd>

   <dt id="ensemble-free-energy">Ensemble free energy</dt>
   <dd>−RT ln Z, the free energy of the whole ensemble. It is always below the MFE, and the gap between the two measures how much of the ensemble lies outside the MFE structure. <code>RNAfold -p</code> prints it in square brackets.</dd>

   <dt id="base-pair-probability">Base-pair probability and dot plot</dt>
   <dd>The probability that nucleotides i and j are paired in the Boltzmann ensemble. The dot plot shows all of them in the upper triangle of a square, with the area of each dot proportional to the probability, and the MFE structure in the lower triangle. A well-defined structure gives a sparse plot with large dots; a rugged ensemble gives a cloud.</dd>

   <dt id="centroid">Centroid structure</dt>
   <dd>The structure with the smallest expected base-pair distance to all structures in the ensemble. It consists of exactly the pairs with probability above 0.5, so it can contain far fewer pairs than the MFE structure when the ensemble is diverse. <code>RNAfold -p</code> prints it in the third output line.</dd>

   <dt id="mea">Maximum expected accuracy (MEA) structure</dt>
   <dd>The structure that maximizes the sum of the probabilities of its pairs and of its unpaired positions, with a weight that trades the two against each other. <code>RNAfold --MEA</code>. A compromise between the MFE structure, which can be improbable, and the centroid, which can be nearly empty.</dd>

   <dt id="ensemble-diversity">Ensemble diversity</dt>
   <dd>The expected base-pair distance between two structures drawn at random from the Boltzmann ensemble. A small value means the ensemble is dominated by one structure, a value of the order of the sequence length means it is not. For yeast tRNA-Phe the unconstrained prediction gives 23, the SHAPE-constrained one 0.9.</dd>

   <dt id="suboptimal-structures">Suboptimal structures</dt>
   <dd>All secondary structures within a given energy band above the MFE, enumerated by <code>RNAsubopt</code> (Wuchty et al. 1999). The number grows exponentially with the width of the band. Suboptimals are the input to <code>barriers</code> and the direct way to see which alternatives compete with the MFE structure.</dd>

   <dt id="pseudoknot">Pseudoknot</dt>
   <dd>Base pairs between a loop and a region outside the loop, so that two pairs cross when the structure is drawn as an arc diagram. Pseudoknots are excluded from the standard secondary structure algorithms because they break the nested decomposition. They are common in viral RNAs: the <a href="#xrrna">xrRNA</a> fold and the <a href="#dumbbell">dumbbell element</a> depend on them.</dd>

   <dt id="accessibility">Accessibility</dt>
   <dd>The probability that a stretch of nucleotides is unpaired in the ensemble. <code>RNAplfold</code> computes it locally along long sequences. It is the thermodynamic part of whether an siRNA, an antisense oligonucleotide or a protein can bind a site, and it is the quantity the <a href="{filename}/blog/2023-03-31-Investigating-RNA-RNA-interactions-through-computational-and-biophysical-analysis.rst">RNA–RNA interaction</a> work starts from.</dd>

   <dt id="ensemble-defect">Ensemble defect</dt>
   <dd>The expected number of nucleotides whose pairing state in the Boltzmann ensemble differs from a target structure. A sequence with an ensemble defect of zero folds into the target and nothing else. It is the standard objective in computational RNA design, more informative than asking whether the MFE structure equals the target.</dd>
   </dl>

Folding kinetics and energy landscapes
======================================

.. raw:: html

   <dl class="glossary">
   <dt id="energy-landscape">Energy landscape</dt>
   <dd>All secondary structures of a sequence, each with its free energy, together with a move set that says which structures are neighbors, usually the opening or closing of a single base pair. Folding is a walk on this landscape, and most of the kinetics work on this site is about describing landscapes compactly enough to compute on them.</dd>

   <dt id="local-minimum">Local minimum</dt>
   <dd>A structure that has no neighbor with lower free energy. A molecule that reaches it stays until thermal fluctuations carry it over a barrier. Local minima are the metastable states of an RNA, and a landscape of a 100 nt RNA has many thousands of them.</dd>

   <dt id="saddle-point">Saddle point and energy barrier</dt>
   <dd>The lowest energy that a path between two local minima must pass through is the saddle point, and the difference to the starting minimum is the barrier. Barriers set the rates: a few kcal/mol are crossed in microseconds, a barrier of 15 kcal/mol can hold a misfolded RNA for minutes to hours.</dd>

   <dt id="barrier-tree">Barrier tree</dt>
   <dd>A tree that summarizes a rugged landscape: the leaves are the local minima, internal nodes the lowest saddle points connecting them, and the branch lengths the barrier heights. It is computed by the <code>barriers</code> program from a list of suboptimal structures by a flooding algorithm. The construction and its extension to landscapes with many structures of equal energy are in <a href="{filename}/blog/2002-07-01-Barrier_Trees_of_Degenerate_Landscapes.rst">Barrier trees of degenerate landscapes</a>.</dd>

   <dt id="macrostate">Macrostate (basin)</dt>
   <dd>The set of all structures that reach the same local minimum by steepest descent. A landscape with billions of structures collapses into hundreds or thousands of macrostates, which is what makes the kinetics of larger RNAs computable; see <a href="{filename}/blog/2008-06-01-Folding-Kinetics-of-Large-RNAs.rst">Folding kinetics of large RNAs</a>.</dd>

   <dt id="folding-kinetics">Folding kinetics</dt>
   <dd>How the population of structures changes with time. On the coarse-grained landscape this is a continuous-time Markov process between macrostates, with rates computed from the barriers; <code>treekin</code> solves the resulting master equation and gives the population of each macrostate over time, from the first microsecond to equilibrium. The approach is laid out in <a href="{filename}/blog/2004-04-14-Efficient-Computation-of-RNA-Folding-Dynamics.rst">Efficient computation of RNA folding dynamics</a>.</dd>

   <dt id="cotranscriptional-folding">Cotranscriptional folding</dt>
   <dd>An RNA starts to fold while it is being transcribed, so the 5' part forms structures before the 3' part exists. These early structures can trap the molecule in a state that the full-length landscape would never favor. Modeling this means following the population across a series of landscapes, one per transcript length, which is what <a href="#barmap">BarMap</a> does; the <a href="{filename}/blog/2017-01-31-NMR-Structural-Profiling-of-Transcriptional-Intermediates-Reveals-Riboswitch-Regulation-by-Metastable-RNA-Conformations.rst">riboswitch NMR study</a> shows the consequences experimentally.</dd>

   <dt id="barmap">BarMap</dt>
   <dd>A method and program for folding kinetics on landscapes that change with time. For each snapshot, a transcript length or a temperature, a barrier tree is computed; a map between the macrostates of consecutive snapshots transfers the populations from one landscape to the next. Described in <a href="{filename}/blog/2010-07-01-BarMap-RNA-Folding-on-Dynamic-Energy-Landscapes.rst">BarMap: RNA folding on dynamic energy landscapes</a>, and extended to ligand binding in <a href="{filename}/blog/2018-07-01-Efficient_Computation_of_Cotranscriptional_RNA-Ligand_Interaction_Dynamics.rst">cotranscriptional RNA–ligand interaction dynamics</a>.</dd>

   <dt id="folding-time">Folding time</dt>
   <dd>The time an RNA needs to reach its native structure from an unfolded start. It is a random variable with a broad, often multimodal distribution, because different trajectories get caught in different traps. <a href="{filename}/blog/2025-01-22-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst">KinPFN</a> approximates this distribution from a handful of simulated folding times with a prior-data fitted network, which makes kinetic criteria usable in sequence design.</dd>

   <dt id="metastable-state">Metastable state</dt>
   <dd>A local minimum that holds a substantial population for a biologically relevant time without being the thermodynamic ground state. Riboswitches use metastable states to make decisions during transcription; several of the viral RNA elements on this site have alternative conformations whose populations the thermodynamic model alone does not settle.</dd>
   </dl>

Chemical probing data
=====================

.. raw:: html

   <dl class="glossary">
   <dt id="shape">SHAPE</dt>
   <dd>Selective 2'-hydroxyl acylation analyzed by primer extension. A reagent acylates the 2'-OH of nucleotides that are flexible, mostly unpaired ones; reverse transcription stops at the modified positions and the stops are counted. The result is one reactivity per nucleotide. How these numbers enter structure prediction is the subject of <a href="{filename}/blog/2015-09-02-SHAPE-directed-RNA-folding.rst">SHAPE directed RNA folding</a> and of the <a href="{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst">step-by-step tutorial</a>.</dd>

   <dt id="dms">DMS probing</dt>
   <dd>Dimethyl sulfate methylates the Watson-Crick face of unpaired adenines and cytosines. Like SHAPE it reports flexibility per nucleotide, but only for two of the four bases, and it works in living cells. The ViennaRNA soft-constraint methods accept DMS reactivities the same way as SHAPE reactivities.</dd>

   <dt id="reactivity">Reactivity</dt>
   <dd>The per-nucleotide number a probing experiment produces after normalization, typically between 0 and about 2. A reactivity is not a pairing state: a low value means the nucleotide is constrained in some way, a high value means it is flexible, which is true for unpaired nucleotides but also for nucleotides at helix ends and in dynamic pairs. The values are noisy and their scale depends on the experiment.</dd>

   <dt id="soft-constraints">Soft constraints and pseudo-energies</dt>
   <dd>Experimental data enter the prediction as additional energy terms instead of fixed pairing states. A reactivity is converted into a pseudo-energy that rewards or penalizes the pairing of that nucleotide; the folding recursions stay the same, only the energies change. ViennaRNA implements three conversions, after Deigan, Zarringhalam and Washietl, compared in <a href="{filename}/blog/2016-07-01-Predicting_RNA_Structures_from_Sequence_and_Probing_Data.rst">Predicting RNA structures from sequence and probing data</a>.</dd>

   <dt id="hard-constraints">Hard constraints</dt>
   <dd>Pairing states that are forced: a nucleotide must be unpaired, two nucleotides must pair, a region must not pair. <code>RNAfold -C</code> reads them in dot-bracket-like notation. Hard constraints remove structures from the ensemble; soft constraints reweight them. Probing data are too noisy to be used as hard constraints.</dd>

   <dt id="perturbation-vector">Perturbation vector</dt>
   <dd>In the Washietl method, a small energy correction per nucleotide, chosen such that the predicted unpaired probabilities match the probing data as closely as possible while the energy model changes as little as possible. <code>RNApvmin</code> computes it, <code>RNAfold --shapeMethod=W</code> uses it.</dd>
   </dl>

Structured RNA elements in viral genomes
========================================

.. raw:: html

   <dl class="glossary">
   <dt id="utr3">3' untranslated region (3'UTR)</dt>
   <dd>The part of the genomic RNA downstream of the stop codon. In flaviviruses it is 400 to 700 nt long and densely structured, with elements that are conserved across the genus. Most of the viral RNA work on this site is about this region; <a href="{filename}/blog/2021-09-02-Functional-RNA-structures-in-the-3UTR-of-MBFV.rst">Functional RNA structures in the 3'UTR of mosquito-borne flaviviruses</a> is the overview.</dd>

   <dt id="stem-loop">Stem-loop (hairpin)</dt>
   <dd>A helix closed by a loop, the simplest structural element. The flavivirus 3'UTR has a series of them, named SL-I to SL-IV and the terminal 3' stem-loop that ends the genome, each with its own degree of conservation.</dd>

   <dt id="xrrna">Exoribonuclease-resistant RNA (xrRNA)</dt>
   <dd>A structured element that stops the host 5'→3' exoribonuclease Xrn1. The element folds into a ring-like, pseudoknotted structure through which the 5' end of the RNA is threaded, so that the enzyme cannot proceed. In flaviviruses xrRNAs sit in the 3'UTR and produce the <a href="#sfrna">sfRNA</a>. Comparative predictions of these folds across tick-borne and insect-specific viruses are in <a href="{filename}/blog/2019-03-25-Functional_RNA_Structures_in_the_3UTR_of_Tick-Borne_Insect-Specific_and_No_Known_Vector_Flaviviruses.rst">this 2019 paper</a>; the <a href="{filename}/blog/2021-03-01-An_African_Tick_Flavivirus_Forming_an_Independent_Clade_Exhibits_Unique_Exoribonuclease-Resistant_RNA_Structures_in_the_Genomic_three_prime-Untranslated_Region.rst">Mpulungu virus</a> and <a href="{filename}/blog/2020-09-14-Discoveries-of-Exoribonuclease-Resistant-Structures-of-Insect-Specific-Flaviviruses-Isolated-in-Zambia.rst">Barkedji virus</a> papers confirmed predicted xrRNAs in Xrn1 assays.</dd>

   <dt id="sfrna">Subgenomic flavivirus RNA (sfRNA)</dt>
   <dd>The fragment of the 3'UTR that remains when Xrn1 degrades the genomic RNA from the 5' end and stalls at an xrRNA. It accumulates to high levels in infected cells and interferes with host antiviral responses. Which xrRNA stops the enzyme determines the length of the sfRNA; a single 3'UTR can produce several. The <a href="{filename}/blog/2024-10-15-Pan-flavivirus-analysis-reveals-sfRNA-independent-3-UTR-biased-siRNA-production-from-an-insect-specific-flavivirus.rst">pan-flavivirus siRNA study</a> separates sfRNA production from the 3'UTR bias of small RNAs.</dd>

   <dt id="dumbbell">Dumbbell element (DB)</dt>
   <dd>A conserved element of the flavivirus 3'UTR whose secondary structure, a stem carrying two hairpins, looks like a dumbbell. Mosquito-borne flaviviruses have one or two copies; the top loop forms a pseudoknot with a downstream sequence. Dumbbell elements carry conserved UAG motifs, the <a href="#musashi">Musashi binding element</a>, and are among the elements that even the basal tick-associated <a href="#xifv">Xinyang flavivirus</a> retains.</dd>

   <dt id="cyclization">Genome cyclization</dt>
   <dd>Long-range base pairing between the 5' and 3' ends of the flavivirus genome, mediated by complementary cyclization sequences and neighboring elements. The circular form is required for replication, and it competes with the local structures of both ends. The <a href="{filename}/blog/2023-03-31-Investigating-RNA-RNA-interactions-through-computational-and-biophysical-analysis.rst">Japanese encephalitis virus study</a> ranks the candidate interactions computationally and tests them by binding measurements.</dd>

   <dt id="musashi">Musashi binding element (MBE)</dt>
   <dd>A UAG-containing motif in a single-stranded context, recognized by the Musashi family of RNA-binding proteins (MSI1, MSI2), which regulate translation in neural progenitor cells. Zika virus and related flaviviruses carry such motifs in their 3'UTRs, often in dumbbell elements, as mapped in <a href="{filename}/blog/2019-05-06-Musashi-Binding-Elements-in-Zika-and-Related-Flavivirus-3UTRs-A-Comparative-Study-in-Silico.rst">this comparative study</a>.</dd>
   </dl>

Viruses
=======

.. raw:: html

   <dl class="glossary">
   <dt id="flavivirus">Flaviviruses (<em>Orthoflavivirus</em>)</dt>
   <dd>Positive-strand RNA viruses with a genome of about 11 kb: one open reading frame flanked by structured untranslated regions. The genus includes dengue, Zika, West Nile, yellow fever and tick-borne encephalitis viruses, which are transmitted by mosquitoes or ticks to vertebrates, and the insect-specific and no-known-vector groups. The RNA structures of their untranslated regions are a long-running theme of this site; <a href="{filename}/blog/2025-07-29-Functional-RNAs-in-Virology.rst">Functional RNAs in virology</a> gives the wider picture.</dd>

   <dt id="isf">Insect-specific flavivirus (ISF)</dt>
   <dd>A flavivirus that replicates in insects only and cannot infect vertebrate cells. Two groups are distinguished: the classical ISFs, a lineage of their own, and the dual-host affiliated ISFs, which group with the mosquito-borne pathogens phylogenetically but have lost the ability to infect vertebrates. Their 3'UTRs are unusually long and carry several xrRNA-like elements.</dd>

   <dt id="barkedji">Barkedji virus</dt>
   <dd>An insect-specific flavivirus of <em>Culex</em> mosquitoes, named after the village in Senegal where it was first found. <a href="{filename}/blog/2020-09-14-Discoveries-of-Exoribonuclease-Resistant-Structures-of-Insect-Specific-Flaviviruses-Isolated-in-Zambia.rst">The Zambian isolate and a Barkedji-like virus</a> have 3'UTRs with the standard flavivirus elements, including xrRNA folds that resisted Xrn1 digestion in vitro.</dd>

   <dt id="mpfv">Mpulungu flavivirus (MPFV)</dt>
   <dd>A tick-associated flavivirus from Zambia that forms an independent clade, with an exoribonuclease-resistant RNA architecture in the 3'UTR unlike that of the known tick-borne viruses. The <a href="{filename}/blog/2021-03-01-An_African_Tick_Flavivirus_Forming_an_Independent_Clade_Exhibits_Unique_Exoribonuclease-Resistant_RNA_Structures_in_the_Genomic_three_prime-Untranslated_Region.rst">2021 paper</a> combines the genome analysis with Xrn1 assays of the predicted elements.</dd>

   <dt id="xifv">Xinyang flavivirus (XiFV)</dt>
   <dd>A flavivirus from <em>Haemaphysalis flava</em> ticks that defines a basal, probably tick-only clade of the genus. Its 3'UTR still shows the orthoflavivirus architecture, with several pseudoknot-containing stem-loops and a prototypical dumbbell element, which says something about how old these elements are; see <a href="{filename}/blog/2024-05-29-Xinyang-flavivirus-from-Haemaphysalis-flava-ticks-defines-a-basal-likely-tick-only-Orthoflavivirus-clade.rst">the 2024 paper</a>.</dd>
   </dl>

Software
========

.. raw:: html

   <dl class="glossary">
   <dt id="viennarna">ViennaRNA Package</dt>
   <dd>The reference implementation of thermodynamic RNA secondary structure prediction, developed at the University of Vienna since the 1990s and used in the tutorials on this site. <code>RNAfold</code> predicts MFE structures and ensembles, <code>RNAsubopt</code> enumerates suboptimals, <code>RNAplfold</code> computes accessibilities, <code>RNAcofold</code> and <code>RNAup</code> handle RNA–RNA interactions, <code>RNAinverse</code> designs sequences, <code>RNApvmin</code> computes perturbation vectors. The soft-constraint methods for probing data are part of the package since version 2.2.</dd>

   <dt id="barriers-treekin">barriers and treekin</dt>
   <dd>Two programs for folding kinetics on coarse-grained landscapes. <code>barriers</code> builds the <a href="#barrier-tree">barrier tree</a> and the macrostate rate matrix from an energy-sorted list of suboptimal structures; <code>treekin</code> integrates the master equation on that matrix and outputs the population of each macrostate over time. Both are the basis of <a href="#barmap">BarMap</a>.</dd>

   <dt id="kinpfn">KinPFN</dt>
   <dd>A prior-data fitted network that approximates the cumulative distribution of RNA folding times from a few simulated examples in a single forward pass, replacing the many thousands of simulations a direct estimate needs. Described in <a href="{filename}/blog/2025-01-22-KinPFN-Bayesian-Approximation-of-RNA-Folding-Kinetics.rst">KinPFN: Bayesian approximation of RNA folding kinetics</a>.</dd>

   <dt id="tssar">TSSAR</dt>
   <dd>A tool for annotating transcription start sites from differential RNA-seq data, which compares a library enriched for primary transcripts with an untreated one. TSSAR tests the local enrichment of read starts statistically instead of applying a fixed cutoff, and runs as a web service with client-side preprocessing; see <a href="{filename}/blog/2014-04-13-tssar-tss-annotation-regime-for-drna-seq-data.rst">TSSAR: TSS annotation regime for dRNA-seq data</a>.</dd>
   </dl>
