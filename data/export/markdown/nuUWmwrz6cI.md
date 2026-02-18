---
title: "ActInf Livestream 055.0 ~ "Realising Synthetic Active Inference Agents” Part I & Part II"
category: "Livestream"
series: "Livestream_055"
episode: "0"
speakers:
  - "Part I & Part II"
duration: "1:34:22"
url: "https://www.youtube.com/watch?v=nuUWmwrz6cI"
views: 464
exported_at: "2026-02-18T22:37:37.916878+00:00"
format: markdown
---

# ActInf Livestream 055.0 ~ "Realising Synthetic Active Inference Agents” Part I & Part II

All right, hello and welcome everyone.
It is October 24th, 2023, and we're an ACT-INV livestream number 55.0 on realizing synthetic
active inference agents.
Okay, welcome to the Active Inference Institute.
We're a participatory online institute that is communicating, learning, and practicing
applied active inference.
You can find us at some of the links on this page.
This is a recorded and an archived livestream, so please provide feedback so we can improve
our work.
All backgrounds and perspectives are welcome, and we'll be following video etiquette for
livestreams.
Head over to activeinference.org if you want to learn more about participating in livestreams
or other activities.
All right, well, we're in livestream 55 series with a goal to learn and discuss these two
very interesting papers on realizing synthetic active inference agents.
Part 1 on epistemic objectives and graphical specification.
Part 2 on the variational message updates.
As with all videos, it's an introduction for some of the ideas, not a review or a final word.
We're going to introduce ourselves, then jump into a fairly lengthy background section that
will prepare us to ask the questions and get to a place where the paper's contributions can
be figured out.
So, let us begin with introducing ourselves and saying hi and saying maybe something that
was exciting to us or made us want to participate in this series.
So, I'm Daniel.
I'm a researcher in California, and I was interested to go a little deeper on message passing.
It's something that's brought up a lot in the textbook and implicitly in other papers,
but this was an opportunity to tackle it head on.
And I'll pass to Bert.
Yeah, so I'm Bert.
I study civil engineering in the Netherlands.
And I struggle with the math of active inference.
But recently, I picked up reinforcement learning.
And together with this paper, I think it really helps.
Jacob?
Hi, I'm Jacob.
I'm also a researcher in California.
And I'm really excited about this paper from a number of different angles.
I guess the graphical notation and the notation that the paper introduces, I think, can have
really profound impact on the field from both a computational and a theoretical viewpoint.
And I'm interested to learn more about the implications of the new notation for the research.
Yeah, new notation just dropped.
Okay.
There's a pair of papers, as mentioned, and the information is here.
So, each of us can phrase the big question that brought us to the paper.
But I wrote it this way, which is, right there in the title, there's at least a triple play,
a triple pun tondre.
And there's a diad of papers.
So, what is this realizing in the context of the title?
Well, in one sense, we're realizing something in terms of implementing it or manifesting it.
They're deploying something that is being realized.
So, there's an accomplishment sense of realizing.
Also, the work calls attention to our own realizing process, our relevance, realization,
how we come to appreciate and interact with synthetic intelligence.
Ours.
And then, we're also talking about building agents that do some kind of realizing in themselves,
like realizing agents in that sense.
So, what kind of inning starts off with a triple play?
I don't know.
Bert or Jakob, what big questions brought you to the paper?
What do you think the paper takes on?
I think in terms of creating scalable active inference models that are reproducible across a variety of settings is quite exciting.
So, maybe realizing in that sense across a number of different domains is part of the meaning here.
And, of course, the triple play that we were exploring with our own work from going from just a simple graphical representation
to a mathematical description of the generative model and the algorithm for message passing and updating the generative model through time
to then a code implementation that can be deployed in various dynamic settings.
That is also what I think is an important part of this paper.
Oh, yeah.
Oh, yeah.
And for me, especially as not an expert on active inference, but someone who is more interested in applying it,
their work on working towards a PyTorch of active inference is really valuable.
And I think their way of deconstructing the mechanisms of expected and variational energy and to combine them into one function makes it,
simplifies it a lot, I think.
Cool.
So, we're going to look deeper at the papers, of course, soon.
But just a few of the aims of the paper.
Part one, they construct a purely synthetic approach to the active inference framework,
motivated from the point of view of engineering rather than neurobiology.
And we're going to talk about what synthetic is.
And in part two, they use a variety of technical phenomena, variational calculus, message passing,
and reactive programming to simulate a perception action cycle on the T-MACE.
Okay.
One of you, would you like to read the first abstract, and then the other can read the other abstract.
Whoever wants to go first.
I can read the first one.
So, the free energy principle, FEP, is a theoretical framework for describing how intelligent systems
self-organize into coherent, stable structures by minimizing a free energy functional.
Active inference is a corollary of the FEP that specifically details how systems that are able to plan for the future agents
function by minimizing particular free energy functionals that incorporate information-seeking components.
This paper is the first in a series of two where we derive a synthetic version of active inference on free-form factor graphs.
The present paper focuses on deriving a local version of the free energy functionals used for active inference.
This enables us to construct a version of active inference which applies to arbitrary graphical models and interfaces with prior work on message passing algorithms.
The resulting messages are derived in our companion paper.
We also identify a gap in the graphical notation used for factor graphs.
While factor graphs are great at expressing a generative model, they have so far been unable to specify the full optimization problem, including constraints.
To solve this problem, we develop constrained Forney-style factor graph, CFFG notation, which permits a fully graphical description of variational inference objectives.
We then proceed to show how CFFGs can be used to reconstruct prior algorithms for active inference, as well as derive new ones.
The latter is demonstrated by deriving an algorithm that permits direct policy inference for active inference agents, circumventing a long-standing scaling issue that has so far hindered the application of active inference in an industrial setting.
We demonstrate our algorithm on the classic team-based task, ensure that it reproduces the information-seeking behavior that is a hallmark feature of active inference.
Thank you.
The latter is the final step of the final step.
The final step is to embrace the basic approach to synthetic active inference agents.
By message passing on free-form Forney-style factor graphs, FFGs, a companion paper part one introduces a constraint FFG notation that visually represents free energy objectives for active inference.
The current paper derives message passing algorithms that minimize generalized free energy objectives on a constraint Forney-factor graph by variational calculus.
A comparison between simulated BAT and generalized free energy agents illustrates synthetic
active inference behavior on a team-based navigation task.
With full message passing account of synthetic active inference agents, it becomes possible
to derive and reuse message updates across models and move closer to industrial applications
of synthetic active inference.
Great, thank you.
So here's the roadmap, section titles of the first paper.
Here are the section headers of the second paper.
So before we jump into the background and then the papers, let's just have one last train
stop.
What is synthetic?
And what's synthetic about active inference?
So as it being 2023, we went to the language model and we asked for some adjectives that
are in the semantic neighborhood of synthetic.
And you can see them here.
Artificial, lab-created, synthetic, counterfeit, phony, deceptive, inauthentic, unnatural.
A lot of these are somewhat negative associations semantically.
So how does synthetic come to be meaning something negative or deceitful?
And then in what ways is that a similar or a different sense of synthetic than referring
to the unified compositionality of something that's blended?
And similarly, we could talk about artificial, like artificial intelligence.
Is that artifice, like crafted?
Or is it artificial, like phony, bogus, false?
So in the context of the paper, there's probably a bunch of different ways that we can draw out
with the authors and a little bit here too.
What is being synthesized?
If you have any thoughts on this, but what else might be synthetic?
It might refer to something that's not just a hypothetical, like a real synthesis, a realized synthesis.
It might refer to information risk and synthetic intelligence.
It might refer to synthetic judgments.
Those whose predicates are wholly distinct from their subjects.
And then recently at the Topos Institute, there was a great talk by Jonathan Sterling,
synthetic domains in the 21st century.
So there's a lot of very interesting differences and ways that synthetic is used.
Do you of us have any preliminary thoughts on what's synthetic about these papers?
I think, I guess, building on what you already said, part of the synthesis could be the
decreasing the gap between the mathematical description of a model and its graphical representation
and its subsequent code implementation.
So the focus on graphical models on constrained phony cell factor graphs
combines the aspects of generalized free energy or bethe free energy,
which is motivated by a phony cell graph structure with the actual implementation of a synthetic agent
or an artificial agent in code or in synthetic settings,
which themselves are trying to model some part of reality.
Okay.
Cool.
We'll explore.
Okay.
So to Bert for background part one, and thank you for all the work leading up to this dot zero, Bert.
So take it away with the background.
Just let me know when to switch slides.
Yeah.
All right.
So for the background of part one, it will delve into what are base graphs,
and how do you do inference over these graphs,
and then the authors use, make extensive use of our content to optimize over the graph,
the phony vector graph,
and then some miscellaneous stuff that will be relevant to the play smaller parts in the paper.
All right.
Next slide.
So first off base graphs, working up eventually to phony graphs,
but starting with the simplest one, which is just a Bayesian network.
And then the classical example is the earthquake network.
So you can, so each circle is a random variable, and they represent a particular stake.
So whether, for example, the alarm goes off, yes or no.
And these variables can be continuous or discrete.
And so the total generative model is the joint probability of all these random variables,
and you can factorize them so they only relate to one or two or several others,
at least a limited set of other variables.
And then moving on from that is the hidden Markov model,
where you add time.
So you have multiple time steps.
So in this case, X0, X1, X2.
And this works under the Markov assumption,
which is that all the relevant information of the past is in the current time step.
So you only need to consider the current.
And on top of that, you can only, you cannot observe hidden states directly.
So you need an observation error.
So that's the E.
And then the next step, building on top of the hidden Markov model,
is the partially observable Markov decision process,
which is a lot of words.
But really, it's the same where you have a hidden state,
S, with an observable state,
and you transition from states.
But now you add an action.
And the action acts the policy.
And it acts on the B, the transition.
So for an example would be,
I expect S1 to have a certain value given my action.
And this observation O2 should be in line with that.
And the policy selected using the expected free energy.
All right, next slide.
And then how do you actually figure out the values of a base graph?
And that requires inference.
And there are multiple ways.
So the first one is exact inference,
which is what you would do if you calculated by pen and paper,
which is really only practical for small discrete models,
like the example model on the last slide.
And if you want to go to bigger models, more complex models,
you need approximate inference.
And within that Monte Carlo sampling is a key pillar,
and there are a bunch of algorithms that apply it, that use it.
So the core idea is the same.
But the core idea is the same.
You sample many times from an idealist distribution
to approximate another distribution of interest.
Another method is method,
which you may be familiar with,
is variation of free energy,
which active inference uses a lot.
And then you indirectly minimize the difference
between two distributions using the KL divergence.
You try to minimize the KL divergence,
but you cannot do that directly.
So instead,
you maximize the elbow.
And this works with a family of distributions.
And a family is,
for example,
Gaussian or exponentials,
which you have to pick one.
And embedded free energy works on this.
It's also a free energy,
but it has the assumption
that only local interactions matter.
So instead of going over the entire generative model,
you only look at one factorized part at a time.
And optimization,
which is also used in the paper
to find some parameters
and is Newton's method.
But you have a function
and you want to know
where this function goes through the x-axis.
So you can take the slope
and iteratively take more slopes
until you get at approximately the point
where it goes through the x-axis.
Next slide.
And then others use Lagrangian paper.
And so to quickly introduce this,
it is a method
to describe an objective function with constraints.
So in the first derivative of the Lagrangian,
if you set it equal to zero,
those are the optimal points.
So that would be where the blue and red curve
intersect in this picture.
And the Lagrangian multiplier lambda
is the rate of change
the objective function would change
if you relax the constraint.
So in this example,
it would be the same
as changing to constant B
of the red function.
So concretely,
if the lambda was positive here,
then increasing B
would result in objective function
also increasing.
So you have some leeway to work
to improve the function even further.
So you can optimize more.
That's what it's saying.
All right.
Next slide.
And as for miscellaneous stuff,
so the term entropy is used a lot,
especially in terms of epistemic foraging.
But for now,
it's just a measure
of how uncertain a distribution is.
And in general,
sampling and uncertain distribution
gives you more information
than sampling a certain one.
For example,
if it rains every day,
seeing rain again doesn't tell you much
because it rains every day anyway.
A direct delta function
is a probability distribution
that is one for a single point
and zero elsewhere.
And then a statistical moment.
I will just read,
in mathematics,
the moments of a function
are certain quantitative measures
related to the shape
of a function's graph.
If a function is a probability distribution,
then the first moment
is the expected value,
so the average,
the second is the central moment
of variance,
the standard deviation.
The third is the skewness
and the fourth is the kurtosis.
And finally,
the coolback-Leibner control,
which is a term from control theory,
which basically attempts
to make a system converge
to a set prior
and adjust it
by minimizing the KEL divergence.
Yes.
Yes.
Thank you.
Great background.
So that kind of speed runs
Bayesian stats
first layer.
Now we're going to head
into a second layer
of background
that's going to bring us
into the Forney graph space.
and after the second
background part,
we'll be in a position
to understand
two papers a little better.
So,
here's the big picture
on background part two.
Even with all of background
part one
in hand,
there's also some more
modern,
important
ACT-INF
as well as
non-ACT-INF
related advances
that are going to get us
up to speed.
So,
for a lot of the concepts
here,
we're just overviewing
it first
and then we'll be
talking more to the authors
about them.
And so,
I'll take a more
narrative overview
of recent updates
and then we'll steer
towards the technical.
So,
first,
graphical models,
active inference,
and belief propagation.
Over the last years,
Carl Friston et al.
have been collaborating
with the lab
and collaborators
of Bert DeVry.
And around 2017,
they released
several
very important
papers.
One was
a factor graph
description of
deep temporal
active inference
and another was
the graphical brain
belief propagation
in active inference.
So,
as Bert alluded to
earlier,
many of the
operations or
formalisms of
active inference
can be understood
as manipulations
of parameters
or variables
that might reflect
data,
observations,
priors,
precisions,
different kinds
of variables.
And that
is given
exact form
in the
graphical model,
specifically the
Bayesian graph.
And here we see
the familiar
figure 4.3
from the
2022
textbook.
Now,
the nodes
on that
graphical model
are variables
and edges
are their
causal
or their
informational
relationship.
And so,
especially after
Perl et al.
and the causal
modeling
developments
in the
1980s and
90s,
this was
adapted into
a probabilistic
or cybernetic
setting where
certain nodes
on this graph
were associated
with action,
with perception,
with cognitive
phenomena.
And so,
this is a
causal model,
a Bayesian
graphical model.
It's the kind
of thing that we
see in very
many active
inference papers.
Now,
the Bayesian
graph is
awesome.
It allows us
to tackle
some really
challenging
compute problems,
get a lot
of semantic
interpretability,
and so on.
However,
there's also
a few
limitations
or challenges
in execution.
So,
first,
just epistemically,
there's some
side information
that is needed
to provide
in order to
get to a
fully reproducible
Bayesian
graphical
simulation.
And Livestream
54 shows
how that
information is
provided for
formally by
category theory.
But,
more to the
pragmatic point
for this
discussion,
in actual
computational
execution,
whether you're
running that
Bayes graph
on a single
core,
single thread,
or whether
you're using
multiple
computing
elements,
a given
or a
particular
generative
model must
be implemented
in a certain
way or
order.
If we were
doing a
single agent
or a
multi-agent
simulation,
we might
wonder,
so should we
update the
perception of
everybody and
then let
everybody make
action?
Or should we
do action and
perception of
number one,
then number two,
then number three?
But then isn't
that unfair?
Because then isn't
one of them always
getting to see
and act first?
And so on.
So,
just drawing the
graph doesn't
give you the
actual order of
operations to
carry it out
reproducibly.
So,
that underspecification
of the
Bayesian
graphical
logistics or
scheduling leads
to a lot of
degrees and
freedom in
model deployment.
Now,
this might be
an issue or
not be an
issue for
any given
task.
However,
whether you
use an
off-the-shelf
or a custom
solution to
address this
challenge,
these different
approaches might
take time,
they might not
transfer,
they might not
be general,
and so on.
Also,
there might be
different simulation
outcomes or
different computational
costs that
happen when you
implement the same
graphical model
differently.
So,
that limits
high reliability
use and also
transfer.
And then lastly,
kind of related,
the computational
complexity estimations
are difficult to
understand just by
looking at the
Bayes graph.
It'd be really nice
if there was a
way to have
the model and
then know how
much it's going to
cost or take
to run.
So,
enter the
Forney factor
graphs.
In 2001,
Forney wrote a
technical paper
called Codes on
Graphs,
Normal Realizations,
just like normal
2001 stuff.
And this introduced
some fundamental
components.
Let's ask the
authors and find out
what exactly those
fundamental moves
were.
But,
what was introduced
led to the
development of what
is now called
a Forney factor
graph,
FFG,
or a normal
graph?
Again,
another interesting
question,
how is normal
being used here?
The Forney factor
graph representation
is dual or
informationally
equivalent to
any given
Bayesian graph.
Importantly,
though,
FFGs enable
message passing.
Message passing
provides node,
local,
and whole graph
scheduling logistics
for messages
in a way that
allows for more
tractability in
execution.
Importantly,
these messages
are being passed
amongst variables
at a very granular
level.
This is not
referring to
two bounded
agents sending
each other a
postcard,
simply.
The network
or the graph,
it's a very
general data
structure,
so it's not
surprising that
we're going to be
encountering multiple
kinds of graphs,
but it is
relevant to
know which
kinds of
graphs we're
talking about.
Because this
FFG representation
can be applied to
anywhere a
Bayesian graph
is used,
people have
applied both
Bayesian graphs
and, to a
lesser or more
recent extent,
40-factor graphs
to a bunch of
different statistical
problems like
filtering,
smoothing,
prediction,
MDP,
POMDP,
and so on.
So, to
kind of
lock this
in,
here we see
on the right
figure 7.3
from Par,
Pizzullo,
and Friston's
textbook.
So this is
the standard
discrete-time
partially
observable
Markov decision
process,
and on the
left here
is a figure
from the
graphical
brain
paper of
2017.
So across
the top,
these two
Bayesian
graphs are
actually
identical.
They're the
same exact
type of
graph,
and they're
both the
same
Bayes
graph.
And then
the 2017
figure shows
that that
Bayes
graph has
this one-to-one
relationship
with a
Forney
factor graph.
What is
the difference
with a
Forney
factor graph?
Why do we
need to have
a different
format to
describe what
might at
first glance
appear to be
the same
information?
Let's go
to graphical
brain
2017.
We use
graphical
representations
to characterize
message passing
under deep
generative models
that might be
used by the
brain.
We use
three sorts
of graphs
to emphasize
the form
of generative
models.
One,
the nature
of Bayesian
belief updating,
two,
and how this
might be
accomplished
in neuronal
circuits,
three.
So here's
the three
sorts of
graphs
that they're
going to
talk about.
First,
Bayesian
networks or
dependency
graphs.
That's the
one that we
see the most
commonly.
Nodes
correspond to
unknown
variables.
Edges denote
dependencies
amongst
variables.
Thorney
factor graphs
have nodes
that represent
local functions
or factors
of a probability
distribution over
random variables,
while edges
come to represent
variables per se,
or more exactly,
a probability
distribution over
those variables.
And finally,
neural networks
have nodes
that are
constituted by
the sufficient
statistics of
unknown variables
and other
auxiliary variables
like prediction
errors,
while the edges
in those graphs
denote an
exchange of
the functions
of sufficient
statistics.
Crucially,
these graphical
representations are
formally equivalent
in the sense
that any
Bayesian network
can be expressed
as a factor
graph,
and any
message passing
on a factor
graph can be
depicted as a
neural network.
However,
as we will see
later,
the various
graphical
formulations
offer different
perspectives on
belief updating
or propagation.
So this is a
very rich
topic.
This background
section was to
say that
Forney graphs
have a
different
style or
format than
Bayesian graphs.
However,
they exist in
this dual
relationship.
So there's
things like
algorithms,
procedures that
you can do
on FFG
that you
can't do
on Bayes
graphs,
but it's
all good
because you
can go from
the Bayes
graph to
the FFG
representation
and then
implement some
procedure on
the FFG.
So,
let's get to
the papers.
The background
one and
background two
sections have
got us to
perhaps the
point where
we're very
excited to
see how the
authors
implemented
fully
synthetic
active
inference
agents
using
message
passing
logistical
and
operational
scheduling
algorithms
on
40-factor
graphs
representing
Bayesian
graphical
models
crafted to
calculate
a
constrained
Bethe
free
energy
as a
generalized
or unified
free energy
imperative
unifying the
variational
and the
expected free
energy
for
sense
making
and
decision
making
inactive
inference
agents.
So,
now,
we're heading
into another
double movement
of the
coming two
papers.
The first
paper is
itself going
to be like
a background
and a
notational
paper,
but also
one that
adds to
the literature.
And then
the second
paper will
make the
addition on
top of
the advance
of the
first paper.
So,
a lot of
material,
let's go
into the
first paper.
Bert.
Yes,
so,
for the
first paper,
we'll be
going over
chapter by
chapter.
To start
with setting
up the
Lagrangian,
then defining
the epistemic
objective and
how to
include it
in a
synthetic
agent.
Then in
chapter 4,
the layout
what it
means,
what Lagrangian
active
inference means.
In chapter 5,
they
describe the
notation for
the constrained
for any
factor graph.
In 6,
they highlight
why the
original
generalized
why
classical
active
inference
and the
original
generalized
free
energy
algorithm
are special
cases of
the Lagrangian
active
inference.
So,
of their
definition of
the
for any
factor
graph.
and then
in 7,
they do
an
experiment
for
policy
inference.
And then for
chapter 2,
the Lagrangian
approach to
message
passing.
So,
as Daniel
described,
phoney
factor graphs
represent a
factorized
function over
variables,
which you can
see in
equation 1
and figure
1.
So,
on the
left,
you see
equation 1
that shows
per node
where V
is,
so A is
a node
in the set
of all
nodes,
V.
And so,
on the
height,
you can see
the image
which says
that each
node is
a factor
of all the
variables,
and the
variables are
on edges,
and that's
really important.
And as
mentioned in
the background,
approximate
inference is
used,
in this
case,
variational
inference.
And so,
we start
with a
free energy
function,
an equation
3 on
the left,
which is
used to
approximate
variational
distribution,
Q star,
and Q star
is the
optimal
distribution
that we
want to
get to,
and we
achieve that
by minimizing
it.
And so,
Beth free
energy is
distinct from
variational free
energy by
factorizing the
calculation of
free energy.
So,
instead of
computing it all
by once,
out once,
you compute it
per node
and edge,
and then
aggregate the
results,
which you can
see on the
height.
Each
local free
energy will
include entropy
terms from all
connected edges.
And since edges
can be connected
to two nodes,
the entropy of
these variables
would be counted
twice.
So,
one edge is
a variable,
and if you're
connected to two
nodes,
you would be
counting the
same variable
twice.
And so,
to cancel
that out,
they add the
one minus
degree of
the edge.
And at the
bottom,
I've added
that normally
an edge has
always degree
of two,
which might
sound weird
because how
can an edge
have a degree?
Because normally
nodes have
degrees.
But in chapter
five,
we will show
that it's
possible to
have dangling
edges that
are not
connected,
that are not
factorized on
one end.
So,
it is
possible to
have edges
with degree
one.
And last,
three constraints
ensure that the
sum of probabilities
for each node
and edge
equals one,
and it's
normalization.
And also,
that it is
possible to
retrieve edge
and node
probabilities
from the
joint distribution
so that the
edge says
something about
the nodes
and the nodes
say something
about the
edges.
Yes,
next one.
Yeah,
just that
we have the
variables on
the edges
of this
graph,
and the
f's are
like functions
or operations
or little
factories
where variables
can come in,
potentially multiple
variables can
come in,
and some
activity happens,
but we're
putting the
variable that
would be in
the node
of the
base graph,
and we're
having it on
an edge
connecting
functions.
So again,
the information
is identical
or congruent,
but everything
that we're
going to see
now is
flipped into
this space
where the
edges are
the variables,
and that's
what is going
to enable
the node
local
computations.
in chapter
three,
defining
epistemic
objectives.
The
author
writes that
ages interact
with the
world they
inhabit and
entail a
generative
model of
the
environment.
Achieving
future goals
can be
cast as
free energy
minimization.
And then
they ask
the question,
what should
this free
energy
functional look
like and
why?
And that
sets up
the rest
of the
paper
basically.
Only
optimizing
bad free
energy or
variational
free
energy
does not
lead to
exploration
but
clear
control,
which means
that only
prior values
are satisfied.
A hallmark
of active
inference is
alternative
functionals
specifically
made for
inferring
policies
like expected
free
energy,
which
includes
information
collection.
And so
epistemics
arise
from
optimization
of
approximate
mutual
information.
Mutual
information
on the
bottom
height
is a
metric
like
the
r-square
if you
make
a linear
equation
and that
it tells
you
how much
one variable
relates
to another
one.
And to
go back,
mutual
information
between
x and
z
in
equation
10
on the
left
to work
on it,
the
uncertainty
entropy
of
x
as
z
yeah,
that's
in the
height
equation.
So it's
how much
you know
about the
one given
that you
know the
other.
And so
say x
is an
observation
and z
is an
internal
state.
Then an
agent
can choose
x
and
to
see
and
gain
information
about
that.
And then
how to
define a
functional
that
combines
battery
energy
and
dynamics.
So to
have
energy
and add
negative
mutual
information.
And
minimizing
the free
energy
functional
elbow
with a
negative
mutual
information
means
maximizing
the mutual
information.
So you're
trying to
get as
much
information
about
internal
and
observation
states.
Yeah,
just one
comment there,
Bert,
and then
Jakob,
feel free
to add
anything.
That's a
great
comparison
you made
with the
r-squared
for a
linear
regression.
So in
a linear
regression,
r-squared
summarizes
how much
the two
axes,
the x
and the
y-axis,
resemble
each other.
r-square
of one
means
they're
exactly
co-linear.
They're
on a
manifold.
r-squared
of zero
is there's
no linear
relationship,
and r-squared
of negative
one would
be a
negative
association.
Mutual
information
is kind
of like
that,
but two
characteristics
are
importantly
different.
First off,
you can't
have
the worst
thing that
two things
could be,
or the
least that
they could
be,
is just
noise to
each other.
So you
can take
the negative
of the
mutual
information,
but you
can't have
negative
information
on something.
And then
secondly,
it's not
a linear
relationship.
relationship.
You could
have
something
that is
an
inverted
u,
and the
linear
regression
might
find
that
that
had
a
low
r-squared
because
the best
regression line
might go
through the
middle of
the u.
But then
if you
just think
about that
a little
bit more
generally,
of course
one of
those
variables
has
information
on the
other
variable.
And so
it's
kind of
like moving
a lot
of our
intuition
and also
some of
the epistemic
status of
linear
regressions
into
more of
a pure
information
geometric
space.
And it's
a really
important
point,
too,
that the
VFE
doesn't
endogenously
have an
epistemic
drive.
It's just
about the
real-time
surprise
level of
beliefs
and incoming
data.
And so
a hallmark
of active
inference is
the construction
of these
functionals
such as
expected
free energy
or free
energy of
the expected
future or
generalized
free energy.
Okay.
And so
expected free
energy only
works for
future time
steps,
whereas
variational
and bad
free energy
work for
past and
the current
time step.
And instead
the authors
posted
generalized
free energy
works for
both at the
same time,
and it
includes a
part that
tracks
in equation
14.
But that's
on the
end.
You have
P with a
curvy
stripe
XK,
and it
basically
keeps
count of
which time
step
at this
moment.
And also
note that
the policy
control is
fixed, so
that's
you with
a roof
on it.
And so
past time
steps have
observed data
and are
locked
using the
direct
delta
function,
which was
the function
with a
probability
of one
at a
specific
value and
zero at
the rest,
whereas future
time steps are
still open to
optimized using
generalized
free energy.
And so
below that
you can see
this
free energy,
how you
lock some
values and
keep them
open at
other moments.
And so for a
sneak peek on
the right,
on the figure
in the
right,
from paper
two, you can
see that as
time goes on
and time
steps are
observed,
data constraints
are added.
And that's
the little
black circle
with a delta
in it.
Committing to
a full modal
specification
Rporee limits
what a generalized
free energy
function can
do.
Instead,
making it
fully node
local is
synthetic active
inference,
as the
autoside.
Okay.
And then in
chapter four,
they discuss
the Lagrangian
active inference,
which is the
key of the
paper.
And so with
node local
generalized free
energy, we can
construct the
Lagrangian for
active inference.
And the goal
is to have a
distributed
inference
procedure,
solving for each
node individually
and constraining
the solution
as shown in
equation 13.
So on the
height.
And we need
to assume that
actual and
approximate
probabilities
are about
equal to
each other.
We had to
make that
assumption.
So I guess
we can ask
that next
week.
And now
with this,
messages can
be derived
as done in
part two,
which is the
next paper.
However, in
this paper,
they attempt
another way to
arrive at the
node local
generalized free
energy.
And this is
done in two
steps.
So first,
they apply a
mean field
factorization.
That ensures
edges are
independent
for each
node,
which you
can see
on the
height.
We have
a defractor
of the
node as
a product
for all
edges.
So they
are independent.
And then the
second move
they make is
that you can
partition the
connecting
variables,
edges,
into two
sets.
One that is
adjusted and
the other that
is left
alone.
And to the
adjusted set,
they apply
P substitution,
which is very
important.
And this
basically replaces
a local
free energy
with a local
generalized
free energy.
And on the
bottom is the
formula for
applying P
substitution,
which I also
don't fully
understand.
So maybe you
guys know a
little more
about that.
definitely will
ask.
I'll just
note here
that the
slash is
used to
mean except
for.
I hope this
is correct.
So here we're
able to take
something that
contains all
and we're
able to
kind of pull
out one
with this
more intractable
integral.
and then
still do
the simpler
log.
But we'll
ask.
The second
paper will
show how
P substituted
nodes are
gradually
removed from
the
funny
factor
graph over
time.
As these
nodes are
now in
the past
and do
not need
to consider
the future
anymore.
Again,
for a sneak
peek,
see on
the height,
everywhere
you add
the delta
in the black
circle,
you remove
the square.
And the
square is
the notation
for P
substitution.
And then to
construct the
active inference
Lagrangian,
it is important
that P
substituted nodes
work with
different messages,
generalized free
energy instead
of path free
energy.
And in this
way,
add epistemics.
lagrangian,
the optimal
points of
Lagrangian,
where the
first derivative
is zero,
are the
stationary
points of
the message
passing process,
which means
that nodes
do not change
anymore if
you keep
updating.
And so
there's a very
long formula
for Lagrangian.
and I
said you
split the
nodes into
two,
one set
that you
P
substitute
and the
order that
you don't.
And on top
of that,
you add
three constraints
which have
a lambda
in front of
them,
and that is
the marginalization,
the normalization
of both nodes
and edges.
That's very
important about
the stationary
point of
message passing
being kind
of like
settled,
where everybody
can pass all
the messages
they want
and nothing
is changing.
And that's
going to be
probably leveraged
in the
reactive message
passing
programming
environment,
where rather
than needing
to send
all messages
once to
the calculate
and send
all messages
again,
it opens
up the
ability for
different regions
of the graph
to be sending
and receiving
messages at
different frequencies.
So if one
sensor was
sampling a
thousand times
a second,
one was
sampling one
time per
second,
no longer
do you have
to decide
should we
coarse-grained
to one
second,
or should
we waste
999 cycles
on the
slower cycle
sensor.
Now,
with reactive
message passing,
because there's
no local
descriptions,
it's possible
to open up
that
implementational
space.
And now
we'll get
into
defining the
notation for
the constrained
for any
factor graphs.
And so
for any
factor graphs
are useful
for describing
generative models,
but it is
important to
know the
exact
functional
to be
minimized.
and the
authors develop
a new
notation for
writing
constraints
directly as
part of
the
for any
factor
graph.
Because
normal
for any
factor graphs
do not
show that.
It's just
no.
The figure
4 on the
right builds
upon representing
vectors with
squares nodes
and edges
as variables
that can be
factorized.
And they
add circular
beads which
indicate
constraints
that define
our family
cube.
And that
has to do
with the
variational
distribution.
a bead
on an
edge
denotes
the edge
QSI
while a bead
in the
center of
a node
is
QSA.
And then
they build
they introduce
four constraints
that are
needed
as notation
for the
for any
factor graph.
So the
first one
is a
factorization
constraint
and it
can either
be a
naive mean
field
or a
structured
mean
field.
When
naive
mean
field
is a
stronger
constraint
which
means
that
every
factor
is
independent
which
is
figure
five
it's
in the
middle
on the
right
and
structures
is
less
strong
because
you can
factorize
multiple
variables
together
and I
added
some
example
for
mass
many
edges
like
needed
for
if
you
want
to
have
many
edges
many
variables
into
a
factor
they
introduce
the
notation
with
dots
in
between
and
this
is
useful
when
you
have
for
example
a
Gaussian
mixture
model
which
is a
bunch
of
components
we'll
we'll
see if
this
is
accurate
but
let's
imagine
these
four
variables
are
coming
in
and
meeting
in
the
factory
for
prerequisite
components
of the
car
assembly
process
the
fully
factorized
way to
represent
that
is shown
here
that's
the
mean
field
assumption
that we
can just
treat
those
components
separately
like if
what we
were doing
was just
multiplying
or I
mean adding
the numbers
together
maybe we
could treat
them
separately
but then
also
there
are these
intermediate
structural
factorizations
where you
can take
four
joint
coming in
and then
you could
separate it
into
these two
are separate
and these
two are
connected
or two
pairs
so it
gives you
the expressivity
to do
the continuum
from fully
joint
to fully
factorized
mean field
and everything
between
all the
combinations
in between
in a
per node
fashion
rather than
at the
whole graph
level
whereas
that is
often how
it's discussed
elsewhere
somebody
constructs a
big generative
model and
says and
then we
took a
mean field
approach
to the
graph
so here
we have
that kind
of expressivity
in a
given node
on

