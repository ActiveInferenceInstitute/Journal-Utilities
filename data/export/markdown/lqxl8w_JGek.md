---
title: "ActInf Livestream #024.2 ~ "An empirical evaluation of active inference in multi-armed bandits""
category: "Livestream"
series: "Livestream_024"
episode: "2"
duration: "1:35:53"
url: "https://www.youtube.com/watch?v=lqxl8w_JGek"
views: 110
exported_at: "2026-02-18T22:37:37.908397+00:00"
format: markdown
---

# ActInf Livestream #024.2 ~ "An empirical evaluation of active inference in multi-armed bandits"

all right
hello everyone and welcome to actin flab
live stream number 24.2 today is
june 29th 2021 and
we're looking forward to this follow up
or jump off discussion
with some of the authors as well as
other lab participants on this
awesome paper an empirical evaluation of
active inference
in multi-armed bandits welcome to the
active inference lab
we are a participatory online lab that
is communicating
learning and practicing applied active
inference you can find out more about us
at the links on this slide
this is recorded in an archived live
stream so please provide us with
feedback
so that we can be improving on our work
all backgrounds and perspectives are
welcome here
and we'll be following good video
etiquette for live streams it's great
that there's
so many on the call and i'm sure we'll
have many questions and opportunities to
raise our hand as well as for those in
the live chat to ask questions
whenever they feel like it we're closing
out
june with this dot 2 discussion
on paper number 24. so last week we
also spoke with sarah and dimitri and
others that was very
informative and now we're in the dot 2
we're able to take it to a few different
places
and raise up a few questions that were
asked over the last
week and the goal is really just to
learn and discuss this paper and related
topics we have a few
cool related areas that we're going to
be going into
so we can just begin with a introduction
round
each person can say hello or check in
say anything that they're thinking about
today
and then pass it to somebody who hasn't
spoken yet so
i'm daniel i'm a postdoc in california
and i'll pass it first to blue
hi i'm blue i am an independent research
consultant based out of new mexico
and i will pass it to ryan
um yeah i am ryan smith i'm an
investigator
at the laureate institute for brain
research um and i'll
ask you sir hi i'm sarah i'm a postdoc
at the technical university in prison
and i'm looking forward to the
discussions today
and i pass on to dimitri
hi everyone i'm dmitry markovic postdoc
at technical university of raisin also
uh chair of neuroimaging and i pass it
to
dave can he talk actually
no my background's
a basic psych and cybernetic learning
thing
and i'll pass this to stephen please
hello i'm stephen i'm based in toronto
i'm doing a practice-based phd around uh
social topographies and
immersive experiences and i think i'll
pass it back
to daniel if i'm not mistaken yep
great thanks for the cool intro round
so sarah prepared this slide which we
just want to
start off with so go for it sarah
how does this set the uh intention in
the mood for what we're going to be
going into today
uh wait how can i make it so that i see
it pick again
no okay so um after
the discussion last week and also the
questions we've got we thought it would
be a good idea
to just make a short overview slide
about what we understand as active
inference
and as cognitive neuroscientists you
said in the discussion before also
we are often or mainly interested in
this
action perception loop that an agent
where we as living agents are in with
our environment
and that's what you see on the right
in this loop and on the left side on the
right you see the environment it may
have
hidden states that are the states that
you may know
from markov decision process processes
in reinforcement learning
but that may also be more abstract
things that aren't observable tone
agents like
contexts volatility parameters
anything that describes the environment
and these hidden states may also
evolve with time and then such an
environment generates an observation
that the agent then integrates together
with
its prior beliefs in order to infer the
hidden
states of the environment which is what
we call perception
then you can use this information to
plan ahead
and select an action accordingly and in
turn the action may
change the environment the agent is in
and concretely how the agent side of
this works
in active inference is so that you
specify
a probabilistic generative model
that contains the hidden states
you are a priori knowledge or your
assumptions about how these hidden
states relate to each other
which states may follow up on which
states and so on
it contains observation generation rules
it contains actions or policies
which in active inference are also
treated as hidden variables that need to
be inferred
and additionally the generative model
may contain its own parameters
as a random variable so that they can be
inferred
and there was learned then you
specify a probability distribution of
approximate beliefs
in theory you could also
solve the beliefs of the generative
model
analytically but that becomes very
computationally expensive
really quickly or even analytically
intractable
so what you do instead is formulate
these approximate beliefs
which are supposed to be of a simpler
form
and for example in your approximate
beliefs you could assume
that all hidden variables are
independent
random variables which makes the beliefs
very easy to calculate
but may not properly capture the
temporal dynamics for example of your
environment
and this this independence assumption
is also called the mean field
approximation but you could also
say no with some hidden variables it's
very important that they
are allowed to co-vary and be dependent
on each other
and then you would have pairwise
dependencies in these approximate
beliefs which is then called the beta
approximation
you may have different approximations
for different variables some may
vary together others are independent
then you plug in the generative model
and your approximate beliefs
into the free energy and then you find
your approximate beliefs at the minimum
of this free energy
and this way you can form about beliefs
about
hidden states of the environment which
really can be anything
your location
volatility of the environment the
context you're in
you infer believes about policies which
is a probability distribution
over actions from which you can then
choose
and you can even form beliefs about
parameters of the model
and there with update your knowledge of
the model in each time step
and then in the end you can use all this
inferred knowledge
to make actions um
yeah we as cognitive neuroscientists are
often interested in this whole loop
but um what dimitri showed last week is
also that in principle this
can be really modular right so um
in our paper for example perception
was the same for all different
agents whereas dimitri then
plugged in different action selection
algorithms
one corresponding to the expected free
energy and active inference but other
well-known action selections algorithm
too so
um here you can really also play around
with this framework
and um use its modular nature you could
on the other hand use the same action
selection algorithm
and compare different learning
algorithms which is something
we're also often interested about in our
work
and yeah with that that's it from me for
now
cool very interesting and anyone can
raise their hand but i think the part
that spoke to me
there was just that it's a framework and
so it's kind of like the framework of a
desktop computer you can
take out the memory or change out the
hard drive
and so we can talk about changing the
environmental dynamics
with respect to the hidden states and
how they evolve through time
we can talk about changing perception
but we can also like
lock in multiple of the components
and then explore how different learning
rules influence system behavior that's
what we
explored in this multi-arm bandit paper
but it could be the same
learning and policy selection rule but
then a different perception
rule and then those might map onto
very subtle differences in um decision
making of
agents that we care about like what's
the difference between somebody who has
blurry vision but they know the language
versus clear
vision but then they're semantically
unsure
about what the symbols are representing
um yeah stephen and then anyone else
who raises their hand yeah this is
really
interesting and helpful to see your
thinking here i'll just be curious how
action states or um you know the idea of
different types of states
alongside these hidden states and just
how that
you treat those in your thinking um
because there could be kind of the
action states that are imagined
um and the action states which are
part of the kind of external environment
that you're somehow immersed in
so in the end yes actions are also
treated as hidden variables i think they
are very separate from
other from the hidden states for example
because
the space of actions determines what an
agent can choose
and you cannot choose a state
um in terms of other hidden variables
i think so for example if i think
location versus context then um in my
head the generative model becomes a
hierarchical model exactly
and in the end yeah
that's also what i meant when i said you
plug
in your a priori knowledge or your
assumptions about the environment
because different types of hidden states
will have different
relationships to which and then you
really end up with a completely
different
uh generative model
just to follow up there sarah you said
that when
location and context are differentiated
that it's a hierarchical
model so what does that look like on
this
layout
you mean in this figure here like what's
the setting where
location and context are identical and
so it's a non-hierarchical model versus
a case where they are differentiated and
then it is a hierarchical model
so for example um if i want to model
myself
walking through my flat that wouldn't be
a hierarchical model
where just each location maybe the
different room
rooms count as states that i infer based
upon
the curtains i see for example
but then if i want to introduce another
person's flat
then the transition dynamics
may be different for their flat so for
example in my flat i can go from the
living room into the kitchen but in my
friend's flat
i cannot make the state transition and
that's actually something i'm working
with currently where an agent
like the underlying decision process is
very similar but an agent needs to infer
which context he's in in order to
then load the correct transition
dynamics
that reminds me of the spm textbook
how it talks about hidden states being
just the state that
a process is in that generates outcomes
so we have a clear distinction between
the hidden stage which aren't directly
observed
but there is this hidden state like
which
flat am i in and then that is going to
change the transition dynamics between
the rooms
but the observations are what are
coming to the agent and then also
there's like learning
which we don't have here but that would
reflect the prior beliefs being updated
through time
what about this planning stage like what
is happening in this planning module
um that's a good question actually
nowadays um so this figures from my
previous paper
nowadays i um lamp in perception and
planning together because it's really
not that easy separable
um the pro so in this case what i meant
is
perception is really inferring passed
up into the current hidden states um
to which i had the observations that
belong to each state
whereas planning is inferring future
hidden states and future observations
and potentially future rewards
but in the end it's all one model and
it's a
chain to go through the states so the
differentiation
only makes medium sense i think it's
rather one
inference problem
interesting thanks blue and then anyone
else
so just thinking about metacognition and
where
that might fit into this model
um i didn't actually have some
um has published a paper on a meta
cognition recently also
so map control actually right uh
but but yeah i mean one can just see uh
one can stack
multiple agents on top of each other
and imagine as a kind of higher level
agent controlling what the
bottom level agent is doing and so this
would be like
well deep active inference models and
in one of the recent papers we're also
exploring this in a kind of
as a meta control approach for
describing
uh like cognitive control
so if there's some kind of downward
causation does that then inhibit like
what's going on at the
like lower agent level
yeah so basically right you can see kind
of actions on the higher level
uh are defining flyers on the lower
level and
selecting the policy space right so what
kind of your level age lev lower level
agent can actually do
where this right this isn't
now just kind of illustration of kind of
separating maybe
higher level cognition from the
executive part which is kind of
moving uh uh arms or muscles on your
body
uh it's it's interesting about that like
kind of like a virtual machine
or a hypervisor that there's this like
emulated
agent you know what would my better self
do
that's a classic metacognition question
and then also it was just interesting
that you know blue you asked about
metacognition and then
dmitry you write to meta control and so
that really
speaks to the way in which we're
thinking about cognition
as control and that's part of a control
theoretic perspective which is that like
the cognition
planning as inference the cognition is
about
action selection but then one piece that
differs potentially
is an active inference relative to just
sort of
the um way that control theory is often
discussed
is the insight of perceptual control
theory
which is that the planning as inference
is being done
in service of the expected observations
and so we're planning and acting in
order to control our perceptions
and that's happening as part of this
integrated loop
so it's kind of cool that there's like
this like good regulator
theorem in terms of cybernetics and then
it is like there actually is an emulated
regulator agent and then um
yeah pretty cool where does that
play in with like art thought does that
i don't know
what does that relate to our actual
experience of thought or does this
happen
all at the sub personal scale
well i mean how i knew it it's really
like a problem of
separating different time skills and
certain uncertainty associated with
different time skills
uh what you can do now and for example
in the next
couple of seconds is very different from
what you can do in the next couple of
months
and potentially your long-term goals and
plans have an impact on what you're
doing currently
uh and there needs to be a way how to
resolve this
uncertainty on different levels of
representation
and right from active inference
what one's solution for that is just
like you stack
agents on top of each other which just
representing increasingly
longer time skills
interesting um so it and i mean
as each agent i mean we can see it right
as a little
as a something which is separated from
an environment through the marker
blanket so basically through the actions
and the observations it's making
i mean you can also separate your brain
in multiple
nested blankets right where one part of
the brain just informs and
sends information to other parts and
accepts signals as
actions right so uh and
i mean we know this from experimental
research a lot of this is here are he
constructed so
all both in like temporal and like
spatial hierarchies
thanks dimitri stephen and then anyone
else
yeah would i be correct in between
perception and planning you've
kind of got this more conscious belief
awareness
being sort of available and and the
prior beliefs
once you get from around the
observations to perceptions
might be below consciousness in the
sense that it might be part of the
visual system or whatever
and i was just wondering how you see
that transition
from you know below
awareness to phenomenological
consciousness
uh playing out with the types of models
i know sometimes
like ryan smith uses some semi-markovian
processes which
start with some um
you know self-reports about beliefs so
it's working at a level which is
kind of building on top of the dynamics
that might be going on
in the kind of biology so i was just
wondering how you see those
different dynamics playing out and where
you fit your models with some other
models if they were sort of to play
play with each other
um if i may say so i think this relates
back to dimity's
um statement about the hierarchy of time
scales
because um obviously if it's like my
conscious
thought is on a slower time scale for
example than my visual perception is
and i think the
yeah my conscious thought is maybe
rather responsible for the slower time
scales
where it helps me to narrate through
the slow markov decision process
whereas it would be not useful if i have
to
critically think about any inference i
make on my retinal image for example
it's interesting you said there that the
conscious thought
it narrates because first off we've
talked about narrative
and active inference but also just like
you described how there was this hidden
state
of which flat i'm in and then that sets
the transition probability of the rooms
maybe you have a narrative that sets up
like
which policies you're transitioning
between like in
baseball you know there's a story to the
alternation of the innings and then it's
like okay we're going to be enacting
this policy because we're in this
phase and so there's like a higher level
narrative that helps connect
when policy transitions might
be um plausible to be
adaptive and then that is almost by
definition at a slower time scale
than the play-by-play because the
play-by-play is going to be a lot more
like motor control
the icicating and then as you slow down
you get slower transition dynamics
that are more and more narrative in
nature because they narrate like
different
phases of action but then the sub
actions are very rapid
i mean in a sense it does have to do
with a level of abstraction right if i
see a leaf
it's just a leaf it has a very concrete
meaning
in terms of my physical environment
whereas
my study program for example
um is something a lot more abstract
that is a lot harder to grasp without
abstract states that you maybe need a
narrative
for more
um ryan and then anyone else
oh i mean i was just gonna say i mean
you know like when we went through
mine and chris's paper on consciousness
a couple months ago or whatever
i mean the this question about how
conscious our conscious processes
relate to active inference really any
related kind of computational model is
is a complicated one
in part because what consciousness what
the word consciousness is used to mean
can be different
in different contexts you know i don't
personally
think that um yeah i mean
the question of what processes are
conscious or unconscious in and of
themselves
doesn't really fall out directly from
active inference right all we're doing
is modeling things at different time
scales and their relationships to one
another
um you know i mean in in the model of
you know uh visual consciousness uh you
know in that paper that we published a
few months ago
um you know the idea was very similar to
what other people were saying
you know which is this idea about
different time scales um
but but here i mean the idea the idea
was something more like
you have a particular level in a
hierarchy that
operates over a sufficiently long time
scale that you can do the kind of
goal-directed things that consciousness
allows including generating verbal
reports which themselves are very kind
of extended
um you know integrative policies um
but that um you know but that also
requires that it integrates information
from enough different low-level sources
right to do that um but beyond that
you know talking about consciousness as
itself the slower time scale process can
also i think be a little bit
um sort of subtle because
what a lot of people mean by
consciousness um
you know has to do with the kind of
subjective character of the kind of like
moments moment
you know phenomenological aspects of
experience and that's clearly not
happening on a slow time scale
right like the those the
moment-to-moment changes in
conscious perceptual experience are fast
um you know so what what we're doing in
this kind of higher
narrative level that i think you're
talking about is something about
you know integrating evidence for those
over time and you know using them to
come up with
um you know certain sorts of longer time
skill policies
to adverse certain sorts of longer term
skill policies um
and you know so the way that you know
we've talked about it previously is just
that
you know you have you can have these
sort of depending on the
precision of the interactions between
the first and the second level
uh in a model um if that precision is
low then the lower level can
um to a certain extent just kind of
operate semi-autonomously
in which case the higher level doesn't
really need to have all that much
influence or know that much about
right what's going on at the lower level
um so you probably have as a kind of
selection process
where the precision gets turned up or
down um
at different times and for different
hidden states um so the second level can
kind of selectively become aware of and
start integrating
evidence with respect to certain lower
level processes
which simultaneously allows this kind of
top-down control
over those first level processes um you
know so
so with the perceptual phenomenology
stuff it's probably more about
um the moment-to-moment updates between
lower level perceptual processes
and these higher levels or timescale
processes when the precision is
sufficient
for those updates to the second level to
matter but anyway i mean that's
more long-winded than i meant it to be
but mainly just trying to point out that
it's
it's subtle and it means a lot and it
depends a lot on what you mean by
consciousness
and it's not specific to active
inference necessarily
nice great i i think i mean the
difficulty when talking about
consciousness is
i don't i mean we don't know what is
what it is doing right
what kind of problem is consciousness
solving
what would be like a hyper-intelligent
uh
organism without the conscious
consciousness yeah i mean i think there
are definitely there are definitely a
number of ideas in the literature it's
not
you know it's not like it's completely
pinned down right i mean like
there are there are things for instance
like requiring
um working memory maintenance right like
like extended working memory maintenance
beyond a specific time scale
looks like it can't happen unconsciously
at least in current experiments
um any kind of like multi-step um
mental processes like for instance like
um you can get unconscious priming
effects where people can do something
like two plus two
um but you can't them but they can't
unconsciously do
two plus two minus four um right so
anything that requires holding this kind
of intermediate result
in mind um to do a further operation on
it is something that at least thus far
nobody's able to
do an experiment to um you know that
people can do that
unconsciously um there's um
but you know what ryan would you think
that consciousness is like a zero one
state i mean
from that respect right i mean right for
example giulio tanoni right
kind of sees this as a continuum like
consciousness
is really a continuum of states where
you can just have higher levels and
lower levels of consciousness
well so so again i mean this gets back
to what
what you're using consciousness to mean
right so in consciousness research
there's a distinction between levels of
consciousness
and content of consciousness um now like
content of consciousness is
i think most people agree it's fairly
binary
i'm actually not totally sure what the
um
um what the iit crowd would
say i'd have to kind of look back at um
look back at some of the more recent
stuff there
but but um in terms of neuroscience you
know it's it's
it's very well characterized we're
called like ignition events
that are that are non-linear all or none
you know sorts of processes where if
something becomes conscious you get this
global non-linear just kind of
broad uh activation widely across
large-scale networks
whereas if you don't get it you don't
pass this like ignition threshold then
you still get the local
like perceptual like local activation in
let's say visual cortex provision
or whatever sensory cortex um but you
don't
get but it's just kind of linear and it
doesn't
kind of percolate up or pass this
threshold to cause this large scale kind
of
more all or not kind of thing where that
where the information becomes kind of
broadly accessible throughout the rest
of the system
um so that that aspect i think has a
fairly binary character to it
um that's different than this kind of
levels of consciousness
and issue which is something kind of
like the
being in a predisposition to represent
conscious contents
um which would kind of be like a
continuum from say like coma
to like alert awareness um and that that
probably just has to do with kind of
like the state of cortical processing
that
um allows for uh
the the kind of dynamics that support
this kind of all or none
um the the stuff that allows for
selective contents
um but anyway i mean all this is going
pretty far afield from
from uh active inference in your guys's
paper now so
i don't want to uh go to the tractor
delay
it's fun stuff and it's important so um
we'll go to a more applied
question and then following this kind of
round on an applied question
we're going to go into a few code
walk slash talk throughs as well as
learn a little bit about a few
approximations and some of other work by
sarah
so lars asked us a question on twitter
which
anyone is always welcome to do and wrote
i would love to hear any thoughts on how
this
work on the multi-armed bandit might be
related to real world problem spaces or
applications
how might active improvements in
multi-armed bandit tasks
translate to improving how some problems
or
decisions are currently solved we talked
a little bit about
this in dot zero and dot one but i'll
go to any of the authors for a first
take and then everyone else is welcome
to give any thoughts or like ask a
follow-up
question so when you present the work
and somebody just goes to this kind of
obvious applied active inference
question
what is your thought
well i mean as i said right multi-arm
bandits are applied to
a super wide range of real world
applications
so i opened a survey like a survey on
practical applications of multi-arm
bandits and contextual bandits
one bone f and irish
irina rich and jalal bonifo right uh
so this is like one of the recent
surveys i found 2019
on archive uh and they hear the list for
example couple of
domains where they are applied
healthcare finance dynamic pricing
recommender system
maximi maximization
dialog system telecommunications anomaly
detection and
i mean just by looking from that like i
would
first try things out with active
inference based bandits in
kind of non-stationary problems
and this is from what i see dynamic
pricing and your commander system they
are kind of
in this domain quite obviously
uh but one can also imagine that right
uh telecommunication systems would also
be a non-stationary problem and as kind
of
searching for the fastest routing path
and similar
uh where different routes can change
over time and then you have
constantly ready to explore different
channels
for for passing along the information
more optimally and right this is a kind
of
uh practical uh
uh domains where one could first try
uh multi uh active inference based
bandits
um in as i study non-stationary kind of
problems
which is most of the other things i
listed um this is a bit more difficult
but
first to see if there is a way to deal
with um
this kind of uh asymptotic bad
asymptotic behavior
basically over optimistic uh
information search
awesome sarah any thoughts on that or
anyone else
stephen yeah could you just repeat that
last bit this
you said something about isotropic
behavior or some sort of type of
behavior i didn't quite catch
asymptotic right so this is like in in
stationary
bandits people are interested in the
asymptotic behavior after like infinite
many
actions so to say uh and how the
how different algorithms scale there
whether they converge to a good solution
or not
and i mean this is what we find in uh
right
in the stationary problems active
inferences uh too optimistic in a way
it converges to a solution too fast
as the way we define it at least
and and that that's why it doesn't have
good asymptotic behavior so if you would
apply to non stationary problem
when you would like with high
probability to find good solution
i mean active inference algorithm is not
one to go for
there
again we have some ideas how to change
this but
i mean just based on expected free
energy this is not something which
behaves nice nicely
so you almost have to do like a hack on
it to keep
bringing it back away from premature or
yeah exactly it kind of just gets stuck
prematurely into a
into a solution which the agent believes
it's a good one
and the reason for this one can see
immediately just from this
from the term which drives the
exploration which is this uh
[Music]
let's just expected information game
right in reinforcement learning this is
called like exploration bonus
or something like this and this this
doesn't increase with time
so in a way uh all these previous
algorithms like uh
upper confidence bound ucb uh the
reinforcement learning based algorithms
they have a bound which increases with
time so if you are not
sampling from one arm uh this bound
becomes bigger so your
algorithm is kind of forced to switch at
some point
uh and this is not happening here so
right
either one would need a different
generality model or a different way
to introduce more randomness into into
the behavior
one aspect of um it was uh figure
one or no this figure figure two in the
paper
was that that uh on the top left there
that the variance across active
inference agents was
increasing so it wasn't that like every
instance
was um slightly degrading in performance
it was actually that a small subset what
you wrote there
a small percentage of the ensemble did
not find the accurate solution
and were over confident in their
estimate so it
it does suggest a few ways in which
maybe you know when the variance of a
few parallel
instances of active inference starts
diverging that could be like a
a warning sign that some of them are
getting too confident too early and then
also it's interesting how you explored
that
um the learning rate um or
lambda through time and just kind of
said that
okay there's no simple answer here but
it's it's an area of future work for
sure
yeah i mean the problem with like
parallel runs in practical applications
you don't have that
uh how do you say um
that advantage is to keep in like
simulations i can just run
i mean any number of simulations just
see how it behaves right in practice
when you're solving the problem you just
have one trajectory and then you have to
kind of provide insurance that this
sample or this sequence of actions
will behave better than random or better
and that there is some probability to
converge over
over long over long run and this is
something which you don't get
right with uh
uh with active inference in stationary
problems at least right in
non-stationary we don't see this
uh issue anymore because of the
basically the generative model itself
because the more you are the less you're
exploring the more
your uncertainty rises on the arms which
you haven't observed
uh because the agent believes that
things will change
over time simply this is also what
helps it shift
between arms and it's also very
efficient to
kind of extract information from them
because
agent picks up really fast what what
kind of arms were not simple
and it's aligned with its beliefs
i wonder if this also might reflect the
difference between
optimizing the model for practical
application
in i don't know a computer simulation
program
and the way that organisms behave you
know it may be that
you know we we prematurely shut off and
let things become a habit
but that may have downsides you know
maybe that
you know organisms just to minimize use
of energy
prematurely converge on something
inaccurate and so
maybe that's like gambling than that
could it could show
a fragility at times so there's
maybe two ways that it's being applied
you know
yeah i mean i would say that organisms
are never exposed to a stationary
environment so
right i mean in a way if you are not
doing that you are suboptimal
because you are living in environment it
changes constantly
uh right so in a way you can exploit
this by now
creating situations where uh
well people behave weird and you have
gambling issues and stuff
but right um i don't think that's kind
of disadvantage for
well for what we evolved to do actually
uh for that we are very good in doing
finding good solutions reasonably fast
yeah sorry i was just i was just curious
i mean because
you know i mean this is something that
you know like with some of our like
empirical work we've run into
you know so like when trying to model uh
like change point detection tasks for
example
um using active inference where um yeah
like same thing like the thing becomes
too confident too quickly
um but i wondered i mean because i mean
in
in a lot of other empirical work like in
neuroscience especially like it's it's
pretty clear that people
don't just kind of learn and then
unlearn the like like reward
probabilities or just whatever the kind
of
environmental statistics are like when
there's like abrupt changes
right i mean what what people do is
instead they infer that there's some new
hidden
cause right there's some new light in
context and then
under that new context you basically
just have
really flat low you know really really
small
you know like magnitude concentration
parameters and then you just build up
right like your beliefs anew under that
new context
um and so there's there's like something
so there's like that kind of approach
which
either would require having some
something hierarchical or having some
kind of like
additional hidden state factor that
would correspond to contact
right and you know it seems like you
could do it either of those ways
um the um then the the other thing to do
would be to have some kind of
like in the hp like in the hierarchical
calcium filter where you have some kind
of uh
like dynamically adjusted learning rate
um
you know or or really something more
like um you know so in
like recently when we were updating um
some of this with our tutorial paper
um you know like after talking with carl
um
you know it seemed like it would be a
good idea to also include this kind of
like forgetting rate parameter as
opposed to just like the standard
learning rate parameter
which is just kind of like a scalar
parameter on the actual um
on the actual concentration parameters
right prior to
prior to adding on the new counts um you
know and so you could
that's not dynamic but but at least it
does um
prevent you know it can act as kind of
like a
something like an implicit prior
volatility that can prevent the thing
from becoming too confident too quickly
um but um but yeah i guess i just um
um i wondered if you know you guys had
like thought about or you know like
played around at all with with something
like that something like inferring
inferring new kind of like latent
context as opposed to just having to
kind of like
you know like the thing becoming too
confident and uh having to spend a bunch
of time over writing
right it's uh you know it's old it's old
beliefs which happens way too slow
i mean in the end um my current
model um is actually based on such a
hierarchical model as you describe
where my agent instead of unlearning
all action outcome contingencies it um
opens up a new context
of have you inferred that the context
changed
and i think um when we were looking for
proper learning algorithms for the paper
we most definitely looked in contextual
learning
and um i think yeah in the stationary
case
there are no contexts um
that's why we didn't introduce it there
and um
i think the uh smile algorithm we used
for the
non-stationary bandits also has a
forgetting rate
um just like you say for getting right
on the concentration parameters
which i think is another reason why this
algorithm
worked well in the non-stationary case
or better than in the stationary case
and in theory i think we also tried some
version of this where we have both
contacts and
getting parameters but yeah in the end
then
for the randomly moving bandits we had
also thought about then having another
layer
to this hierarchical model that
impersonal volatility
to adjust the learn uh the floating rate
and
if you start that your learning model
becomes
very abstract pretty quickly maybe but
overkill
but i guess i guess what i don't
completely understand still is
so even in the stationary case if uh if
you're getting rid of sufficiently high
i mean that all that's going to happen
is your the actual like
magnitudes of your concentration
parameters are never going to build up
to too high of a value right
so like does that not still help with
the overconfidence issue
i just would have thought it would uh
well we don't have a per kind of
forgetting parameter in non-stationary
case
at least this shuts off because uh
well assume agent believes it's in a
stationary environment
yeah i got a reasonable you could still
put an agent in a stationary environment
but it seems like it could be plausible
that it
has a kind of yeah
right so yeah i agree i mean that's one
way one could
try out right to resolve the
uh exploration problem mean stationary
case right just simply
uh giving agent to the wrong beliefs so
that
things will continue
just tell this we use the same
learning the same bayesian belief
updating algorithm for all the different
action selection methods that
we compared and then it's a weird
interplay between
the learning model that we chose for the
stationary case
and the action selection rule and i mean
thompson sandling which
uses the same learning does not have
this issue
yeah and that i think is also
interesting
so to the second part of the question
where how would that translate to
improving how some problems our
decisions are currently solved
i'm hearing a few things we talked about
speeding up
computation relative to other approaches
but that's not a solved problem for
example if there's a 10 times speed up
but then you have to run 10 agents in
parallel to get a good
ensemble estimate then it's a wash so
potentially for speeding up just the
computational requirements
for certain challenges a second would be
that it might be possible to more
rapidly lock in
to dynamically changing regimes and to
avoid some of the pathologies
of model fitting in
multi-armed bandit contexts and then a
third
way that it could translate to
improvements would be it might reveal
some hidden similarities between these
different problems and settings
like we already know that they're
somewhat similar because we can apply a
multi-arm bandit to
you know health finance recommendation
systems etc so we know that there's a
lot of problems
involving data that have similar enough
structures such that a
similar kind of general algorithm can be
applied but then it could be interesting
once we have them on the common
grounding of active inference
to say actually you know the structure
of the decision making
is similar across these two settings or
you know the telecommunications routing
and the logistics routing are similar in
this unexpected way
so maybe insights relating to what kinds
of tweaks
an agent uh could improve on their
performance with
like what we're talking about here with
the category categorical
hidden states or learning and forgetting
tweaks maybe some of those insights
could be
implemented in active inference and then
more easily transferred across different
domains
so hope that conveyed some of our um
uh thoughts on this question to lars and
anyone else
yeah yes i mean one issue there is just
that
in different domains you will in
principle have different generality
models right i mean
although the problem is the same
multi-unbended i mean you would need
different representation of the
environment and this is then where the
challenge comes
potentially uh as
if you can represent it as a
multi-embedded problem you can
uh choose different whatever action
selection
algorithm you find works best and in
non-stationary situation
at least from for what we investigated
this seems to work well this doesn't
mean necessarily that this generalizes
one will still have to try out different
things just to make sure
but in the end the bigger challenge is
like okay what is a good generative
model for
this dynamic problem which i have
one can go there right with many
different things so i mean for example
what
uh ryan also mentioned this kind of
uh open-ended contextual learning i mean
one can represent simple in
in the environments where you don't know
anything about what
what's going on you can just do a
non-parametric generative model like
dirichlet process or gaussian process
you just try to learn even what the
model itself should be
[Music]
awesome so let's go
to this little sub discussion
on sarah one of your previous papers and
then we're gonna turn
to some notebooks and walkthroughs of
the
bandit project but hopefully this will
be informative because
first off belief propagation and message
passing and these types of
approximations are of interest
to the lab in the community and also
we're
seeing a few faces that we can ascend
active inference mountain on
we have ryan with a matrix based matlab
approach we will walk through in just a
few minutes
with a python based approach of the
bandit and then this is a slightly
different approach
based upon the beth approximation
so sarah anything you'd like to
describe i'm sure this will be new to
many people so it will be helpful to
convey what you were working on here
sure so in figure 2 the upper one what
you see
is the generative model of a normal
observable markov decision process
where the um in the upper row
the unfilled circuits are the hidden
states sorry they were called as
in the previous slide and below are the
observations
and then the whole um the dynamics of
which states follow upon each other
is determined by the policy pi on the
left side
and then what
people often do is assume in this
queue that we saw two slides before
um the mean sheet approximation which
means
exactly which means that
um for example here we have a bunch of
hidden states
h t h t plus one and so on
and then if you assume the mean field
approximation
um the approximate belief distribution
would be just
q of h t times q of
h t plus one times and so on and so
forth
and there with you create an implicitly
yeah you essentially treat all the
hidden states
as independent in your approximate
beliefs
and then their dependencies will be
averaged out
in figure 3 you actually see the
inverted model and in with
m you see the messages that are being
passed in between
notes so if you it doesn't matter what
approximation you use in the end you can
calculate your beliefs
with some sort of message passing
algorithm
except that now if you chose a mean
field approximation
and you estimate all hidden sets
separately
what we found is that actually they may
not fit very well to each other so for
example
when my agent predicted um how it will
go through the
grid under a certain policy it actually
often predicted
it will jump and go places that don't
adhere
to say transitions
and there is of course leading to
decreased
goal reaching success
and then instead of doing this mean fit
approximation
we assume the beta approximation
which instead of having qht times q
h t plus 1 and so on you have
small pairs of joint distributions so
q of h t and h t plus 1
times q of h t plus 1
and h t plus 2. and then doing the math
you can show that
if you assume this type of approximation
and you plug it into the free energy you
want to minimize the free energy
the belief propagation method path
passing algorithm comes out
and so you can use the belief
propagation and message passing
algorithm
under the beta approximation
to calculate beliefs and this is
actually exact on
graphs with our loops
and then you get a more appropriate
joint representation
or in this case of temporarily dependent
hidden variables
but i mean in the end yeah what i do
nowadays that i also
have a hierarchical model where now for
example the parameters of the markov
decision process are context
dependent i look into my model and think
which variables belong together and then
i apply the
mean the bit approximation in these
parts
but then some slower varying variables
like the
context i just use an infinite
approximation because it
it varies differently anyways
thanks for that breakdown um
what is message passing like who are the
messages being passed between
and does that reflect a variant
on active inference or is it
the same exact active inference model
can be
approximated or can be calculated
through message passing or through other
mechanisms
uh correct me if i'm wrong dimitri but i
think in the end all active influence
agents do message passing
depends on the approximation which type
of message passing algorithm
so um yeah another the better
approximation it's
belief propagation propagation message
passing i think there are equivalences
for the
sum product algorithm also you just get
different messages
that may be better or worse but okay
what are the messages
essentially each node in the graph so
each hidden variable
sends other hidden variables that it's
connected to
a message about which state it should be
in so
ht would say hey we're currently here
then i think in the next state we should
be there
and then vice versa uh ht plus one can
send a message back that says
hey we wanna be there next time sir
where should we be now and so
yeah these variables essentially send
each other messages on what they should
be
so that they are in agreement with each
other that's how you
get essentially a probability
distribution over what you think
your which state you're in
and will be in yet dimitri any
thoughts on message passing or where do
you see message passing fitting into
bayesian statistics and a few other
topics
well i mean as sarah said mo i mean they
would say all the algorithms are message
passing
so when you talk about mean field
approximation this would be
traditionally variational message
passing it's called the algorithm right
uh here uh this is like belief
propagation
it's a message passing algorithm based
on
uh marginal probabilities uh
instead of in the variational message
passing you have like uh
expectations of the log of conditional
probabilities right i mean this is these
are kind of the differences
uh what you're what you're getting and
losing
and i mean we have another paper with
thomas parr
and carl neuronal message passing using
mean field beta and marginal
approximations
where we kind of contrast these
different ways so who is interested in
this topic can
uh look into a bit unpacked discussion
of similarities and differences
in practice the difficulty with mean
field approximation it's
i mean for dynamical problems for
numerical decision making it's not
really a good approximation this is not
something
which one would use and
implementation wise in inactive
inference mean field approximation is
not used on the dynamical level
uh what what they're using in matlab for
example is all this marginal
approximation it's still kind of
gradient-based method but
it's computed slightly differently so
uh yeah sorry uh
well i just wanted to kind of wrap up is
basically the more complex
problem it is the more uncertainties you
have on the state transitions
the more difficult you would
difficulties you will have it mean field
and marginal approximation basically the
bt approximation is the only thing which
kind of
uh corresponds to actually exact
inference in the
in non-cyclic graph so basically this is
uh this is
theoretical solution you know that you
can be exact
under specific conditions
on the marginal um a yes
i can only warmly recommend by adida and
vice i think in 2001
called understanding belief propagation
and its generalizations
and i find it very didactic it hurt me a
lot and they explain
in detail how uh variational inference
is also connected to
message passing algorithms
interesting so just to capture that one
interesting
thing you said there about the gradients
the gradient it's sort of like your
model is in a given spot
on the landscape and then it checks the
temperature and it goes
in the direction of the gradient so
we've talked a lot about gradient based
methods with the straight line versus
the iso contour
message passing kind of breaks that down
into a process so at each click of the
model
messages are being passed back and forth
to one another
which is both computationally tractable
uh it's also shown through some work of
uh
the bias lab uh burt devries and others
that four specific categories of
bayesian graphs
that message passing algorithms are
basically equivalent in the forney
factor graphs the ffg
which we're going to be learning about
in the future and also
this topologically puts you more
into touch with the predictive
processing
for example the messages that neurons
are passing to each other
so it's one thing to say well it's as if
the neurons
are messaging to each other and that's
doing a gradient descent
but it's another thing to actually
saying we have a message passing scheme
for modeling how these message passing
agents
do inference so there's a few
points of contact there that i think are
pretty important and it's pretty
it's also interesting that you brought
up that early paper
so it's we'll check that one out stephen
did do you have a question
i think it's been sort of covered really
it's
cool area though so thanks sarah for um
sharing that just one last question on
this before we go to the bandit codes
and walk through like
where do these approaches um
are they converging and they're going to
weave together
more closely or is one of them
like an umbrella over the other such
that work will continue mainly
under the generalized form where do
these different approaches that we're
talking about to implementing active
inference where are they heading
like is it is more development happening
on the message passing
approximation or on other
modes of breaking down active inference
i'm not sure i have the overview of
hundreds of papers
publish every month and that's active
influence to say something like
about uh
as far as i mean our motivation is here
we just want to have in different
situation good enough
inference approximations so
in a way for me more important question
is like what is a good representation of
different tasks and environments to have
rather than
what is the best kind of inference
algorithm to use
uh because especially if
i mean depending again on the
environment you're working on and but in
dynamic context it's
uh difficult to get like
lots of advantage with just improving
slightly on the
inference performance great
just because there's lots of uncertainty
in things and anyway change
all the time so um
yeah i mean with this we also kind of
write for for this multi-unbanded paper
we tested very
lots of different algorithms uh there is
kind of one of the notebooks in
repository just kind of lists different
things we tried out
but in the end one doesn't see you i
mean
any reason why one algorithm would be
specifically
a way is better than another it's just
they're very similar uh
subtle subtle differences great
point that there's a lot of work on the
comparability of different
approximations and different algorithms
but actually it might be more beneficial
for
a given application to focus more on how
they're specifying the generative model
and making sure that that really
captures essential features of the
environment
because it's like okay let's just roll
with active inference
and spend our attention on the
generative process and the generative
model
rather than try to finesse potentially a
a grossly
inferior generative model with some
better approximation
there might be limited returns there so
stephen and then we'll
go to looking at some of the bandit code
yeah this is a kind of general question
related to that
is i often think about
sort of didactic deontique type
sort of um ways of making inference
um this sort of deductive thinking and
such like
and i'm wondering whether the message
passing is is is more
present in those types of models because
it's it's something that's been detected
in the environment
and decisions based on that are being
made
and you've got then you've got your kind
of inductive where you're trying to
narrow the gap
between a goal and then you've got your
abductive where you're trying to build
something up
and infer from like a landscape
that you're trying to work out what what
is out there so to speak
and i'm wondering if this
is correct in my thinking that the
message passing is more
used when you have like a particular
deductive reasoning approach and
ad inductive or abducted ones would be
different interesting question about
how those different modes and types of
logic
are connected to message passing
one thought which might be on or off
base
is that we're thinking a lot about how
variables in a model are like nodes
and then there's edges connecting the
nodes that reflect
the relationship between those variables
and
message passing is just one way to
describe
as a model updates through time which
information is being passed between the
variables
so it doesn't say anything about the
mode of operation of an agent
which might be engaging in different
kinds of logics and i think that's
in really excellent question like how
how do we um break out of
the known with respect to how our
algorithms update
and it does actually touch upon this
mean field approximation
for example if you think that all
through all time past present future
that there's some stationarity of the
hidden state
then the mean field approximation will
work
but then if there's going to be a change
in
the state then the mean field
approximation
is potentially going to give a
misleading outcome
but in any case message passing is just
describing sort of the
mechanics of how the model updates and
which information between
variables is connected but importantly
which variables are not connected
like the observation at a time point
doesn't influence the observation at a
different
time point directly but it could via
a specified path of message passing
let's look a little bit at the bandit
code um so the the links to the
github dye markov
you have the right name to work in the
area
[Music]
um so we have a few of these notebooks
up
and uh is there we can look at the
overall notebooks folder or do you have
a sense of
which of the notebooks might be
interesting to
walk the record go to a few or if you
want to jump to a first one
i think just this first one think about
this maybe
oh go ahead uh
yeah there are a couple of things i mean
a couple of notebooks which are not
immediately relevant for the paper
so which we can focus just on the things
uh
which are part of the paper or i can
just generally kind of
talk also about these other things which
are just process of thinking about the
problem
okay how about before we even how do you
as a researcher working on this area
keep that separate like the paper
specific developments but then your
overall
developments do you find that you're on
an overall development
mood and then you dip into specifying a
paper or do you pursue the paper
and find that you have more general
insights while you're working through
the problems
well i mean i pursued the paper but i
mean then
i mean there are lots of branching pads
on that way in a way
you have to figure out uh what's
potentially interesting what's relevant
and so part of this code is just
exploration a bit of things
topics which were interesting for me but
which turned out not to be so
important in the end just
maybe for some other paper uh and
things which are just focusing exactly
on the
comparison of multi-arm-banded
algorithms and
right uh discussing this part uh
so in a way it's difficult to
combine lots of potentially unrelated
things into one paper so
one always has to make some favorites in
the end
i knew it would be a a both type of
question because it's something that
researchers are often
you know interested in general questions
but we need to deliver on specific
research projects with a defined scope
and conclusions
as well so it's just cool to see that
this repository holds a little bit of
both
so so for example this uh notebook which
you opened first like
expected free energy comparison this was
just my contemplation of just
different ways you can define expected
free energy
so typically people will think about
expected free energy in this terms of
expectations of their outcomes
but for example another question is okay
but why not
why not computing in terms of
expectations over states
and there is the relation between these
two right uh one is an upper bound on
another so
basically you see this last relation
there is
s of pi there is g of pi and there is i
of pi
uh and um basically g of pi would be
expected free energy in terms of
expectations over latin states
so this first and this is upper bound on
what this would be like expected
surprise for me
uh in equivalence to the free energy
being the bound on marginal
surprise like log likelihood or
surprising uh
and then there is the i of pi which is
just kl divergence between
posterior prior which gives you then
something else
and anyone can also think well we can
select policies or make decision-making
algorithm based on any of
on these quantities and what happens
when you use one or over another
so this is something which uh i was just
testing out
for myself uh and
i'm still not clear what to think about
this so that's why
i don't have a paper it this is very
interesting um it's like it's all
conditioned on policy with pi
and then we're approaching it from the
top and from the bottom
and so the free energy is like being
sandwiched in between
these other approximations um and then
you wrote here that the minima of i and
g of pi
match but s is giving a different minima
so what what was curious about dot co no
at least in this example right uh so i
just kind of build up simple example and
one can see that optimal policy uh or
like minima of
these different quantities is different
and one can also think probably of
different examples well this will
i mean this relation will not hold
anything but what i just wrote as a
comment there
uh but i mean this is more like than
practical question
so if you would then build an agent
uh which one of these quantities should
you use they are all kind of effectively
can be seen as a right expat expectation
of a future
surprise uh and
having different bounds on that uh
expectation as an approximate
quantity uh so just the question is uh
and i also found in different uh
problems depending how i formulate
problem
one of these algorithms works well not
algorithms but
objective functions let's call them
works better so
all right
so in this particular multi-methods task
which we if
we explore the g of pi is not
so what should i mean what should
corresponding to expected free energy
this is not uh
behaving that well so in a way you don't
get
uh such a good performance but i can
slightly change the task
uh and i i can get better performance
with geophy or
sf5 so as i said i'm not sure what to
think about this still so
cool well it's really like exploration
of
different things we'll we'll have you
back on this
topic when you're in a different phase
do you want to look at inference
algorithms comparison
or is or well yeah so inference
algorithms as i said this notebook
and just list some of the things which
we consider right
in the literature when you think about
this um
well approximate difference problems in
changing environments one can think of
different ways how
to solve this uh what we used
here is the radius representation which
comes from change point models
as an approximation for the task which
is a good approximation for this kind of
kind of pitching bandits which is what
we
uh what you show our job showing here
right for example this is the question
blue had
last week also so this would be how
probability
changes in us in switching bandits
on one arm uh over time
right now probability of generating uh
one or let's call this a reward uh
this is what this plot is showing uh
and right and this is the switching
concept that after each
uh whenever switch occurs we are just
sampling the new probability for each
arm so this is this kind of uh setting
with
non-stationary uh uh difficulty right so
that basically this difference between
the best
arm and second best is it varies over
time
uh and then you have like a drifting
dynamic for which just like the
different generative approaches uh model
would also
be better uh
but then one can also say well we can
use any generative model for any of
these problems and let's just see
which does inference better are there
any differences there right
so can you just uh
use different representations in for
different underlying uh
environmental dynamics in a way miss
specified in the model but still
doing reasonably well in for the
inference part and
right when you kind of look at the
results kind of
posterior expectations you get over time
uh different approaches to lead to very
diff similar
results in the end so there is no kind
of strong
advantage or disadvantage of one or
another and that's that's the reason why
we just picked the simplest
thing which can the more most efficient
basically algorithm because then it's
much easier to scale to
more arms more time steps
[Music]
okay very interesting this is a
pretty thorough walk through the
hierarchical variational smile yeah
exactly
it just describes right the generative
model
some of the steps one needs to take to
get to the
posteriors uh they're also uh
then just implementation of the
algorithm is unpacked there
but beside this right what we used in
the paper we also
implemented some of other approaches
which are non-variational kind of asian
inference
uh which is seems to be quite good and i
mean right
on average it performs better it's like
more optimal
representation now this comes from i
think also recent paper and multi-armed
bandits
um do you remember sarah they'll first
start a louis at all maybe or
unfortunately
[Music]
written paper and one can see that it
does slightly
better job so that would be i guess this
algorithm you're
showing now yeah what are the
lines representing the red blue
green and then the sort of flat the
green is just for the ex posterior
expectation
or like reward probability so right the
perfect algorithm should just match
green with blue
and the red is basically a
change point inference so basic
posterior probability that the change
occurred at
this specific uh moment of time
uh and as you can see this process is
quite noisy in a way right you
you have lots of small errors in a way
or slight jumps in in places where
change didn't necessarily occur you know
what what this reminds me of is um
the blue is some hidden true price
of an asset and then the green
is like the markets tracking that
price or value and then the red are like
orders like buy and sell orders on the
market
that represents the underlying
situation changing and
it's like just uh maybe
well i mean markets yes ma'am i can see
markets is doing some kind of difference
on the true friend by value of the price
uh right this will be kind of
distributed inference problem
yep i mean it's the whole no one knows
the price of a pencil but maybe
the person making the eraser knows when
the price of rubber
changes a little bit but but their
colors are just the coincidence
okay and then here we see something
um yes here is this this is a if i
remember
correctly this would be the hierarchical
ocean filter applied to to the same
problem
so this is work from matisse christmas
so so
he actually in his first paper he he did
apply to
inferring the price of an asset over
time
uh so when he introduced that but but
it's
found lots of uh applications in the
cognitive neuroscience and just
uh understanding how people adjust to
volatile environments so there
so what we have here is that this kind
of change probability is constant over
time but
you can also think of the environment
the change probability itself changes
over time so that you you need to kind
of adjust
uh to these changes also uh
so that would be also quite one uh
straightforward extension of
this multi-arm banding problem like
different types of dynamics
and uh testing out then more complex
generality models and
approximations to deal with that problem
and so right we are just comparing now
how this algorithm
tracks the underlying price value in
different environments
so i i have a question about um what
action
does so here the underlying generative
process
is stochastic but the actions don't
change the process
like choosing a different slot machine
isn't changing the probability of slot
machines
so it's almost like a little bit more of
a niche
modification setting or
can it just um be directly put into the
model that
certain actions actually change aspects
of the underlying generative process
or is that kind of a feedback between
action and then future hidden states is
that like another module that has to be
constructed in
well for what we have implemented here
that would definitely need an extension
right
so we kind of this is more than this
general representation which
of uh also implementation of active
inference which for example is
implemented in spm which then helps you
deal with
uh these more extended problems
so here we really are working with the
uh simplest algorithm just for
having it like very efficient and
compact so that it can scale easily
uh what the more general you are and
trying to capture
many different problems the more
difficult to have with scaling
right uh it's it's like
inference all the way up or all the way
down and it's it's a theme that we'll
return to many times which is that
it's all good to track the absolute
value of what you're interested in but
then the uncertainty on that and then
the uncertainty
on your uncertainty about that can get
you into this
infinite recursion so you just do you go
quick and dirty
and just have a simple idea of how
variance and higher order
uncertainties propagate or does one
fully specify
all the possible ways that uncertainty
can exist across multiple levels which
can get
to an explosion of the computational
requirements really fast
well i don't think that necessarily
hierarchy is the issue
but it's more right if you then start
assuming that your actions
change the states
state changes uh or transition matrices
in this stuff right
so basically you're effective with
actions you're modifying the state
transition matrices
then this requires that i mean you also
think about the planning problem and
it's not any more simple um action
selection problem but it's
then becomes a planning problem uh
and this makes things more complicated
if you introduce such an environment
because then it depends where you are at
different moments of time in different
states
yes because we've seen in the markov
decision processes
that policy pi plugs into
b which is the transition matrix between
hidden states
and so that's like actions changing the
way in which
hidden states are inferred to change
through time
whereas the one-step decision making
is um doesn't have to be done in that
same uh
way but yeah
and i mean i think also i mean at least
original implementation in spm what is
used this doesn't scale also very well
for this type of problems and different
groups or people have
started exploring like monte carlo
research and other methods which
actually allow you to then
figure out potentially best policy in a
very complex
high dimensional problems
all right but but i mean as long as
you're kind of in domain of cognitive
behavior in neuroscience you can like
get away with this by just making your
task reasonably simple
you have this control so yes
but even as as ryan like pointed out
earlier that uh
real humans even when you control
the experiment or you think that you're
introducing like
a gradual change in a parameter they
might actually
be cognitively doing a different type of
inference yeah humans are problematic
i don't like them oh humans
we should do experiments with robots
well
maybe that will be the uh i mean we
brought up the conversation
of course logistics planning motor
behavior
exploration exploitation spatially those
are things where maybe
having a defined digital twin for some
robotics
and then we go from in silico to
robotics
to starting to introduce the element of
the human
and the unknown um
stephen
sorry i think i mean like but in in
behavioral experiments you always have
this problem of
uh just like convincing yourself that
the model you're using
is something which reasonably well
represents with humans
are doing and you can be quite certain
that this is not what they're doing
exactly right this is just another
approximation of all the complexity
which we kind of
uh have in well our non-parametric
representation of the world
uh right and i mean
kind of there's this issue right you can
kind of get people to perform very well
on the task through lots of training
but then it's like okay this really what
i want to kind of
test experimentally whether like how
can humans learn to do this task well or
i'm actually interested what people are
doing when they are solving any tasks
how they represent the environment
date the time representation how is this
incorporated in their decision
uh model so and
i i think it's i don't know how other
people feel maybe ryan
i can comment on this but for me it's
always like a difficulty to
to deal with it's like it always
certainly or whether you're doing the
right thing like
simply enforcing something on
some task on people
yes thank you stephen
yeah so talking about this the problem
with humans
but um is i'm interested in how the
precision parameter you talk about the
precision parameter and it helps
to sort of determine whether someone's
going to explore or exploit
the context i'm interested in how
exploration can become a pragmatic
uh this precision about the usefulness
of something that's exploratory i.e what
art
or an experience of some sort and how
that meaningfulness
in the future could offset a pragmatic
gain
in the near term so i i i'm interested
in this
the way that precision fits in with that
um and sort of the evolution of that and
they even talk about that a bit with the
um
charge with casper hess by affective
charge is
how your precision
about an expectation has been violated
or not you know it's not necessarily
whether it's good or bad
it's whether your your prediction of how
well you could expect something to
happen suddenly got violated and that
amplifies everything um so
i'm interested in that because i'm
trying to create immersive experiences
for
theater and places like that but i was
just wondering what your thoughts about
the precis
how that precision parameter fits in
with that dynamic and how that could be
extended or if there's other
other parameters that kind of can fit in
there as well
um i'm not
quite sure that i understand the
questions
but let's see the
are you asking like can is precision
always relevant
yeah can you stack the precision with
the pragmatic
if that makes sense so say you've got
low precision
but you have a high precision over the
fact
that exploring the low precision would
be useful
so the two things kind of stack on top
of each other
as being a sort of a pragmatic epistemic
game
i can see that being used yes so i mean
we in this other paper on meta control
we are playing with this a bit
differently so we are saying that uh
you can kind of control your exploration
tendencies
if you learn over time the exploration
is bad
and this is kind of where this kind of
stacking of different levels of the
hierarchy here like
a higher level kind of agent controlling
the lower level comes in play
all right because simply if this higher
level observes that over time
uh you're like the agent is not
performing well
in a way it's not reaching the goals
efficiently then it kind of punishes
exploration
and learns uh just to be more
exploitative
in this specific settings uh
and the other way around where we can
make kind of a setting where the
exploration is beneficial always and uh
right yeah and this is then the agent
learns to kind of behave in this way
better so one can like
then i mean assume in real situations
this is something which people learn
right so just if they observe that
depending on what they do they gain more
or less they will also adjust
their uh tendencies uh and associate
this with different contexts right
so you could have almost like it's not
just precision
you could have like another generative
model managing those
yeah exactly i mean you can just have
another kind of higher level
representation which controls
uh priors or precisions on the lower
level
so right and basically
inducing different behaviors through
that
to connect that to the um ostensive cues
it's almost like if you had a a sound
or a cue that said okay now we're in a
brainstorming
period okay now we're gonna drill down
and by alternating between a
brainstorming period
and by drilling down we're going to have
the right kind of outcomes but giving a
cue
for when one should be in a more
exploratory
mode versus potentially like more
working with what is already known
but this looks like an interesting paper
this meta control of exploration
exploitation dilemma
and also framing it in terms of the
hierarchy of time scales whereas often
it's framed in terms of um
i guess just instantaneously what
maneuver would be best whether one is
instantly
preferring exploration or exploitation
rather
than uh through deep time
the interaction with reviewers during
that paper is what motivated these
papers
so that's that's like sticking like okay
i
really need something to just explain uh
unpack some of these similarities and
differences between
active inference and everything else
around
[Music]
nice um well if there's any other
sort of closing thoughts this has been
an awesome
set of discussions i think we'll have a
lot to think about and hopefully people
will work through these
notebooks keep an eye out for when the
final
paper is uh published with so
you got this one fully published
while the multi-armed abandoned is is
still not
ready it's still under review yeah
we are finished yeah hopefully soon
cool it's a first revision around
currently
well to anyone who's on here any other
thoughts or questions or what do we take
moving forward
i'm just thinking about different tabs i
could be
having a regime of attention on as the
multi-arm bandit you know
do i check something i haven't checked
in a while because i'm uncertain
or should i pull back to my higher level
and be like you know what it doesn't
even matter if i'm uncertain about
that tab i should just stick on this
one
i'm sure there'll be some fun um yeah
dimitri
well i mean it's a very general problem
as i said so
most of the problems are multi are
invented
it's not surprising right awesome well
sarah and dimitri thanks so much it's
great to have your like
engagement from the 1.0 on through it
really
made it awesome for the lab so thanks
everyone for
watching and until next time thank you
for having us here yeah thank you
yep yeah thanks very much until next
time bye bye bye
