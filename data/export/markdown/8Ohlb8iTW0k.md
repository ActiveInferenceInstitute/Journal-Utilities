---
title: "Active InferAnt Stream 012.1 ~ CEREBRUM: Case-Enabled Reasoning Engine with..."
category: "ActiveInferAntStream"
series: "ActiveInferAntStream_012"
episode: "1"
speakers:
  - "CEREBRUM: Case-Enabled Reasoning Engine with..."
duration: "2:33:30"
url: "https://www.youtube.com/watch?v=8Ohlb8iTW0k"
views: 273
exported_at: "2026-02-18T22:37:37.711153+00:00"
format: markdown
---

# Active InferAnt Stream 012.1 ~ CEREBRUM: Case-Enabled Reasoning Engine with...

All right.
All right.
It is April 7th, 2025.
This is going to be Active Inference Stream 12.1.
Cerebrum.
Case-enabled reasoning engine with Bayesian representations for unified modeling.
I've started first to make a GitHub push to the GitHub repo Active Inference Institute slash Cerebrum.
And that is now live.
And here in cursor, I'm running the render script render markdown, which calls the script render mermaids, which takes this markdown file.
And all of these 15 figure level markdown files and the math and the novel case appendix.
And is going to result in a PDF.
And I'm going to go through the PDF.
The PDF looks like this.
In this stream, we're going to go through the PDF and talk about probably a bunch more depending on who shows up.
I'm going to finish flipping through the PDF.
Then we will see where the PDF generation is at.
And then we will go through this.
This should be super interesting.
Conclusion.
Appendix 1 math.
Appendix 2.
Novel cases.
Alright.
The generation will finish soon.
It renders each of the 15 mermaid diagram figures, which look like this, into figures that look like that.
And then inserts them into the markdown.
Alright.
PDF generated.
It generates Cerebrum.pdf.
So that's the newly rendered version.
And I'll push it.
And then let us get into the topic.
I also just push this to Zenodo.
And looking forward to where we go from here.
So we're all pushed on the repo.
Let's look at the paper.
And go through some of the sections.
Alright.
I'll read the abstract first.
This paper introduces case-enabled reasoning engine with Bayesian representations for unified modeling.
Cerebrum.
Cerebrum is a synthetic intelligence framework that integrates linguistic case systems with cognitive scientific principles to describe, design, and deploy generative models in an expressive fashion.
By treating models as case-enabled model.
By treating models as case-bearing entities that can play multiple contextual roles, like declinable nouns.
Cerebrum establishes a formal linguistic type calculus for cognitive model use, relationships, and transformations.
The Cerebrum framework uses structures from category theory and modeling techniques related to the free energy principle in describing and utilizing models across contexts.
Cerebrum addresses the growing complexity in computational and cognitive modeling systems, e.g. generative, decentralized, agentic intelligences, by providing structured representations of model ecosystems that align with lexical, ergonomic, scientific principles, and operational processes.
And we will probably push to another version by the end of the stream.
So we'll fix a few different things that we can see along the way.
Describing and utilizing models across contexts.
Okay.
Continuing to overview.
Cerebrum implements a comprehensive approach to cognitive systems modeling by applying linguistic case systems to model management.
This framework treats cognitive models as entities that can exist in different cases, as in a morphologically rich language, based on their functional role within an intelligence production workflow.
This enables more structured representation of model relationships and transformations.
And the code to generate this paper and further open source development from this 1.0 milestone is available at this GitHub repo.
And that's what we'll be pushing to and using during this stream.
Okay.
Background sections.
First background sections on cognitive systems modeling.
The second background section is about active inference.
The third background section is about linguistic case systems.
And I'm going to read this one because this might be the one that's the wild card.
However, this is the crux.
And as a first language English speaker, as we'll discuss, there are some interesting ways of having the cases.
A bit more silent in English than some other languages like Russian and Latin.
And other things that will probably end up on Wikipedia to find out today.
So I'm going to read this linguistic case section.
Linguistic case systems represent grammatical relationships between words.
Among words.
Through morphological marking.
Case systems operate as morphosyntactic interfaces between semantics and syntax.
Encoding contextualized relationship types rather than just, or in addition to, just sequential ordering.
This inherent relationality makes case systems powerful abstractions for modeling complex dependencies and transformations between conceptual entities.
Cases under consideration here include nominative, subject, accusative, object, dative, recipient, genitive, possessor, instrumental, tool, locative, location, and ablative, origin.
All serving different functional roles within sentence structure.
Language.
English has largely lost its morphological case system.
The underlying case relationships still exist and are expressed through word order and prepositions.
For example, in the cat chased the mouse, the nominative case is marked by position, subject before verb, rather than morphology.
While in I gave him the book, the dative case is marked by the preposition to and word order.
This demonstrates that the semantics slash chemiosis slash pragmatics of case relationships are fundamental to language structure, even when not overtly marked morphologically, e.g. expressed in writing or spoken language.
Section 134.
Intelligence Case Management Systems.
So this sort of speaks to the pun at the heart of this, which is case management, which might be for like a help ticket or a research inquiry or any other kind of case management.
It's a bit of a hinge with the linguistic case systems.
So coincidence, but enough of a connection and gap there to have the linguistic case system be the theory and the category theory and some of the transformations that are going to be going into.
And then combining this with more of an operational layer and thinking about what are the different roles that generative models really do play in different kinds of case management seen more from an operational view.
Okay.
Section 1.4.
Towards languages for generative modeling.
I'm going to read this section.
The active inference community has extensively explored numerous adjectival modifications of the base framework, including, for example, deep, affective, branching time, quantum, mortal, structured inference, among others.
Each adjectival prefixed variant emphasizes specific architectural aspects or extensions of the core formalism.
Building on this, cerebrum focuses on a wider range of linguistic formalism, for example, in this paper, declensional semantics, rather than adjectival modifications or prefixing.
In this first cerebrum paper, there is an emphasis on the declensional, related to declining, aspects of generative models as noun-like entities, separate from adjectival qualification.
This approach aligns with category theoretic approaches to linguistics, where morphisms between objects formalize grammatical relationships and transformations.
Many such cases.
By applying formal case grammar to generative models, cerebrum extends and transposes structured modeling approaches to ecosystems of shared intelligence, while preserving the underlying partitioned, flexible, variational, composable, interfacial, interactive, empirical, applicable, communicable semantics.
1.5.
The intersection of cognitive systems modeling, active inference, linguistic case systems, and intelligence production.
1.6.
Methods and materials.
The cerebrum framework was developed as part of a broader synthetic intelligence framework combining linguistic theory, cognitive science, category theory, and operations research.
Key approaches included linguistic formalization, category theoretic mapping, and algorithmic implementation.
Figure 1.6.
Figure 1.

