ViennaRNA training and workshops for researchers, starting in 2027
##################################################################

:date: 2026-10-28 18:00
:tags: ViennaRNA; tools
:category: outreach
:section: talks
:slug: viennarna-training-workshops-2027
:title: ViennaRNA training and workshops for researchers, starting in 2027
:summary: A series of practical ViennaRNA training modules and workshops is in preparation at RNA Forecast, planned to begin in early 2027. The training is for researchers who use RNA structure prediction in their own work and want to understand the results well enough to base decisions on them. The waiting list is open.
:description: Practical ViennaRNA training modules and workshops for experimental and computational researchers, planned for early 2027 at RNA Forecast. Waiting list open.
:social_image: {static}/static/og-viennarna-training-1200x630.png

.. role:: link-flat(link)
  :class: m-flat m-text

Whenever it comes to RNA secondary structure prediction, running the calculation is the
easy part. RNAfold returns a predicted structure, a minimum free energy and, on request,
a dot plot with the base pair probabilities, and it does so within a second for most
sequences. Understanding what this result means for the research question at hand takes
considerably more practice. Which features of the output deserve attention, how
confidently can a predicted structure be interpreted, when is one structure sufficient,
and when should one consider alternative structures, the uncertainty of the model or
additional experimental evidence?

I am preparing a series of practical ViennaRNA training modules and workshops through
`RNA Forecast <https://rnaforecast.com/>`_, planned to begin in early 2027. The training
is for researchers who want to use ViennaRNA and RNA structure analysis in their own
work and understand the results well enough to make informed experimental and
computational decisions.

From running RNAfold to interpreting the result
-----------------------------------------------

ViennaRNA provides a comprehensive set of tools for RNA secondary structure prediction,
however, obtaining an output is only the first step. A predicted structure is a model,
and its usefulness depends on the biological question, the sequence, the assumptions of
the calculation and the evidence available to support it. The training will therefore
connect the computational output to practical research questions. By means of worked
examples and hands-on exercises we will examine what RNAfold and the related programs
can tell, what they cannot tell on their own, and how to set up analyses that can be
reproduced and explained.

Depending on the module, participants will learn how to

- interpret RNAfold results, i.e. predicted secondary structures, folding energies,
  base pair probabilities and dot plots, and recognize the information that a single
  structure drawing leaves out (the
  :link-flat:`RNAfold tutorial <{filename}/blog/2026-10-28-rnafold-in-practice.rst>` on
  this site gives a first impression of this part),
- use ViennaRNA beyond a one-off calculation on a web server, i.e. build reproducible
  structure prediction workflows that can be applied to new sequences and questions,
- compare structure predictions critically and recognize which conclusions are well
  supported and which depend strongly on model choices or on uncertain base pairs,
- understand alternative structures and folding dynamics, and judge when structural
  heterogeneity matters for a given question,
- integrate experimental evidence such as chemical probing data into the analysis (see
  the :link-flat:`SHAPE tutorial <{filename}/blog/2026-10-19-shape-probing-data-rna-structure-prediction.rst>`
  for the mechanics), and see where uncertainty remains, and
- communicate computational results clearly, i.e. explain what a structure prediction
  supports, what it does not establish, and what a useful next analysis or experiment
  would be.

The aim is to get from "I ran RNAfold" to "I understand what this analysis contributes
to my project", rather than to teach commands or to produce attractive structure
drawings.

Who the workshops are for
-------------------------

The initial modules are intended for experimental biologists, biochemists, molecular
biologists and researchers in academic or biotech teams who work with RNA. No background
in computational RNA biology is required. The workshops will be particularly useful for
those who have encountered questions such as the following.

- How much trust should I place in this predicted structure?
- What does the folding energy actually mean?
- Why does the dot plot look different from the structure drawing?
- How can I compare structure predictions between sequences or constructs?
- When might RNA structure explain unexpected expression, activity or experimental
  behaviour?
- How can I make an RNAfold analysis reproducible?

More advanced modules will be developed for researchers who already use the package and
want to extend their workflows, use the scripting interfaces or interpret more complex
analyses with greater confidence.

The material draws on my experience in developing RNA analysis methods and in teaching
computational RNA biology. The focus will be practical and question-driven, i.e. how to
use ViennaRNA appropriately, how to interpret its output critically and how to decide
what the analysis contributes to the next research step. Participants should leave with
a clearer understanding of RNA structure prediction, reusable analysis workflows and the
ability to recognize both useful findings and important limitations.

Waiting list
------------

The first workshops are planned for early 2027. Dates, formats and the initial
selection of modules are currently being worked out. If you would like to hear when the
first workshop or module is announced, join the
`ViennaRNA training waiting list at RNA Forecast <https://rnaforecast.com/training/#viennarna>`_.
The form has a field for topics, example questions or workflows you would like to see
covered, and these suggestions are welcome. Joining the list expresses interest only and
does not commit you to anything, you will receive one email when the first dates are
available.
