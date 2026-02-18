---
title: "ActInf Livestream #052.0 ~ Geometric Methods for Sampling, Optimisation, Inference and Adaptive..."
category: "Livestream"
series: "Livestream_052"
episode: "0"
speakers:
  - "Geometric Methods for Sampling"
  - "Optimisation"
  - "Inference"
  - "Adaptive..."
duration: "1:56:03"
url: "https://www.youtube.com/watch?v=LPj_ok8Pxxw"
views: 208
exported_at: "2026-02-18T22:37:37.769377+00:00"
format: markdown
---

# ActInf Livestream #052.0 ~ Geometric Methods for Sampling, Optimisation, Inference and Adaptive...

Hello and welcome. This is ActInf livestream number 52.0 and it is February 28th, 2023.
Welcome to the Active Inference Institute. We're a participatory online institute that is communicating, learning, and practicing applied active inference.
You can find us at the links here on this slide. This is a recorded and an archived livestream, so please provide feedback so we can improve our work.
All backgrounds and perspectives are welcome and we'll be following video etiquette for livestreams.
Head over to activeinference.org if you want to learn more and participate in learning groups and projects at the institute, including these livestreams.
Well, we're here today to learn and discuss the paper, Geometric Methods for Sampling Optimization Inference and Adaptive Agents by Alessandra Barp, Lancelot DaCosta, Guilherme Franca, Carl Friston, Mark Ghirilami, Michael Jordan, and Gregorios Pavliotis.
This video, like all .0 videos are, is an introduction for some of the ideas. It is not a review or a final word.
And as we've joked before, it's more than anything, a call for help.
So if you're curious about these topics, if you're knowledgeable about these topics, we would really look forward to you getting involved in the upcoming 52.1 and 52.2 discussions, as well as in an ongoing basis to help us understand some of the technical details.
This is going to get technical at times, and certainly beyond the technicalities I understand, though I am looking forward to presenting them.
And it will be great to have those who have backgrounds of all different types to come together and talk about this awesome work.
Also, big thanks to Ali and Kandon for the assistance, technical and moral, during the preparations here.
In 52.0, we're going to bring up some aims and claims, read the abstract, look at the roadmap, and talk about the keywords.
And then we will walk through the paper with an emphasis on the figures, formalisms, and key points.
In the coming weeks, we're going to be discussing this paper with one or more authors.
So, as usual, get in touch if you want to participate, or if it's after the fact, you can still get involved.
We can start with an introduction or a warm-up.
I'm Daniel. I'm a researcher in California.
And I'm tempted to say, just totally honestly, I'm happy to get this one over with, but that sounds a little bit different than I might intend it to be.
I'm really excited to dive into this work, which is going to be approaching active inference from an angle that we haven't necessarily highlighted on these streams.
So, I think it's going to be a fascinating discussion. It's going to run the gamut, span the gap, however you choose to see it, between technical sophistication and intuition, which is a great place to be.
So, I've been really excited and motivated to prepare, and I'm looking forward to the .0 we're doing right now, and to the upcoming discussions.
So, let's jump in with the big questions that might motivate one to read this paper, this kind of paper, even if they were not familiar with the authors or topics.
And these are just a few ways to write it up, of course not the only ways.
So, first question. How can we effectively and efficiently navigate information geometric or information theoretic landscapes?
And how can we tackle that question from an analytical, which is to say, equation based, as well as a computational, which is to say, real implementation based perspective?
Often, it's really fun, intuitive, natural to talk about information theory, even for those who haven't taken the technical prerequisites.
And this work may help us navigate to a space where we're able to think with good intuitions about information geometry, information theory, and also make sure that those intuitions are going to be caught by our technical tools.
Second, how can we optimize inference in complex models, including cases where we are doing inference on action as a parameter, also known as active inference?
Optimization and functional analysis, as we'll come to see soon, has long been interested in these complex or challenging models that are right at the margin, right at the border of what is tractable or not, given the computational hardware that modelers have access to.
For example, big data sets, high dimensional states, complex dynamics, complex dynamics, and so on.
How about cases where we're also interested in doing parametric inference and optimization on action or action plans as a parameter, also known as active inference?
And third, what technical underpinnings support the rigor and applicability of active inference?
And what special cases are revealed when we consider possibilities and constraints?
These are those two branches of analytical and computational coming back again.
We want to make sure that when we're thinking within the active inference paradigm, the active inference ontology is the language that we're speaking, and that there's a technical rigor to what's being discussed.
Additionally, we want to make sure that it's not just an analytical rigor, but it's also going to be computationally plausible, tractable, or maybe even preferable.
That would be awesome.
Those are the questions that at least appeared.
We are discussing this paper, Geometric Methods for Sampling, Optimization, Inference, and Adaptive Agents by Barp and DaCosta et al. Shared First Authorship, and it was published on Archive.
I'll just note a few key claims from this paper.
They wrote,
Our goal in this chapter is to discuss the emergence of natural geometries within a few important areas of statistics and applied mathematics, namely optimization, sampling, inference, and adaptive agents.
That's the title.
We provide a conceptual introduction to the underlying ideas rather than a technical discussion, highlighting connections with various fields of mathematics and physics.
Though whether it is a conceptual introduction or a technical discussion is all going to be about your perspective.
Third, to illustrate a generic use case for the previous methodologies that are going to be discussed, we consider active inference, a unifying formulation of behavior, subsuming perception, planning, and learning as a process of inference.
So, inference on adaptive agents is not necessarily new.
It goes by reinforcement learning, machine learning, and so on.
However, to use those methodologies in the context of active inference, a unifying formulation of behavior, is something that the authors are bringing forth here.
And last, we describe decision making under active inference using information geometry, revealing several special cases that are established notions in statistics, cognitive science, and engineering.
So, active inference is not just unifying.
It's going to be shown to be generalized as well, which is to say that special cases of the generalization emerge different formalisms that were known disparately across fields.
On to the abstract.
They write,
They write,
In this chapter, we identify fundamental geometric structures that underlie the problems of sampling optimization, inference, and adaptive decision making.
Based on this identification, we derive algorithms that exploit these geometric structures to solve these problems efficiently.
We show that a wide range of geometric theories emerge naturally in these fields, ranging from measure-preserving processes, information divergences, Poisson geometry, and geometric integration.
Specifically, we explain how.
One.
One.
Leveraging the symplectic geometry of Hamiltonian systems enable us to construct accelerated sampling and optimization methods.
Two.
The theory of Hilbertian subspaces and Stein operators provides a general methodology to obtain robust estimators.
And three.
Preserving the information geometry of decision making yields adaptive agents that perform active inference.
Throughout.
We emphasize the rich connections between these fields.
E.g.
Inference draws on sampling and optimization.
And adaptive decision making assesses decisions by inferring their counterfactual consequences.
Our exposition provides a conceptual overview of underlying ideas rather than a technical discussion, which can be found in the references herein.
And indeed, there are several hundred references in this paper.
Let's go to the roadmap.
So, first, we can start on the right side.
Here's an active agent.
Vroom, vroom.
Vroom.
Vroom.
Doing accelerated optimization in the carpool lane.
Looking ahead to the almost dessert-like visual representation of active inference.
That's where we're going to go.
And on the right side, it's just some cars.
One of them is accelerated.
The other one isn't.
The paper begins with an introduction.
And then in section two gets into the topic of accelerated optimization.
Covering the areas of principle of geometric integration.
Conservative flows and symplectic integrators.
Rate matching integrators for smooth optimization.
Manifold and constrained optimization.
Gradient flow as a high friction limit.
And optimization on the space of probability measures.
In section three, they turn from accelerated optimization in general to Hamiltonian-based accelerated sampling.
The subsections of three are optimizing diffusion processes for sampling and Hamiltonian Monte Carlo.
From the Hamiltonian-based accelerated sampling, they turn towards doing statistical inference with kernel-based discrepancies in section four.
The subsections are topological methods for MMDs, smooth measures and KSDs, the canonical Stein operator and Poincaré duality, kernel-Stein discrepancies and score matching, information geometry of MMDs and natural gradient descent, minimum Stein discrepancy estimators, likelihood inference with generative models.
Finally, in section five, adaptive agents through active inference.
They're going to bring it home to active inference.
Section 5.1, modeling adaptive decision-making, behavior agents and environments, decision-making in precise agents, the information geometry of decision-making.
And 5.2, realizing adaptive agents, the basic active inference algorithm, sequential decision-making under uncertainty, world model learning as inference and scaling active inference.
So, a quick note.
We have all the formalisms entered into our .0 teams coda document.
There are 46 numbered equations in this paper and 83 overall.
We're going to bring in some, but not all of these formalisms in the .0 video.
And we're ready to bring in more during the .1 and .2 discussions with the authors.
Just for those who are watching along, I'm going to scan through all of the formalisms from our coda.
And again, for those who want to help get involved with a .0 preparation, this is a little bit of what .0 preparation looks like.
I'm going to now scroll through the formalisms just in case anybody wants to screenshot or see them.
.
.
.


.
Great.
On to the keywords.
Keywords of the paper are information geometry, Hamiltonian Monte Carlo, Stein's method, reproducing kernel, variational inference, accelerated optimization, dissipative systems, decision theory, and active inference.
In no particular pedagogical order.
Let's start with decision theory.
From the Stanford Encyclopedia of Philosophy, the article begins,
.

.


.


e.g., the differential geometric treatment of smooth statistical manifolds,
whose origin stems from a seminal article by Rao, 23,
who introduced the Fischer metric tensor on parameterized statistical models,
and thus a natural Riemannian geometry that was later observed to correspond to an infinitesimal distance
with respect to the Kolbach-Leibler or Kael divergence.
So, going into Citation 23 and 24,
Citation 23 is Rao from 1992, and Rao wrote,
The objective of the paper is to derive certain inequality relations connecting the elements of the information matrix as defined by Fischer, 1921,
and the variances and covariances of the estimating functions.
A class of distribution functions which admit estimation of parameters with the minimum possible variance has been discussed.
The concept of distance between populations of a given type has been developed starting from a quadratic differential metric defining the element of length.
So, I'm only going to give the disclaimer one time, everything in red text is beyond speculative.
It's just priming the pump for discussions with those who know more and with those who know less,
and it's just a first pass that we're going to continue to develop on.
But broadly, if we can compute inequality relationships, which this paper developed in 1992,
we can bound estimators, test for relative improvements, and basically do stuff with those distributions.
And if we can compute certain kinds of statistical distances, such that a distance requires a length metric,
we can find optimal estimators of parameters, specifically their variances and covariance structure,
in principle and in practice, by finding the maximum informational alignment to other estimators or empirical data.
So, we'll often say, like, if you had the optimum parameterization, you'd be predicting as well as you could.
And so, we want to be able to operationalize that using distances and metrics.
And citation 24.
This is an invariant form for the prior probability and estimation problems by Harold Jeffries.
And Jeffries wrote,

