---
title: "ActInf ModelStream #001.4: "A Step-by-Step Tutorial on Active Inference""
category: "ModelStream"
series: "ModelStream_001"
episode: "4"
duration: "2:27:21"
url: "https://www.youtube.com/watch?v=QRGaGmT-VFM"
views: 635
exported_at: "2026-02-18T22:37:37.796096+00:00"
format: markdown
---

# ActInf ModelStream #001.4: "A Step-by-Step Tutorial on Active Inference"

foreign
okay i think we're live okay yes the
screen was blocked out for a second but
hello everyone
welcome to the active inference lab this
is february
5th 2021 and we are here in
model stream 4.0 with ryan smith and
christopher white
i'm daniel friedman i'm a postdoctoral
researcher
in california and a participant in
active inference lab
maybe the two of you can just briefly
reintroduce yourself
um yes for anybody who hasn't you know
been watching the previous
sessions i'm ryan smith i'm a
investigator at the
laureate institute for brain research in
tulsa oklahoma
yeah hi i'm christopher white i'm a phd
student at the mrc cognition brain
sciences unit in cambridge england
awesome well we are here today in part
four
which will be the last section on this
paper hopefully not the last time we
get to speak together on any stream but
it's part four of four
on this paper a step-by-step tutorial on
active inference and its application to
empirical data you can find the link to
the most updated version of that
resource
in the video descriptions and as far as
points of process if you have any
questions or
comments or thoughts during the live
stream you can type it into the live
chat
and we'll address it when the time is
right if you have questions arising
after this live stream or you're
watching it after it's occurred
feel free to leave a comment and we'll
try to address it in future
sessions because the model stream never
ends so to learn and participate
and learn about how to participate go to
activeinference.org
that's where you'll find more
information on active inference lab
so today in our fourth session it's
going to be pretty exciting because
we've covered a lot of the groundwork
and
daniel are you crying ryan yeah you're
we're not hearing anything daniel
oh um
give me one sec okay do you hear me now
no yeah yeah you you froze
all right give me a second
it's all good this is how it happens
sometimes when
live streaming let me go back to the
event
and i will rejoin the event
all right
cool waiting this is just how it is
welcome to live streaming everyone
cool look at that ghost daniel friedman
he can be kicked out you're really quiet
again okay okay okay yes
device settings
okay yes thanks microsoft
teams for facilitating these
conversations
i it's still live and happening it's
just a little
a little hiccup with teams that now
we've gotten that out of the way
so it's fixed but thanks ryan and i
don't know if this other person can be
kicked out
but take it away we're all good though
thank you
okay uh maybe um
which one are you the ghost of daniel's
past
it's okay it will auto drop them um
like after you share and unshare but
it's all chill okay okay
perfect okay
i think that that worked okay so we are
still
we are still alive and going yep okay
all right so uh so i should just start
or is there anything else you were kind
of in the middle of saying something
just um if we could start with some
recap for those who probably have seen
the first three
sessions just where did we get to as of
today and then where does that take us
into the future
um okay so yeah just as a quick
recap um as daniel said the the kind of
whole purpose
of this tutorial that we
put out was to try to make methods for
actually building active inference
models
and applying them to experimental data
we wanted to try to make those methods
more accessible to a broader audience
um because up until now it's been fairly
difficult
to find sort of clear resources for
beginners
to start learning these sorts of methods
and so
the whole kind of the whole you know
point of what we've covered so far has
kind of been building to this section
um if the focus again is on b
being able to actually use these models
for experiments
so obviously the earlier sections could
be useful on their own if you want to do
simulation work and there's lots of
papers
reporting simulation work but in terms
of
then applying the models and simulation
work that you do
to um to actual experiments to actually
fit it to
um task behavior with participants and
you know
predict things about like neural
responses and fmri studies and all that
kind of stuff
then it all kind of boils down to what
we'll talk about today
um so in earlier sections we kind of
covered the basics of active inference
you know what free energy
what variational free energy is what
expected free energy is
what the motivation is for doing active
inference what the
potential benefits are over
traditional reinforcement learning
models um you know things
things like things like that just kind
of the nuts and bolts and then we
covered how to
build um active inference partially
observable markup decision process
models um and um as an example
um we built a um a simple kind of
explore exploit model
which i will uh or exploit what task
model should i say
as a just kind of a concrete example of
how you would build a model
um and we showed some simulations both
for
perception and decision making and for
learning um
with that model um and so
and then we also kind of um uh
took a took a break from that we're
going to return to that now but we also
took a break from that a little bit
to um cover um hierarchical models
and the neural process theory um
but now we're going to come back to
using the explore exploit task model
because it's
um simpler and more straightforward in
terms of
what you do with participant behavior
and and how you fit it
um so so all that like i said is
building up to
using the task model we built as an
example for
fitting it to data um so christopher i
don't know
yeah great summary christopher what
would be your perspective or what was
something that stood out to you
from the previous sessions yep because
you're
you're so both deep in the game and
actually producing
this artifact that it's been fun for us
and for the audience just to be
kind of talking through it because it so
what what does it
leave upon somebody who's been involved
in the generation of this artifact
now to be talking about
interesting question i suppose um
i thought i think it has made and i'm
just so this is kind of in
for context i have i started my phd four
months ago
so this is all kind of in the context of
figuring out
not just how to build these models kind
of for myself
um or sorry how to teach other people
how to build these models rather
but actually how to build these models
for myself and apply my own research
questions
um and so i actually have never fitted
them to data
all of the stuff that i've done so far
has been theory
essentially just i've done a lot of
simulation work but no um
no data fitting so
i don't know i think that's actually the
the frontier in active inference at the
moment is actually figuring out how to
get these models to hit the road
um and there's a really one one really
tricky thing is most the people who work
on active inference
in a real way are neuro images
so i for i for example i'm in your
imaging department
um i know ryan you work in your imaging
as well
um it's actually challenging to test
these models in the domain of
neuroimaging
neuroimaging is really hard um actually
i think many of the clearest predictions
actually in terms of neural process
theory are actually things that you
could test
really quite easily with optogenetics
not optogenetics or anything like that's
easy
but say predictions about micro
circuitry in pfc
which active inference certainly makes
um
can very much be tested easily in
a rodent model but it's really difficult
to test it in
a human and so i think
the point that i'm trying to in a rather
rambling way get to
is i think we need to think very deeply
about when we build models
about what it actually is that we're
trying to solve do we just want a
directional hypothesis
in which case you don't necessarily need
to fit these things to data
you're just saying a's b a will be
bigger than b which is still better than
most psychology
let's let's be honest um
yeah it's it's really interesting the
neuroimaging case
has a few specific difficulties massive
amounts of data
in a system that has massively complex
internal
and external dynamics like the brain and
you're making a ton of data with a very
complex error profile and in the spm
textbook
it's chapters and chapters of
normalization and re-warping and all
these different kinds of ways to deal
with these very complex data sets
and now we've almost built out that
framework and now just like you said
where it's hitting the road
is in being applied to empirical data
and it's a little bit of a surprise
at least to me and probably others that
maybe neuro imaging although that's the
home
of spm we're seeing it applies to
systems beyond
neuroimaging and even there's other
systems that help inform
our neuro imaging quest so pretty
interesting stuff
um okay so should we just get started
then sounds good and anyone in the live
chat just
drop a question and we'll get to them
thanks a lot
okay so one brief thing
that i did want to mention um is that a
couple times ago
we um we talked about we covered
learning um
but since then um just wanted to let
people know we actually
caught a little a small error in the
learning section
um in the previous version that we've
now corrected and it has to do with the
way that you
calculate the um the novelty term and
expected free energy that gets added to
um it gets added to expected free energy
when you're doing learning so it's what
drives the parameter exploration
um term expected free energy it
basically drives an
agent to seek out policies that will
tell it more about in this case what the
a matrix looks like
so tell it more about what the
relationship is between states and
observations
and there's equivalent terms that could
be added if you're trying to learn
transition beliefs or
other matrices and vectors in the model
but um
so now just to kind of make that clear
we actually have added two different
additional worked examples
of how um of how to calculate
the uh the novelty term just to make
sure that's clear
so um if if anybody doesn't happen to
have the kind of most updated version
and you're interested in kind of knowing
the kind of rigorous details
about how learning works um in the uh
in the formalism then um you know i it
might be helpful
um to download the updated version so
that you can
have additional work examples to to get
a better sense of how that works
um so i just wanted to um make that
uh clear like i said it wasn't it's not
like a big error but it's a small error
that if you
were to read it it could be confusing um
so
i just wanted to make well just wanted
to highlight that for people
um but today like i mentioned
the focus is going to be on actually
building task models
so and applying them to data and there's
actually
you know it's probably you know this
doesn't this isn't necessarily like
the only way you could break it up but
i've broken this up into kind of six
steps
that um are probably a good kind of
heuristic
um you know road map or or whatever you
want to call it
for doing this kind of work so the first
thing
is that you have to have a task and you
have to have participants perform that
task
the second thing is you have to build
one or more models of that task so
one or more models in this case
partially observable markup decision
process models
in the active inference formulation
that can reproduce or generate um
simulated behavior for that task
um and so once you do that
then the next thing you need to do is
you need to find somehow find parameter
values
in each of those models that you
construct construct
that can best reproduce each
participant's behavior
so for instance under one model you
might find that
the first participant the model can
reproduce the first participant's
behavior the best
if it has a particular um
say value for how much they want the
reward so for instance like the value of
the um
or the think about it as a precision of
the preference distribution
or you might find that for another
participant
you need a lower value for that to
reproduce their behavior well
and but they need something like a
higher learning rate
or a lower action precision value
right there's all these different
parameters in these models we've been
covering
and different values for those
parameters are going to
be better different parameter value
combinations and these models can be
better at reproducing one person's
behavior versus another on the task
um and so what that requires is having
some kind of estimation algorithm
um something that basically searches
through in some way
different combinations of parameters and
checks how well
it reproduces um a given participant's
behavior
um and so and so like i said those are
called parameter estimation algorithms
and there's a few there's several
different um
types that you can use um i'll briefly
mention a few
and then we'll go into detail on the one
that is probably most consistent with
um the general kind of theme of active
inference models
which is a scheme called variational
base
so once you've found for each model
the parameter values that best describe
each participant
then you want to know okay well which of
those models is the best model
and so in that case you need some kind
of way of comparing
how well um each model on average can
reproduce the behavior
of the whole group of your participants
so each model is going to have their
best fit parameters for each participant
but still the best fit parameters for
one model
might still do a better job than the
best fit parameters for another model
and again we'll go into this
and then once you've identified what the
the best model is
then and this is something that might
not be obvious but it's really important
is you have to somehow confirm that the
parameters in the best model
are recoverable so you can either talk
about this as whether the
the model is identifiable or that the
parameters in the model are
recoverable and that's something that
again i'll expand on
but the but the basic idea is more one
one kind of simple way to think about it
is um what if it's the case
that two different combinations of
parameter values
are equally good at reproducing or
explaining
a given participant's behavior if that
were the case then there isn't any
unique
combination of parameter values that is
kind of
the best set of parameter values
and what that means is that
you could take one set of parameter
values
generate behavior with it but when you
ran estimation on that
you could get a very different set of
parameter estimates
and if that's the case then the
parameter estimates that you're actually
getting for that model for a participant
aren't necessarily a reliable or
uniquely best
description and so that means that
parameters aren't recoverable or there's
no kind of
uniquely best set of parameters under
that model
so you need to do that to make sure
that's true for the winning model
and if it's not then you might move down
to say the second best model and see if
that's the case
right so you want to find the best
fitting model ideally
you want to find the the best fitting
model that is also
clearly recoverable that has clearly
recoverable parameters
finally once you have identified
the winning recoverable model um
you have this set of parameter estimates
that describe each person so these are
individual difference variables right
one person has higher action precision
than another one person
has a more precise preference
distribution than another
and at this point you can take these up
to the group level and you can say okay
you know for instance does a healthy
group
have different parameter values on
average than
say a group with depression or a group
with anxiety
or you can say you know do parameter
values predict something on a continuous
you know in a continuous way right maybe
higher anxiety levels are associated
with
lower action precision
or something like that and so i'll show
you guys examples of this kind of thing
as well
um so first and you know we've kind of
already covered this in previous
sessions
or just examples of it but there are
lots of different kinds of tasks that
you can
model which is kind of a nice perk of
active inference models
is that they're not just about decision
making as a main component you can also
use them to model
kind of simple perceptual tasks so
christopher in a previous session
showed how you could build a model of a
simple perceptual oddball or local
global
task which is almost entirely about
perception
you won't get necessarily interesting
individual differences in behavior in
these tasks
but you can show differences in say
simulated event related potentials and
eeg studies
and in principle you could fit the erps
to find the best parameters for a person
but you can also do um inferential or
inferential or prospective decision
making tasks like where you
plan for the future and make a decision
based on what you expect future outcomes
to be
um which is the kind of thing um uh
kind of like what i'll be showing you um
or with the explore exploit task um but
the explore exploit task
that we'll be showing is is kind of very
similar to a standard kind of
reinforcement learning task it just
requires that you
seek out information before you can
really know or even learn
what the right reward values are
and then lastly you could combine this
with neuroimaging
in the context of predictions from the
neural process theory which is what
we've talked about
and what we covered in relation to the
hierarchical model that christopher
covered
so i should say that this is kind of a
fairly new emerging
field and so there's not that many
papers um empirical papers that do this
kind of thing
um you know it's it's something that my
lab has kind of been trying to
make more common uh practice
which is again part of the motivation
for this tutorial is so that
a larger number of researchers can do
this kind of thing
um but so you know i mainly work in
computational psychiatry
um and so you know we've this has been
used to show say for instance
less uh less precise um lower action
precision
and substance use disorder and also um
slower learning rates for negative
outcomes and substance use disorder
you know we've shown things like that
greater decision uncertainty
is associated with uh people with
depression anxiety and substance use in
the context of
approach avoidance conflict tasks
most recently we also used kind of a
simpler
bayesian perception version of an active
inference pmdp to show
differences in the sensory precision in
an interceptive context so for instance
when people
how how precisely or accurately people
perceive their own heartbeats
and interesting differences there
between
again clinical multiple clinical groups
and healthy participants
and then lastly and you know one of the
first papers using this kind of approach
was actually philip fortenbeck's
paper where they looked at
predictions about mid-brain mid-range
dopaminergic responses um
and uh changes in the expected free
energy precision
term that we had talked about um in
previous sessions
and was able to show nice relationships
between
these expected precision updates and um
and uh what and neural responses using
fmri
in a region of the midbrain that is
known to
be rich in dopamine neurons um
so this is just kind of these are recent
examples um
that you know we're hoping other
researchers can can you know
build on um on that neuro slide
these examples we're seeing a couple
examples of different technologies
like fmri but we also heard it goes
beyond neuroimaging the scope of these
methods
and we're also seeing a couple of
biological questions or
conditions um related to your clinical
experience
let me complement those two axes of
variation with the methods in the
biological question
with this algorithmic dimension and
there's a question in the chat that says
what kinds of tasks
reflect the relationship between dynamic
programming and active inference
for example bellman optimal state action
policies thanks for the elaboration
so how do we connect some of these
biological and methodological
uses and axis of variation to some of
the algorithmic questions about
optimization dynamic programming so
um yes i mean it's a great question we
actually have a recent um
pre-print that uh lance decosta's first
author on
um um where he was able to come up with
some proofs to show when active
inference
is and is not bellman optimal um and
in terms of what the the conclusion was
in terms of
one-step policies um active inference
is bellman optimal in the context where
um
the uh precision of the preference
distribution is maximal uh
it's maximally precise over whatever the
reward outcome is
um active inference models in the kind
of simple md
pomdp scheme we've been talking about
here um they're not belmont optimal
or they're not guaranteed to be um in
the context of uh multi-step so like
deep
temporal policies um but um
whereas the um more recent uh
sophisticated active inference
algorithms
um are uh bellman optimal um for deep
policies
uh that's because they more or less
correspond to backward induction
um so um that's that's um
the probably shortest answer i could
give to that
christopher did you have something to
add there
uh no i yeah i was just going to point
to the lane slot to costa paper
great i posted the cost of papers that i
think are relevant in the chat so
thanks for that question and continue
okay
so just to be clear this is a very
specific paper
that you know lance and i and nora and a
few other people put out as a preprint
just a couple of months ago um so so i'm
talking about one particular paper
of lance's um um so i mean i can
certainly that point that
that specific one out so people know
which one i'm talking about
the relationship between dynamic
programming and active inference the
discrete finite horizon case
with yeah that's the one decosta sajid
par fristen and smith
yep okay cool um
all right so hopefully that helps um
um okay so now i'll kind of be going
through um each of the the steps here
that i was talking about
um kind of one by one right with our
explore exploit test
example so first step one is you have to
have participants perform a task
right so in this case um and i should
say for some of this it's really going
to be assumed
that people were following along with
previous sessions
um the time constraints just really
don't allow us to cover
all the background um so that somebody
could watch this one without having seen
the other ones and fully follow
everything i'll be talking about
um so just just to make that clear if
anything is kind of confusing then the
previous sessions are kind of necessary
we walked through the matrices and some
of the degrees of freedom
in this setup so i think it should be
good check out the other videos if you
haven't already
but but you know as a brief you know
kind of refresher about the task that
we're talking about
um the on each trial the agent starts in
a start state
and then he can either directly choose
one of two slot machines
and if they're right they'll win four
dollars but if they're wrong they'll win
zero
um and they start out not knowing you
know
like just flat prior over whether the
left or the right one is
whether it's the context in which the
left one or the right one is more likely
to win
so it's just 50 50. so it's pretty risky
to just pick one right away
at least before you've learned if one of
them is actually more likely
if the context in which one is more
likely to win is more common
so instead the other thing that the
agent can do is they can choose to get a
hint
and the hint will tell them which um
whether it's a context in which the left
bandit is the one that
is more likely to win and when it's the
right one
um and in each of the contacts in the
left
in the context where the left one's
better it will pay out eighty percent of
the time
uh whereas in the context of the right
one uh the right one will pay out eighty
percent of the time
um but the catch is if you choose to
take the hint then you'll only win
two dollars if you get the right one
afterwards
um so this trades off this kind of
reward seeking and information seeking
where if you seek information first
you're more likely to win
but if you choose first right away then
you'll get a higher reward if you're
right
um so it specifically trades off reward
and uncertainty
um and this is where a lot of this is
not going to make sense unless you've
seen the previous sessions
um is that and the second thing is you
have to build one or more models
of the task we just talked about in our
example we'll use two different variants
of the model
one where we're just going to fit the
risk seeking parameter
and an action precision parameter and a
second model where we also assume that
the agent has a learning rate
or that there are differences in
learning right
so for those that don't remember um the
risk seeking parameter
just corresponds to the magnitude of
this rs value
um so what this says is at time two
if the agent observes a win so this row
is a win then
the value of that win will be rs
and if they instead wait and choose the
hint they'll continue to observe this
start thing
at time two but at time three if they
win
then the value they will win will be
this rs value divided by two
um so so whatever rs ends up being
the win at the third time point if they
take the hint is half of that
um so we're going to be fitting for each
person what that rs value is
which again stands for risk seeking
which would be clear to anyone who's
watched the
previous sessions because the higher
this value is
the um the less exploratory drive the
agent will have
and that means that they'll be more
likely to take the risk and just
choose one of the slot machines randomly
as opposed to
taking the hint first to be more
confident in which one's right
so the second parameter is this action
precision parameter
alpha and all this basically says
is the precision or the probability of
selecting some action
given an alpha value corresponds to this
um so our corresponds to
whatever the probability is of an action
given the
given a policy um scaled
by this alpha thing and then softmaxed
to become
a um just a proper probability
distribution again
um so it just controls how more or less
it controls how precise action selection
is
given the choice of policy
and then finally in the model in the
second model where we're also going to
assume an agent has a learning rate
um other than just the optimal learning
rate of one
then we're also going to be fitting this
thing eta here which is the learning
rate
and this just says that your beliefs
about the probability of the context
being
that the left slot machine is better
versus that the right slot machine is
better
just updates based on your beliefs about
whatever the that state whatever the
winning state was
on the previous trial again four times
step one
so basically each trial whatever the
posterior beliefs were
over states um they
the count for that just gets added to
whatever the prior
initial states was um athena is at the
next time point
but it's scaled by this etta thing so
you know if etta is one then it'll
attack on a count of one
again if if it knows with certainty that
it was in say like state one
but if that is 0.7 that only add a count
of 0.7
on each trial given that the posterior
distribution was like one
zero um um so
so that's um the the basic setup is
we're going to fit either just rs and
alpha or we're going to fit both of
those and eta
um one note on that ryan i like this
step
to build one or more models because
we're thinking about
active inference as like this process
theory it's instrumental
you know the whole instrumentalism
versus realism question we're using it
as an instrument
and that means that we're iterating over
models we're relating our models to each
other in specific ways like make the
simpler one and then make one that just
adds one more variable
and then it's not like you're asking
what is the active inference model here
it's here's the active inference
approach
and we're going to combine our
perspectives and make multiple models
and we'll be comparing models so the
only limiting factor there is
how many models can we think of at the
beginning and how wise can our model
selection process b
so it's just really like a pluralistic
but pragmatic way to go about it
by saying construct one or more models
because then you're never going to fall
in the trap of thinking you're making
the active inference model because there
isn't the model of anything
statistically
they're just instruments so it's a
really helpful perspective and so this
isn't just a little
um convenience to make one or more
models it's something that reminds the
scientist
or the modeler that they're actually
making one of many or infinite possible
ways to think about a situation
yeah i mean i mean hopefully you've
really kind of you know thought deeply
about what
the most plausible models are given
current theory and you know current
previous or previous empirical research
right so i mean they should be informed
um but yes so you're just you're trying
to find
the model that has the highest evidence
that the observations or the behavior
provides the highest evidence for
and yes it is always possible that
there's some other model
that you haven't thought of that would
be better um but
you know if you have a model that
explains behavior really well
and it does so better than any of the
other ones you can think of then it's
kind of a good
bet um as at least giving you um
interesting individual differences
to to again bring up to a group level
analysis
um so so okay
so you know to get kind of a little
nitty gritty in terms of the the
code and the matlab structure and
everything um you know the kind of thing
you need to do
is you first so you have a participant's
behavior right like
they chose the hint and then slot
machine one that shows the hint and then
slot machine two okay now they just
chose the whole
machine right away over slot machine two
right away
um and so forth and those have to be
coded in
right to each trial in the mvp structure
which
which again uh previous sessions will
explain
um so the mdp structure in matlab
um for each so each uh
each number right inside these
parentheses here will
be the trial that you're talking about
and the dot u here
is the um the matrix that described that
encodes the actions that a participant
took um
now if we remember um so row one here
corresponds to state factor one which is
the context
whether left or right is better and
there is no action for that that's not
something agent control it's just stable
within a trial which one it is
so these just get ones and there is no
other possible action
for the second row though so this is the
state factor that corresponded to
action selection um two
you know action two corresponded to
taking the hint an action three
corresponded to choosing left
so if that was what a participant did on
trial one
then you would have to feed in two
followed by three
right they chose the hint and then they
chose left on that trial
um and so you just have to iterate that
over all the trials in the task
so one to you know end trials um
whatever they did
um so that's mdpu and in this case like
i said there are two actions so two
columns and there are two state factors
where only the rows which only the
second one is control
um so now mdp o.o
is the observations um so
again if you're familiar with the um the
way we set up
the model for this task before there are
three different
uh outcome modalities three different
types of observations you can get
so the first um observation modality
what a hint or not so in this case
one is just you're kind of still
observing the start observation
if you observe two that means you get a
hint
that the left one is better and if you
observe a three that's the hint that the
right one is better
so in this case they got the observation
that the left one was better when they
took
one two one because after they got the
hint they just returned back to
observing kind of the initial
observation
for the hint modality um whereas
um for the second modality here which is
the wind's losses
for the first two time steps they just
observed kind of the starting
observation here
because they chose the hint at the
second time point so there was no win or
loss
and then at time point three they
observed a win so
win is encoded as a three in this model
and two or losses is encoded by a two
um and then uh the final
outcome modality is just the agent
observing what it does
so in this case this just says started
in start state
chose to take the hint and then chose
the left uh
chose to it observed itself choosing
the choice of the left slot machine
so that's it so all you have to do when
you're
instead of simulating behavior you're
actually um
fitting that way you're actually feeding
in participant behavior
to uh fit it uh to fit a model to it um
then you just have to you know sort of
translate the behavior and the raw data
into a form like this that matches the
action and outcome
representations in the model um
and um and so that's it you first feed
those in
um and then once you've done that then
you have to use some kind of estimation
algorithm
which basically means the thing is going
to somehow repeat
simulating behavior in that model until
it finds a model that maximizes the
overlap
between the probability of choosing the
participant's action of the probability
of choosing
actions and what the uh participant
actually chose
right so for instance if it shows hint
and then left bandit left slot machine
on trial one
um it's gonna find a set of parameters
that apply across all trials that
maximize the probability
that the simulated agent also would
choose the hint followed by
choosing the left slot machine
so there are a number of different
estimation algorithms that
can be used um you know the
the simplest possible one is just
something like a grid search
so in this case say you just have two
parameters which this is just arbitrary
called alpha and beta
you can kind of divide this up into
little grids different combinations of
parameter values so for instance like
you know parameter 0.2 for alpha
and parameter value 3 for beta
and then you can just encode for example
what the probability
of the model is given the participants
actions
um or um that would be the posterior
which i'll talk about or just the
probability of participant behavior
given the model and those parameter
values i mean so in this case this
is kind of clear nice result where this
value right here
something like point three and four
that um is maximally and uniquely
the best set of parameters for
reproducing that participant's behavior
and and in this case you're using
something called in this case you're
using something called maximum
likelihood
so maximum likelihood estimation
which just means again you're trying to
find the
model and set of parameters for which
the
uh probability of the participants
behavior given that model is highest
which is a type of likelihood right so
you're trying to find the maximum value
for the likelihood
which you just in this case encode with
these you know redder colors
equals higher uh likelihood
of behavior given the model you can also
do something
a little bit um so to be clear what we
actually would want
right is there is the inverse of this we
would want the probability of a model
given participant behavior which is the
posterior
but when you're doing maximum likelihood
estimation you're just assuming here
that you have essentially a flat prior
for what the probability over models is
so in this if that's the case then the
probability of the model given
participant behavior is just
proportional to
the likelihood but another thing you can
do
is called maximum posterior or map
estimates
which is the same thing except it
doesn't assume that you have a flat
prior
um overalls right so if you just start
out with a prior expectation
that one model is better than another
then you can incorporate that
information
into um into parameter estimation
and this is kind of an example of this
where
um you might find this distribution in
terms of just the likelihood
right the probability of data given the
model where a parameter combination
right around here
would be best but then you might also
have some reason to have a prior
expectation
that models down here right are are
actually more likely
and so if you combine those guys
together you can get a posterior that
looks a little different
right like a something very similar um
a very similar model wins in this case
but that's just because
the behavior that's driving the
likelihood here is just already a really
good fit so it kind of dominates over
over the influence of priors but that's
not always going to be the case
so so those are two approaches um
and and again you can you can do them
with a simple grid search
or you can do something so
i should say that the grid search kind
of thing it only really works
when you have a few parameters we don't
have very many
and the reason is because the more
parameters hat you have the higher
uh dimensional um this uh parameter
space becomes
and it just becomes it it takes sort of
intractably long
um to do to search through every
possible combination
um so what you do instead
is you use some kind of gradient descent
process um
exactly like the gradient descent on
free energy that we've been talking
about
for how active inference models arrive
at posteriors
over states and posteriors over policies
um so there's a
really kind of interesting overlap
between the way that you estimate models
via gradient descent and the way that
you actually
the way that active inference models
update their beliefs via gradient
descent
um so in this case or is a very
good point and i just want to point out
one similarity and difference because
people may have heard about these
grading descent algorithms for
descriptive statistics or for fitting
descriptive models
so that's from going again from the data
that's empirical
to a descriptive model or descriptive
statistics like regression
coefficients and if it's a
multi-variable regression
you might need to use not just a grid
search but act that you can do a simple
maximum likelihood approach like a least
squares approach or something like that
you need to use this kind of a complex
multi-dimensional optimization
to get to that descriptive statistic and
then there's this little twist
where actually in active inference we
might be using those computational
techniques
but we're estimating the parameters of
an underlying generative model
and then there's this nice little return
where actually the generative model is
implementing that as well
yeah so so in so in this case
you you absolutely need
some kind of prior value because with
gradient
descent you're not exploring every
combination what you're doing is you're
starting at some starting point
which is just coded by a here um
and then you're just like when you're
minimizing free energy
in in an active inference model you're
searching neighboring values and trying
to find a value
that has a higher
likelihood or a lower free energy
and then you just kind of keep doing
that iteratively
until you find some value
that where the likelihood stops getting
bigger
or free energy stops getting smaller
and that then corresponds to your
best estimate or your posterior
posterior
estimate for the
parameters for a given participant
and so when you're doing this
with when you're doing it with a
gradient descent for
uh free energy then um that ends up
corresponding
well to um the actual approach that
we'll be talking about
um or actually using in our example
which is a variational base
so the variational bays you do exactly
this you set a prior
mean value and a prior variance for each
parameter
and then you do gradient descent until
you find a set of parameters
that minimize free energy
which is again an approximation to the
model evidence
so but but it's important to keep in
mind some potential limitations of this
approach which is if you see here
this parameter space it does look like
there is a kind of nice
single right like local minimum right
the local place where the free energy is
lowest
or um where the uh again it would be a
local maximum be like top of a mountain
in this if you were talking about the
highest
likelihood um they typically do
log likelihoods as opposed to
likelihoods
and but one of the issues is this sort
of
the parameter space need not have a
landscape that's quite this clean
you might end up for instance having a
landscape just moving to a
two-dimensional case now
that looks kind of like this where if
you start out say with a prior value
with prior values that um you know like
this kind of red
circle up here then if you do gradient
descent
you might end up getting stuck in a
little local minimum like this
um where you know and then and then the
gradient descent algorithm would say hey
you know actually
you know this seems like the best one
because if i move in any direction
then the free energy goes up um
whereas actually the global minimum the
one that you would want to get to is
this different one that's on the other
side of this little kind of
free energy hill um and so
you know this is this is an example
where
i'm choosing the the right priors is
important um to get the
to be able to get the the best parameter
estimates
um but also this speaks to the kind of
thing about parameter recovery that i
was talking about earlier
because it could be that if you set your
parameters kind of right on the top of
this hill thing here
then even if the parameter combination
over here is the one that actually
generated the data
you could get stuck over in this one in
which case the estimation algorithm
would not give you the right parameter
estimates
so this is why what i mentioned earlier
about
assessing parameter recoverability is
really important
so all my way of saying it's important
to choose good priors
or to figure out what good priors are um
and there are there are interesting ways
to try to
optimize that so there are kind of
hierarchical bayesian techniques we
won't talk about these explicitly but
where you can kind of and these won't
necessarily solve this problem but where
you can
more or less you can think about it as
it estimates the parameters for each
person
and then it notices hey you know looks
like these are all shifted over
you know the distribution of these looks
like they're all shifted over say to the
right
you know so actually the looks like the
distribution is more kind of over here
and so then it might um choose that
um choose that uh that the kind of mean
value of that
um as the new uh priors
um for uh for redoing the estimates
um until it finds uh values that um
that essentially it's it's helping you
to find whatever the optimal priors
would be
um but uh but again that won't um that
won't always
solve this sort of problem with a lumpy
landscape
you know um one other little thought
it's actually almost three
layers with the red dot so there's us as
agents on a landscape
we actually need to come up with policy
as agents in our niche to get around
local minima like my door's closed i
need to step away to open the door
before i can move
through it then how are we going to fit
policies for ourself
under pervasive uncertainty well we're
doing this state estimation with the
policy
so that we can actually come and then
how are we going to converge on those
parameters
using a a little bit like a gradient
descent
algorithm internally not internally to
us is just within the agent
computationally it's just it's very
interesting because people may have
i'd imagine there's one kind of person
who sees this and says oh we talked
about optimization for a year
in my course so i've heard all about
non-convex non-complex optimization
techniques or rugged fitness landscapes
and there's another group of people for
whom actually this optimization theory
might be quite novel because of
how they've looked at modeling before so
very interesting
and to put into the fourth section like
that really spoke a lot
so interesting stuff ryan i just want to
ask christopher you want to add anything
before we continue with this
no this really is very much ryan's part
of the paper oh cool
yeah yeah i'm just here kind of oh if
anything
more than welcome to add thoughts or if
you have any other insights about
technical aspects
no no nothing really um i would just
i might ask some questions if something
if things come up
um because i'm gonna be doing this at
some point in the next couple of months
but um so yeah
great thanks okay so
um so um like i said the the kind of
detailed example that we are going to
use is variational days
um and note that variational message
passing is
again what agents are using within
um within active inference models
which we talked about before so we're
using something very very similar to
this
or i mean so technically i should say
now it's using marginal message passing
in the latest
versions but again we cover this it's
very similar um to variational message
passing it's just kind of a slight
improvement
um but so we're using um the same sort
of approach
to estimate parameters uh to estimate
the parameters that people are using
uh the parameters that are kind of you
know potentially kind of uh stored in
their brain
in some sense um so
so we're doing gradient descent on
variational free energy as i mentioned
and as i mentioned you need to specify
prior means and prior variances for each
parameter
and then you just move the prior values
in the direction
of increasing action probabilities um
but what you're doing because it's a
gradient descent and variational free
energy
is you're not technically just trying to
find
the maximum likelihood value like you're
doing with like a grid search
um instead um what you're trying to do
is you're trying to
well i should say that the variational
free energy part of it
means that there's a complexity penalty
um and what that basically means is so
if people remember from
variational free energy when we talked
about it before the simplest way or kind
of intuitive way to think about it
is that it's just complexity minus
accuracy
right and what complexity means is how
much you have to change your beliefs
so if you start out with particular
prior values
then the farther you have to move those
move your beliefs from those prior
values
the that's going to push a variation for
energy up
whereas at the same time free
variational free energy is going to go
down
as the model predicts behavior better
um so what it means is for instance
you know if i start out with a prior
value that's say way down here
like around like i don't know one and
three
then it's going to have to move from
those prior values
a pretty long way before it gets to
a set of parameter values that fit well
whereas say if i started over here it's
not going to have to move those as far
but if i were to do that then
potentially
instead of the posterior estimate
posterior parameter estimates actually
settling on this thing that has the
maximum likelihood
it might stop say like around this one
right a little lower than it or
something like that
um because that maximizes that leads to
high
accuracy while also not having to move
the parameter values
uh really really far not having to
change beliefs too much
from what the um uh informed
prior belief was um so it's you know
it's
it's important right to think that this
assumes something that
that the priors you have that you have
them for a reason right that they're
actually based on something
that they're informing you um so that
so that it is actually does actually
make sense not to move them
too far from prior values and in
practice the reason this is helpful
is because one thing that often happens
when you're just doing maximum
likelihood
is that um that maximum likelihood will
be with respect
to your particular data set right your
particular
set of parameters or set of participants
um but often if you choose just the
maximum likelihood value
then that's kind of over fit to just
those participants
where if you were to say apply that
exact same model to a new set of
participants
um it might not do as well because
it was fitting you know specific things
that were not generalizable about your
data set in particular
um so by by um
by putting this kind of complexity cost
on it it prevents overfitting which
means that
the predictions of that model are more
likely to uh generalize
to a new set of participants later so it
prevents overfitting which is a very
common issue in in just standard
frequency statistics as well um
um okay so so that's so that's what
you're doing with variational base is
doing this kind of
complexity minus accuracy thing where
you're preventing overfitting while also
maximizing
the accuracy of model predictions um
okay so then like i mentioned you need
to do model comparison to identify what
the
best model is um
now uh uh let's see so i just realized i
should probably set something in motion
here let's
see if i need to uh so when we actually
go into the code here in a minute one of
these things takes a long time
um let's see so i set it to store stuff
i just want to triple check that i
shouldn't um you know set this thing
um let's see
uh yeah i bet i should have double
checked this beforehand
um
[Music]
cool though it's really
interesting and christopher you want to
add anything or maybe just a quick note
while ryan's figuring out like what is
it like to be learning these models or
what kind of skills do you wish you had
earlier when you were learning the
models um
other than of course your own tutorial i
mean
[Laughter]
i think everyone who did undergrad
psychology is probably
at some point in there i i did cognitive
science as an undergrad but
um i took a lot of psychology classes
when you take staff psychology a lot of
people read this andy field textbook
and he has a chapter on um
uh some type of like esoteric regression
and introductory sentence is like i've
never done this
i don't see myself ever doing it but i
wrote this chapter about it and if i
ever need to do it i will be very
impressed by how much i seem to know
um so that made that probably will
describe my experience with um
this tutorial to a certain extent uh
okay so yeah so real quick i'll just i'm
just gonna
jump to the code and explain why i
should have started this thing
is that that so what if you set this
thing to sim equals 5
then what it's going to do is it's going
to actually generate simulated behavior
for six hypothetical participants
where each participant has a different
combination of parameter values that's
generating
that simulated behavior and then what
it's going to do
is it's going to then apply the
estimation algorithm
to the resulting simulated behavior
and it's going to give you a set of
results
and then what it will do is it's going
to do bayesian model comparison on those
to identify what the best model um
is and then i'm going to try to do this
i'm going to try to set the so i'll just
say for
for um for
the purposes of um you know you actually
you guys actually doing it
yourself at home um
i'm going to uh
i've set this thing to 32 trials for
each
uh simult for each set of simulated
behavior
but maybe if i set this to 16
then it will go faster just to think
about what's happening
people looking through these equations
every time two matrices or
two numbers are getting multiplied the
computer has to do something
so we're kind of nesting matrix
multiplications
inside of even bigger ones so if you
want two time steps for two
larger time clicks for four models you
know for four participants it really
starts to balloon
rapidly especially when there's
computationally intensive steps
yeah so here just uh just to show you
guys what's going on so i just started
this thing
and if you look in the matlab window
here
it's calculating log likelihood so ll
stands for log likelihood
over and over again under a particular
set of parameter values
and in this case it's negative 31 and
it's trying to
minimize that or in this case it's
moving it closer to zero so
maximizing in a sense but bringing it
closer to zero so now it moved via
gradient descent to a second set
of parameter values and now it's found
that okay now the log likelihood is
negative 22. so we're even closer to
zero
and again same thing now we're at
negative 19 and it's going to keep going
until it settles on a stable value
and in this graph that will update
every time which i'll uh
show you here so this is just showing
ignore i should say these so something
to explain
is these routines were originally
designed for dcm for dynamic causal
modeling with fmri
so um a lot of the a bunch of these
graphs and also the the sorts of labels
that they have
are don't really apply in this case they
only apply to dcm
um so you know so ignore a lot of the
labels but the point here is is that
each iteration as you go from left to
right is a new estimate
of the log likelihood for
every um for the set of parameter values
it's trying
during gradient descent um and so you'll
see
that after a while the thing is just
going to kind of
plane out it'll converge onto a value
you see right now is it's
like 17.35 and now it's like 17.16 so
the thing is kind of
starting to converge on a stable minimum
log likelihood um so now you know i
found a set that actually is still at
16. so the thing is still
going for a bit to converge and down
here
these are the posterior deviations and
again ignore the
ignore a lot of the units here but the
way that you can read this
is just that 0 here corresponds to the
prior values
that you set um and if it's going
if the bar here is going down then that
means that the
posterior parameter estimate is uh
is lower at this point it's gone down
from the prior value
and the this kind of red pink thing
around it that's the posterior variance
um so in this case and parameter one
here
is uh the action precision and parameter
two is the
reward seeker reinforce or risk seeking
i think i can double check whether those
are backwards or not um
but uh which order those are but this is
just saying that whatever this first
parameter is
um the the posterior mean estimate here
is
um you know whatever that is that
actually corresponds to the real units
of the um
of the uh parameter but it's not very
confident
in that posterior immune estimate
whereas here
the second parameter um it's also this
negative
posterior at the moment but it's very
very confident in that posterior
estimate
um um so so that's what that means and
these will update
with each iteration um but so now you
can see that actually the thing kept
exploring
and now it's actually found a set of
parameter values
that um you know continues to actually
explain the behavior
the simulated behavior quite a bit
better right so now it's at like
negative 13.
so you're gonna see this it almost kind
of converged for a bit but now it's
actually kind of going back up
um so eventually eventually it will
converge but it's just doing really
really well
at finding values that explain behavior
uh well um one thing i should point out
though is that the actual values of
these absolute value of these are not
really informative because they're
they're they're basically the sums of
the action probabilities
for each trial so these numbers will be
bigger if the task has more trials
um so in and of themselves it's only the
relative values that are meaningful
um this reminds me actually it reminds
me a lot of
bayesian methods in phylogenetics
where it's like what is the likelihood
of this phylogenetic tree
it it's given some number by a program
which sounds weird to think about the
state space of all the possible trees or
something like that
but it turns out by doing this kind of a
gradient descent
searching through all the possible trees
you actually do
converge on a tree that is
generative of the kinds of data that are
observed and so it's just really
interesting to see how this is working
and it's fun to watch the number
drop down to so
so now so in this case it converged for
the first person
um and you know these were the posterior
deviations and then here's the simulated
behavior
of the participant under those
parameters
so you can see that you know the
parameters do
fit the behavior really well right the
probabilities are pretty high
under those parameters for each for
every action
you know there are some little
exceptions but but it does pretty well
um right so now it's just now it's just
moving on to the next person
sorry what oh it might just be helpful
to describe what the blue dots are
just for yeah sorry again i'm assuming
people have
watched video sessions so blue
corresponds to the actual chosen action
um on the first at the first action for
each
participant um so basically this is
saying and so black
means probability one and as it goes
toward white that means probability zero
so this is just saying basically 100
probability under the model
that the agent would choose the hint and
the blue dot says that's what they
actually chose
and so on and so forth so anytime that
there's a
light gray you know that's on the part
where the blue dot is that means the
model didn't really do that well at
predicting that behavior
um but you can see in this case most
it's pretty dark
around most of these blue dots so it
does pretty good
um is the point um so now like i said
this is just going to iterate around
for the six agents that i mentioned and
it's just going to compare
and then it's going to compare the three
uh the three
that did have a learning rate and the
three that didn't have a learning rate
in the model
is what it will do um and so just to
kind of summarize what you've said so
far so the steps would be something like
you would actually get your empirical
task right and think about how
the sub the actions that the subject has
actually got or the participants
actually going to make relate to what
the model is going to make
all the actions available the model you
come up with some mapping
and then you would then presumably in
this just translate them
in some way and plug those into your u
mdp dot u which is the actions
participant shows and mdp.o
which is the observations that they
actually saw
yeah and then you would plug into the
algorithm essentially
yep you plug it into the algorithm and
um
and then it just the algorithm just
repeatedly
computes the sum of the log likelihoods
for each trial
um and then and then tries to find a
minimum of that sum
okay and so in terms of this is a
something i've wondered about um how do
you choose what the best trials
uh or what the best priors are is it
okay just to kind of
in in silico uh
simulate a bunch of things and just say
hey this this seems reasonable
um in a lot of cases yes i mean so
so there's a couple things to do one is
you can
you can do the kind of modelist or the
recoverability stuff
um you know beforehand and try to find a
set of parameter values
a set of prior values for which the um
the the parameter estimates are
recoverable right
so if you set one set of priors then
maybe the thing does get stuck in local
minima but if you said
another set of priors then the
generative parameters
um actually do end up matching the
estimated parameters really well
um so so there's a couple different
things so one is
yeah do some of the simulation
recoverability stuff ahead of time to
find good priors
another thing is you know if you just
you know estimate participant behavior
and you start to see
that the posterior estimates tend to be
really far away from the priors you're
setting
um that's kind of an indication that
you're probably not setting very good
priors so then you might like try
setting new priors that look closer to
where everybody's kind of moving um yeah
so we do have we do have a footnote
about this in the paper from memory
um but it'll be good to kind of make
that explicit
another way that i've seen that in the
field of evolutionary biology is
if you have wildly disparate priors like
the so a fallacy is that the uniform or
the flat prior
is like unbiased there's so much to say
about that i'm sure
ryan knows well but like if you have one
prior that's stacked up against zero
and another prior that's stacked up
against one and then they both converge
like from kind of multiple sides
that's a simple example but if different
families of priors
and models that are very um paired down
ranging to ones that have very complex
error
models if a lot of different layers of
complexity of the model
and densities that start stacked up
versus one end versus another
then of course that's a difficult thing
to manage but that at least means that
given the empirical data you have and
the task that you're modeling
you have a really predictive model so
again we're not realists we're not
actually getting the truth with these
recursive and iterative and
multi-perspectival models
we're just fitting more and more of the
variants explained
in our empirical data yeah
yeah so just uh just to kind of give you
guys another example so you can see
now for this other set of parameter
estimates you know convergence took way
less time
right it just took you know seven
iterations and it converged really
quickly
and one reason to see why is that for
this one it didn't have to move
values very far from priors because this
was an agent
whose behavior was generated by
parameters very close to priors
what one other point there though is
even if it looks flat for ten time steps
it could still be trapped which is why
things have to be seated and have really
good randomness
because there's no hard and fast rule
for when you terminate
so for example in a lot of the
evolutionary simulations we would do
you discard the first like 10 000 or
more
time steps like burn in you just discard
them because you think that actually
it's too much reflecting your prior
estimates
and then even if it looks like it's
converging or as one of my professors
called it a fuzzy caterpillar
because it's kind of like the model was
sampling from the fullest possible range
of variables
and it was still coming back home that's
the fuzzy caterpillar
but even then it could look like a fuzzy
caterpillar for like a lot of time steps
and then just totally
hit on a new combination break into a
new realm so it's really
hard in a challenge so just so people
know that's actually not
true in this case so variational base is
a is a deterministic in the sense that
um you you don't do this kind of you
know
burn in you don't um right variability
you just deterministically like if i ran
this over and over again it would give
me the exact same parameter estimates
each time
um so there is there is actually no
variability i mean the kind of thing
you're talking about is more like monte
carlo
yeah it's gonna say sorts of approaches
yeah sorry i didn't mean to say that
there was a burn-in
um i agree that was just yeah little
analogy but thanks for clarifying so one
advantage of monte carlo like sampling
methods is that you over
given infinite time you're guaranteed to
margin to approach
the true posterior or to obtain the true
posterior
uh it's also extremely computationally
expensive
um variational base is really quick
like you can run this stuff on your
laptop so um the monte carlo is based
upon sampling that was the different
domain that i was um referencing there
you have to sample
in cases where you don't know some of
these distributions don't have them
defined so perfectly
but when you have access to this level
of specifying
then there's a whole new range of
techniques which is why it looks more
like matrix multiplication
and this sort of like convergence to the
variational
free energy estimate rather than just
sampling endlessly from a landscape
that's of unknown
you know anything else but yeah thanks
for that sorry
so so just take i mean show again just
to give you guys a sense so in this
so this kind of participant you can see
that it's pretty kind of
the distributions are a lot less precise
and this is a person who has a much
lower action precision value
so these were generated by a lower
action precision value
agent and the model is doing a pretty
good job just finding a low action
precision value that kind of spreads the
distributions
flat enough around it that it captures
it provides decent evidence for each
action
um and so anyway so just just to uh
again to to give you guys an intuition
for what's going on
um but so once this is done
then what will happen is we'll have
these
uh the free energies of the winning
model for each person for each of the
two models
um the one with and the one without
learning rate um and so we want to do is
we want to do bayesian model comparison
um which is where you're going to
compare the free energies for each model
for each participant
to find the model with the lowest free
energy across participants
and the winning model um so the the
little spm function that you know we
include here
it'll spit out several things but the
one that you want to focus on
um just to keep things simple is um
the one that has the highest what's
called the protected exceedance
probability
um and this is just the probability that
each model
is the most likely model across all
subjects while taking into account the
null possibility
the differences in model evidence or due
to chance so
so it's like i said it's just it's just
which is the best model
um when taking into account the null
model
um as a possibility um
and i'll um i'll show you that
um in a second let's see is this thing
it's still going
it's uh yeah okay still going
um hopefully it'll be done soon but so
i'll keep i'll keep moving through here
and then we can return to this once it's
done
it's actually going pretty fast since i
made it so few trials
um but so so that's you know what we're
doing here
um and uh so now
you know we've kind of already touched
on this a bit but
so now is the point where we would
confirm
that the best model is identifiable you
know or that the parameters are
recoverable
and this is so i already mentioned this
a little bit but that you know it's it's
clear that not all models are
necessarily going to have
unique parameter solutions right so if
you have a landscape like this
you might start out priors at very
similar places
and gradient descent would lead you to
minima
different minima you know different
combinations of parameter values that
are equally good
at reproducing a participant's behavior
so so you always have to show
that whatever model you're using and the
priors that you're using
will give you the same parameters
that you fed in to generate the data to
begin with
and so here um again we've already
talked about this a little bit but step
one is
you would specify multiple sets of
generative parameter values which is
what we're doing
um and this is important as you should
select values
that are the same or similar to the
actual parameter combinations
that you got in your in your true
participants
um because it can be the case that
parameter estimates are totally
recoverable
for certain parameter combinations but
are not recoverable for other parameter
combinations so you care about the ones
you're actually getting
for your participants um
so then you want to simulate behavior
so generate simulated behavior using
each of those parameter value
combinations
run that simulated behavior through the
estimation routine
just like you would for real data and
then check whether the
generative parameters and the estimated
parameters are highly correlated
so when i run this in advance
you know so without having to run it in
real time like i'm doing right now
then for this particular case and bear
in mind this is when i'm using 32 trials
not like the
16 or whatever i put in now um just to
make things go faster
this is what i get for it for alpha for
action precision for the two parameter
model
so you can see even with only six people
the correlation between the
generative uh action precision and the
estimated extra precision is pretty good
it's 0.81 so even with six people
right it's significant um
whereas for uh
the only one well anyway i have a i have
a bunch of them i can i can
i can pull uh i could probably pull them
up um
let's see that's for a totally different
thing
um cool
that was very tutorial
interesting uh yes sorry i'm just trying
to find um trying to find the uh
the figures that i have it's probably
here um
well no okay not positive where i put
them actually
but if i can't find them here then
uh it will it will spit them out
um but um but
point point being um these are uh
um in this case even with just six
values um
all of the parameters um tend to be
really good
right in terms of recoverability the you
know the correlations between generative
and estimated parameters tend to be
you know between point seven and one
point seven and point
nine something or other um so they're
they're
they're good um so then so then finally
the last thing that we wanna do is once
we have
parameter estimates for each person in a
winning model
that is recoverable then we can take
those values
and we can put those parameter we can
use those parameters
as individual difference measures
between subjects um
you know at that point there's a number
of things that you can do
so you know the kind of simplest thing
you know if you if you want to kind of
fall back on on frequentist
statistics is you know you can do
standard you know t
tests anovas correlations regressions
etc um
and um and you know i mean you know
we've done that before
it's fine in some cases um if you want
to kind of stick
with the more kind of general bayesian
theme of active inference then you can
also do things like
um you know do things more like base
factor analyses
and you know both of these are often
kind of used
or or even used together um
and just to give you a couple examples
sorry i'm just going to triple check
that this thing is not
done yes still not done just one note
there is the spm textbook
has many points of contact between
parametric
and um like standard very classical
statistical approaches and then very
bayesian
approaches and mixed methods and it will
switch out or show it both ways
so it really is pretty interesting how
it comes together here
so so to kind of show you guys a couple
examples of how you would use
um these kind of you know use parameters
at the group level
um you know this is just i'll give you a
couple examples from from our papers
um so in this in this one in journal of
uh psychiatry and neuroscience
um what we did is we had a this simple
kind of approach avoidance conflict task
where more or less the participant had
to kind of choose to move this little
avatar guy
closer or farther from one of these two
ends
of this little kind of runway thing
and they knew that the closer they were
to one side the higher the probability
was that they would get an outcome
associated with symbols on the left side
and same goes the closer they are to the
right the higher probability of getting
the outcomes associated with the right
side
i mean here a rain cloud means they
heard like a really aversive sound and
saw like a really aversive picture
you know like it's like hearing girls
screaming and seeing a picture of her
being like pulled into a van
you know like really negative stuff um
and uh whereas the sun thing here man
you kind of saw this kind of like
neutral maybe slightly happy thing
um and uh you have this kind of red this
kind of bar thing on the side and the
more
filled the red bar was the more points
they would win
um so you have kind of clear cases right
where it's just if it's just rain cloud
versus sun
you should just go to the right if it's
just sun
and sun plus some reward you should want
to go to the right
and then you have these conflict cases
where it's negative stuff
plus you get some reward negative stuff
but it gives you plus you get even more
reward and negative stuff and even more
reward than that
um and so and so that's how the task is
structured
and so you can make a pretty simple
model of this
where one state factor is beliefs about
the trial type
right whether it's uh this kind of trial
this kind of trial this kind of trial is
controller that kind of trial
um and then you can have a state factor
corresponding to
beliefs about the runway position right
so uh beliefs about whether the avatar
is in position one two three four five
etcetera
that's it and then you just have um
you set up likelihoods that generate the
probability
of um of each position
generating what sorts of outcomes and
what sorts of runaway positions
given beliefs about trial type right
here ryan so you have it phrased as
there being five trial types but
would it be possible to have like a
model where it was like a state
estimate left and a state estimate right
for
the stimuli type and a state estimate
left and say estimate right for the
reward value
because this frames it in a very
behavioral trial
centric way with doing estimate on which
one of the five scenarios you're in but
i'm just trying to think about cases
where
you might not know which scenario you're
in or even what the total set of
scenarios is
so you're just doing state estimate on
reward and on stimuli
um yeah i mean i mean yes i mean the
well
well i guess it kind of depends right so
i mean if you if you were to
give somebody sort of uncertain cues
about trial type
um then um then
i mean presumably you would just you
wouldn't need to i mean you would just
still have
um if they know what the different trial
type possibilities are then you could
just have uncertain cues so they just
don't have a precise
belief a set precise prior belief over
the different
over this state factor but if you
didn't if there wasn't any set beliefs
about trial types and there's just any
possible combination
of you know sun clouds zero points two
four and six
then um um i suppose you could do
something where you just have a kind of
non-factorized state factor that has
like
just every possible combination
or something like that um you could do
that i mean it would uh
um there are reasons to actually build
like so there are
obviously time saving and model building
considerations that mean you should use
factorized distributions
um but there are actual empirical
considerations which means that
i think if you want to build a model
that's kind of realistically how the
brain works
you should tend towards in a lot of
cases you should tend towards factorized
distributions
so for example there's good evidence
that there's a factorized representation
of task phase
in pfc and mtl uh there's pretty good
evidence so
i mean the what versus where streams
in vision that's a factorized
representation
um so very
yeah so you're kind of using it in like
a coarse graining
sense to say sometimes you don't want to
even
allow for the all by all because it's
more categorical
how the task is being modeled anywhere
like fight or flight
you wouldn't want to have all
combinations of elbow and knee movements
you're fitting something that's kind of
at the wrong dimensionality
and so for a lot of reasons not the
least of which it seems like that's what
organisms would do would be at that high
dimensional manifold or the factorized
representation
yeah well and and in this case right i
mean just we have experimental
the experimental design is such that
they are they do know ahead of time what
the different possible combinations are
right so i mean they just they just
already know that there are these
combinations
um so it's it's consistent with their
beliefs about the generative model that
we have given them
via the instructions um so
um so so in this case
um you know we had a a pretty uh typical
you know sort of sort of model graphical
model with two parameters
we had our the beta here which
corresponds to the
expected for energy precision um here
you know just to be intuitive for the uh
clinical audience we were going for we
just called this decision uncertainty
um and then we had a and so that's just
this is again
this is the rate prior um or rate
parameter for a gamma distribution
uh over uh over this uh
gamma term um and uh
which again is a uh a thing that
modulates the
expected free energy estimate over
policies
um so it modulates this g thing um but
then the other parameter we had
was this uh emotion conflict parameter
which just said basically how much
they uh dislike the negative stimulus
how
aversive they expect the negative
stimulus to be um
and so you can kind of show in
simulation so each one of these uh
vertical bars here corresponds to
beliefs about
uh the what state you were in on the
runway um
so if beta equals one and uh
the um and uh the emotion conflict
equals one
then you should expect that if the you
know good thing is on the uh
oh it is okay and this is a this is a um
conflict plus
two points uh trial um so basically the
thing will
approach the reward even if it's going
to see something negative if vc is one
and it will do it deterministically
whereas if ec is three then it will
fairly deterministically
choose to go away from the negative
stimulus even if they would get
reward whereas if they have higher
values so more decision uncertainty than
this distribution becomes
they become a lot less confident in this
distribution and
end up choosing these kinds of values
that are more like in the middle
um and um
and uh the likelihood is is you know
pretty clear it's just in each trial
type
each of the different um each column
here is a different runway position
they will just generate the negative
stimulus with an increasing probability
as it goes left
and the positive stimulus with an
increasing probability as it goes right
um etc uh the only confusing thing here
is that
white means a higher probability in
these whereas block it means higher
probability here but
um but anyway so that's that's it and
just kind of
etc etc for the five trial types so
in this case what we found was if you
look at
healthy controls versus people with
depression and anxiety versus people
with substance use disorders
the emotion conflict is actually
interestingly higher
in healthy and lowest in substance use
disorder
whereas decision uncertainty is highest
in substance use disorder
and kind of medium and depression
anxiety and low
and healthy controls and these are
significantly different
and that's true in a propensity match
propensity match sample and in a
larger sample so this interesting thing
where
it might be more of a what might be more
clinically relevant as this kind of
uncertainty over options as opposed to
just
being more sensitive to negative stimuli
um right how would you say how would
that shape just kind of curious if
it doesn't have a if it's not known but
how would that shape
treatment or conversation or approach
in a given situation from whichever role
makes sense like to say oh it's not
actually
this psychological construct but it's
actually
related to something like this
um i mean in terms of like informing
treatment or something like that
sure like treatment via any modality
um yeah i mean so i mean typically the
the main source of things you might want
to do is you know either talking about
um
so say you know at baseline before
somebody starts treatment
what their beta value was right
it might be the case you'd have to study
to show this but it might be the case
that
given different beta values at baseline
you know
like people with high beta values might
respond well to cbt
cognitive behavioral therapy whereas
people with low beta values might
respond better to act or might respond
better to
an ssri or you know like something like
that
so either it's either it's something i
mean that's kind of the ideal thing is
you want to say
can i get this information and it will
give me information about how to treat a
person
um but there are lots of other things
you might do besides that but that's
that's like a primary kind of
you know like ultimate goal example yeah
it's interesting how there's probably a
lot to be
said and learned about the actual
application of active inference
clinically
but even here on the beginning of
applying it
we can use it as just a potential
biomarker
just like a summary statistic related to
a questionnaire
or some other thing that's estimated
from empirical clinical data
fitting a different kind of underlying
generative model so instead of doing a
regression oh people who have
higher on this end up doing better or
worse in this kind of a program
well now we can just do that same kind
of parameter
testing in the context of a different
type of model it's an active inference
generative model so i think that those
are just some points of contact but it's
really interesting stuff
yeah definitely i mean you can do lots
of other interesting things with these
right so this
this beta parameter if you remember from
previous sessions is what's associated
with
um it's proposed to be associated with
um
dopamine dynamics in uh
in the brain and i'll show you briefly a
a study
um an example study later which
where philip shorten back like i
mentioned before actually showed that
the
trial by trial updates in beta that are
predicted by the model
um were correlated with a bold signal
in fmri in
in the midbrain in a midbrain region
that's associated with dopamine
you know so whereas whereas the way that
we're doing this here we just have a
stable beta estimate for each person
but you might look at um say individual
differences between
contrast values in an fmri analysis at
the group level
um you know so like people with higher
beta values have higher
say uh basal ganglia
uh responses to reward versus no reward
or something like that
um so you could do that kind of thing as
well so both both individual level and
group level um
fmri sorts of approaches as well as
much fancier things but those are just
two kind of simple examples
[Music]
so as another example of doing this in
the in the domain of
kind of perception instead of decision
making um
you know we we used uh this is in the
context of a task
where a person is just told to uh push a
button every time they feel their
heartbeat
um and um so in this model uh
we don't even have like an explicit
policy selection part
um all we do is they start with a
precise belief that they're in this
start state at time one
and then they have prior beliefs about
whether or not
they're going to transition into a state
of feeling their heartbeat versus not so
probability of no heartbeat probably of
heartbeat
and those priors are encoded in this in
the
b matrix here the transition matrix
where sort of the higher the php is the
more they expect to feel a heartbeat you
know more often
right on each trial um
and um and then also there's a precision
value here which corresponds to
beliefs about how precise the actual
afferent signal is coming up
from the heart um and so we can estimate
this ip parameters intercept of
precision and this
prior over heartbeats um i should say we
also compared this to a model that
included learning
in this task and in this case the model
including learning didn't win
um and so what we found here is
and i should say also that they do this
task three times they do it once when
they're told they're allowed to guess
once when they're told they're not
allowed to guess and only to press it
when they're sure they felt something
and one where aside from in addition to
no guessing they're told to hold their
breath which kind of makes it
um on average easier uh to feel your
heartbeat
um and um so it kind of like amplifies
the afferent signal makes it more
precise
what we found was that in healthy people
the breath hold actually amplified into
receptive precision a lot
whereas in all the clinical groups
anxiety depression comorbid depression
anxiety eating disorders and substance
use disorders they just stayed flat
low intercepted precision values
so that the actual changing the
actual precision of the afferent signal
didn't have any effect on their beliefs
about the precision of the signal
um you know so it's something like like
a rigidity in the way that the brain
treats
uh afferent interceptive signals and
psychiatric disorders trans
diagnostically
uh and so again this is just a again
kind of a standard like mixed model sort
of analysis
um whereas if you compare say
estimates for prior expectations
everybody
um showed higher prior values in the
guessing condition
than in the other two conditions which
you would expect
but there were no differences between
healthy and clinical groups so it's kind
of interesting it says hey maybe this is
more a precision issue than it is a
prior expectation issue
in terms of clinical significance or
another task or another task has to be
explored
chris put in a plug how cool that paper
was i think there's
been a lot of conceptual work on
interception active inference and
there's been a lot of discussion about
whether it's priors or precision or
anything like that
um and to my knowledge i'm happy to be
corrected
about this by ryan but um that was the
first time that
it's really been tested empirically
right uh
yes there's no there's no other there's
no other
like actual formal fitting models to
data
um studies that have tried that before
nice epic work
there are there are papers that have
tested like more kind of like
quote-unquote qualitative or just kind
of like go up versus down sorts of
predictions that fall out of
computational models but
not actually fitting a model yes this is
the first model based analysis of this
kind of thing right
yeah and we've um and it's cool we've
actually replicated the results in
healthy controls in a second
uh sample now so it seems like the
effect at least the effect in healthies
is pretty robust
we haven't been able to replicate we
haven't tried to replicate the uh
the lack of uh of an effect
um in uh clinical populations yet but
that's kind of in the works
um cool so
so so anyway so this continues this
continues to go here
yeah but it should be i think it should
be almost done
pretty quick it only does six people i'm
surprised
an interception question and then one
question from the chat so what other
interceptive
methodologies might exist so you did a
heart rate
estimation task what other
interroceptive modalities might be
amenable to this kind of quantitative
analysis
um so definitely um definitely
cardiac interception tasks are
um are uh most common
just because it's it's actually quite
difficult the methodologies is it's
pretty difficult to
um you know use so for instance in
vision right you can like
very tightly control or in audition you
can really tightly control the timing
and magnitude
you know of like the of the the input
signal right whereas it's it's hard to
say
precisely control um changes in
the signals that you're getting from the
inside of your body um
so so it's um you know it's difficult at
least the heart
is a kind of like signal that has a rate
and um
and you kind of know precisely when it
sent the signal upward you know and
things like that so they're definitely
the most common there's lots of
different
ways that people do cardiac there's lots
of different cardiac
perception tasks a lot of them have come
under
a lot of recent criticism recently um
for various reasons
um there's been some studies that show
that
um for instance like standard uh what
are called heartbeat county tasks
where people are just kind of asked to
like over a period of a couple of
minutes
just count every time they feel the
heartbeat and you just kind of
look at how close their counts are to
the true number of heartbeats
um there's a there's a number of papers
including our paper actually that show
that this looks like it's primarily just
tracking
prior expectations um it doesn't it
doesn't tell you a lot about
you know what the the way that they're
actually treating individual signals
um and i mean in ours in ours we
actually showed this that um
that if you used a standard heartbeat
counting measure instead of the
heartbeat tapping
you know which was our primary measure
that we fed into the model um prior
expectations in the model
predicted the heartbeat counting uh
like accuracy values like 0.9 something
so so it was it was like a nice
confirmation that yeah this is
primarily about price
it points towards having a generative
model that can then be deployed and
modified and corroborated across
settings because then you could say well
what would be the task or what would be
the trial and set structure how many
participants would we need to resolve a
parametric difference of such and such
so statistical power down to a lot of
other features would be
influenced okay let me ask this question
from the chat
so that we do hold on i need to finish
that previous question
um so so but aside from cardiac stuff
there
are a number of other methods um
there's so one that i currently do in my
lab is something called i'm using like
breathing uh breathing
resistances so basically you can you
have these people wear this little kind
of
darth vader mask kind of thing and you
can change in really precise subtle ways
how is how much resistance there is when
they try to breathe in
um and you can um and you can get sort
of individual differences in sensitivity
you know where some people you know feel
uh
that change in like the how hard their
lungs are needing to work basically
um at different at different loads of
different resistances than
than others um and you can also use it
as kind of like an anxiety induction
which is how we use it to try to
you know precisely induce uncomfortable
intercepted states at different uh
intensities and see how that affects
things what about muscle there's also
sorry what what about muscular like how
heavy is this or how what angle is your
arm at
um i mean we don't consider that
interception that's more like
proprioception or
um or some other sensation um but
certainly i mean there's lots of tasks
like that out there
um the kind of thing that that you know
we mean by interception is things like
you know feeling what's going on in your
stomach feeling what's going on in your
you know your heart or your lungs or um
you know like various like
effects of hormone levels you know like
stuff going on
inside cool um so um i mean i should say
i can't talk too much about it
but we have actually developed a method
for
um precisely inducing inducing with
precise timing
um sensations in your stomach um and
we're currently just finishing up a
paper on this uh using that method with
eeg
um to test some predictions of the
neural process theory for uh
uh gastrointestinal intraoception so
that's another thing that's kind of
common looking forward
let me ask the second question if it's
okay yes
what are the similarities and
differences between the active inference
model
of emotional inference was how it was
phrased
and lisa feldman barrett's approach to
emotion construction so if you don't
know
once i i i just wanted i'm just reading
it off but um
[Music]
that's probably that's probably a
question for another time i mean for
people who are familiar with
you know my actual like simulation work
in this area i've
you know i and my group have published
multiple
active inference simulation papers
specifically about emotion
inference um and um
those uh models to the so i should say
it's not a straightforward question
because you could build
active inference models that are uh
that would do more or less something
constructionist
or you could build an active inference
model that does something
less constructionist so so it's it's
actually not as though
um active inference has something really
unique to say about
whether or not constructionist views of
emotion are right um
but um but the um but i should say that
the the most straightforward models
um that have to do with uh
constructionist views where where what
you're trying to do is
learn and infer emotion concepts um
those the most straightforward ways of
doing those are via the sort of
multimodal
inference inference process that
definitely has a kind of when those
mappings between
emotional concept like emotion state
concepts and um
lower level you know sorts of like uh
observations like for instance like
observing your arousal level you know
observing how negative or positive you
feel things like that treating those
lower level things as observations
um when the likelihood between those
and um emotion concept states at a
higher level when the mapping is in the
likelihood is uh
probabilistic then you end up having to
learn probabilistic mappings that look a
lot like
constructionist types of inference
stories
um but what's kind of less clear is is
that um
constructionist views say don't say very
much about
how the kind of states in your body are
generated in the first place
um you know say like you know if i see a
predator or something and i have
i have this big change in my heart rate
and like muscle tension and things like
that
um and then i feel that and i infer
construct
right some kind of belief about what
emotion that corresponds to in this
context
there's a you also need a story and an
active inference model for the
mechanisms that generate those responses
before you make sense of them
and you know we've we've talked about
doing things like that with active
inference models um and it's not
so clear whether or not something like
that would be consistent or inconsistent
with um
constructionist views um but uh but yeah
anyway
um so hopefully that helps the active
inference doesn't solve the
does it doesn't uh take sides
necessarily i guess that's my point
really interesting i didn't know about
that um
theory so it sounds like something where
we can use active inference
to construct various kinds of models so
all these orthogonal
models and we're like looking always at
the two by two on the active stream
is it going to work on this axis and
this axis which debates are
relevant which ones aren't for active
inference and the free energy principle
so you want to just carry on a little
bit yeah i mean so
i mean just to just to say i mean
because this this actually comes back
very well to the to the actual topic of
you know today's session um is that to
really solve these questions
what you need to do right is you need to
construct an active inference model
that looks very constructionist and an
active inference model that
doesn't look very constructionist and
see which one fits
empirical data better right so um
see it's more kind of a way of precisely
testing uh different you know
hypotheses of different models as
opposed to you know saying this model
must be correct theoretically
yeah i think it's kind of important to
when you're thinking about this kind of
stuff people often talk about like
active inference as a theory
and as we've said like multiple times
there are multiple process theories that
could fall out of this i think it's a
very general framework under which you
can build
multiple hopefully competing theories
um so yeah i mean and in addition with
computational psychiatry stuff
you could just use you could think
active inference is literally false
like as a theory but it would still be
you could still also
simultaneously think it's an awesome
individual differences all
like that would be an odd set of beliefs
to hold but there's no contradiction
there
yeah um yeah no
for sure uh yeah i mean this comes back
to the you know like
uh whether you think of models this kind
of model is getting to like the ground
truth versus just using it
you know instrumentally um but uh but
yes
um so okay so so last kind of thing here
is is that
um you know in addition to being able to
do standard you know sorts of like you
know again like anovas regressions you
know frequencies approaches or even
you know base factor analyses um
in place of or in addition to them um
one thing that's really nice about
getting parameter estimates the way
we've been talking about is you don't
just get um point estimates you don't
just get posterior means
which is you know what we've been
talking about you know with like
analyses like like that
right like this is just you know means
of posterior means
um whereas um
the active inference to the parameter
estimates in variational bays
also uh correspond to posterior also
have posterior variances
right so it's not just the mean but it's
also the confidence that the estimation
had around that mean um and so that's
actually additional information that's
useful
to incorporate when you're doing group
level analyses
and and
parametric empirical bays which is um
something that again
was initially developed and is primarily
used for dynamic causal modeling
um happens to work really well
um with the uh with the the setup for
getting parameter estimates
and for the way that we get parameter
estimates again like i said before
already uses dcm scripts um so you can
actually do
these parametric empirical bayes
approaches that are more or less
general linear models but that also use
the posterior variances
um to get kind of um probably the most
principled
you know way of doing you know like the
fully bayesian
um group level stuff that you know kind
of thing that you could do
with these individual level parameter
estimates incorporating both the means
and the variances
um and so uh i think this
is this thing done
okay this has got to be the last one
but uh but um anyway
uh i had there is a thing that i can i
can if it takes too long i do have saved
versions of this i just wanted to show
you
uh um i was hoping to be able to show
you the actual model comparison part
um but so you know as an example of
using parametric empirical bays
in this paper on substance use we did do
this
so in this model in this task it's
pretty simple
all people do is they just um repeatedly
choose option one two or three um
and on each one either a green ball
falls or a red ball falls
green all means green ball means a win
and in advance they don't know
which of the options has the highest
payout probability
so again it's explore exploit right so
you have to kind of try out different
ones until they become confident which
one's best and they kind of keep picking
it
and in this case we were able to
estimate a number of parameters
we estimated action precision um we
estimated
that risk seeking parameter that i
mentioned
um we estimated uh separate learning
rates
for um when they had a win versus when
they had a loss
um and we're also able to estimate this
kind of a information sensitivity
parameter
um it's probably too much to explain at
the moment but it's kind of like a
belief rigidity it's like an initial
how uh the higher it is the less you
should think you need to seek
information
um basically um
and what we were able to do with that is
um over here we did standard
kind of group differences and you could
see that action precision was a lot
lower in substance users
and um learning rates for uh
losses were uh lower um but we also did
the pebb version the parametric
empirical base version over here where
we could get these group level
uh effects that included the means and
the variances
and um and you could also see that these
effects
were were there and you could actually
show like the posterior probabilities
um and things like that um that were uh
again it's just a it's just a kind of
nicer thing to do that would give you
um that'll give you additional be able
you'll be able to incorporate additional
information and keep things fully within
a bayesian framework
um and um and so
if this thing is still are you done
uh i have another question we can ask if
you wanted to just let it run
on this all right so just curious
christopher said that he'll be using
this in his phd
so what is your phd project or i know
it's
starting the phd and everything but what
are you thinking about using it um
that's the first question and then
there'll be a follow-up part
um so i work in alex wolgar's lab
who's a pi at the mrc cognition brain
sciences unit and her lab studies
cognitive control
so i'm planning on doing a lot of work
on cognitive control
um at the moment the
so i don't really want to say too much
about what projects i have
yeah most because just what questions
are you curious about or what
do you think are exciting so mostly i'm
really curious about using
or using active inference to help us
think about
and formalize some otherwise kind of
less formal hypotheses in the realm of
cognitive control
and then using those kind of generate
some testable predictions
um cool although yeah one thing i should
say is like
i don't think the active inference is
always the best tool to answer all
questions you might have
depends on what level of analysis you're
working at i happen to be really
interested in like algorithmic level
questions where active inference is
really good
um if you're interested in
implementation level stuff this might
not be the best tool for you
great and so the second part of the
question was are there any
fep or active oriented supervisors at
cambridge but
if there's yes or no that one but more
generally i'd like to hear both of your
perspectives on like
let's say somebody were starting
research as a graduate student
in a lab that wasn't in this actual
line of research already so what would
you convey to a starting grad
student or starting researcher who was
looking for a phd mentor
or who wanted to do a research program
that was like aligned with a lab that
was studying something cool
and interesting but they wanted to take
an active inference perspective on it
um okay just so just so people know it
is now done yeah
yeah but but go ahead if you want to
answer that question quickly
um i was just gonna say i have a couple
things to say i think it just depends on
your personality really
uh are you the type of person who
doesn't mind doing a lot of things
alone and without much help in which
case you can do something
that you or other members of your group
aren't doing if that doesn't bother you
then go ahead
this tutorial is a great resource um
if you are working in a lab i i would
genuinely just try and find a lab that
studies what you're interested in
that's probably the good advice i mean
so one thing to say is like ryan is
i haven't signed the paperwork yet but
um he's going to be my associate
supervisor
so i do have someone in my like
supervision group who can actually help
me with this stuff and so i would always
say make sure whatever you're doing you
actually have people who can help you
great point and i wonder if in the
remote world
it will be easier to say i i remember it
was kind of a big thing to have
i didn't even have this but like
somebody who's a committee member from
another
university so now it might be a little
bit more possible to connect remotely
anyways
ryan i'd be curious to hear your
thoughts on that and then we can go back
to the model
um sorry i don't think i fully uh just
suggestion
a a starting researcher somebody who
asked to be in your lab but they were
you know there's not room for them in
your lab or they're in a different lab
already
but they want to do something with
research
in this area oh i say i see yeah i mean
so that's a very tricky question
i think i mean when you're deciding
where to go to grad school
i think it's really really important
that
you find somebody and that you're
confident you found somebody
um where you uh was a good match between
you and your
and your supervisor um you know i've
seen cases where people
start in labs and it's just a not a good
match between your supervisor's style
and your own style as a student um and
you know a lot of times that's a recipe
for either a really tough time getting
through grad school or even deciding
that maybe you don't want to be in
science anymore um i've seen
i've seen that personally you know like
the case with other people whereas if
you find somebody who
you know kind of matches your style
right in terms of like
how much direct micro management
supervision you want versus how much
independence you want
you know like having a supervisor that
really allows you to be creative and
come up with your own projects versus
someone who
you know would prefer that you're
working a lot a lot of stuff that's sort
of directly
um sort of more narrowly in line with
what the lab's already doing
um you know i mean all sorts of
supervisors
will have will have
you know types of grad students that
work well with them but
finding the right matches is really
really important
and part of that you know does also
correspond to common interests
um i mean if the question is you know i
absolutely cannot find somebody
who does what i want to do that is
really tough um
um but i would say in that case uh you
know what you were mentioning about um
you know kind of uh remote or uh
co-supervisor sorts of situations where
as long as you can get
your primary supervisor who's a decent
match to you in general
to be okay with you having some other
supervisor
um or mentor of some sort that will do
the sort of thing
that you want to be doing
methodologically and there's enough kind
of overlapping interest between
real you know primary mentor and
co-mentor then i think that can work
well
um you know in those cases but um but
if at all possible identifying a primary
supervisor who does that
the methods and is associated and has
the same interests um
is you know definitely the best option
if you can
um great advice but um
okay so all right so this is now done so
you can actually see what the script
does once it's done um
so you can see so what it will spit out
um
i i should say this is also a new
feature i just added this
to the uh to the to the tutorial script
to this main tutorial script so
if you go to the github and download the
newest version then it will generate
these
these uh scatter plots for you um but
um so it will show you for instance so
when we only did 16 trials right
then recoverability for learning rate
for the three parameter model wasn't
awesome right the correlation between
true and uh
estimated parameters was only 0.58
whereas for risk seeking the correlation
was 0.95 so super recoverable
and for alpha it was um
i don't know it's not showing up but it
was 0.42 so not
great um whereas for the two parameter
model
risk seeking was 0.95 and alpha
was 0.94 so i should say
depending on the values the r and p
values might not show up on those graphs
so i have it set up but it will print
them out for you here
so alpha recoverability 0.94 p equals
.046 etcetera
so it will give you all of that it'll
just spit that out for you
it will also tell you the average log
likelihood
under the two parameter model and the
average
action probabilities um of the two
parameter model and the same thing for
the three
so the fits are actually very similar
in terms of the log likelihoods and the
um
action probabilities and so
when you actually calculate the
protected exceedance probability
which it also will do for you pxp um
it will show that the um in this case
the um
the second model so the model with
learning has a
uh has a higher exceedance probability
than the first model
but this is actually not necessarily a
very clear winner here i mean what
you're hoping for is
something like one and zero or you know
point point eight point two point nine
point one
something like that um so um
and again this is just an example this
is not going to be reliable at all
because i did
16 trials right you know if you did a
real task if you just use the 32 trials
that i actually have in the
in the real code on the github um
it will be better than this but you know
most
actual behavioral tasks you know like
for computational modeling studies are
going to have
you know like 100 you know or more
trials um to really get kind of precise
estimates and and know how good these
models are actually doing
um so but um so
so that's the kind of thing that you get
here at the end so you'll get
so i should say this trajectory thing is
not that meaningful it's just showing
for the first and second parameter what
the trajectory of the change in the
parameters are
as it converges toward the posterior
values but when you have more than
two parameters it's not that informative
um so
so um you know we have in the paper
you know we have this figure that more
or less just kind of depicts
an example of what this kind of thing
looks like um
and more or less as long as this kind of
you know iterations converge and has
this kind of nice increasing
slopey thing to it then you're probably
fine but if you're doing this
and you find that through iterations it
kind of bounces up and then bounces way
back down and then bounces up and it
looks really kind of inconsistent does
have this nice kind of
slope to convergence that's usually a
telltale sign that you're running into
some local minima or you know
something's going wrong um in which case
you might want to like tweak your priors
and see if it works better or you might
that might tell you there's just
something wrong with your model
um so it's a good kind of diagnostic i i
just
would love to hear like sometimes it's
hard to grasp
how can it be converging downhill like
you
like when we were talking earlier about
the difference between sampling based
methods and the factorized methods
so there's obviously a world of
difference in the setup and in the
computation
but like how is it that just doing
something like minimizing free energy
does
take us to these acceptable parameter
ranges
if there's any sense that you have of
working so closely with it
um like what is it that that's what is
it about that accumulating bars
that leads us you know inevitably
seemingly at least
reasonably to an acceptable set of
parameters in a vast
space what is actually happening there
that somehow it doesn't converge into a
local minima
or you know which way you go it doesn't
converge in a local solution set
oh there's no there's no guarantee that
it doesn't do that
usually this could easily converge into
a local minimum that's not the global
minimum
um you know i mean all this is literally
all this is saying is that there's a
kind of
smooth you know like locally convex
right like gradient descent towards some
stable value
um but no i mean that could totally be a
local minimum there's nothing that that
stops it from being that it just means
that there's a kind of
clear slope it's not like a super kind
of like bumpy
weird you know parameter landscape but
then that we need to inject some layer
of sampling first with many starting
positions
in order to to get good meta conversions
because
it's not enough to look at one model
trace
and say like yep well this one converged
that model converged somewhere
and it settled in given a very complex
free energy
function but then we need to pull back
another level
right to get traces from many points in
the landscape
um well i mean that's just a that's just
another approach that is a potential
you know like not you know like trying
to
not testing out a bunch of different
prior values and seeing if everything
converges from a bunch of different
prior values to the same spot
um like yes it is a limitation because
this could represent a local minimum
but if it if it um stably converges
on um like different
reliable you know parameter estimates
for each person
you know which which corresponds to a
range of places in a landscape
then um then like those will be
stable individual differences you'll
probably get slightly different values
if you start your priors at a different
place
almost inevitably because the complexity
cost will be less if you don't have to
move as far
to find accurate parameters
but so long as you're getting
interesting variability and convergence
for each person
has a nice kind of slope like this then
um it's not like everybody
is is getting stuck in some particular
um you know single
well or attractor of some kind um
but again the question isn't necessarily
what the true one is per se it's
you know like can you find estimates
that you know provide
interesting individual differences given
a set of priors
um you know i mean it's it's it's
important to realize too and we
mentioned
mentioned this in the paper that um you
know typically
the model the model that will win the
model though have the best parameter
estimates
will typically be simpler than whatever
the true underlying generative process
was in the person that generated the
data because typically there are simpler
explanations
um than the ones that generate the ones
that actually generate
data in a complicated system like the
brain
you know so so you're not necessarily
treating this as though it's
the true one but if it gives you nice
convergence for each person
and you're getting nice individual
differences then it still is a it still
is a reasonable measure
of you know of individual of interesting
individual differences
um and if you can simultaneously do
things like
show that parameters parameter estimates
correlate with other things like um
so just you know i happen to have it up
um
you know so this is this you know eeg
ceg study that uh i'm uh in the process
of putting a paper together before
and we have parameter estimates here um
for intraoceptive precision um in that
gastrointestinal task
task i mentioned now precision here
correlates with reaction times
negative point point negative 0.74
despite the fact that the model is not
fit to reaction times
um and it's a direct prediction of the
neural process theory
that as interrupts you know higher
interceptive precision
should mean faster evidence accumulation
which should mean
faster convergence time which should
mean shorter reaction times
right so you know if you have you know
so you can separately validate that your
parameter estimates are tracking what
you want them to be
by seeing what they correlate with um
you know
in a way that they ought to correlate
with for construct validity for things
that didn't get fed into the model
um you know so there's there's lots of
ways of doing this um
um but but you're right i mean if you
using other approaches that use multiple
seeds the kind of like the monte carlo
stuff that you were talking about before
that is another approach and um you
might be more likely to
um you know find like a global
minimum um but uh but again they're just
they're just different approaches
there's just a quick plug so i think the
model that's kind of most closely
related to active inference and is
actually fittable
fitted can be fitted to data is probably
the hierarchical gaussian filter
um and i think they're actually gen at
the moment
it's estimated the parameters of the
rest made they're using variational base
but as i understand that they're also i
don't know if they have developed it or
are still developing
but they're also developing monte carlo
markov chain version
um very exciting yeah this is all just
yeah so so okay so last thing here
just uh just to um to you know to kind
of
you know wrap up everything so at least
people know
what um know what's available you know
for them to kind of expand on this in
our example code that we've
um you know set up is um
so down here uh when we actually do the
um where is this
uh so this this right here
is the function for doing model
comparison
so spm underscore bms bayesian model
selection
you just feed in the free energies for
each person
so for instance if you um
you know if i just uh
if i so i just it will just store these
right so for instance
four um so these
are the negative free energies for
um my six simulated people for their
best fit models
um best fit parameters uh for the two
parameter model
whereas that's it for the three
parameter model
and um and so
bayesian model comparison is just
um just feeding you just feeding both of
those vectors
into column vectors into that function
and it will spit out the expect expected
or predicted exceedance probability for
you as well as a number of other sort of
diagnostic checks and you can um
read uh there's good papers um like
class stuff on
and um anyway we we reference them and
they we cite them in the paper
that describe this in detail if you go
into
the actual uh you know function itself
it also
will tell you exactly what the inputs
are and exactly what the outputs
mean right so alpha is just a vector of
the model probabilities
again xp is the exceedance probabilities
before doing the
protected part and so forth
so once that's all done
and i should say i'm not going through
every kind of line in this but
we commented it you know as well as we
could and we hope it's
we hope it's clear as you go through you
know what we're doing um but it also
will spit out
right cleanly into the into you know the
main
uh terminal here what uh you know what
the outputs are
um so if you wanna you can kind of
hopefully adapt
this code for your own purposes to do
recoverability and
um do model estimation and stuff like
that um
but once you've done that um
then you can do i was just going to show
you briefly
the um the hierarchical base the
peb um stuff and for that we put things
into
these gcm structures so gcm for model 2
gcm for model 3
and you can just pick which one
here that you want that you want to use
right whether you want to do peb on the
two parameter model outputs or the three
parameter model outputs
um and this just sets a bunch of
defaults in peb you shouldn't have to
mess with any of those
but if you but if you run it so i've so
what i've done is in the glm and the
general linear model for peb
i've just set the mean value across
subjects i've put a
uh regressor for group so this is saying
compare groups
um and then i've put in this sort of
fake age variable
just with random numbers basically so
if i run this section on the three
parameter model
then i'll get you know it'll do this
kind of estimation thing
and it will spit out a bunch of things
um and basically the way
to read this is um
ignore that so this one just ignore
uh when it spits it out this one will
tell you
um for instance this is saying like four
uh so this one is probably the best one
um so these are the reduced models
so the best model um removing the
parameters
uh parameter differences that um didn't
matter didn't win in bayesian model
comparison um so this is saying
parameter two and parameter three
were different between groups
and were and remain different between
groups and the best fit model
and again we we explained this all in
more detail in the paper
you can really ignore these ones at the
bottom
in the in the figure uh in the paper we
show you
which ones are um which ones matter
to look at such as these more or less
those top three
so the you know the estimated
differences and the estimated
differences that survive model
comparison
so kind of pruning away the parameters
that don't stick around in the best bit
model
um so in this one this is just gonna say
what the pink bars are
because to me it wasn't immediately that
they're the they're just the variances
they're just the variances and the
posterior estimates um
um so so uh so yeah so i mean for
instance
so you'd expect right this one has a
really high variance you you might
expect this one wouldn't survive
um you know as a winner in the in the
reduced model um
but even even this isn't probably the
most
useful the most useful um is the actual
like peb review parameter
gui um see so this is the actual
glm so this is just saying the mean the
group difference so this grape light
gray versus dark gray because the first
three subjects are a group
second three are a group this third
column is just the randomly generated
age values
um so you can just say for instance
you know which of these which of the
means are different well the means for
one and two are different
um you know so there's a main effects
essentially of those two
um you could go to group and
you could say okay these are the two
that are different
but you can put a threshold on it right
so weak evidence you know posterior
probability has to be above
you know some ever some value for
positive evidence
right so if i make it if i give it a
higher it has to there has to be decent
evidence for it then only the second
parameter here is the one that actually
has good evidence for a group difference
um you know for example so you can
you know but if i make it required to
have very strong evidence
so posterior probability greater than
0.99 then the whole thing gets removed
um so so this is a nice and you can you
know just do it in terms of free energy
or just in terms of
probability that a parameter is greater
than zero
you know so there's different ways to uh
different ways to do it but so this is
actually probably the nicest thing for
navigating
the the results of peb that will matter
if you're doing group analyses using it
um so
um so that um so that is
pebb um and um yeah i'm trying to think
if there's
anything um anything else really
um because that's i mean that's
primarily where where things end so i
mean at that point you should be able to
um should be able to do
everything um i guess the
yeah i mean i was gonna briefly i did
skip over this just the
this was the thing i mentioned that
philip um did where he was able to
do kind of like within trial by trial um
model predictions as opposed to these
just group differences and show the
trial by trial the
beta updates um correlated with this
midbrain
dopamine area but um but yeah i mean
really i mean that's more or less um the
steps you need to know
right so so what we talked about was you
have to have participants
perform the task you build one or more
models we did two
find the parameter values in each model
to best reproduce uh the data
right the behavior we did that we did
model comparison
we used the correlations between true
and generative parameter are
generated in generative and estimated
parameters
to make sure the winning model was
identifiable
and then you could do either normal
group level frequency statistics or
something like pep
to test for a between group or just
uh yeah group level um
you know between subjects sorts of
analyses on parameters at the end of the
day
um so i think i think that um
yeah i think that really covers um most
of the
you know kind of meat of it i mean the
only oh okay
sorry one other thing that i do need to
show you um
is that the um to actually
do the parameter estimation um
that calls where is it um
that calls this estimate parameter
script which is one that we also
included
so if you open that just right click it
and say open
um then this is where you set your prior
means and variances
so here so it says here we specify prior
expectations for parameter means and
variances right so we say that um
so this is where so in this case i just
set the same prior variance for all the
parameters you know one over four
you don't have to do that but so here
you can think about it as the smaller
the value you put here the greater the
complexity penalty that you're
adding right so the smaller that is the
more you're going to prevent overfitting
um but if you make it too tight then
then the posterior estimates probably
won't be that accurate
so so in this case what you can see that
we've done is
um so if you're estimating alpha so
action precision
then this is where you'd put the prior
so we put a prior here of 16
um we log it here
i'm just so it's in log space um and
that just makes it so during estimation
um it doesn't allow that number to ever
become
a negative value um so it keeps it it
needs to stay
a positive value during estimation if if
estimation ever tried to test out a
negative value for that parameter then
the thing would break
um same thing if if we were doing beta
so that would be
um which we didn't try here but i just
like we include it if you want
to so this would be the policy expected
free energy precision
so there the prior is one and again
we're just keeping the prior variance
um equal to one-fourth you know up there
for everybody
this is the loss of version which we
didn't include
um but is in there if you want to that's
the risk seeking parameter and we gave
it a prior of five
and then eta the learning rate this has
to be
not just any positive value it has to be
a value between 0 and 1
which means that you have to put it into
logic space as opposed to log space
and that just means that to set the
prior you have to make that
whatever your prior is and then also
put that same number here um so in this
case we've
given it a prior for learning rate of
0.5 which is just kind of halfway
between zero and one so it's just kind
of middle of the road
you know which you know would make sense
in a lot of cases
um and then more or less this function
down here
just turns those back into their normal
values so it exponentiates
the um the log values
um you know and so forth um so it just
brings them back
re-transforms them um
and uh this is just where we
um for technical reasons this is where
we set what the uh
what the values are for risk seeking
um and uh and then this is the actual
log likelihood
so it will just for each trial it will
add the log likelihood so the
mdp.p here is the probability of each
action
um that it will show that just as in the
mdp structure
which again we showed last time in in
other
sessions and in the actual um we have a
table
in the um table three i think in the
tutorial that says what each mdp field
is so it just takes those and just adds
them just logs them and it just adds
them
up um across trials to get the total
probability
and then the the less negative this is
at the end the better
the the um the better the the better the
fit is
um so it's important to know about this
one just because this is where you would
change your prior means and your prior
variances um
so so um so yeah and then
and then uh this for instance this dcm
field thing it's just set up so that
you would just enter the name of
whichever parameters you want to
estimate for that model so here if you
put an alpha in rs it'll estimate
alpha and rs but you could also add you
know eta here
right if you wanted to you could add
that then it would also estimate
anyway i mean i'm sure there's other
little things in the in the code here
that could be explained in more detail
but
um you know this this hopefully will be
enough to to get
people going well thanks so much
ryan and christopher this was really an
awesome series it was our first
model stream and it was really just a
great learning experience for all of us
so i'm going to give some final comments
from the chat so
uh someone wrote thanks for the authors
continuous
updating of the paper it will be great
if these uh slides as
in their current version are somehow
made available at the end of the episode
so maybe like you mentioned
doing a supplemental file or something
for the paper
so that was one thing
for these just for these slides i like
to put them maybe so someone could say
oh that was slide 87
at hour three of this thing and then we
could just have this version
so that people could know where that
figure was because i know that they're
probably in other places or just copied
over but
that would be one is that
like i mean i guess i can imagine i
could imagine
putting together a powerpoint that just
kind of you know kind of concatenates
all of the slides that we've gone
through over these over these sessions
the vast majority of them will be
just the same as the figures in the
tutorial itself
but the best the best i could do
probably is to
put that as a supplemental file um in
the um
for the supplement or the supplementary
materials on the psy archive
uh version um that's probably that's
probably the only thing we could
imagine doing we could have a first um
page on the pdf or something that just
says here's a link to the these streams
as this version so that'll be one thing
and then a related question
was um just that future people wanted
future tutorials and model streams
so either both of you it's an open
invitation to just come on whenever the
time is right
and talk about any kind of modeling or
all these other cool ideas we've been
bringing up
so i mean i'm happy to continue this um
you know in a more kind of
yeah on the fly you know way as people
request things i mean but
but at this point i mean i would i would
probably need
um or we would probably need um any kind
of requests
right like what is it that people want
to cover because i mean now we've kind
of gone through
the tutorial start to finish at least in
broad strokes
um so i would need to know at that point
what
you know from now forward i need to know
what else people would want us to cover
because you know we've gone through most
of it
cool well this tutorial definitely took
us to kind of the brink
of all of these papers i maybe it'd be
interesting to
walk through a paper like a tutorial of
the paper especially this enteroceptive
one like
how would we adapt that for other do
kind of a walk through that'd be one
thought or we could go into the
formalism side we could invite a
colleague
or collaborator who came from a
different perspective more on the
analytical
more from some other dimension that
we're
that we are just also all learning about
yeah i mean i should say i mean there's
certainly a lot of areas of like the
broader kind of free energy literature
free energy principle literature that
we're
totally not covering here intentionally
right like our focus is this is what you
need to know
to build models and use them
experimentally
right so you know for instance there's a
lot of other stuff in
for instance like the physics
formulation for
for you know that also gets called right
part of active inference
um or the free energy principle more
broadly that includes things like for
instance like
um carl fristan's kind of variant on
talking about markov blankets
um you know or i mean there's a lot of
stuff on them like uh non-equilibrium
steady states
right and how that how that can be
talked about in terms of um
uh minimizing variational free energy
but also a lot of the physics
um you know like thermodynamic right
like free energy and things like that
also come in and um
that stuff's quite a bit more
theoretical and um um
it's certainly interesting but it's not
uh
not things that you need to know or all
that directly relevant to actually
build models and do the stuff in
practice so um
yeah there's other places other places
to look to that can they get that kind
of stuff i guess this is what i'm
pointing out as ours
this is not true completely
comprehensive of look it's called the
active inference or at least free energy
principle there sure
so any other final thoughts from either
of you
no i'm just been really fun thank you
yay great well it was really fun same
yeah and like i said i mean if if people
want to like
you know like go through get walked
through specific
you know papers either like you know
simulation either some of like our
simulation papers or empirical papers in
more detail
um so they could get a sense of how they
would do that in practice i'm happy to
do that
um but um i guess that's something that
we can just kind of
uh determine at a later date nice so we
will
wait for somebody to stimulate
us to do a walkthrough on a certain
topic or on a certain
um with a certain distribution of people
we'll figure it out but we'll um
we'll figure it out then so really
thanks again both
i'm gonna finish the live stream so
peace out everyone thanks for watching
activeinference.org
thanks so much ryan smith christopher
white