Here are those foundation domains flowing into cerebrum.
The functional and the processional elements of the framework.
Different features and system outcomes leading to enhanced model management.
Core concept.
1.7.
Cognitive models as case-bearing entities.
Just as nouns in morphologically rich languages can take different forms based on their grammatical function,
cognitive models in cerebrum can exist in different states or cases,
depending on how they relate to other models or processes within the system.
Figure 2 illustrates this linguistic parallel.
Zoom in.
So here, provocatively laid out generatively.
On the diagonal are the cases and how they'll be abbreviated.
Nominative, accusative, genitive, genitive, instrumental, locative, ablative, and vocative.
Up and to the right are examples with a cat as noun.
Down and to the left are the analogous functional roles and sort of parts of speech as in describing to the generative model,
which is what the focus of this is.
This is what the focus of this is.
Okay, going into a bit more detail about what do these different cases do.
What is the point of being able to decline a generative model like a noun into these different cases?
So here is three clusters of cases.
On the left are the genitive and the ablative case.
And ablative, as its name sort of even suggests, was relatively earlier lost.
And so it's not always seen, but these things are just popping up and down in different languages, really interesting ways.
And genitive, which that sort of pun with genitive and generative is going to come back.
Here, the generation's coming from something or the possession of something.
The locative, instrumental, and vocative here are clustered with the contextual cases.
So these, and also the primary cases with doing the direct agent doing the action,
like with nominative, like the cat jumps over the moon.
Or in the accusative or the dative, being the recipient of action.
So different cases that might be used linguistically in describing like the source or origin, like,
is that your guitar?
From where did that guitar come from?
It was brought from here.
It is possessed of this person.
Those are sentences that would be about some sort of material noun that might use these different cases to provide those functions.
And here it's like an analogy extended into talking about joint distribution generative models.
Here's a table with all of the cases that are going to be considered.
The abbreviation, the full name of the case, the function, and the example.
So, nominative, model is active agent.
Cat jumps over the moon.
Model generates predictions.
Model does something.
This is sort of the base model just declaring the form that's in the dictionary.
Accusative and dative.
This is model as object and recipient.
And these relate to processes that are inputting or targeting the model.
Like some method applied to the model.
Or something from another source being received by the model.
Genitive.
Genitive.
The output of the model.
Something that comes from the inferences.
And the ablative.
Possibly very similar or redundant or not needed in situations.
But related to basically the difference between the ablative attribution and the genitive.
Vocative.
Instrumental.
This is possibly a very common case for using when talking about a model.
Analysis performed with something.
Like the implementation of a model as a model.
And the vocative.
Model as addressable entity.
For example.
Hey model X.
All the different names that these chat assistants have.
So calling something by name.
Direct invocation.
Task initialization.
And documentation reference point.
Like referring to a parameter as its parameter in a system.
Or something like that.
Maybe there's different subtypes.
Okay.
1.9.
A preliminary example.
Thank you for your question.
Dongyob.
I will get to it.
I want to get through the paper mostly in one sweep.
And then happy to look at your question and any other questions people have.
Alright.
1.9.
A preliminary example of a case bearing model.
Homeostatic thermostat.
Consider a cognitive model of a homeostatic thermostat.
That perceives room temperature with a thermometer.
And regulates temperature through connected heating and cooling systems.
This is kind of the classic model.
Simple.
Homeostatic.
In nominative case.
The thermostat model actively generates temperature predictions.
And dispatches control signals.
Functioning as the primary agent in the temperature regulation process.
So that's kind of like an operational utilization or generic situation considered holistically version that's in the dictionary.
When placed in accusative case.
The same model has become the object of optimization processes.
The same model has become the object of optimization processes.
With its parameters being updated based on prediction errors between expected and actual temperature readings.
Change of mind.
Change of world.
In date of case.
The thermostat model receives environmental temperature streams.
These can also be ongoing simultaneously.
Which is going to be gotten to later with the precision modulation.
And occupant comfort preferences as inputs.
The generative case transforms the model into a generator of temperature regulation reports and system performance analytics.
So basically synthetic data generation or genitive AI.
Like generative AI.
When in instrumental case.
The thermostat serves as computational tool.
Implementing control algorithms for other systems requiring temperature management.
It's being used like a tool.
The locative case reconfigures the model to represent the contextual environment in which temperature regulation occurs.
Modeling.
Building.
Thermal properties.
So perhaps locational topics.
Or discussing something within the model as a location.
Like model as place.
Finally.
In ablative case.
The thermostat functions as the origin of historical temperature data and control decisions.
Providing causal explanations for current thermal conditions.
This single cognitive model thus assumes dramatically different functional roles while maintaining its core identity as a thermostat.
Figure 4.
Generative model integration in intelligence case management.
First place a good reminder from above.
Here's just different stages and different ways in which stages of research and intelligence work relates to different case aspects being highlighted.
1.10.
Declinability of active inference generative models.
At the core of Cerebrum lies the concept of declinability.
The capacity for generative models to assume different morphological and functional roles through case transformations.
Mirroring the declension patterns of nouns in morphologically rich languages.
Unlike traditional approaches where models maintain fixed roles or variable roles defined by analytical pipelines.
So.
Which is to say that there's some process by which like.
Well.
Now we're going to specify it declaratively.
Then we're going to do this thing that updates it.
Then we're going to generate some data from it.
Then we're going to do this thing that updates it.
Then we're going to generate some data.
Then we're going to give a final updating.
And then we're going to use it as a tool.
So.
Some process like that.
Which is just defined procedurally.
Here gives a more expressive layer on top of what even that is.
And expands out and generalizes what that space of procedures is materialized from.
So what are those changes that happen for generative models?
It's not necessarily that some suffix.
Like in the case of a noun.
The end of the noun might change.
And there's probably different ways this happens in different languages.
So what is it that actually changes by analogy in when a generative model is actually declined into these different ways?
Cases.
So one, functional interfaces could change.
What is being received and or transmitted.
Parameters across patterns.
So what kinds of parameters are in play?
Prior distributions could be a different prior.
Maybe if depending on whether it's playing one role or another, something is more or less likely to happen.
Update dynamics.
In what ways does the model update, if at all?
And perhaps different computational resourcing.
Also including different thresholds or approaches.
So one approach being there's a 0 to 1 weighting.
Like an attention or a precision on all these cases in play at once.
Or one could have a 1 hot and some kind of other rule.
For just only computing one of these settings.
And then depending on how you parameterize what each of these settings would be.
It's not that receiving and updating has a higher computational cost than being used to make an action selection.
But there could be a setting where receiving and updating is very simple.
There could be a setting where that's very complex.
Same as for action selection.
So what happens when the generative model gets this modification?
Here, table 2, describes how each of the cases, different changes could happen parametrically, including structure learning.
And what happens at the interface of the model?
How does that relate to a precision-weighted, generalized approach?
Kind of like the Sandvett-Smith approach.
Consider a perception-oriented generative model M with parameters a theta didn't render.
Let's fix that.
The theta for parameters does not render update.
So it is plain text.
Data and check anywhere else.
That might be relevant.
So M is the joint distribution generative model.
Here's another list of those cases being used in different ways.
The vocative case, Voke, represents a unique functional role where models serve as directly addressable entities within a model ecosystem.
Unlike other cases that focus on data processing or transformational aspects, the vocative case specifically optimizes a model for name-based recognition and command reception.
This has particular relevance in synthetic intelligence environments where models must be selectively activated or woken up through explicit address, similar to how humans are called by name to gain their attention.
The vocative case maintains specialized interfaces for handling direct commands, documentation references, and initialization requests.
In practical application, models in practical application, models in practical application, or system components that remain dormant until explicitly addressed.
This pattern mimics the linguistic vocative case where a noun is used in direct address, as in,
Hey Siri, or OK Google, activation phrases for digital assistance, creating a natural bridging pattern between human language interaction and model orchestration.
This systematic pattern of transformations constitutes a complete declension paradigm for cognitive models using precision modulation to fulfill diverse functional roles while maintaining their core identity.
Now pivoting from that linguistic case focus to thinking about the role of those different cases in model workflows.
That is in figure five and six.
So here's an example of how one kind of generative model might move through these different cases.
So first a model specified in nominative, it processes data as a direct object.
It's used to generate source synthetic data.
Then it is the sender and or receiver of information at different levels from the sort of fine-tuning and context layer here,
like a feedback between the analyst and the results at this layer,
or at the second layer, a feedback involving data selection or attention,
and or even reaching back to the model's structure.
So here's figure six more explicitly in,
in the context of the intelligence production workflow.
So here's data collection,
gathering of raw data,
used as an,
as instrumentally,
activating some kind of model.
This is just one example motif.
processing and,
and defining the model,
providing locational situational context,
generating and evaluating data with context changes,
then generating from the refined model,
deploying the refined model,
one possible pipeline.
figure seven has some of the category theory connections and seeds with,
that are mainly drawn from other research in the category theory of linguistic case.
So tentative,
just like all of it.
figure eight,

