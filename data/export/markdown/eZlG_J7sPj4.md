---
title: "ActInf Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”"
category: "Livestream"
series: "Livestream_026"
episode: "0"
duration: "1:21:51"
url: "https://www.youtube.com/watch?v=eZlG_J7sPj4"
views: 223
exported_at: "2026-02-18T22:37:37.875469+00:00"
format: markdown
---

# ActInf Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”

hello
and welcome everyone this is the active
inference lab it is active inference lab
live stream number
26.0 on august 6 2021
we're going to be discussing the paper
bayesian mechanics for stationary
processes
welcome to active inference lab everyone
we are a participatory
online lab that is communicating
learning and practicing
applied active inference you can find us
at the links
on this slide this is recorded in an
archived live stream so please provide
us with feedback so that we can improve
on our work
all backgrounds and perspectives are
welcome here as well
today as you can find out at this short
link
we're going to be having the context
video for the discussions on august 10th
and 17th in number 26.1 and 26.2
which are going to be group discussions
with some of the authors joining
so if you want to join for any of these
talks
or discussions then please just let us
know
and also we have a few weeks where we
don't have a paper decided so if you
have a suggestion
and want to be in those discussions let
us know
all right today in acting stream number
26.0 the goal is going to be to
learn and discuss this paper bayesian
mechanics for stationary processes
by decosta fristen heinz and pavliotis
which was posted in june 2021
this video just like all the dot zeros
is just an introduction to some of the
ideas in a walk through the paper one
way it's not a review or a final word
we're gonna give some overview to the
paper then
address a few of the key words from a
big picture perspective
then go through the figures in the
formalism
i'm daniel and i'm a postdoc researcher
in davis california
so in this paper the aims and the claims
are
laid out as followed they wrote in this
paper
we considered the consequences of a
boundary mediating interactions between
states internal and external to a system
so it's about interfaces and
interactions that's the first point
on unpacking this notion we found that
the states internal to a markov blanket
look as if they perform variational
bayesian inference
optimizing beliefs about their external
counterparts
so uh when the boundary is set up in a
certain way
for which kinds of systems that's what
we'll be
asking uh how do those systems look from
the outside or what does it look as if
they're doing
and then three when subdividing the
blanket into sensory and active states
we found that autonomous states perform
active inference in various forms of
stochastic control
i.e generalizations of pid control so a
lot of these terms like variational
bayesian
markov blanket pid control we're going
to be
talking about more but at the overview
level that's the aims and claims as the
authors write them
the abstract states that the paper
develops a bayesian mechanics for
adaptive systems and then there's only
these three claims again
which are again related to the blanket
and adaptiveness
of systems and then this partitioning of
that interface into sense and action so
first we model the interface between a
system and its environment with a markov
blanket
this affords conditions under which
states internals of the blanket encode
information about
external states second we introduce
dynamics
and represent adaptive systems as markov
blankets at steady state
this allows us to identify a wide class
of systems whose internal states appear
to infer external states
consistent with variational inference in
bayesian statistics and theoretical
neuroscience
finally whoops we partition the blanket
into sensory and active states
it follows that active states can be
seen as performing active inference
and well-known forms of stochastic
control such as pid control
which are prominent formulations of
adaptive behavior in theoretical biology
and engineering so this is going to be
relating to
math and physics with the markov
blankets and the far from equilibrium
thermodynamics
component and information theory and
then
it's also going to be developed into
some domain specific
cases or shown to be a generalization of
domain specific
cases like theoretical biology
and engineering these are the sections
of the paper so first there's an
introduction which has some of the
general concepts then there's a section
on markov blankets which is going to be
a key
framework and a key uh formalism to
track because it's kind of what the
paper is about
so first technical sections about the
markov blankets
followed by a discussion of how that
relates to bayesian
systems or certain types of bayesian
systems
and then this general bayesian framework
is then sort of uh
specified towards an active inference
model specifically with an eye towards
stochastic control
and then there's a discussion and
conclusion and then there's three
supplemental sections related to the
synchronization map
which is about the synchronization of
internal and external states
and how that's related to some math
results
there's the helmholtz decomposition
which
is related to vector fields and
splitting them into different components
and then there's the free energy
computation and
some more details related to what
exactly
that formalism is used as here
the keywords of the paper were
variational bayesian inference
non-equilibrium steady state markov
blanket
free energy principle predictive
processing and active inference
so first non-equilibrium non-equilibrium
steady state here's a figure
from this paper stable unstable and
meta-stable states of equilibrium
definitions and applications to human
movement so
there's going to be some mathematical
definitions and uses of non-equilibrium
steady state but this is a domain
specific usage that gets at some of the
nuances
there's not just one single way to frame
equilibrium
especially for dynamical systems and
this is shown as
with an example of a person in movement
so there might be a total thermodynamic
equilibrium
like death but even within the non-death
regime there are still many types of
equilibrium
there's lying down they're sitting in a
chair
there's a walking steady state there's
this meta-stable state
and then there's unstable states of
equilibrium so a few
just questions would be like what does
it mean to have equilibrium
of a measurement or a system at a given
level and what's the difference between
that
static just something on the ground
versus a dynamic equilibrium
like something that maintains its
position and uses energy to do that
so in those cases where does the energy
come from
how does this relate to dissipative
systems
so something where there's energy to be
expended like a battery
or a tornado and how does that relate to
adaptive
systems and predictive systems
which ones are related to active
inference one or both
and what about when there are
multi-level
systems of equilibria so some that are
higher frequency or shorter timescale or
smaller spatial scale
and others that are broader and also
what if we want to have
action-oriented models of those systems
so we want to have the description
that's optimal
for some other set of requirements other
than just accurate measurement
and that's where this paper is going to
be kind of headed
is thinking about dynamical systems in
general and looking
at equations that relate to solving them
another keyword was variational bayesian
inference
and there's a lot of good literature on
this
topic from a lot of different
perspectives but this article
had a good way of phrasing it which is
that
variational inference methods consist in
finding the best approximation of a
distribution among a parameterized
family and in contrary to sampling
approaches
a model is assumed which is the
parameterized family
implying a bias but also a lower
variance in general
variational inference methods are less
accurate than sampling based like mcmc
ones but produce results much faster
these methods are better adapted to big
scale very statistical problems
so again to just kind of give a
qualitative example it's like the real
world is giving you this data which is
the blurry image of a cat
one way to get at what was the
generative
uh underlying cat that generated this
blurry image
would be to sample and find the most
likely cat generating this image
or do various other sampling schemes and
if it's set up properly it can fit
arbitrary
distributions however it can be
computationally expensive and really
hard to know if you're
solving the problem at
a functional enough rate in contrast the
variational inference approach is
related to fitting the data
based upon a pre-specified family of
distributions
which can still be really general and it
can be fast but it can sometimes
lead to fitting the optimal support for
a given distribution
but having it just be categorically
wrong on some other dimension like
estimated through deep time or something
like that
so variational bayesian inference is
this lower
cat where there's a known cat and then
you stretch and distort the cat for
example
reparameterize the cat to find an
underlying likely cat
another was markov blanket
and there was good discussion of this
with mel
andrews in active stream 14
and we kind of had this continuum from
markov on the left here which was
studying systems from a mathematical
perspective didn't have
computer so it was looking at matrices
and which elements
of matrices were connected to each other
or not
and then that was developed later by
pearl
and others in this broader bayesian
statistical framework
that's where the markov blanket
terminology
starts to come from and
it's also oriented towards empirical
data and discovering dependencies in
data and it's very computational
and then part of the
literature that we're discussing is
where
fristen and others have built on or
used this pearl blanket slash markov
blanket
theme and done a few things like
separating the blanket states into
sensory in action
incoming and outgoing nodes
uh introducing the cybernetic
imperative to be a goal seeking or a
multi-scale good regulator
to maintain that non-equilibrium steady
state which we'll talk about
or and we did um and then also
what's being explored from a formalism
perspective in the paper we're
discussing
is how is it or under what conditions do
internal states act as if they're a
model of their non-local dependencies
so causal dependencies in the world
would be
reflected by how the brain or some other
computer system
works so that entails this generative
model of
the action in the niche and also
brings in the element of including the
uh blanket in internal external states
as part of this broader
inactive embodied and cultured slash
pragmatic term
also in active stream 14 we
had this sort of progression emerging
from the
structuring of the paper where there's a
uh
sort of vector field meets diffusion
thermodynamics uh branch on the bottom
with the
uh focker plank and helmholtz
and that's related to non-equilibrium
steady state
densities and then the free energy
principle
uh subsuming all these sort of pieces
like the markov blanket being maintained
through time
necessitates the degenerative model of
action
is what the internal states have to be
inferring so the useful components
of the external world
and then uh under free energy principle
there's all these sort of related areas
like
active inference is that an
implementation of systems under the free
energy principle
how is this related to predictive
processing
bayesian brain so we talked more about
that but today we're going to look at
how it's used more by the authors in
this paper
so the first thing is that the
code is available on connors
github and we'll also be
talking with connor hopefully so
let's um maybe work through it or if
anyone has
the chance to run it tell us about how
it went or what they learned from it but
i didn't
get to run it so
we can start with figure one which is
laying out the big
graphical intuition of the whole paper
and everything is going to be
specifying uh constraints
or some details or implications of
a way of interpreting this intervention
of the blanket states between
internal and external states so we have
mu the internal states b the blanket
states
and eta which are looks like a curly n
and um this is going to allow us to
separate any set of nodes
mu that we're specifying and
ask what are the blanket states that
insulate from a some
statistical codependency sense which
we'll be exploring
insulates these two partitions
and the caption says the mark called
blanket is depicted graphically as an
undirected graphical model also known as
a markov random field
the circles represent random variables
the lines represent conditional
dependencies between random variables
the markov blanket condition means that
there is no line between mu
internal states and eta the external
states
this means that mu and eta are
conditionally independent given b
so conditioned on the blanket these
internal
external states are separated in other
words knowing the internal state mu
does not afford additional information
about the external state eta when the
blanket state b
is known thus blanket states act as an
informational boundary between
internal and external states so that's
what the
blanket states do and this paper is
going to explore some of the
consequences of
that and again anyone who
has more expertise in this area or
some piece of knowledge that i totally
missed or got wrong my apologies but
um just want to try to represent it as i
saw it
because a lot of the details i was just
wanting to
learn more about and go over with the
authors
uh so if anyone has comments in the chat
they can also
just like mention it okay
so let's jump into how they present some
of the key pieces
of the formalism because that's the
details of free energy
principle slash some of the grounding of
active inference so
even if this is new uh formalism for you
then also hopefully it's also
interesting
so keeping that picture in mind of
figure one
another way of writing out that
graphical model
with a formalism is this eta and then
upside down t
so that's the external states
and then mu conditioned on b so that is
blanket states are markov blanket
separating internal external states so
the top third of the slide
these are like writing out in pros the
same thing as this graphical
model and then
we can take that tuple that
set of those three kinds of nodes
so we have measurements from all these
different things or generative models of
each of these different categories of
nodes
and then that set
so all the measurements slash generative
processes
that x is existing in a bigger
state space so the little x which
consists of like the real
measurements are part of the bigger
x which is kind of like the capital
versions of each of these
and those spaces the the uh e b
and i are taking to be euclidean spaces
for simplicity so i don't know
if it holds for other kinds of spaces so
that's just defining the total space the
possible
states of each of these nodes and then
also the ones that you actually observe
they start with
this case of a gaussian distribution p
encoding the distribution of states of
the world
so p is a random variable
that has drawn from n that's like a
normal distribution symbol
with a mean and a variance and the mean
is zero and the variance is this
um pi to the negative one
and um this has an associated precision
covariance matrix so mean zero that's
the convention n means the normal
distribution
and so it's zero mean that's the
variance pi
and the precision matrix is pi
so then the variance is this pi inverse
and sometimes the equations are
formulated in terms of precision
other times they're they're discussed in
terms of variance
but those are kind of like two sides of
the same coin because the same
it's just like describing it whether
it's how uncertain you are is like
looking from the mean out
and then your precision might be kind of
like is like focusing down
uh unpacking
in terms of gaussian densities so we
would find that a markov blanket is
equivalent to sparsity in the precision
matrix so the mark called blanket
condition is entailing
that the covariance the pi between
external states and internal states
that's the first
one here is equivalent to between
external states and internal states
the mu and the eta and that both of
those equal zero
so there's no covariance and they're the
same as zero
so they're conditionally independent
that's the
bayesian covariance matrix
framing of the marcal blanket sparsity
blanket states act as an information
boundary between external
and internal states and this allows
the breakdown of instead of the all by
all
consideration of correlations for data
fitting or generative modeling
you can reduce
the model space to a much better
uh formulated subset of equations
which are related to inferring
distributions
relating to like external states
conditioning on the blanket states and
internal states
conditioning on the blanket states this
enables us to associate to any blanket
state its corresponding expected
external and expected internal states
so then this equation
said uh drew us a set of equivalencies
which were that the internal states as a
function of blanket states so mu of b
were equal to the expectation
fancy e of mu conditioned on b
so that's the expectation of external
states conditioned
up on of internal states
um internal states conditioned on
blanket i
think that's corrected is right then
three
that that expectation is the same
as the distribution that's
being calculated involving uh the
objective distribution
p and that also that that's related to
uh the variance in covariance like this
sigma variable of internal
and blanket states mu and b
mapping to the space of all the possible
internal states
which was i from here
and then they wrote pursuing the example
of the nervous system each sensory
impression on the retina and ocular
motor orientation
blanket state is associated with an
expected
scene that caused sensory input which is
the expected external state
and does an expected pattern and an
expected pattern
of neural activity in the visual cortex
expected internal state
so it's a way that that objective
distribution
of uh p gets
integrated into the internal model's
output given blanket states
or maybe there's another interpretation
too so i was just i don't know
one way to look at it
this question about the relationship
between the internal and the external
states after you've not
denoised them but decorated them in a
specific way
is this topic of the synchronization map
so they go from just pointing out that
okay we've decorated internal and
external states with these blanket
states
now we're going to ask how these
internal states might encode
information about expected external
states
so after we've decorated systems how do
they have a memory or a model of one
another
for this we would need to characterize a
synchronization function
sigma mapping the expected internal
state to the expected
external state given the blanket state
so
sigma mapping function of internal
states of
blanket states is going to
relate to the
external states at a conditioned on
blanket states
so there's still the dependence of both
internal and
external states on the blanket states b
and now there's a sigma mapping that
is gonna connect internal and external
states
and lemma 2.1 goes
through some details of that
specification
so the first is proposing that there is
a function that maps
internal and external states
for any blanket state
i don't know how generally it holds but
or
this would be cool to talk to the
authors about but it's sort of proposing
this sigma function and
maybe in certain cases it's a zero line
maybe in other cases there's some
meaningful
relationship but for biological systems
it does seem like there's a meaningful
relationship
so those are the systems that we want to
explore modeling
they then write in how to construct this
synchronization map the key idea is to
map an expected internal state mu of b
to an expected external state
eta of b and to do this the
two points they provide are
one to find a blanket state that maps to
this
expected internal state i.e by
inverting mu and 2 from this blanket
state find the corresponding expected
external state
i.e by applying eta we now proceed to
solving this problem
given an internal state mu we study the
blanket states b
such that the
internal states of b
equals mu
they provide some details
maybe that is meant to be external
states i'm not sure
um here um
they're framing that inference
that mu is doing the internal states
in terms of covariance matrices
which is in
this equation 2.4
and then frames that
matrix of unknowns as a system of linear
equations
or those are kind of similar
representations and then
solves for it in the vector space using
this
equation 2.5 they use this
matrix negative
function which is the more penrose
pseudo inverse
it would be helpful to have someone
explain in a little more detail
what the matrix inverse is or what
degrees of freedom there are in choosing
different
kinds of matrix inverses but i just
found it interesting from wikipedia that
a common use of the pseudo inverse
is to compute a best fit or least square
solution to a system of linear equation
that locks a solution
another use is to find the minimum norm
solution to a system of linear equations
with multiple solutions
so this means that there might be
multiple
solutions that are equally well fit and
this just allows you to pick one
fast maybe
and then they write that the key for the
existence of a function sigma mapping
expected internal states to expected
external states given blanket states
is that for any two blanket states
associated with the same expected
internal state
these be associated with the same
expected external state
this non-degeneracy means that the
internal states eg patterns of activity
in the visual cortex
have enough capacity to represent all
possible expected external states
eg 3d scenes of the environment that's
formalized
in this lemma so first
was the point discussed before that
we're interested
in positing the existence of this sigma
function
and then 0.2 so these are all
points that are going to be equivalent
to each other
0.2 is that for any
two blanket states one and two that the
if the two external states
are equal i'm sorry if the two internal
states are equal the muse
of those two b's then it's going to map
onto
equal points in
external world so
the blanket is a is a
map that conserves certain properties of
the relationship between
internal and external states
then points three and four of the lemma
2.1
use this kernel
in image notation
so here was a image that was kind of
interesting
about how spaces were mapped to each
other
so someone could definitely
help explain what some of these mappings
mean or what the emblem
implications are and then this sideways
u shape is the proper subset
symbol so that's meaning that every
element
of the first one is in the second one
but b
is a bigger subset so
certain mappings between the internal
and blanket covariance and the external
and blanket covariance
and then uh similar for the
pi
figure 2 provides a visualization of
some simulations drawn
that uh support just from a simulation
perspective
the existence of a useful
synchronization
map function so
figure two on the left side shows
the external states given blanket states
so those are the orange
yeah external states up these are
the flipped
sorry about that so
the blue are the
internal states the sigma
mapping corresponding to the internal
states conditioned on the external
states
and they're doing a very accurate job
of mapping onto the external states in
orange
and then in b is a so-called non-example
and i'd be curious what
changed or what was different about this
second example or is there more than one
way to break the model
what are the cases where it does or
doesn't have a mapping
then in section 3 they
go from that sort of static estimate
of variables that are just
having a specific relationship to one
another
to beijing mechanics operating through
time
so they write in order to study the time
evolution of systems with a markov
blanket
we introduce dynamics into the external
blanket and internal states
henceforth we assume a synchronization
map under the conditions of the
lemma 2.1 so that was what was discussed
up here
and now in contrast with
figure 1 which was just the variables
by themself now we're
putting the t subscript and looking at
how those variables are changing through
time
we use bacillus to depict an intuitive
example of a markov blanket that
persists over time
here the blanket state between the
membrane and actin filaments of the
cytoskeleton
which mediate all interactions between
the internal states and the external
media external states
in example 3-1 they write there are many
examples of stochastic processes at a
gaussian steady state p
to name a few uh stationary diffusion
processes with initial conditions
x0 tilde p the time evolution is given
by an ito stochastic differential
equation
appendix b next slide that will be on
the next slide
and then also example three one more
generally
any markov process at steady state p
such as the zigzag
process any mean zero gaussian process
at steady state and any random dynamical
system at steady state p
so questions for people who know more or
the authors would be
what kinds of systems fall under this
category of stochastic processes
and what kind of real world systems
would be modeled well or not by this
formalism
and then going a little deeper into
that first point in the examples
appendix b points to this helmholtz
decomposition
and that is conditioned on this
ido stochastic differential equation
and again just questions for someone who
knows more or for the authors
what does this edo calculation entail
and what does or doesn't fit under this
edo
framework that would work using some
other definition
uh just
not sure about that but in this
helmholtz
supplement there is
a very nice figure 10 that is
looking at in this kind of hill climbing
perspective
so in an algorithm that's looking in its
local
neighborhood and doing a calculation to
sort of make local decision making and
hill climb that action
of a stochastic but hill-climbing
algorithm
up this gradient
or down depending on which way you set
it up
is going to have two components to its
motion
this straight up the mountain component
like putting a ruler on the mountain and
the maximum slope
and then another component that's at the
same likelihood like the same altitude
same energy that's going
at an iso contour just like you can
always do for a mountain
so with that idea in mind
it's possible to take the full dynamic
of a stochastic trace
on the top left this is like this
particle that is going
different colors through time that just
like converging to the top of this
mountain
diffusing like to the bottom of the bowl
like a marble going to the bottom of a
bowl
and then that trajectory can be
separated
into this spiral or i mean this um
oval the time irreversible component and
then a time reversible component
that has a much more direct trajectory
and that was in the section with remark
three one
which is again related to the ido
stochastic differential equation which i
just
i'm not too sure about um
but they write when the dynamics are
given by this edo stochastic
differential equation
a markov blanket of the steady state
density does not
necessarily imply that internal and
external states cannot
influence each other so that's i think
kind of the interesting
tension in question is how do certain
mathematical definitions of conditional
independence of blanket states
separating internal external states how
does that partition
sometimes result in subsets or systems
that don't influence each other
versus systems that do so in the case of
systems that don't influence
each other i was thinking of like an
empty bottle
of air in a room of air like they're
separated systems
but they interact through the bottle
so they could transfer heat for example
through a hot
bottle could transfer heat to the room
but the systems would only interact
conditioned on the temperature of the
interface
versus a person in a room
could be planning or thinking about the
external states
so just how do we think about what kinds
of systems are still having
influence or a long-term implication
for each other even after conditioned on
the interfacing a certain way
and then also just how does this example
provided kind of
show that that'd be good to walk through
and the absence of reciprocal influences
between two states
in the drift sometimes but not always
implies conditional independence
okay going back to the main uh
facts and figures in figure four there's
now looking at this synchronization map
and transition probabilities for
processes at the gaussian steady state
so on the left is we plot the
synchronization map as in figure 2.
only here the samples are drawn from
trajectories of a diffusion process
with a markov blanket so now it's
a temporal process
on the right panel there are the
transition probabilities of that same
diffusion process for the blanket state
at two different times
and this is called a joint distribution
because there's two
distributions that are being looked at
jointly and
if you kind of went to one side and
looked through the cornfield one way
you'd see this gaussian
p of b sub s and if you looked at it the
other way you'd see
p of b through t
and uh then they write which is kind of
interesting
um this shows that in general processes
at a gaussian steady state are not
gaussian processes
so that was just like very i'm curious
about what that meant
in fact the ornstein olbeck process is
the only stationary diffusion process
that is a gaussian process so the
transition probabilities of nonlinear
diffusion processes are never
multivariate gaussians
not sure what that means but sounded
kind of interesting all right so then
uh from this sort of mapping between
internal and external states through
time the synchronization mapping
sigma they write in the section on
predictive processing
we can go further and associate to each
internal state
mu a probability distribution over
external states
such that each internal state encodes
beliefs about
external states so
now rather than just framing these as
two dynamical processes that
track one another like oh there's this
synchronization map between this random
variable
internally and this random variable
externally
they're going to frame this q
distribution
so q is going to be
a probability distribution inside of mu
that's over external states such that
each of those states encode beliefs
about external states so q
of internal states is about eta
and that's going to be a normal
distribution
with a mean of the actual external state
it's like mean and variance
um so it's eta and then sigma of mu
the mapping function comma variant so
here these two
are both what it's being uh
is being inferred is the the external
state and the mapping
and then there's the variance of the
precision on external states
and then um 3.4
is just giving a little bit more details
about how that
q is like this internal function where
the states of it
are reflecting beliefs about external
states
um and then there's a relationship to
how the internal states are conditioned
on blanket states
this was a um interesting remark that'd
be cool to
have people discuss would be uh when
they wrote
note a potential connection with
epistemic accounts of quantum mechanics
namely a world governed by classical
mechanics sigma
conditioned at zero or i don't know if
there's another way to read that symbol
with three lines
in 3.2 um not sure because in 3.2
i'm not sure if there was a sigma in
which each agent encodes gaussian
beliefs about
external states the could appear to the
agents as reproducing many features of
quantum mechanics
so this was just cool like what is the
relationship between the sigma
internal external mapping function and
then classical
versus quantum mechanics so maybe
classical systems are like
the ones where there's a clean
separation between the internal and the
external states
quantum states being ones that are more
uh with residual influence between
internal and external states
so returning to the um
predictive processing they
write that under that 3 4 so under this
implication of the q internal
distribution
expected internal states are the unique
minimizer of a callback liblar
divergence so that mu through time
internal states through time are the
minimization the argument
over the mu states internal states
of the d kl the kl divergence
of
the internal belief distribution q about
external states
q of eta double line
divergence between the objective
distribution
of external states conditioned on
blanket states
so if that q distribution can converge
to the p
then that is being minimized effectively
this measures the discrepancy between
beliefs about the external world
q mu sub mu of eta and the posterior
distribution over
external variables computing the kl
divergence
they're going to obtain this 3.5
and um that's
argument so it's minimizing
the differential uh between sigma's
prediction
so that's sigma of mu minus
the actual external states through time
sigma
mapping function of internal states
minus the actual state
multiplied by so pi
of the precision matrix of eta
relating to how wrong
that differential is so that's kind of
an interesting
framing um and then they write that
the right hand side of 3.5 that equation
is commonly known as the squared
precision weighted prediction error
which is the discrepancy between the
prediction and the expected state of the
environment
and it's weighted with a precision
matrix that derives from the steady
state density
this equation is formally similar to
that found in predictive coding
formulations of biological function
which stipulate that organisms minimize
prediction errors
and in doing so optimize their beliefs
to match the distribution of external
states
so that's pretty cool and we can talk
more about it but
it kind of reminds me of this
uncertainty reduction imperative rather
than reward
maximization imperative it's kind of
like saying
if the organisms are minimizing their
prediction errors
not maximizing the reward they will
optimize their beliefs to match the
distribution of external states
so maybe that's related to that
variance reduction imperative
um so we had the uh
predictive processing section and then
there's one more layer that gets added
on
so from the markov blanket to making it
a bayesian
markov blanket happening through time
to introducing this q distribution
that's a special type of internal state
they write in the next section we can go
further and associate
expected internal states to the solution
to the classical variational inference
problem from statistical machine
learning
and theoretical neurobiology so
it's going to be that q function is
going to be a very specific kind of q
function
so not all systems are going to be
doing this subtype of variational
inference or
maybe they are um that is something we
could discuss
but we can finesse
that mapping function between
the internal and external states and
what exactly the internal states are
because if
you can co-design both the internal
states and the mapping
then you have a lot of degrees of
freedom
in mapping on to external states
even as they change so now we're going
to
do a really sub-special
phrasing maybe it's a more general one
but just one specific phrasing
of how the internal states could map
onto the external states
and that's going to be as expected
internal states
as the unique minimizers of a free
energy functional
i.e in evidence bound so now there's a
f function over blanket and internal
states through time
and that f
function is going to consist of two
elements which is like a divergence term
that we saw before with a divergence
between
q's internal estimate of external states
divergence and actual external states
conditional blanket states
minus the uh the evidence
term and then that can be
equivalent to this energy minus entropy
term
so that last line expresses the free
energy as a difference between energy
and entropy pretty cool energy or
accuracy measures to what extent
predicted external states are close to
the true
external states while entropy penalizes
beliefs that are overly precise
so that's cool like energy is locking in
on the good solution that's like
maybe the component that is going up the
hill
and then entropy is keeping things
away from just going up the hill and
keeping this other component in
but if um
entropy overwhelms the entropy uh the
energy then the solution
will not kind of fit the situation
so at first sight
variational inference and predictive
processing are solely useful to
characterize the average internal state
given blanket states at steady state
it is then surprising to see that the
free energy says a great deal about a
system's expected
trajectories as it relaxes the steady
state
pretty interesting so here's how they
kind of show that
figure five is using that free energy
minimizing
framework to look at variational
inference and predictive processing
so the highlighted part says the figure
illustrates the system's behavior
after experiencing a surprising blanket
state
so kind of like a perturbation this is a
multi-dimensional ornstein olbeck ou
process with two external blanket and
internal variables
initialized at the steady state density
conditioned on an improbable blanket
state
which was given at the initial time
actual distribution of x and b
at time 0. and
on the left top left quadrant
is sort of this red to blue gradient
of free energy so it's kind of high
elevation to low elevation
and through time the blanket stage just
converged down to the bottom of the bowl
so that's the free energy minimization
in action the upper right is the is the
free energy
over time averaged over multiple
trajectories so it starts out
really high and then it kind of rolls
down and it converges to
this low level at 40 time points
the lower left is showing
this uh predictive processing
framing of the q distribution
versus the actual distribution and said
at steady state from time step about 100
the predictions become accurate
so that's showing how for the estimate
of the parameter converges to the
accurate
external states under their simulation
be cool to do a walkthrough
and then on the bottom right is looking
at the error prediction errors
the covariance of so the two co errors
um the evolution of precision weighted
prediction errors
over time these are normally distributed
with zero mean at steady state
uh figure six
is uh
maybe i didn't change not sure exactly
it's a similar
figure it has a little bit of
differences
uh again showing the predictive
processing
lock in on a free energy minimizing
process
showing the average free energy
initially having a
slight increase maybe and then just
decreasing through time
and then also just showing that the um
the relationship
of the covariance um
[Music]
was raised up from zero and then started
converging back to zero
so just cool figures but cool to see
what other people would think about them
in figure four or i'm sorry section four
we get to
active inference and stochastic control
so they write in order to model agents
that interact with their environment we
now partition blanket states into
sensory and active states
so for active everything that we've
talked about before is like an
undirected
bayesian graph um
it's not using that frist and blanket
separation so that's where we're gonna
be bringing in a lot of other
uh cool formalisms and
ideas so let's go from that sort of
blanket one type of fiber in the blanket
to
two now uh in order to model agents to
interact with their environment we now
partition blanket states into sensory
and active states
so the blanket state b of t blanket
through c
is now two subsets of sensory
and action states through time so now
that whole
tuple the whole set that you need to
infer the four kinds of states are
external sense action and internal
eta s-a-u yeah
and now that previous example of the
bacillus so here we had
just one we had external and internal
states mediated by one kind of node
and now the external states are coupled
to the sensory states
that's s of t and sensory states are
coupled to internal states
internal states are coupled to action
states and actions connect back to
external states also sense and action
are connected to each other
but i wonder if that part is needed or
i'm always wondering what topologies
of connectedness different
functionalities arise from
and uh miguel aguilera's
paper and recent uh guest stream
speak to that so
we take that dynamic markov blanket
model from the previous sections and now
split the blanket states into sense in
action
that was this piece here
now then they write intuitively in
agents actions and internal states
depend
upon its sensations therefore we are
interested
in characterizing autonomous i.e active
and internal
so we can't control our senses directly
but we can control internal states and
active states
so those two states we're going to think
about that pair of notes
given sensory states so
that is the following free energy
equation
that was brought up earlier so taking
that free energy
minimizing perspective on the
distribution of mu
internal states and blanket states as a
whole b
before we introduce the split here then
do a similar free energy equation
with three variables on
the sensory action and internal states
which is just another way of saying the
blanket states
and the internal states mu
and then etc etc more details that
people can
explain if they know better but the
result
that um comes out
relates to action so it'd be cool to
learn more about what this equation
means
but then they write this is known as
active inference because expected
autonomous states minimize free energy
crucially active inference is a
well-known framework to describe and
generate adaptive behavior in
neuroscience machine learning and
robotics
see figure eight so
figure eight is a similar
diagram to we had before
but now it's an active inference
agent rather than just the free energy
minimizer
of the previous framing and then they
write
the figure illustrates a system's
behavior after experiencing a surprising
sensory state
averaging internal variables for any
blanket state this is an ornstein olbeck
process
with two external one sensory one active
and two internal variables
initialized at steady state density
conditioned upon an improbable sensory
state
and also one pattern that they found was
that
the free energy minimization here it's
relatively monotonic
it kind of doesn't ever bump back
up it just goes down or stays the same
but then it was kind of interesting they
said
we plot the free energy of the expected
internal state averaged over multiple
trajectories
so this is not just one aberrant run
in this example or maybe this is just
one example
but they wrote the average free energy
does not decrease monotonically
see figure five for an explanation and
then um
maybe we can learn more about that but
that was kind of cool
okay they
continue on and write that any mean
stationary mean zero stationary gaussian
process with exponentially decaying auto
covariance function
so it resembles itself less and less
through time
is an ornstein obec process which is
kind of cool because in phylogenetics we
sometimes would use this
for let's just say the average femur
length of
some mammal and then you would be
inferring a model
that had an average value so it's kind
of like a
peg and then like a tether so it's like
a diffusion term
and then a mean so just a mean
and a variance that drift through time
is like the orangeteen olbeck or the oh
you
process sometimes known as dub's theorem
so those kinds of processes which
are apparently general enough to be
really good
model systems for studying math i guess
thus if
c equals a finite sum of exponentially
decaying functions
we can express s of t the state's
sensory states
as a linear function of several nested
ou processes
i.e an integrator chain from control
theory
so the integrator chain was kind of a
cool idea and
we'll talk about maybe applications of
integrator chain in a few slides
but just to continue with the math that
they
have so there's this um
s of t states through time sensory
states is going to be this f
function and then there's these um
d these these kind of similar
d equations so it says in this example
f and f sub i are suitably chosen linear
functions
not sure what the pronunciation is but
the squiggle are matrices
and w are standard brownian motion
thus we can see sensory states through
time s t as the output of a continuous
time hidden markov model
whose hidden states s of t superscript i
encode various orders of motion position
velocity
jerk etc these are known as generalized
coordinates of motion in the bayesian
filtering literature which we'll look at
graphically in figure 9
and more generally the state process s
of t and a function
f need not be linear which enables to
realize
non-linear non-gaussian processes sst
technically this follows as ornstein
obec processes are the only stationary
gaussian markov processes yet we
emphasize that stochastic
realization is not as well developed in
the general case
so this is um in a way saying
that we're going to have like the
position of the ball
is the sensory data that's like the
first pass
um of where the ball is that's the
measurement that's the sensory data
then there's the variance and then
there's the second
derivative of that statistical moment
and so if the variance is equal through
time then you can just integrate away
and the higher levels are zero and
you've kind of locked on to the pattern
after just one or two levels
but there's other distributions where as
you go to higher and higher
distribution uh higher moments
there's just more or different
information
so there's this concept of the
integrator chain
where these relationships of equations
are all
integrals or derivatives of each other
which are kind of like going up or down
in this rows of equations and then this
helps
use gaussian type mathematics like the
ou
stochastic process where a lot of the
math is clean
it allows you to apply these
systems of equations of well-behaved
types oh you to model highly non-linear
systems so
this was related to some interesting
discussions
um uh i i will look forward to hearing
what you
have to say about these so-called
generalized coordinates of motion
and that relationship between control
theory
and then looking at nonlinear functions
as relationships of integrals and
derivatives
leads to this discussion of the pid
control
so proportional integral derivative
control pid
is a well-known control method in
engineering more than 90
of controllers in engineered systems
implement either pid or pi
no derivative like just proportional
integral control
the goal of pid control is to control a
signal
s sub t its integral s sub t
with a 0 instead of a 1 and its
derivative
s sub 2 of the 2 close to a
pre-specified target
value so it's like i want 95
battery and i want to be a rectangle at
95 percent and it's derivative to be
such and such during use this turns out
to be exactly what happens
when we take stochastic control of an
integrator chain
with two with three orders of motion so
that's just
a three level model in this sort of
infinite rows of the moments of the
distribution
the three levels are just what are
described here the signal the integral
and the derivative
when f is linear expected autonomous
states control to what extent
integral proportional and derivative
processes s t at zero one and two
levels of derivative are from their
target value of 0.
so it's like if it's a linear response
function then the first derivative
is going to be a constant value as in
the second derivative you get rid of it
furthermore from f and k alone one can
derive integral proportional
derivative gains which penalize
deviations of these three moments
respectively from a target value of zero
so these are highly optimizable problems
and
computable crucially these control gains
are simple byproducts of the steady
state density and the stochastic
realization problems
this is a cool question why restrict
ourselves to pid control when stochastic
control of integrator chains is
available it turns out that when sensory
states s of t
are expressed as a function of an
integrator chain one to get away with
controlling an approximation of the true
sensory process obtained by truncating
high orders of motion as these have less
effect
on the dynamics though knowing when this
is warranted is a problem in
approximation theory so how
let's just say we open the door to doing
infinite derivatives of statistical
distributions
infinite variances upon variances how
would we know when to stop
that's the problem in approximation
theory or approximation science
this may explain why integral feedback
control
which is just like battery good
pi control n equals one and then the pid
control with
two extra layers of the derivatives are
the most ubiquitous control methods in
engineering
applications however when simulating
biological
biological control usually with highly
non-linear systems
it is not uncommon to consider
generalized motion to fourth
or sixth order so that's pretty cool um
like how many levels of recursion and um
depth in modeling
are needed to have a people
so calling back to
here when we defined that initial sense
function
as part of this integrator chain setting
off the integrator chain
here's that initial sense function
as part of a broader set of dependencies
so here is that sense function
at time 3 6 and 9.
the figure is depicting in a graphical
format
the bayesian network of those
equations flipped
the encircled variables are random
variables and the processes are indexed
an arbitrary
sub an arbitrary arbitrary sequence of
subsequent times
the arrows represent relationships of
causality so
the sensory states are not causing each
other through
time they're getting measured through
time but
they are being emitted through time
by this s at the zeroth level like the
just the base generative model
of this s of zero
level function so this is the generative
process
then that can have higher derivatives
of change and each of those are
being framed as well behaved
statistically
so in the hidden markov model and these
um white nodes are
hidden states but they're inferred by
statistics
the hidden integrator state hidden state
processes sat
is given by an integrator chain i.e
nested stochastic differential equations
these processes can be seen as encoding
the position
velocity jerich etc so higher
derivatives of the distribution
so this integrator chain is kind of a
cool
idea so here was one paper stabilization
of integrator chains
in the presence of magnitude and rate
saturations a gain scheduling approach
so this paper wrote and the conclusions
in this paper we have given a time
varying controller
so kind of like a heuristic or an
algorithm for control
for stabilizing a chain of integrators
in the presence of magnitude and rate
saturations
it is proved that the controller gives a
convergent closed-loop system
i.e for any bounded state initial or
initial condition the state will
converge to the origin
the main strength of the controller is
that it gives provable convergence
without being overly conservative
this is verified in a simulation study
so
it's kind of like we have the frame of
the airplane
at steady state and then
which is flying through the air so how
are we going to re-equilibrate all the
sensors
so that if we get knocked off to the
side
what's the path by which we're going to
get those sensors back to their desired
level
and it's just a question i oh and this
is kind of what it looked like one of
the figures from the paper
so these are these derivative functions
they get get like bumped and then they
can come back to
the level that they're desired
almost in this signal processing like
way
so what are integrator chains how are
they used maybe someone has
used them before that'd be cool and then
one kind of random thought was there's a
lot of cases
where we frame a process as mean
zero because it
allows thinking about something in
relationship
to uh a defined axis whether it's the
number line or whether it's some other
variable
it kind of splits half the things
negative and positive or there's various
other times
but there's actually a bunch of places
and maybe more or maybe these are not
all the same so
it's okay if somebody knows more and
helps us all out
but there's actually a few cases where
a distribution that's hard to estimate
is replaced with a zero mean like
sometimes there's replacing elements of
a list
with a z score like their standard
deviation
from the mean or the mode um
but then it's like half or above and
half are below
so that's like replacing something with
a zero center
z score or t distribution sometimes
there are error distributions which are
extracted from a signal it's like the
signal
is the underlying line and the goal of
the signal
extraction is to leave your error
distribution
mean zero and then equally
distributed in both directions so
sometimes we're
pulling out an error distribution
we're trying to find uh
that mean zero get to a level of
derivative of a signal
where the mean is zero like where the
rate of change of some
high derivative is zero which implies
that it's not changing at that level
and then sometimes we're trying to get
um like in predictive processing
study the differentiable or predictive
processing with
trying to get a zero centered variance
on the sensory input but more
about how we can study the differential
between some controllable distribution
and then some other distribution that we
can't control
and then how to make how does zero
center that
to determine which solutions are better
or worse than each other and there's a
lot of different methods there
and then there was this other paper time
optimal regulation of a chain of
integrators with saturated input and
internal planet variables in application
to trajectory planning
so again just kind of a open question
what is the relationship between
integrator chains and then this idea
that we talk about a lot with
action planning as inference
then the conclusion this paper outlines
some of the key relationships between
stationary processes
inference and control these
relationships rest upon partitioning the
world into those
things that are internal or external to
a statistical boundary
known as a markov blanket when equipped
with dynamics the expected internal
states appear to engage
in variational inference while the
expected active states
appear to be performing active inference
in various forms of
stochastic control the rationale behind
these findings is rather simple
if a markow blanket derives from a
steady state density the states the
system will look as if they are
responding adaptively to external
perturbations
in order to recover the steady state
conversely
well-known methods used to build
adaptive systems implement the same kind
of dynamics implicitly
so the system maintains a steady state
with its environment
so maybe there's i mean this isn't a
totally accurate
uh classification but there's some
algorithms
that are being connected on one side to
each other
so we have learning and optimization
learning as inference
all of machine learning etc learning and
optim
optimization and then variational
inference being used as an optimization
technique with the gradient descent by
free energy
in machine learning and maybe in
evolutionary systems then there's this
question about
estimating latent causes in the world
and connecting that to
higher derivatives in the integrator
chains
or as just variables under consideration
that's that mapping
of external states which aren't directly
seen
and then maybe
this one goes on this side but
uh there's this whole other set of
algorithms related to
adaptive systems and these are framed
variously but we have adaptive systems
cybernetic systems
anticipatory systems holism homeostatic
slash
active learning allostatic agents
all these sort of biologically inspired
yes drawing on far from equilibrium
thermodynamics
but here was like the flame dissipating
like it's about something that just sort
of gets to its free energy minimization
just like gets there
but with these active systems
the question becomes how do we take this
ongoing
multi-scale inference
side and connect it to this multi-scale
action in the loop niche modifying
also action planning biology section
um one friend uh looked at these slides
and then made a comment
and they wrote i think it would be good
to expand on the differences
of the paradigms in section three which
were lettered
as they were in the paper a priori
a posteriori estimate estimation
afterwards estimation
predictive processing and variational
base
i get the differences formally but still
not at a super intuitive level so this
might be good as a pedagogical
exercise for ourselves so that'd be cool
maybe everyone can think about that
and come to their own explanation for
what the difference is between these
three and we'll talk about it in the dot
one and dot two
then just a few of the implications and
bigger questions that are raised by the
paper
so in the section on interacting markov
blankets they write
the sort of inference we have described
could be nuanced by partitioning the
external state space into several
systems that are themselves markov
blankets
such as markov blankets nested at
several different scales
from the perspective of internal states
this leads to
a more interesting inference problem
with a more complex generative model
it may be that the distinction between
the sources systems we generally think
of as engaging in cognitive
inferential dynamics and simpler systems
rest upon the level of structure
in their generative models i.e the
steady state densities
that describe their inferential dynamics
so that's pretty cool about maybe this
framework or at least work in this level
of analysis
mapping just directly to nested markov
blankets
and it brings up this whole discussion
about what kinds of systems can we model
with active inference so no one's saying
that
the stock market is an auto-regressive
model
but people use auto-regressive models so
what kinds of
systems will we usefully be able to
model with active inference
without really just getting into a
debate about whether it quote
is active inference in the system just
how are we going to use variational
based methods
with modern twists and developments
related to
cybernetics and multi-scale systems so
that's like the instrumentalism side
and then the realism side
is what kind of systems are doing active
inference
so there's maybe even a realism of
philosophy branch and then even maybe on
the applied side
like it's a philosophical debate is the
cell doing
active inference doing free energy
principle is it realizing
certain constraints of nature or how
would we know what
um uh you know an ant is quote doing
free energy minimization in its brain
and then on the engineering side
it could be argued that if a robot is
implementing active inference code that
it is actually doing
active inference so this question about
designing systems within the active
inference framework
so instead of saying i think all
internet networks
are active in front systems it's
definitely a claim somebody could make
interesting claim but it's quite another
thing to design
a computer network that is within an
ontology of
active inference then it would be fair
to say that that network is quote doing
active inference
so that's like realism and maybe for
some it's more of an engineering realism
others it's a philosophical realism
another implication and bigger question
that arises in the paper
is about temporally deep inference so
they write
this distinction may speak to a
straightforward extension of the
treatment on offer
from simply inferring an external state
to inferring the trajectories of
external states so again moving from
not just the point estimate current
estimate of external state
that was what was presented earlier to
inferring the trajectories of external
states
which is to say decomposing their
higher orders of movement this may be
achieved by representing the external
process
in terms of its higher orders of motion
by solving the stochastic realization
problem by repeating the analysis above
internal states may be seen as inferring
the position
velocity juror etc of the external
process
consistently with temporally deep
inference
in the sense of a bayesian filter a
special case of which is the extended
kalman boosie filter
so these are cool things to talk about
we could talk about
what is temporally deep active inference
what are the ways that the model deals
with internal and external categories
and discrete variables
how do we deal with the inference on
external states and how does that relate
to our action selection
and then what happens when there's a
feedback or um some other type of
interaction with the niche
the informational niche the social needs
the stigma niche
so or other questions people can write
um well that was
a sort of quick run through
paper and i'm not
sure if i got each section 100 correct
so it will be good to have
the author's perspective on a lot of
pieces as well as a lot of other
experts who i'm sure could have said a
ton
more and better about some of the math
but
we can offer up the same questions that
we have for any paper
like what might a good understanding
enable
what are the unique predictions and
implications and the unique developments
of this
paper what are some of the next steps
for
free energy principle and active
inference research
what are the goals of this research and
then
also to the participants and the authors
what are they still
curious about learning so
thanks for participating it was a fun
26 and uh we hope that you'll
join for 26.1 and 0.2
if you can or comment on the videos or
whatever
and thanks talk to you later bye
