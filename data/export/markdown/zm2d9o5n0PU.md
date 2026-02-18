---
title: "2nd Applied Active Inference Symposium on "Robotics" ~ 1st session"
category: "Applied Active Inference Symposium"
series: "2022 Symposium on Robotics"
speakers:
  - "1st session"
duration: "3:43:33"
url: "https://www.youtube.com/watch?v=zm2d9o5n0PU"
views: 700
exported_at: "2026-02-18T22:37:37.963103+00:00"
format: markdown
---

# 2nd Applied Active Inference Symposium on "Robotics" ~ 1st session

[Music]
hello and welcome everyone to the second
applied active inference symposium
hosted by the active inference institute
it is july 31st 2022
and this is the first session of the
symposium
the focus of the symposium will be
robotics and the presentations will be
centered around that theme
if you have ideas for future symposium
topics and want to participate in
organizing please reach out to us for
those of you watching live please post
questions in the chat and we will ask
the presenters during the roundtable
discussion
this symposium will be recorded
transcribed and archived for lasting
access we will make the playlist
available for asynchronous participation
if you would like to participate in the
transcription of the video please reach
out to us at activeinference
gmail.com
we will have five presenters followed by
a roundtable discussion
the presenters in the first block are
going to be tim schneider
presenting active inference for robotic
manipulation
with
co-authors let's see
sorry oh i don't have any listed here
um okay and then
next
let's see next is tim
verbellen um
and he is presenting robotics modeling
the world from pixels using deep active
inference
also no co-authors listed
and
then next will be
next will be ben white with artificial
empathy active inference and collective
intelligence and he has co-authors
mark miller and daphne
damascus
demacos sorry if i got that wrong
and after that
we will have a talk by noor sajid
learning agent preferences
and
let's see
her
are
ah there she is
oh she doesn't have any listed here
either
and then finally we have one hua chen
with the talk called dual control for
exploitation and exploration and its
applications in robotic autonomous
search
and that's it so
with pleasure i introduce tim schneider
uh please take it away
yeah thanks a lot for the introduction
i'm just
quickly going
to share my screen i hope you can see
that all right
yeah
so my name is tim schneider and today i
want to talk about our work on active
influence for robotic manipulation
[Music]
so i think we can all agree that
manipulation
so there's some noise on the background
sorry yeah it never went i think we can
all agree that uh manipulation is one of
these central abilities that we need in
our everyday life like be it cooking
writing or using tools and you can
obviously think of a variety of other
tasks that also require dexterous
manipulation
however despite
this significance
of manipulation in our everyday lives
robotic manipulation is still a largely
unsolved topic
and
i think one of the main reasons for this
is that
usually in classic robotics how we did
it for years we always assume that
everything is kind of known that we know
where everything is
how everything behaves
but in unstructured environments this is
usually not the case
and so what we need
is very adaptive policies that are able
to react to changes in the environment
and are robust to
to all kind of
perturbations
so
what my lab focuses on or at least
in part focuses on
is applying reinforcement learning to
robotic manipulation so learn these
skills instead of programming them by
hand
however this is also not super
straightforward in manipulation
and one of the central challenges here
is
to
to perform the exploration so in
reinforcement learning we always have to
explore a task before we can complete it
like for example here in this task um
this robot has to move up this little
ball into a target zone on this tilted
table and what we usually do and what is
done here is that we just apply some
random actions in the beginning and also
throughout the the entire optimization
procedure
and we just hope that this will give us
some useful insight into how the world
actually behaves and how we can create
a high reward in these settings
but i think in manipulation this is
usually not the case because if we just
apply random noise we end up dropping
the objects we are trying to manipulate
we end up maybe destroying even parts of
the environment
so i think this approach is simply not
feasible
for interacting with the real world in
manipulation
and if we look at how humans explore the
world we see a very different picture um
so this is a toddler that has obviously
the task of building the highest
possible tower of these other piece
blocks
and what we can see is that this toddler
is not simply applying some random noisy
actions
this kit has actually a fairly directed
way of exploring it has an idea of what
is useful to learn
what might bring it forward or maybe
maybe this is not as planned but more of
an intuition but
but certainly this exploration is much
smarter than what we are currently doing
in reinforcement learning
and so to summarize this
exploration is a very challenging task
in reinforcement learning for
manipulation
humans if we take them as an example
explore very actively and in a very
directed fashion and the question that
we want to ask in this in this work is
can we do this with robots too
and so this is where we started looking
into cognitive science and also came
across active inference
mainly because it uh it proposes a way
well it proposes a theory of explaining
curiosity in intelligent beings and the
question was whether we can translate
this on onto robots
so i just for completeness i want to
quickly go over the basics so in active
inference we assume that every agent
maintains some kind of model of the
world
which consists of observations o
hidden states x that the agent cannot
observe and some
actions or policy pi
and the objective is to minimize the
price which is the negative log
likelihood of the marginal observation
probability
under the model of the agent
and it has the agent has two ways of
doing this the first one is inference so
understanding the causes of the
observations it is making
this is done by applying variation
inference
to compute an upper bound of this
objective which is called variational
free energy
and then we minimize this which
corresponds to finding a variational
posterior
for hidden states given the observations
we are currently making
and the other avenue
which is what got us interested in the
topic is um the selection of actions in
order to minimize this free energy
objective
uh so if we want to do this we have to
make sure that we kind of plan ahead so
we have to take an expectation
of future states we might encounter
given that we choose some form of action
and we take this expectation of this
free energy term and what we get out is
fairly interesting namely
we get this kind of formulation here
which decomposes into an expected
information game term and an extrinsic
term
and the way this expected information
gain term works or what it
what it encourages is to take
informative actions because this term
becomes maximal when we take an action
which causes us to learn as much as
possible about
the current latent state of the world
so for example if you're in a very dark
room
a very informative action would be to
turn the light on it's not immediately
goal directed or anything but
it will at least tell you where you are
what your surroundings look like and
and so on
and then the second term is this
extrinsic term and here the agent
maintains a
preference distribution over
observations this is a bit of an
unorthodox thing for me as a
reinforcement learning person
we usually simply define a reward but
here this extrinsic preference is
defined in terms of
of this target observation distribution
but this is also exactly the point where
we can inject a target behavior into the
agent by basically saying okay this
agent should
prefer to observe some specific
observation
now taking a step back and going to the
reinforcement learning part of this talk
again
so the problem statement that we are
looking at is a
finite horizon mdp
which means that there are states
actions and rewards
we assume that these states fully encode
the entire state of the environment so
this is there's no hidden state in the
environment
and the objective of the agent is to
maximize its expected return for one
episode
and it's
the challenge here is that
the
dynamics and the reward distribution so
these two distributions here are
completely unknown um so the only way
the agent has to figure those out is to
probe the environment with different
actions
observe the outcomes and then learn some
kind of
model out of this
i mean obviously there are also other
ways of doing this this model doesn't
have to be learned but in our case it
will be learned
now we can see reinforcement learning
through the lens of active inference i
just wrote down this mvp again from the
previous slide here
the first thing we need is to define the
internal model of the agent and we do
this in a way that we say okay there's
two models the agent maintains one is a
model of the dynamics and one a model of
the reward distribution
and both of them are modeled as gaussian
distributions
conditioned on on neural networks so
these are neural networks theta being
the neural network parameters
and this
introduces a
latent state now into the environment
namely the
neural network parameters so
um what was
x before in in the inactive inference is
now here theta the only thing that the
agent cannot directly observe which is
what are the optimal parameters that
describe what is currently going on in
the environment what the agent is
currently observing
and the second thing we have to do is to
we have to make the agent desire a high
reward um and we do this here by making
the reward part of the observation
so now it's observing the the
environment state and the reward and
then we are setting this um desired
distribution in a way that
it prefers high rewards namely by
setting it to the exponential of
a scaling factor of beta times the
reward at time step t
and if we do this
we end up
the with the following planning
objectives so this is the expected free
energy now but uh
everything puts into its place
um and so the planning objective of the
agent is now according uh to the
expected free energy to maximize this
objective here
which consists for one of the extrinsic
reward which is just the sum of rewards
the agent expects to encounter by taking
some policy pi
and then there's also this intrinsic
term again
which in this case here becomes the
mutual formation between the neural
network parameters theta
and the observation the agent is making
so ideally the agent wants to make
observations that are both
good in terms of reward but also have a
lot of information about what the ideal
model parameters are going to be
uh i just said that
exactly and now we can do the use this
to forge an algorithm out of that
and it it works like this so
we take
so in every episode we start by
resetting the agent to some initial
state
and then in every step we have to solve
this planning objective of selecting
a sequence of actions
that minimize the objective function i
showed here in the previous slide
we execute this action obtain a new
state and reward we store all of that in
the replay buffer and then after the
entire episode is done
[Music]
we use this data in the replay buffer to
perform the infrared step of
of learning our models and adapting them
to the data we saw
now the challenging part about
about this is to perform this
optimization here and the first
challenge here is already to compute
this term even for for any given action
so computing
the expected reward for for a given
action is
has been done before in many works and
usually here monte carlo methods are
used so um just explain estimating this
expectation via monte carlo
but this intrinsic term which is the
mutual information
is known to be fairly hard to compute
and so there have been a variety of
methods proposed to
to compute or to approximate mutual
information many of them rely on
variational inference or amortization
but the issue is that we would have to
do variation inference over
[Music]
over the model parameter theta which is
a fairly high dimensional vector and
also we have to do this
potentially thousands of times in real
time while we are
yeah while we're optimizing this
function here
and so this is simply too expensive to
do anything fancy like that
so what we are left with is a nested
monte carlo approximation
and nested because we have an
expectation of a curl divergence
this means we have an outer expectation
and an inner expectation
and we
we apply monte carlo for both of them
and
the good thing about this is first of
all it's very fast and it allows us to
represent p of theta by a set of
particles because we just we now only
need samples so we can also
just
keep these samples and treat the entire
model as an ensemble
but the disadvantage is that
we require quite a lot of samples of
data in order to to get anything done
here
because um we have this outer and inner
loop for every sample that we draw from
for this outer estimator here for every
example
of theta we need to have
nj samples of this inner estimator here
of theta again and this means you can
quickly calculate if we take
five samples on this outer estimator and
five on the inner estimator
we already end up with 30 samples of
theta so we have in like a yeah and
a quadratic growth in in samples that we
need in order to compute the sum is this
this
mutual information approximation here
and what is also important to note is
that each of these samples is a full
neural network that needs to be trained
and maintained so this is simply going
to be very very expensive very quick
and so what we propose to do instead is
something that is a bit illegal in terms
of math
or at least it will lose us a lot of
formal guarantees
and that is to use the same samples on
the outer estimator as we used in the
inter inner estimator uh vice versa so
to use in the inner estimator the same
samples of the outer estimator that
means we draw a bunch of samples once
and then um we use all of these samples
except the one we just now used in the
outer estimator to perform this inner
estimation
and again as i said we lose some formal
guarantees because what usually is
assumed is that
these samples are iad this is not the
case anymore right now
but we found empirically that this
actually improves sample efficiency
a lot
so i mean here you see a little
comparison we did on a
discrete
like a randomly generated discrete
probability distribution where we could
compute mutual information uh
accurately
and
here you see a plot of the error of this
sample reusing estimator the second one
compared to the vanilla estimator that
doesn't reuse samples and this is over
the number of samples so the sample
efficiency is actually much higher
even though we are losing these formal
guarantees here
now
this means we now know how to
approximate or get like at least some
approximation of this
of this objective but what is still
unclear is how do we actually
maximize this objective
like what kind of optimization algorithm
we are using
and the first thing we tried here was to
simply use
a vanilla cross entropy method
this is a fairly common choice in
robotics to
to use this method because it's very
robust and
doesn't require gradients in anything
and it's also
considerably fast
it works in a way that you
initialize some some gaussian parameters
um so you you always maintain this
gaussian distribution of your current
action distribution you initialize it to
mean zero and one variance
then you sample a bunch of action
trajectories from this distribution for
each of these you evaluate the reward
and then you collect the end samples
that have the highest reward
and for those you fit
the parameters of the current gaussian
distribution you have over
over actions
in order to yeah to gradually shift this
distribution towards areas of f that
have a high reward and if you iterate
this for a while you usually end up with
a fairly
fairly good plan
now the issue is that this applying this
delivers fairly poor results
and the reason for this we quickly found
is something that is called
detachment or has been called detachment
in prior work i should say i don't think
this is an established uh term yet
um and the problem works a bit like this
so
consider you are in this completely
reward free environment right the only
thing that there is is intrinsic reward
like that leaves you out to explore this
environment
and you start in the middle here of this
maze and you can either go left or right
and in green is everything that is uh
intrinsic reward so everything that is
not explored has a lot of intrinsic
reward left
and so your agent decides maybe to go
for the left side first it explores it
for a while but at some point decides
that now the more immediate intrinsic
reward is towards the right side right
because this part has been explored now
so on the right side it's easier to get
intrinsic reward
so it might switch over to exploring the
right side first and remember this is
distorted episodic
so
after a couple of steps this agent
always gets reset to the middle and has
to do this over again
and so at some point the writers may be
completely explored or
whatever and
now we are in a bit of a tricky
situation because
we're again starting in the middle
but
the entire right set is explored and the
left side is so much explored that in
the immediate vicinity of this state
there is actually no intrinsic reward
left
and because many planners and
many planners that work well on high
dimensional problems rely on very local
optimization
we found that um
that these planners are unable to find
now a trajectory that leads all the way
into this
into this zone with high intrinsic
reward on the left
and the reason simply being that in
cross entropy method in order to reach
this zone you would have to randomly
sample a complete trajectory that goes
all the way around this maze and ends up
somewhere here in the middle or like at
least somewhere close to the border of
of the intrinsic reward here and this is
usually not happening
the solution for this we found
is to realize first of all that the only
reason there is no intrinsic robot left
in this area here is because we already
explored it so at some point in the past
we must have taken a trajectory that led
us all the way around towards the border
here and stopped somewhere here and so
what we can do is we can simply remember
all the past trajectories we took
and use those as an initialization for
the cross entropy method to start off
the planning from
so the way this looks like is that in
the end instead of simply returning the
plan
we store the entire plan together with
the current state in a memory buffer
and then when we plan for the next time
when we start the planning we not only
sample from this initial distribution
we also sampled from this memory buffer
take into account all the previous plans
we had
and start optimizing those as well
and we found that this usually leads to
behavior that is very well able to
escape this area of low intrinsic reward
yeah and that brings me to the
experiments we did
so this is a task we designed to be
specifically hard to explore
so the task is as i said before to move
this ball into this target zone the
tricky thing is that first of all the
table is tilted
if the robot loses the ball it ends up
somewhere here in the bottom and it
cannot be recovered anymore so the robot
has to wait for the end of the episode
to continue exploring
and also the reward is completely sparse
meaning the reward is zero everywhere
except for
if the ball is in this target zone
and this means that the robot has to
explore this entire environment purely
based on intrinsic reward and without
any extrinsic signal in the beginning
until it discovers this reward for the
first time
so if we apply just like as i told you
before this classical technique and
reinforcement learning of just applying
some random noise we can see that the
ball gets dropped immediately every time
and even after like 5 000 episodes will
soon see
we are not able to
reach even one third of this table so
here on the right is a histogram of
positions the ball has visited so far
and we are completely unable to leave
the start of this table
however if we use our method we can see
that we actually
explore this environment in a very
systematic manner and achieve a very
good state coverage
or at least ball position coverage and
our agent is quickly able to find this
reward here and
find a strategy that consistently pushes
it into the right location
this is also reflected in a learning
curve here's a comparison with a bunch
of baseline methods we ran one is pets
which is just a model based
reinforcement learning algorithm there's
also suck and mbpo
and neither of these methods manage to
to find the reward
in the given time
uh so we wrapped it up a little bit made
it this task a little bit harder so what
you see here are um
are sorry holes in this uh in this table
so now this becomes amazed there's still
no uh no extrinsic reward in the lower
area and also up until here um
so that means that again based purely on
intrinsic report the agent has to learn
to maneuver this wall like this is a
fairly tricky task right to maneuver
this ball around the corners of
of this maze into the target location
um and although it takes a bit long i
longer to train here obviously because
this task is much much harder oh it's
also important to know once the ball is
inside of this hole is lost and it
cannot be recovered
so
although this is much harder and it
takes a bit longer you can see that our
method is able to to solve this problem
and push the ball
into the target location
at the end
so this is a bit
of a slower version of of this policy
and you can see that it is actually
fairly tricky to maneuver around these
corners
there's a learning curve here
unsurprisingly the baselines did not
manage to solve this task but i mean
this expected since it's harder than the
previous one
and finally we also evaluate our system
or our algorithm on the real system uh
so we built this actually in reality
and trained it from scratch
so there's no transfer going on no
pre-training and simulation or anything
and you can see here the behavior is
similar the agent starts exploring the
environment more and more pushing the
ball systematically around
and uh ultimately um discovering the
reward on the top of the table and then
finding
a consistent strategy of moving it up
there's a learning curve for this as
well
but yeah this brings me to my conclusion
so we presented an algorithm based on
active inference
that is able to solve very challenging
sparse reward manipulation tasks
and at the core lies this augmented cost
function that is derived from
the expected free energy and this one
like encourages the agent to perform
very directed exploration while also
maximizing reward
and
we demonstrate that this method works
not only in simulation but also on a
real system
and so to give you a bit of an outlook
uh i think what
is very important to note is that if we
compare to to human haptic exploration
we humans rely very heavily on tactile
sensing for all of this exploration we
have developed a variety of different
strategies for
for actively perceiving using tactile
sensing for example like rubbing an
object to figure out the texture
or what you can see soon in this video
like grabbing it with our full hand in
order to to figure out the shape
can measure temperature there's all kind
of stuff we can perceive actively from
objects using tactile sensing
and
tactile sensing is also something that
is being actively researched in
in the robotics community there have
been a variety of new tactile sensors
coming out lately one of them is the
so-called digit sensor
you can see it here and it works in a
way that it has a gel that deforms upon
contact with something there's a camera
in the back and some leds
and if there's some contact you can see
the deformation of the gel in the camera
which is giving you some kind of like
local tactile feedback
and i think it would be very interesting
to see what we can achieve with active
inference on
using tactile sensors although there is
a variety of challenges that need to be
solved i mean this is a high dimensional
image
the contact dynamics are much more
complicated and
yeah there's a lot to consider but i
think this would be a very
very interesting avenue for future
research
and yeah this also brings me to the end
of my talk i want to thank you a lot for
your attention
i want to thank my collaborators as well
boris georgia hani and jan peters
if you want you can check out our paper
here under this
qr code there is also a project page
which will soon contain an extended
version of this paper that has been
accepted to iros
but i haven't
uploaded it yet so i will do this within
the next one or two weeks
so if you're interested in more details
i recommend you to check this out but
again it's not up yet
and yeah there's my contact details in
case you have any more questions
so um
yeah
if i got that correctly before we do the
questions afterwards in the round table
is that correct
correct thank you very much tim
you may exit and re-enter the stream
when we
go to the round table
okay thank you very much
and there will be just a few seconds of
a break
and then we will be going to the next
talk which is tim verbellen robots
modeling the world from pixels using
deep active inference so we'll be right
back
hello
[Music]
all right here's tim verbellen's talk
robots modeling the world from pixels
using deep active inference
thank you
so unfortunately i could not
make it live
but i regarded this talk for you and i
hope you'll find it interesting
i'm going to
highlight a bit of our research like
sketching out the picture what we work
on and put it short basically what you
want to do is you have don't have robots
that can model the world they live in
from pixels but basically we can extend
it to any sensing modality
uh using the factory entrance
so why do we work with robots well
basically
we figured out that if we want to have
something intelligent to build something
intelligent that
is actually doing something relevant in
the real world then you need to do
action you need to interact with the
world you need some kind of embodiment
and that's why we work uh with all kinds
of robots we have manipulators that can
scatter around grouse projects and
directed objects we also have navigating
robots that can drive around and fly
around so you might be wondering yeah
why are you looking at both navigation
and manipulation and then everything
there whereas all over the world there
are labs that are dedicated on like
manipulation as like a single domain and
navigation as another domain and they're
like
distinct like problems well the thing is
that if we take it from another approach
if you look at it from an active
inference perspective then it's
basically the same thing you're doing
the same thing and that's why we're
trying to combine
all kinds of robotic
problems
from this single scope and see to what
extent we can kind of address it and
solve them and and to compare where are
we
compared to state of the art in robotics
let's say
that's like our overall objective
so in this talk i will talk a bit on
uh sketch out what is the general
approach we're taking and then some
current results in both navigation
manipulation and some of the work in
progress stuff that we're excited about
and working on right
so let's start off with what is active
inference
uh i guess most of you will know already
but just to set the scene and grow
for at least next 40 minutes on the same
page regarding location and what do we
mean with the terminology
uh so basically active inference just
means to us we have our agent or brain
that just built a genetic model of its
environment which we call the joint
probability over outcome so
actions a and then some hidden states as
so your agent is distinct from its
environment it can
interact with the environment by doing
actions it gets some observation then i
try to model with a hidden state like
how is this environment
generating me
generating my observations and can i
model this through these mistakes
we use
the the single principle of uh
optimizing this this this uh this thing
by minimizing circle figurity which is
like another bounce on surprise or a
prediction error and importantly
not only you use this to model the
system to build a model of the world but
you also use this to select the actions
that you will hold that will minimize
your expected ability in the future and
like
looking at everything from this angle of
minimizing your prediction error not
only for the pulse but only for the
future this basically gives you a very
powerful mechanism to
start doing robotics
so
just some mods uh equations uh that's
that kind of relates to this this
reality concept so basically minimizing
the energy entails having this kind of
complexity minimization so you want to
have the simplest model that explains
your world where on the other hand you
also want to have an accurate
description uh of how the world works so
you want to predict your outcomes from
your states this basically means that
you're having all the information that's
out there in the world you can actually
have this in the state representation
but at the same time you want to have
your explanation as simple as possible
according to fire and this is the list
it's basically the variational
uh i was here which is like saying i
want to be
able to reverse the model like if i have
some observations i won't be able to
infer
what is the most likely state that could
explain whatever happened to now
and then
if you look at the future then of course
we don't know the outcomes that will
come in the future so now it's basically
the
same formulation you can have like
the expectation also considers what
might happen in the future so what
outcomes might i create and then
your
your expected strategy
becomes again like two terms one is the
instrumental value it's just says how do
i think the outcomes that i witness will
actually realize what i expect to be
what i want to be like it's like
realizing uh preferences
and in a reinforced learning context you
might see this attack reward symbol but
rather having it's coming from the
environment it's now more like something
that's uh intrinsic that defines what
you are as an organism and then
is like um gain like
how do i think my beliefs will shift
for what i think now that will happen
versus what i think my state belief will
be if i supposedly i get these outcomes
and you're basically searching for the
observations that will give you more
information about uh what you're doing
so
automatically you get this on the one
hand gold direct behavior but on the
other hand your your agent is also
driven to find out um the development
observations find out information in
this environment
but of course um we have this kind of
deep active influence flavor where we
basically want to learn this model just
by feeding it data basically and we use
uh these deep neural nets that you you
know uh from from the so-called
artificial intelligence nowadays uh like
it's basically a functional approximator
where you give it some data and then you
can you can match any function with them
and we use these then to uh approximate
the densities that were on the previous
slides so how does it go we have our
observations or actions we basically
feed those to a neural net
which then represents this approximate
posterior so this outputs like means and
standard deviations of gaussian
distributions and these are there like
your posterior distribution so it looks
like a bunch of multivariate reductions
and this is then your your state
representation like what's happening
right now given the
observations i had until now
then we have a
new an additional neural nets that then
like predicts the dynamics in the
slaving stages like if i do these
actions how will my state evolve in the
future
this now puts again uh parameters of uh
gaussian institutions for example and
this allows me to plan in this latent
state space like what will happen if i
do this or that
and in order to kind of train them all
from
that then tries to predict the
observations that you expect to see from
the state and so the
the trading mechanism is then minimizing
the energy which entails it
here you have your
accuracy
minimization so you minimize your
constriction error but at the same time
you minimize complexity with which
basically boils down to the l divergence
this thing and this thing is like
what i expect
to happen uh without observations i
wanted to have it so as close as
possible to what i expect has happened
given that i saw the observations and by
minimizing the scale divergence you
basically of course small to have like
very concise um
encoding that allows you to imagine
what might happen and at the same time
emerging information coming from your
outcomes but not
more than as necessary so you don't want
to necessarily model all the details in
your in your pixels for example as long
as you have enough information to
predict uh sufficiently
so that's like
roughly at the approach
and so now we look at some instances uh
in in robotics cases and we'll start
with the navigation so in this case we
have roles like these
you know but then with some
additional sensors mounted on top of
them so we can get get all kind of
inputs we just drive them around this
map environment where we have rex that
simulate kind of a warehouse setup and
then we just
train these kind of models that just
have to predict
for example from camera images what will
i see if i do certain actions and then
after training such a neural nets then
this is
the kind of
thing that we get so these are basically
imagined views from uh from a viewpoint
from from inside this lab environment
and now you can say okay what do you
think will happen if i do certain
actions
and this is the kind of thing that that
it starts imagining
and these are four different samples
from this distribution so you'll see at
the beginning they're they're all
imagine kind of the same thing but as
the further you go in the future the
more they disperse in their kind of
modeling all kind of scenarios what
spikes happen in the future and you can
also see that
even though the model is trained on long
sequences it doesn't really capture like
long term
dependencies or like very accurate uh
location information like here if i turn
it around i will be facing the wall
whereas
if i turn it around or just another
part of the severe things i'm in the
middle of the you know
i'm at the edges let's say so it kind of
all has this inside the model that these
are all kind of scenarios that can
happen
but because we condition these these
these models on the action we can also
generate kind of uh action condition
samples we can say what will happen
so it actually encodes these dynamics
inside
this model and this is just training
from data from just driving around and
learning to predict what can happen
so
one of the things that we found out is
actually by by training such a model we
can then after effects that's that's at
runtime compare always your prediction
what you think will happen to your
posterior belief what's what's actually
happened given your observation and then
what's the yellow version between the
two which is one kind of a notion of of
the basis size of the model and if you
then put like a new object like you have
this stable header there and if the
robot drives over it then this kind of
dynamic dynamics is it has never seen
before which should result in like a
huge spike in spike and the robot is
like yeah what's going on here and in
order to show that this is not just a
measuring the difference in pixels we
also have this scenario where there are
people walking by the robots which also
happens when you're recording the data
so this is kind of an environment
scenario and then actually the robot is
like oh yeah this is something that can
happen i see some next
is nothing to be surprised about so here
you can see that it's more than just
learning pixel dynamics it actually
captures like this is a normal state
versus this is a weird kind of dynamics
and one of the nice things from from
using these learned models is that you
can actually put in any sensor so we
focus a lot on the pixels because that's
also nice to visualize and you can
relate to
how it looks like but we can also give
it like a bigger uh lights you can see
the lighter computer
sweep and there's some ranging and here
we have like a rainbow which is a bit
more expensive basically
i mean the range axis like
something
it just means is something going towards
me or is it going further for me and
also here we can then have like
imaginations of the model like what's
going to happen in this state space you
already saw the pixels it also relates
like okay this is how lighter scans will
be this is how radars will be if i if
i'm looking at the air i see much more
reflections in the radar damage stairs
if it looks at the air
it has like only a few uh reflections so
it actually captures all these dynamics
from any of these
modalities in this in this latent space
so that's one of the strengths of this
work
but as i told you
it it has very a very narrow like
temporal depth that can predict for a
few seconds maybe one second maybe up to
two seconds but then it becomes
dispersed and blurry so you cannot
really use it for like long-term
planning so we figured out yeah what do
we need to do in order to
use the system but then like do
something more uh relevant longer and we
figured out that what we need is go a
little higher and make like an article
model that instead of predicting like
the next sensory observation it can like
predict uh
which kind of state you expect like a
bit further in the future and then we
found in this kind of model where the
blue board is actually what you saw
right now but then the red part has
cycle
where we kind of combine some some ideas
from engineering from slab right what is
the thing that you expect to be like in
minutes or a few seconds there and it's
actually like okay i'll do that at a
certain location right now and in a few
seconds i'll be at a different location
and this different location will there
be more the kinds of observations and
poses that i expect to be there so if we
implement such a model it basically
boils down to having on the one hand
this is
abstraction of the sensory inputs which
is what you you saw before and then
together some representation of the pose
so if you turn around you keep track of
it so you know kind of uh where you're
heading and you have some sense of fault
integration and then these two combined
then build kind of a map which is then
becomes your your model of the world is
then traversing this fabrics
and then we get something like this so
here we go it's set up uh so here we
have the camera now we have a late
encryption nation from the sensory
inputs here we have the odometry which
is very nice you can see it go over the
place but then
by integrating both like this rough
sense of where you are together with uh
what you think it looks like and then
combining like if this pose and you is
pretty much the same as what i visited
before then it's probably the same
location and you merge the two and so
then you see that it actually covers
different nails in the um
in the lab and it actually makes sense
out of it and it and then you can
basically use this model also predictive
what is this looking like and then you
can use this to like plan longer in
longer term things
so then we go to the more manipulation
kind of uh
use cases where we have like a robot arm
and we didn't have a camera in the
in on the wrist so it's actually getting
information what is currently looking at
you might think yeah this is like a very
different use case but again the way we
approach it it's just an agent that can
move around and its main objective is to
predict what will i
move around and then use that to kind of
figure out how this first world works
but of course now it has much more
degrees of freedom but other than that
the concept stays the same
so
here we basically have been
similar thing where it basically learns
other viewpoints from the information
government so first we give it back very
it's straight looking at the enemy board
the table twitter there's nothing and
then it's regal's work for all kinds of
business like instructions for all kinds
of poses in the workspace which just
figured out and it was trained on like
simple cases with some blocks in front
of it in simulation then if you start
adding observations to the system you
can see how all the different poses are
kind of imagining ah there was a yellow
cylinder there so in these few points i
probably need to imagine a cylinder and
this way you can kind of
start building the world and
reconstructing the world from all kinds
of viewpoints
um so it's always predicting the future
observations from the information it got
until then
and the model is improving as
information but then you can of course
also use the model to kind of
assess which would be a good viewpoint
that i haven't seen before that gives me
some new information
and then basically what we do is uh we
use our this
expected energy term to then uh
drive the
and what we found is that by just doing
this mechanism in this case we also give
it like a preferred observation like
this uh
blue cube uh the current observation
doesn't looking at that in space i want
to found it a bit is actually it first
goes all the way up because that it's
what it figures out we'll give it more
information and then it will start
zooming in and scavenge for the
preferred observation and then stay
there it was a
really cool effect to see from just this
principle that it works right now it
goes up to to have an overview and then
once it's uh explored
the workspace you can then kind of vary
it in normal viewpoint so this is the
imagination state of the robot arm
wandering around like we had in the
navigation scheme but now with the
arm action stage
so it's again the same principle but we
get
some similar
results then of course we were thinking
okay we need to throw a lot of train
data like different scenes of different
objects added before it could kind of
start imagining these kind of scenes but
if we look at how we learn how the world
works how the world around us is then
then bubblers are actually looking at
objects and and and manipulating them
and looking at a single object at the
time and that's how they learn to figure
out
this is the better way to to learn in
the
scenario how the world is working so
that's then what we did instead of like
having uh
trajectories of random scenes we just
made the robot look at particular
objects and then predicts other
viewpoints that still from that same
object so it's always looking at kind of
the same location and predicting how
will this thing look like from this side
and then
you basically get something where you
can imagine for this particular object
this is how the dynamics are for this
object
and then we take a similar model but
then we trade it on a different object
so now instead of having a huge
model that has to learn about any object
around we can basically compress this
into a very uh
well very it's maybe a little brave with
a much smaller real net um and then we
instantiate a new instance for every new
object that we created so we can give it
max
our a can or a banana and it can start
imagining how all these objects look
like from other views
but then again we can give it like a
preferred view
and then all of our air which would be a
trajectory that brings you to the
preferred view and that's then uh that
is what you can see here so then the top
view is like like the target you just
randomly give it a viewpoint and it
figures out how to move in this space
just by imagining how um
what this kind of objects you'd like
from from different views
then you can also use this to kind of
specify objects because if we if we then
have a
a random object that it either had seen
or never saw before it can use all the
models and just
very like
which which model is actually matching
my prediction for what i'm seeing right
now and this then gives you like an idea
like it showed me that object and you
can see here that for an initial view
it's already pretty good at knowing what
it is
but in some cases you have like a very
ambiguous viewpoint you cannot really
distinguish the two objects and then you
uh you can just have another view and
that will then resolve the ambiguity and
that's exactly exactly what you see here
so the energy agent will look for the
most informative view and then for the
node objects it reaches like 100
accuracy and then
and for this particular case it's not
100 accurate and why is it because there
are objects that might be very related
so for example if no it knows it knows
about spoons and then you give it a fork
and it's like
yeah it's kind of looking like a spoon
so i'm i'm i'm not sure but and these
are the errors it makes but these are
like sensitive because actually the
dynamics of the objects are very much
matching an object i know before and
then if you query it like what would be
a the next view you would like to see
you typically want one with a low
expected free energy
but if we ask it like what would be a
view that you don't want to see then you
get this kind of uh uh
imagination in the in the the
rightmost flow where it's not like
foreign
or this particular view it's very dark
so i cannot really distinguish it from
anything and
the mystery bubble in bottom right like
yeah this is kind of looking like a
banana so this is not the viewpoint i'll
i i'll choose to go next but in practice
we saw because these objects are so
distinct and a random agent is also good
at just integrating information because
the chances are low that you actually
end up in this ambiguous viewpoint so
in this scenario it's equally well just
randomly looking around but the more
your uh your objects become ambiguous
the more benefit you have from actively
sampling uh a particular viewpoint
yeah for sure
yeah exactly so so immediate like the
same thing as as using radar and camera
for navigation it's like using textile
and
visual information for
for just
inferring what this object is like to be
uh as a as a robot
we haven't done a particular experience
yet on on tactile because it's also a
bit more difficult to kind of uh yeah
just to simulate and and but yeah
it's on our minds to do this kind of uh
things uh but yeah it's a very
interesting route to take a
and so finally
uh what we can also do then uh is look
at a c with different objects and then
say okay i want to i'm going to open the
gang so i need to have the top view
this type of
circular gray thing inside the gold
image search the only thing it will do
is like randomly search around he
doesn't see something alive and then go
to the target but in our case
you know the the system
like this thing
is probably more related to the can
rather than instead of the sugar box so
it will draw its attention to the can
and then also yeah this is more like a
top view and this is more like a side
view right so it can imagine like the
the thing it should the the movement it
should make to go to the top queue so
this is exactly then for
it directs its attention to the correct
object and immediately finds out
the movement it should make to kind of
get to a similar um so that's kind of
the real powerful uh system and you can
see this kind of like adding another
hierarchical layer on top it's similar
to the the navigation where you where
you then have like an abstraction of
locations now you have like okay i have
an abstraction of objects being
somewhere spatially arranged then i kind
of infer where they are and how it
should move
in this space in order to operate
so then to end
something that reflectively and actually
get resectively working on this is
basically okay
we now have this system where we can
build a model where we can relate action
to what is happening but one of the
difficult thing is still like
the
further the further in time you used to
plan
the your your your potential of
trajectories explodes it's like yeah you
cannot plan using all these these fine
grain actions so can we figure out like
new
sensible actions or skills that we that
we can use to explore
and so one thing in order to
avoid this explosion of options is to
amortize
a policy to now betray again a function
that is then more kind of habit policy
that given the state gives you the
action but instead of using a reward
signal as done in reinforcement learning
you basically give it an uh
an objective that's more like related to
the expected free energy so in
in particular here we
use what we call latent asian surprise
which was like terminally invented to
relate more to the oral community but it
is just like the information game on
your expected states basically and then
we found that it actually found out to
play these video games just purely from
an intrinsic motivation and also if it
compares to other like terms that they
add in the url 18s to get this this
intrinsic drive we actually found that
our method was
either on bar or slightly better than
others and especially in cases where we
had some noise in the states so if if
the observations are kind of noisy or
ambiguous the more methods still up then
it was it was more easy to outperform
the others because
they were like okay the noise is like
very interesting so we're dropping noise
observations although maybe they they
don't give you extra information so that
was um
something interesting before and now
we're actually expanding that like
instead of having this is more like
having an exploration policy but now
we're thinking more like okay if we want
to plan maybe we just won't have like a
few distinct options that make sense to
explore like can we
can we kind of find some elementary
skills that are worthwhile to explore so
in this case we have again a robotic r
and here we need uh we again explore
using this this uh
intrinsic drive for information gain but
then we give it like 32 potential slots
to learn policies and just have to
find out which ones are uh good
trajectories that in total allow me to
explore the state speed together and
then we ended up with like a manageable
set of skills that we can then find for
particular tasks uh
and that's actually what the some of the
things that we're working on right now
so with that uh i
thought thank you all for listening i
hope you enjoyed it should you have any
questions you can always reach out via
email or via twitter
and hope to see you soon
the next location
thanks
all right
that was tim verbellen's presentation
robots modeling the world from pixels
using deep active inference the next
presentation is going to be by ben white
artificial empathy
active inference and collective
intelligence
hello everybody my name's ben white i'm
a first year phd philosophy student at
the university of sussex and i want to
start by saying a really big thank you
to the organizers for inviting me here
today to share this research with you
it's a real pleasure to get to do this
even if
it's just in a pre-recorded format
um i want to say right now at the outset
that this is very much a collaborative
and ongoing project it's work that i've
been
doing with mark miller and daphne
demacus and it's very closely related to
the kinds of things that i do here at
sussex
so i'm interested in looking at the
relationship between human human
well-being and material environments
i'm interested in things like ambient
smart technology
social media
augmented and
virtual reality
and affective computing which is what
i'm going to be talking about today
and because this is an active infant
symposium i'm going to afford myself the
luxury of not going over the basics of
the framework
and instead i'm going to jump straight
in and i'm going to tell a fairly broad
stroke story
about how we think active inference
might be able to shake things up in
affective computing
so affective computing is a research
program which as many of you will know
uh aims to build computing devices
uh capable of interacting with human
users on an emotional level by
uh identifying categorizing and
responding appropriately uh to emotions
in human users
and just to give some examples we have
the paper in the top right from the mit
computing lab and this
project aimed to put affective
interfaces into cars
because any of us who drive know
that there are certain emotional states
we can sometimes find ourselves in that
probably hinder our decision making
progress sorry decision making process
and that can have some pretty negative
outcomes and so this project was really
geared towards increasing road safety by
intervening uh in the emotional states
of drivers
the two devices at the bottom so the
screen on camera in the bottom center
and the rectangular headed guy
who's yellow these are jibo and robot
respectively and these are therapeutic
interventions that use facial
recognition technology emotion
recognition technology
to
learn about their users and then make
suggestions for certain tasks or games
or even clinical interventions that are
geared towards supporting the emotional
well-being of the user
but as you can imagine
these are not the
dominant deployments of affective
computing
we mostly find affective computing now
in industries like uh recruitment and
marketing
so for example
uh companies like unilever and many many
others use emotion recognition devices
in their hiring process
in order to analyze certain non-verbal
responses and facial expressions which
they say are indicative of certain
desirable or undesirable uh character
traits relevant to
the job
however um you won't be surprised to
know that this has come in for fairly
heavy criticism so there are certain
kinds of worries about this technology
um
the first worry is that it is simply not
functional uh that it's based on bad
science and that it doesn't do what it's
supposed to do
and closely related to that to that is
the um various kinds of ethical concerns
uh mainly that these systems are in
danger of propagating certain kinds of
biases and prejudices
so lisa feldman barrett for example who
is a major leading light in affective
neuroscience
has come out uh fairly heavy against
this kind of technology uh she's labeled
it neophrenology and said that it's
there's simply no way that it can do
what the people who make it say it can
do
and this is because she says it's based
on a very outdated theory of emotion
which states that humans have six to
eight basic emotions
um things like anger fear disgust
surprise and so on
and that these emotions are expressed
through sets of facial expressions which
are universal uh across different
cultures and different contexts and
anybody familiar with lisa feldman
barrett's work will know exactly what
she thinks about that theory of emotion
uh she's not a fan of it at all
and the ethical concerns um
have been raised by ai ethicists like
berber biharni
who's argued that basically the fact
that these systems are trained on very
very large data sets mean that they are
inherently conservative and this is why
they propagate certain kinds of biases
so
the two pictures of the hand holding a
device you can see on the right hand
side
in this case it's google's vision cloud
in the top picture with the dark-skinned
individual that device is
identified as a weapon and on the bottom
that light-skinned individual it was
identified as some kind of electronic
device and there are other studies as
well that have shown that emotion
recognition technology just works
completely differently on non-white
individuals and so
with technology like this making such
consequential decisions for people's
lives
it's really really important that we
start to get this right and we don't
have these kinds of outcomes that we
have in the current program okay so we
need the strongest most up-to-date
theoretical underpinnings that we can
get
and we think the place to start with
that by
the place to start in updating the
science is to recognize that these
devices are very problematically
disembodied they're very superficial and
they are inactive in the sense that they
don't perform any actions and this of
course is a million miles away from the
way human beings interact socially and
emotionally
and we've known this for a very long
time so we've known for example
this example from luis pizza's work that
emotions are not simply um partitioned
off from the way human beings think or
act actually cognition and affect are
very very closely intertwined okay
there's no discrete separate brain areas
that only do emotion and only do
cognition
and
furthermore
research paradigms in
cognitive science so embodied cognition
for example
tells us that actually we need to go
even further than that and recognize
that embodied action is an integral
constituent part of how we think and
feel
and then the other ease that make up for
e cognitive science so in activism
activism
extended cognition and embedded
cognition have come together with niche
construction theory in really
interesting ways to tell us that
actually we also need to consider
how elements of our external
environments can scaffold the way that
we think and feel
so
this is where active inference comes in
because we think that if we're serious
about designing these kinds of devices
taking into account these most
up-to-date theoretical developments then
active inference basically brings all of
that in with it so active inference is a
theory that really elegantly
kind of intertwines action perception
thinking um cognition and affect
together
under the unified imperative of
minimizing an agent's surprise
so that's the first thing that it gives
us off the bat it gives us this
unified computational
unified conceptual framework that can be
shared by researchers in different
fields but mainly as the name suggests
active inference really puts action
front and center it's not some
afterthought or just some kind of
bolt-on gimmick
and i think it's worth reflecting for a
second just on how central actions are
to the way that we interact socially and
emotionally okay so human beings are
very far
from being a passive uh classification
device we're constantly sampling the
world and probing the world in order to
get more information so that we can
update our models of the world
so imagine
the following scenario which happens to
me fairly often uh imagine you're on
public transport and somebody's giving
you a weird look or maybe they're
scowling at you in some way
we tend to not sit there and just look
at their facial expression to try and
work out what's going on we have other
avenues um open to us so we might look
behind us to see if they're actually
looking at someone else we will probably
look at the broader scene for some
context to see if there's something
going on that can tell us more about
that scowl or depending on our mood we
might even scour back at them or flash
them a smile and see how they respond to
that
and i think
another scenario that really brings this
intuition out very strongly is to think
about the peculiar kind of tension that
comes in a job interview
so i think that tension is the result of
a confluence of two things firstly very
high uncertainty
uncertainty that's really important to
us and also the fact that our usual
embodied epistemic resources have been
straightjacketed by social convention
because it's the case that in a job
interview even though we want to know a
lot about what the other people are
thinking and feeling
social convention dictates that we can't
ask them
we can't prod them and we can't really
sample the scene in ways that are going
to give us more information we're kind
of stuck to the chair we just have to
wait and see
and that's an unusual situation to being
because so much of uh human
social and emotional interaction relies
on active states to use active inference
terms so
speaking listening
prodding smiling scowling raising an
eyebrow all of these things are embodied
actions
that we take to learn more about social
setting
and i think the thing to emphasize is
how important context is as well so the
ability to kind of actively survey a
scene to drink in context
but also the way we learn about the
relevance of that context is um
something that's built up and scaffolded
through action and uh different kind of
patterns of practice
so if you think about the scala on the
bus again there's a
high degree of uncertainty around that
facial expression
but if you imagine that same facial
expression transported into
the onto the face of somebody on the
other side of a boxing ring
all of a sudden the uncertainty around
that facial expression is minimized
because the context of
boxing ring tells you everything you
need to know about why that person is
scowling at you
and this emphasis on context is
something that's badly missing
um in current iterations
and the active inference community is
already producing really cool work
premised on these kinds of insights
so there's this paper thinking through
other minds by samuel vasiere and
colleagues and this paper highlights
just how it is that we come to
understand our socio-cultural niches
through precisely this kind of active
social foraging so it's really
emphasizing the importance of context
and the fact that we come to learn about
context through action
and there's an example
um of where we see a gap between
artificial systems and humans
when dealing with context is how
artificial systems and humans compare
when
performing selective attention to in
regards to some tasks
so it's a really pervasive problem in
artificial systems that they don't tend
to look at the same places that human
beings do
when human beings are surveying a scene
for some kind of task
relevant information so the question is
how do we get
artificial systems to drink in context
in the same way that humans do and then
how will that improve the performance of
emotion recognition devices
so selective attention is all about
filling in epistemic gaps it's about
filling in gaps in your knowledge with
information from a scene that may or may
not be task relevant
and
one of the reasons humans are so good at
this is because obviously we have this
huge knowledge base of
uh what different contexts mean we live
in the world we've always inhabited
socio-cultural niches and so we have a
lot of experience
but as i said before it's important to
emphasize that the way that we learn
about context is about sampling
different contexts it's about
the fact that we have our entire lives
been actors in the world not passive
observers
and i think this work by moser and
colleagues that you can see on the slide
here
it's really interesting because it shows
that active inference is capable of
modeling selective attention
in ways that give us much more
human-like results so they used certain
kinds of internal precision dynamics and
they demonstrated that these precision
dynamics can map accurately covertly um
task relevant and task irrelevant
features of a scene
and then update precision estimates in
in relation to that information which
then drives overt actions which then
serve to update the system's model so
it's this very close relationship
between
covert attention and overt tension which
i think is really interesting on this
account
and i think active inference is a really
powerful framework for recognizing
addressing context generally and for the
importance of action in learning about
context so the models that i just
outlined they provide the tools for this
very elegant top-down
first principles approach to selective
attention
which is based on these internal
precision weighting dynamics but also on
uh embodied action perception cycles
and of course one nice side of side
effect is this side effect of this
is that systems based on this would be
able to autonomously
select the data from a scene which is
going to give them the most epistemic
payback and this means that they can do
away with the very very large data sets
and long training times which ai
ethicists have said are probably the
root cause of a lot of the ethical
concerns that i talked about earlier
and so from a practical standpoint this
means that we need to think about
building affective computing devices
which are not merely
inner lumps of plastic we need to start
thinking about approximating something
much more like a fully embodied agent
one consequence that's really
fascinating about the kind of active
social learning that scaffolding
scaffolded through other minds um that i
was talking about earlier with the
thinking through other minds paper
is that active inference agents can come
to enjoy a degree of synchrony between
their internal states
so
this paper by carl fristen and chris
fifth a duet for one
it utilized simulations of songbirds to
show that quote generalized synchrony is
an emergent property of coupling active
inference systems that are attempting to
predict one another
so in rough terms what they demonstrate
is that according to active inference
meaningful communication between two
agents
requires that they are sufficiently able
to model one another in a kind of
infinite regress so what it is is me
modeling you modeling me modeling you
and that by doing this by making and
testing these kinds of predictions we
essentially ultimately converge on
model model synchronization
and this is a core part of the paper the
original paper by daphne de mekas that
she did with um fristen and parr
which has already suggested that if we
take active inference as a starting
point for building affective computing
devices
then what we have is the prospect of an
artificial system which can potentially
sync internal states with the user and
that's obviously going to hold an awful
lot of promise
for um certain applications of effective
computing and i would say to anybody
interested in the kinds of things i'm
talking about now to go and start with
this paper by daphne
because i think it's a really
interesting and wonderful starting point
but
one thing that we want to say is that
for this sort of deep
affective synchrony between artificial
devices and users
it means that the artifact itself will
need to have some kind of interroceptive
signals
some kind of internal affective dynamics
of its own
and it needs to be able to act in ways
that expresses those signals so so far
i've been talking about
acting in ways to express those signals
and acting in ways to sample the
environment
but i want to say something now about
the prospect of active inference devices
which actually have their own
internal affective dynamics because i
think that the active inference
framework has already shown the
potential to provide this
what i'm talking about here is some
fairly recent developments in the
framework called aerodynamics
um and using aerodynamics we can start
to understand how embodied affective
states are an intrinsic part of
the motivational drive for curiosity and
epistemic foraging
so one of the really elegant famous
strengths of active inference is that it
has the power to dissolve
this opposition between explore and
exploit
and while there are there have been
numerous strategies for building the
motivation to explore into artificial
systems active inference has the
potential to put embodied activity and
emotion
right at the center of solving that
problem and so this is obviously going
to be relevant if we want to build
emotional recognition devices that are
intrinsically motivated to probe the
internal states of their users
so i think it's worth taking a second to
refresh how active inference accounts
for emotion and effect
so
the first attempts to understand
um interoception and active inference
were
they beared a lot of resemblance to the
way that we were thinking about
perception under active inference
um so it was about um
predicting um signals
hidden states in the world except that
the signals that the brain was trying to
predict were internal signals they were
coming from inside their own body
um so gastrointestinal
respiratory circulatory signals
and feelings like hunger thirst
temperature pain these were seen as
top-down predictions about the hidden
causes that underlay those physiological
changes
but it was the case that researchers
that were working in affective
neuroscience so people like lisa feldman
barrett uh neil seth and mika allen they
were quick to add that these
interoceptive predictions probably held
a kind of special prioritized place
in terms of the overall system because
they were likely to ground other
predictions predictions about the
external world in terms of what really
matters which fundamentally is
maintaining the homeostatic states of
one's own body
but more recently than this affective
states have been hypothesized to fill
another role within the active inference
framework
which
is essentially says that felt bodily
states things like mood and other
affective states valence bodily states
they reflect a kind of second order
information within the dynamics of the
active inference system and that
information is essentially tracking the
rate at which surprise is being
minimized relative to the expectations
of the system
so according to aerodynamics affective
states
are essentially uh just the subjective
level feedback about how the system is
doing at minimizing surprise at keeping
itself within expected bounds
relative to the expectations that we had
going into that scenario
the second order information doesn't
just it's not superficial in the sense
that it just reflects that kind of
information but it actually plays an
intrinsic role in modulating the
internal precision dynamics over action
policies
so from a phenomenological perspective i
think this makes really intuitive sense
so when we're doing better than expected
at a certain task we tend to gain
confidence we might take more risks
and when we enter a certain scenario or
task with a particular action policy
which doesn't work out the way that we
expected it to
we would be very quick to switch things
up and try something else
and in this sense aerodynamics can be
said to keep agents
flexibly attuned to the opportunities
for success within their environment as
they learn and develop new skills and
abilities
and the thing to notice is that agents
that are outfitted with a sensitivity to
aerodynamics and naturally curious
because
finding new um
uh new surprise in the environment which
can be successfully minimized it
literally feels good to us um and the
places where um
we find surprise that we can minimize um
in the greatest amount is at the edge of
our skills and abilities and this is why
we like to find scenarios that are kind
of
maximally challenging without being
frustratingly challenging without being
too hard so we like to occupy areas that
are neither too well known nor too
complex
and aerodynamics also plays a role in
helping us to direct and enhance
learning so um surprise and its
reduction rates signal the expectations
about the learnability of particular
situations so that helps to guide our
attention and prioritize certain areas
or certain tasks where we know we can
find the most success
and we've already seen this kind of
optimal
surprise minimization show up in robots
in terms of curiosity
so there's this work here by odoya and
smith where their robots were trained to
seek out optimal levels of complexity
where the most learning can take place
and specifically
now there have been active inference
approaches that have begun to use
aerodynamics in real world robotics
so this is really exciting and this is
kind of real world proof of concept in
the work of skelassi lara and syria
and these researchers have actually
built robotic systems that make use of
this internal
aerodynamics
machinery
so their work has shown that robots that
are equipped with aerodynamics are
actually better able to manage
uncertainty um by fluidly selecting
adaptive actions in an environment
compared to more traditional and
traditional approaches
so artificial agents equipped with
internal aerodynamics are better able to
learn um and then autonomously select
the proper
surprise minimization strategies in any
given situation
and they do this by allowing their
valence states that second order
information about performance relative
to expectation
to weigh the selection of the most
suitable behavior so in other words by
allowing that second order information
to have a direct impact on the internal
precision dynamics over action
and this work showed that this kind of
internal aerodynamics also provided a
way for artificial agents to navigate
the temporal aspects of goal selection
so basically what that means is these
agents were very
knowledgeable about how long they should
persevere with a certain task and when
they should give up which is obviously
something that even human being human
beings struggle with a lot of the time
so
thinking in terms of aerodynamics
it shows us that affect is intrinsically
linked to goal selection
and we want to suggest that
by introducing these aerodynamics into
affective computing devices we would
start to see devices that are
not only motivated to kind of
exhibit a kind of curiosity
in implementing new policies for action
but we'd actually start to see a real
paradigm shift in the affective
computing program to a much more
biomimetic approach so instead of just
having classification devices
in lumps of plastic or in smartphones
we'd start to see embodied devices that
can actively engage with the world
and that have their own internal
affective dynamics based on
what we think is going on in living
systems so this is really exciting
and this new wave of affective computing
devices would not only um
be able to perform much better but we
think it might go some way to um
addressing some of the ethical concerns
that i was talking about earlier
but the thing to be really clear with we
don't want to a kind of disclaimer at
this point is we are certainly not
saying that an affective
sorry an active inference approach to
affective computing
is a replacement for thinking about all
of the kinds of social justice issues
that come with the implementation of
this technology we are just kind of
speculatively saying that it's on first
glance it certainly appears like some of
the ethical concerns might be addressed
by this new approach
um but we think there are going to be a
lot of benefits of this new approach so
first
if you think about the kind of model
synchrony
um that i was talking about earlier and
think about that within the context of
therapeutic intervention
we think that when we get this degree of
model synchrony um
any any dysfunction in the user's
internal dynamics is going to be
mirrored in the internal dynamics of the
artifact and so this is going to be make
the device very well placed to make
suggestions about potential
interventions and this is essentially
what cbt already attempts to do so this
will be building on approaches that have
already been proven to be
effective
and the next thing is to think about
the fact that so far when we've been
talking about action
i've been talking essentially about
epistemic foraging um but once you have
the possibility of humans and artifacts
establishing this kind of model
synchrony and you have these artifacts
that are properly embodied and able to
act in the world it might be possible
for the artifact to begin to install
prior preferences
uh about what states in the agent are
actually preferable
such that the artifacts may actually be
able to steer
with a degree of autonomy the emotional
synchrony between it and its user to
specific ends so when we have this uh we
have these active inference theories um
beginning to emerge of depression and
anxiety
and other kinds of disorders
with that full understanding coupled
with the kind of model synchrony i've
been talking about we start to open up
avenues for the device itself
steering the user away from these kinds
of dysfunctions
now it might be the case that these
active inference devices come with their
own set of worries and ethical concerns
i think it's very plausible that they do
and it's something that we're going to
be thinking about as we go forward in
this research
but i don't have time to explore it here
but i think the last thing to say is
most speculatively is that this active
inference approach also sets the stage
for beginning to address the well-known
value alignment problem between humans
and ai devices
basically what we have here to our mind
is
a initial and very speculative building
blocks of building artificial systems
that have a degree of genuine empathy
with their users
so these devices would not merely be
simulating empathy or passively
categorizing human emotion they would
generally have genuinely have their own
internal dynamics that would synchronize
and match with the internal dynamics of
a user and this is going to be a bedrock
for much more interesting and much more
rewarding human ai collaboration into
the future
and that's the end uh i wish i could be
there to answer questions um
unfortunately i'm not uh i'm pretty sure
mark miller's going to be there with you
so maybe he'd be happy to answer some
questions but i would also encourage you
to get in contact with myself i'd be
really happy to hear from anybody that's
interested in this kind of stuff
um you can see my email there be white
at sussex.ac.uk
and you can get in touch with me on
twitter as well at
midnight biscuit
thank you again for listening it's been
a real pleasure to get to present this
work
thank you very much
all right
um should i start
we're back
and yes
please this is the presentation of north
sajd learning agent preferences thanks
north for joining and take it away
brilliant thank you um daniel um
so just before we get started i just
wanted to thank daniel and the active
inference um conference i guess um for
inviting me to give a talk on this
project um i'm really excited about that
um so just to introduce myself i'm noor
i'm a current phd student at the welcome
center for human neuroimaging
with carl fristen um this is some work
that we've been uh thinking about over
the last
uh year or so
um
feel free to i don't know how well so do
we have questions that um sorry do we
have questions throughout the
presentation or are they at the end
um but if there are any questions
we'll be uh
taking questions in the live chat and
then the round table will be bringing
them
directly during your presentation
okay um yeah no worries
okay so the project is focused on
learning agent preferences and it's from
my perspective is super interesting
because that
sort of changes the dynamics of how you
consider the problem setting and that's
what i'm going to start off with
but before i do that um
i just wanted to highlight my wonderful
co-authors that i'll be uh sort of
presenting the work on behalf of uh so
we've got panus alexey
zaff lance and carl um and the project
so the work i'm presenting is based on
two different projects and i'll
highlight the
the different work as we go through
um so my print okay so i'm trying to
flip okay let's yeah so the the way the
presentation's going to be structured is
just i'm going to briefly motivate the
the problem setting um and then describe
the problem setting in a bit more
technical details and then really drill
down into exactly how we can learn these
preferences
that we can equip the agent with and
then some experiments and
remarks
so what i wanted to highlight is that
when we learn agent preferences there's
usually a bi-directional association
between the the agent and the
environment
and what i mean by that um is something
that you can see in this graphic really
clearly so you've got uh the main part
that the agent would have taken um
as it was um walking down this
particular route uh when hiking
but as
perhaps many
other people are joining along the agent
ends up um walking along the shorter or
maybe the more
smaller part
um so what this highlights is that
agent preferences are essentially
dictated by the environment that it's
surrounded by right so
depending on the constraints so for
example other agents maybe an animal or
something else happening on the road
would mean that the agent um ends up
taking the second part instead of the
first one
and as a consequence of that it changes
the environment so as more and more
agents do the same thing um the the
shape or the construct of that part
becomes more prominent and it becomes
part of that environment and what i'm
really interested in as part of my work
is this sort of bi-directional
association between how the agent
changes the world and the world changes
the agent's preferences because it
constrains the
the the actual state space that it
exists in
um but as part of this project and the
work i'll be presenting we're purely
focusing on how the agent's preferences
or the how the agents uh i guess
objectives are changed as a consequence
of the environment constraints
um but before i do that i really um
i wanted to highlight what preferences
actually are because a lot of the time
um we're not really aligned
on what that means um so i'll just
briefly uh describe how we are
considering preferences so preferences
here are usually a subjective assessment
of what agents would like to experience
and this can be continuously learned or
modified even in the absence of external
feedback so there might be some internal
motivations or some um objectives that
the agent is learning internally
that shape exactly how the agent wants
to behave in the world so in the
previous example when we were looking at
the case of
going between the two parts depending on
the constraint of the environment it's
essentially the agent's subjective
preference because it could have taken
another route which uh so for example
maybe
here um and that could have also shaped
the environment as well um
okay
um so let's motivate this problem
setting slightly more formally
um so we're going to be working um
as part of um
and the idea that these agents that
we're interested in have an internal
model
and this internal model is um
composed um really briefly of uh three
important components um so three
important random variables and then one
deterministic variable so let me just
qualify that a little bit more so we've
got our
outcomes so this is something that the
agent is
exposed to in the environment
and
for example um the the actual i guess um
constraint in the instance of the the
hiker being having to choose between the
two parts for example um it might see a
hindrance or it might um
like have some grass or um some
some other agents that are exposed to
and it needs to that's the data coming
through and it needs to then identify
whether it wants to choose uh one part
or the other part
um
so that would be based on the its own
inferences about what that outcome
actually means and so that's denoted by
s here
and then based on that it needs to then
decide what action to take um and that's
denoted by the a here
um
and at the same time the agent is
keeping track in this particular
formulation of the the agent's model or
the general model that we're interested
in
which is denoted by this deterministic
variable h2
or h3 depending on which
time point we're interested in that is
essentially this deterministic recurrent
model that we have um that's encoding
all the prior history um the the actual
states uh sorry the actions and the
states that the agent has been exposed
to sorry
in the past
and that encodes what is the
the updates that are then used to select
the the posterior estimates uh for the
the next time point
um then you've got your
in this particular model you've got your
latent state and prior and and we're
just
calculating them in really a specific
way so your prior is defined as
categorical distribution and this
becomes really important for us because
this allows us to use some conjugacy
rules to update the way the agent's
preferences are land and i'll come back
to what i mean by preferences in this
technical setting a little bit more
on the next slide
and the state posterior here is again a
categorical distribution that the agent
is estimating based on the history and
the current observation it's been
exposed to
then we've got the standard formulation
if you're working within a mdp
formulation where we've got a transition
function so this is denoted again as a
categorical distribution conditioned on
the history of the agent that's what the
agent is encoding and then we've got an
image predictor um that determines
exactly what would be the next um time
point oh sorry what would be the next
observation given the history and the
state
um so the idea with this gender model is
that you have an encoding of how the
agent is representing the world it tells
you exactly how this
outcomes
are then um
inferred as particular states that then
allows the agent to evaluate particular
actions but i haven't really um defined
how the actions are selected um so we
work in a standard uh active inference
setting where the
actions
are defined as um
being sampled from some probability
distribution a so the actions we saw
before which is calculated as the arg
max of minus g over a so what is that
exactly
um so for our work um we were interested
in essentially extending the minus the
expected free energy um with a conjugate
prior and so the expected free energy in
standard terms would be something where
you have an extrinsic
imperative you have a salience
formulation and you have novelties
extrinsic imperative is something that's
contained by the environment saliency is
when you want to have accurate belief
updates and novelty is when you want to
be able to estimate your world
appropriately given the the parameters
of the model that you've been able to
learn um
and
when we extend it for the preference
learning setting um and this is
something other folks have done
um maybe introducing it as part of uh
prior over the outcome space um so we're
looking at as part of a prior over the
state space so
um
sorry um
let's see if i can get the color to
change okay so this is the
the prior and we're conditioning it on a
categorical distribution d which i
highlighted before and that allows us to
take him to um i guess
i'm sorry
use uh some of the conjugation rules of
interest
so now i'm gonna um
go to the next bit so um sorry just
going back here so
um what do we have so far um before we
move on to how do we actually land this
um d that we were interested in the
previous slide
so we have an agent who's equipped to
the model
the agent is interacting with the world
and based on this interaction the way
the agent is learning its preferences
can shift
and the way is shifted is a consequence
of the type of actions it's making that
we had using the expected free energy
so how do we learn um preferences um
so in the literature there's been um
well at least in the psychology
literature and some of the
the spiking neural networks and other
formulations um there's been a few
different ways it's been proposed how
agents are learning preferences
um so one of them is mere exposure
effects so the idea that when you're
seeing something quite frequently
that that pairing is more absurd sorry
more preferred than if you want um
seeing that
and this can be uh categorized as a
heavy plasticity learning rule
then you've got attention mechanisms
where when you're attending to an option
um it becomes more preferable so maybe
you're selectively looking at x or y
and based on that you've filtered out
all the other data that you've been
exposed to um and that's what becomes
more uh something that you as an agent
would prefer
um
and if you were to think about a more i
guess um biological construct of that
that might be a consequence of some
synaptic gaiting that can encourage the
enhancement or some sort of suppression
of the data or the noise that you are
exposed to
another formulation could be the
contextual effects where
an option is only preferred when it's
compared to some other options so
there's this relative
comparison happening and based on um
that in particular in certain settings
you would want to do x instead of y and
here x could be taking the path uh the
longer route sorry the wider route route
in comparison to the
maybe the the tinier route that we saw
in the hiker picture and that could be
on you you only prefer the wider route
when you don't see an animal some
blockage there
and this encodes some behavior relevant
signal selection for the agent
um so now what i'm going to do is i'm
going to go through
some rules um and some formulations that
we've been thinking about in terms of
encoding preferences
and they
are um
the way we've um sort of privatized the
the learning of those preferences it's
it
is aligned with some of the um i guess
things people in psychology have also
been thinking about
so the first one is learning preferences
from your exposure
so we start off with extending the
agent's gender model with a conjugate
prior over the prior beliefs and what
that simply means is that we take the
categorical distribution
that we've
conditioned our prior state on
and then we introduce a prior over that
um and that allows us to take into
account some of the the conjugacy up to
update rules that we're interested in
um because our
categorical distribution is oh sorry our
prior distribution over the state space
is d
um
which is a categorical distribution we
can now define a directional
distribution as a conjugate prior
which is denoted here
and we've just got two different
formulations here of how you can update
that
so essentially
as you're exposed to more data you are
introducing um you're counting your suit
accounts over the summation of all the
suit accounts in that particular um
factor that you you're interested in
so
taking this into account we can do have
been learning um
rule which we do using online
interactions through preference
preferences so the way it works is that
given your
hyper prize in the time point before you
can update those based on um
some alpha sorry some learning rule
alpha and also the belief um
updates you've had in the past so this
is denoted by the s for that particular
um
pseudo counts or the territory um
primatizations uh for this current time
point and you add all of this together
and that gives you the updated
preferences
um so the way this particular
formulation works is that the more you
see something the more you're going to
prefer it because
there's a very simple
learning happening here
and in the simulations and the way we
formulated at the moment
we've got alpha set as a static
parameter equal to one so you can
manipulate that and the way you uh you
can manipulate it where if you
have it alpha going to
uh greater than one um
you will then wait the new data coming
in a lot more in comparison to if you
had it out for less than
one um then you're not taking into
account the the weight of the new data
coming in as much
and what this allows us to have is
accumulation of particular contingencies
or the way we are privatizing our prior
and these dictate the land preferences
um
okay
the next formulation of learning
preferences i wanted to speak about was
how we can learn by attending to
preferred options
so here we're going to slightly change
the model um
by introducing us
an additional preference learning
component so we again are extending the
agency enter model with conjugate price
over the
prior release so the hyper price so this
is exactly the same as before but the
the
the different thing that we're adding
here
is the synaptic gate scene code
preferences and these just are
computational homologs that we've
introduced um
and
in terms of the actual
uh
biology of like the the formulation i
think that's open to interpretation but
these allow us to have an attentive
mechanism which is what we're interested
in
and we do this to a two-step procedure
so first we encode memories and how that
how that works is we
take a sample of all the data that the
agent is
interested in
um sorry the the agent has actually um
um
okay sorry um so the way the way the
encoding of preferences is working is we
have two components um which we're then
um combining together the first
component is the the online exchange
that the agent has had so by online
exchange i mean
um the agent is selecting its um actions
based on the expected free energy and
that's allowing you to
essentially gather data about all the
different trajectories it follows
depending on what action is taken and
it's got the data and its posterior
estimates given that
the next um so this would be the the on
policy
um
the second bit that we have is the
imagined interactions so this is when
the agent is offline in the sense that
it's no longer being exposed or given
outcome with outcomes uh based on its
imagined or the way it's interacting
with the world
and the only thing it's getting is the
the updates in the states
uh the latent states depending on what
actions it's selecting and this is the
imagination part
um
so what we're doing is we're combining
this together
and we take 30
of this
and all of this um so these are 10 steps
into the future
um and then we're essentially
interleaving them together and that
gives us an encoding of the memory
um the reason for only using 30 is to
allow for
um the imagined interaction of the new
percep things that the agent is
considering to be taken into account
and
and the the idea with the interleaving
is that we're allowing for but the the
real experience and the imagine
experience so the the reel is here the
on policy experience to be um used to
shape the way the agent is um
encoding its perception of what has
happened in the past
um and then using the encoded memories
we then encode the preferences using um
a selective attention process so this
memory buffer that we have here
is what i showed in the previous slide
so this is the memory buffer
um and then using this we essentially um
encode the preferences using two gating
mechanisms so the first one is an
attention block and the second one is a
gating block
the attention block um
essentially weights some part of our
distribution slightly higher and then
the gating block
constrains or restricts that data out by
filtering it
and we are optimizing these
two
blocks using maxim entropy and the idea
with
optimizing through maximum entropy is to
allow for
some shifts in what's happening
um
and by shifts i mean to have a more
flexible representation because we're
trying to maximize the entropy of the
distribution
okay and this formulation allows us to
encode filter contingencies that can
dictate land preferences this is a
slightly different formulation built on
the same bayesian updates but we're
introducing this uh selected memory
component
um okay so i'm going to quickly go
through the experiments
um so we evaluated this um the two
algorithms in a 16 by 16 by 10 grid
world um so an example grid is here so
the agent is presented with this image
including its own location at each time
step and we've got four distinct states
so we've got red we've got blue we've
got the light green and the dark green
as well
and in this particular formulation
we have no reward or score outcome
modality so the agent is learning purely
on um
its um motivation to understand the
world and if there are questions about
that we can talk about it
um and the grid is change every k steps
and and the k determines how volatile
the environment is and at each uh
episode the agent is initialized in some
random applications so maybe here or
here
and that constrains how it interacts
with the world
um so for sake of time i might skip this
this bit um but
essentially uh the tables are
highlighting exactly what the training
parameters were and they were fairly
consistent um actually exactly the same
between the two algorithms so the pepper
formulation where we have had been
plasticity and the north formulation
we're doing um
non-reinforced um updates using
selective attention
and then the preference uh learning
parameters um that like how long the
planning horizon was um so it was 15 and
we have an episode length of 100 and we
do this for 50 episodes and we reset so
k
so k
is reset every 1 25 50 75 and 100 steps
and this gives us a nice way of
evaluating what's happening
um
so then the first thing we were
interested in was evaluating how the
preferences are shifting in a static
setting
um so this is one where we have hebbian
so this is
learning
um and this is where we have the
attentive um
gating measure here and with the heavy
and we can see the um so this is the on
the x-axis we have the states dimensions
and the y-axis we have the epochs or the
time consideration and this is the same
for both uh the figures that we've seen
at the moment
and we can see with the hebian one that
um
as we go further down it becomes more
concentrated and there's no really shift
here whereas for this um for the the
attentive uh preference planning um
measure we've got these random blocks
that appear that once they're before uh
but they also disappear so it's quite
interesting that over time the
preferences are shifting as a different
measure compared if you're doing a
qualitative assessment of the comparison
between the two
um and then the content and our post
talk uh analysis of trying to actually
understand what is happening
quantitatively we compared the heavy
learning formulation with the attentive
selective attention preference uh
formulation and then we compared it with
the baseline which is the expected free
energy of g
here
and on the y-axis we have the
environment volatility again this is the
k percent k but just denoted as percent
and then we on the y-axis we have
preference satisfaction and exploration
trade-off that we're using as orthodox
distance and this is just evaluating how
far particular trajectories have shifted
so what we're comparing um is
whether there's an increase exploration
or not depending on which preference
metric we're using because based on our
qualitative assessment that we saw
before there is this shift um between
the different uh encoding of preferences
given the
the the preference measurement sorry
formulation that you're using
so we can see that when we get to 50
volatility there is this shift from
exploitation to exploration um
for
the pepper algorithm and so we see that
here
based on this
nice
mode of the distribution that we're
seeing here whereas for the the new uh
formulation is slightly um
expanded out but it's not as
exploitative as the
pepper formulation
um
and then when we are looking at extreme
ends we can also see that there is this
shift from exploration exploration to
exploitation
um for
the pepper formulation but we don't
necessarily see it for the more
formulation so at the moment
there is some quantitative differences
in the way the two agents are evaluating
um
encoding preferences and how that shapes
the behavior
and this is just an example of the north
formulation in terms of how much it's
exploring the path
and the the way it's interacted with the
environment
so these are the grid worlds and this is
just a heat map of that
exploration trajectory
um then i'm just going to quickly do
some takeaways
um so both of the formulations that we
have even though
quantitatively and qualitatively they
are providing different ways of encoding
preferences they do have a tendency to
influence the agent behavior that's
different to the baseline or the
expected free energy where you didn't
allow for this change uh preference
assessment
and um if we are to compare with the
standard reinforcement learning setting
we are here casting what is preferred to
an agent instead of the environment or
the designer and it's particularly
important in a robotic setting where you
want to be able to
go back and allow the agent or a robot
to be able to shape some of its own
goals and objectives
purely if it's working in a more
creative setting maybe in
one in settings where it has to do a
really specific task this type of
formulation might not be the best
um but this does provide a flexible
formulation um where we're only
modifying the
the preference learning component and
using the same gender model so the the
initial general model that i defined for
the agent is kept consistent for both
the pepper and the normal formulation
but the behavior that we're getting is
through this additional component that
we add
um
but the the key thing to note is that
these preferences are a consequence of
learning suitable um learning a suitable
gender model so if your gender model
isn't that good then the way you would
learn the preferences themselves might
not be the best so there's a slight
trade-off um because whoever's designing
this formulation or working with this
foundation needs to take into account
how well the the gender model has been
encoded or launched by the gen agent
um and on that particular note i'm just
going to end the presentation um so
thank you so much everyone for listening
and i want to thank my quarters uh for
this great work and my funders and i've
got the the qr codes for both the the
papers if you're interested
um and that's it thank you
thank you
awesome talk
um
okay i'll just stop sharing and
you can
depart the room and you can rejoin for
the round table if you'd like otherwise
thanks again for joining
thank you so much have a good day bye
bye see you bye
awesome
all right the next talk is going to be
by wen hua chen
do a control for exploitation and
exploration and its applications in
robotic autonomous search
just one second
hi there yo
hi
one
all right we're back we're back with
with wen huachen
thanks again for joining and please take
it away
okay thanks for uh you want me to this
uh
particular meeting uh it's quite
interesting for me
and as we are not
i'm not always operating this particular
community so thanks for providing me
this uh chance to share my working
experience with you
so my talk is about how to uh develop a
autonomous search strategy for uh
robotics
and investing at a context about a
chemical biological and other
interesting
dispersion
so the approach i'm there is called due
control for exploration exploitation
and as you will see is actually a lot of
similarity with
the active influence
theory
so i came from uh loughborough
university i'm working
in the airspace and automotive and union
department so i have quite a strong
engineering
and background but not on the
neuroscience
so this is the best outline of my talk
and you can i can show you some
background about the application and
also
discuss
design method and then talk about the
simulation and experiment results
and also particularly i'm interested to
share with you about my thinking about
what are the relationship between the
the approach we discussed here and also
the active influence reinforcement
learning and other similar kind of area
and then talk about what is the way move
forward
so and let's talk about the autonomous
search as the case study
so this is a
so basically they can why they found it
in the natural environment and for the
the polar bear if they try to find the
prey or the food
and they need to use a small audience
and also similarly you can find insects
if they are such mating and other food
they can use similar kind of strategy
the idea here is and by
making use of the sensors they are near
to reasoning about where the food or the
soil might be then think about it what
is the best strategy in order to find it
and particularly interesting for us is
how to convert this um
in kind of intelligence from natural
world into the engineering area so we
are able to teach robots or uavs try to
search and be chemical marriage and
resources and also and in the future you
can be using for
environmental uh force uh
enforcement for example and try to fund
the protein aware resources and many
many other applications so basically you
can think about it the idea here is
somehow like you try to develop
a small dog which can slip around them
try to find the drugs and other
endangered materials
this is not a new area there are lots of
research in the area and particularly
bio inspired a lot of research
people can be using and the campbell
texas or and
the other
reactive strategy like you fly down the
wing if you found something you try to
follow the trace in order to search the
resources
another mainstream uh
working this area is based on we call
the information theory approach which is
uh you treat this kind of process
as a information game process
somehow at the beginning you don't know
where are the sources and you have high
level of anxiety then during your search
you drive the level also in the lower
and lower so this is actually is that
you can think about it this is a
information game and then you can using
the reward function like entropy like
the uh
k or divergence of many others to
measure
the success of your search and then
based on that you can derive the
strategy to driving to do this but now
we're not we're looking to another angle
and we treated it as a control problem
and then think about how to
link this with a active interference
the same kind of work
so when we
try to search the uh
a source and you don't need any
information so basically on the robot
you have a chemical or biology agent gas
sensors
and then based on that every time you
need to reason where you need to move
your robot
in order to have best chance to find
the source so there is a strong
interaction between the robot and the
environment and the environment rover
and also they have a strong impact
coupling between the
the perception
and uh and any decision making so
basically if you decide to go to
different location and then you will
take a different kind of chemical sensor
maybe this will
affect your belief about where the
source might be
and this will also change your cause of
action because based on that you need to
decide where you want to move in the
next step so there is a strong covering
between the perception
and
the planning or action
so and this is also a typical example of
the
cycle that you need to trade off between
the exploitation exploration so you need
to maximize your chance
so a lot of people in this field are
much familiar with this kind of trailer
i will not go into the
detail now i will try to explain to you
about the strategy uh whether we have
development
so and now we try to formulate the
problem and uh and there are some
methods here and you can ignore that but
they try to understand the high level
understanding and what the the math here
is each time we have a x which is a
state of the agent of the robot and also
you have a variable set of action you
want to take and which is basically try
to make the robot move forward backwards
or left and right to move to different
direction with different
step size
and also you have the moments the
measurements in this case is you are
first is your gas magnet on the on on
the sensor you can have chemical sensors
on the on the robot and also you have
send the moment about your position or
your location with respect to the
environment
and the other things that we have is the
unknown information about the source and
also about the environment
and which will include the location of
their source
and also include that
constant environment like the wind
direction and the speed which will
significantly affect the dispersion of
the chemicals or any uh audio
so and the idea here is you take the
connect all the data during the process
and which is included anytime the action
you take which is you
and also the sensory sensor measurement
but which is that here
so you add all together give you
something we call the information state
which is a connection about all the data
you have so far
and then we decide what is a cost
function or reward function it should be
and in the simplest way what do you
think about okay and my aim is to try to
move my robot position close to the
source location as close as possible
which is quite a sensible uh
the mayor but the problem now is i don't
know where the source is location
resolves it so what is this is why the
condition on all the data is connected
so far
so it conditions this one trying to
minimize this cost function
which is a typical way and in our
control community and there is a
particular name called the stochastic
mtc model for the control
and but what we want to do is move away
from this just doing this we want to uh
to further and because this will move
further this is actually beautiful link
with the active inference
so what we do is now okay we're not just
the conditional on the other data we
connect so far but also we connected on
some
virtual data so what is the basically is
we also added the future
all the the actions and what are the
future outcomes so somewhat because you
have a model he said oh if i do this
what is going to happen what kind of
moment i'm going to get if i do another
thing what can moment i'm going to get
and how this man will affect my belief
of the world of the environment
so that it means i now condition on not
only on the ik but also condition on ik
plus one and here and we need to have
taking into account
the
contraction on our future measurements
and how future amendments will affect
our belief
okay but you know before i introduce the
uh the detailed mathematics a little
more method i try to give you uh some
definition of mutation
so suppose any time you have the
probability density function of any
unknown parameter theta you want
estimate this is a
pdf for b density function of that and
if we take the the mean the expectation
of that this will give you something we
call the nominal estimation
okay use the mean of that as your
nominal estimation and you try driving
europe maybe to the nominal estimation
location
as a matter okay but also we have to
quantify how the uncertain level of this
estimation
so how reliable this your estimation
about the environment so basically we
define the error between them and then
the nominal one and from any
measurements then this will actually
give us as a variance it will define the
variance of this
one so uh and once we
have this notation we can simplify the
cost function we had before like like
here but now is the condition around i k
plus one and it can simplify it into two
terms the first term is about okay
so
we it may be the uh the active inference
we call
extrinsic value the second one is the
intrinsic value the first part is okay i
want to move my robot location to that
believe the source location which is
denoted by the normal estimation of your
as a targeted
location you want to make this error as
close as possible so this is the task
you want to perform something to
basically move your robot close to where
you believe it might be
the second is how reliable disbelief
and we quantify here by using the
variance and initially remember those
two relationship is derived from the
very best
the cost function there's no weight
between the u2 is naturally this is the
optimal way if you minimize this
naturally the optimal way to do it
so that that this the cost functions
consist of two terms here which is uh
the task of the objective you want to
perform and the uncertainty of your
belief so you have that extrinsic and
also interesting values
and optimal to combine them together
okay so now we can go to a little bit
more detail about the equations and i
will not go into too much but it
basically is somehow like this is the
best agency equation like as a next time
the robot position depends on the your
actions and also you have the dispersion
model which is somehow like a ghosting
model but it also depends on a number of
parameters which is uh the wind speed
wind direction what kind of chemicals
you have they have some lifetime uh in
the in the in the state in the air and
then some other uh parameter associated
with the
location of the source
but also we try to model the sensors and
you should we should know that in the uh
in the environment the chemical and also
those viral agents their kind of changes
are really low and many times it may be
not able to detect anything
but also you should also know they have
lots of local turbulence which upset
your sensor so that it means a lot of
time you couldn't follow the gradient
method try to say oh i fold the gradient
i found the maximum
concentration no it didn't work this is
maybe what it looks like after the
true dispersion fields you can see the
concentration change quite dramatically
so that's a challenging so we also need
to
model in the sense of behavior
somehow like
when the sensor you can have a reading
so it's true reading plus some sensor
noise whether many times you don't have
sensor reading
and so you just have purely have a
background noise of your sensor so this
is another point
and once we do that and we have the uh
try to try to see what are the unknown
parameters about the environment of our
source one estimate so basketball
include the wind speed and the direct
direction and and other things
associated with the chemical components
or i know them that parameters
associated with the target i think it is
the source location the release rate and
then we can be using uh in our framework
we're using basic uh inference uh to do
to do it uh try to estimate those
parameters
so this is what the diagram looks like
and so basically you have two parts one
is about the reasoning another part is
about the planning or control action in
the rhythm every time it takes a new
measurement and you based on the prior
information and the and the model you
have this way more and you try to update
your kind of visual estimation and then
you build up a previous map about your
local environment and then you fit this
into your planning uh that here you try
to estimate if you take any con action
what's the influence about your belief
and always how to make your uh agent
close to the source so you do the
planning here and is this somehow like
this red box is somehow like that you
tried using your virtual or
a moment to do the reasoning and repeat
this again and give you a dedication and
then just keep doing this
and so you can do some simulation study
about this for example if we start from
here this is source this is a kind of
changing and then we can put the source
in different locations and as a agency
different location to see how they are
performed and then try to understand
the behavior performance and what we can
see is that
if we quantify the performance in two
ways one way is we call the successful
rate which is a and if we run the
simulation 100 times or excellent 100
times uh what's a successful rate so for
the new approach you can achieve about
100
and for the uh some entropy based
original hour method you can achieve
about eighty percent chance found that
if we're using uh classical model free
control you always have about around
eighty percent of chance to found this
another uh the mayor is about how
quickly your conversion move to the the
true source location which is denuded by
distance uh from the agent to the
source
in terms of the root mean square because
you run it many times and what you can
see uh the our approach is actually can
decrease very convergent to the source
very quickly and but others is open
slowly converge into that
and we also can do the experiment this
is exciting bit you can put on the
physical uh robots try to let it wrong
and then you can do that
using the software to
implement your high level argument at a
low level you also have a control loop
try to command your robot try to follow
drive it and follow your high level uh
the division to see where you want to
move that really will follow that we're
using the sensors and also and
some level control to do it so here's
some uh
explaining result you can see it's very
turbulent and the conditions change
quite quickly the robot starts from any
points and there's a purple point
giving your idea about is that believe
where the source smile being represented
by particle filters you can see with the
time goes they're concentrating too uh
closely and
then to the um the location of the soil
source and this is uh after that you can
measure the area give you the idea about
the concentration uh in this particular
area and also we can do that in flight
outside using your implement all the
strategy on the uavs and the real test
you can have the uh chemical sensors
here this is a and
all the other gps the cameras and all
the sensors and you have a low level uh
the ground control station are here
and then you can do all the experiment
outside they can this is a trial on the
chemical plants they have a leakage of
the gas and then what even happened and
you can see uh the test and we did it
and then
and
the industrial side and the uav taking
off and they got the chemical sensors on
that and they they don't lose and where
are the sources they're based on that
they give up some search strategy when i
first started with we didn't do the
intelligent research we just let the uav
to fly around try to pick up the data
and then we moved to intelligent
research and try to demonstrate that so
that pretend someone died because the
the chemical
leakage and then you need to send the
uav to
to identify where the uh the problem and
then first respond can take a proper
action
to this
so then we can map in the area this is
not the intelligent such one but it
justify wrongly to connect the data
beautiful understanding you can say
where are they are but then we move to a
fully uh intelligent search and then is
somehow like hands off we don't have
anyone that's that is fully that you're
able to decide where to find to connect
the data and them and and the child
understand where they're so smiling
could it be
and this is another scenario i can see
here and you have
the car here maybe this is simulated
environment you have vehicle involving
the accident whether you have any uh
petrol a liquid to that because this
might be it means you have a risk of the
explosion under them if you send the
first responder to this area that were
under the higher risk so if you could
have an agent to be there try to search
uh where have any uh potential and
leakage of gas under the um
where there might be then you found
found them
so that's uh
and there's some idea about it and doing
the this kind of research and
and then we also and
develop this extent this one to more
broad applications a particular one we
call the self optimization control that
the idea is for any uh or mozart
system you want to maintain it operate
in best possible way
which can change with the environment
because the way the environment changes
the best possible operation way for the
changes however you want you are
you have a consistent and by taking the
same idea as we already talked about
they're able to explore the environment
influence on them they understand how to
best operate themselves so somehow like
here just change your environment and
reward the function you just try to
follow that and then try to do the best
so there's many many applications i just
talked about one this is a situation
where we have you is about reliable
energy you have a pv farm uh the energy
and the aim is very simple
you try to harvest as much energy as
possible but the problem is the optimal
operation is changing with the
environment with the sunshine the
temperature the the
the sonar insulation has changed your
operation
optimal operation so what we developed
is a strategy no matter what kind of
weather condition you always can
maintain the solar farm open in the best
possible way it could be so the red one
is ideal one
the
green one is actually what we uh
the blue one is what we did you try to
follow the optimal this is optimal
operation we always try to follow
so that's some examples not only for the
autonomous search but we can use
australia
to solve much wider range of problems
now we talk about that relationship with
some others uh
existing work one is sunday is a due
country concept
why we call dew control because the
control action is not only changing your
physical behavior of the u.s
system but also changing your belief of
the world of the environment so this is
why you call it due control but it
however is not complete new con concept
in the control community we did this
before but many on the dynamic system
are estimate your own state how to
understand some of your own parameters
the idea now is try to extend from uh
uav for example itself
understand itself it's more to the
environment because we think about it
for
autonomous driving for the uavs we have
all those information about ourselves
what we really need is the enviro
information about the environment
answering about the environment
another link is uh with the uh
the active uh in uh inference uh the the
community and this is a very uh
interesting surprise funding from me
because when i developed a strategy i
don't have any idea about this community
and is that somehow like you can start
from completely different area different
angle but however you found that you're
landing on the similar kind of idea or
area so this is i think one of the most
exciting things
in this
research so so basically you can think
about it is that uh that you control the
idea is also about that your action will
change uh
your belief about the uh uh the
environment and the you then connect the
information this will again change your
belief about that so there's the
interaction between the action and the
perception and how they're connected
with each other
so i will not explain too much
especially in this country people maybe
must understand what i'm talking about
and another is about it it's linked with
us yeah it's linked with uh
the world by the way there are some
other research in this area another is
about the reinforcement learning and
this is my view about the link within
reinforcement learning so basically the
reinforcement learning is trying to make
an optimal dedication for a given
dynamic system and subject a
reward function and then it proven
itself converging to uh
found a solution for a beyond equation
basically
and then what a reinforcement learning
though is
how to solve this problem by
the optimal value function and also try
to find the uh option uh personally
found that
optimal uh policy so idea you try to
learn the strategy by through the
iteration but what we do is that from uh
the work i'm doing is developed from
something we call that modal project
control we try to solve the same problem
but however with uh truncated the
infinite horizon problem into uh
finally the horizon problem so every
time we try to solve uh find the horizon
optimization problem find
the uh optimal solution but uh
reinforce them early and try to do using
the iteration uh like uh uh
learning try to do that so basically and
and the whole idea about link between
them is actually explaining this paper
and i just the publisher if anyone in
the community interested in this and
again please have a look this is my view
about a link between those two and also
it's a link with active interference
so and
because the approach are different i
just given the conclusion for the
reinforcement learning they have three
major problems i think about it one is
they need a lot of data to help them to
learning the optimal strategy
opportunity function and the second is
once if you learn from the simulation
environment when the environment changes
and oh there is a mismatch between your
simulation environment the real
environment the optimal strategy learned
in a simulation environment will not
work very well in real life and in
particular in this case if i learn the
try to search the
sourcing
based on this environment okay the wind
comes to this direction speed i learned
how to do it but if you come to real
emergent situation the wing is actually
blue to this direction
the strategy you learn maybe doesn't
work at all because it's not optimal
another problem is actually that
being frozen like black box is very
difficult to prove the stability or
safety this kind of thing but we don't
have
in the control we have a rich body of
tools we are able to prove the stability
safety and other things i think the
first tool is able to solve by active
inference as well like a new reducer the
number of data required and also that
have to deal with the unknown
environment but however that controls
also have another uh office which is
about safety
about this so this is a quick try to
think about how the link between the
approach to talk about here and the
reinforcement learning
and and then we can discuss more itself
for this particular talk then the the
the kind of work whatever we are doing
we try to
move this from single step to multiple
stack looking ahead and the final
horizon but this will have a problem
about a computational load because now
we have to deal with a much higher
capability how to reduce the
combinational load is quite difficult
and and last time when i talked with a
car freeze it gave me some ideas about
the team how to do it we are trying to
learn from your community about how to
reduce
the
computation alone
another thing is what we are doing is we
try to prove that a sense of rigorous
properties for the
approach somehow like to try to prove
they can converge into the two sources
and there if you do anything there your
belief can converge into true as a the
external environment under them and and
also and
you are able to prove the safety of that
which is particularly important for our
area when we deal with cars and
aircrafts we have to prove it is safe to
do it so we are working on in those
areas
yeah so um yeah conclusion is uh
we develop some new framework in our way
and we try to
make system cam operating on the
environment by uh
somehow like a trade-off between the
exploitation exploration and try to
understand the future action is
influence on our belief so this is uh
can deal with the coupling between the
action and the belief and
and then
our approach is not somehow like many
other approaches they are saying about
uh if you want to trade off your
artificial stitches uh uh interesting or
extrinsic values together add some
weight and it's actually this is
naturally it happened this is a
it is optimal in some way
and the particular center for us i think
about it is we have a particular aware
of the community of active experience we
can learn a lot from there because they
have a
community here people working in this
area develop many good ideas and the
question is how to send it to that how
to promote more collaboration between
those two communities i would think it's
one of the very interesting things to do
so yeah that's all of my
talk i think i very much come to the end
of my time yeah it's 29 minutes now yeah
so that's good
okay yeah thanks yeah so i will join the
roundtable yeah thank you
yes okay thank you i will leave it first
and we do join
okay thank you
all right well welcome back everyone
so as it turns out
we may or may not have any
people join we will have just one
join right now and then we'll see who
else joins and
so welcome back when what
um
was just saying that anyone who's in
the live chat please feel free
to
write any questions in the chat and
we'll be looking at them
when hua not sure who else will be
joining us but i think actually this
will be a a
great opportunity just for as short as
long as you'd like
to talk a little bit about
a little more about what you presented
on and also connect to some threads that
were happening earlier in the
presentations how does that sound and
we'll see who else joins
sound good
i actually don't hear you anymore
okay one second we'll figure this out
yes
alright so we can hear you now um yeah
okay sorry all right
welcome so
um
we'll
talk about some of the previous
presentations not sure which ones you've
seen and otherwise i'd like to pick up
on a few threads in your presentation
um
and then we'll take any questions that
people are asking live how does that
sound
yeah um
awesome so
one point that you highlighted was this
notion of dual control
and how it brought you to some of the
similar
places that active inference has arrived
at so i'm curious what you think
led to that
and
what led to those vectors intersecting
in a dual control
and what is at that nexus or why does it
exist that way and why is it coming
clearer to the forefront at this time
yeah thanks for that that's a very
interesting question i know also i i
also think about it myself from time to
time
i think that there is a
certainly those two areas i feel
original was quite far away uh we have
different strategies different way to
think about the the world
typically control we normally we are
interested in uh as i said the due
control concept uh is not
entirely new
and uh the people in the in the control
community already realized that many
years ago
somehow like if you take any action the
action we are not a changing behavior of
a dynamic system but also maybe you
could have
some influence
on
the variables you are interested in in
tragic traditional control this could be
for a physical system there are some
parameters yourself
like a mess or a damping or other uh
things that you don't know
you by doing that will help you
understand what you really are just like
when you're driving your car you have
some river you know what i mess or
inertia my car have by doing some
certain action
so the people realized that uh before
but the difference is now because we
control the move from uh typical maybe
can talk about low level automation now
move to high level we call that
intelligence or automation uh autonomy
okay now you move to the more higher so
then that means that you cheated that
dynamics is like more like an agent in
our way in our languages computer
science or neuroscience is an agent so
now we're more interested in not only
about ourselves more interesting about
the environment surrounding us the
outside so my the work i think is now
progress like what i did is move from
you're concerned about your agent
yourself more about what are the
environment
surrounding you how to explore the
environment how to understand your
behavior in the environment so by doing
this i feel we bring the typical
engineering heart
sorry the control in feed into
this kind of natural water in this kind
of biological kind of sense because now
you're more interested in how to deal
with coexisting with the environment how
do we know so this is why i view on this
and but on the other side this is also
what i i reading on the on the active
inference but suddenly this community
have more say i feel traditionally
before the due control people already
have some idea about a treat human brain
as a basing machine
so now he said okay i have prior
information about the environment i have
a new data coming helping you understand
what is happening around me about the
environment but i think what active
interference
for me i think about it
suddenly the other wrong side of how we
define the reward function and in
particular talk about it using free
energy to quantify that this is really
wonderful to the world but also i think
about it is key things here is
is about
you now think about it i action the
action is also linked with my uh
understanding of the environment about
perception so the carbon so using the
action to explore uh
the environment gives you better
understanding
so that it means you move from just that
to the human as a passive way to receive
the information from the environment
nowadays that i can actively do
something helping me to better on the
same one so i feel this may this is my
understanding that the key feature of
active inference so because this is the
reason you can see the naturally will
link with the control we talk about it
because the control normally talk about
what is consequence of your action how
to take the best action
so this is why i feel those two areas
they from quite a different area
gradually because the need for the
research and also
something like a trend in the field they
are now moved together
in this particular area
they come conversion
to each other so this is
what i'm thinking about
awesome if i can just like
pull out a few threads that i i thought
were really insightful there
so
you you cited a paper from the 70s about
this dual controlled notion the idea
that we had to have not just like a
single imperative or have an imperative
that contained epistemic and pragmatic
components and all that that entails
like the unknown consequences of action
so what we would have is like expected
free energy as opposed to the
variational free energy and then
you you described how there was a
movement from lower level automation
control systems
the classical thermostat and other kind
of like um single variable yep single
fixed point implementations
and then
as the implementation complexity
approaches the multi-joint
and way way way beyond how that
multi-joint is going to be in a social
context or
a changing environment
that
system that's being designed
comes to convergently require
the same imperatives of a nervous system
which is to say like the real-time
integration of sparse
sensory data and also that is what
authorizes
the ecological stance and the embedded
cognitive perspective which ties in with
some other recent threads in
cognitive science and neuroscience like
the pragmatic turn
and so it really is interesting how like
from the technical capacity side
the questions that were converged upon
in terms of memory and forgetting and
all these things
are like the challenges that natural
systems have been involved in solving
for a long time
yeah and that's absolutely right that's
a very very interesting part of their
technology develop but also there is a
maybe demand from the society and
because of lots of things like of the
traditional mechanical thermal kind of a
simple control already while existing
they help us to boost our productivity
for many years but now we reach to the
stage we want to further increase our
productivity increase our efficiency you
have to develop a highly automatic
system and which is able to deal with
some unexpected events
uncertainty and so in order to have this
kind of uh like capability
they also require a high level of
intelligence like our human or animal so
this is actually another reason the
technology of the move is because
the society and economic the demand for
this kind of thing to happen
okay i have another question about your
uh scenarios that you explored
how
is explore exploit balanced
automatically how can such a a large
statement be made
and how is it balanced when risk is in
play like risk of going into a dangerous
area so within the search task how is
explore exploit
uh mediated
and then how does that become
more complex or how is it integrated in
the model when bodily injury is on the
table
yeah thanks for this yeah that's very
interesting question and uh also we
try to and think about this along
ourselves for a while and the first i
would like to say for just using the
autonomous such this particular
examples to illustrate the key ideas
and
the the fundamental objective for this
particular task is very simple or clear
somehow like based on my understanding i
try to move our agent try to move close
to
real life
to resources okay so
under them they will formulate this as a
reward function or cost function somehow
like you want to move your next times
agent the location to
the source
location as much as possible but however
because you don't know that so there'll
be conditional on all the information it
connects so far
so this is a the reward function your
origin defined but from there we derived
this particular function if
formulating this kind of way and then
and also try to introduce the
the note about it the action will affect
our belief and then we'll naturally you
found the cost function or the order
function becomes
two terms won't consider two terms long
term is about the exploitation another
term is about uh exploration so there's
a natural happening there is no like you
need to introduce some terms or they
just naturally come together in this
kind of way so this is why we think
about is
maybe that is
the best way to try to do that but also
you you you mentioned a very good
question about the risk for example if
they naturally you're not only something
like a target they want to follow but
also during the process you need to
aware of kind of
risk there so
normally you have to deal with in our
framework in two ways one way is we have
to add some constraints in our
action generation it means for example
one example is in our search if there is
a obstacle in some way if you command
your vehicles or aircraft move to that
direction suddenly this risk because the
client is going to collide with the
obstacles we added the constraints in
the search domain you said in this area
you couldn't go this is one way to do
that but also you can add some we call
it called softer constraints that means
in the cost function you add some
penalty in your cost function said okay
there is some area
might have some risk you try to avoid if
possible
and that when you generate or optimize
your uh your action you try to take this
into account
all right awesome i want to connect that
to active inference and then ask a great
question from dave
so you mentioned
how
various constraints could be provided to
prevent like situations of of risk or
hazard to the entity
and so that
is uh what may work in practice and so
that's why it's been so interesting in
the presentations to see that
most of them have featured at the very
least um a laboratory robot
context
and that kind of makes the full stack
make makes uh increases our confidence
that the full stack kind of touches like
there's like a tesla coil like there is
a path through
some implementation and then the
question is how deep in the specifics do
you have to go versus how um far up in
the generalities
and then there might be some
situations where the constraint is
applied in a very situational way
but also
as you
laid out
dual control and reinforcement learning
you said reinforcement learning is not
really amenable to being
formalized analytically in practice
whereas um one active inference strategy
that we've seen to balance like a task
performance with survival is you say i
want to reduce my surprise about the gas
cloud and i want to reduce surprise and
have a high battery percentage
so then
it will
just like balancing explore exploit
within a drive like to detect the gas or
to stay high battery it also can have a
nested model that's balancing those
drives
and so there's also an
analytically
simple and first principles way
to
bring homeostasis and risk avoidance
into very generalized framings of the
active inference framework
and then again in the specifics it might
be useful to do different model uh
variations closer to the edge but then
it's very interesting to think about
what it looks like when also there's
something in the center
that has a simplicity to it
yeah yeah yeah thanks for that that's a
very useful discussion
uh
are different ways we can deal with the
balance between the uh you want to do
what you want to do and also try to
avoid any risk or beautifuls and then
try to balance try to deal with
particularly i think the problem here
my feeling is called uncertainty
because on sunday will have
affect all those things because if you
think about risk how relia
how possible reliability this risk might
be so there is a lot of things like this
and
my uh
this will come back to my uh my
fellowship my fellowship was funded by
epsrc for five years i concentrated on
this particular area the goal of my
fellowship as we already somehow
indicated we tried to increase the level
of autonomy by if there's more
intelligence arguing into the control
and and on other
field but one of the the idea for me is
i we could
want to develop something we call that
goal oriented control system it means we
want to promote because high level of
intelligence like us
people or animals
they are more have a goal-oriented
behavior you rather than just people you
said oh i give you the goal you try to
figure out how to do it if you have a
next intelligent one he said oh i need
to give you instruction every step about
how to do things properly so the first
is
to promote the goal in the behavior i
said okay for this particular what is
the task what do we want to achieve what
a requirement
so then second things in the key
integrating my framework is about the
constraints the why the constraint is so
important because you try to avoid any
like before any risk of things or
for example if you want to develop
autonomous driving cars you have to
follow the
rule of the traffic at the road and they
have to follow that and they have
followed the traffic light and other
things
and they and you don't want to collide
with any other vehicles or uh or hit any
potential so those are the constraints
you have safety concerns in this case
but you also have a lot of physical
constraints because if they have a
maximum power
maximum like temperature or pressure
your system could have otherwise you are
going to destroy yourself so constraints
play a very key role here but the sunday
the question as you said four different
scenarios how to abstract formula this
constraints is a question but the whole
idea is you have to for any decision or
action you made you have to respect
those constraints
before you try to think about oh wow
won't achieve any uh meaningful
objective the another key
part of this one is uncertainty
the onsen they came from many many ways
could be the environmental changes or
onsen we already talked about it but
also could be answered about your
information because you have a sensor
sensor could have error or the sensor
range is not enough to pick up all the
information you need and there is a yeah
so there are so and also you answer
their body your belief of the world for
example we talk about the
risk but how reliable this risk it'll be
could it be
so that i will think about it and this
is my belief in the whole framework
for uh you control
the key thing is about how to quantify
the answer
about your belief of the surrounding
environment
this is driving you are you rewarded
somehow like
expert
exploration
so those are the key things in my view
and basically if what our idealization
is think about you talk about in the
active
inference we are able to formulate that
in electrical way
and then we are formulated in electrical
way we are able to using some tools or
theory people developing the last 30 50
years in particular in the control
community and other community we're able
to formally prove if we do it in this
way we can make sure you are able to
satisfy certain safety requirement it
will not hit the some obstacles you'll
not put yourself in the danger in the
for example like you eat in the natural
world either by other animals for
example so so
you this is the dream we have some
progress in this area we're already able
to do some a very simple system we are
able to prove stability or safety of the
uh that you control but however is and
we want to do is try to extend a much
wider world and therefore the free
energy principle
is much more difficult because the
energy the functioning level is quite
complicated how to understand that is
another level of difficult but however
in principle we are able to work
together to push this
thank you there was really a lot in
there i'd like to make one remark on
active inference
and then bridge to
dave's question in the chat
so you highlighted uncertainty
and that's of course a core aspect of
active inference with bounding surprise
using free energy and then you mentioned
goals and constraints
and that really seemed to me like a a
common point with cybernetics and goal
orientation constraints general systems
theory cybernetics branch but also
engineering and entrepreneurship and
innovation as your colleague stephen fox
has
worked on
and those perspectives on goals and
constraints of potentially nested
systems of organization like projects
within an organization
or
a firm within a market
or a cyber physical system nested within
a firm within a market
yeah to have interfaces
that can even just be described
in an information partition way
and then you brought it back to safety
and to be able to have certain like
probabilistic or formal guarantees on
those kinds of arbitrarily composed
systems
is very exciting direction um any
remarks on that or i'll ask the question
from dave
i just have a quick remark i think it
really
for me i'm more on the technology side
but however is absolute this kind of
goal in the behavior you can using for
the social organization for the
biological or many many other things
because basically when you survive you
have a goal this goal you try to survive
on the food and then the society you
want a new organization the goal is to
try to find more profit constrained by
the kind of marketing environment and
many other things yeah yeah i absolutely
agree with you
i'm just gonna make one more comment to
refer back to an earlier talk not sure
if you saw this one but this was tim
verbellen's talk and he was talking
about video games
and about how just with a only
a
epistemic drive
some of these video games were able to
be played very well like with pong and
with mario and then it made me think
about how in a lot of video games
staying alive is an imperative whether
you're just tapping something or a maze
or something that's growing or shrinking
it's like staying alive
bridges the gap between
search and exploit and all these
different behavioral modes it's like if
you're not staying alive if there's no
like idle process for your cpu
then it's over so then yeah there's no
point in future epochs so that's
really interesting so let me go to
dave's question
so dave uh wrote
professor chen i didn't notice
discussion in your presentation of of
affect or emotion or drive
what do you think about adding such
mechanisms to the dual control model
could this amount to explicating
internally generated motivations
or would such a trick be a mere disguise
for inserting arbitrary experience
experimenter specified rewards
yeah
that's that's very interesting question
and when am i
reading the uh literature in active
inference and i'm fully aware of that
the focus of our research is quite a
layer and we focus on do something uh
specific or useful and in this case for
example in the case uh the autonomous
search is just try to find
uh
the location resources and in the in the
pv farm for generated renewable energy
the object is quite simple said okay we
want to harvest as much energy as
possible given the condition so in that
one means
the focus of our one is a
very specific but however when we come
to the biological and also human and
others they have a lot of things like
the the emotion and many other things we
didn't consider in to in our current
work and i i can see this is the gap
between the due control and the active
inference is actually you can deal with
talk about a more general uh skills like
empower or confidence or some other more
things emotional things
and and this is actually the direction
of the maybe the future of the and our
work should move try to learn from this
community over that but in principle and
as i said if we are able to formulate
those kind of emotions or many other
things as kind of a reward function for
example you you you encourage people to
be happy to but you need to have some
way to quantify that if you couldn't uh
capture that maybe you will not promote
the behavior uh try to
get make you happier so that is the key
things for us is how to uh formulate uh
interesting uh
reward function and and this is also
what you can learn from active inference
in principle and we didn't have a
restriction on what time
what type of
reward function should it be what type
of constraints should it be the
framework is quite
in some ways quite a
general but however for more complicated
systems still did a lot of work yeah
that's very interesting
if i could uh build on that so i was
imagining the setting of
firefighters and there's some
different chemicals that are being
sensed
and about the way that the extended
cognition paradigm and seeing the cyber
physical team
as being just qualitatively whatever
tools they're using even if it's just
the walkie-talkie
and their bodies it's still like an
extended cyber physical team and then
as we move forward into futures that may
in different areas like include all
kinds of tools that we do and don't know
about
so then that's what's interesting about
a framework that can start and pick up
in the um
like qualitative zone
and then also take it all the way to the
application
and then as to value alignment i thought
that what you just added had um some
seeds of
new ways to think about the human
robot or just more generally the
multi-entity alignment question and that
is their preference vectors or some of
their preference vectors
could be about the same thing and in the
same direction like the semantics of
what the firefighter on the survey says
i want i want to like balance x and y
and z in this ratio and then there can
be an entity
whether that's another person
or some kind of explicitly structured
cyber physical entity that also has that
same like preference distribution
and then yeah
that is like a formal way
to find that probabilistic alignment
because the question has to be addressed
one way or the other and how will those
distributions align accidentally
or using some other simple heuristic
yeah that's absolute is actually when we
talk with our end user and also
firefighter and also the
minister of defense they're interesting
therefore the terrorist attack or some
other kind of things you know in
london in the tube station there's some
scenario like this and here they'll talk
about is
very rarely just send the robot out and
let it do
off do all the things he's actually
always have an interaction between the
first responder and the robot really
want to pass the information about oh
where i thought it might be and then the
the the operator first to provide some
extra information and they'll always
work together as a team and also there's
some preferences for example in some
areas based on the
first responders experience they knew
where they are more likely could it be
that when they see a picture or see the
season so there is always the
interaction with that yeah absolutely
this is actually our future step is
somehow like to promote this kind of
interaction between the human that in in
some interference and many other
emotional other urgent things because
some area if you close to maybe
exit or somebody you maybe
have a priority to search or find
whether there's some probe there so
okay a few remarks on that so it made me
think about how
the response
network like of an emergency could be
seen as embodying a prior like where i
am in california maybe firefights are a
certain likelihood different seasons so
then
um a phone call to emergency services
might have a different likelihood of
something being the case in one region
versus another or it could be kind of
used in like a bayesian filtering way
where are we getting 15 reports of the
same thing and then where are we like
we're already
working on that situation and there's
something else that needs attention to
be brought to it so we don't want to
like have a sampling bias and then that
question of how training data
in a static learning context
results in basically like biased
implementations in the real world was
was a theme of several of the talks um
a question i wanted to ask was about the
turbulence
of the
flow
it brings a
chaotic
multi-peak landscape because what i saw
in the cloud was there's like it's like
island chain
it's not just one ridge
and so um
how does a
smooth gaussian variational
approximation
make sense of something that otherwise
we might think we would use like complex
simulations to resolve
i think you're a really expert that's a
really good question and we struggle
with this for quite a while and
and
you can think about that
you have a lot of local turbulence is
there and also uh com coupled with
any case if you have a chemical biology
dispersion the concentration of the air
is actually really low
and and also for our uav the small
drones or the uh the robot the sensors
they carry is not very advanced you
can't carry some level uh grade very
comprehensive equivalent is actually we
use a very simple uh gas sensor so that
means you have a high level of
that mis detection or and and also this
what makes it even worse is because you
talk about it that the turbulence you
can make and when we operate on the uav
the propeller
didn't help us it itself it generates
lots of local fluid it's upset our
sensor so it's hard now it's somewhat
appreciated lots of hard work getting
into this area but but try to answer
your question is
and when we uh reasoning
we could use a more complicated model
but however the complicated model
sometimes didn't give us in this case
didn't give us too much benefit for to
reading one reason is uh the complicated
model is always have a um because the
environment have a high level of
uncertainty
and even you have a complicated model if
it's accuracy to represent a real
environment then that's a complete model
give you benefit you feel that come the
model
is environment is so much uncertain
there maybe the simple good enough model
is able to do the job there's a first
question but also by using a simple
model it can signify driving you a
computational lower down the simple
gaussian mode it is very simple but
however you are able to driving your
computational lower down because
compared with a
safety model computational fluid
dynamics mode or more complicated model
uh second is because there's a
particular scenario
the uh the sensor is not high grade so a
lot of onsen they caused by model maybe
uh just the uh
display
within the sensor noise because that
noise is quite high even you try to push
it more and more and more accurately but
it's just maybe one percent since the
sensor lawyers give you five percent so
it didn't give you too much benefit this
is what we found in this situation
so i'd like to
maybe connect that
gas dissipating
setting to one of the earlier talks and
again not sure um if you saw it but just
to kind of recapitulate the point so
this was from tim schneider's talk
and tim spoke about goal-driven active
exploration so i'm sure that there would
be a lot of resonance there with the
um
dual model
and one of the questions that he really
highlighted was he asked can the
familiar have intrinsic value
because he described this uh
problem called the detachment problem
where like a region of high
posterior likelihood a good region to be
in
is getting walled off by like a
well-explored region and so that
dissuades further epistemically driven
actions into that kind of ring
it's almost like we've already been
there but then it's like
the you know the the new finding was
just one more paper down that down that
bridge um yeah and then
we talk a lot in active inference about
morphological computation and body
computation and i think in the setting
of the gas dissipating there are several
ways like we can be really specific when
we're talking about applied embodied
computation so one was what you just
mentioned with the uavs and the fans and
how that was causing a distortion it
wasn't just like a free-floating sensor
and that's like our own body models and
so people talk about how the body is a
model and it has a model of itself in
space and that's how we can do all these
actions um and then the second example
of like embodied and extended cognition
was the way that the gas was dissipating
so it's almost like the forgetting in
the model was happening automatically
because you couldn't just build up
a heat map
of where of you know the integral of gas
flowing through a region of time
you have to have something that is
dynamic but you're local
searching a space
and so your estimate in other areas that
are distal will become increasingly
uncertain
so yeah what does that make you think
about in terms of the work that you're
doing
yeah all those things are very
interesting there are many directions
for that and we we think about it the
work we're doing here is just try to
illustrate the very best principle about
how to
take the advantage of the um the action
you take to give you the new information
and then from there to help you so this
is basically as we talk about bear the
same spirit as a active inference so
this is the fundamental things and in
terms of scenario and the complexity
there are many many layers so we can add
the things on and also one thing you
mentioned about the uh
for example the influence of the uh
the agent or the robot is dynamics but
also it could be for example we consider
a source now is in the in the stationary
is fixed they are just released the gas
but in the real life maybe there is a
mobile and uh things that people some
terrorists for example put something on
the on the truck or on something the
driving around or some other uh
things could happen and there are also
people talk about uh intermittent
release sometimes release and stop and
then release again so there are many uh
much more complicated scenarios here and
could be very interesting um coupled
with some other things things people
talk about for example you could have
more than one uh sources in this
release and it's just not one single uh
sources could be have more than one and
also people talk about if you have a
larger area and you have a number of
agents try to work together now we talk
about the collaboration between the
different agencies how to work together
more efficiently to to
search the area so there are many many
things here and the one particular thing
that i feel is directly can get from
your the help from your communities now
we only look at a
one step ahead but in real life we
already have some similar if we look
five step ahead it actually give us a
much better result because you look
further after the influence
of those changes so so there are but
however the the the the downside is uh
we'll already talk about it is a about a
computational load so now you have a
like a tree search because each step you
have a number of directions you want to
move your agents and you very many uh
multiple steps and the accumulation
could be quite nasty and we now have a
researcher trying to think about using a
multi-colored research or similar kind
of and the car is also provide for
instance provide some idea about it and
you work in the area uh how can embedded
into uh our work and try to take the
advantage of this so there are lots of
interesting things here
awesome i i'd like to um i think just to
create a few of these points of contact
pick up where you said that you're
planning one step ahead
um which is analogous to the variational
free energy it's like the instantaneous
best action
and then the expected free energy takes
into the future and i wanted to mention
a few different ways that
temporal planning is accomplished and
some were mentioned in the earlier
presentations
also it's interesting to note that
however many years ago i don't know the
exact number but somewhere in the 10
years ago range
active inference was kind of like an
instantaneous perception cognition
action theory and several elaborations
have specifically enabled it to account
for
increasingly distal planning so one
example is like in the continuous time
setting
having a taylor series approximation of
the generalized coordinates of higher
and higher
approximation depth is one approach
another approach that can happen in
discrete time is having just a broader
time horizon for policies
as well as with different uh tree
pruning approaches
another approach that can work with
discrete time or with hybrid models with
discrete and continuous time is
hierarchical modeling yeah and so it's
very interesting to wonder whether for
planning a hundred steps out
to go to think really deep into how
the uav will do something far away
how does it chunk that
and how does that chunking into is it a
hundred steps or one ten steps to ten
two steps of fifty and five of ten
inside the way that it starts to chunk
and understands
are the ways in which the computational
burden is reduced and also those ways
that start to resemble the ways in which
biological cognitive entities also make
sense of their environments
yeah i think that's absolutely right
that's a very good way to move forward
we're also doing
some thinking this way but not
necessarily coming from the same
direction because we think about it for
example when you make a decision on on
the uh
on the for example using the uh
autumn search problem you somehow like
you try to design your your way point
where you want to move to that and then
suddenly you have a question about how
far the step size this exactly can
change and even the larger area maybe
you want to move a little bit longer
distance so somehow this is a you can
regard this as a
hierarchical uh strategy and then we
actually uh give the commander to
low-level uav control or autopilot they
try to follow those kind of things so
there's a lot of things that we need to
think about that
somehow like is trade-off between the
performance computation load and the
horizon you won't be looking ahead in
theory if you're longer it gives you
better performance but however how far
you are able to looking at so there is a
trade-off between those terms maybe four
different applications could have
different
factors but the whole idea i think
that's quite interesting
is exactly worth to explore
cool um
we
have also kind of to to pick up on some
similarities and differences with the
presentations
some of them utilized neural networks
as modules in their training other used
variational bayesian methods
which can be fit as an optimization
problem and also we saw sampling based
approaches so i guess just pretty
broadly how do you see
these different ways of
doing
robotics and edge computing
how do you see them working
in different situations or together
with
sort of pre-trained or updatable models
that are large or variational or
sampling based approaches
yeah that's that's a very interesting
topic and i was quite abroad and there
are
lot of research nowadays about using uh
pre-training the model and particularly
in the context of
reinforcement learning for example if
you learn things and then try to deploy
them in the real life particularly for
the other robotics as well they have
lots of research in the area and uh for
me and as i didn't have any time to
explain uh articulate those ideas fully
but i think about it is lots of problems
and
whether it's engineering system robotics
or the biological or the the human is is
however the the the city could be
described like in how to uh
like make a optimal division at any time
the optimal division could in terms of
try to find a food or try to survive or
try to do something useful no matter so
that overall those all this problem in
my view can be summarized as a optimal
decision making problem
and
for this one even when you have all the
environment information unknown and also
all the behavior of your agents unknown
is not easy but when you try to deal
with something like what we talk about
is uh uncertainty in the environment on
the environment it will become much more
challenging so and uh
there may be there's no time being no uh
like a single solution for this this is
why you talk about many different
approaches they try to deal with and the
problem for me is um
the
the
the
uh there are two major uh approach i'm
thinking about it one is i call the uh
iteration process the iteration process
in particular like in the
reinforcement learning what it means you
have some initial strategy you try to
take the action from the environment and
reward the function or set the change
you learn from that gradually somehow
like you make your uh policy uh or
or very function close to true truly the
optimal one option policy so you're
always doing that in uh in the in the
iteration learning learning learning so
this is a approach and uh and but
because this approach you need a lot of
data this is why now people tend to
train in the data i train is australia
beforehand and let them deploy that
maybe online you can adapt to a little
bit to that but you if you can using
offline training using a lots of data to
take the advantage
but there another approach like maybe
more like in the uh
in active interference or more like in
the due control i call it as a purely
like a online optimization approach
the online optimization process just
like said okay giving all the scenarios
giving all the information i have with
the about the environment giving all my
what is my objective i try to work out
what is the best strategy i should have
given all the information i have and on
the body environment about my
reward function
i just try to work
out
what are the best strategies so then
this problem can formulate as an online
optimization program you try to say okay
give all the information connect so far
i give all the understanding
you charge it to that and uh
for this approach uh you need to have a
larger computational load normally as
you talk about aging computing and you
this is why we struggle we talk about a
one step ahead because once never had
these means is the optimization problem
easier to solve if you look at a
multiple state the optimization problem
could have getting much more complicated
and aging computing maybe you're not
good enough try to do it to do it but in
principle i can i regard itself as a as
a two broader
approach to suggest that and in the
inactive inference this is precisely you
tried using free energy or expected free
energy as a reward function you had
optimal
optimize your action so to give you the
best possible one so so this is why i
feel is this kind of a similar kind of
approach as we talk about it
so i i was also
while you
spoke to the dual control systems
thinking about
how it might have formal differences
from free energy principle and active
inference as we know it today
or again like we discussed earlier how
it might have reached some of the same
points from two different angles
and it made me think about the
particular partition
and the markov blanket or the first in
blanket so do you have any thoughts on
this or i can provide any more context
but first i just wanted to ask you
if
the concept of blankets
was relevant or there was some analog in
the control literature from your
perspective
yes we we
maybe we can say we always do that in
our control community
so we always do that in the sense
traditional m control look at is our own
dynamics itself and the sensor try to
pick up the information then the action
will take
so this is a controlled way the sensor
and your own thing and then take the x
but however previously control we very
much like
ignore the the interaction with the uh
too much of body environment we talk
about environment in the control
typically we call that disturbance
so the aim of our control system when we
are existing is try to act against any
uh disturbance because we try to uh to
do something ourselves
or keep it for example if you think
about want to keep your room at
temperature at a third degree if some
open door is a little if the external
temperature changes all those our
control is somehow like i don't care
about anything outside i care about it
sensors take information i do something
under them i take the action so this is
always regarded the water is
information from the sensor and we take
the action which will have some
influence outside then we take the
information from the sensor so whenever
i think that michael blanken i found
that there's a natural and maybe some
somebody close somebody with some
thinking we we have i feel this is quite
interesting the way to looking at the
world and because of you that you in
this way you don't care about it in
someone open the door don't open the
door you don't know because you just say
from the sensor what's the temperature
changing and we we take this
ignore anything outside that
i'm glad you added that because i also
had wondered whether the control
loop
was like a
pretty active partition i mean input
output systems systems with interfaces
holographic systems more and more
equivalences have been found but it's
kind of like the sparsest representation
of interaction between two agents or
with an agent in a niche is like well
you know you need the road going one way
and you need the road going the other
way otherwise it's not like you haven't
closed the loop so you have those four
pieces like the two entities and the
edges
and then it is interesting with the way
that what comes from the environment is
described is it a perturbation or
disturbance something that should be
controlled
or
as the case with allostasis and like
biological
processes that are anticipatory
and then going all the way into like
novelty which is like the ultimate
anticipation
it's just anticipation of the different
and then it's like again paralleling the
development of industrial control
systems going from stabilizing
vibration
yeah into needing to be proactive
there's also again a natural coming
together
as the attention in these fields turned
to
finding formal cognitive models
yeah yeah absolutely i think that
the the principle of the market uh
branch i think i quite found quite
interesting relevant um but they are the
the big difference from traditional and
uranic cultural thinking to what are
thinking in your area or a current our
thinking is about how to represent the
environment in your brain
so how you try to say this is that make
the all the whole things different
because
as i said previously maybe you don't
care too much everything like today the
disturbance or are just interesting
that your
heating system another and now is
actually no i want to have some way to
if you want to anticipate something
happen it may have a better
implementation about the environment and
also you want to align your belief of or
inside state more close to external
state so that is where i think all the
city things comes and also where you are
able to make some high-level division
make a
where the intelligence come from because
you have better implementation about
that you can figure out a better way how
to do it and then how to get the benefit
from the environment
so
one example that made me think of and
also connecting back to the embodied
intelligence and the morphological
computing i remember seeing a
a robot or a little vehicle
and it was able to move over a surface
that looked kind of like a stair on its
side like it was just very jagged um
but the wheel that this machine had was
shaped like a square that was the right
radius so basically it was able to roll
perfectly smoothly across that one
frequency of stair
but a different frequency of stair it
would have just been a total
total bumpy ride um yeah so
if the wheel would have been small
then there would have been a debate
around well should we represent chunks
of stairs and up and down hill and all
that fine scale but then
when the morphology
is fit to the niche
in a way that's natural
or in a way that is off sourcing some of
the computation
to the physicality
then that
entity only needs to consider like a
linear movement as if it was like in a
simpler space
yeah and so then it's almost interesting
to ask um like in some of the
presentations they they used
um very standardized robotics platforms
like the quadcopter and the turtlebot
and other standard
to the extent i understand standardized
robotic hardware which is awesome
because it increases accessibility and
it demonstrates it in a clear way like
tomorrow we'll hear from legos
implementations and so
on um
but then that
element of embodied computation
starts to
show how we could almost work in a
different way
and ask what kinds of
systems could implement
certain functions
maybe there are shapes of
robots or other objects that we we just
haven't seen the shape yet they don't
have to have two legs they don't need to
be
five feet tall
they don't need to look like a trash can
like that's some of the morphologies but
then with the air and the water and the
ground there's so many bodies
just of insects
so yeah it's it's going to be really
amazing to see how this is used
proactively to design morphologies and
behaviors that just do things we haven't
seen
yeah yeah yeah absolutely right i think
your abs are right yeah and
in this kind of uh i think maybe people
call uh
the the fitness thrive somehow like this
and that is actually somehow like we
always maybe you can using free energy
or some other notion to describe because
you you're living the environment you
want to get the best out of that and we
talk about now is a strategy how to do
it or how to
but however in the natural world because
you're physically uh
happier you your things are gradually
involved with you and if we are in our
design we can choose those physical body
as always as options as something we are
able to change and maybe gradually can
combine those two things together it's
not only your brain to make the best
strategy but also you are maybe called
the actuators or your physical bodies
other things you are gradually will
change with that so this is about how
you i feel how to set up the problem but
what i feel much more interesting is uh
in the active ingredients when you're
using free energy and then you can try
to capture much broader kind of behavior
and as i said in the control area we now
is
maybe more focus on the specific task
specific mission this is what we do
physically we want to do it but however
a lot of things like uh soft skills and
like more uh uh broadly about like our
confidence or a capability we don't talk
about it but human when we do the things
we learn learn build up the confidence
or embody our skills and then we do more
things now this is a and i think this is
a things happening there and active
embarrassing able to explain that they
able to have a true framework to do this
we are maybe at a more on the physical
alignment so i can see things that
gradually can move together and you may
can make robots for example more capable
to do something if they have the ability
to change their borders or change their
activation change other things or even
maybe they have come
improve their sensing because there's
something greater they learn and
they found more important than other
sensing particular environment they will
try to more develop
that kind of particular sensing
capability
so i can see that naturally and but the
question is about how to set up the
problem we allowed it to make this
happen
well
um
one fragment that kind of
that reminded me of from my own area of
insect behavioral modeling is there are
many models of task performance like
digging or foraging however there are
fewer models that are describing task
transitions
even though those are really important
for the colony and then the models of
task transitions tend to be more
generalized dynamical simulations and
less getting into the kind of
agent-based modeling perspective
and so it's like
as we're seeing robotics with the
physicality and the technology pushing
the frontier
that kind of task switching becomes
important higher and higher orders and
then again that
brings us into the bio-inspired design
conversation because task switching is
so essential
and the idea that like
the human is this unfolding of memory
and anticipation and all of these
different features
and
it's hard
functionally or neuroanatomically to
separate out
how
the human brain works and how animal
nervous systems work
and so i think that'll be another
interesting area with this tension
between explainability
and
potentially even austerity of the models
in that they'll have parameters
but the parameters
in the way they interact even for a few
parameter model
might be
difficult to understand because it's not
like going to be all the information is
in those generative model parameters
it's going to be those model parameters
and the dynamics of how gas is in the
world that are sort of relied upon
like
outside of the focus like the the
background context for the model
so the model itself won't be fully
understandable or explainable because
it's going to rely on this context just
like no sentence can stand alone so
there's just so many interesting
areas and and um
to see that the directions that
different fields can meet at and then
start to structure a productive
relationship
yeah
that's that's absolutely right and uh i
think i also
absolutely agree with you
it's about the
the importance of models they in many
ways they are very very important for us
we quite we i knew that in the machine
learning area they have a model-based
approach and a model-free approach i'm
more biased to model-based approach
because um you can using um
like a model-free approach they are
quite powerful in some ways but however
maybe they suffer some issues you
already uh highlight how to explain this
uh to
why you make this kind of deletion why
take this kind of action and more
explainable and and furthermore the best
one because a lot of things we are doing
and particularly in our area there are
engineering systems they are have a
first principle or other models already
they are for many years but however is
now is the question is about how to make
a use of that and so i prefer modal uh
based approach in
many ways along
for the explanation and try to you can
either understand the action but also
for the uh i call that um
somewhere like
maybe people yeah use the word sampling
efficiency somehow like you can use in
less data because you have a model based
approach and in the in our engineering
award that data means money
and then
i knew a lot of people say okay the
google facebook can harvest
billions of data online freelance but
however in the engineering if you want
to do something you need to experiment
to test you if you're into physical
wrong something to get a useful uh data
come out from that so that isn't the
money so when we're using the model
based approach is much more efficient in
terms of learning understanding what's
happening around the environment and so
this is why
economically
i feel is quite important for this not
just for the yeah so for for the safety
or how to make it more explainable but
there are some other reasons
well very interesting is there any other
remarks you'd like to add or questions
you'd like to raise
uh not really i think that's really a
very good accommodation i i'm very
pleased about this community as i said
and it's a surprise for me and people
share the same idea so what i'm
interesting is and they is getting more
involved in the primary community and
also i would like to open the door if
anyone working in this community they
want to talk with us want to work
together and develop some new ideas as
we already discussed and they're more
than welcome and you could have my
contact under them try to talk with me
and so basically i think we
share a lot of
fundamental ideas and we and also there
are some
different tools uh different slides
different concepts and approach if we
are able to work it together i will
think about we make them not only as the
tools try to interpret how the
natural water and the human or animal
the behavior like how but also make it
as a useful tool to drive us like this
theme to design more capable robotics
and do something for the society
amazing
great okay close to the first session so
you can depart
okay thank you
wow what a great discussion
big appreciation to professor chen for
joining for that
well
that concludes the first
interval of the second applied active
inference symposium on july 31st
or at least it is now where i am
and
in about eight hours we're going to have
the second interval
it will feature presentations by bruno
lara matt brown adam saffron and jf
claudia
it should be a great set of
presentations followed by a round table
discussion featuring several of those
presenters as well as carl firsten so
hope everybody has a good break
in the eight hours before the second
interval and
prepare some thoughts and questions and
writes them in the live chat or emails
us
really appreciate you spending the time
and attention
listening to this active inference
institute symposium and hope that you'll
stay involved participate and
keep on acting
and inferring so
goodbye everyone and see you in the
second interval
you