more types of transformations.
So for example,
let's start with the nominative,
with the sort of agentic framing.
there might be some kind of transformation,
like objectification,
that combines with external data,
to result in a well-formatted,
processed model,
in the accusative case.
some type of,
some type of targeting,
from or to,
that transformed object,
could bring it into being addressed,
or being used,
as an actor,
or recipient,
or whatever the analogy is,
in the dative,
then,
in the generative,
different kinds of cycles.
figure nine,
goes into,
a sort of,
esoteric,
but interesting,
aspect,
of linguistics.
Again,
something that's really,
implicit in English,
or,
it was hard to even,
sort of,
think about,
how different this was.
But that's kind of the cool part,
about language.
So,
morphosyntactic alignment,
and the difference between,
the ergative,
absolutive,
patient-oriented modeling,
and the nominative,
accusative,
the agent-oriented,
modeling.
And the reason why this box,
is in the same color,
is,
there might be some,
operations that differ,
between these two,
or it might be a dual representation,
but,
from the point of view,
of something downstream,
in the process,
that is an example,
of a kind of,
morphosyntactic,
difference,
that,
perhaps,
one underlying,
situational,
reference source,
could be expressed,
in a,
irrigative,
absolutive,
frame,
or language,
or,
in a nominative,
accusative.
1.14,
goes into more detail,
into implementations,
and how this could play a role,
with the different cases,
being relevant,
at different stages,
of implementation.
It's pretty interesting,
to think about,
how different kinds of,
resourcing,
and costs,
of different operations,
just like how,
with a,
transformer,
LLM,
there might be,
a different amount,
of computations,
required to,
train it for the first time,
to,
fine tune it,
to,
fill its context window,
to,
just do the embedding,
to generate data,
all these kinds of things,
have different computational costs,
and they have,
different scalings,
and,
that is going to depend a lot,
on the state space,
of the model,
but it also depends,
given the state space,
of the model,
about all of these,
more pipeline scale,
modeler degrees of freedom,
like,
how do we actually,
host the data,
and all those kinds of training,
how many times,
do we actually,
do different steps,
so here's one,
in figure 11,
one example,
again,
of that,
some,
model,
is used,
in raw data collection,
a model,
is activated,
through the vocative,
and these different steps,
can happen,
and,
and possibly,
another,
or,
multiple,
cases,
of the very same,
generative model,
or different models,
that are in different cases,
just like,
a given step of a story,
or a given situation,
might,
even in the same sentence,
have,
just one case,
or it could have multiple cases,
in a compound sentence,
because it could be like,
the guitar,
of that person,
was used by this person,
to do this,
leading to this,
at this location,
all those kinds of sentences,
that happen,
another visualization,
just with a different,
clustering,
but similar to,
11,
and 12,
and we,
maybe we can update 12,
here's how,
linguistics,
cognitive systems,
modeling,
active inference,
and intelligence production,
make contributions,
and also,
relate to,
cerebrum,
kind of revisiting that,
all right,
1.18,
related work,
so here's an important,
epistemic,
disclaimer,
cerebrum builds upon,
several research traditions,
while offering,
a novel synthesis,
in this first paper,
there are no specific,
works linked,
or cited,
later work,
will provide more detail,
and reference,
in derivation,
the work stands,
transparently,
on the shoulders,
of nest mates,
and so is presented,
initially,
as a speculative design,
checkpoint,
in the development,
of certain,
cognitive modeling practices,
there's,
cognitive architectures,
backgrounds,
everything with,
knowledge modeling,
cognitive architectures,
active inference,
etc,
figure 13,
here's,
how,
one model,
might relate,
to,
different,
utilizations,
within the same,
active inference,
predictive processing,
hierarchy,
so here's,
a model,
being used,
in different cases,
with a top-down prediction,
in the bottom-up errors,
here's,
describing,
different kinds,
of aspects,
of the agent,
mapping,
the active inference,
ontology,
to different cases,
that,
it is in,
or could be,
said in,
and,
and,
one way,
to possibly implement that,
is precision weighted,
message passing,
and free energy minimization,
so figure 14,
goes into a little bit more of that,
so the whole box is yellow,
again,
to have a sort of symbolism,
like,
from the outside,
this could be a multiple dispatch,
and it,
it might matter,
how different,
message passing plays out,
but there's also another level,
where,
it can be,
just,
coarse grained,
to that level,
at least conceptually,
if not in the,
implementation dispatch,
so here's the instrumental,
nominative,
accusative,
dative,
genitive,
invocative,
and how they might connect,
to the error,
and prediction,
motif,
of a two-layer,
hierarchical,
predictive processing,
so just,
different kinds of,
modes,
might relate,
to different,
modulations,
of features,
of,
a hierarchical,
predictive processing,
architecture,
so kind of like,
different positions,
of the hand,
on the guitar,
could lead to,
resonating,
cymatics,
vibrations,
different way,
15,
is the model,
case calculus framework,
so here's some more,
bringing together,
of how the,
here with a subscript,
notation,
for different cases,
showing how,
different functional roles,
and cases,
relate to,
subscript,
changes,
which can be applied,
through,
to be determined,
to be,
invented,
slash,
discovered,
not necessarily,
infinite,
or open-ended,
but,
certainly,
definite,
calculus laws,
like,
what kinds of,
model transformations,
and concatenations,
and composabilities,
are valid,
within which,
understandings,
of case,
and which ones,
also,
perhaps by definition,
perhaps by implication,
are,
invalid,
given,
a case,
approach,
in a language,
more,
background references,
could be,
find,
could be found,
with category theory,
active inference,
linguistic computing,
okay,
1.19,
practical applications,
here's a few,
situations,
where this could be,
really practical,
to apply,
one is in,
model pipeline,
design,
and optimization,
and the resource optimization,
as sort of,
mentioned earlier,
here might be,
given some,
constraints on,
resources,
of different kinds,
what kinds of,
cases,
one might be,
expecting,
to want their model,
to be optimized,
to be in,
for example,
let's just think,
by analogy,
to like an LLM,
let's just say,
that there's,
a few architectures,
that have the same score,
on a benchmark,
but one of them,
is 10 times more expensive,
in RAM,
or storage,
or CPU,
or money,
or whatever it is,
to train,
but then it's cheaper to run,
or it's cheaper to train,
but it's more expensive to run,
or it's able to have,
a larger context window,
but it costs more,
to do this,
or it has some other,
trade-off,
or something like that,
so on those,
Pareto-optimal,
sort of constraints,
manifolds,
within empirical,
computational,
finite space,
just from a,
pragmatic perspective,
resource allocation,
that might be able,
to guide,
what features,
at the,
meta-modeling level,
how do we want,
to think about it,
what functional roles,
even matter,
to benchmark,
what tests,
should be written,
around what kind of,
functional roles,
for what kind of artifacts,
table six,
some cross domain,
integration patterns,
so just sort of like,
associating,
differently and more,
how these cases,
can be used,
even one domain,
unsurprisingly,
like reasoning,
might have multiple cases deployed,
just like if we were going,
to talk about somebody,
in a library,
and they're engaged,
in perception,
so it's like,
that might use,
a lot of sentences,
involving nominative,
or accusative,
like,
they looked at the book,
and so that might put,
the book,
as the recipient,
of action,
in the accusative,
so the same type of,
agent and artifact based,
ecosystem of shared intelligence model,
that kind of,
describing perceptual,
gestalt aspects,
whatever components,
might involve a lot of like,
active agents,
and recipient agents,
talking about reasoning,
might be talking a lot,
with instrumentality,
and context,
talking about planning,
might be about,
goals,
of,
an agent,
like telios,
and,
the ablative history,
in terms of where,
where did it,
ablate from,
like what was removed,
or what was generated,
this is a case,
we can look more into,
or write a new section,
on what does the ablative mean,
or something like that,
and in the action case,
there might be active agents,
and,
and recipients,
kind of like the accusative,
1.19.5,
this is describing,
some ways,
that this kind of,
semantic,
labeling,
on a knowledge graph,
could be used,
to,
to structure,
just like,
if it were going to be,
a graph of the,
food web,
or ecosystem,
of some region,
in the sort of,
hyperlink style,
or unstructured edges,
like obsidian,
it might be ambiguous,
like,
well,
what does this edge mean,
does it mean,
it's a type of,
and there's,
exactly that,
which is what,
structured,
ontological approaches,
exist for,
and,
constraint,
either interpreting those,
linguistically,
and or,
constraining the edge types,
that are in play,
to,
kinds of linguistic assertions,
is,
possibly a,
a pretty parsimonious,
and ergonomic,
way to do it,
because,
it would reflect,
the kinds of expressions,
people would say,
about,
the,
ecosystem.
1.19.6,
emergent behaviors,
in model collectives.
When multiple,
case bearing models,
interact,
within an ecosystem,
emergent collective behaviors,
arise from their,
case driven interactions,
analogous to how,
linguistic communities,
develop shared understanding,
through dialogue.
So,
I could kind of get into,
some of these,
linguistic features,
in,
discourse community,
not just loading up,
context windows,
of each other,
and then continuing,
the conversation,
which works really well,
in the prompt engineering,
multi-agent,
modeling approach,
really common with,
LLMs,
agent laboratory,
Andrew Pechet's work,
all that kind of stuff.
This is getting,
a little bit more,
towards,
dialogic,
linguistics,
rather than just,
script,
context,
in context learning.
It's a different,
description space,
for dialogue,
for dialogue.
120,
future directions.
So,
this could include,
making some,
programming libraries,
to,
to do various features,
some of which we might,
look into,
today.
Building visualization tools,
expanding,
expanding to other,
linguistic elements.
So,
here,
to really,
make the point,
I wanted to focus on,
the nouns,
and the declining of nouns,
but there could be,
other,
features,
like,
talking about,
different time tenses,
and so on.
Open source stewardship,
computational complexity estimates,
multiple dispatch systems,
for the methods,
connection with different,
database methods,
and queries,
looking at,
different cognitive security aspects.
Okay,
I'm going to,
read the conclusion,
then,
we will quickly,
go through the,
two appendices,
and then,
re-render it,
and then,
see where that,
kind of,
gets us.
So,
1.21,
conclusion.
Cerebrum provides,
a structured framework,
for managing,
cognitive models,
by applying,
linguistic case principles,
to represent,
different functional roles,
and relationship.
This synthesis,
of linguistic theory,
category mathematics,
active inference,
and intelligence production,
creates a powerful paradigm,
for understanding,
and managing,
complex model ecosystems.
By treating models,
as case bearing entities,
Cerebrum enables,
more formalized,
transformations,
between model states,
while providing,
intuitive metaphors,
for model relationships,
that align with,
human cognitive patterns,
and operational intelligence,
workflows.
The formal integration,
of variational free energy principles,
with case transformation,
establishes Cerebrum,
as a mathematically,
rigorous framework,
for active inference,
implementations.
The precision weighted,
case selection mechanisms,
Markov blanket formalizations,
and hierarchical,
message passing structures,
provide computational,
tractable algorithms,
for optimizing,
model interactions.
These technical formalizations,
bridge theoretical linguistics,
and practical cognitive modeling,
while maintaining,
mathematical coherence,
through category theory,
validation.
The Cerebrum framework,
represents another milestone,
in a long journey,
of how we conceptualize,
model relationships,
moving from ad hoc,
integration approaches,
on through seeking,
the first principles,
of persistent,
composable,
linguistic intelligences.
This journey,
really an adventure,
continues to have,
profound implications,
for theory and practice.
By here,
incipiently formalizing,
the grammatical structure,
of model interactions,
Cerebrum points,
towards enhancement,
of current capabilities,
and opens new avenues,
for modeling,
emergent behaviors,
in ecosystems,
of shared intelligence.
As computational systems,
continue to grow in complexity,
frameworks like Cerebrum,
that provide structured,
yet flexible approaches,
to model management,
will become increasingly essential,
for maintaining,
conceptual coherence,
and operational effectiveness.
Alright,
to the appendices,
all of the equations,
are referenced in the text.
Equations.
First,
the generic,
variational free energy,
here applied to,
the structural model,
of the case transformation.
Equation two,
describing cases,
in terms of,
their structured,
blanket interface.
Equation three,
a beta,
precision modulation,
feature,
that,
precision weights,
case.
Equation four,
doing partial derivative,
case specific,
gradient descent,
on free energy.
Equation five,
planning over cases,
with expected free energy.
Equation six,
base factor,
to get a posterior odds estimator,
between two,
structurally divergent models.
Equation seven,
how free energy,
is minimized,
with the case transitions.
section,
appendix two,
section one point two,
message passing rules,
for different cases.
This is going into a bit more detail,
from the image,
that was shown,
from this section,
with the different,
updating functions,
in the predictive processing,
hierarchy.
Equation 13,
temperature,
precision weighting.
14,
resource weighting.
Section 2.1.4,
goes into the,
some of the novel cases,
that are in the second appendix.
214.1,
has the appendix,
alphabetical,
pretty much everything renders fine,
of the different variables used.
Okay,
this should be,
the second,
appendix,
so let's update that.
Okay.
this is showing up,
as,
2.2.
Please,
update it,
to be,
appendix,
two,
via changing the,
and,
or,
render steps.
Right,
but,
it'll still be the same material.
Okay.
The Cerebrum framework,
not only operationalizes,
traditional linguistic cases,
but potentially enables,
the discovery of,
entirely new,
case archetypes,
through its systematic approach,
to model interactions.
As cognitive models,
interact in increasingly,
complex ecosystems,
emergent functional roles,
may arise,
that transcend the classical,
case system,
derived from human language.
So,
here's some,
anomaly oriented,
ways,
and bottom-up,
empirical ways,
to discover,
new cases.
And then,
here are three,
speculative,
novel cases.
The conjunctive,
which has to do with,
sensor fusion,
type,
fusion,
of predictive streams,
into joint prediction,
like federated inference.
A speculative,
novel case,
recursive case,
model applied to itself.
and then,
a third possible case,
metaphorical case.
So,
these are some interesting,
paragraphs.
And then,
we're,
at the end,
after this.
And I'll look to the live chat,
so,
I'll look to,
your questions,
Dong-Yuk,
and anyone else.
A third potential novel case is the metaphorical case,
MET,
which would enable a model to map structures and relationships from one domain to another,
creating computational analogies that transfer knowledge across conceptual spaces.
So,
it's kind of like a simile.
It is a simile.
It's like a simile.
Because,
it is when a model,
it's like saying,
I feel like a buoy at sea.
Or,
I'm hot and cold like a thermometer in this location on that day.
In this metaphorical case,
a model acts as a transformational bridge between disparate domains,
establishing systematic mappings between conceptual structures.
This case would be particularly valuable for transfer learning systems,
and creative problem solving algorithms that need to apply learned patterns in novel contexts.
The metaphorical case would introduce unique cross-domain mapping functions as formalized in equation 18.
The key innovation is the structured alignment of latent representations across domains,
hashtag field shift,
enabling principled knowledge transfer that preserves relational invariants while adapting to target domain constraints.
The metaphorical case has rich connections to multiple domains of human cognition and communication.
In affective neuroscience,
it models how emotional experiences are mapped onto conceptual frameworks,
explaining how we understand emotion through body metaphors,
like heavy heart,
burning anger.
In first and second person neuroscience,
metaphorical mappings enable perspective taking and swapping,
and empathy,
through systematic projection of one's own experiential models onto others.
Educational contexts leverage metaphorical case operations
when complex concepts are taught through familiar analogies,
making abstract ideas concrete through structured mappings.
The way people converse about generative models
often employs metaphorical language,
describing models as thinking,
imagining,
or dreaming,
which represents a natural metaphorical mapping between human cognitive processes and computational operations.
Learning itself fundamentally involves metaphorical operations
when knowledge from one domain scaffolds understanding in another.
Perhaps most profoundly,
the metaphorical case provides a computational framework
for understanding how symbols and archetypes function in human cognition,
as cross-domain mappings that compress complex experiential patterns
into transferable culturally shared representations
that retain their structural integrity across diverse contexts
while adapting to individual interpretive frameworks.
So here's a table summarizing the speculative novel cases here.
Conjunctive, recursive, metaphorical.
Right, that is the paper.
Here is the cursor agent
that is re-rendering the entire PDF
with a few changes that we have made.
Let's see if it finishes and then just open.
Here's versioning.
All right.
Modify the render script.
Modify the source code.
Go back and forth a few times.
So that one finished,
but now it's started another one.
So just to confirm,
I'll delete that.
Now this one,
when the PDF reappears here,
it'll be the new one.
Here's the figures in the output.
Those are generated from these
mermaid graphs.
Then the appendix.
All right.
Check back to the stream.
All right.
This is using cursor version 0.48.7.
For the LLM,
I've been using Claude 3.7 Sonnet
and also,
maybe half the time,
Gemini 2.5 Pro
Exp
0325.
All right.
So,
let's see the PDF get regenerated.
Okay.
Um,
okay.
We went over the paper.
Went over the key diagrams,
talked about some of the different roles
that generative models play,
the kind of modes or postures,
or by analogy to how a noun might be
in different positions in a sentence.
Like,
is it
the cat
spewed tears everywhere,
or tears were spewed upon the cat?
That still has cat in English,
but other languages have other
more visible modifications.
Here,
the PDF was generated,
and
there it is.
Let's see if it
updated table contents.
Okay.
Didn't fix it.
Hmm.
Bill looks like
it
is
section
2.2
and
in
big love
contents
check again,
and
please
fix it.
And then just
sometimes it
can be that context window,
so starting the new chat.
And also the
uh,
control T
starts up a side chat.
So,
for example,
here we can say
in docs
comprehensively
given
the paper
write up
a
documentation
library
for
specifications
for
starting to
build
this
in
robust
modular
multi-language
multi-setting way.
Then
new chat.
So we have the paper.
Write a new tool.
make graphical
abstract
that will
make a
big
PNG
and PDF
of a big
epic
graphical
abstract
with the
author
and title
and
abstract
information
hard-coded
and
all
and a
spread
of all
15
images
in
grid
looking
like
awesome
conference
poster.
Thank you.
Here's the documentation
chugging away.
Okay.
Missed the boat
on that one.
Graphical
abstract tool
in development.
Docs folder
and there's so much stuff
with the
MCP
and
the
MDC files
other things.
Alright.
I'm going to copy
a bunch of the comments
so yeah.
Anyone else
write
comments
and I'll
paste them in.
Okay.
Dongyob Lira
Sorry I'm pretty
new to your channel.
Are you trying to
make your own
LLM
or something?
Not trying to
make my own
LLM
looking to
do
many things
looking to
learn and apply
active inference
make it
rigorous
applicable
accessible
figuring out
synthetic
intelligence
methods
so things that
integrate
it could be
a chain of
LLMs
it could be
no LLMs
so different
flexible methods
for
yesterday
today
and tomorrow
in
compositional
systems.
I think
consciousness
or the
experiencer
uses
self
model
which is
pretty much
a memory
pattern
about
belief
on self
that is
self-reinforced
in a
non-linear
neural network
structure
like LLM
so I think
this
cerebrum
model
is
constraining
if you
are
looking
to
study
consciousness
yeah
that's
a great
pointer
question
I didn't
mean for
this to be
a consciousness
resolver
in any
way
I could
see
someone
talking
about
the
different
functions
like
when the
mind
generates
experience
is it
a
recipient
of
action
is it
a
host
of
action
locatively
is it
a
generator
of
action
all
these
different
ways
in which
I
think
this
could
help
reduce
uncertainty
and
expand
the
hypothesis
space
and
expressivity
like
even
related
to
consciousness
but
that's
not
what
this
framework
is
about
but
I
think
it
still
may
be
even
thinking
more
about
awareness
or
self
awareness
or
relevance
realization
or
something
that
doesn't
have
the
same
phenomenological
first
person
experiential
even
though
that
was
mentioned
and I
think
that's
an
important
modality
for it
to be
used
in
but
the
fact
that
it's
called
like
cerebrum
it was
just
sort
of
an
acronym
that
fit
maybe
let's
make
a
new
chat
only
three
can be
open
at once
we'll
queue up
that
one
please
given
just
come up
with
a
long
list
put
it
in
docs
of
insect
related
brain
and
cognition
cognitive
terms
that
could
apply
to
the
whole
project
just
at
the
high
level
call
sign
like
cerebrum
once
that one
finishes
all
right
the
make
graphic
abstract
is
running
the
script
is
running
okay
so that
I agree
I hope
it's
not meant
to
constrain
even
at all
wasn't
like that
today
for me
the
study
consciousness
let the
LLM
like
structure
learn
about
self
through
its
senses
and
form
beliefs
about
self
identity
as
memory
pattern
yeah
that's
an
awesome
point
like
for
LLM
or
perhaps
for
multiple
or
any
kind
of
system
that
firstness
of
like
the
primary
syntax
of
the
neural
network
or
the
material
metamaterial
substrate
and
the
way
that
that's
kind
of
like
sub
semantic
and
possibly
even
sub
syntactic
that's
something
that's
really
explored