So, if all the parameters in our model, whether there's one, two, or more, are differentiable,
which is to say they're smooth, etc., etc., there are technical details,
then there are certain transformational invariances.
So, just like every Gaussian distribution, by shifting it and stretching and shrinking it,
you can map those onto each other.
It's like that.
It turns out that some of those constraints can even be somewhat relaxed.
For example, this approach may still be effective, even where parameters are not differentiable everywhere.
And this is big for helping us do Bayesian estimation,
which can be seen as a special case of informational transformations
or of manipulations of statistical distributions in the information theoretic or information geometric sense.
Functional analysis.
So, let's begin as tradition in our year 2023 with a brief quote from ChatGPT.
How is functional analysis helpful for us who are learning and applying active inference?
I'll just read the last section.
Overall, functional analysis provides a powerful mathematical tool set for understanding and analyzing the principles of active inference.
And one can read more.
Functional analysis is the study of functions.
Functional analysis.
And here we see one way of showing what a function does in terms of being this box, f of x,
that takes in an input, an argument x, and outputs a result y.
And also, that can be understood as a mapping between or amongst spaces.
And there's a lot more to go into.
Just wanted to bring up that in math, sometimes people have analyzed functions and their properties.
And we're interested in the properties of a special class of functions, which are probability distributions,
well-behaved probability distributions.
What do we do with those probability distributions?
Well, one thing we might want to do is sample.
So, the paper writes,
Sampling methods are critical to the efficient implementations of many methodologies.
Most modern samplers are based on Markov chain Monte Carlo methods,
which include slice samplers, piecewise deterministic Markov chains, and so on.
The original Hamiltonian Monte Carlo, or HMC, which we're going to get to,
algorithm was introduced in physics to sample distributions on gauge groups for lattice quantum
chromodynamics.
It combined two approaches that emerged in previous decades, namely the Metropolis-Hastings algorithm
and the Hamiltonian formulation of molecular dynamics.
So, the way that they state it in the beginning of section three of the paper is,
The purpose of sampling methods is to efficiently draw samples from a given target distribution,
rho, or more commonly to calculate expectations with respect to rho, by equation 33 and other.
They write,
Modern Hamiltonian Monte Carlo, which again we're going to get to in a second,
relies heavily on symplectic integrators, another keyword,
to simulate a deterministic dynamic,
responsible for generating distant moves between samples,
and thus reduce their correlation,
while at the same time, preserving important geometric properties.
Now, we want to make our samples as informative as possible.
If we're just drawing samples and it's the same sample again and again,
one can imagine that it is uninformative.
Conversely, one can imagine a situation where samples are informative.
And that is brought into practice by making sure that the samples are minimally correlated with each other,
as noted above.
And this also has analogy in cryptography.
So, if we're sampling something where the successive samples are 99% correlated,
you can imagine that you're oversampling.
So, you're taking 10,000 frames per second of a YouTube video with 30 frames per second.
I think I'm streaming at 25 frames per second right now.
Conversely, if one were to sample every 10 minutes,
then their correlation structure would also not capture the video's 25 frames per second.
So, in order to generate good and large moves in the space,
we would need perfect knowledge of what the space is,
or how it's generated,
which is sometimes knowable in cryptography.
However, empirically, we need to use heuristics and statistical approximations.
So, this is the applied statistics angle on the analytical relationships that we're going to be talking about.
And it's going to come up again and again,
this tension between analytical formulations, what's true in principle,
and the statistical or numerical or computational applications.
Two, Hamiltonian Monte Carlo.
From Wikipedia.
The Hamiltonian Monte Carlo algorithm,
originally known as hybrid Monte Carlo, still HMC,
is a Markov chain Monte Carlo method for obtaining a sequence of random samples
which converge to being distributed according to a target probability distribution
for which direct sampling is difficult.
So, just a few first pass reflections.
We're sampling, which is to say Monte Carlo,
and Monte Carlo is hearkening back to a different time
when gambling was done in Monte Carlo,
and the state space of all the hands of poker
were too vast to compute analytically,
or equations were not known.
And so, what one used to do, and still does,
is draw samples and say,
well, I don't know if this is the final estimate
on how likely a royal flush is,
but from the two billion hands that I sampled,
there were two royal flushes.
And so, it's one in a billion based upon my sample.
So, we're sampling
because this is a complex distribution
for which an analytical solution is not possible,
not known, not relevant,
or not tractable computationally.
So, there's various situations where we want to sample,
and we don't necessarily have an analytical solution.
When we're sampling from a converged stationarity,
hashtag live stream 26,
of a statistical landscape,
from a numerical perspective,
we understand that landscape well enough to do inference.
So, imagine that we're sampling height estimates
from GPS locations in the X and the Y coordinates,
and we're getting a Z value in our sample.
At some point, we can say,
we're unsurprised by new samples.
At that point, we understand the landscape
well enough to do statistical inference.
And just like the frames per second
in the previous example,
one can imagine,
if the landscape is changing
on the spatial scale of one mile,
and you're sampling every millimeter,
you might be oversampling.
If you were sampling every league,
maybe you'd be too coarse-grained with your samples.
And so, one reason that comes up in science all the time
for using sampling is that the search space
might be just too large.
For example, the combinatorics of a phylogenetic tree
with a thousand species might be vast.
And so, it might be better to say something like,
well, 99% of the million samples we drew
were consistent with X
because an analytical solution
or a brute force search,
neither might be possible.
And the Wikipedia wrote,
this sequence of samples
can be used to estimate integrals
with respect to the target distribution.
So, sometimes we're sampling
not from the target distribution itself,
but rather from a distribution
that is related or transformed
from the target distribution.
This is because sampling directly
from the target distribution
might be difficult
or less than perfectly informative.
So, we might, for example,
hint, hint,
sample from the derivative of the target,
which might help us identify points
where, for example,
the derivative is flat in all directions.
In the case that we're sampling
from a derived landscape
of the target distribution,
this is called a symplectic integrator.
So, let's look at
what a symplectic integrator is.
So, first, backing up
to what is differential geometry.
Differential geometry
is a mathematical discipline
that studies the geometry
of smooth shapes and smooth spaces,
otherwise known as smooth manifolds.
Symplectic geometry
is a branch of differential geometry
and differential topology
that studies symplectic manifolds.
That is, differentiable manifolds
equipped with a closed,
non-degenerate two-form.
Symplectic geometry
has its origins
in the Hamiltonian formulation
of classical mechanics,
where the phase space
of certain classical systems
takes on the structure
of a symplectic manifold.
So, the keyword density is high.
These topics are all
very closely linked.
From the paper,
it has been known for a long time
that the class of symplectic integrators
is the preferred choice
for simulating physical systems.
Only the finest
for our simulations
of physical systems.
These discretization techniques
are designed to preserve
the underlying symplectic geometry
of Hamiltonian systems.
And they also form the basis
of Hamiltonian Monte Carlo
or hybrid Monte Carlo methods.
We're going to come back
to this tension again and again,
which is,
what good is a, in principle,
smooth and differentiable
analytical formulation
if our discretization scheme,
the way that we actually
implement the steps
on a computer,
are inferior.
We might ruin
all those nice properties
that we work to get
about the analytical form.
We might just throw those out
when we discretize it
coarsely or inappropriately.
So, what is a symplectic integrator?
It's a numerical integration scheme
for Hamiltonian systems.
Symplectic integrators form
the subclass of geometric integrators,
which, by definition,
are canonical transformations.
They're transformations
we know a lot about.
Symplectic integrator schemes
!
Integrator schemes
are referring to,
again, just broadly,
both the analytical formulations
and the software packages
and approaches
that we can use
to implement those formalisms.
And these integration schemes
are useful
across difficult estimation problems,
which is why they're used
to study nonlinear dynamics,
molecular dynamics,
like protein simulation,
discrete element methods,
accelerator physics,
plasma physics,
quantum physics,
celestial mechanics.
The time evolution
of Hamilton's equation
is a symplectomorphism,
meaning that it conserves
the symplectic two-form.
A numerical scheme
is a symplectic integrator
if it also conserves
this two-form.
Let's hear more
if this is not correct
or not complete,
but the one-form
is like the differentiation
and integration of a line.
The two-form
is like the differentiation
and integration of a surface,
and the three-form
is like integration
or differentiation
of a volume.
And John Denker
has a great blog post
on the basic properties
of a symplectic integrator.
Some really interesting quotes
that are good
to just keep in mind
when we're hearing
about all these avenues
we're going to be exploring
in the paper.
A symplectic integrator
conserves the area
in phase space
delimited by an ensemble
of systems.
For a periodic system,
there is an area
that is conserved,
namely the area
inside the phase space
orbit of the system.
The main reason
for mentioning the orbit
is to make the point
that there are lots
of different things
with dimensions of area
in phase space.
Some are conserved
and some not.
Some are interesting
and some not.
You have to specify
which sort of area
you are talking about.
So,
another theme
that's going to arise
is we're interested
in very well-behaved outcomes
from a very specific
or constrained,
still broad,
but definitely constrained
set of distributions.
For example,
distributions
that can be interpreted
in an information theory sense
as probability distributions.
What was that mention
of the Hamiltonian
and the shadow Hamiltonian?
So,
the author is right.
For symplectic brackets,
which is the kind of operation
that reflects
the symplectic integrator,
the existence
of a shadow Hamiltonian
can be guaranteed
beyond the case
of splitting methods,
e.g. for variational integrators,
which use variational inference,
which use a discrete version
of Hamilton's principle
of least action.
And we've heard it before
that free energy principle
is a principle
of least action
for inference and action.
And more generally,
for most symplectic integrators
in which the symplectic bracket
is preserved
up to topological considerations
described by
some technicalities
that we can learn about.
As we shall see,
such geometric integrators
can be constructed
by leveraging
the shadow Hamiltonian property
of symplectic methods
on higher dimensional
conservative Hamiltonian systems.
In short,
as a consequence
of having shadow Hamiltonian,
such geometric integrators
are able to reproduce
all the relevant properties
of the continuum system.
These arguments
are completely general.
So,
even before one knows
what the shadow Hamiltonian
necessarily is,
the authors are letting us know
that if we can discretize
the shadow Hamiltonian appropriately
through symplectic integration,
we can provide
a discretization scheme
that ends up staying
consistent and compatible
and all down the middle
with the analytical properties
that we worked so hard to get.
And there were some
different papers
that were cited
and some that were found
during research.
This paper,
Time Step and Shadow Hamiltonian
in Molecular Dynamics
Simulations
by Kim,
demonstrates symplectic integrators
on the simplest possible system,
a simple harmonic oscillator.
So,
if one wants to
go to
a technical example
but one that
builds intuition,
that's a great place to start.
And,
from the Wikipedia article
on energy drift,
these integrators
do not in fact
reproduce
the actual
Hamiltonian mechanics
of the system.
Instead,
they reproduce
a closely related
shadow Hamiltonian
whose value
they conserved
many orders
of magnitude
more closely.
The accuracy
of the energy conservation
for the true Hamiltonian
is dependent
on the time step.
So,
if we can,
for example,
just metaphorically speaking,
capture
a high-resolution
image
of the shadow,
then,
we'll be able
to know something
do something
with the actual.
Some technical details
on Stein's method,
which is a general method
in probability theory
to obtain bounds
on the distance
between two probability
distributions
with respect
to a probability metric.
And,
Stein's method
is used
in the context
of Stein operators
and Stein class,
which we're going to get to
in the subsequent discussions.
Reproducing Kernel
Our discussion of inference
builds upon
the theory of
Hilbertian subspaces
and, in particular,
reproducing kernels.
These inference schemes
rely on the continuity
of linear functionals,
such as probability
and Schwartz distributions,
over a class of functions
to geometrize
the analysis
of integral probability metrics,
which measure
the worst-case
integration error.
We shall explain
how maximum mean,
kernelized,
and score-matching
discrepancies
arise naturally
from topological considerations.
So, we've added
some background links
here to the slide,
but it'll be a great place
to start with authors.
What is a reproducing kernel?
And how is it used
in this paper?
Onwards through the keywords
we go.
Accelerated optimization
and variational inference.
So, here's a 2016 paper
from Michael Jordan
and other authors
and some quotes
from the abstract.
Accelerated methods
achieve faster
convergent rates
than gradient methods
and, indeed,
under certain conditions
they achieve
optimal rates.
However,
accelerated methods
are not descent methods
and remain
a conceptual mystery.
We propose
a variational,
continuous-time framework
for understanding
accelerated methods.
We provide
a systematic methodology
for converting
accelerated higher-order methods
from continuous time
to discrete time.
Our work illuminates
a class of dynamics
that may be useful
for designing
better algorithms
for optimization.
And,
this is going to be,
again,
something awesome
to discuss.
We've talked about
on many streams
variational inference
in the context
of gradient-based
optimization.
For example,
the ball is rolling
to the bottom of the bowl,
bottom of the hill,
and what you can do
is you can take
the gradient,
div, grab, curl,
and all that
of where the ball is
and just go downhill.
And if you designed
the hill
to be the right shape
or you're using
a chosen family
of variational estimators
that are the right shape,
are a good shape,
well-behaved shape,
then you follow
the gradient on down.
And that's how we've talked
about variational inference.
Accelerated optimization
is going to be
accelerated
from that.
And so,
it's fun to think about
and it'll be great
to talk about.
Distributive systems.
The vast majority
of statistics
and machine learning
applications
involve solving
optimization problems.
The author's right.
Accelerated gradient-based
methods
and several variations
thereof
have become workhorses
in these fields.
Recently,
there has been
great interest
in studying such methods
from a continuous
time-limiting perspective.
Such methods
can be seen
as first-order integrators
to a classical
Hamiltonian system
with dissipation.
This raises
the question
on how to
discretize the system
such that
important properties
are preserved,
assuming the system
has fast conversions
to critical point
and desirable
stability properties.
Originally,
such a theory
of geometric integration
was developed
with conservative
systems in mind
while optimization,
in optimization,
the associated system
is naturally
a dissipative one.
More recently,
it has been proved
that a generalization
of symplectic integrators
to dissipative
Hamiltonian systems
is indeed
able to preserve
rates of convergence
and stability,
which are the main
properties of interest
for optimization.
So,
from the Wikipedia
on Hamiltonian systems.
An example
of a time-independent
Hamiltonian system
is the harmonic oscillator.
So,
it's just
a frictionless spring
oscillating around.
The Hamiltonian
of the system
does not depend
on time
and thus the energy
of the system
is conserved.
And so,
we can say
that that is
a conservative
Hamiltonian.
If the Hamiltonian
decays in time,
it is dissipative.
Recently,
the advances
of these authors
and others
have extended
our ability
to make
discretizations
of dissipative
Hamiltonians
that respect
the rates
of convergence
and stability,
which are the main
properties of interest
for optimization.
And,
we've talked about
Hamiltonians
on livestream number 49
with Dalton
Saktivitvelle
on Bayesian mechanics.
So,
pretty cool.
what is conservative,
what is dissipative,
we'll explore.
As the final
keyword,
here,
I just wanted
to start
with a blank
slide on active
inference
and see what
happens in
52.1.
So,
consider
the slide
to be blank
and for the
authors
and discussants,
looking forward
to hearing
how are we
approaching
active inference
given
everything
that we've
just loaded
onto the
table
and everywhere
that we're
about to go
with the
paper.
Let's get
into it.
Section 1,
Introduction.
So,
the authors
begin with,
Differential
Geometry
plays a
fundamental
role in
applied
mathematics,
statistics,
and computer
science,
including
various
domains,
citations
1 through
22,
which can
be shown
here.
Various
citations
from this
well-cited
paper.
The geometric
study of
statistical
models has
had many
successes,
ranging from
statistical
inference,
where it was
used to
prove the
optimality
of maximum
likelihood
estimator,
to the
construction
of the
category
of
mathematical
statistics
generated
by Markov
morphisms.
So,
what are
Markov
morphisms
from
NCAT
lab?
The
formalism
of Markov
categories
can be
thought of
as a
way to
express
certain
aspects
of
probability
and
statistics
synthetically.
In other
words,
it consists
of
structure
and
axioms,
which one
can think
of as
fundamental
in
probability
and
statistics,
which one
can use
to prove
theorems
without
having to
use
measure
theory
directly.
Intuitively,
for the
purposes of
probability,
a Markov
category can
be seen
as a
category
where
morphisms
behave like
random
functions or
Markov
kernels,
hence the
name.
So,
just some
red text
speculation,
it was a
big success
and a
breakthrough
to think
about the
category
from a
formal
category
theoretic
perspective,
to think
about the
category of
statistical
distributions
from an
information
geometric
perspective.
This means
that we
can understand
many analytical
properties and
transformations
of statistical
distributions,
hashtag
Bayesian,
and develop
general
methods that
work for
that whole
category,
like
accelerated
optimization.
And the
applications
are vast.
Originally,
such a
theory of
geometric
integration
was developed
with conservative
systems in
mind.
While in
optimization,
the associated
system is
naturally a
dissipative
one.
Nevertheless,
symplectic
integrators
were exploited
in this
context.
More recently,
it has been
proved that
a generalization
of symplectic
integrators to
dissipative
Hamiltonian
systems is
indeed able
to preserve
rates of
convergence
and stability,
which are
the main
properties of
interest for
optimization.
So,
citation 9,
what is it
about?
2021 paper
on dissipative
symplectic
integration with
applications to
gradient-based
optimization by
some of the
authors.
And,
it's interesting
to pull out
some quotes
from the
abstract and
just hear a
little bit about
what they're
up to.
Recently,
continuous-time
dynamical systems
have proved
useful in
providing
conceptual and
quantitative
insights into
gradient-based
optimization,
widely used in
modern machine
learning and
statistics.
An important
question that
arises in this
line of work is
how to
discretize the
system in
such a way
that its
stability and
rates of
convergence are
preserved.
So,
this is the
sampling problem.
In continuous
time,
the math is
continuous and
nice.
However,
the sampling
problem,
which actually
comes into
play when we
use modern
computational
methods that
are implemented
on discrete
time,
space,
and constraints,
what happens
when we use
unconventional
computing?
That's an
interesting
discussion
question,
but in
practice today,
the
discretization
approach is
going to
matter a lot.
In this
paper,
we propose a
geometric
framework in
which such
discretizations can
be realized
systematically,
enabling the
derivation of
rate-matching
algorithms without
the need for
a discrete
convergence
analysis.
More specifically,
we show that a
generalization of
symplectic integrators
to non-conservative
and in particular
dissipative
Hamiltonian systems
is able to
preserve rates of
convergence up to
a controlled
error.
So,
this is the
advance of this
paper,
that within a
controlled error,
good enough,
they can model
conservative and
non-conservative,
even dissipative
Hamiltonian systems.
Moreover,
such methods
preserve a
shadow
Hamiltonian,
despite the
absence of a
conservation law,
extending key
results of
symplectic
integrators to
non-conservative
cases.
Our arguments
rely on a
combination of
backwards error
analysis with
fundamental results
from symplectic
geometry.
We stress that
although the
original motivation
for this work was
the application
to optimization,
where dissipative
systems play a
natural role,
they are fully
general and not
only provide a
differential geometric
analysis for
dissipative
Hamiltonian systems,
but also
substantially extend
the theory of
structure-preserving
integration.
So,
they made this
generalization in
the case of
optimization,
however,
it's exciting that
it extends even
deeper into the
math and the
symmetry.
Those are a few
highlights from
section one.
on to section
two,
accelerated
optimization.
Vroom,
vroom,
here we go.
So,
there are going
to be a lot
of slides from
sections two
through five,
and to keep the
video a reasonable
length,
I'm going to just
highlight a few
pieces,
not even
necessarily what
I intended to
highlight,
but I'm just
going to go for
it so we can
get through it.
Section two,
we shall be
concerned with a
problem of
optimization of a
function,
finding a point
that maximizes
v of q,
or minimizes
negative v of q,
over a smooth
manifold m,
r,
in the real
numbers.
Many algorithms
and optimization
are given as a
sequence of
finite differences.
Even when these
algorithms are
seen as
discretizations of
a continuum
system whose
behavior is
presumably
understood,
it is well
known that most
discretizations
break important
properties of
a system,
and they
continue to
write.
The analysis
of such
finite difference
iterations is
usually challenging,
relying on
painstaking algebra
to obtain
theoretical
guarantees,
such as
conversions to
a critical
point,
stability,
and rates of
convergence to
a critical
point.
Even when
these algorithms
are seen as
discretizations of
a continuum
system whose
behavior is
presumably
understood,
it is well
known that most
discretizations
break important
properties of
the system.
It can't be
highlighted enough.
When we
implement optimization
algorithms on
modern computers,
we have to make
discretizations in
space and time
and in practice.
So, even if the
analytical properties
of the distribution
are totally
fire, when we
try to solve and
fit models to
empirical data,
unless we also
match that
elegance and
power with a
discretization
approach, we
end up failing
to realize
analytical
promises.
2.1.
The principle
of geometric
integration.
Fortunately, the
authors write,
here comes into
play one of the
most fundamental
ideas of geometric
integrations.
Many numerical
integrators are
very close,
exponentially in
the step size,
to a smooth
dynamics generated
by a shadow
vector field.
A little
whisper of a
shadow
Hamiltonian.
And the
shadow vector
field is
a perturbation
of the
original vector
field.
This allows
us to
analyze the
discrete
trajectory
implemented by
the algorithm
using powerful
tools from
dynamical systems
and differential
geometry, which
are a priori
reserved to
smooth systems.
So, we're
going to be
able to
discretize
our cake
and have
it be
smooth, too.
Crucially,
while numerical
integrators
typically diverge
significantly
from the
dynamics they
aim to
simulate,
geometric
integrators
respect the
main properties
of a system.
In the
context of
optimization,
this means
respecting
stability and
rates of
convergence.
Seems like a
good idea to
respect the
main properties
of the
system.
This was
first demonstrated
in 9 and
further extended
in 10.
Our discussion
will be based
on these work.
So, citation
9, Franca,
Jordan, and
Vidal, mentioned
previously.
And, citation
10, Franca,
Barp,
Giralami, and
Jordan, optimization
on manifolds, a
symplectic
approach, authors'
previous work.
So, big
development.
We can use
geometric rather
than coarse
numerical
integrators, so
our sampling-based
optimization schemes,
including their
discretization,
respect the
main properties
of the system.
Sounds great.
Section 2.2,
Conservative
Flows and
Symplectic
Integrators.
As a
stepping stone,
we first
discuss the
construction of
suitable
conservative
flows.
These are
very well
studied, and
they're very
intuitive.
More
intuitive.
To construct
vector fields
along the
derivative of
x, which
is the
function of
flows along
which some
function is
constant, we
shall need
brackets.
Geometrically,
these are
morphisms, x
star to x, also
known as
contravariant
tensors of
rank 2 in
physics.
So, calling
back the
2 form and
the brackets.
Importantly,
vector fields
that preserve
f correspond to
bracket vector
fields in which
b is
anti-symmetric.
Constructing
conservative
flows is
thus
straightforward.
Unfortunately,
it is a
rather more
challenging task
to construct
efficient
discretizations
that retain
this property.
Most well-known
procedures, namely
discrete gradient
and projection
methods, only
give rise to
integrators that
require solving
implicit equations
at every step,
and they may
break other
important properties
of the system.
Citation 96.
This is the
issue.
Again, no
matter how
nicely behaved,
in principle,
our analytical
underlying smooth
differentiable
function is,
if we
discretize it
and we
chop it up
in a way
that's
inappropriate,
we don't
respect the
properties of
the system,
we don't end
up with being
able to realize
those analytical
promises.
Indeed, in
practice, the
Hamiltonian usually
decomposes into
a potential
energy, associated
to position and
independent of
momentum, and a
kinetic energy,
associated to
momentum and
invariant under
position changes,
both generating
tractable flows.
Thanks to this
decomposition, we
are able to
construct numerical
methods through
splitting the
vector field.
A few ideas
coming together
here, recalling
some of our
generalized
coordinate-based
approaches to
non-equilibrium
steady-states in
Bayesian mechanics,
and also
decomposition of
complex functions.
Note also
that for
symplectic
brackets, the
existence of a
shadow
Hamiltonian can
be guaranteed
beyond the
case of
splitting methods,
e.g. for
variational
integrators, which
use a discrete
version of
Hamilton's
principle of
least action,
and for most
symplectic
integrators in
which the
symplectic
bracket is
preserved up to
topological
considerations
described by
the first
Dirham
cohomology of
face space.
So, for
discussion with
authors and
you all, what
are the
splitting
integrators?
What is split
from what and
why?
What is the
bracket notation
or operation?
And what is a
Poisson bracket?
What is a
Poisson system?
Section 2-3,
rate-matching
integrators for
smooth optimization.
So, having
obtained a
vast family of
smooth dynamics
and integrators
that closely
preserve f,
we can now
apply these
ideas to
optimization.
What is being
set up in this
section and
why?
In equation
7, we see
that the
damping
coefficient,
gamma of
t being
greater than
zero,
reflects the
dissipative
component or
the second
term in that
right-hand side
of equation
7.
So, damping
coefficient controls
the strength of
the dissipation.
One can imagine
that if the
damping coefficient
is zero, the
dissipative side
zeroes out and
b has
conservative
behavior and
so on.
So, what is
being set up
here and
why?
Dot, dot,
dot, dot,
dot.
The existence
of such a
Lyapunov
function,
described above,
implies that
trajectory starting
in the
neighborhood of
q star will
converge to
q star.
So, it's like a
ball rolling to
the bottom of
a hill, just
like we've
always wanted.
In other
words, the
above system
provably solved
the optimization
problem, minimum
of v on
q, such that
q is in the
d-dimensional
real.
Punchline.
We're setting
up a system
with good,
smooth
optimization
characteristics,
ball rolling
to the bottom
of a smooth
hill, that
is also on
the path or
using the
notation of
or prepared
to make the
transformation
to a
tractable
discretization
approach.
So, some
more on the
damping
coefficient.
They bring
up some
common choices
for the
damping
coefficient,
and big O
notation
describes on
the order of
which something
occurs.
For example,
linearly, order
of the
variable, or
sub or
super linearly
as a function
of time or
data points.
So, in
computational
complexity
analysis, people
are often
interested, as
I double the
amount of
data I'm
analyzing, does
that make the
algorithm take
twice as long?
That's linear
computational
complexity.
Does it take
four times as
long?
Does it take
the same amount
of time?
and so on?
And it'll be
great to talk
about the
intuitions and
implications and
generalizations about
how the damping
coefficient influences
the computational
complexity estimates
for convergence in
different settings.
They write,
the conservative
system from
equation 16
reduces precisely
the original
dissipative system
13.
The second
equation in
16 reproduces
14, and the
remaining equations
are equivalent to
the equations of
motion associated
to 13, which in
turn are equivalent
to 8 as
previously noted.
Formally, what we
have done is to
embed the original
dissipative system
with phase space
R2D, so real
with 2D
dimensions, into
a higher
dimensional
conservative system
with phase space
R2D plus 2.
The dissipative
dynamics thus
lies on a
hypersurface of
constant energy
k equals 0 in
high dimensions.
The reason for
doing this
procedure, called
symplectification,
is purely
theoretical.
Oh, come on,
it's not purely
theoretical.
Since the theory
of symplectic
integrators only
accounts for
conservative systems,
we can now
extend this theory
to dissipative
systems settings
by applying a
symplectic integrator
to 13 and then
fixing the relevant
coordinates, 17
in the resulting
methods.
Geometrically, this
corresponds to
integrating the
time flow exactly.
We're going to
talk about a
relationship between
time and
dissipative systems.
After all, it's
dissipative systems
that are dissipating
in time, and so
discretization of
time plays a role
in the appropriate
discretization of a
dissipative
Hamiltonian.
And in Citation
9, previously
raised, such a
procedure was defined
under the name of
pre-symplectic
integrators, and
these connections
hold not only for
the specific example
above, but also for
general, non-conservative
Hamiltonian systems.
So, what is
happening here?
What's an intuition
for conservative and
dissipative systems, and
how have the recent
works of Franca et al
expanded what is
possible?
We are now ready to
explain why this
approach is suitable
to construct
practical optimization
methods.
The coordinate
t sub k becomes
simply the time
discretization, which
is exact.
And so, is u sub
k, since it is a
function of time
alone.
Importantly, u does
not couple to any of
the other degrees of
freedom, so it is
irrelevant whether we
have access to u or
not, because we're
looking to solve a
function of t.
17a can be
substituted in 15
to get 18, and
you can replace 13
to get 19.
We'll talk more
about it with the
authors.
Therefore, the
known rates,
equation 11, for the
continuum system are
nearly preserved, and
so would be any rates
of more general time
dependent dissipative
Hamiltonian systems.
Let us now present an
explicit algorithm to
solve the optimization
problem.
This is all happening
as a consequence of
having a shadow
Hamiltonian, such that
geometric integrators
are able to
reproduce all the
relevant properties of
the continuum
system.
Section 2.4.
Manifold and
constrained optimization.
Following 10, we
briefly mentioned how
the previous approach
can be extended in
great generality to
an optimization problem.
So, equation 21, we
present our
minimization problem,
V of Q, variational
distribution on Q,
citation 10, Franca
et al.
They write, there are
essentially two ways to
solve this problem through
a dissipative
Hamiltonian approach.
One is to simulate a
Hamiltonian dynamics on
T star M by
incorporating the metric
of M in the kinetic
moving part of the
Hamiltonian.
Another is to consider a
Hamiltonian dynamics on
R n and embed M into
R n by imposing
several constraints.
The first approach uses
a Li group.
We'll talk more about it.
An example of a second
approach, one can
constrain the integrator
on R n to define a
symplectic integrator on
M via the discrete
constrained variational
approach by using some
techniques.
The above method
consists in a
dissipative generalization
of the well-known
rattle integrator from
molecular dynamics,
citations 100
through 103,
used in computational
biology.
Section 2.5, gradient
flow as a high
friction limit.
Let us provide some
intuition why simulating
second order systems is
expected to yield faster
algorithms.
As an illustration,
consider figure one on
the left, we'll look at
in a second, where a
particle immersed in a
fluid falls under the
influence of a potential
force, negative delta
sub q on v and q.
So, partial differential
with respect to q of v on
q.
That plays the role of
gravity and is constrained
to move on a surface.
So, ball rolling down the
hill.
We weren't joking about
it.
In the underdamped case,
the particle is underwater,
which is not so viscous,
so it has acceleration and
moves fast.
It may even oscillate.
In the overdamped case, the
particle is in a highly
viscous fluid, such as
honey, and the drag force,
that damping coefficient,
gamma, is comparable or
stronger to the gradient.
Thus, the particle moves
slowly since it cannot
accelerate.
During the same elapsed
time, delta t, an
accelerated particle would
travel a longer distance.
Here's figure one.
So here, why simulating
second-order systems
yields accelerated methods.
So on the left,
constrained particle
falling in fluids of
differential viscosity.
Here on the left, we have
the particle falling through
honey.
It's slowly making its
way to the bottom of the
bowl, but it never really
builds speed.
Its terminal velocity is
being dominated by the
viscosity of the fluid.
Whereas this ball falling
through water or falling
through air is, with
respect to the honey
dampened bowl, this is
like an accelerated
optimization.
optimization.
And they present some
numerical results that
help us bolster that
intuition.
Really fun and embodied
way to think about
optimization.
We've talked about that
ball rolling to the
bottom of the hill and
what the ball does when it
hits a small bump, but
we have not talked about
what media the ball is
floating through and the
media is the message and
the fish doesn't know what
it's swimming through.
section 2.6, optimization
in the space of
probability measures.
It'll be great to
explore more because
we're going to see free
energy calculations on
the stationary density,
KL divergence, and
more.
For now, we can just
say all those
optimization techniques
we were bringing up
earlier, we're going to
be able to do them on
information geometric
spaces that correspond to
probability measures that
are well behaved.
not all distributions are
probability measures or
probability distributions.
Just because you draw a
line doesn't mean you can
use that in part of your
variational inference scheme
for Bayesian statistics.
That's section 2.
on to section 3.