mute
then
continue
Bert
good call
so the
second is a
form constraint
which enforces
a particular
function
or distribution
really
on a local
marginal
of an edge
or a node
figure 8
shows
what enforcing
a Gaussian
constraint
on an edge
looks like
and figure 9
shows
two different
constraints
on the
nodes
and the
authors
explicitly
note that
a constraint
on an edge
is independent
of the node
and that it
factorizes
into
and vice
versa
so
the messages
pass
and then
after
everything is
done
it's like
squeezing
clay into
a box
it just
has to
fit
but it's
only
after
the
fact
and then
they note
dangling
edges
which do not
terminate
on a node
on one
side
so
they wouldn't
require a
bead
but you
need it
to be able
to do
a form
constraint
so they
still hide
them in
and
you
have
that's
why they
add a
sort of
dummy
factor
node
on one
end
and
then the
third
constraint
is a
delta
constraint
delta
constraints
and data
points
allow us
to incorporate
measurements
into a
model
equation
30
and figure
10
show this
for data
constraints
these are
special
since they
denote
observations
and block
the flow
of messages
so these
points are
now fixed
nothing
goes through
it
because it
is already
set
and then
another
option
is that
when you
don't know
which value
to fix
it to
so the
s i
hat
then you
can optimize
the value
and then it
is called
a delta
constraint
and the
optimization
of this
is
using
expectation
maximization
what i
saw in
this
section
was
let's
just say
that we
were
drawing
height
observations
from
a
forest
so
one way
to think
about that
is
the
gaussian
distribution
that we're
drawing
from
okay but
now you
get the
data
point
and
you
can
think
about
that
data
point
as
just
an
entry
and
a
value
you
could
also
think
of
it
as
a
dirac
delta
distribution
parameterized
exactly
by the
value
of
the
data
point
and
so
thinking
about
data
as
being
a
dirac
constraint
variable
where
here
the
variables
are
on
edges
brings
unification
between
empirical
data
coming in
from the
outside
or passed
around
internally
and
broader
distributional
perspectives
and
then
the
fourth
constraint
is
moment
matching
which
replates
the
hard
marginalization
constraint
used to
include
the
entropy
of
edges
and
so
this
loosens
the
marginalization
as
now
only
the
moments
need
to
align
and
equation
eight
contains
both
node
and
edge
terms
since
the
moment
matching
constraint
applies
to
both
at
the
same
time
and
they
apply
to
both
at
the
same
time
because
of
the
top
formula
and
the
middle
one
the
middle
formula
shows
the
sufficient
statistics
described
by T
capital
T
and
so
basically
what this
means
is that
you
pick a
distribution
and
you
only
pick
the
moments
so
the
first
would
be
the
mean
of
the
distribution
and
the
second
would
be
the
standard
deviation
and
so
only
those
need
to
fit
you
don't
care
about
the
rest
and
piece
substitution
is the
final piece
needed to
represent
the
active
inference
Lagrangian
on a
C
constraint
for
any
vector
graph
and
constructing
the
local
generalized
free
energy
using
mean
field
vectorization
and
piece
substitution
was
only
done
to
represent
the
Lagrangian
active
inference
on
a
constraint
for
any
vector
graph
and
he
called
the
p
substitution
involves
substituting
part
of
the
model
p
for
q
in
expectation
only
and
that
is
the
formula
on
the
bottom
and
it's
represented
with
a
square
in
the
four
in
the
vector
graph
and
it
shows
the
substitution
on
figure
13
replacing
the
local
variational
free
energy
with
a
local
generalized
free
energy
pool
replacing
q
on
the
data
or on
y
with
p
that
conditions
on
x
and
z
this
red
piece
is
being
called
attention
to
and
we'll
unpack
that
more
with
the
authors
and
on