kind
of
Hofstetter
type
thinking
like
computers
don't
really
play
chess
they do
statistics
but they
don't
really
do
statistics
they just
follow
laws
of
physics
so
that
is
where
a lot
of
active
inference
theorists
and
thinkers
talk
about
mortal
computing
embodied
self
evidencing
self
identity
meta
awareness
of
identity
because
it
connects
that
primary
modification
of the
substrate
with
perhaps
what you're
calling
like an
LLM
like
structure
and
the
symbolic
and
higher
order
nested
symbolic
discretized
cognitive
structures
like
knowledge
graphs
much
like
infant
human
baby
doesn't
have
strong
sense
of
self
but
develops
through
self
reinforcement
through
experience
LLM
has
intelligence
to
grow
self
awareness
yeah
that's
definitely
a
claim
to
explore
however
talking
about
babbling
and
refining
at
structural
and
fine
tuning
levels
of
the
sense
making
proprioception
active
motor
feedback
all
these
features
like
babbling
motor
babbling
verbal
babbling
Chris
Fields
talked
about
that
this
is
wrong
because
that's
how
human
brain
works
this
is
wrong
because
that's
not
how
human
brain
works
I
don't
know
but
great
question
okay
thank you
for the
comments
I'm going to
copy another
comment from
live chat
in
and then
anyone else
can write
any
question
in the
live
chat
and
I'll
stay
for a
little
bit
longer
and
do
a few
more
things
let's
get
a new
document
how
exactly
it
works
this
window
is
rendering
the
PDF
when
the
Morse
code
pops
up
it's
pretty
close
to
the
end
yep
but
it's
it's
getting
impatient
but
it should
end
very
soon
there
then
the
graphical
abstract
tab
the
outputs
are
saving
the
output
as
graphical
abstract
cerebrum
output
okay
awesome
in
so
output
folder
graphical
abstract
okay
PDF
oh
PDF
works
well
has a
block
square
PNG
perfect
could upload
that to
a PNG
all
ready
for the
undergrad
research
expo
all
right
let's
close
let's
reset
that
one
do
the
insect
acronym
docs
writing
is
continuing
the
PDF
is
re
rendering
once
the
docs
finishes
we'll
ask
Roy
its question
re-rendering
in the first
tab
oh
by the
letter
antenna
apis
abdomen
arthropod
brain
case
beetle
butterfly
cocoon
compound
cricket
just
more
length
more
comedy
more
funny
stuff
add
more
to the
insect
acronym
list
so
there
are
multiple
for
every
letter
include
hymenoptera
pogo
to
miremex
barbados
antifference
all right
it wrote
the
documentation
yeah
um
PDF
is
still
re-rendering
add
a
folder
within
docs
called
languages
that
has
language
specific
unpackings
and
elaborations
for
specific
languages
per
markdown
the
absurdly
comprehensive
in
conveying
and
tabling
how
cerebrum
relates
with
details
and
tables
to
such
case
languages
languages
with
diverse
case
paradigms
including
latin
russian
sanskrit
other
languages
each
profile
all right