Hamiltonian-based
accelerated sampling.
So we talked about the
Hamiltonian, conservative and
dissipative, and the shadow
Hamiltonian, which is going to
be orders of magnitude better
to approximate.
We talked about gradient-based
methods and how accelerated
sampling is going to help us
accelerate those sampling
techniques.
And now section 3 brings it
together with Hamiltonian-based
accelerated sampling.
section 3.
The purpose of sampling
methods is to efficiently
draw samples from a target
distribution row, or more
commonly to calculate
expectations with respect to
row.
And from the end of the
paragraph.
An efficient sampling scheme
is one that minimizes the
variance of the Monte Carlo
Markov chain estimator.
Monte Carlo, that means that
we're sampling hands from the
poker table.
And Markov chain, which means
that the past only influences
the future through the
present.
It's a quote, memoryless
process.
In other words, fewer samples
will be needed to obtain a
good estimate.
Intuitively, good samplers are
Markov chains that converge as
fast as possible to the target
distribution.
It's like if you laid down a
jump rope on a mountain, if
that jump rope converged
quickly to the topography of
the mountain, it would have
been a fast converging jump
rope.
And we're doing something like
that, but with sampling from
the jump rope.
3.1 Optimizing diffusion
processes for sampling.
As many MCMC methods are
based on discretizing
continuous time stochastic
processes, the analysis of
continuous time processes is
informative of the properties
of efficient samplers.
And diffusion processes
possess a rich geometric
theory, extending that of
vector fields and have been
widely studied in the context
of sampling.
A lot of very fascinating
ideas here.
Stratanovich stochastic
differential equations are
going to come into play.
Equation 34.
More technical details on
diffusion.
The calculus of twisted
differential forms allows us
to have a measure-informed
calculus on multi-vector fields.
What are twisted differential
forms?
I'm looking forward to that
conversation.
What is the untwisted
differential form?
Have we been twisted all along
or not?
And they go on to write,
A fundamental criterion
for efficient sampling
is non-reversibility.
A process is non-reversible
if it is statistically
distinguishable
from its time reversal
when initialized
at the target distribution.
So, once the jump rope
is lying flat on the mountain,
it's like in a position
of reversibility.
Mixing metaphors
at will here.
Measure-preserving
diffusions are
non-reversible
precisely when
some conditions are met.
Intuitively,
non-reversible processes
backtrack less often
and thus furnish
more diverse samples.
So, if you're that ball
rolling on the mountain,
you want to just
plow forward.
And whether you're going
up or downhill,
you want to be sampling
and making moves,
but you don't want to be
going back and forth
because at that point,
it's not an efficient
sampling path.
It's well known
that removing
non-reversibility
worsens the spectral gap
and the asymptotic variance
of the MCMC estimator.
So, time discretization,
spectral gap.
In diffusions
with linear coefficients,
one can construct
the optimal
non-reversible matrix A
to optimize
the spectral gap.
we can have
well-behaved parameters
that help us
get at
optimal
discretization schemes
so that that
shadow Hamiltonian
can be preserved
when we do
discretize it
during optimization
so that we can
respect the key
properties of the system.
However,
there are no
generic guidelines
on how to optimize
non-reversibility
in arbitrary
diffusions.
This suggests
a two-step strategy
to construct
efficient samplers.
One,
optimize
reversible
diffusions.
And two,
add a non-reversible
perturbation.
Equation 36,
citation 125.
Diffusions
on manifolds
are reversible
when
certain things
are the case
and they're not
when other things
are the case.
equation 37.
We got a triangle
pointing down
and a triangle
pointing up.
We're going to
talk more
about it.
Underdamped
Langvin
dynamics
combine all
the desirable
properties of
an efficient
sampler.
It is reversible,
has degenerate
noise,
and achieves
accelerated
convergence
to the target
density.
So,
all of this
groundwork
is helping
us get to
an analytical
formalization
that's going
to have
the right
kind of
properties
so we can
do that
discretization
right on
the shadow
Hamiltonian
so we can
get the
accelerated
optimization
done.
3.2
Hamiltonian
Monte Carlo
A challenging
task consists
of constructing
efficient sampling
algorithms
with strong
theoretical
guarantees.
We now
discuss an
important family
of well-studied
methods known
as Hamiltonian
Monte Carlo
HMC
which can
be implemented
on any
manifold
for any
smooth
fully supported
target measure
that is known
up to a
normalizing
constant.
Some of
these methods
can be seen
as an
appropriate
geometric
integration
of the
under-damped
Langvin
diffusion
diffusing
down that
hill
but in
simpler
it is in
general
simpler
to view
them as
combining
a
geometrically
integrated
deterministic
dynamics
with a
simple
stochastic
process
that
ensures
ergodicity
equation
38.
If we
interpret
the
negative
log
density
V
of
Q
as a
potential
energy
e.g.
a function
depending
on position
Q
one can
then plug
in the
potential
within
Newton's
equation
to obtain
a deterministic
proposal that
is well
defined on
any
manifold
as soon
as the
acceleration
and
derivative
operators
have been
replaced
by their
curved
analogs
so
what
pulls
the
ball
down
the
hill
or
if
you're
an
instrumentalist
what
force
describes
the
movement
of
the
ball
moving
down
the
hill
gravity
I think
there's a
John Mayer
song
about it
surprises
like
gravity
it can
be
understood
as
the
minimizing
force
that
pulls
the
ball
down
the
hill
or
describes
the
movement
of
the
ball
on
its
path
of
least
action
down
the
hill
how
cool
more
discussion
around
38
bringing
these
ingredients
together
we thus
have the
following
HMC
algorithm
given
dot dot
dot
we're going
to compute
a function
according
to
one
a
heat
bath
two
shadow
Hamiltonian
dynamics
and
three
metropolis
correction
that's
the
recipe
we're
bringing
those
ingredients
together
the
above
rudimentary
HMC
method
was
proposed
for
simulations
in
lattice
quantum
chromodynamics
with
M
being the
special
unitary
group
S
U
N
and
used
a
Hamiltonian
dynamics
ingeniously
constructed
from the
Maurer
carton
frame
to
compute
the
partition
function
of
discretized
gauge
theories
this
method
has
later
been
applied
in
molecular
dynamics
and
statistics
there
are
three
critical
properties
underpinning
the
success
of
HMC
in
practice
the
first
two
are
the
preservation
of the
reference
measure
and the
existence
of a
conserved
shadow
Hamiltonian
for the
numerical
method
the
third
critical
property
is the
existence
of
splitting
methods
for which
all the
composing
flows
are either
tractable
or have
adequate
approximations
namely
the
geodesic
integrators
so
geodesic
methods
Buckminster
Fuller
tensegrity
synergetics
or however
you think
about
geodesics
as
paths
in
curved
space
that
is the
kind
of
approximation
and
splitting
we're
gaining
access
to
with
appropriate
discretizations
on
those
balls
rolling
to
the
bottom
of
the
hill
let
us
also
briefly
mention
some
useful
upgrades
that have
been
proposed
in
recent
years
!
So
for those
who
it's
been
a few
years
since
you
checked
in
with
this
domain
this
is
a
great
place
to
look
first
you
can
grant
the
method
extra
integration
steps
when
the
proposal
is
rejected
or
you
can
use
criterion
that
aim
to
ensure
the
motion
is
long
enough
to
avoid
random
walks
but
short
enough
that
we
do
not
waste
computational
effort
such
as
the
no
u-turn
sampler
which
is
integrated
in
a lot
of
software
packages
second
modern
HMC
methods
bypass
this
issue
of
slow
convergence
by
replacing
the
heat
bath
with
an
Ornstein
Olbeck
process
which
ensures

