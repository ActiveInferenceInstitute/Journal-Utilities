---
title: "ActInf ModelStream #001.3: "A Step-by-Step Tutorial on Active Inference""
category: "ModelStream"
series: "ModelStream_001"
episode: "3"
duration: "2:40:56"
url: "https://www.youtube.com/watch?v=vacR2gYgOxk"
views: 932
exported_at: "2026-02-18T22:37:37.949028+00:00"
format: markdown
---

# ActInf ModelStream #001.3: "A Step-by-Step Tutorial on Active Inference"

and we are live
hello everyone and welcome to active
inference lab
this is the third part in a four part
series
it is model stream 3.0 and today we are
here with ryan smith
and christopher white and max murphy and
we're going to be having a really
interesting discussion so thanks
everyone for joining just to quickly
introduce ourselves
before we go to points of process and
then into the material
i'm daniel friedman i'm a postdoc in
california
i'm ryan smith um i'm an investigator at
the laureate institute for brain
research in
tulsa oklahoma hi i'm christopher white
i'm a phd student at the mrc cognition
brain sciences unit in cambridge england
hi i'm max murphy i'm a postdoctoral
fellow at carnegie mellon
awesome thanks everyone for joining for
our panelists and the authors for max
for contributing your
experience and also for everybody who's
going to be live and in replay
asking us questions this is the third in
a four-part series that is going to be
highlighting different perspectives and
addressing questions related to
the active inference tutorial paper of
smith
at all from uh i guess you could say
2020 but it's been versioned several
times
and that tutorial is called a
step-by-step tutorial on
active inference and its applications to
empirical data
so if you have any questions during the
live stream you're more than welcome to
type it in the live chat and we'll try
to get to it
if you have questions after this live
stream just leave a comment and we're
gonna try to address it as well
to learn more and to find out about
participating
check out activeinference.org that's all
so for today in our third session we're
going to be picking up with just a brief
overview even shorter than the second
parts overview and then we're going to
be diving into two main sections today
ryan is going to be leading a section on
the neural process theory
and then christopher is going to be
leading a section on hierarchical models
so two very interesting topics let's
just start with
one warm-up introductory question before
we go to the neural process theory
and my question would be let's say
somebody were sent
just this third part of this four part
series
what would you say is the summary of the
first two parts that we can catch them
up with right now before we jump into
these next two parts so what happened in
the first two parts
that led us to want to talk about the
neural process theory and the
hierarchical modeling today
um okay well i can try to start to take
a stab chris feel free to add anything
but it's obviously a lot to summarize in
uh just a couple
uh seconds here but in session
one primarily we went over the kind of
like
broad um broad stroke sort of
description of active inference
um the ideas of how you can do
approximate bayesian inference to solve
problems with perception and learning
and decision making
using uh free energy minimization and
expected free energy
energy minimization um where exact
bayesian inference just becomes
intractable
for most kind of real world problems
when you're trying to
do something cognitive or perceptual
and then we went over how to build
specific
task models um and specifically
we used an explore exploit a simple sort
of explore exploit model
um similar to any you know a kind of
behavioral task that you might use
in an empirical study and we just showed
how
at the level of matrices and vectors and
things like that how you specify a
generative model
in order to simulate behavior on that
kind of task
and that's more or less what we've
covered so far so
the kind of general mathematics and
motivation of active inference
and how to apply it to um to
model tasks but that was all
like i said at the kind of computational
and algorithmic level of description
um whereas one of the really nice things
about active inference is that
you have not only the computational
algorithmic level but you
also have an attached what's called a
neural process theory
which more or less corresponds to a
specific hypothesis
about ways that neurons and neural
populations can be connected up
in plausible ways to implement the
active inference algorithms
and specifically the variational
updating algorithms that are used
to solve the sorts of tasks
that you use to model with active
inference so that's kind of where we're
picking up is
now that we've got the now that we can
build models and understand their
background
and motivation you know how can we
actually move this into neuroscience and
make
um make uh trial by trial predictions
about what neural responses you ought to
see
which you could for example feed in um
to like an fmri experiment
to see if you can actually find
correlates of those uh predicted trial
by trial responses
and just kind of add to that i think the
general way that you would
feed it into an fmri experiment would
just be the standard way that people
usually do this stuff so you just put it
in and add it as a regressor
in um into a glam yeah
and as you'll as you'll see we can also
do it's not just fmri you can also do it
i mean we
the the most direct predictions it makes
are about earpiece
and eeg so and we're going to talk about
what the erp is and the biology of it a
little bit along the way
and other frameworks for how people have
interpreted it but yes
as we've kind of looked at a few
different times there's the observables
which are the behavior
or the neural imaging whether it's fmri
or eeg or some other type of measurement
technique and then there's the
measurement of behavior
and we're talking about models that
start from those observables
and then do some interesting generative
modeling under the hood
and that's where the power arises from
so any other comments on that max before
we jump
into part one with the neural process
theory
no i'm just uh like i said last time i'm
excited to hear about
um tying and relating specifically you
know gradients
on you know variational free energy to
you know dopamine expression and just
hearing about like the links between
those
and why that might be an elegant way um
to um kind of express things in terms of
the neural process theory
and what we know about the connectivity
of these regions and things like that
sounds good then ryan take it away
okay so let me just
share my screen here
um okay so just um
as a kind of very brief um you know sort
of just
catch people up a bit um
um so we we started out
you know like describing active
inference um like i said at the level of
generative models
um and those uh sorry i'm trying to find
the right
figure here yeah
um and those have
this particular sort of graphical
structure
and just focusing on the one on the
bottom right here which is the full
generative model
you have a particular set of
observations over time this 010203 thing
and then you have particular hidden
states so beliefs about what's going on
out in the world
outside of the brain and so you have
your beliefs about what happened at time
one
and then time two and then time three
and this a matrix thing
um is what encodes the likelihood
mapping or the belief about what
outcomes
will be present if particular states out
in the world
are the case um and then you have
beliefs about how
in this b matrix thing here about how if
you're in particular states at time one
how that's going to transition into
different states at time two
um and so forth and uh this d
thing is just an initial prior um about
what states are going to be at time one
um and then you have policies pi up here
which control which allow the agent to
control some of the
transitions between states um so for
instance the transition of
moving my leg up versus down right would
be something that the agent could
control
and then policies are selected based on
this g thing which is the expected free
energy which is a function of
c which is your preferences so the
outcomes that you prefer over others
so policies are selected that are gonna
transition between states that generate
outcomes or observations that are as
close to preferences
as possible um and then policies
are also um in part controlled by e
which is a prior over policies that acts
as a kind of
influence of habits and this gamma thing
which will be important in the neural
process theory i'll talk about
which is um it's essentially it's like a
temperature parameter more or less
on like a dynamically updated
temperature parameter that
basically controls um how much
the expected free energy contributes to
policy selection so it's basically
saying if i don't trust my model very
much
then policy selection is going to be
influenced by expected free energy less
and by habits uh more um and the way the
gamma is updated is
through this hyperparameter beta
which again i'll uh i'll uh you know we
covered this a little more detail last
time but i'm just kind of reminding the
reader about
the elements that are going to
correspond
to different aspects of the of the
neural process theory
um so it just might only happen
my only comment on this is again think
about incremental
layers of complexity in the model on the
top left is static perception
hidden states observable states and
you're doing inference on the hidden
states s given your prior d so
instantaneous
hidden state inference given observables
bottom left you're talking about hidden
states
changing through time with the inference
of a b matrix
top right you introduce the idea that pi
policy
is going to intervene into how states
change through time
and that that policy is selected by a
preference c
that gets transmuted into a free energy
g and then the bottom right is the full
fleshed-out skeleton where we also see e
gamma and beta as described by right so
just start top left
bottom left top right bottom right and
that's adding up
one more thing for each layer of the
model and then now we're going to be
working with the bottom right model
yep and um and the the last sort of
important thing is is about the
the underlying way so each of these
equations
um on the at each of these boxes
um the the way that you infer beliefs
about
states based on observations is through
a set of equations that correspond to
approximate bayesian inference through
minimizing free energy and expected for
energy
so the idea is more or less how the
system how in the neural process theory
does the system settle on
a set of posterior beliefs over states
through free energy
free energy minimization and how in the
brain um that's going to correspond to
the neural process theory
to minimizing particular types of
prediction errors
um now but i want to be clear though the
these sorts of prediction errors are not
identical
right this is not the same process
theory as what's associated with
predictive coding and perception
where predictive coding is a continuous
state-space model as opposed to the
discrete state-space models we're
talking about that have categories
right you can only be in state one state
two state three as opposed to
these sorts of continuous state spaces
associated with things like
brightness for example um
so so this is this has a similar kind of
prediction or minimization flavor
to predictive coding models but it's not
the same thing um
so now um
to start with um kind of abstractly
the the way to see how prediction errors
come in really naturally
is just to remember that free energy
right one one decomposition that we've
talked about in previous sessions
is you can think of free energy as to be
being decomposed into a complexity term
minus an accuracy term um where accuracy
just
means basically how close your predicted
outcomes are
to um the observed outcomes
and complexity corresponds to basically
how much you have to move your beliefs
um from prior beliefs to posterior
beliefs so
minimizing free energy means coming to
the beliefs that
um change your beliefs as little as
possible while also maximizing accuracy
um so so that's the kind of idea and a
very kind of intuitive way to think
of free energy
and so given that definition
you can think of the gradients or the
way that free energy changes
with respect to these approximate
posterior beliefs that we're trying to
come to
right these can always be expressed as a
particular mixture of prediction errors
and you think about this is pretty
intuitive because complexity like i said
is
just the average difference between
posterior and prior beliefs
so minimizing that difference can be
seen as a type of prediction error
and minimizing and then accuracy is
similarly just the difference between
predicted and observed outcomes
so minimizing that difference can also
be seen as a
as a type of prediction error so
active inference can be implemented then
um
as this kind of prediction error
minimization that just corresponds to a
minimization of these two
differences at a computational level of
description as opposed to an algorithmic
or neural
level description so the
the kind of standard and fairly daunting
looking figures that you'll typically
see
in active inference papers associated
with the neural process theory
looks something like this so on the left
you have a bunch of initially pretty
scary um you know equations
that correspond to the the actual kind
of dynamics that a neural system is
going to have to implement
um and then on the right these kind of
little
fun kind of schematic ball neuron setups
where you have particular
layers that are supposed to kind of um
you know kind of heuristically perhaps
correspond to different
um different layers of neurons and
cortical columns
um and each of these layers of neurons
are sort of proposed again very just
kind of like schematically
to correspond to different variables in
the equations over here
and the synaptic connections correspond
to particular
mathematical operations so
um so here kind of the easy way to think
about it is that
these uh red connections here are
excitatory or excitatory just means
addition
in the equations whereas these
inhibitory
uh blueish purple connections with the
balls at the end instead of the arrows
are inhibitory which just means
subtraction in the equations
whereas the green modulatory connections
um that just corresponds to
multiplication um
in the update equations on the in the
other side of the panel so the idea is
that
you can use this kind of using this kind
of scheme you can just follow along
you know just follow the synapses and
the ball neurons that correspond to the
particular variables
um and you can kind of get a sense of
how
you can just connect up neurons like
this to
solve the equations that need to be
solved to implement active inference
just say one thing about this i think
makes it a little bit more intuitive
so because all of the updates are done
in log space
addition and um face click adding or
putting probability distributions
together is just addition and
subtraction
which is nice thinking about in terms of
this scheme and then generally speaking
the modulatory connections will
correspond to some precision parameter
which will modulate the precision of a
distribution if that makes sense
so that's kind of how you can think
about the rule or i find that helpful in
thinking about the relationship between
something like this
and the actual update equations
themselves
yeah no absolutely uh yeah thanks for
adding that it's almost like
the anatomy of the model we're doing a
schematic
neuroanatomy that's simplified or
abstracted based upon the actual
patterns of neural connections
and then we're looking at the anatomy of
this computational
model and thinking about how it could be
plausibly carried out on
neural uh systems neural processes but
also it stands alone and so this is just
another way that we can look at it
yeah so so another thing that i really
want to be
clear about is that active inference per
se
isn't committed to this particular
implementation
there's there's quite a few different
ways that you could come up with
to connect a bunch of neurons together
to solve these equations
so there's there's not kind of a
one-to-one mapping between
the way that the equations look and the
way that neurons could solve those
equations
so this is an example but ultimately
it's a separate empirical
question what way uh the brain is
actually set up
to solve these equations even if those
equations are what are being solved
um yeah exactly and even if so then we
can also
let's say it turns out variational
message passing or like marginal message
passing is just a really bad
metaphor well that's fine because we've
got all sorts of other things like
belief propagation blah blah blah
and they can all i think
the main thing is that you're minimizing
variational free energy
and expected free energy the rest is
part of
specific parts of a process theory that
we can
hopefully falsify or at least more
realistically
not find useful anymore yeah so let's
just sorry one more note on that you
brought up how there's the computational
and the algorithmic levels and we're in
the process theory realm so for those
who might not be familiar with process
theory or
mars levels of analysis the
computational level is like the function
like you have to sort a list from the
biggest to the smallest
you can't falsify that idea it's
computational it's functional
then you go one layer down into the
algorithm so you say i have a sorting
algorithm there's many
sorting algorithms but this is the
implementation as
it's actually going to be written in a
certain pseudo code
so that's one of many possible
algorithms that do a certain
computational task like sorting
and then the process theory is like the
specific program you can think of
it's the actual implementation now as to
whether it's actually being implemented
that way
you might be right or wrong so that's
what we're talking about with the false
falsification of the process theory but
at the computational level
it's what christopher just said it's the
imperatives that there's a free energy
minimization happening
and now we want to be building up
specific plausible examples to work
within that framework
for just to jump in real quick it sounds
like in the next stream we might be
discussing more of these empirical
examples and instantiations but just to
say
that from the bio biological standpoint
of what's going on for example when we
talk about a
modulatory layer or that that could
happen in a multitude of different ways
um in in terms of you know changing what
the membrane potential of the cell is
and making it more responsive or
receptive to being activated
or it could happen through you know
gradual um plastic processes that
recruit
more receptors to the um to the surface
and cause it to become more responsive
to any individual message so it's really
going to be context specific
and depend on the experiment and what um
circuit we are specifically studying
uh yeah absolutely and i mean the the
thing you mentioned about plasticity
uh makes an important point that i yeah
i should make sure that
i you know i might have forgot to
mention but but so
in the context of inference right over
the shortest time scales
we're just getting observations right
and based on the way that these
the current weights of all these
connections the system is just going to
settle
on a free energy minimum right like a
predictionary minimum
and then the the activation patterns in
these neurons
specifically these ones at the top here
the s pi t and
s or s pythau and s tau are gonna be the
posterior
beliefs about what states you're in um
and uh but that's again just given a
fixed set of synaptic connections that
corresponds to
your generative model now um
but with learning like we discussed last
time when we shift learning simulations
learning corresponds to slowly changing
the synaptic the strength of the uh each
of these synaptic connections
themselves um so you also over slower
time scales
minimize expected free energy and
variational free energy
um through um through changing these
connection strengths
um again over slower time scales via
kind of synaptic plasticity processes
um like long-term potentiation and
long-term depression for example
um as a way of improving the accuracy of
your generative model
um so so just to kind of reiterate
inference corresponds to changing
activity levels whereas learning
corresponds to changing synaptic
strengths
um so if that's if that's uh helpful
um so so again yeah i mean like like
they were saying you have
basically three different levels of
hypotheses to test one is
at the computational level does the
brain uh
minimize free energy and expected free
energy or at least
is it helpful to describe it as doing
that
um and then second question is given
that that first one is true
which of several different algorithms is
the brain using
and then question three is given that
it's using a given a specific algorithm
how are the how is the brain set up to
uh
implement that algorithm so there's kind
of a one-to-many mapping between each
level
um and a final point to make is actually
some people talk about these different
you know are called quote unquote marion
levels
of computational level algorithmic level
and implementation level
people talk about them as though they're
entirely independent um but they're
actually
not necessarily independent in all cases
because sometimes
the algorithm can depend a bit that can
be dependencies
between the algorithm and the
implementation because some of the
things that the
algorithm is going to have to compute
are things about for instance like
energy costs
which are going to depend on the
implementation um
so anyway just as kind of a side point
um
but um but in general um just to kind of
you know walk you through
you know a sense here so you might start
out with these observations at the
bottom
right and these are going to go up
through these excitatory connections
to this pink layer 3 here which is going
to correspond to the state prediction
error
we'll talk about so these excitatory
connections are going to drive increases
in activity in these pink guys
and those are going to be inhibited by
prior beliefs about states at this
higher level
which jointly right is going to lead
this uh
this level to decrease
while the system finds states up here at
the
level above that best account for
um or predict those observations um
so these red arrows going up here um
can correspond to interactions between a
and o in these equations um
and so you can kind of you can walk your
way through kind of step by step and we
do this kind of step by step in the
paper
where each of these interactions
corresponds to elements in the equations
so for instance like to get states
to get states up here right that
corresponds to this
fourth equation down and that's by
multiplying
policies um by states given policies
right so pi here
multiplying the
the s's and the t's here that are added
so
we'll lead to the posteriors over states
just as one example
um and then another thing that's
important to
um to stress is a lot of times you'll
you'll notice in these uh diagrams that
there are kind of
multiple uh rows kind of going back
right so there's like these three
pink ones and then these three other
pink ones behind them um
and that's because um each of these
uh posterior beliefs over states the
system is trying to come to
um are with respect to a particular
policy
so the thing is actually calculating
what its beliefs would be
under each of many policies where each
of these rows corresponds to
a policy and that's what allows it to
then infer a distribution over policies
based on the states
that are expected under each policy and
the outcomes that they would are
expected to generate
so so again i'm not going to kind of do
this for you
now just because it would take forever
but if you just kind of look at each of
these equations
you know where addition is where
multiplication is etcetera then you'll
find
um that these connections um
you know basically reiterate or or show
how
uh uh how this can implement
uh how the neural connections can
implement each of these equation
equations
um but um
to uh to kind of go into certain
aspects of how this would work and where
the neural processor really really comes
in in terms of making
um empirical predictions just
just just to jump in real quick um for
the sake of moving forward um just to
help me thinking about
what the biology is as we start to talk
about the neural process theory
here you have um pie and you have kind
of like
you know connections that are inhibitory
excitatory um
sometimes when i think about phenomena
in in the biology
you know you have an emergent concept
that that's the result
of kind of a population of cells in this
case would it be
um better to think of this uh like a
policy as the actual
like you know the activation i'm looking
at a single neuron or am i going to be
thinking about
that like at a you know a layer or a
population level
oh yeah yeah very very good point i mean
like i said these are very schematic and
in any active inference paper you'll see
that you know the statement as the
cheese balls is supposed to correspond
to a population of neurons
okay right so a population where i mean
just as one example
right like one subset of neurons in a
given population might encode the
expected free energy of
each policy right so activation across
the population of neurons would code
for instance a distribution over um all
the policies being considered
um or something something along those
lines so yeah no no no one's
no one's thinking about this as uh each
of these being you know single neurons
that are solving um all this i mean that
would be
um uh really it'd be a really vulnerable
system
very little damage that system would uh
would knock the whole thing out
um so um so so yes definitely they're
they're
supposed to correspond to populations
but a lot of the details of that is
really um kind of underspecified in the
in the theory as stated it's still
fairly abstract
um kind of at the level i'm showing here
um
so uh so is that is that
that helpful yeah yeah that does
okay um so okay
so the first ones here to focus on the
left are
so this epsilon pi tau thing
um and this is what's called state
prediction error
um and more or less what this does
is by minimizing this we end up with a
posterior over states
um and then the actual variational free
energy for each policy is just
calculated
based on beliefs about states and that
error signal
um so and this corresponds to
layer three um and layer two here
um in the um in the uh
schematic on the on the right um
so to um to give you a sense so in the
paper we show a specific example like a
worked example of calculating this kind
of prediction error
um and so what this says so this is the
prediction error for each
policy for each time point tau
and the the first part here this one
half ln
b pi tau s pi tau minus one et cetera
all the way over
the whole thing here with the b's that
are multiplied
by one half you can think of this whole
entire thing
as your prior expectation so
b from pi tau minus one um
this is saying what do i expect about my
current state
given the state that i was just in
before
um whereas this one is something a
little more interesting
it's saying um this is saying sort of
beliefs about
um expectations that come from the
future
so you know what are my beliefs about a
state at a given time
given my beliefs about the state after
that um
and um you know this this might seem a
little bit counterintuitive but um
it allows for uh retrospective inference
um which is something that humans
definitely do so think about think about
a case where you're sitting in a room
and it's dark and you don't know whether
the room is the green room or the red
room um
and but you sit there for like five
minutes and then all of a sudden you
turn on the light
and you see that the room is red you
don't just infer i'm in a red room now
you infer i've been in a red room the
whole time
so your beliefs about the past are
updated based on your
beliefs about the current time point so
what this this second be here so
expectations
propagating from the future to the past
allows you to come
to beliefs about the states you were in
at earlier times based on beliefs about
later times
um and um and so so it's important to
also reiterate here that
each of these s's um s for pi you know s
pi
tau minus one um these beliefs about
each s at each time point are updated
at every time point so at time three i
can observe something and update my
belief about
the state at time one um so this is kind
of being
recomputed at each time point with a new
observation but about each time point
um you know in both the past and the
future um
as well as the the present so
so broadly then this whole thing this
one half times
both of these b's and s's is your prior
expectation
and then that gets added to the
likelihood function here which is so a
um times o which is the actual
observation
um at a given time and so this is like
your
uh this thing together is like your
likelihood um
so this again is very similar um
to uh just kind of another form of
representing uh
bayes theorem where you have priors and
you have a likelihood and you're trying
to come to
something that will inform your
posterior beliefs over states
and then that whole thing is subtracted
from
beliefs about the current state at that
moment
and more or less if you just kind of run
this over and over again
you'll settle on a set of beliefs about
states that minimizes
um this thing um and just to show an
example of that
um we specify here um
you know what a could look like right so
in this case
um state one versus state two the two
columns state one would generate
say observation one um with point
eight um whereas state two here
right and the right column would
generate outcome one with point 0.4
and so forth so that would be your
likelihood
now b here like i said before this is
your prior from
based on the previous time point and
here we're just saying
column again here is state at time
tau and rho is at time tau minus one or
uh you know from tau minus one or
this is basically this is saying given
that i was in a given that i
was in a state at time tau what is my
belief about the state i'll transition
to
so this is saying i believe if i'm in
state one
i'm most likely staying at state one
but there's a point two probability that
i could move to state two um
whereas the um be pi tau
is point three point three and point
seven point seven which means no matter
what i expect it's more likely i'm gonna
move to state two
um and then what i actually observe is
outcome one um and my prior beliefs
are just 0.5.5 so i have no
i didn't have a strong prior either way
to start with
um and this v thing is um just a
depolarization
uh variable which doesn't come into this
uh predictionary equation
well so i'll just kind of leave that for
below
but so this is just an example of how if
you plug in
each of these things into this equation
then just kind of follow along with the
numbers eventually
you'll end up with this prediction error
this negative point two two three one
negative point nine nine
nine one six three um and uh
and you can think about so then if we
move
uh here
then we can take this v which is your
initial
kind of depolarization um uh
level in a given neuron then you add the
prediction error to that
um so the depolarization depolarization
level changes
so this would be a change in the
activity level of the neuron in terms of
depolarization
but then posteriors over states then
correspond to
normalizing putting a softmax over this
depolarization
which then turns it into your actual
posterior over states
so this is b so this ultimately says my
posterior belief is that
i'm more likely in state one you know
0.66767
then in being in state two point three
through three three
um and this then would correspond to the
firing rates
um in the process theory um associated
with
um uh each possible state
so v is to be your depolarization
um and s is going to be the resulting
firing rates
yeah just add something to this so
generally thinking
e here or sorry not e epsilon yeah
yeah a little epsilon is a free energy
gradient
um it is a variational free energy
gradient
and then this also what would what we
end up doing here when we're adding
essentially when we have v when we're
plussing our free
our negative friendship gradient we're
essentially just doing a gradient
descent
on variational free energy that's
exactly what this is actually
and that's how it's implemented in the
code the only difference between this
and what we're doing in the code is that
we have little steps
have a little step thing so we divide
our epsilon by like two or whatever our
time constant for gradient descent is so
when
you know tying it back to that previous
uh schematic that we had
where we had the arrows that were
excitatory and here we're adding this on
to the
putative you know membrane potential
that we have described here that might
reflect these kind of probabilities
then if we have this kind of perhaps
this if this were an excitatory
interaction that we were looking
at then maybe if that excitatory
interaction from
one particular layer to another was
representing that
uh variational free energy gradient we
might expect to see this kind of
response and we might measure that in
terms of some kind of related
you know uh bio like biomarker
um of interest is that more or less than
just
yeah i mean so well i mean just to go
back to the kind of schematic here
like where this is happening is like
right here right so you have b
from time one right which is this purple
guy
so s through b from the previous time
point
adds on to the prediction error at the
current time point
and s from the future
belief about the future also adds here
whereas
the likelihood a um
yeah is added from from oh uh
there's this inventory thing here um
anyway i mean so that's that's the uh
i have to walk through a little bit to
figure out where this uh
inhibitory what this inhibitory one is
coming from um
oh this is the minus ln yeah the current
state
yeah um yeah okay but anyway so that's
that's kind of as an example um but
uh but yeah so
so by doing that you get this posterior
over states that gives you
both uh predicted depolarization levels
in cells and predicted firing rates
um that being said um
those and of themselves are not that
easy to
to measure empirically unless you're
doing like single cell recording or
something like that
so the idea that gets taken sort of from
here
is how you can get from these predicted
firing rates to something that you can
measure
um like event related potentials in um
doing eeg or electroencephalography
where you have a bunch of electrodes
basically attached to somebody's scalp
and you're measuring
changes in neural activity changes in
potentials
through the scalp from the brain when a
person is exposed to a particular
stimulus
and the uh the neural process theory
uh the kind of prediction is that um the
erps are gonna correspond to the rate of
change um
um in beliefs uh which is gonna be the
rate of change in um
where's this slide
the rate of change in um in v very i've
changed this
depolarization thing which is going to
be the prediction error
so so just to show an example of this
um that me and chris uh published
recently
um in the uh literature on the um on
visual consciousness
um you know there's a big interest in in
what erp's
um are specific to having conscious
experience
um and an example of an erp that
in the past has been linked to conscious
experience but
more recently there's been some sort of
controversy because it looks like you
can get
these p3 potentials in a way that's
not specific to conscious experience um
and so we're interested in seeing
whether the neural process theory
would allow us to kind of show um where
this is coming from and could reconcile
these sorts of results and so it was
based on this really kind of simple
paradigm
where you start out the person starts
out looking at a stimulus like this
where there's just these red discs and
these um kind of slanty lines
um and then in some trials
what will happen is they'll kind of
transiently be a little square here
that comes up um in the midst of these
slanty lines
um then it'll go away um
and basically what what um what the
manipulation is
is in some cases you have the person you
know focus specifically on these red
discs on the outside to see if they
change color
and then you ask at the end you know did
you ever notice
these square things that pop up um
and there are cases when um
when they do see the square in cases
when they don't and you're looking for
differences in erps corresponding to
when they do versus they don't
under conditions of different sorts of
attention um
and so what so what we were trying to do
is to see whether um when you built
um a an active inference model
that um that corresponded to this
particular
um attention uh
task um that's called an intentional
blindness task
um you know could we reproduce the the
p3 pattern so this kind of in red here
this extra um
dip um in uh
neural activity as measured by eeg that
um looks like it typically only happens
when a person consciously experiences
something
but with these recent exceptions where
it looks like it depends just on whether
a stimulus is a
task relevant or not um and chris
actually i think you know this was
primarily your work so
so maybe you could describe this in a
little more detail yeah yeah so first of
all i think that just
give a shout out because we've got to
reference it on the slides is um this
paradigm was designed by michael pitts
um and he has done a lot of really
incredible empirical work on um visual
consciousness so
just kind of important to acknowledge
that anyway um
so generally they speak there's three
phases in this experiment so phase one
is they're not told there's going to be
a square kind of self-assemble
and they're asked just to monitor the
disks on the outside
and then there's a huge literature on
this but generally speaking in
intentional blindness when you have a
setup
that's kind of analogous to that about
50 percent of people
are intentionally blind to whatever your
manipulation is
so i think the really famous one is like
a group if you ask
people like monitor um how many times a
basketball is being passed back and
forth between a group of people a
gorilla can walk past and wave at people
and about 50 of them um don't report
seeing it
um so the idea here is just kind of
operationalize that a little bit more
carefully
um and then in phase two is after
everyone's kind of been because like
literally when you ask people after
phase one hey did you see a square
you're kind of alerting to them the fact
that there was a square present there
but it's still not top the square's
still not task relevant so in phase two
they just do exactly the same tasks
monitor the external disks
um and in phase three the manipulation
is they
then say okay well we now want you to
count how many times like hit a button
whenever the square appears
and so the idea was was that if you kind
of see here when we say percent scene we
basically said a hierarchical model
which we're going to look at in a minute
and we just had it kind of report what
type of trial
it thought it was in did it see a line
or not
where a line was like this categorical
variable
or did it see a square um
and essentially we just in the same way
that you might in psychophysics like
titrate
the stimulus or the contrast of a
stimulus or whatever
until people see it 50 of the time
basically what we did was we titrated it
until the model saw it 50 of the time or
titrated the precision of the a matrix
kind of corresponding to contrast or
whatever and then
we just manipulated attention where
attention corresponds to basically
how precise the model's a matrix was
um and what we showed was that when
attention which we operationalized was
basically like we had two steps of
attention we had focal attention
and um like
super precise task relevant attention
when there was just the focal attention
condition the model reported seeing the
thing
99 of the time so basically all the time
and
when there was precise like task
relevant detention the model reported
seeing 100 of the time again
but we see a dissociation between the
presence of the p3
in line with empirical results and so
the idea so i can actually just
highlight this since i'm the one with
the cursor
so so in this first condition so this is
when uh like chris said the
you know the thing had no expectation
right that it was gonna that there's
gonna be any square there
and um and the precision of the a matrix
was low because there was no attention
um so as a result the erp is totally the
simulated erp is flat
and similarly this uh the second
the second dip here which is what would
correspond to a dip here
is absent and here at the bottom
are the simulated firing rates so in the
first level basically when black at the
bottom changes to
black at the top that just means it
starts to believe the upper row is a
belief that the
square was present and the bottom is the
belief that the square was absent
so basically what this means is when it
goes from black at the bottom to black
at the top
that the belief changes so it's more
likely that the stimulus was
uh present um and then
but you can see because the a matrix is
uh imprecise
then um which corresponds to like a low
stimulus strength and this
um then this is not very uh
you know it's still pretty blurry and
then at the second level
these are beliefs about sequences that
are what's actually gonna in other words
did it go from no square to square and
back to no square
um and you can see that the beliefs
remain really imprecise
um because it's not uh it's not
attending to it it's not task relevant
um in this case though
like chris was talking about you can see
that even though it's not task
relevant the beliefs at the higher level
ultimately do converge onto this top row
which is the one where
the square was present but you can see
that the beliefs change pretty gradually
whereas when attention was precise
because it was task relevant
then you can see that the belief changes
from being kind of flat
over these two possible top states to
being
black fully confident that the square
uh turned on and off and that
really quick change in beliefs is what
corresponds to
the strong erp and in this case because
of the higher level it's a kind of late
erp
corresponding to the p3 so really what's
going on is the prediction of the neural
process theory
is that it's going to be the rate of
change in in beliefs
basically that is what's going to be
measured as as an erp
um you have anything further you want to
say about that chris
no no not at all i mean one thing i just
want to highlight is like the the only
difference between phase one and phase
two is a very slight difference in the
precision
of the a matrix that we um took to
basically be the addition of some uh
some slight focal attention
um and but you can see like just looking
at the figures like it really made very
a very minor difference but it still
bumped it up enough
above the threshold just enough for it
to basically go from 50
report to basically 100 report just
also one point on the erp or the event
related potential it's defined on the
bottom left of the slide
it's like a population level measure of
the electromagnetic activity
in populations of cells in the brain
and so it's kind of like on the left if
something's passing under the radar
the population is not changing in
broad strokes but then when there's this
event that's task relevant
it transiently synchronizes the
population to be doing certain things in
a certain timing
and then that's reflected by changes in
the population level
electromagnetism patterns reflected by
what are called erps but there's a whole
literature with fristen and many others
on this topic
yeah so basic erps are just
depolarization of
dendritic trees
yeah which corresponds to the prediction
error yeah which corresponds to
prediction
yeah cool so basically as prediction
error
initially goes up and then goes back
down then that would be
the uh the predicted erp
um so um
and this um is kind of related to
uh you know pretty standard neural mass
models um that are used
in the in the literature that make
pretty similar assumptions
right they assume that the average
firing rate of a population can be
treated as
a sigmoid function so a function that
looks like this
of the average membrane potential um
and you can do things like for instance
shift
this function to the left or the right
based on things that uh control the uh
the firing rate threshold um you know
which could relate to inhibitory
interneurons or you know there's a bunch
of
different neural mechanisms involved but
basically this
the point is just that um this idea
about where you get
um firing rates um from average membrane
potentials is is not kind of out of
nowhere it's
something that's kind of used as a
standard assumption
in um in uh these sorts of
models and one interesting note is the
soft max that sigma
that we use to kind of renormalize
probability
it's actually utilized in artificial
neurons in neural networks
as also a probability renormalizing
trick
so we're thinking about it in kind of
like the intersection of the physical
thing and the instrumentalist approach
realism and instrumentalism
and we're sailing our active inference
ship together through there
yeah so so that's and and you know later
chris will show
specific simulations based on an actual
task that will produce
predicted erps that are consistent with
existing literature
um when he goes through the code um in
the second part of this uh
this session um but so i'm gonna
sort of stop talking about the state
prediction errors at this point which
again
chris will pick up um in his part the
second thing
that's kind of commonly talked about as
part of the neural process theory
in inactive inference is this idea
of expected free energy precision um
being associated with dopamine so let's
say right from the start that
to be technically correct we call this
expected for energy precision
in the literature it's often just called
policy precision
but that can be slightly confusing
just because the precision
of the actual posterior distribution of
our policies right this bolded pi
here corresponds not just to
the precision of expected free energy g
here
but also to f and to e um
so there are ways in which the expected
free energy precision this gamma thing
that scales g
um you know could be precise or
imprecise while the actual posterior
distribution of her policies could still
be
precise or imprecise in a way that
differs from um
the precision of g yep so you can be not
sure what to do
but have very clear understanding of two
policies and their implications it's two
separate levels of uncertainty
no it's not quite that it's my life yeah
it's not yeah like like so so a good a
good example would be for instance so
um in the um you know in uh
you know the paper uh you know that i
wrote with casper um
and others on the on deeply felt alpha
so deeply felt affect so the idea about
um changes in emotional states or
affective states
um relates specifically to this uh beta
term here that controls the expected for
energy precision
um now when expected free energy
precision goes down
um then that will often correspond to
right a negative or when expected for
energy goes up sorry then that will
correspond to a decrease
and expected for energy precision um
but uh or a difference between f and g
um but uh but there will be cases where
gamma will go down meaning the the model
becomes less confident
in its beliefs about uh its ability to
minimize expected free energy
essentially it decreases its beliefs
its confidence in its action model but
there are cases when that can happen
despite the fact that the actual
posterior additional distribution over
policies becomes really precise
so so a kind of nice example of this
would be
you know say you're kind of walking
around in the woods and at the moment
you're really confident in the
walking around policy right so there's a
precise distribution
over you know i should be walking around
um
but now you unexpectedly see a bear um
now immediately you're going to switch
to having a very precise poster
posterior distribution over the runaway
policy so
you're going to have two policies two
distributions of our policies that are
both very precise
but they also but they change rapidly
so the the policy that the that the
model was confident in before is very
different than the policy
that the model was confident in after so
despite that the
posterior distribution is still over
policies is still precise
that things very confident what to do um
gamma will still go
down um so the thing will feel negative
like in motion despite being very
confident and running away
so the thing that the thing that's
driving that is f i think that's
important to put in
or to say
if you want to cash it out ryan oh well
i mean yes i mean just in the sense
so f is f is going to be so based on a
new observation
f is the um is the kind of evidence for
each policy
at the time of the new observation so if
f
strongly contradicts g then that means
that the distribution is going to change
in a way
that suggests that you ought to have
less confidence in g
and um and we can we can i'll show a
specific example of that below
um when we actually show simulations of
the um
you know postulated dopamine responses
but
so the idea here is is that dopamine
phasic dopamine responses correspond to
changes in this parameter beta which
controls
gamma which is the expected free energy
precision um
and the way that these updates in beta
so
this equation here just corresponds to
the initial beta
so the non-bolded one here plus
this thing so the posterior distribution
of our policies
minus the prior distribution of our
policies so basically how much did
beliefs about policies change
and then dotted with the negative
expected free energy
um that was that you know that
correspond to that trial
and then minus the previous uh beta
which allows this thing to just
continually iterate um
but because the change from posterior
release or policies
from prior beliefs or policies um
just adds f basically the prior over
policies we don't show it here is just
ln e minus gamma g
so the f only comes in to turn the prior
over policies into a posterior policies
um and so this change is driven by f
um and so the more that f
is consistent versus inconsistent with g
um is what uh is what controls
the the agent's sort of changes in
confidence about
about its g estimates um
and so changes in that are what are
expected or
proposed to correspond to phasic
dopamine responses
and then the kind of tonic level of beta
is also
proposed to be associated with tonic
dopamine
levels so if i can just very briefly say
something
um so essentially gamma is a
gamma is a a rate or bright beta sorry
is a rate parameter from a gamma
distribution
and essentially we get you get this
derivation so beta dot
that that technically that's a that's a
temporal derivative right
and so this isn't exact it's a little
misleading kind of because this
actually is a variational derivative
of gamma
with respect to variational free energy
if that makes sense so the idea is is
that updates or changes
in essentially this beta value will
minimize variational free energy
and if you want to see like the so the
actual um
the actual derivations of that get kind
of kind of gnarly
but if you're interested if anyone's
interested i would just say
um go and read and the appendix of
ann sales paper that's in plus
computational biology
on the locus cerealia cyrillus and
um learning rate and prediction error um
where they show motivations yeah ana's
yeah anna's
anna's the appendix and this paper is
like actually really great for this
because
plus cb uh basically like required
it looks like that she spell like every
little detail about
deriving everything um in active
inference so it
has a really great paper both in the
main text and in the appendix for
showing kind of exactly where you get
each of these things um
uh yeah like pretty much as clearly as
i've seen it
anything else to add on the neural
process front because there's some
questions and then we'll head into the
second section but this is awesome
uh there's a lot more actually let's
keep going then
then so yeah we'll do more neural
process theory however much
and then we'll be taking questions we'll
have a intermission with a few questions
that are really nice and then
christopher will
launch into the hierarchical modeling
so so to actually give examples here
because you know everything we've said
about the about dopamine and beta
updates is
um still pretty abstract um so
you know in the in the tutorial we give
specific numerical examples of this as
well
um um to show and give a kind of like
geometric actually um intuition
um about this um and um
so here you can see so so here we show
right that the prior over policies this
pi zero
like i said is just the soft max of ln e
minus gamma g
and then the posterior is the softmax of
lne
minus f minus gamma g which we showed
before
and so and these are the equations for
quote unquote dopamine phasic dopamine
responses
um and so if you just take a specific
really simple example
so let's say there's no hat so let's say
that beta 0
and therefore gamma 0 and the initial
beta posterior those are all just one so
we're just starting out
you know totally flat basically um
and and we'll say that the agent has no
habits
um so there are two possible policies
here i should say so the agent has no
habit so it's just one and one
for counts over uh policies
now let's say that g
is 10 and nine so in other words there's
slightly higher expected free energy for
the first policy then the second policy
so now let's say that f the agent gets a
new observation
and the free energy for each policy
corresponds to 20 and one
so as you can see this is still
consistent with
um the 10 and 9 right it's not like
contradicting the um
the you know policy one still has higher
uh free energy than policy two um
so when you calculate uh pi zero
using this equation and these numbers up
here you end up
initially having a probability over
policies of 0.218 and 0.728
so policy 2 is the one that
is has is uh more likely uh given the
expected free energy because it's lower
right expected for energy is nine
um now the posterior policies after
we put in f just ends up being zero one
um and so if you take the difference
here so we're just called pi diff so pi
minus pi 0
that ends up being negative 0.218.218
and then if you do this a dot pi diff
with negative g um and these two betas
just cancel out because it's just one
minus one
and so you end up with 0.22 and then
if you compute the update
then uh the yeah what the change will be
then gamma ends up equaling 1.28 which
went up from one um which means that
you'd have a
positive uh phasic dopamine predicted
positive physic dopamine response
um and a way to kind of think about it
geometrically is
um whether or not the vectors
corresponding to
uh pi diff so the difference between pi
and pi zero point in the same direction
as negative g
um because that implies that they're uh
consistent with one another that implies
that essentially the
g was on track um and that's worth a
a re-run so what is this geometric space
and then what would it mean if the
vectors were totally correlated and they
were like
pointing the same exact direction versus
here they're almost at 90 degrees or
what would it mean for different arrows
to be pointing in different directions
so these are the vectors corresponding
to
the vectors here in g and the vector
um that corresponds to pi minus pi zero
one so this is so this is and i should
say that these are scaled
um so that they're similar lengths
but the same directions because
otherwise one arrow would be way
way longer than the other and the kind
of point isn't clear
wouldn't be clear but so basically pi
diff right is negative 0.218.218 so it's
pointing left and up so negative x
positive y um whereas g is
um negative g would be negative 10
negative 9 so it will be
down and left um and so the
the general kind of um intuition that's
supposed to be given is that
um when these two vectors point in the
same direction where that just means
that the angle is less
than 90 degrees um then uh
the gamma update will be positive um
whereas
if for instance instead we do a
different example
now the only thing we're going to do
here is we're going to change f we're
going to change off from 20 and one
to or no sorry we're gonna change
g so g is going from 10 to nine
to only being one and nine so in other
words
while in this case the first policy at
higher expected free energy
now the first policy has lower expected
free energy
now if you run through the exact same
set of steps
to solve the equations you're going to
end up with a gamma of 0.14
which means there's going to be a
negative
there should be a drop in dopamine in
other words the agent should become less
confident
in its uh g estimates
and you can see that if you look at
where the vectors are pointing in this
case
um then they're then the angle
difference is 128.66 degrees so
more than 90 degrees so therefore they
point in different directions
therefore they provide evidence against
g um
if uh if that uh makes sense
yep let me try with the dopamine so
we're thinking of dopamine
as a tracker of confidence it has many
roles and colombo and others have
talked about pluralism in dopamine so
we're not this is not a lecture on
dopamine we're thinking about dopamine
as like confidence and
we're headed in a direction we're on our
road trip and the dope means coursing
through our brain
and we want to know how confident we are
that we're on the right path as new
observations are coming in
now as we've seen from the earlier
sections we're doing a lot of
matrix math and just like a vector
is a simpler version of a matrix and a
tensor is a more complicated version of
a matrix they're all kind of in the same
math space and a given vector
from computer science it's like two
numbers that are in a column
but also a vector has this arrow
interpretation
so if someone says the coordinate 3
comma 3 it's like a vector from 0 0
pointing to 3 3. so lists of numbers
like a computer science vector
is basically the same thing as a vector
with a
star and a head at the at the end so
it's physics and computer science
and we're thinking about vectors and
matrices and tensors
and then we're laying out after scaling
and renormalizing
which direction these different vectors
are pointing
and then it's kind of like it are we
headed on the basically the same path
is the the vector of the evidence sort
of pointing us in a similar direction
that we're already believing in
or is the new evidence coming in like a
tailwind or a headwind
that's kind of surprising us and it's
not in line it's not headed in the same
direction as what we're already
believing
and then this meta with a gamma the
hyper parameter
is about how much reliance we're putting
in to g
versus our observations yeah so i mean
another kind of
a nice a nice thing here is that so as
as gamma goes down right so if you look
if you look at this posterior
you know distribution of our policies
equation as this gamma value gets lower
right so as the agent becomes less
confident in its
in its action model more or less it's
less confident that its model
will be good at minimizing expected free
energy right as that goes down then g
contributes less
which means that f and e contribute more
so
if an agent has built up really strong
habits
um then its beliefs in its model will
control
action if gamma is high but if gamma's
really low
then the agent will just kind of choose
whatever it's
uh habitually chosen in the past so
habits will kind of take over
if it's not confident in its model um
which is kind of a nice way to think
about it has some kind of analogs to
like model based versus model free
um uh algorithms and reinforcement
learning
for example that um again we could think
about in terms of actually
making decisions based on you know
explicitly simulating what's going to
happen in the future
if i make one choice versus another
versus just doing what's typically
worked in the past
um is another kind of way to think about
what gamma is
arbitrating um did you uh do you want to
say anything else chris
no i was just going to say there's some
really nice numerical results um
so i think i've forgotten i'm sorry if
i've gotten the name um i think it's
thomas fitzgerald
is the lead author on this but um they
have some stuff
just showing that related schemes i
think that the equations have changed a
little bit since then but they're
pretty much the same um that this scheme
gives very very similar
answers as something like temporal
difference learning which is a very
simple model-free algorithm in
reinforcement learning
um and that's also i think the the gold
standard model of dope phasic dopamine
at the moment ryan correct me on that
but no i mean yeah i mean it's like
temporal the
temporal difference account of of uh
reward prediction error is definitely
yeah
treating phasic dopamine responses as
reward prediction errors in temporal
difference learning models is
definitely a very standard and kind of
like widely supported
view um and this i mean the idea is that
this
this can um this sort of um
this sort of active inference model of
dopamine um
is kind of saying something different
it's not saying it's a reward prediction
error
but it's something that will have the
same kind of dynamics as reward
prediction error
because if you think about it so say you
know i'm walking along and i'm not
expecting a reward
and then all of a sudden i get a cue
that
makes it so now that i expect now i
expect
um reward um so you know for instance
like
or say like in like a simple kind of
like experiment like a like
auburn condition experiment conditioning
experiment with like a rat or something
you know it learns
that every time it sees a light it's
going to get a reward in five seconds
um then the reward prediction area story
would say
oh you're going to get a real word
prediction error when the rat sees the
light because now
it's going to get it knows it's going to
get a reward that it wasn't expecting
um so in this case though you'll get
something kind of similar but for a
different reason
where you can think about the rat
initially just kind of wandering around
not being super confident
you know in in any particular policy
but then it gets that cue that it's
going to get rewarded
you know if it goes up and pushes the
the lever right as a standard way this
works
um so so instead of it being a reward
prediction error
what would be happening is the queue is
actually um
unexpectedly making the rat a lot more
confident in what to do
right a lot more confident in the policy
of going and pushing the lever
um so you're going to get something that
looks just like
a reward prediction error at least in
that sort of setup
um but actually has to do with an update
and confidence about what to do
so so that's kind of in part
that's one kind of intuitive way to
think about um you know where
similar looking dynamics come from but
but i should also kind of be be clear
that i mean this is
definitely not meant
necessarily to be kind of a universal uh
unifying account of dopamine you know at
least
at least as far as um you know i can
tell a present there's lots of
other things that dopamine does that you
know look like they couldn't be
explained by
just this sort of model but this sort of
model
um looks like it's decent as a contender
for
making sense of things like um why
dopamine doesn't just respond for
prediction errors but also responds for
events that are salient
um for example um this kind of saliency
versus word prediction or sort of thing
there's a couple others but
but um this is not necessarily meant to
be a
you know this is all dopamine does um
but anyway um so
uh so just making that clear um
so now the kind of last thing to show
and this is the actual figure in the
paper that just shows both of these
things
is that um if you do the actual
variational updating
where just beta continually changes then
the uh the actual kind of
gradient like that the changes look like
this where the thing would start out for
instance
at um around at a certain value
um and then for for this case right so
it starts at
um you know down coming from one and
then it will
gradually go up and converge um after
uh 16 iterations is the what's set in
the code um
to that posterior value over what gamma
ought to be
whereas in this case it will drop coming
up from one
down and then converge over those
iterations onto
um this value of 0.14 so it's not as
though in the neural model this is
kind of happening with one little step
it's it's kind of a
it's a you know it's a convergence um
that you can think of as related to a
kind of prediction error
um essentially kind of like an expected
free energy prediction error uh some
people have talked about it that way
um in previous papers and for those
following along in the code would this
be in the efe precisionupdating.com yeah
yeah yeah thanks so yeah there's a yeah
to play around with this exact
this this exact example um as well as
ones where you can specify
uh bigger policy spaces so like like
when the agent has like five policies to
choose from instead of one
um you know which is a little more
realistic it's just um
it's hard to show uh vectors um
sorry to illustrate those in like five
dimensions um so we went with two for
this simple examples
um but yes um in that efe precision
updating
you can reproduce these results and then
try changing like private beta values or
changing g and f um to see to get more
of an intuitive sense of the dynamics
um and so like in the um
in the eq in the the um what you might
call it
when we were showing in the explore
exploit test model last time
um these sorts of simulated simulated
behaviors
right where the agent either chooses to
take the hint and then go left or right
to get a reward oh it just makes
or it's just rick's risk seeking and
just goes left versus right
automatically instead of taking the hint
first
um in in the previous session we went
over this
and but we kind of ignored this bottom
right section on expected
uh free energy precision and these
dopamine plots
but now that we've kind of walked
through that a little bit
um you know we can kind of come back to
that and see that in this case
um the agent started out
in the beginning and it chose to take
the hint um and then it knew
um whether to choose left
uh choose the left machine or choose the
right machine so you can see what
happens here is
when it takes the hint then it becomes a
lot more confident about what to do
and so it's at that point that you
simulate a big jump in dopamine
right so in this case it's not because
it's got a reward immediately it's
because it got a
cue where it learned what to be able to
do to get a reward
um so then it chooses left and then it
observes a win here at the third
uh time point or this third column um
so so this is kind of an example um
and then in the learning simulations
that we showed last time as well
before we leave that slide could i just
jump in real quick and i had a quick
clarification about that
figure um so in that middle panel for
win lose and you look at that matrix
it actually looks like if that's the
expected probabilities for
win loss at any given uh time
epoch one two and three um he actually
it actually looks like in this
case the way that the simulation goes
it's more confident about winning
on this time step when it knows to take
the hint and then after it's taken a
hint
um it becomes less confident about
winning
is or is that it's actually to do with
the fact that those aren't so they're
probabilities but they're not
probabilities
in the way that the rest of the modulus
probabilities so these are
these are preferences where we model
preferences as a probability
distribution
i see i see so that has to do with more
of the
you know it's had more update it's had
more observations at time
three and so as you're going since
you're it's an accumulator
um in that optimization process is that
no
it's just it's just so when you're
trying to encode essentially what's
rewarding for the agent
right you're just setting you're just
saying that
it has a particular distribution over
each possible set of outcomes for each
outcome modality and that distribution
just encodes
which observations are more preferred
than
others and formally that's just a fixed
uh probability distribution over the
different observations you might get
where the higher the probability is
quote unquote the more the agent prefers
that observation
um so this is so this is just saying
like for the first output modality it's
just all
gray here because the agent doesn't
prefer a hint or
not a hint um and then the third one
here observed action it doesn't
prefer innately to observe itself do one
action or another
but in this middle one observing wins
versus losses versus null
just not observing an outcome yet um at
the first time point so the first column
it just does it doesn't have any
preferences at the second
time point so this middle column the
thing has a strong preference for
wind so this black one which corresponds
to high probability
it has a strong preference against
losing observing a loss which is a very
low probability
and then the null state is just this
kind of like intermediate thing it's not
like
it's not bad like a loss but it's not
good like a win and so the person that
shows the null
there or there is is because it shows a
hint because of the epistemic value of
the hint
i should say yeah so it so basically
what's
happening is if you remember that the uh
this distribution is a little
lighter at time two because the value of
winning is higher
at the second time step than the third
remember because it can win four dollars
if it tries to get us it just chooses
one right away
but at the third time point this is a
little less
precise it's a little flatter which is
like looks darker gray because the black
here
only corresponds to winning two dollars
instead of four um so the difference
between winning and losing isn't quite
as
stark i think okay yeah um
so but the point is it's not actually
getting a big bump in dopamine when it
wins
you know it's getting a big bump in
dopamine when it observes the hint
because that's
when it becomes confident in what to do
to get the win
um and that's to re-emphasize that we're
doing this trajectory of policy which is
what ties it to the path integral as
well
so at each time point that it's being
evaluated at it's in the past and in the
future and it's conditioned
on policy so it's almost like the reward
if you always expect the envelope has
the paycheck
if you get it and then you open it it's
like neutral with respect to what you
already believed about the way the world
worked
and you'd get a negative if it was less
than expected and a positive if more
than expected
and so in that way the reward of what is
initially just pure stimuli that could
be rewarding or thought of in that way
gets moved up that's kind of like re
reinforcement learning or reward
learning
and that's why we're in this area of
thinking about stimuli and policy and
rewards and risks
yeah i mean the idea is just that in in
that context
uh these dopamine responses the
simulated dopamine responses here
corresponding
to changes in confidence about what to
do or changes in confidence
that your model will give you the right
answer about what to do
and uh and that will look that will have
the same dynamics
as a reward prediction error
from a queue that predicts reward
so so the dynamics will look like a
reward prediction area even though
in these models it corresponds to
something different
um so it's kind of like in behaviorism
everybody can agree on the behavior we
agree that if we train up the animal it
learns to do this after
x um experimental paradigm is carried
out
and then now we're talking about
internal we're thinking either at a
neural process level like which regions
of the brain or
computationally like what is happening
and then
here there's a common trunk with the
predictive processing the reward
prediction error all of that
and the active inference models we're
talking about which is and reinforcement
learning which is that
over time the reward gets moved up to be
associated
apparently more with the queue than with
the actual stimulus delivery
but we're taking a point of divergence
in that we're adding in a few
different pieces that differentiate an
active inference free energy
gradient descent driven policy selection
from
just q association even though they do
have some similarities
this is like a generalization or a much
more nuanced way to approach similar
situations
yeah and you know ultimately right the
hope is to find situations
where active inference and reinforcement
learning models are going to be going to
make different predictions
right about what dopamine will do um
and uh because that's where you can
actually say you know which model has
more
you know empirical support um and um
yeah thomas fitzgerald i think it was
the paper that chris was talking about
before you know he did show
there are interesting findings where
when you
get rid of dopamine when there's
dopamine depletion there's some kind of
lack of dopamine in the system for one
reason or another
um that doesn't actually get rid of
uh reward learning like an agent can
still learn about rewards despite
um the dopaminergic function being
impaired um you know which makes it look
as though um
you know dopamine uh might not be
serving this reward prediction error
function at least if you think that
reward prediction
is necessary for reward learning um
and um and so there was he showed some
simulations again with a slightly
different formalism than the current one
showing how you can get the same
dopamine responses
um as you would expect in a
reinforcement learning model
but it explains why you don't need
dopamine to do the reward learning
um but uh but like i mentioned the
formalism isn't exactly the same as it
is
now because that was a slightly older
paper um so
you know i think there's just a lot more
kind of empirical work to do to try to
kind of
find uh you know differential support
for one model of dopamine or another
here
very uh any other any other uh comments
chris
um no i think just looking at the time
um do you want to kind of speed through
the slides and then you can get onto the
stuff yeah
okay so yeah i mean i can skip i can
skip or to skim over a lot of this i
mean the last thing i was going to talk
about is
that this isn't used as much um because
it's not actually implemented in this
way in the code
but carl has made this point that you
can also implement
minimizing expected free energy i'm
using a different kind of prediction
error called an outcome prediction error
and that just corresponds to the
different elements
in expected free energy so which is here
just
um here is just minimizing
the expected difference between the
preferred outcomes c
and the outcomes that you expect under a
policy
right so um under some policy uh
for under some policy the state for that
pi um
multiplied with a will give you the
expected outcomes of a policy
so you're just trying to um this
prediction error minimizing this
prediction or just corresponds to
finding the policy that
min or that minimizes the the difference
between basically what you want and what
you expect
given what you choose to do and the
second term
is the ambiguity or information seeking
term and it effectively you can think
about it as the expected difference
between
beliefs about states before and after a
new observation
so you're trying to find basically um
a difference that like uh the state that
maximizes how much information you gain
about what state you're in um but
formally it's the
it's the entropy of the likelihood
distribution for a state or how kind of
flat or uninformative the distribution
is
of expected outcomes given that you're
in one state versus another
um and in the paper we um we uh go
through
uh numeric numerical examples of um
computing these sorts of outcome
prediction errors as well
um but the the basic point again i won't
go through them in detail is just
if you have some policy that is going to
generate the state
uh state one with probability point nine
and state two probability point one
and your preference is perfectly precise
over observing outcome one um and that's
your likelihood mapping
then um policy whereas policy two
is gonna is expected to um just
uh generate 0.5.5 over states
um then um and the outcomes
that are associated with those states
look like this
then what you're going to get is
a policy one is going to end up if you
just
do the math um out policy one is going
to have a value of 2.4
for that for that term whereas policy 2
is going to have a value of 7.3 so this
difference is going to be a lot bigger
and therefore there's going to be more
outcome prediction error and so the the
policy that
the first policy that's going to
generate the outcomes that are closer to
what you want
is going to minimize that prediction
error more
and so again we just show examples we
also have some examples of
of this part but the basic idea here is
if this is your likelihood function
then state one here is kind of imprecise
in what it predicts right it predicts
one outcome with 0.4 and another outcome
with 0.6
whereas state 2 has a more precise
distribution
it generates outcome 1 with 0.2 and
outcome 2 with 0.8
so the agent would learn more if it
moves to state 2
because the outcomes are more
informative
and so basically these work examples
just show how
um the agent should to minimize outcome
prediction or the age shouldn't the
agent should be
driven to uh choose to move to state two
um and so um finally and i'm not going
to go into this
at all but we also show this um
panel here that corresponds to another
kind of element
um that's been proposed in the neural
process theory that has to do with
model reduction and sleep and the basic
idea is that sleep
allows you to search for other models
that you might you might entertain that
can produce the same experiences you've
had during the day but can do so in a
simpler way
so it's finding so sleep is basically
still trying to minimize free energy
but not with respect to new observations
but just with respect to
your model based on the experiences that
you already had earlier
and that corresponds to
internal dynamics that can essentially
prune away or reduce
the weights of synaptic connections that
are contributing less
to explaining um what you did so
essentially kind of noise
uh like like if there's a bunch of kind
of coincidental
um uh you know connections between
different things you observe then
there's some kind of noise in what
you've learned
and so you can during sleep you can
reduce that um
and here's just a few papers that have
talked about that and shown
simulations um in case people are
interested
um but so now
moving on to what chris is going to talk
about
are hierarchical models and the idea
here is you can just take
the same exact structure of the model
here
that we've shown before um but instead
of
um but put a layer kind of below it
that's the same kind of thing but
instead of the observations being
actual outcomes the observations are
just whatever
the states the beliefs over states are
at the lower level or the observations
the observations for the second level
are just the posteriors over states
at the first level and so that
just looks like this where you see here
that you still are selecting policies at
the higher level
although you can also select policies at
the lower level but
states at time two here just generate
states at time one and states at time
one or states of
sorry states at level one act does the
observations
for level two
as you can see necessarily these operate
over a slower time scale as well
so for instance at time one level two
the first state state of time one is
gonna generate
the uh first state
at time one at the lower level but then
the lower level is gonna move to its
beliefs at state two
over a faster time scale
and so this whole thing is going to
repeat at the lower level so the thing
is going to infer posteriors over states
based on two
observations at fast time scales
and then the posterior beliefs over
states at the lower level are then going
to propagate up and act as
the observations um for
state one at time one at the higher
level
and then that's going to transition
through a second level b matrix
to beliefs over states at time two
which then is just going to provide
priors
to a second trial to the start of a
second trial
at the lower level which again operates
over a faster time scale so essentially
this whole lower level model
completes its belief update um before
the higher level transitions to its next
state um
and in the neural process theory it
really just involves taking
the first level just kind of tacking on
another level of neurons on top
and making the observations of the
second level the things that drive the
prediction error
and the states as just the posteriors
over states at the first level so it's
just kind of repeating the same thing
but at a higher level in treating the uh
the interactions between the second and
the first level the same way that
observations feed into the first level
um and so if i raise a question on this
slide
from the chat someone asked can you
please explain the relationship or
difference between models based upon
deep active inference versus
sophisticated inference
and how is that related to the current
discussion around
dopamine signaling whether it's phasic
or non-basic so
two questions one is what is deep
active inference and how is that related
to sophisticated active inference and
how are those
related to what we're discussing now
about dopamine and i have i thought if
but you can go ahead i can answer all
these very quickly
this is perfect answer go for it so
deep active inference can kind of
correspond to two things uh you can talk
about it in terms of using deep neural
networks to
parameterize your your essentially your
a's and b's
a and b matrices or your policies uh
that would be kind of like a machine
learning application in when i
say deep active inference what i
generally and what other people have
talked about like the paper that first
came out called like deep whatever
the impact of inference it was just one
of these hierarchical models whereas
deep in the sense that there's this
uh temporally deep uh or temporally
thicker
one could say uh time time scale stacked
on top
and so then in terms of sophisticated
active inference that's just to do with
policy selection
um and where you're essentially doing
something that
looks more like a tree search
um so i would just say i don't know it's
equivalent to backward induction and
reinforcement learning
so you essentially instead of saying
kind of propagating forwards on a tree
you start at your terminal node and then
you propagate backwards
so you say given where i want to go how
do i best get there
and then propagate backwards uh and then
i don't really know what the
phasic non-phasic thing means uh
yeah yeah i'm not i'm not aware of
anybody
sort of saying anything about um if
there's any change in the dopamine story
in sophisticated active inference um in
that
sophisticated act of inference you're
still you're still obviously updating
beliefs about policies when you make a
new observation
um but uh but yeah i mean the main
difference like chris said is just it's
just
how you come to post your beliefs over
policies
by doing this sort of more thorough
research where you have this
additional element where you say you
know given that i observe a thing
at time two at a given branch and a tree
what will my beliefs be at time two
um and like like chris said it's
equivalent to backward induction
um and uh it's it's um
anyway yeah so i without without again i
don't think anyone's talked about this
much but
presumably you still make new
observations that update your beliefs
over policies as you move through time
um and so i don't necessarily see how
the dopamine story would need to change
um but uh but yeah um
and i will say in addition to what chris
said um
they're really um two kind of related
uh meeting meanings um independent of
the kind of machine learning deep neural
network thing that chris talked about
one is and like you said the standard
one is talking about deep temporal
models
yes and that's just exactly what i am
was showing here where the second level
necessarily operates at a slower time
scale than the first level
because the first level has to kind of
complete all of its time steps
um before it can provide an observation
to the higher level
and then the higher level so basically
each higher level state
corresponds to a whole lower level trial
um
you know so if you wanted to you could
make a lower level trial have ten time
steps
but the posterior beliefs at that lower
level at the end of this whole time step
all those time steps
would be you know what the observation
um
is that you know provides evidence for
the first state at the first
the state at the first time point at the
second level
so and then second level states
transition
and then the second level state so that
basically one trial
at the higher level with a two time
points
each of those time points corresponds to
providing priors for a whole
trial at the lower level so you're going
to have
as many trials at the lower level as you
have time steps in one trial at the
higher level
so so that's what deep temporal models
means
it's just that the second level operates
at a slower time scale than the first
and provides priors for
initial states at the first level um
another
another meaning that some people use
like in the deeply failed affect paper
is just d parametric models
which basically just means the first
level
out things that happen at the first
level can be used as evidence for
updating
hyper parameters for the higher level um
and like in the deeply filled effect
paper basically we had second level
states that corresponded to
valence um but those were updated not by
first level beliefs but by changes in
beta
at the lower level so when gamma updates
were positive
right when the confident and expected
free energy went up
there was a ascending signal that then
updated beliefs at the second level
that corresponded to feeling better
right so positive valence
um and those also that state could also
act as
a prior on um what the beta update
should be right how confident the agent
should be um
at the lower level as trials go forward
so it can also have to do with
with um with uh and it's quote unquote
deeper
parameters um as opposed to just deeper
uh
deeper uh levels that control priors
over states at the lower level
um but that's not as commonly
used um by far the most common is just
deep temporal models
do you have any more to add on the
neural process or can we do our switch
over
um no neural process is pretty done um
the only thing
is is that before chris starts
because what we're simulating when we're
doing this
example in the code of a hierarchical
model the example we're using
is an empirical task called a local
global
or oddball paradigm so chris is just
gonna i'm just putting up this slide so
that chris can
walk us through the um the uh
design of this task so just before we
cross over just while we take a breath i
want to make one
ultra rapid summary for um just contrast
and then ask one question from the chat
so the brief summary is
we're dealing with the active inference
framework we are within free energy
principle we're talking about active
inference that's why it's active
inference lab
now we've heard about a couple of
adjectives deep sophisticated
affective and even inactive inference
and those have been in the titles of
papers or they've been the titles and
models
we heard about just very um concisely
about what deep can mean
whether deep neural networks or deep
time and then there's a third definition
of deep meaning like
fully or radically parametric and that
is interpreted within within the affect
of valence framework
within the paper that ryan just
mentioned so that's deep and affective
which are related
then sophisticated is related to this
tree surge counterfactual
policy and state estimation we talked
about the
sophisticated inference in a previous
stream and an active
is highlighting more from an ecological
or even a philosophical perspective
about the embodied and enacted aspects
of cognition
so that's just a summary about a few of
the flavors
under the umbrella of active inference
and
they don't necessitate a renaming of the
lab because they're like variants or
paper titles
but this is the total umbrella that
we're working under
and then the general question from the
chat which i hope that set it up for
and then we'll address this question
each person give a very you know short
response that we launched into
chris's when preparing a model for
exploring
free energy principle active inference
in matlab do you often sketch out
equations
with sample bayesian calculations for
each term to help clarify your thinking
and track what will happen
or in other words how do you go from
thinking or specifying the generative
model of even
a experiment into what you do when
you're
talking like you go from this behavioral
example to the code
how do you do that um i mean
so for me honestly like when i'm
actually setting up
a model for a task um i don't really
think about the equations hardly at all
because you don't need to right i mean
what you need to what you need to focus
on
is just what the necessary elements are
in terms of states and observations
um and policies um
that are just in a task right so you
have to think okay
in a task what are the observations
that the participant has right is there
just
one possible observation modality they
either observe this or that
or are there multiple observation
modalities like maybe they observe a cue
and then they observe a reward right and
so then you need two observation
modalities
um right you think about how many in
each modality right is it just q
or no queue you know is it just reward
or no reward or is it
no reward reward or loss
you know so you just think okay what are
the different types of observations
and how many observations within each
type just you know what does the actual
participant observe
um and then you have to think about the
states right what are the what is the
participants beliefs what is the minimal
set of beliefs they need
to be able to make a decision right
about
how to get reward if it's a reward task
um
you know so that might be beliefs about
what uh trial type
it is right or might be beliefs about
what are the different
choices i might make um right like
moving into the state of choosing
say option one versus option two um
you know and then you have to think okay
what are the different action sequences
right like
does the agent just push a button and
get lucky you know
reward or no reward or you know does the
agent have to
you know make a couple choices in a row
you know just what are the actual
options
right and so i mean that's that's really
what it boils down to is just
figuring out what things do the
participant observe
you know what beliefs do they need to
make choices
what choices are available um you know
and
i mean it kind of it kind of builds
itself beyond that um i mean you have to
you have to realize that the the update
equations in active inference you know
we've actually been showing
are are very general right they don't
change at all
depending on what task you're
implementing so you're not changing the
equations all you're doing
is using the exact same update equations
on a generative model
that can successfully simulate behavior
on a task so i i mainly think you just
have to think about matrix and vector
structure
so i can actually answer this question
just by building or showing how you get
from this
task structure to the code in question
perfect
um and so just to basically build on
that um all that you think that's
is the structure of the generated model
because the update equations are totally
generic
and unless you're doing something like
fairly advanced
where you actually do need to specify
some type of
addition to the generative model use a
new type of distribution whatever
then you would need to rederive the
update equations and you're going to
have
some time on your hands using taking all
the functional derivatives and setting
setting it setting the result equal to
zero and figuring out what the answer is
but i have never had to do that
personally and i think very very few
people in the active infants literature
have had to do that
okay so in terms of
this task this is a local global or
basic like auditory modified auditory
oddball paradigm
um it was kind of i think this was the
first paper that used it although i'm
not completely sure about that
but basically they just have play you a
series of tones
and there are four possible conditions
and what they're trying to manipulate
is your level of or the the time scale
over which your expectations operate
because they're trying to get at
expectations at different levels of the
cortical hierarchy
and so the idea is is that you can have
regularities at two time scales
so the first time scale is the local
time scale and that is just
the series of five tones say so it might
be
and these tones can be two different
frequencies so it might be beep beep
beep
beep beep beep beep beep beep that type
of thing
um and the idea is is that
let's say you violate an expectation on
this local time scale this might be
something like the bottom row here
um this would be beep beep beep beep
beep beep
beep beep beep beep and if that happens
80 percent of the time or 80
of the trials you would have like a
global expectation or expectation over a
long time scale
that there would be a violation on the
four on the fifth
um beep if that makes sense but on a
local time scale for neuronal processes
say in primary auditory cortex or
wherever
that are operating over this very rapid
time scale they are blind
to this more global regularity and so
you will get
essentially what this will give you is
global
expectations and violations of global
expectations particularly
give you a p300 so essentially that is a
large
positive potential over kind of like
fronto-central electrode sites
and that corresponds to a violation of
global
regularities whereas a mismatch
negativity
correspond which is kind of a negative
uh
i think i actually haven't i'm not an
auditory neuroscientist so
i'm sorry about this if i get it wrong
but broadly speaking
it's kind of over association cortices
in like all the tree association
courtesies
not a hundred percent about that though
sorry i should look that up
um anyway and that will correspond
that's a negative going potential that's
corresponds to violations of local
expectations
and so kind of i just the reason we use
this is because it's kind of the
simplest possible model
that gives you some type of realistic
dynamics
and also kind of highlights the face
validity of
this computational framework if that
makes sense um so any any questions
would you like to add anything ryan
before i
pull out the code i mean i guess you
know just just because i'm the one in
control of the slide and the pointer
here i mean i just just want to make
sure that people understand exactly what
what's corresponding to what you say so
so basically the idea is just that
at each short time scale right you could
have each green one corresponds to a
beep and the red one corresponds to a
boop
right so at the fast time scale you
could be surprised that there's a boop
at the end of four beeps um for instance
if
if most of the time for example it was
just bpp beep
then whenever there's a bbb boop then
that's unexpected
right so that's an expectation violation
at a low fast time scale
um but um what chris is saying is
is that um you can also have a long time
scale thing which is like
how many times in a row is it bpb boop
versus bbb beep
right so one longer time skill pattern
would be
four bpp beeps in a row um
and so if you come to expect four bpp
beefs in a row
then if you hear a bbb boop then your
belief about the expected sequence
you know of these four trials um is what
would be violated
or or not so at the fast time scale you
can have
violations for each series of bpp beeps
at the higher time scale you can have i
expect expectation violation
about the sequence of bpp beeps
um so that's so that's the idea is you
can have long time skill violations and
short time scale violations
where the short test time scale ones
correspond to the low level and the
highest
high uh the high level
the second level of the model
corresponds to the beliefs about the
sequence
of ppp beeps um so anyway so that's
what's called global regularity versus
local regularity
yeah just for simplicity i just
simulated the local deviation global
standard condition
so that would be um if you kind of look
the third from the bottom
on the right hand side of the screen
imagine that um
and the local standard global deviation
um so that might be yeah exactly
which is the very top um on the right
hand side of the screen
and so i'll just pull out the code um
sorry
okay so now we gotta switch screens yep
cool nice very interesting so far thanks
a lot
everyone and great questions too so can
everyone see my screen
yeah it looks good it's coming let's see
cool
okay let me just okay
cool um so i now cannot see the chat or
any of the anything so if you need to
get my attention just like you'll have
to shout out
cool okay or just ask us periodically
yeah yeah yeah so at the first level um
so there's two levels this model
and at the first level it's very simple
the model there are
there is one hidden state factor and it
has two mutually exclusive states
um high and it just corresponds to the
tone of the stimulus and just high
or low
then in terms of we then separate the
generative model from the generative
process
here like we talked about in the
previous code walkthrough
and then as we're going through kind of
in terms of the likelihood mapping it's
again really simple
uh it's just an a matrix so the a matrix
is just an identity mapping
where sorry these just to go through it
very briefly to revise a bit
the columns correspond to hidden states
and the rows correspond to the
observations so this is saying when you
are
in uh hidden state high tone
you what is the probability that you
will see a high tone well it's an
identity matrix so it's probability one
um when you're in state low tone what is
the probability that you'll see a low
tone and it's again hidden state one
we can then separate the generated model
from the generative process
and the reason we do that is because
this idea of there being uh
so the generative process it is going to
be the probability of a high tone
hidden state or high tone state out
there in the world giving rise to a
high toned observation is is probability
one
but our generative model is noisy and if
you want to actually simulate have an
insular co-brain that's at all realistic
you need to have some level of noise in
that so what i did what we do there is
we just run it through a soft max
function
run the a matrix through a softmax
function
with a temperature parameter that will
very slightly
turn down the precision so if i just
kind of
i'll just run all this
and then if we just open up little a
we see that's now not a perfect identity
mapping but it's something pretty close
by the way so the reason i do that is
because one it's realistic but
also if you want to get erps at all
where erps are essentially changes in
belief
if you have a perfect identity mapping
you'll never get erps because the agent
is 100
confident all the time
so you never have to change your beliefs
if you've got perfect beliefs
um okay then in terms of transitions
um this is just the bees it is again
a identity mapping so that's just saying
these
that's perfectly stable uh high tones
don't turn into low tones low tones
don't turn into hype tones
and at this first level of the model
this is now we essentially plug all
those variables into our mdp structures
that we saw last time
and at the first level of the model the
thing that we need to specify
is this t how many time steps are going
to be at the first level
per time steps at the second level and
we only want there to be one so i'm just
going to set that to one here
and again erp we need to set that to one
this is essentially a resetting
parameter mdp.erp
is the extent to which you reset your
beliefs at each hidden
after each time step at each new time
step and the reason so say you are
modeling a
human being wandering through a maze
where your time steps correspond to say
a couple of seconds in between things it
actually you actually should to be
realistic
or to be kind of have a realistic model
you should have a little bit of
resetting in your
posterior expectations if however
in this case there's uh where on the
scale of seconds or milliseconds
then it makes absolutely no sense to
have resetting going on in your
posterior expectations so we set erp
equal to one
and um
that will yeah the only thing the only
thing i'll say here is this is this is
something that you got to kind of watch
out for because
for whatever reason the default in the
uh standard routines in the vbac the
spm underscore mdp underscore vb
underscore x script
default is the default is four the
default value for erp is four
if you don't specify it and so you'll
get
pretty funny probably inaccurate um
simulations for erps if you don't set it
back to one explicitly
so there's a time scaling factor for how
things are playing out at the
neurophysiological versus the behavioral
time scale
well i mean it affects behavior too it's
just saying it's just saying basically
like
yeah like chris said it's just how much
do your beliefs go back to baseline
um could compare to your posterior
beliefs about that time about the
you know like after the first
observation um
so like you could be just as surprised
or more surprised at time step two
even if your beliefs at time step one
already favored what was going to happen
in time step two yeah
in a lot of cases you just don't want
that you want priors to carry over
so just in terms you could have
something like complete resetting which
would be completely ridiculous but you
could do it if you wanted to
or you could have no resetting at all
which is what makes sense in this
situation because we want there to be
complete carryover
you can do model fitting on empirical
data and ask whether it's a better
fitting model
to have a empirically a 0.6 or a 1 or a
1.5
could you could fit this you could you
treat this as
a parameter that you fit as well yeah
yeah if you were fitting to like match
erp waveforms or something yeah
yeah i would definitely fit it um okay
so this is now this this next part is
where
there are two key points in this where
we kind of there is a
separation from how we would do
a first level model or what a single
level model so
we need to clear so essentially usually
you'll just clear all of your a's b's
and d's because you're going to reuse
those matrices at the second level
and then you'll save your mdp structure
and run it through this little mdp check
thing which should give you some nice
little error
like very usually pretty helpful error
messages telling you if you've got some
weird shaped matrices or i don't know
if i uh if i just have a zero here and
ran it for example
it would tell me hey your b matrix
doesn't make any sense
um so then
you'll then generally clear this mdp
structure and
save the mdp1 into this little mdp
this other mdp structure here so then
moving on to
the slower time scale or second level
beliefs so this is where things get a
little bit more complicated
and so there are three hidden state
factors where these are all independent
probability distributions the first
is sequence type and so this
this is essentially there are three
sequence types
where this corresponds to sequences of
tones at the first level so there can be
a whole sequence
where it's just there's no boobs
and so that would be all high there
could be all low so it's all boots
there could be a high and then a low for
example
and there could be a low and then a high
so this would be does that kind of all
make sense and this correspond where
this corresponds to
different sequences of hidden states at
the first level
got it not all of them have to be used
in each experiment but that's the whole
state space
yep exactly then this is this is
actually where things get interesting so
you have to specify when you build this
type of models
you have to specify a time in trial
hidden state factor which is essentially
the agent's beliefs about how things
evolve over time
and there's actually some really it
seems kind of
like when i first ryan first taught me
how to build these things i kind of just
just had the assumption like oh yeah
this is just like a
this is something that you need to build
for the model to work but it doesn't
it's just kind of a bit of formal
machinery that doesn't track what the
brain's doing
to my delight and surprise there
actually is quite a bit of
neurophysiological evidence
that there are factorized
representations of task phase in both
medial temporal lobes
and lateral prefrontal cortex which is
really cool but essentially this would
be something like
the time in trial that so i'm at time
point one
regardless of what stimulus there is i'm
at time point two regardless of what
stimulus there is i'm at time point
n or i'm in the final time point where i
have to give a response
um regardless of what my response will
actually be does that kind of all make
sense
cool and then the last hidden state
factor is just the agent's response
so we make the to make this interesting
so we could have just set this up as a
hidden markov model and not had the
agent give responses
um which would have been fine just would
have been a very passive
model and just kind of to make this
interesting and then
so that people can read it and then
build their own more sophisticated
models and see how you would specify
policies in a deep model
i basically had the agent at the last
time step so the sixth
time step just say whether the last
beep or boop in the trial was the same
as or different from the previous
the previous beeps or boobs
is that all clear so far yep
yeah and then so the idea is is that
these sequent types the agent has no
prior expectations over all of them it's
totally flat
so when this gets when this d first d1
gets run to a softmax function this will
just be a completely flat vector
now but the agent always has a perfect
prior belief
that it is in state one
and it also has the perfect prior belief
that it doesn't know or it's just not
it doesn't have any response prepared in
terms of
what report it will make
again and what we do here is essentially
we separate the generative model from
the generative process
so just put little d2 just so it's kind
of not to confuse people with
these different levels and we multiply
what's this is actually really crucial
so when you specify a d and separate it
there's a little flag in the vbx script
or the model inversion script that
tells it okay you are now learning d
and you'll get updates to d but
sometimes you don't actually want to
simulate learning
you want in the very same way that you
want to like simulate
some process outside of learning or some
process independent of other things
in a lab when you actually run
experiments sometimes you just want to
isolate one process and simulation
so to essentially turn off learning you
just make the concentration parameters
in these which are concentration
parameters from dirichlet distribution
like really massive and so the
difference between say
100 and if adding one adding a count of
one will essentially do
nothing to the agent's behavior then if
the concentration parameter is already
at 100
which is why we specify this way
yeah so if you think about it i mean
depending on the type of task
if if the thing thinks that learning is
going on because you're separating the
generative model from the generative
process
then if you have low concentration
parameter values
then the uh then the epistemic value for
parameter exploration will will make a
big difference
right the thing will actually be driven
to move to states
that will help it learn something about
what those concentration parameters
should be um so it can affect behavior
in ways that kind of um uh
cause problems for the kind of tasks
that you're trying to model
um so so one thing yes is that
having them at really high values means
that the agent just isn't going to do
any
seeking information about parameters
because it just thinks it already knows
them
really well um but also it still
is going to add counts to those
distributions after each observation
so like you know changing a distribution
from like 100 to 100
2 100 to 101 the actual distribution
is like still basically the same whereas
if it was like
one and one and you add a count so it's
not one and two
that's a very big change in the
distribution um
so both of those things together just
kind of make it as though
it doesn't think it it's learning
anything
cool okay um is that cleared everyone
all good to
move on
yep so okay so then the next thing so i
think
the hardest part of doing active
inference or building these models is
factorizing the a matrix so these are
all independent distributions
right but they interact in the a matrix
and so you have to that you have to
think about that when you're specifying
it
and so what this one what this matrix
says is so remember that
our first hidden state is uh sequence
type
so this is just and our first outcome
modality is just the stimulus
and i'm just going to quickly dip down
to see how these how this level is
connected to the bottom level
we have to specify something called a
link function and this will just be a
little matrix or a vector depending on
how
many states hidden state modalities you
have at the first and second level
where the rows in this matrix correspond
to lower level hidden state factors
and the columns correspond to high level
uh outcome modalities and so all that
we're saying and so when you specify
these things you actually need to be
careful
that say the number of even states
you have at the higher level well sorry
the number of outcomes
that are possible in your outcome
modality match the number of hidden
states that you have
in your first level
at the first level does that make sense
because
your second level of your model is
treating those first level hidden states
as observations
so here the two observations are high
tone or low tone and all this is saying
so this this
first column is high tone second column
is
or high sequence second column is low
sequence
third column is high then low
and last one is high is low than high
this is
and we're specifying this for time step
one to three
so what we're doing here is we are going
to
so we have a set up at a matrix where
there's four hidden states
corresponding to sequence type and two
outcomes just to reiterate and then what
we're going to do is we're going to loop
over
the six time points in the trial and
loop over the order of states in the
report and so then we're just going to
step
but um
then basically i'm just going to set set
set this up so that
um the time that there's just an
identity mapping
essentially between hidden states and
observations
and i've done this i've looped this over
all but this is actually not an accurate
generated model because we want there
to be an oddball at the fourth time step
and so i
just specify that here so i take this i
set which corresponds to
this kind of second hidden state factor
and i set it equal to four
and what you can see here is that
there's now a change in the mapping
so remember this first column is high
second column is
low third column is high low third
and then fourth column is low high so we
now see a change so this is then saying
when you're in a high hidden state
at the fourth time step you'll see
a high tone when you're in a low tone at
the same thing
but it gets interesting or it gets a
change you get a change from the matrix
above
at the fourth time step because when
it's in a high low
at the fourth time step it will it will
hear a low
low tone and at in low high you'll hear
a high tone
is everyone pretty clear about that
yes and we're looping over
all this one what j equals one to three
in both of these is just saying we're
looping over all possible responses
so we're not making that identity that
mapping between those hidden states
between
the first sequence sequence um first
hidden state sequence
and in any way dependent on the response
so it's independent of that
so then the second outcome modality that
we need to specify is just report
feedback
so with the agent we're going to have it
make an action
or specify a policy allowing it to make
an action at
the fifth time step at the end of the
fifth time step
so i'm sorry the sixth time step rather
um
and we then
need to kind of give the agent feedback
so
there are three hidden states and this
is no longer
this feedback modality is not connected
to the first level
and so there are three outcomes null
which is just we don't give the agent
any feedback so it just has a totally
flat
preference distribution essentially over
this
over null doesn't care for the first
five time steps
and then at the sixth time step we need
to start messing with
whether it thinks it's going to be
whether agents thinks it's going to
receive
wrong versus right feedback so
this would be saying something like okay
so here you report that they
are the same so this is response
two so j equals two and i
equals six correspond to the six time
step so these where these correspond to
what we're indexing into elements of
these hidden state factors
and then so the idea is then what this
is saying is that
at hidden state for one and two if you
say they're the same remember this is
all highs all lows if you then say it's
the same you will get correct
feedback and because this is high
low and low high if you say it's the
same will give you incorrect feedback
then we see this is reversed when we say
the agent is going to give the agent the
option to report
different so these two will be incorrect
for high and low sequences and correct
for low high and high low
everyone with me
yep cool okay then again
just like we did before we're going to
reduce
the um constant we're going to separate
the hidden states in the
um sorry the uh hidden uh
generative model from the generative
process and reduce the precision
by with a temperature parameter of two
which is super precise it's just not a
perfect identity mapping
and we're then going to disable learning
again because we're not interested in
learning at the moment
um by the way you do get fairly similar
results if you do learning so i'm not
kind of like uh cooking the books
it's just that in terms of the tutorial
it didn't really make sense
to add an extra several lines on
learning for a fairly simple simulation
it's awesome and just to highlight that
is a similar design move
as when you mentioned several times
separating the generative process from
the model
it allows you to have a cue that isn't
always associated like
high tone is the high tone they hear it
perfectly but now it's a situation where
they can't really tell if it's one shade
of a color or another so
it it allows a lot of expressivity and
it will just be really awesome to
in the coming months and years see and
return to the code
to understand exactly how different
groups are implementing it to model
different specific situations that kind
of just go down these roads that you're
just pointing out but we're staying on
the
on the freeway but you're pointing out
different exits that really are
interesting
yeah exactly so there's lots of i mean
there's quite a few different
like like in previous papers you know
for instance like
we've modeled things like noisy like
noisy learning right so where for
instance like in the generative process
it is
you're always being presented with one
object right and that's like 100
true but the the a matrix and the
generative model
you know you kind of soft max it with
some precision parameter like chris was
doing so it's
it's um not very precise so it's kind of
like for instance like seeing an object
but having it be blurry
you know or something like that um you
know so it's how well do you learn
uh from stuff even if what you're seeing
is kind of imprecise or like for
instance figuring out where
whether a tone was present in some like
white noise you know like into some
experiments to do that kind of thing so
yeah i mean these models are incredibly
flexible um for whether you want to do
just perception or just learning or just
decision making or decision making with
or without learning
um so it's i mean that's part of why
they're so why they're so uh
nice yeah and so then just kind of
moving on to the transition
probabilities
um so b b2 this is just
so this corresponds to our first ident
uh sequence
of tones hidden state factor and this is
an identity matrix
four by four identity matrix because
there are four hidden steps
um this is just saying that our our
sequence doesn't change to another
sequence halfway through that makes
sense right
um now our things get interesting in
terms of specifying the transition
functions
uh when we talk about the second our
kind of
trial phase uh
transitions and our policies so the idea
here is that
we then specify this trial phase
transition function so that
it will kind of deterministically step
through
all of the phases in the sequence so
this is state one
or row sorry columns r state hidden
state one
rows are will be kind of hidden state
one hidden state two
so what this is saying is that at time
one a hidden state one transitions to
hidden state two
hidden state two transitions to hidden
state three and so on and if i wanted to
if i wanted to
to simulate some infinite number like
it's not actually infinite this is a
finite horizon mdp
but if i wanted this infinite sum or
sorry simulate some very large number of
these trials
i could put the last one so this last
trial
or sorry when it's in the last report
phase it will transition back
to the first phase for example but i
don't want to do that i just want to
have the last time step in the trial as
an absorbing state
that it'll that the simulation will stop
on and then
uh simulate each trial as kind of a
separate thing
but just highlight that in case you
wanted to do it if you wanted to like
simulate um
there are some ways of simulating kind
of heartbeats and things like that where
you specify
a transition function that has an orbit
built into it
so then in terms of report this is this
is the controllable hidden state factor
and these it'll will add will now have
like a multi-dimensional matrix
um where the third dimension in the
matrix just corresponds to
basically the control state so this
would just be uh i am in null and i am
going to stay in null
i'm not going to do anything the second
one would be you can get
from any hidden state you can chorus you
can transition yourself into reporting
same
and this third one is from any hidden
state you can transition yourself into
reporting different
then in terms of the policies there are
six hidden
six time steps so we specify that here
we specify the number of
hidden state factors so remember again
there's uh sequence type
uh time and trial and report modality so
three then we've got two policies so
these are the number of options that the
agent will have
and then these are deep policies so the
agent which is consistent throughout the
whole trial and so basically
or this is to say the agent will be
computing these
over the course of the whole trial if
that makes sense
um and so all this is saying is that the
agent stays in state hidden kind of
action one which is just null it doesn't
do anything it doesn't do anything it
doesn't do anything can't do anything
and at the last time step we allow it to
choose
and that just corresponds to kind of you
can imagine not actually presenting the
participant with
in a psychophysics experiment or
whatever not
presenting it with an option to actually
move change the key
hit a keyboard or anything like that
until the last time step of the trial
um okay so last bit uh any questions so
far
no looks pretty good though thank you
um then okay so then we've got the first
c matrix
this will just be a two by t
or two by six matrix
of zeros so if i just kind of hit go on
this we can take a look at it
[Music]
whoops
i'm going to hit run at some point soon
we can check out everything
but this is just what the c matrix looks
like so it this is the preference
for the agent's preference for hearing a
particular tone so this is just saying
agent doesn't care at all it has no
preference for tone
then our report hidden state this is
again it's going to be completely flat
essentially except for at the last time
step when it receives feedback
it has a preference for not being
incorrect and
a uh preference for being correct
um so i just uh just i just want to make
sure people understand that that
so the uh the brackets um you know we
went over this last time but the
brackets
cor like are what say what outcome
modality corresponds to what a matrix
oh yeah so like c2 brackets two means
that that corresponds to the
observations
in uh the a matrix uh with brackets too
right so so that's how you that's how
you know
that this is the one that corresponds to
observing
feedback um whereas the first one is the
one that corresponds to just observing
tone
so just just to make it clear that you
use the bracket numbers to assign
to the outcome modalities yeah
and then so then that's basically we've
built our mdp so we're just going to
specify it so we've we've now got our
earlier mdp structure if we remember
so this is mdp one and this is the thing
that we specified all the way back when
we were talking about level one
um and we then plugged that into our new
mdp
structure so we'll have mdp.mdp so this
is the
the markov decision process at the lower
level
we then plug it into this our new mdp
structure
or this will just be a subordinate mdp
and we have to specify a link function
we talked about that before but just to
reiterate
rows here are or sorry i'll start with
rows are lower level hidden state
factors
and columns are higher level observation
modalities so all that we're saying here
is that we want the low level
observation modality or
low level hidden state one to plug into
observation modality
one so the hidden states the first level
will be treated but as observations at
the second level
um okay then we just plug in all of our
variables that we saw before
time our likelihood mapping the
generative
model for our likelihood mapping um etc
etc
and so c's these and our v which is
our policies and then again we need to
reset our
decay reset parameter to number one
then in terms of mdp that we can just
specify names
for our outcome modalities and our
transition functions which will just
kind of make
interpreting the plots a little bit
nicer and then lastly
you just plug the whole thing this whole
mdp structure into spm
mdp check thing which will again give
you some nice informative error messages
which are extremely helpful
um i still use that thing all the time
um and then we can just run it
and so let's do that right now and by
the way so i i do have a lot
of uh i'm just going to run it and kind
of show you what it looks like and then
i'm going to go through how i simulated
each of the specific conditions
because we did something similar to how
we simulate ryan simulated learning
um
okay
cool so i'm gonna hide this stuff for
now um
slight spoiler
um okay and so this is just i'll just
look at one of them
sorry just so we get an idea of what's
going on
um so this is just hidden state sequence
the sequence is the same
the agent believes it was the same
throughout the whole trial great that's
true
uh time in trial transition to the next
point just as we expected it
and then at the last time step because
this was a
um all kind of uh all high
it just said they would um they were the
same
and so then would it got the answer
right and
i think it's only sharing your uh it's
only yeah it's only showing
the matlab window we don't see that we
don't see the
plots oh really
uh um okay
let's see if i can goddamn it
if you if you dock if you dock them you
might you might be able to pull it up
yep slide into the ide
i can try um or share
a whole spring one can you see the
screen
now yep yes now yes okay thanks now we
get to the plot
yeah sorry i was just like talking to
myself then that sucks
it was fun um yeah okay
um so this again this is the stable
hidden state
hi this is our trend this is our kind of
time
time and trial thing stably
transitioning from one point to another
and this is our report hidden state
which just says at the second time step
the agent reported
same and then it got feedback that it
was correct
cool so then i'm just going to quickly
go through
essentially how i simulated all the
conditions because remember we want to
simulate local deviation and global
standard and local standard
global deviation that makes sense so i'm
going to simulate 10 trials where that's
10 collections of
beeps or big boops in a row
um and what we want to do
is essentially have the agent where it
is going to be doing some learning it's
going to be learning a prior expectation
over what sequence it should be in
if that makes sense and so yes
just to make sure they understand this
so go back up to the diddy's
so if you notice he's only multiplying
d2 and d3
by a hundred yeah
d2 brackets one the first the first up
the first state factor
is still just one one one so
which allows it to learn one but not
learn stay factor two and say factor
three
yeah exactly um and so what we should
have at the end of our local deviation
thing for example
so we have two oh sorry wrong part of
the code
okay so for our local deviation global
standard manipulation
or simulation what we're going to do is
just the first nine trials
will all be a
high low so it will be
boop and then the global so then our
tenth trial however
is going to be a um
is going to be the same because it's a
global standard so the global standard
is
the bbb boop but we should get a kind of
local deviation and we should always get
a mismatch negativity
because there's the last one deviates
from the kind of the local temporal
regularity if that makes sense
then in our local standard global
deviation we're going to invert that
structure
so the first nine trials are all high
low
so again we've got bbb boops
but at the last time it's time step
there
is a beep beep beep
and when we do that what we we won't get
a um we won't get any type of mismatch
negativity or first level erp to that
last
kind of surprise response that last at
the last time step
we will however get a a global deviation
because the second level is now really
surprised that there wasn't
a deviation at the first level does that
all kind of make sense
nice cool and basically what we do is
we'll just specify
n equals 10 this number of trials we'll
put our we'll get our mdp structure that
we kind of
put together before we'll put it into
our mdp deal
so that will just be give us 10 mdps
which are to start with
all identical and then we're just going
to choose to select the 10th one
and change either have
and mess with the hidden state factor so
here we're not actually changing it's
the same as
the first 10 uh the first nine but in
the second example we're changing it
we're changing it from a
local deviation to a local standard
or um which will give rise to a global
deviation and so now if i just
i've then kind of i'm actually not going
to for the sake of time i'm actually not
going to go through all of the code for
kind of just plugging this stuff in
because this is literally just putting
our structures into a
plotting script and here things get more
interesting
here is where i make some custom erp
plots which i think are kind of cool
but again i actually don't think walking
through the code is particularly helpful
i think it's just the type of thing like
the way i learned this was i just spent
like a day or
half a day just reading through uh
someone else's code
and figuring it out um so the the only
thing that i would
make sure is that so when you um
when you're doing this uh u1 underscore
one
i'm sorry like it's just these are ways
of indexing and pulling
the uh the actual simulated um
firing rates and erps um out of the spm
out of the mdp structure after you run
it through the vbx code
yeah so these are this is just
representing uh kind of the
the most straightforward way of pulling
those similar simulation results out of
particular
cells in the um in the mdp structure
after it's run
and we have a table in the tutorial i
think it's table three
that explains the structure of each of
those cells and where each of those
um each of those uh simulation results
are
yeah exactly and so then i'm just going
to hit run or kind of walk through what
this stuff looks
what these plots look like together um
nice cool okay
so these are my custom erp plots
on the right and so i'm going to start
start there actually because i think
they're kind of nicer
okay so
cool so far left we have a
or top top left sorry we have a
global standard versus a global
deviation
and the way you calculate the mismatched
negativity is you just subtract
the global step the global deviation
from the global
standard and then you get this nice
that's what we have on our top right
we have this nice kind of negative going
erp that looks exactly
i mean i'm not going to show you this
but if you want to satisfy yourself with
this
it this looks like kind of for such a
simple model this is it's kind of
shocking how much this looks like a
standard mismatched negativity
so that's really cool then on our second
one here this is our two this is our
global standard
which is in blue and our global
deviation which is in red
and then we can subtract them from one
another and what we can we can just look
at
kind of the um the
we get a nice large positive going
potential
that looks a lot like a p300
so then in terms of
our i'm just going to show you a couple
of the local deviation local standard
things um sorry i'm gonna close these
and these just kind of clean up the
screen it's nice though that someone can
just download this and also
an important note is installing all of
the spm
prerequisites maybe we could do a
standalone in the future but
once the packages are installed someone
can just run the script and have
also all of these figures be spit out
and then it looks like there's enough
commentary and hopefully these videos
are enough of a
walk through at least of early versions
of the code where you can tweak
different things and start seeing how it
plugs into other
things you might want to explore with
the model but all these figures just
come out in one batch and
just fighting them away over there
christopher yeah exactly
so i guess one thing to say is one
reason why i'm not particularly
motivated to
make a big standalone kind of thing is
by the time even if i were to do that
which i don't want to do but even if i
were to do that
by the time i'd written all rewritten
all of the functions i would essentially
have a package
that is as cumbersome to download as spm
but spm is written in a really nice way
and it's super easy
to install um and so it would actually
be a lot easier
it's just a lot easier to install spm
that would be to go to my github say
and put all of this stuff onto your
laptop make sure all the paths work nice
because they've automated
a future supplement could just be start
with a virtual machine
and let's just install the prerequisites
and just actually do a full
clean installation could be a good point
of reference but thanks for that
point continue yeah i mean it's i mean
it's really very it'd be very
short and sweet to do i mean downloading
spm like is
you know it's freeware i mean it doesn't
just takes a couple of minutes to
download and really all you have to do
is just once you download it is just go
into matlab and set the path like that's
it yeah
i think there's a function called
install spm so you go into matlab and
run the
run the function install sp
um okay but returning to this so
each of these points kind of everyone
see my my pointer i'm hoping yes yes yep
each of these pointers this is all a
time step at the first level
and so this is kind of local standard
and
a global deviation right
um so this will be we see there's a
little erp each time there's new
stimulus presented
but there's not not a major one that
makes sense because it's the same
um and our this is trial 10 by the way
i should say this is trial 10 so i i
have trial one
versus uh maybe i'll just maybe i'll
just contrast all the trial tens because
otherwise things get messy okay
cool this is trial ten um
and so this is trial 10 for local
standard
global deviation and so we see kind of
no
first level erps really all no enhanced
erps they're all the same
but this last one because it this last
or sixth
erp right because it disconfirmed
a prediction essentially there is
a enhancement in higher level beliefs
when the model suddenly changes from
thinking it was a
high high low high high low
to a high high if that makes sense
and then if you compare that second
level erp to this one over here which is
this local deviation
global standard it's smaller
that p300 there is smaller amplitude
but at this first level because it kind
of confirmed that there was a deviation
at this first level you see this first
level there's this
massive like deviation response in
um so does that all is that all fairly
clear because i think that's just about
all i have to show
um i i do think this stuff is really
cool it's kind of nice to chat about it
um
so just to i want to be very clear that
i'm understanding
with the um event-related event-related
potentials that you're
showing that you superimposed and you
got
based off your hierarchical model um you
could then superimpose those
uh erps which are related
to gradient descent on the variational
free energy which is related
to dopamine expression and as we showed
uh way at the beginning of this video
that relationship between membrane
voltage and
expected firing rate mean population
firing rate and we're taking all of
these things together
to provide the superimposed traces of
the local fuel potentials at any given
instant
um and we're showing how this oddball
paradigm
could play out uh conceivably by
re you know with a simulated version of
this model how it could be realized is
that
yeah exactly the only thing i would say
is that this
these these simulations have like
nothing to do with the dopamine stuff
yeah i was i was about to say the same
thing inside
okay with the exception of like dopamine
having to do with how you choose
policies
so if we just like blew up the dopamine
receptors
or sorry this like in silico dopamine
and just made it like
we could make the agent behave totally
randomly or we could make it behave in a
super precise impulsive way
um or something something along those
lines
sorry i shouldn't have said that uh
impulsivity is a bit complicated
um but we could make the um agent behave
in a totally random way and choose
random actions which would again
have effects on the sensory sense on the
sensations that the agent would receive
so it would indirectly affect erps
but there's nothing about like that
gamma term that would affect
uh state prediction error which is there
so the primary could effectively turn
off
you could just turn off gamma right and
like
and it wouldn't yeah it wouldn't make
any difference to this exactly
so so then just so that i'm getting it
correct
the more important thing then would be
the membrane voltage which is related to
the
free energy minimization and your
schematic diagram of those excitatory
imputative inhibitory connections that
you're realizing in this model
exactly yeah it's just it's just about
rate of change and posteriors over
states
okay totally so i'm just going to stop
showing my screen at this point um
so hopefully you guys can no longer see
my screen
nope we're back to just just you
know cool well wow what a fun and
interesting
session let's uh
first just really appreciate everyone
for coming on because these are
extremely
didactic and it's really just something
else to be walking through the code and
seeing how many degrees of freedom there
could be and also how
real it can be when we actually specify
it so any closing thoughts
or and what can people look forward to
for part four which is the final part
before the
semester begins for some of us
yeah no i mean uh like i said i mean the
last the last one is just the last
section of the of the tutorial which is
kind of where we're
building to this whole time right is how
to actually
apply this stuff to empirical data and
do real experiments
uh can i ask a question on that is
someone asks
can we use this tutorial to construct a
generative model
of metacognitive control of attention or
meta awareness
i.e modeling task-free conditions say
while doing meditation for example so we
talked a lot about task modeling
how does this generalize yes i mean you
kind of have to
so i mean uh you know the first question
is just how do you make that
you know like really concrete right
so i mean there's there's very easy ways
you know like i've published a couple of
papers and so has um
you know several other people um doing
something like cognitive actions
selecting cognitive policies as opposed
to behavioral policies
and these are things like where you like
selectively choose what to pay attention
to
um you know or selectively choosing you
know what to kind of hold in working
memory
or you know like things things along
these lines that don't involve any kind
of like over
observable behavior but involve um
selecting cognitive fully internal
actions
right like something like selecting ways
of manipulating lower level
representations things like that
um so that's certainly possible but what
you would need to do then
is say okay you know what does
uh meditate what does a meditative
action look like
right like it could be something like
for instance making a
like choosing a policy at a higher level
that say like for instance like
really really really reduces the
precision of like
an a matrix or something right if you
wanted to completely
you know like cease to attend to
anything like in the external world
you know for example um you know or for
instance
maybe the opposite right maybe like
mindfulness you know has to do with
actually paying really really precise
attention to the present
but like making your uh transition
matrices
super imprecise so essentially it's all
about the present and like you're not
thinking about anything in the past or
the future
you know or i mean i could i could think
of lots of different ways you might do
something like that but
to really make it you have to turn it in
to something task ish right you have to
define actions
you know even if they're fully internal
actions you have to define the way they
relate to perception the way they
manipulate the processing perception
um you know i guess like you have to
ultimately boil it down to something
really concrete with an exact
quantitative structure
but all the resources are certainly
there to do it
if you're creative enough to come up
with a regenerative model so i have a
yeah i have two things to add to that so
first is that i think there's a really
there's a really cool kind of like early
pre-print i'm not sure if it's been
published anywhere it's just called
towards a formal neurophenomenology of
metacognition
um lars sandoval smith is first author
maxwell ramstead who i think has been on
the podcast before right there he's the
he's the senior
um they actually do try and model
metacognition and
specifically in meditation and
meditation context
um i would just say one thing that i am
personally skeptical about um i
encourage everyone to do this kind of
work but this is just
this probably highlights my biases but
i think if something is hard to study
empirically that is to say
it's very hard to study in terms of
urine imaging
for example how are you in creating like
an event related design
where you can get precise time locking
to neuro between neuronal responses
and cognitive processes for example if
something's hard to do that in an
experimental context
it's going to be extremely difficult if
not more difficult
to do it meaningfully in terms of the
generative model because i think
these generative models are only
meaningful and helpful to the extent to
and other people are free to disagree
with this um this is just very much
you're going off on my own kind of
tangent that's just to say it's almost
like you need to get more rigorous it's
no longer just like well this one thing
happened with this one setup
it actually demands a higher standard
but things that it lets
above that higher standard are very
cross-referenceable very interoperable
so very nice very nice statement
yeah i mean i should i should say that
like like i guess you can think about
these models as you know beyond the kind
of more specific applications we've been
talking about
is doing kind of two you know doing like
a couple of like broader things
one is is that you can use them for kind
of
theory making theories precise
right so for example like um so a lot of
my past work like
i focus a lot on like like theories of
like emotion and emotional awareness and
how that light still
relates to like you know psychiatric you
know like clinical
contacts and things like that um but
you know prior to doing a lot of this
modeling stuff
um it kind of comes out of these like
fairly hand wavy conceptual review
papers right where it's like boxes and
arrows and
you know like it's and sometimes in
those cases it's hard to
go from kind of the theoretical boxes
and arrows
um you know even if you assign say
neural regions or systems to them
it's hard to to make those things really
precise so that like
it's very clear that one empirical
result would actually confirm or just
confirm it
um whereas so you can take you know like
a kind of conceptual you know somewhat
hand-wavy model like that and then turn
it into an exact
generative model which can just make
your theory really precise you know so
so like one day you know it'd be really
cool if instead of like review papers
it's like review paper plus
actually here's a model you know like a
precise quantitative
model that we think comes out of
unifying all the results
as opposed to um less precise
um theories one one other nice thing you
can do with these models is just like
have a
total proof of principle someone someone
might make a radical claim like there is
no way that you can conceivably do
x and then the response that is here is
a model that does
x um and that's useful right
that might not be it might even not be
an empirically tractable example like i
think the dark room problem is an
example of this right
like you could say there is no possible
way of designing an active inference
model
that will escape the dark room and then
you can build a model and say
active inference agent escaping the dark
room like
that would be a really shitty boring
experiment to run i hope one
but it's a argument about argument by
construction
but especially when people have these
edge cases or perceived to be edge cases
but that's how philosophy
is at the fringe and at the border and
expanding and critiquing and improving
all these different metaphors that have
come up
in discussing like 14 was what is the
dialogue
between science and the modeling and the
actual
quantitative components of it and the
empirical work and
philosophy so it's really just we're
coming at that same question from a
little bit of a different angle
so i think this has been a great length
and a great
session ryan christopher max really
appreciate all of you for
coming on so that's going to be it for
today but it will be
our final session next friday
at the same time at 9 00 a.m pacific
on february 5th is going to be
number four so thanks everyone for
watching live and replay thanks again
to authors and participants so peace out
everyone
yeah thank you bye thanks