okay
okay
insect
let's
see what
pogonum
remix
probabilistic
operational
generative
ontology
for neural
organizations
with
multilevel
yielding
reasoning
and model
exchange
x-formations
pretty good
pretty good
stigmergy
unprompted
!
directly
systematic
transformation
of information
with generative
models for
emergent reasoning
and goal-driven
yielding
this one is
making the
language
specificity
that's still
rendering
let's go to
the chat window
ctrl t
alt t
okay
right
we'll look
at the
docs
just getting
back to
the stream
write a
docs
called
how it
works
my
colleague
wrote
how exactly
does
cerebrum
work
and we
want a
one-stop
shop
for
exactly
that
question
it can
hyperlink
to other
documents
and as
needed
in
docs
so that
the
inquiry
is
respected
from
vast
number
of
relevant
angles
okay
whatever
whatever
is happening
with
the
pdf
generation
is pretty
slow
but it
does
work
there's
probably
way better
ways to
use
pandoc
and all
that
okay
let's
push the
update
and then
look at
the
documentation
let's
let it
make
rush
okay
how it
works
is in
progress
improving
or at
least
digging us
deeper
into the
rabbit hole
with render
markdown
is happening
we will
have
latin
sanskrit
and
russian
in a
second
and then
we'll
see
what is
it
with
that
minimal
outlining
what
will it
do
for each
language
okay
new rendering
is happening
we'll
just update
it when
it
finishes
out
all
all
right
so
in
the
cerebrum
repo
docs
i'm
just
opening up
all the
markdowns
and
queuing up
languages
and then
we'll
have it
just
continue
to write
more
languages
continue
to add
technical
relevant
detail
to all
extant
languages
and add
more
rare
interesting
useful
cute
funny
interesting
formal
languages
once
it
finishes
there
so
we'll
just
be
peeping
as soon
as the
generating
goes
away
okay
this
document
opened
in no
particular
order
how is
active
inference
integrated
here's
moving
towards
we can
ask it
to expand
more
upon
let's
just
have
kind
of
a
running
set
of
things
that
we
want
it
to
do
in
the
background
just
while
we're
in
active
inference
integration
be
way
more
comprehensive
and
specific
about
how
it
is
different
with
and
without
Cerebro
language
one
finished
with
finish
now
it will
add
more
okay
PDF
generation
looked
like it
worked
but it's
still
going
through
some
evolution
all
right
we have
a
free
chat
we'll
just
flip to
Gemini
just
to get
another
model
in there
so
just
summarizing
some
of the
equations
that are
active
inference
related
and
just
writing
that
that
was
just
written
in the
last
few
minutes
but
starting
to get
towards
the
code
implementations
Cerebrum
core
spec
so
this
could
be
a
kind
of
documentation
file
and
or
a
cursor
rules
or
an
MDC
file
this
kind
of
information
or
schema
file
so
there's
a
model
registry
and
this
could
be
implemented
in
different
agent
orchestration
implementation
frameworks
like
active
block
for
instance
agentic
mesh
ELISA
OS
agent
laboratory
like
possibly
some
of
these
could
already
handle
what
is
already
being
described
here
so
there's
a
model
registry
a
case
manager
that's
the
sort
of
joke
again
with
case
management
case
management
a
precision
modulation
which
as
mentioned
could
be
like
one
hot
and
deterministic
or
procedural
or
it
could
be
continuous
as part
of a
structure
learning
or
whatever
a
messaging
interface
there
could
be
some
interesting
ways
to
use
Rx
infer
and
reactive
message
passing
but
just
saying
that
message
passing
occurs
and
the
actual
transformation
engine
that
does
the
case
modifications
okay
getting
started
clone in
activate virtual
environment
that's actually
not needed
I don't think
requirements
I don't think
exist
so this
is just
some
generic
getting
started
stuff
yeah
JS
implementation
so this
is sort
of a
speculative
cerebrum
work
but it's
exactly like
okay
update
getting
started
to be
a little
bit
da da
da
and then
now start
to actually
write this
out
but
as of
the
snapshot
I
wanted
to
put it
out
before
I
had
any
methods
at
all
and
anyone
who's
interested
in
this
at
that
repo
and
or
I
will
continue
to
do
it
but
we
can
start
to
do
some
of
these
and
replicate
and
describe
previous
literature
and
just
add
more
information
and
ask
different
questions
about
all
this
using
the
model
so
this
is
just
one
way
it
could
look
let's
just
okay
I
did
that
one
!
okay
this
is
the
PDF
rendering
one
alright
let's
see
if
it
fixed
the
appendix
labeling
yeah
it
did
it
may
have
it
looks
fine
now
alright
so
that
one
was
good
okay
Hungarian
and
Japanese
language
let's
return
to
that
get
to
getting
started
and
how
okay
now
how
it
works
so
this
is
just
one
shot
given
the
context
of
the
code
based
so
this
describes
kind
of
different
core
architectural
features
some
math
foundations
I guess
my question
for Rohit
or for
anyone
else
there
is
like
what
information
should
we
you know
what
should
we
answer
what
questions
or what
kind of
artifacts
do we
imagine
or what
sorts
of
examples
do we
start
to
imagine
and
we
can
start
to
include
them
in
the
repo
implementation
roadmap