the
overall
algorithm
is
irreversible
an
OU
process
is
like
a
Brownian
diffusion
with
a
linear
regression
so
it
vibrates
and
has
volatility
and
it
has
a
trend
line
that's
linear
third
many
modifications
of the
rudimentary
HMC
algorithm
only
provide
improvements
when
the
acceptance
rate
is
sufficiently
high
a
third
class
of
upgrades
improve
the
acceptance
rate
by
using
the
fact
that
the
shadow
Hamiltonian
is
exactly
preserved
by
the
integrator
big
point
of the
whole
paper
finally
the
metropolis
step
can be
replaced
with
a
multinomial
correction
that
uses
the
entire
numerical
trajectory
excepting
a given
point
along
it
according
to
the
degree
by
which
it
distorts
the
target
measure
some
path
based
inference
methods
with
some
caveats
all
right
on to
section
four
statistical
inference
with
kernel
based
discrepancies
so
section
four
the
problem
of
parameter
inference
consists
!
of
estimating
an
element
theta
star
within
big
theta
using
a
sequence
of
random
functions
or
estimators
theta
hat
n
of
omega
onto
big
theta
equations
!
and more
generally
probability
distributions
that act
continuously
by
integration
on
an
R
K
H
S
H
are
exactly
those
for
which
all
elements
of
H
are
integrable

