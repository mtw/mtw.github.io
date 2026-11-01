People & Supervision
####################
:title: People & Supervision | Michael T. Wolfinger
:summary: The people I supervise and have supervised, and how supervision of theses and research internships works, including the conditions and the enquiry form.
:description: Supervision by Michael T. Wolfinger: current and former students, the conditions for bachelor, master and doctoral theses, and the enquiry form.
:hero_eyebrow: People & Supervision
:hero_title: People & Supervision

.. role:: link-flat(link)
  :class: m-flat m-text

.. Layout note: the three people groups (title + note on a 2px rule, then a two-column
   grid of name / role / affiliation rows) are one raw-HTML block on purpose. The prose
   is plain <p> text and stays editable.

.. raw:: html

   <p class="page-intro">The work spans computational RNA biology, with a focus on RNA structure prediction, RNA design, structured viral RNAs, RNA&ndash;protein interactions, and folding kinetics. Those involved come from backgrounds including bioinformatics, chemistry, molecular biology, physics, and data analysis.</p>

   <div class="people-group">
     <div class="group-head"><h2>Current supervision</h2><span class="note">researchers currently supervised or co-supervised</span></div>
     <div class="people-grid">
       <div class="person"><div><div class="n">Leonhard Sidl</div><div class="r">PhD student</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Yannick Seitz</div><div class="r">Master student</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Milan Geyer</div><div class="r">Master student</div></div><span class="y">University of Vienna</span></div>
     </div>
     <p class="small-print" style="margin-top:18px">Affiliations show where each researcher is enrolled. I supervise them through ongoing collaborations with those institutions.</p>
   </div>

   <div class="people-group">
     <div class="group-head"><h2>Former group members</h2><span class="note">supervised at the University of Vienna and FH Campus Wien</span></div>
     <div class="people-grid">
       <div class="person"><div><div class="n">Katrin Gutenbrunner</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Florentina Bayer</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Denis Skibinski</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Teodora Bucaciuc</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Michael Kail</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Markus Delitz</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Julia Wielach</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Daniel Oser</div></div><span class="y">University of Vienna</span></div>
       <div class="person"><div><div class="n">Dominik Luntzer</div></div><span class="y">FH Campus Wien</span></div>
       <div class="person"><div><div class="n">Werner Gradwohl</div></div><span class="y">FH Campus Wien</span></div>
       <div class="person"><div><div class="n">Daniel Hooker</div></div><span class="y">FH Campus Wien</span></div>
       <div class="person"><div><div class="n">Christian Mayr</div></div><span class="y">FH Campus Wien</span></div>
     </div>
   </div>

Thesis and internship supervision
=================================

I supervise bachelor, master and doctoral theses as well as research internships on
topics in RNA structure prediction, folding kinetics, functional RNA design and viral RNA
biology, the areas described on the :link-flat:`research page <{filename}/research.rst>`,
and the people I currently supervise are listed above. Students enrolled at the University of Vienna are supervised through the Theoretical
Biochemistry Group, students of other universities through a collaboration with their
home institution.

.. class:: m-block m-primary

   **No open positions.** I currently have no funded doctoral or postdoctoral positions,
   and I do not accept doctoral candidates without secured funding. Generic requests for
   PhD supervision, i.e. messages that name neither a specific topic from my research
   nor a concrete source of funding, are not answered. This applies to the form below as
   well as to email.

The form is for bachelor and master theses and research internships of enrolled
students, and for doctoral candidates who hold a scholarship or fellowship of their own,
or have applied for one (name it in the message). It asks for the few things I need in
order to answer: your programme, the kind of thesis, the funding, the earliest start, and
a few sentences on what you would like to work on and what you bring, e.g. relevant
courses, programming experience or laboratory background.

.. raw:: html

   <p class="form-sent" id="supervision-sent">Thank you, your enquiry has arrived. A confirmation has gone to your address, and you will hear back from me, usually within a few working days.</p>
   <p class="form-error" id="supervision-error">The enquiry was not sent: a required field was empty or the email address was not valid. Please check the fields and send again.</p>
   <form class="site-form" method="post" action="https://forms.rnaforecast.com/mtw-supervision">
     <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
     <p class="field">
       <label for="sv-name">Name <abbr title="required">*</abbr></label>
       <input class="input" type="text" id="sv-name" name="name" autocomplete="name" maxlength="200" required>
     </p>
     <p class="field">
       <label for="sv-email">Email <abbr title="required">*</abbr></label>
       <input class="input" type="email" id="sv-email" name="email" autocomplete="email" maxlength="254" required>
     </p>
     <p class="field">
       <label for="sv-programme">Programme and university</label>
       <input class="input" type="text" id="sv-programme" name="programme" maxlength="200" placeholder="e.g. MSc Molecular Biology, University of Vienna">
     </p>
     <p class="field">
       <label for="sv-level">Thesis or position <abbr title="required">*</abbr></label>
       <select class="input" id="sv-level" name="level" required>
         <option value="">Choose one</option>
         <option value="bachelor">Bachelor thesis</option>
         <option value="master">Master thesis</option>
         <option value="doctoral">Doctoral thesis (own funding)</option>
         <option value="internship">Research internship</option>
         <option value="other">Other</option>
       </select>
     </p>
     <p class="field">
       <label for="sv-funding">Funding <abbr title="required">*</abbr></label>
       <select class="input" id="sv-funding" name="funding" required>
         <option value="">Choose one</option>
         <option value="enrolled">Thesis or internship within my degree programme, no funding needed</option>
         <option value="granted">Scholarship or fellowship granted, named in the message</option>
         <option value="applied">Scholarship application submitted or in preparation, named in the message</option>
         <option value="none">No funding (the enquiry will not be answered)</option>
       </select>
     </p>
     <p class="field">
       <label for="sv-start">Earliest start</label>
       <input class="input" type="text" id="sv-start" name="start" maxlength="100" placeholder="e.g. March 2027">
     </p>
     <p class="field">
       <label for="sv-message">What you would like to work on, and your background <abbr title="required">*</abbr></label>
       <textarea class="input" id="sv-message" name="message" rows="6" maxlength="5000" required></textarea>
     </p>
     <p class="field check">
       <input type="checkbox" id="sv-ack" name="ack" value="yes" required>
       <label for="sv-ack">I have read that there are no open positions. My enquiry names a specific topic and, for a doctoral thesis, the funding. <abbr title="required">*</abbr></label>
     </p>
     <p class="form-note">Fields marked <abbr title="required">*</abbr> are required. What you enter is stored for handling the enquiry and sent to me by email. See the <a href="/datenschutz/">privacy notice</a>.</p>
     <button class="form-submit" type="submit">Send enquiry</button>
   </form>