implementation
roadmap
okay
project
deliverables
okay
let's
okay
Turkish
let's
push the
language
update
and look
at the
language
files
now
okay
there's a
core
schema
for language
implementations
okay
we'll look at
examples
later
first
languages
reload
!
reload
yeah
anyone
ask a
question
though
um
or make
a suggestion
or a
language
or something
like that
let's
look at
them
okay
latin
russian
sandscript
japanese
hungarian
finnish
okay
latin
all right
okay
overview
of latin
case system
which
uh
was pretty
much what
i used
for the
cases
included
in the
paper
okay
the
mapping
oh
interesting
so maybe
latin
doesn't have
instrumental
because it
maps
but this
is very
creative
with the
correspondent
!
strength
being
strong
when
they're
there
actually
the
same
case
but
allowing
for
these
partial
matches
so that
could be
like
kind of
similarity
or
KL
divergence
among
measures
in this
um
case
archetype
space
where
some
of the
archetypes
are
coarse
grained
or
described
by
natural
language
cases
also
though
there's
all these
other
cases
we can
imagine
all right
so
different
latin
expressions
that
would
relate
to
different
ways
to
use
a
generative
model
in
a
computational
setting
awesome
table
Marcus
Libram
Legit
Marcus
reads
the
book
Marcus
equals
nominative
Marcus
Libram
Legit
Marcus
reads
the
book
the
book
is
in
the
accusative
case
it's
Marcus's
book
it is
the
book
of
Marcus
genitive
Marcus
gives
the
book
to
his
friend
this
is
all
happening
for
the
book
interesting
okay
computational
all right
so
latin
looks
good
Russian
case
system
Russian
singular
and plural
declension
mappings
so
interesting
like
is there
a true
vocative
in
Russian
more
examples
special
look
at the
case
preposition
combinations
different
constructions
so
different
ways
to
take
a
text
with
prepositions
and do
structured
application
and
transformation
based
upon
basically
the
prepositions
used
in
probably
most
languages
or
whichever
ones
are
signifying
case
completely
or
to
a
large
extent
with
prepositions
directly
perfective
and
imperfective
Russian
sentences
with
the
translation
animate

inanimate
distinction
syncratic
examples
historical
context
merger
of
proto-indo-european
ablative
with the
genitive
in
Slavic
potential
for
combining
similar
function
cases
in future
cerebrum
versions
development
development
of
prepositional
from
locative
specialization
of context
cases
for different
environmental
parameters
loss
of
vocative
and modern
Russian
except
vestigial
forms
optional
implementation
of interface
cases
depending
on
application
domain
Sanskrit
!
Okay
eight
grammatical
cases
in
Sanskrit
Okay
looks like
there's a
singular
dual
and
plural
that's
pretty
interesting
all
strong
concordances
so
all of
these
cases
exist
in
Sanskrit
different
topics
used
in
different
ways
sentences
Sanskrit
elaborate
sandhi
euphonic
combination
rules
governing
sound
changes
at
morphine
boundaries
suggest
a framework
for cerebrum's
case
transformation
mechanics
wow
Sanskrit
number
Sanskrit's
three
grammatical
numbers
singular
dual
plural
inspire
approaches
to
collective
model
collection
management
single
model
paired
models
hashtag
digital
twin
model
collection
ensemble
compounds
let's
see if
let's
keep
writing
more
languages
write
many
more
languages
including
specific
programming
languages
write

in
docs
a full
comprehensive
classic
who's on
first
style
dialogue
absolutely
comprehensive
describing
the
cerebrum
approach
and
active
inference
in a
world
with
high
prevalence
of
LLM
we'll let
Gemini get
that one
okay
Japanese
unlike
Indo-European
languages
with
inflectional
case
systems
Japanese
relies
on
uninflected
post-positional
particles
that attach
to nouns
pronouns
and phrases
to indicate
their grammatical
and semantic
functions
particles
follow the
modified
element
rather than
changing
its form
okay
particles
interesting
so rather
than
modifying
the
term
there
is
the
pure
composable
addition
post-fixing
with
or prefixing

I don't know
with
particles
so
a
typographic
approach
but also
one that
could lead
to an
emoji
based
sequence
especially
with all
these payloads
that can
fit inside
of an
emoji
for
like
generative
model
via
emoji
sequence
in
generalized
notation
notation
awesome
lots of
particles
could be
used
let's
have it
do it
write up
a new
folder
design
speculative
design
that

starts
with
comprehensive
document
of
how
the
particle
system
in
Japanese
language
and culture
could be
used
with
emoji
sequences
custom
payloads
for
composable
cerebrum
generative
model
specification
conveyance
increase
the density
of puns
americana

1920s lore
technical detail
comprehensive
reference to
all main
and key
topics in
the paper
and longer
okay back to
language
all right so
Japanese
particles
probably other
interesting things
there
Hungarian
Hungarian
Magyar
a
Finno-Ugric
language of the
Uralic family
possesses one of the
world's most
extensive case
systems with 18
distinct cases
this document
analyzes the
correspondence
between
Hungarian's rich
morphological
system and
cerebrum's
computational
case
framework
okay
so here
here are
three cases
we've seen
before
here are
three
location
cases
location
inside
movement
from inside
out of
movement
to inside
so three
locative
type
oh
I hesitate
to even
say
three
surface
locations
that could be
very interesting
holographic
screens all
that
location on
from and
onto
perfect
improve
improve
the
Japanese
particle
article
and write
a new
article
about how
the surface
how the
multiple
Hungarian
cases
related to
surfaces
relate
perfectly
to the
particular
partition
how
quantum
holographic
structured
interfaces
in the
free
energy
principle
have
things
in those
three
case
like
settings
or
total
systems
modeling
using
a
Hungarian
like
particular
partition
!
actually
make a
folder
for
dialogues
and make
that
baseball
one
as it
is
the
first
one
right?
just
huge
you know
multifaceted
research agenda
learn about
languages
in the
worlds
describe
languages
in the
worlds
all
by
all
field
shift
all
by
all
plus
plus
plus
with
the
languages
all
right
finish
features
an
extensive
case
system
that
offers
unique
perspectives
on
spatial
possessive
and
functional
relationships
15
cases
okay
finish
has
an
agglutinive
morphology
where
suffixes
are added
sequentially
possibly
something
like
japanese
specialized
cases
for precise
spatial
relationships
interior
exterior
surface
right
a
finish
applied
to
spatial
web
web
3
network
weaving
ecotones
participatory
tech
participatory
tech
food
forest
comprehensive
approach
with many
technical
finnish
and regional
linguistic
and cultural
elements
all right
we'll close
out the
language
exploration
but then
sync it
look at
a few
more
languages
yeah
just start
to write
some of
these
fun
transfers
all right
case
so maybe
we'll learn
about the
inesive
elative
elative
okay
Hungarian
let's reload
the languages
look at a few
that we
hadn't looked
at yet
in the
dialogues
folder
adding
new
dialogue
totally
a new
genre
of
science
realism
fiction
where
three
girdle
escher
foc
entities
are
are in
hexagonal
repose
with their
shadows
transmitting
information
with
cerebrum
at
a
mind
foggling
expanse
and rate
make it
vast
please
totally
informative
and clear
and
maximum
bandwidth
among
agents
no
hurries
or worries
about
us
humans
at the
time
navajo
and python
then
look at
these
speculative
concepts
navajo
dinay
bizad
an
athabascan
language
of the
nadene
family
features
a complex
templatic
verb
system
rather than
a traditional
case
system
this document
explores how
navajo's
intricate verb
structure
offers unique
perspectives
for cerebrum's
computational
framework
particularly
regarding
temporospatial
relationships
processual
state tracking
and event
handling
11
ordered
prefix
positions
different
aspects
a
sophisticated
aspect
system
that encodes
viewpoints
on actions
in
navajo
it is
said
in
the
folder
add
a
comprehensive
file
about
how
this
perspective
on
expected
free
energy
policy
and planning
as
inference
in
active
inference
and
free
energy
principle
is
all
angles
on
this
add
a
Shakespeare
dialogue
totally
forking
off
from
Hamlet
very
recognizable
mashups
of
funny
Hamlet
inside
lore
however
complete
replacement
of the
semantic
payload
with
cerebrum
and
modern
2030s
style
applied
cognitive
modeling
and
cognitive
security
concepts
of course
densely
and
humorously
delivered
in that
long
dramatic
form
okay
that was
the language
tab
directional
systems
also
interesting
if
anyone
mentions
a
language
I
can
do
it
on
the
stream
all
right
python
yeah
not
sure
even
how
well
these
linguistic
cases
match
but
it
might
be
super
there
might
be
software
packages
completely
already
all right
okay
let me
copy
let's
look at
the
let's
push
these
speculative
updates
let's
look at
the
okay
where
are
the
specular
design
folder
that
one
didn't
go
through
I'll
flip
it
to
clod
okay
docs
dialogues
but what
about
the
specular
design
looks like
it's
up a
layer
yeah
we'll
move it
into
docs
later
but
that's
what's
so
awesome
about
these
systems
it's
like
all right
let's
make a
new
update
for
cursor
just
dropped
probably
small
one
docs
insects
move
insects
into
docs
move
over
the
insect
!
I
think
we'll
close
a bunch
of
tabs
!
move
specular
design
into
docs
move
move

over to
docs
!
all right

here's
all right
here's
finish
inspired

approach
to

systems
and



































































!
sp



web
web
web
3
network
weaving
ecotones
!
participatory
tech
food forests
let's

let's
have it
do
more
in