So
analytically
!
we
have
we
have
that
nice
property
denoting
by
fancy
P
sub
H
the set
of
such
probability
measures
such
that
dot dot dot
we can
define
the
maximum
mean
discrepancy
or
MMD
as
such
more
definitions
!
a
practical
expression
for
the
squared
MMD
So
just
like
in
linear
regression
we're
often
interested
in
the
sum
of
squared
errors
here
we're
interested
in
the
sum
of
squared
MMD
4.1
topological
methods
for
MMDs
just
remember
MMDs
maximum
mean
discrepancy
a
key
feature
of
R
K

S
is
that
they
are
Hilbertian
subspaces
more
details
about
embedding
in
Hilbert
spaces
and
subspaces
the
geometric
analysis
the
geometric
description
of
RKHS
and
MMD
allows
us
to
swiftly
apply
topological
methods
in
their
analysis
there
are
reasons
this
reduces
the
matter
to
a
topological
question
instead
of
defining
T
star
to be
the
set
of
probability
measures
it
is
commonly
done
to
define
statistical
manifolds
it's
desirable
to
embed
fancy
p
within
a
more
structured
space
such as
the
space
of
finite
radon
measures
which
enables
the
method
to learn
the
target
function
independently
of the
data
generating
distribution
what
is
a
radon
measure
we're
going
to
find
out
however
it
enables
the
method
to
learn
the
target
function
independently
of the
data
generating
distribution
sounds
pretty
important
if we
want
that
tale
of
two
densities
MMD
can
discriminate
distributions
that
makes
it
useful
to
do
other
things
let's
find
out
more
section
4.2
smooth
measures
and
KSDs
so
more
information
on
MMDs
and about
making
them
computationally
tractable
and
citations
to
Stein's
method
are
provided
for
195
which
is
the
1972
Stein
paper
and
196
which
is
a
paper
written
by
some
of
the
authors
about
Stein's
method
meets
statistics
a review
of some
recent
developments
from
2021
and
I
thought
it'd
be
fun
to
look
at
some
figures
from
this
paper
and
look
at
the
abstract
so
I'll
put
the
figures
up
above
Stein's
method
compares
probability
distributions
through
the
study
of
a
class
of
linear
operators
called
Stein
operators
while
mainly
studied
in
probability
and
used
to
underpin
theoretical
statistics
Stein's
method
has
led
to
significant
advances
in
computational
statistics
the topics
that are
discussed
in that
review
include
tools
to
benchmark
and
compare
sampling
methods
such as
approximate
Markov
chain
Monte Carlo
deterministic
alternatives
to
sampling
methods
control
variant
techniques
parameter
estimations
and goodness
of fit
testing
and
from
the
paper
they
write
the
list
of
results
given
in
this
paper
are
but
a
mere
sample
of
the
ongoing
activity
in
this
newly
established
area
of
research
at
the
boundary
between
probability
functional
analysis
data
science
and
computational
statistics
for
instance
Stein's
method
has been
used
for
designing
sampling
based
algorithms
!
for
non-convex
optimization
learning
semi-parametric
multi-index
models
in high
dimensions
and
in
Bayesian
statistics
Stein
discrepancies
have been
used as
variational
objectives
for
posterior
optimization
which is
what we're
all about
free
energy
functionals
using
variational
inference
as
objectives
for
posterior
approximation
of
inference
and
action
free
energy
principle
and
these
images
have
some
nice
intuitions
too
here
we see
depending
on our
step
size
we're
getting
different
sampling
when
our
step
size
is
to
the
negative
fifth
power
we're
oversampling