top
of
that
lastly
the
authors
compress
the
constraint
for
an
effect
to
make
it
easier
to
read
and
only
deviations
relative
to the
default
battery
energy
are
shown
and
the
B
chain
is
introduced
as a
series
of
beads
connected
by
edges
and
is
summarized
if
it
contains
no
extra
information
and
the
authors
go
into
depth
but
I
will
just
keep
it
to
this
where
they
go
from
the
left
image
to
the
height
so
the
height
is
the
cleaned
up
for
an
effect
graph
and
then
you
can
more
easily
compress
it
and
make
it
smaller
for
very
large
diagrams
allow
us
to
kind
of
compress
or
skip
through
the
uninformative
parts
and
just
call
attention
to
the
new
information
that
is
being
intersected
and
then
chapter
six
they
highlight
how
classical
active
inference
and
original
generalized
free
energy
algorithm
are
special
cases
of
the
developed
Lagrangian
active
inference
so
an
integral
part
of
message
passing
algorithms
is
the
choice
of
a
schedule
which
Daniel
already
explained
which
is
the
order
of
messages
in
which
they
are
passed
iterative
methods
are
sensitive
to
the
order
and
Lagrangian
active
inference
is
an
iterative
method
and
might
be
sensitive
to
the
choice
of
schedule
so
choosing
the
schedule
carefully
allows
us
to
recover
classical
active
inference
planning
algorithms
as a
special
case
and
figure
20
shows
the
constraint
for
an
factor
graph
as a
composite
node
of a
composite
node
for
the
Lagrangian
active
inference
on
discrete
state
spaces
equation
on the
height
show
the
corresponding
factors
where
h
a
is
defined
as a
function
of
the
transition
matrix
required
for
the
order
equations
and
figure
21
shows
the
message
updates
some
cannot be
solved
in closed
form
and
instead
require
multicolor
estimates
u of
x is
the
average
free
energy
of
the
composite
node
and
corresponds
exactly
to
expected
free
energy
issues
and
standard
active
inference
where
the
composite
nodes
the
block
with
a
striped
block
around
it
and
M of
Z
and
M of
A
are
solved
differently
than
the
rest
they
require
Z-bar
is
solved
using
Newton's
method
as it
tends
to
fluctuate
between
multiple
extremes
and
M
A
is
estimated
using
a
sampling
procedure
and
so
below
shows
the
generative
model
of
a
discrete
prompt
and
the
equations
below
that
show
the
factors
and
note
again
the
head
on
u
so
the
edges
are
fixed
and
calculating
the
generalized
free
energy
is
done
using
a
forward
sweep
which
you can
see
with
the
arrows
on the
bottom
right
going
from
left
to
right
and
summing
the
free
energy
terms
over
all
the
substituted
composite
nodes
and
these
should
then be
equal
to the
result
from
the
shown
equation
cool
these
images
are just
so
interesting
even
without
knowing
what
they
are
reconstructing
original
generalized
free
energy
method
is
then a
matter
of
including
past
observations
for past
!
time
steps
adding
data
constraints
while
for future
type
steps
adding
piece
substitution
and
the
name
field
is
applied
to
all
the
nodes
the
schedule
the
order
of
messages
is
shown
below
the
update
equations
of the
generalized
free
energy
using
this
model
are
the
same
as
of
the
expected
free
energy
and
then
the
authors
work
on
an
example
which
is
the
classic
teammates
task
so
the
tools
in
this
paper
are
not
limited
to
restating
prior
work
it
offers
more
advantages
one
of
which
is
the
ability
to
directly
infer
a
policy
instead
of
post
hoc
selection
choosing
actions
which
have
the
best
energy
terms
instead
you
can
do
it
immediately
so
the
optimal
action
to
take
is
therefore
to
visit