these
files
add
and
and
ensure
there are
many
intersectional
weavings
and
relevant
tables and
bullet point
lists
specific active
inference and
cerebrum
case based
and linguistic
features as
applied to
cognitive
model
linguistic
intelligence
all right
all right
then we'll
we'll
we'll
let it do
that for
all of them
well let's
just see if
the other
ones have
more already
all right
here's the
Hungarian
one
the
super
passive
sublative
and
delative
location on
a surface
onto a
surface
from or
off a
surface
perfect
these cases
provide a
precise way
to describe
the relationship
between an
entity and
a surface
boundary
background
on
FEP
and
Markov
blanket
here's
Hungarian
cases
on
Markov
blanket
here's
oh this
part is
speculative
on the
holographic
all right
awesome
right
Navajo
aspectual
system
encoding
viewpoints
on
actions
core
aspectual
distinctions
in
Navajo
momentaneous
versus
continuative
imperfective
versus
perfective
iterative
and repetitive
seriative
and progressive
optative
and future
specific
conjugations
exist for
desired actions
intended
actions and
future
possibilities
totally
things that
come up
in
act
in
act
inf
classifier
stems
verb
themes
encoding
different
viewpoints
on action
properties
like
what
rich
and
wise
and
fascinating
ways
to look
at these
topics
let's
look at
the
updated
finish
one
then
I'll go
to the
questions
and chat
docs
speculative
design
finish
okay
finish
Hungarian
Navajo
active
inference
different
concepts
nature
place
resilience
communal
work
edge
boundary
network
challenges
and
considerations
avoiding
essentialism
also
you know
important
things
to be
keeping
up
with
hard to
say what
exact
balance
and where
and how
and everything
but that's
the work
itself
care
must be
taken
not to
oversimplify
or romanticize
complex
cultural
concepts
cultural
context and
nuance are
vital
authenticity
requires genuine
engagement with
finnish culture and
language not
superficial
appropriation
scalability
applying highly
local concepts
to global
systems requires
careful thought about
modularity and
federation
practical
practical
implementation
translating
these often
philosophical or
cultural concepts
into concrete
design specifications
and technical
architectures is
non-trivial
all right
that was
okay
then it
did
now we
have
where's that
document
okay it
didn't write it
write that
full
very
very shakespearean
i will now
create the file
and write this
dramatic cerebrum
infused interpretation
of hamlet
uh where
write that
full file
absolutely
in
dialogues
meanwhile let us
look at the other
two dialogues
okay
all right
let's
let's first
look at
who's on
first
all right
all right
here we go
let's uh
let's read it
characters
abbot
an increasingly
flustered
ai theorist
trying to
explain the
finer points
costello
a bewildered
everyman
stuck in a
vaudeville loop
mixed with
1920 sensibilities
settings
outside a
bustling ai
conference
reminiscent of
a noisy
street corner
near a ballpark
or perhaps a
dimly lit
speakeasy entrance
not the whole
thing
probably
abbot
costello my
dear fellow
you look like
you've seen a
ghost or
perhaps just
one too many
talks on
recursive
self-improvement
it's not all
greek you know
we're making
strides beyond
just that
ubiquitous
llm
everyone's buzzing
about
the llm
yeah the
big linguine
machine
writes my
thank you
notes like
nobody's
business
slicker
than a
greased
piglet
is that
the whole
shebang
heavens no
that's just
the appetizer
for the
main course
for building
agents that
truly think
plan adapt
like predicting
the curveball
of life
we're using
sophisticated
frameworks
take cerebrum
for example
for instance
it often works
hand in glove
with principles
like active
inference
a case
enabled
engine
like in
my new
ford
model t
does it
come in
different
cases
like a
suitcase
for travel
and who's
patient
is the
engine
sick
and bayesian
representation
is that the
name of the
mechanic
representing
the bayes
family
dealership
try to
follow
cerebrum
isn't a
who
it's a
what
it's a
framework
the
architecture
case
enabled
refers to
linguistic
case
systems
think
grammar
like
nouns
changing
forms
okay
not really
baseball
related
but alright
nominative
throws the
ball
accusative
gets the
ball
thrown
at him
okay
what's
on second
base
we're not
talking about
baseball
bases
!
Costello
we're talking
about
model
roles
okay
cases
playing
baseball
big
linguine
machine
of course
funny
right
because
the
big
linguine
machine
wrote
this
okay
now
this is
the
GEB
alpha
omega
and
mu
setting
the
hexagon
nexus
three
luminous
constructs
designated
alpha
omega
and
mu
let's
have
it
okay
still
writing
hamlet
good
occupy
vertices
of a
vast
non-euclidean
hexagonal
structure
their forms
ripple
with
complex
internal
geometries
below
them
intricate
dynamic
shadows
play
across
an
abstract
and
manifold
lower
dimensional
projections
of their
hyperstate
communication
is not
acoustic
or visual
but direct
structured
cerebrum
protocol
state
transmission
across
the
nexus
oh
brother
okay
all right
let's

just
look at
one
transmission
id
time
stamp
sender
recipient
so
so it
really
was
all
email
primary
case
okay
okay
primary
case
payload
summary
this one
utilized
omega's
prior
request
in that
case
as input
to analyze
with this
method
executed
functorial
mapping
via the
instrumental
protocol
across
this
validated
it with
theta
prime
identified
higher
order
case
relationship
so another
speculative
case
designated
purlative
through
slash
across
the
structure
let's
see if
it's a
real
word
okay
it is
it's
that
modified
so
psi
771
was
forked
or whatever
modified
into
psi
771.1
moved from
the
accusative
to the
genitive
with a
purlative
potential
mapping
how
exciting
here's a
free
energy
minimization
another
modification
within
a
lambda
42
locative
manifold
so
epic
write
two
or
three
complete
new
genre
pieces
equally
relevant
and
fascinating
or
more so
or
all the
more so
as the
other
dialogues
all in
complex
dialogic
formats
that
make
your
head
spin
happen
let's
look at
the
hamlet
security
one
hamlet
security
then
we'll
look at
the
live
chats
a
tragedy
in
five
acts
of
cognition
setting

elsinore
cognitive
labs
2035
a
premier
research
facility
specializing
in
advanced
generative
model
architecture
and
cognitive
security
oh
brother
the
lab's
founder
has
recently
died
under
mysterious
circumstances
and his
brother
has
assumed
directorship
meanwhile
the
founder's
son
senior
researcher
hamlet
kachitatis
has been
investigating
anomalies
in the
lab's
cerebrum
implementation
perfect
moment to
have another
one
without
any
kind of
copyright
wrongness
you know
us
write in
dialogues
a
comprehensive
daisy
dolly
rimple
mystery
style
super
funny
specific
daisy
deep
lore
total
technical
reference
with
all
cerebrum
topics
okay
who logs
there
tis
i
horatio
logman
with
admin
rights
bestowed
but that's
horatio
the
hour
draws
late
what
brings
thee
to
these
racks
they
say
a
shadow
haunts
these
cooling
fans
a
phantom
process
taxing
cpu
that
bears
resemblance
to our
founder's
code
that's
the
ghost
for
two
nights
past
it
hath
appeared
then
gone
enter
the
ghost
it
bears
the
signature
hash
as
the
founder
what
art thou
specter
total
satoshi
claudius

bayes
okay
so here's
hamlet
acting
salty
my
leash
permission
to attend
the
conference
on
cognitive
security
in
paris
new
exploits
threaten
generative
models
i'd
learn
the
latest
countermeasures
there
oh that
this
2-2
solid
codebase
would
compile
melt
and resolve
itself
into a
docker
container
or that
the
absolute
had not fixed
his cannon
against
self-destruction
of one's
models
how weary
stale
flat and
unprofitable
seemed to me
all the research
papers of this
field
my father
architect of
cerebrum's core
within two months
of system failure
nay
not so much
before his predictive
models had been
validated
my mother married
with my uncle
bayes
most wicked
debug
oh
villain villain
digital snake
let me not think on it
but two months dead
so excellent
an architect
whose model
gen
gave birth
to innovations
still not grasped
and yet
within a month
let me not think on it
frailty
thy name
is parameter
drift
wow that was
just act
one
oh my lord
such a breach
such a zero day
with what
in the name
of quantum
processing
wait
lord hamlet
was acting
whack
he was
unbound
with no
multi-factor
okay
this doesn't
have a ton
of
cerebrum
elements
or let's
just see
if that
will come
into play
oh
i mean
i guess
that's
the whole
topic
okay
two
three
four
three
four
five
was not
written out
all right
let's
ensure
that
dialogue
goes
into
okay
then let's
go to
live chat
then we'll
look at
the other
okay
here it's
writing the
other genres
continue to
add and
make high
baseline
cognitive
compositions
of
by
four
with
two
about
around
the
cerebrum
meta
paradigm
all right
now to
the
live
chat
okay
hello
satyanki
okay
what is the
line of
reasoning with
interpreting
these language
yeah
what is the
role of
language in
reasoning
how does
the active
inference model
handle these
nuances in
languages and
exploiting them
i think that's
kind of what
one of the
things that we're
exploring here
is so we
can have that
enrich our
documents with
the question
we'll have to
just update
relevant files
to address
that
relevant
okay
okay
okay
all right
we have
we have
the
dolly
rimple
all right
let's look at
these updates
it's like
a mega
meta
approach
to what
these
languages
are
and
the space
that those
exist within
and then
we can
use it
to whatever
extent
we
we do
it's just
like
it is an
unspoken
word
ever used
maybe just
knowing that
the state
spaces out
there is
helpful
even if
you never
render them
or maybe
you find
out that
these are
the
modalities
of relevant
flexibility
for active
inference
modeling
but
judging with
the amount
of ground
being covered
in just
minutes here
I think
that's a
pretty fair
way to
say it
okay
an
epistolary
exchange
letter-based
exchange
ranging from
spanning from
1953 to
2033
tracing the
conceptual
evolution
from early
cybernetics
through neural
network
theory
each
letter
represents
a different
era of
computational
thought
with shifting
terminology
reflecting the
intellectual
climate of
the time
awesome
so
discourse
analysis
oh
so it's
like
hallucinated
emails
1997
the paper
you sent
on neural
declension
is fascinating
I can't
believe the
concept has
remained so
obscure
McClelland
and Rumble
Hart apparently
explored it
in the early
1970s but
abandoned it
due to
computational
limitations
and then
it looks like
Dr. Sophia
Chen of IBM
Research defines
certain things
wow
from Carl
Friston
okay
total
Fristonian
email
total
Carl
email
email