one
part
of
the
space
then
as
we
make
the
step
size
larger
our
samples
are
drawn
from
different
distributions
so
that's
selecting
the
step
size
epsilon
for
a
stochastic
gradient
Langvin
dynamic
and
also
from
the
anastasio
paper
here's
another
fun
way
to
see
that
here
we
have
that
bowl
that
we're
rolling
the
ball
to
the
bottom
of
and
the
stein
points
and
the
stein
thinning
which
is
helping
us
understand
maybe
how
starting
the
ball
in
different
locations
or
critical
locations
accelerates
what
we're
doing
with
optimization
so
cool
to
talk
about
4.2.1
the
canonical
stein
operator
and
Poincaré
duality
there are
two
fundamental
theorems
that help
us
understand
the
integral
differential
geometry
of the
manifold
deram's
theorem
and
the
Poincaré
duality
the
former
deram's
theorem
relates
the
topology
of the
manifold
to
information
on
solutions
of
differential
equations
defined
over
the
manifold
the
latter
which
contains
the
fundamental
theorem
of
calculus
describes
the
properties
of
the
integral
pairing
alpha
beta
of
differential
forms
which
include
the
pairing
of
test
functions
with
smooth
measures
let's
learn more
about
it
4.2.2
kernel
stein
discrepancies
and
score
matchings
technical
definitions
facilitating
stein
variational
gradient
descent
4.3
information
geometry
of
mmd's
and
natural
gradient
descent
these
tools
have
proved
to be
useful
in a
wide
range
of
contexts
!
more
information
about
the
divergence
and how
divergence
can
improve
the speed
of
convergence
by
following
the
natural
gradient
descent
okay
red
text
speculation
beware
so
the
operator
which
is a
phone
routing
system
like
ring
ring
hello
operator
is
constructed
in
section
4.2.2
kernel
stein
discrepancies
and
score
matching
you
can't
have
a
t-test
without
the
t-distribution
the
t-test
statistic
is
using
a
t-distribution
so
a
class
of
fancy
v
a
set
fancy
v
of
vector
fields
or
more
generally
tensor
fields
whose
image
f
under
the
operator
ring
ring
has
mean
zero
under
mu
that's
going
to
give
us
this
discrepancy
the
sd
and
the
stein
variational
gradient
descent
so
there's
some
class
of
v
vector
fields
such
that
the
mean
of
something
about
them
is
zero
does
this
enable
the
central
limit
theorem
or
just
statistics
more
broadly
like
the
parametric
!
and
non-parametric
methods
that we
know
and love
from
SPM
does
that
mean
zero
enable
us
to
use
Gaussian
methods
generalized
Gaussian
methods
generalized
and
does
it
enable
the
proposed
smooth
distribution
the
one
generating
the
shadow
Hamiltonian
that's
getting
inferred
over
to be
interpreted
or used
truly
as a
statistical
distribution
it's
easy to
forget
that
not
all
distributions
are
formal
probability
distributions
for
example
the
area
under
the
curve
from
zero
to
one
of
a
probability
distribution
is
one
something
has
to
happen
but
not
all
functions
have
an
area
under
the
curve
of
one
between
zero
and
one
so
in
variational
Bayesian
inference
the
kind
which
we
do
in
active
inference
in
fact
the
kind
that's
done
in
machine
learning
and
statistics
more
broadly
but
we're
interested
when
action
is
a
parameter
that
we're
doing
inference
on
we're
concerned
with
the
extremely
well
behaved
properties
of
a
certain
subset
of
distributions
so
why are
we doing
this
why is
it
important
that
we
didn't
need
the
input
data
that we
could
construct
measures
that are
independent
of the
input
data
because
we
want
to
enable
the
tail
of
two
densities
we
want
to
make
generative
models
that
can
be
used
generatively
generative
AI
in the
forward
or the
generative
direction
but we
also want
to be
able
to
enable
the
recognition
distribution
which is
from
empirical
data
to do
hidden
state
inference
and so
just like
least
squares
regression
in the
linear
modeling
case
where
the
sum
of
squares
above
and below
the
regression
line
should
be
as
low
as
possible
L2
norm
sum
of
squares
minimization
always
works
never
complains
we
want
that
kind
of
ball
rolling
to
the
bottom
of
the
hill
with
free
energy
functionals
variational
and
expected
free
energy
functionals
as
the
optimized
or
satisfied
imperative
for
optimal
perception
which is
signal
processing
signals
intelligence
and
control
which is
control
theory
or
action
selection
more
technical
details
and
equations
39b
and
39c
so
what
does
it
mean
that
the
resulting
stein
discrepancy
can be
thought of
as an
MMD
that
depends
only
on
rho
and
is
known
as
a
kernel
stein
discrepancy
what
is
that
as
we
did
previously
we
can
remove
the
super
mum
by
rewriting
the
above
as
a
super
mum
over
some
unit
ball
of
continuous
linear
functional
is
this
like
simulating
or
modeling
a
sphere
rolling
on a
landscape
like
we've
been
talking
about
is
the
ball
of
optimal
radius
for
rolling
on
that
landscape
or
what
is
being
optimized
and
what
is
the
unit
the
scaling
or the
scale
specificity
that this
scale friendly
sphere
is scaled
to
equation
42 and
42a
while in
the
Euclidean
space
yields the
diffusion
score
matching
citation
204
barp
et
all
again
minimum
stein
discrepancy
estimators
from
2019
they
write
the
main
strength
of our
methodology
is its
flexibility
which
allows us
to
design
estimators
with
desirable
properties
for
specific
models
at
hand
by
carefully
selecting
a
stein
discrepancy
we
illustrate
this
advantage
for
several
challenging
problems
for
score
matching
such
as
non
smooth
heavy
tailed
or
light
tailed
densities
so
again
just
with a
little
bit
of
speculation
here
and I
think
my
camera
has
frozen
it's
all
good
all
just
go
without
the
camera
okay
um
one
can
estimate
infer
or
optimize
the
zero
point
and
hence
the
variance
structure
of
the
distribution
this
is
going
to
enable
generalized
well-behaved
modeling
again
from all
of those
nice
perspectives
that we
raised
earlier
like
Gaussian
central
limit
theorem
smoothness
statistical
distance
Euclidean
all of
those
well-behaved
properties
that we're
looking for
this is
going to
help us
get there
we are
only
talking
about
a
specific
subset
or type
of
landscape
here
the
one
that we're
doing
variational
inference
on
that's
the
map
this
is
not
the
structure
of
the
territory
these
well-behaved
attributes
of
models
for
better
worse
and
different
through
sickness
and
health
is
because
they're
maps