but
the
optimal
action
in the
teammates
is
to
first
visit
four
because
you
can
get
information
about
two
and
three
rather than
immediately
try to
go to
two
and
three
and
that
is
the
hallmark
of an
active
inference
agent
yeah

lot
to
explore
here
but
instead
of
relying
on
the
post
hoc
comparison
of
energy
terms
this
is
in
reference
to
the
way
that
usually
expected
free
energy
is
used
by
taking
in
habit
the
policy
prior
and
then
iterating
over
every
element
in
pi
the
policy
prior
and
sharpening
or updating
them
according to
the
expected
free
energy
with a
pragmatic
value
and the
epistemic
value
component
so you
get some
policy
posterior
and then
you might
select
simply the
best one
or you
might take
some
temperature
guided
sampling
across
the
policy
posterior
so that's
a
post hoc
comparison
of
expected
free
energy
terms
and
with
the
!
the
models
now have
the ability
to directly
infer
policy
potentially
without
explicit
consideration
of
counterfactuals
or at the
very least
without this
kind of a
post hoc
comparison
and so
they build
on that
and create
another
model
and note
that
in equation
47 they
use a
mixture
model of
candidate
transition
matrices
indexed by
UK
so each
action
has a
different
transition
matrix
and
yeah
a pinch
of
illustrations
and figure
28 shows
an agent
that initially
prefers the
epistemic
action
and so
moves
down
to state
4
and
subsequently
exhibits a
preference
for either
of the
potentially
rewarding
arms
so of course
left or
right
and this
shows that
the Lagrangian
active
inference
is able
to infer
the optimal
policy
and that
approach
can reproduce
prior results
of the
teammates
and then
the authors
do it
again
but now
by adding
a data
constraint
and this
is similar
to using
a maximum
posteriori
estimate
which basically
means that
the action
is yes
or no
so it's
100%
or not
yeah
by pushing
through the
point mass
constraint
kind of like
that
Dirac delta
constraint
all that can
be shared
is the
first moment
which is
just the
data points
value
so here
it's like
you might
have a
70% chance
of doing
thing
one
20%
2%
1%
but then
the action
selected
is decisive
and so you
have this
decisive
passing
of action
and the
decisive
realization
of location
even if
also
there's like
a location
distribution
that includes
support over
the entire
maze
or a
policy
distribution
that includes
support
overall
policies
and then
to conclude
in this
paper
we have
proposed
a novel
approach
to active
inference
based on
Lagrangian
optimization
which we
have named
Lagrangian
active
inference
we
demonstrated
Lagrangian
active
inference
on a
classic
benchmark
problem
for the
literature
and found
that it
enhanced
epistemic
drive
that is
a hallmark
feature
it presents
three main
advantages
over previous
algorithms
first
an advantage
is the
computational
efficiency
afforded
by being
able to
pass
backwards
messages
instead
of needing
to perform
forward
haulouts
for every
policy
like a
tree
search
so
it
scales
linearly
over
time
a second
advantage
is that
it allows
for directly
inferring
posteriors
over control
signals
instead of
relying on
model
comparison
like
Daniel
just
explained
and
thirdly
it is
inherently
modular
and
consequently
works
for
freely
definable
constraint
for any
factor
graphs
while
prior
workers
focused
mostly
on
specific
generative
models
and they
have also
introduced
a notation
for writing
down
constraints
and piece
substitutions
on a
four-day
graph
and the
constraint
factor
four-day
graphs
are useful
not only
for active
inference
but for
specifying
free energy
functionals
in general
and the
authors hope
that this
can become
a standard
tool
similar
to
four-day
factor
graphs
when it
is
desirable
not
to just
write
the
model
but
also
a
family
of
distributions
in the
future
work
to
expand
to
extend
the
work
to
more
node
constructions
to further
open the
scope
that can be
attacked
with active
inference
awesome
work
great
job
preparing
it
yakub
anything
you want
to add
on part
one
no
at the
moment
okay
scaling
linearly
in time
is really
fascinating
like
if you
planned
10 time
steps
should
the
11th
step
be
a
10%
bump
in
difficulty
or
should
it
be
another
combinatoric
explosion
every
little
kilometer
deeper
into
the
future
so
second
paper
okay
first
just
going
in
deeply
to
the
first
sentences
before
accelerating
across
so
they
begin
the
paper
saying
free
energy
principle
postulates
that the
behavior
of
biological
agents
can be
modeled
as
minimizing
a
variational
free
energy
and
this
is
commonly
brought
up
that
we
can
model
biological
agents
as
or
through
or
with
minimizing
variational
free
energy
just like
saying
we can
model
this
regression
by
fitting
an
L2
norm
we can
model
this
biological
agent
by
fitting
the
elbow
or
the
VFE
active
inference
which is
AIF
in this
paper
is a
corollary
of the
FEP
that describes
how agents
propose
effective
agents
by
minimizing
an
expected
free
energy
objective
that
internalizes
a generative
model
GM
of the
agent's
environment
and prior
beliefs
about
desired
outcomes
so
VFE
is the
real-time
behavior
minimization
EFE
EFE
brings it
into the
prospective
setting
by
introducing
epistemic
imperative
and also
talking about
observations
that haven't
happened
yet
Variational
objectives
for active
inference
can be
minimized
by message
passing
on a
Forney
style
factor
graph
representation
so
everything
we know
about
Bayesian
graphical
models
transposes
into
the
FFG
space
the
FFG
is not
a kind
of
Bayes
graph
it is
a dual
a different
kind
of
graph
conveying
the same
information
in a
restructured
format
that we
can then
optimize
or implement
differently
several
authors
have
attempted
to
scale
active
inference
under
message
passing
framework
however
agents
based
on
these
approaches
lack
crucial
epistemic
characteristics
so
one
question
why
was
that
was
it
that
previous
authors
only
modeled
VFE
but not
EFE
or
was there
some
failure
of the
EFE
loading
on
epistemic
value
I think
the answer
is the
first
one
in
part
one
they
identified
this
hiatus
in the
specification
space
and
they
introduced
the
CFFG
and
then
in
part
two
which
is
the
current
paper
we
use
the
CFFG
notation
as
introduced
in
part
one
to
define
locally
constrained
variational
objectives
and
derive
variational
message
updates
for
GFE
based
control
using
variational
calculus
the
resulting
control
algorithms
introduce
epistemic
behavior
in
synthetic
active
inference
agents
we
reason
purely
from
an
engineering
point
of
view
and
do
not
concern
ourselves
with
biological
plausibility
what a
sentence
in
this
paper
our
contributions
are
threefold
they
use
variational
calculus
to
derive
message
update
expressions
for
GFE
control
they
derive
specialized
messages
for
discrete
variable
model
and
they
implement
the
results
in
a
reactive
programming
framework
simulating
a
perception
action
cycle
on
the
teammates
with
a
full
message
passing
account
and
reactive
implementation
of
GFE
optimization
it
becomes
possible
to
derive
and
reuse
custom
message
updates
across
models
and
get a
step
closer
to
realizing
scalable
!
Synthetic
active
inference
agents
for
industrial
applications
so
what
is it
about
their
contributions
that
makes
the
industrial
and
engineering
work
more
transferable
or
scalable
then
they
summarize
the
coming
sections
section
2
reviews
variational
base
section
3
reviews
active
inference
perception
learning
and
control
in
terms
of
message
passing
on
the
CFFG
section
4
focuses
on
the
constraint
definitions
around
a
sub
model
of
two
facing
nodes
!
and
derives
stationary
solutions
and
messages
for
GFE
based
control
section
5
applies
the
results
to
a
specific
discrete
variable
goal
observation
sub
model
that
is
often
used
in
AIF
practice
they
then
work
towards
implementation
in a
simulated
setting
and
describe
a
perception
action
cycle
in
terms
of
time
dependent
constraints
section
6
the
teammate's
task
is
described
in
section
7
and
simulated
in
a
reactive
programming
framework
in
section
8
section
9
has
a
summary
of
related
work
and
the
conclusions
are
in
section
10
it's
also
useful
to
put
table
1
and
table
2
up
here
table
1
is
an
overview
of
notational
conventions
1
nice