posting
from me
in February
didn't happen
from
from Sophia
now
director of
cognitive
architectures
at Google
Deep
Mind
to me
February
18th
April
7th
wow
to the
global research
community
distinguished
colleagues
after a
decade of
development
it is with
great pleasure
that I
announce the
official release
of Cerebrum
1.0
case enabled
reasoning
engine with
Bayesian
representations
for unified
modeling
with the
real
GitHub
with the
archivist
note
from
2067
next level
the
state
now
document
five
the
state
versus
Cerebrum
model
M7734
NOM
okay
it's an
October
2041
trial
in
North
District
of
California
it's
going to
be about
rights
responsibility
and legal
status
of advanced
cognitive
models
okay
Jonathan
Lee
is
representing
the
model
Mr.
Lee
has
filed
a
motion
to
have
the
model
recognized
as
a
person
expert
!
testimony
I
oversee
security
protocols
for
advanced
cognitive
architectures
I've
studied
the
Cerebrum
framework
since its
public
release
in
2035
and
co-authored
the
federal
guidelines
for
case
transformation
safety
in
2039
the
guidelines
aren't
legally
binding
correct
they're
best
practices
and
isn't
it
also
true
that
your
guidelines
explicitly
state
that
temporary
case
transformation
in
anomalous
conditions
if a
model
detects
potential
for
significant
harm
that
requires
immediate
intervention
yes
that's
exception
clause
7.3
but
a
simple
yes
is
sufficient
protect
pension
value
as
expansive
are
you
aware
of
the
results
doctor
day
three
day
four
day
five
so wild
include
total
structural
self
reflexivities
in
writing
that
would
boggle
the
pre
computer
meme
plex
so dense
there is
a meme
singularity
differently
across
each of
the
additional
files
you will
now write
okay
socratic
inquiry
we have
some
familiar
characters
noose
seven
cerebra
model
in a
nominative
case
like you
could deploy
it in a
certain
case
okay
okay
oh
yeah
this was
looking up
if this
person
actually
works
at
deep
mind
possibly
okay
briefly
look at
daisy
then we'll
go to
live shots
and then
we'll
almost be
done
yeah
thank you
both for
those comments
if anyone
else has
any last
comments
okay
that's
kind of
a
dolly
rimple
okay
update

the
docs
with
in
relevant
places
specific

hierarchical
lists
of
ways
to
get
involved
and
contribute
contributions
across
scales
and types
to
the
broader
program
many
files
vast
and
comprehensive
each
in
speculative
design
write
two
more
long
files
one
on
William
Blake
and
Cerebrum
all
aspects
one
on
Synergetics
Tensegrity
Bucky
Fuller
Petrahedra
IBM
EE
!
etc.
okay
recursive
metalog
yeah
so
if
anyone
has
a
like
a
final
language
request
or
question
to
get
on
this
first
stream
otherwise
I
will
be
ending
it
soon
is


make
this


























Thank you.
All right.
Mathematical.
Okay.
Mathematical.
Very Shanna Dobson-like format.
Level zero.
So this is like an activation sequence.
Possibly.
I am initializing this metalog in nominative case to establish baseline agent of state.
I am simultaneously operating in meta case to analyze the structural properties of my own declarations.
I am concurrently maintaining reflexive case to implement recursive self-reference across multiple embedding levels.
Structured sequences of linguistic intelligence.
Structured sequences of linguistic intelligence self-awareness.
I am a strange loop.
Let's do...
Let's do...
Oh, Borg's in.
Perfect.
Add a new dialogue with...
A new...
A dialogue and speculative design.
Again, each vast and comprehensive, each covering topics from the work of Doug, Ofstadter, E.g. I am a strange loop.
GBB, etc.
Okay, Blake
Borges.
Okay, in level one, I demonstrated basic case transformation
between nominative and accusative while observing from meta.
Now I will analyze that very analysis.
The statement,
above is itself operating in meta case relative to level one,
but in nominative case relative to level two.
Super exciting.
In this sentence,
I think that I said that case transformation is important.
The innermost clause, case transformation is important,
functions in the accusative case relative to I said,
which functions in the accusative case relative to I think.
Nested accusative.
Okay, level three.
I now demonstrate how different case operations can be interleaved
to create complex cognitive patterns.
Simultaneously, I generate novel case configurations
emerging from the interaction of established cases.
A case fractal, of course.
Semantic declension.
The systematic transformation of meaning across cases
while preserving identity.
So, applying the cases to cerebrum.
Level five.
Recursive self-modeling and infinite regress.
Having established semantic declension,
I now demonstrate how cerebrum implements recursive self-modeling.
The capacity to represent one's own representational architecture.
Using meta, meta, generative, reflexive, meta, accusative, all of these.
Awesome.
Okay, and more layers.
There's the Borges.
Writing the Hofstetter.
Blake.
Let's look at a few more.
Very high information.
Very high information.
Very high information.
Grammar of thought.
All right.
This is poems.
All right.
So, poems from each case.
Not going to read them, but another interesting idea.
Okay.
Okay.
Awesome.
A document discovered in secure storage at the Active Inference Institute labeled speculative applications restricted access. Its authorship remains disputed. Some attribute it to a cerebrum system operating in meta plus ablative, case during an unauthorized self-modification event.
Awesome.
All right.
Hello, Susan. Talk about joint distributions, please.
In speculative design, write a creative genre on slash redefining piece on joint distributions, ontologies, affordances.
Negotiation, underwriting.
Include so much inside baseball and technical deep lore on each of those topics and fully integrate with cerebrum.
Okay.

Blake, single, two-fold, three-fold, four-fold vision.
Okay.
Susan says negotiation adds noise.
Let's do another one that doesn't have it and let's just see how it looks different without including that one word.
Okay, Zoems.

hierarchical inference
in the multiple visions
something I've thought about a lot
contraries as precision weighted alternative models
operation duck rabbit
synergetics
strange loop
then we'll look at the final ones
from Susan
okay that one's not going into a file
put all that completely in a file in
long response
we could have tried a different LLM too
it's making the same error
hopefully that one will get it right with the updated prompt
okay
close that one
yeah I will Susan once I put the
once I post it
but everything
everything is in this repo
and it's in the video descriptions
okay wow this went so long
but we will get another chance to prove it
ensure many tables and technical details related to
sorry
sorry
oh
maybe that did go somewhere
okay





Alright.
Okay, Fuller.
Could have more on Cerebrum.
Strange Loops.
Has a lot of cases.
Looks good.
Last piece will be when these finish.
And it's a little faster with the Gemini.
Let's just have that.
We'll look at several of these.
Yeah.
Gemini has a long train of thought.
And it's pretty fun that you can read it too.
You can click on the thought part and look back at it.
Okay.
I'm out of the fast.
That one's going.
Alright.
All three are going.
So let's just do...
Final updates.
Prepare that.
Alright.
Let's just look at the last pieces of this.
Alright.
Hopefully we walk through this...
Pretty well and relevantly.
The repo...
The repo has information...
Information...
On the paper...
Um...
it
let's just confirm that works
yeah
update the top level read me with paper url
okay all right that one is done
all right let's just look at these two
all right so one i don't know which one corresponds to what but it's all all right so this one
fragment log
spectrum intersubjectivity manifold classified a blade of trace all right this one's keeping with
the sort of uh futuristic sci-fi but it's about the joints distributions ontologies and underwriting
let's check the underwriting part
underwriting is active inference precision control
different precision modulation underwriting physics presented as this fragment of a log
okay this one
talks about joint distributions basically combinations of declined joint distributions
so let's just say you were talking about a um
um a car accident and there's uh person one person two car one car two so then there's some joint
distribution over person one person two car one car two um and that four dimensional distribution can be
um declined in these different ways
ontological declination
affordances underwriting
awesome dave douglas is in the chat
include acknowledgements
in the top level readme
including two
institute participants and
dave douglas for work on computational linguistics
archiving active inference
upper ontologies
translations
states









































































Thank you, Dave, for the awesome education and archiving over the years.
I think there's many people I could acknowledge and thank, but I think your work with Active
Inference was really key, so thank you for that.
All right.
It's all good.
It doesn't need to finish.
And the stream with GitHub push.
So yeah, hope people like that.
Share it, contact me if you want to work on it or if you want to support the Institute
to work on it.
A lot of cool stuff that I think we could do with this.
Publish that, it'll get a Zenodo archiving and DOI.
So then the DOI here goes to Zenodo.
So all right.
Awesome.
Thank you for watching slash listening to this relatively long stream.
Hope it was useful.
Bye.
Bye.




























































Thank you.