!
it is
always
the
case
that
our
statistically
nice
generative
models
are
of
a
different
structure
or
form
than
the
generative
process
so this
is
actually
not a
criticism
of
quantitative
modeling
as a
process
in fact
this is
the
entire
basis
of
quantitative
!
modeling
so
we've
approached
this
map
territory
distinction
map
territory
fallacy
fallacy
fallacy
from
many
angles
and
one
will
still
hear
things
like
well
the
structure
of
the
statistical
model
is
not
the
same
as
the
territory
or
how
can
you
say
that
the
organism
has
these
well-behaved
properties
just
because
the
model
does
and
this
brings
a
really
sharp
light
on
it
which
is
we're
doing
this
insane
amount
of
analytical
groundwork
so
that
the
map
has
the
good
properties
not
to
constrain
what
the
territory
is
so
map
territory
all
of the
math
we've
been
talking
about
is
map
we
want
well-behaved
maps
so
that we
can
describe
well-behaved
and
unruly
territories
but
it
isn't
the
case
that
the
organism
minimizes
variational
free
energy
it's
the
generative
model
that
minimizes
variational
free
energy
so
a little
bit of a
leading
discussion
topic
or question
for you
all
feel free
to give
a thought
in the
live chat
or write
a comment
or join
our
discussions
how is
this line
of basic
and fundamental
math
research
by
barp et
all
creating
new
models
that have
the
operational
or
denotational
semantics
that we
want
for
computational
statistics
which is
to say
applied
information
theory
for example
distributions
that can be
interpreted
or used
as statistical
distributions
ideally
directly
compatible
with current
computational
methods
SPM
in matlab
pymdp
in python
and
forny
lab
in julia
and so
on
section
4.3.1
minimum
stein
discrepancy
estimators
more
technical
details
more
citation
to
204
the
parameters
can be
adjusted
to achieve
characteristicness
consistency
bias
robustness
and obtain
central
limit
theorems
see
204
2019
paper
with
barp
et
all
and
let's
just
look
at a
really
cool
image
from
that
paper
figure
one
and
figure
two
pretty
cool
SD
estimators
looking
nice
section
4.3.2
likelihood
free
inference
with
generative
models
so
for
many
applications
of
interests
the
densities
of
the
model
mu
sub
data
cannot
be
evaluated
or
differentiated
we
thus
need
density
free
inference
methods
super
convenient
for
Bayesian
statistics
more
technical
details
information
tensor
under



appropriate
choices
of
kernels
and
models
one
can
derive
theoretical
guarantees
such
as
concentration
and
generalization
bounds
consistency
asymptotic
normality
and
robustness
so
little

bit
of
summary
we
have
good
analytical
and
computational
footing
in
certain
kinds
of
situations
or
under
certain
constraints
certainly
not all
constraints
but
definitely
for
some
that
might
enable
the
efficient
computation
not
just
specification
but
actual
implementation
of
large
generative
models
such
as
described
in
the
paper
of
Friston
et al
2022
designing
ecosystems
of
intelligence
from
first
principles
and
they
use
the
term
ecosystems

of
shared
intelligence
in
that
paper
and
so
it's
relevant
to
learn
about
the
actuality
and
build
intuition
why
slash
how
do
we
know
well
here's
the
one
figure
in
that
paper
of
Friston
et
all
the
one
figure
in
this
absolutely
positional
paper
that
they
have
released
beliefs
as
parameters
of
a
probability
distribution
here's
the
sharpening
of
a
belief
as
a
distance
belief
updating
as
traversing
a
statistical
manifold
which
is to
say
a
lower
dimensional
projected
space
and
what's
being
shown
as
the
parameter
space
of
a
probability
distribution
so
whether
we
see
this
as
gradient
ascent
to
climb
to
the
top
of
the
hill
or
we
take
the
negative
and
we
have
gradient
descent
to
the
bottom
of
the
hill
this
is
the
figure
chosen
by
some
very
well
informed
authors
to
describe
Bayesian
mechanics
and
and


long
and
long
last
we
get
to
section
five
adaptive
agents
through
active
inference
!
We
close
as the
authors
write
with a
generic
use
case
called
active
inference
a
general
framework
for
describing
and
designing
adaptive
agents
that
unifies
all
aspects
of
behavior
including
perception
planning
and
learning
as
processes
!
of
inference
By
exploiting
this
geometric
structure
in a
generic
framework
for
designing
adaptive
agents
we
derive
the
objective
functional
overarching
decision
making
and
describe
its
information
geometric
structure
revealing
several
special
cases
that
are
established
notions
in
statistics
cognitive
science
and
engineering
So
section
5.1
Modeling
Adaptive
Decision
Making
First
they're
going to
talk about
behavior
agents
and
environments
Behavior
is going
to be
defined
as the
interaction
between
an
agent
and
its
environment
and
the
system
is
going
to
describe
the
agent
plus
its
environment
There's
going to
be a
set
of
states
that
are
partitions
from
a
state
space
big
X
External
states
S
are going
to be
unknown
to the
agent
and
constitute
the
environment
States
belonging
to
the
agent
pi
particular
states
are going
to
be
a
subset
of
two
different
things
So
here
is
S
which
is
here
external
states
note
that
in
some
other
settings
S
will
refer
to
sensory
states
so
look
at
the
notation
in
this
paper
and
pi
which
in
other
papers
is
sometimes
used
to
describe
policy
inference
here
is
going
to
describe
particular
states
So
pi
is
O
and
A
O
are
the
observable
states
states
that the
agent
can
see
but
cannot
directly
control
sense
states
and
A
are
the
autonomous
states
states
that the
agent
sees
and can
directly
control
and
those
are
going
to
be
internal
states
and
active
states

figure
2
has
a
great
representation
and
again
note
the
way
that
pi
S
O
and
A
are
being
used
in
this
paper
S
is
the
external
process
hidden
state
latent
state
causal
inference
O
are
the
observations
and
the
agent
process
consists
!
of
pi
which
is
the
observations
and
alpha
or
A
A
is
consisting
of
according
to
the
particular
partition
two
different
kinds
of
states
which
is
internal
states
cognitive
states
and
action
states
and
so
we're
going
to
compute
bounds
for
free
energy
functionals
with
a
special
focus
on
autonomous
processes
because
controlling
our
perception
is
not
possible
and
maybe
not
even
preferable
by
controlling
it
at
the
level
of
what
we
observe

But
rather
if
we
control
our
internal
states
which
is
our
interpretation
of
the
perception
and
our
action
states
we'll
be
doing
optimal
perception
and
optimal
action
so
those
are
the
two
sides
of
the
coin
with
inference
as
perception
slash
learning
and
action
selection
!
That's
how
we
unify
action
and
inference
inactive

inference
is by
caring
about the
bounding
of
self-surprisal
just like
gravity
on our
autonomous
processes
so
this
will
be
super
fun
to
discuss
more
5.1
point
2
decision
making
in
precise
agents
so
what
distinguishes
people
from
small
particles
people
are
subject
to
classical
as
opposed
to
statistical
mechanics
check
out
act
inf
live
stream
49
for
more
on
Bayesian
mechanics
and
some
of
these
distinctions
with
classical
statistical
quantum
and
thermo
in
other
words
they
are
precise
agents
with
conservative
dynamics
precise
agent
definition
5.1
an
agent
is
precise
when
it
evolves
deterministically
in a
possibly
stochastic
environment
more
definitions
and
it's
useful
here
to
highlight
Fristin
et al's
recent
paper
path
integrals
particular
kinds
and
strange
things
which
provides
a
taxonomy
of
things
taxonomy
of
particular
entities
that
run
the
gamut
of
sophistication
from
inert
!
particles
which
have
no
active
states
active
particles
which
have
active
states
conservative
particles
which
have
cognitive
dynamics
that
are
described
as
classical
and
strange
particles
which
represent
in this
visualization
the highest
level of
cognitive
sophistication
in which
those
internal
hidden
states
themselves
have
this
kind
of
what
would
happen
if
this
happens
counterfactual
type
or
thinking
through
other
minds
type
cognitive
model
structure
doing
forward
and
inverse
inference
on
these
great
times
5.1.2
decision
making
and precise
agents
we have
mathematical
formalisms
for decisions
preferences
and predictions
all using
the
partitioned
variables
5.1.2
more
formalisms
we get
to
expected
free
energy
expected
free
energy
is
equation
41k
active
inference
is
Hamilton's
principle
of least
action
on
expected
free
energy
and
expresses
the most
likely
decision
where
certain
features
are met
principle
of least
action
on
manifolds
of
inference
and
action
subsuming
or
bringing
together
inference
and
action
active
inference
free
energy
principle
5.1.3
active
inference
framework
AIF
looks like
it describes
agents
that engage
in purposeful
behavior
we can
rearrange
the expected
free
energy
EFE
in several
ways
each of
which
reveals
a
fundamental
trade-off
that
underwrites
decision
making
this
allows
us
to
relate
active
inference
to
information
theoretic
formalizations
of
decision
making
that
predominate
in
statistics
cognitive
science
and
engineering
figure
three
as
hinted
at
in
the
early
early
keywords
here
on the
top
we have
the
general
formalizations
of
active
inference
and
one
of
the
partitions
or
better
to
say
decompositions
is
shown
here
where
extrinsic
value
is
the
surprisal
about
observations
making
sure
that
what
we're
getting
in
observations
are
what
we
expect
slash
prefer
if
the
body
wants
to be
expecting
homeostatic
temperature
that


is
what
this
is
going
to
determine
and
it
plays
a
role
equivalent
to
reward
in
reward
and
reinforcement
learning
based
approaches
because
we
don't
need
to
actually
set
a
reward
function
but
we
get
something
that
looks
like
self
surprisal
aligned
with
reward
using
the
preference
variable
over
observations
a lot
more to
say
there
and
the
second
term
is
the
intrinsic
value
the
epistemic
value
curiosity
novelty
learning
reduction
of
uncertainty
and
another
partitioning
is
between
risk
and
ambiguity
there
are
four
colored
dots
red
tan
gray
and
blue
corresponding
to
special
cases
so
under
the setting
where there's
no
ambiguity
we
realize
or
manifest
the
special
case
where
control
can
be
seen
as
inference
maximum
entropy
reinforcement
learning
prospect
theory
and
KL
optimal
control
this
is
like
doing
as
good
as
you
can
strategically
or
tactically
given
that
there's
no
ambiguity
in
how
your
decisions
play
out
now
under
the
setting
where
there's
no
ambiguity
or
preferences
a
maximum
entropy
principle
is
realized
and
work
with
Bayesian
mechanics
and
Dalton
et
all
has
shown
that
the
constrained
maximum
entropy
principle
is
dual
to
the
FEP
in
the
case
of
no
extrinsic
value
so
no
quote
reward
no
quote
goals
we don't
use
reward
or goals
in the
active
inference
ontology
but
borrowing
those words
from some
long
long
forgotten
ontology
in the
case
of
no
extrinsic
value
we
realize
the
special
case
of
maximum
information
gain
Bayesian
experimental
design
so
not
to
prove
or
disprove
but
the
maximally
informative
experiment
that's
the
Bayesian
scientific
epistemology
intrinsic
motivation
and
Bayesian
surprise
seeking
out
optimally
informative
stimuli
and
contrast
that
with
the
setting
where
there's
no
intrinsic
value
so
where
there's
nothing
to
learn
we
realize
expected
utility
theory
Bayesian
decision
theory
reinforcement
learning
and
optimal
control
so
special
cases
from
many
different
fields
ranging
from
statistical
mechanics
to
Bayesian
decision
making
and
statistics
integrated
or
perhaps
better
generalized
across
in
the
formalisms
of
active
inference
which
is
something
like
a
Hamilton's
principle
of
least
action
on
variational
or
expected
free
energy
expressing
the
most
likely
inference
and
action
under
certain
constraints
not
the most
rewarding
but
the most
likely
5.1.3
decision
making
minimizes
both risk
and
ambiguity
risk
first
term
on the
right
hand
side
ambiguity
second
term
minimizing