list
of
letters
would
be
awesome
to
connect
to
the
active
inference
ontology
and
then
table
2
has
a
bunch
of
acronyms

okay
section

2
review
of
variational
message
passing
so
this
section
briefly
reviews
variational
message
passing
as a
distributed
approach
to
minimizing

variational
free
energy
so
first
they
review
variational
base
2.1
then
2.2
they
review
forney
style
factor
graphs
2.3
they
move
to
the
Beth
Lagrangian
optimization
using
Lagrange
multipliers
we can
convert
the
optimization
on
q
to
a
freeform
optimization
problem
of
Lagrangian
where
Lagrangian
multipliers
enforce
local
constraints
the
fully
local
optimization
then
becomes
this
expression
again
more
to say
they're
using
Lagrangian
constraint
framework
and
the
Beth
flavor
of
free
energy
which
is
already
node
local
to
provide
a
very
constrained
which
is to
say
possibly
more
solvable
and
tractable
node
local
computation
and
now
they
get
to
the
constrained
Forney
style
factor
graphs
as we
heard
in
part
one
an
FFG
alone
does
not
unambiguously
define
a
constrained
VFE
objective
interesting
question
what is
needed
for that
unambiguous
identification
of the
VFE
CFF
and
CFF
and
so
here
they
review
their
CFFG
notation
here's
figure
one
and
we can
again
see
that
they
go from
the
initial
factor
graph
on the
top
left
with
an
explicit
CFFG
on the
top
right
then
they
compress
it
down
to
the
bottom
left
and
then
that
uniquely
identifies
a
logistical
or an
operational
schedule
section
three
review
of
active
inference
by
variational
message
passing
in
this
section
we
work
towards
a
message
passing
formulation
of
synthetic
active
inference
we
start
by
reviewing
active
inference
and
the
CFFG
representation
for a
GFE
objective
for
control
so
3.1
they
define
active
inference
3.2
they
define
generative
model
now
they
go to
message
passing
in
this
section
we
formulate
a
synthetic
active
inference
as a
message
passing
procedure
on a
model
of
past
and
future
states
inference
on
a
model
of
past
states
relates
to
perception
and
learning
while
inference
on
a
model
of
future
states
relates
to
control
what
is
control
if
not
just
perception
and
learning
we
haven't
had
yet
figure
three
constraint
40
style
factor
graph
representations
for
variational
objectives
on
models
for
past
left
and
future
states
right
!
I
don't
know
if
one
has
to
cross
their
eyes
or
do
some
other
magic
visual
experience
here
there
are
some
small
differences
like
here
there's
a
dashed
box
that's
not
here
there's
a
data
constraint
clamp
dangling
edge
here
whereas
that
constraint
is
open
here
however
the
rest
of
the
figure
looks
pretty
similar
and
that
tantalizingly
points
to
some
similarities
between
learning
and
memory
in the
past
where
we can
clamp
down
part of
the
model
to be
data
and
consideration
of the
future
which is
to say
action
and
control
where
the
observations
are
distributional
beyond
the
DRock
and
they
haven't
happened
yet
and
we
have
agency
over
them
happening
any
thoughts
on that
either
of you
it's
kind of
cool
and it's
kind of
foresaged
in
some of
the other
graphical
models
but we'll
ask the
authors
331
talks about
past
states
and then
332
goes into
the model
of future
states
so
a lot
to read
in the
paper
but that
key idea
because
future
outcomes
are by
definition
unobserved
we include
goal priors
on the
future
observation
variables
those are
preferences
we expect
there to
be
observations
and we
know that
they will
become
constraints
to
DRock
like
form
but
in
anticipation
we take
a
distributional
approach
to
observations
that
haven't
happened
now what
if we
had
uncertainties
about
the past
and we
were doing
kind of
a
policy
like
search
in our
fuzzy
memory
then where
would
time
be
section
four
they get
to
general
GFE
based
message
updates
in the
model
for
future
states
the
goal
prior
and
observation
model
impose
simultaneous
constraints
on the
observation
variable
in the
corresponding
CFFG
this
configuration
is
modeled
by
two
facing
nodes
so
I
I
believe
those
nodes
might be
the
two
in the
dash
box
here
in this
section
we derive
the
general
GFE
based
message
updates
for
pair
facing
nodes
we
express
the
local
optimization
problem
as
Lagrangian
using
variational
calculus
we then
derive
local
stationary
solutions
from which
we obtain
general
update
expressions
for
GFE
based
messages
so
they
describe
the
goal
and
the
observation
model
4.2
local
Lagrangian
after
the
substitution
of
the
factorization
and
applying
P
substitution
to
the
local
variational
free
energy
objective
they
get
the
local
GFE
the
GFE
is all
set up
to
construct
this
Lagrangian
and
to do
a
variational
optimization
on that
Lagrangian
to get
Q
star
4.3
local
stationary
solutions
Lagrangian
We are
now
prepared
to
derive
the
stationary
points
of
the
node
local
Lagrangian
We start
by considering
the
node
local
Lagrangian
as a
functional
of the
variational
factor
Q
sub
X
Lemma
1
stationary
points
of
L
as a
functional
of
Q
What does
lemma
1
do or
show?
Lemma
2
We derive
stationary
points
of
equation
4
as a
functional
of
Q
sub
Z
Note
that
by
symmetry
a
similar
result
applies
to
Q
sub
theta
What
does
lemma
2
do
or
show?
In
this section
we show
that the
stationary
solutions
of
section
4.3
correspond
to the
fixed
points
of a
fixed
point
iteration
scheme
Theorem
1
Theorem
2
What do
these
theorems
do
and
show?
4.5
Convergence
Considerations
Some
further
considerations
and
a
corollary
1
What does
it
do
or
show?
Now
we get
to
5
Application
to a
discrete
variable
model
In
this
section
we
apply
the
general
message
update
rules
of
section
4.4
to a
specific
discrete
variable
model
that
is
often
used
in
AIF
practice
using
the
general
results
we
derive
messages
on
this
specific
model
And
so
here
we
see
figure
5
with
all
it's
been
taken
all
the
way
to
the
point
of
the
logistics
of
the
messages
for
those
two
facing
nodes
5.3
Data
Constrained
Message
Updates
This
message
updates
for
data
constrained
VFE
objective
figure
6
on
the
left
reduced
to
standard
variational
message
passing
updates
as
derived
by
citation
28
and
appendix
A
So
here
we have
those
two
nodes
with
a
Dirac
intervening
Here
we had
x
intervening
in
figure
5
so
we had
a
distributional
bandwidth
now
we're
dealing
with
a
Dirac
distributional
bandwidth
or
channel
which
is to
say
a
data
point
being
passed
Now
we get
to
section
6
perception
action
cycle
In
this
section
we
formulate
a
perception
action
cycle
that
extends
upon
the
GFE
formulation
Specifically
we
illustrate
how
CFFG
notation
allows
us
to
be
explicit
about
local
constraints
As
a
result
the
perception
action
cycle
can
be
visualized
as
a
process
that
modifies
constraints
over
time
Pretty
cool
At
the
initial
time
t
equals
1
no
observations
are
available
and
we
initialize
the
perception
action
cycle
with
the
CFFG
of
figure
7
on
the
top
We
got
a
sneak
peek
earlier
Now
it's
real
figure
7
As
actions
are
executed
and
observations
become
available
data
constraints
replace
the
p
substitution
on
the
observation
variables
So
it's
almost
like
the
p
prepared
us
to
flip
it
out
with
data
in
some
way
Like
data
constraints
are
a
secondary
or
a
further
constraint
that
is
enabled
through
the
p
substitution
When
the
time
horizon
is
reached
and
all
observations
are
available
on
the
bottom
data
constraints
replace
the
p
substitution
on
the
observation
variables
So
it's
kind
of
like
we'll
know
when
we'll
know
and
then
it'll
all
be
inferenced
like
memory
but
before
we
know
what
we
later
found
out
it's
more
like
control
So
whether
we're
in a
retrospective
memory
setting
a
real-time
sense
making
setting
or
a
prospective
control
theoretic
setting
it would
be pretty
cool
to have
like
a
mega
unified
imperative
and
attract
local
procedure
to do
it
which
in a
sense
is
what
they
do
So
the
perception
action
cycle
with
time
dependent
constraints
thus
unifies
the
tasks
of
perception
control
and
learning
under
a
single
generative
model
and
schedule
this
is
the
huge
piece
is
only
through
the
FFG
and
the
constrained
FFG
can
we
get
to
not
just
making
a
base
graph
of
perception
cognition
and
action
cool
enough
but
bringing
in
an
explicit
node
local
scheduling
and
logistics
approach
Wow
The
experimental
protocol
is
summarized
in
algorithm
one
All it
requires
is a
generative
model
and a
variational
distribution
with
associated
constraints
And then
it's
kind of
like a
dance
do
infer
act
execute
observe
slide
We
then get
to
section
7
with
the
experimental
setting
In
this
section
we
describe
a
team
A
task
that
serves
as
a
classical
setting
for
investigating
epistemic
behavior
citation
10
The
setup
closely
follows
the
definition
in
30
citation
10
is
Friston
et
all
2015
active
inference
and
epistemic
value
and
citation
30
is
from
this
Vandelaar
et
all
same
authors
in
2022
active
inference
and
epistemic
value
and
graphical
models
here
here
we
have
the
team
A's
that
was
shown
earlier
with
a
smiley
face
no
smiley
face
here
and
it's
laid
out
and
labeled
starting
position
O
Q
C
that's
where
the
epistemic
value
is
and
then
L
and
R
the
two
reward
arms
and
just
for
those
seeking
continuity
here's
figure
7.4
from
the
2022
textbook
here
we
have
the
2022
active
inference
mouse
in
a
team
A's
and
from
2021
here's
our
active
inference
simulation
where
it's
actually
appropriate
the
nestmate
is like
much
smaller
so
for
the
nestmate
they
can
wander
around
a lot
inside
the
team
A's
that
for
the
mouse
it only
has one
location
it can
be
in
so
it's
not
as
closely
allied
as
7.4
is
with
figure
8
here
but
it's
like
the
same
you
could
do
it
in
the
same
lap
they
further
specify
the
teammates
and
the
probabilities
of
different
things
happening
they
further
specify
the
teammates
and
the
probabilities
of
things
happening
and
then
in
figure
9
they
get
to
a
CFFG
describing
the
teammates
let's
go
through
it
with
the
authors
and
annotate
what
it
means
we
execute
the
same
experimental
protocol
as
before
and
plot
the
minimal
free
energies
in
figure
10
top
right
the
BFE
based
reference
agent
fails
to
identify
epistemic
modes
of
behavior
the
specific
choice
of
prior
for
the
observation
matrix
prevents
any
extrinsic
information
at least
initially
from
influencing
policy
selection
by
the
lack
of
an
epistemic
drive
the
BFE
based
agent
sticks
to
policies
that
confirm
its
prior
belief
without
exploring
possibilities
to
exploit
available
information
in
the
team
a
histogram
of
the
number
of
wins
per
run
is
plotted
in
figure
11
on
left
the
histogram
suggests
a
bimodal
distribution
with a
large
mass
group
to
the
right
and a
smaller
mass
in
the
middle
for
reference
dashed
curves
indicate
ideal
performance
for
agents
that
already
know
a
from
the
start
for
agents
that
first
must
learn
a
deviations
from
ideal
performance
are
expected
the
smaller
middle
mass
then
indicates
that
GFE
optimization
offers
no
silver
bullet
for
simulating
fully
successful
epistemic
agents
namely
for
some
choices
of
initialization
the
GFE
agent
may
still
become
stuck
in
local
optima
section
9
I
won't
read it
they
describe
a wide
swath
of
related
work
ranging
from
early
work
on the
introduction
of
40
graphs
on
through
expected
free
energy
and
active
inference
and in
section
10
they conclude
they took
a constraint
centric
approach
to
synthetic
active
inference
they
simulated
a
perception
action
cycle
through
message
passing
derived
from
a
single
generalized
free
energy
objective
and
dot
dot
dot
in this
paper we
have adopted
a purely
engineering
point of
view
and we
have not
concerned
ourselves
with
biological
plausibility
specifically
the derived
message
updates
come with
considerations
about
stability
and
non-standard
expressions
although
we have
engineered
solutions
to overcome
these
complications
it seems
unlikely
to us
that the
brain
resorts
to such
strategies
interesting
mic drop
but very
humble
and so
now
as we
give our
last
thoughts
we've
always held
up the
side-by-side
at the
institute
with a
minimum
of two
and we've
talked about
that before
in the
textbook
figure
4.3
setting
with
continuous
and
discrete
time
but there
have been
many other
min-2
experiences
that we've
all shared
together
and not
just with
this diad
of papers
but with
this new
intelligibility
of the
relationship
between
base graphs
and different
styles and
constrained
forms of
forny graphs
we're in
yet another
min-2
setting
so
what I
would like to
say in
closing as we
include the
dot zero
yeah I
look forward
to the
point one
and point
two
I have a
bunch of
questions about
for example
what piece
substitution
really means
and for
example the
time window
how many
time steps
you need to
give your
model already
or whether
it can
unfold
automatically
and just in
general to
hear what
they have to
say because
it is a
very
interesting
topic
yeah
same here
also
interested
to
hear what
the
authors
have
to
say
and
I
think
yeah
whenever
there's
a
generalization
that
at least
in the
semantic
space
affords
a
wider
connection
to
different
methods
and especially
in the
context
of
models
represented
on the
graph
I'd
be
interested
to
learn more
about how
we can
represent
agents
in
different
kinds
of graphs
or how
these
constrained
for any
cell
factor
graphs
afford
different
types
of
optimization
methods
to be
performed
on them
and how
this work
can help
active
inference
to
interface
with
other
domains
which
try to
solve
similar
problems
or perhaps
different
problems
from a
different
angle
awesome
my last
thought
is like
we
planned
to
learn
at least
to try
here
so I
commend
you both
for that
policy
selection
and now
looking back
it's like
data or a
memory
and then
in science
it's like
oh it's
1994
this new
genome is
available
or like
this new
thing is
exciting
and here's
the next
step
and it's
like
one
must be
as excited
as can
be
in making
the right
measured
decision
then
which later
becomes an
observation
at a
different
time point
and a
different
perspective
so
there are
probably
many
exciting
and important
syntheses
that this
work
is gonna
build
our
skills
and our
expressivity
around
and the
computational
element
is just
excellent
so
thank you
again
Bert and
Jakob
see you
fellows
in the
dot one
bye
bye
to

























Thank you.