ambiguity
leads to
a type
of
observational
bias
commonly
known
as
the
street
light
effect
when
a person
loses
their
keys
at night
they
initially
search
for
them
under
the
street
light
because
of
the
resulting
observations
I
see
my
keys
under
the
street
light
or
I
do
not
see
my
keys
under
the
street
light
accurately
disambiguate
external
states
of
affairs
first
place
to
look
makes
sense
under
the
street
light
and
the
last
place
you
look
is
where
you
find
it
more
in
5.1.3
decision
making
maximizes
extrinsic
and
intrinsic
value
another
decomposition
of
the
formalisms
of
active
inference
maximizing
information
gain
leads
to
a
goal
directed
form
of
exploration
driven
to
answer
what
would
happen
if
I
did
that
true
counterfactuals
this
decision
making
procedure
underwrites
Bayesian
experimental
design
in
statistics
which
describes
optimal
experiments
as
those
that
maximize
expected
information
gain
and
we've
had
some
great
discussions
recently
in
textbook
groups
and
in
discussion
hours
where
we
contrasted
that
falsificationist
concept
of
accept
or
reject
hypothesis
and
even
the
idea
of
a
scientist
or
researcher
setting
out
to
accept
or
reject
hypothesis
whether
you
take
that
positivist
or
you
take
the
other
path
of
falsificationism
in
both
cases
you
might
end up
with
an
informative
experiment
or
not
but
you
can
easily
imagine
cases
where
you
end up
with
an
uninformative
experiment
because
you set
out to
confirm
something
you knew
or you
set
out to
disprove
something
by
constraining
your
experiment
so that
it was
locally
disproven
in
in
contrast
when
we
take
into
account
the
richness
of
our
generative
model
we
motivate
this
Bayesian
epistemology
and
ultimately
professional
Bayesianism
where
we make
optimal
experiments
in terms
of
their
maximum
expected
information
gain
which
requires
you to
also
state
your
generative
model
decision
making
under
active
inference
weighs
the
imperatives
of
maximizing
utility
and
information
gain
which
suggests
a
principled
solution
to
the
exploration
exploitation
dilemma
great
point
to
jump
into
does
active
inference
simply
by
written
down
by
being
written
down
on
a
paper
resolve
or
transcend
or
dissolve
exploration
exploitation
no
does
it
provide
a
space
or a
framework
a
method
an
approach
software
packages
research
community
that can
help us
address
and navigate
and surf
on the edge
of that
dilemma
absolutely
5.2.1
the basic
active
inference
algorithm
we're
going to
go through
it
with
authors
preferential
inference
we want
to infer
preferences
about
external
and
observable
trajectories
2
for each
possible
sequence
of past
present
and future
actions
a
we're
going to
engage
in
both
sides
of the
coin
perceptual
inference
what
would
I
perceive
if that
happened
and
planning
as
inference
assess
the
action
sequence
by
evaluating
its
expected
free
energy
and
then
3.
Decision
making
execute
the most
likely
decision
at
T plus
one
according
to
some
distributions
sample
from
your
action
posterior
action
prior
that's
like
your
habits
it gets
sharpened
or
modified
with
expected
free
energy
and
then
you
sample
from
the
action
posterior
5.2.1
Sequential
decision
making
under
uncertainty
a
partially
observable
Markov
decision
process
POMDP
is a
discrete
time
model
of how
actions
influence
external
states
in
a
POMDP
each
external
state
depends
only on
the
current
action
and
previous
external
state
that's
the
Markov
property
each
observation
depends
only on
the
current
external
state
and
one
can
additionally
specify
a
distribution
of
preferences
over
external
trajectories
1 and
2 form
the
agent's
POMDP
prediction
model
2 and
3 form
the agent's
hidden
Markov
preference
model
which
defines
the
active
inference
agent
a
simple
simulation
of
active
inference
on
a
POMDP
is
provided
in
figure
4
implementation
details
on
generic
POMDP
are
available
for
more
complex
simulations
of
sequential
decision
making
e.g.
involving
hierarchical
POMDPs
please
see
citations
figure
4
it's a
prediction
model
this is
sequential
decision
making
in a
TMAZ
environment
on the
left
the agent's
prediction
model
as a
POMDP
represented
here as
a
Bayesian
network
on the
right
information
on the
TMAZ
so
here
we have
some
type
of
Bayesian
graph
reflecting
hopefully
a
statistical
system
that's
going to
have
all
of
these
well
behaved
properties
that
we've
been
talking
about
in
the
paper
and
then
the
TMAZ
is
played
out
we'll
talk
about
it
5.2.3
world model
learning
is
inference
due
to a
lack
of
domain
knowledge
it
may
be
challenging
to
specify
an
agent's
prediction
and
preference
model
for
example
how do
external
states
map
observations
should
external
states
be
represented
in a
discrete
or
continuous
state
space
also
some
great
questions
that
come up
every
day
and
are
addressed
in
chapter
six
a
recipe
for
active
inference
modeling
by
time
by
2022
textbook
so
how do
we
get
the
right
priors
or
at
least
approximately
adequate
priors
one way
to
answer
the
question
lies
in
optimizing
!
a
free
energy
functional
f
which
is
an
evidence
lower
bound
we
see
here
variational
free
energy
decomposed
into
an
energy
minus
entropy
and
decomposed
into
a
complexity
minus
accuracy
framing
maximizing
accuracy
usually
results
in
generative
models
involving
universal
function
approximators
minimizing
!
complexity
results
in
organizing
representations
in
sparse
compartmentalized
and
hierarchical
generative
models
where
higher
levels
of a
hierarchy
encode
more
abstract
representations
and
vice
versa
a
computationally
efficient
method
to compare
priors
by their
free
energy
is
Bayesian
model
reduction
free
energy
unifies
inference
and
model
selection
under
a
single
objective
function
5.2.4
scaling
active
inference
planning
for all
possible
courses
of
action
is
computationally
expensive
one
way
to
finesse
this
is
by
planning
only
for
intelligently
chosen
subsets
of
action
sequences
using
sampling
algorithms
!
If you're
interested
in that
check out
the recent
research
on
branching
time
active
inference
similarly
Monte Carlo
sampling
finesses
the
expectations
inherent
in assessing
action
sequences
A
complementary
approach
is to
assess
actions
instead
of
action
sequences
by
conditioning
all
future
actions
to be
optimal
in the
sense
that
they
minimize
the
expected
free
energy
It
leads
to
smarter
agents
whose
computational
complexity
scales
linearly
as
opposed
to
exponentially
in the
length
of
action
sequence
Let's
learn
more
about
it
Scalable
inference
methods
can be
used to
make
active
inference
more
efficient
We
can train
neural
networks
to
predict
the
various
posterior
distributions
including
the
posterior
over
actions
While
training
the
output
of the
neural
network
can be
used
as
an
initial
conditions
for
variational
inference
resulting
in
accurate
inferences
whose
computational
costs
decrease
as the
network
learns
Additionally
optimizing
free
energy
reduces
to
efficient
message
passing
schemes
when
one
imposes
certain
simplifying
restrictions
to the
family
of
candidate
distributions
Lots
of
really
exciting
work
in
neurobiology
and
statistics
around
message
passing
Getting
close
to
the
end
here
A
much
cheaper
implementation
of
active
inference
exists
for
continuous
states
evolving
in
continuous
time
Hmm
Pretty
cool
Par
et al
2022
textbook
Chapter
7
Discrete
Time
Active
Inference
Generative
Models
Chapter
8
Continuous
Time
Active
Inference
Models
This
method
frames
perception
and
decision
making
as
variational
inference
by
simulating
a gradient
flow
on free
energy
in an
extended
state
space
It
can be
combined
with
discrete
active
inference
to
operate
efficiently
in
generative
models
combining
discrete
and
continuous
states
We
talked
about
that
in
Livestream
46
Active
Inference
Does
Not
Contradict
Folk
Psychology
Discrete
Active
Inference
Decision
Making
Active
Inference
DAI
and
Continuous
Time
Motor
Active
Inference
Being
Used
Together
Also
seen in
the
Par
Adult
!
Textbook
As an
example,
High
Dimensional
Observations
in the
Continuous
Domain
e.g.
Speech
Processed
through
Continuous
Active
Inference
are
converted
into
discrete
abstract
representations
e.g.
semantics
and we
can even
go further
and say
rhetorical
and narrative
information
spaces
Based on
these
representations
the agent
makes
high-level
categorical
decisions
e.g.
I want
to move
over there
which
contextualize
low-level
continuous
actions
e.g.
the
continuous
motion
of a
limb
towards
the
goal
location
and
that
is
how
the
paper
ends
so
closing
thoughts
if
anybody
wants
to
write
a
comment
live
feel
free
to
do
so
we'll
be
over
very
shortly
what
are
the
implications
of
this
work
we
have
an
open
space
to
talk
about
it
what
questions
and
discussion
topics
are
you
interested
in
please
write
comments
before
or after
the
dot
one
and
the
dot
two
so
we
can
have
those
interesting
discussions
and
just
as a
little
bit
of a
closer
I'll
share
some
stable
diffusion
images
that
were
generated
using
the
paper
title
as
well
as
various
other
terms
free
energy
lots
of
fun
images
a lot
of
good
balance
to
some
of
the
technical
aspects
that
were
being
described
in the
paper
was
good
to
look
at
what
diffusion
looks
like
aesthetically
and
so
that
is
the
end
of
this
live
stream
52.0
I
hope
that
you
found
it
useful
that
you're
interested
to
act
and
serve
to
learn
more
contribute
more
write
a
comment
make
it
happen
in
your
own
life
or
in
your
own
way
with
this
honestly
challenging
paper
so
if
you've
listened
this
far
thanks
a lot
for
your
attention
and
looking
forward
to
52.1
and
.2
when
we will
speak
with
some
authors
and
some
of
you
so
till
next
time
thanks
again
and
see
you
in
the
dot
one
to
