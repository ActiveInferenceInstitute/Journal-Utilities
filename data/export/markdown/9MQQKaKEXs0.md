---
title: "ActInf Livestream #045.0 ~ "The free energy principle made simpler but not too simple""
category: "Livestream"
series: "Livestream_045"
episode: "0"
duration: "1:54:53"
url: "https://www.youtube.com/watch?v=9MQQKaKEXs0"
views: 788
exported_at: "2026-02-18T22:37:37.715794+00:00"
format: markdown
---

# ActInf Livestream #045.0 ~ "The free energy principle made simpler but not too simple"

Hello everyone.
It is ActInfLab livestream number 45.0.
It's May 27th, 2022, and we're discussing the paper, The Free Energy Principle Made Simpler
But Not Too Simple.
Welcome to the ActInfLab.
We're a participatory online lab that is communicating, learning, and practicing applied active inference.
You can find us at the links on this slide.
This is a recorded and archived livestream, so please provide us with feedback so we can
improve our work.
All backgrounds and perspectives are welcome, and we'll be following video etiquette for
livestreams.
If you want to learn more about the livestreams or any of the other projects to get involved
at ActInfLab, head over to activeinference.org.
We're in stream number 45.0.
Our goal is to learn and discuss this very interesting paper, The Free Energy Principle
Made Simpler But Not Too Simple by Carl Friston, Lancelot da Costa, Noor Sejid, Connor Heinz,
Kai Ultsofer, Gregorius Pavliotis, and Thomas Parr.
And just like with all the .zero videos, and indeed all the videos, this is an introduction
and an overview to a quite technical and lengthy-ish paper.
It's not a review or a final word.
This is like the opening context for some of the coming discussions we're going to have
in the following weeks and beyond.
And we're going to first just say hello, introduce the big question, the aims, claims, abstract,
and roadmap.
Then we're going to give an overview of some of the keywords that are in the paper.
Then we're going to go through the sections of the paper with a focus on some of the key
points, the formalisms, and the figures especially.
So it should be a great discussion.
And let's get into it.
We'll start with just an introduction and saying hello.
So I'm Daniel.
I'm a researcher in California.
And I'll pass to Brock.
Brock, thanks for joining and for all the contributions in this .zero.
Yeah.
It's exciting to be here and participate in the ACDEMF lab.
And yeah, I'm just really drawn to this topic.
And this paper is a great starting point for that.
It's really got a lot of detail to dig into and a lot to learn.
So yeah.
Okay.
So, one of the big questions or one way to state the big question was what are the foundations
of the free energy principle and what does it contribute?
In the paper, they write that they start from a description of the world in terms of a random
dynamical system, systems changing through time, and end up with a description of self-organization
as sentient, sensing, active behavior, and that's active inference.
So that's the question that we're wondering about.
We're all wondering about what is the basis and the essence and the implications of the
free energy principle.
What would you say about that or what were some big questions that you had coming into
and out of this paper?
I think my biggest question around like the free energy principle is kind of it's general,
how general is it?
Where does it end?
And because it seems so...
They say in the paper also, it's like, it's pretty simple.
It's kind of podological in some sense.
So yeah, that's one of my questions.
Where does it begin?
Where does it end?
And like, how general is it?
The other question is, yeah, how does it emerge?
Or what does it look like at different scales?
Awesome.
So we'll be returning to questions again and again.
Let's check out the aims and the claims of the paper.
So again, it's the free energy principle made simpler, but not too simple.
And the authors are listed here.
The paper describes that it's trying to present the free energy principle as simply as possible,
but without sacrificing too much technical detail.
And that's sort of a pun slash self-reference.
That's what modeling in that Pareto optimal or Bayes optimal way is.
And that's going to come back as a theme again and again, giving information, but not overfitting
nor underfitting.
And then several claims that they make are that they're going to step through the formal
arguments that lead from the description of a world as random dynamical system to the
description of self-organization in terms of active inference and self-evidencing.
They're going to discuss Bayesian mechanics and how those Bayesian mechanics have the same
starting point as quantum, statistical, and classical mechanics.
And then they're going to differentiate this Bayesian mechanics for particular systems from
some of these previously mentioned mechanics in that careful attention is paid to the way
that the internal states of something couple to its external states.
Some of the aims and claims, although many more will be introduced and are discussed in
the paper.
Any thoughts on that?
Or if you'd like to.
Oh yeah, go ahead.
Yeah.
Just, well, that essentially that it's, you know, it's a self-evidencing, self-describing
system.
But again, just very, it seems to fit with a lot of different domains and a lot of like
just observed experience.
So.
Cool.
Would you like to read the abstract?
Sure.
Sure.
Uh, this paper provides a concise description of the free energy principle, starting from
a formulation of random dynamical systems in terms of a Langevin equation and ending with
a Bayesian mechanics that can be read as a physics of sentience.
It rehearses the key steps using standard results from statistical physics.
These steps entail by establishing a particular partition of states based on conditional independencies
inherit from sparsely coupled dynamics to unpacking the implications of this partition in terms
of Bayesian inference and three describing the paths of particular states with a variational principle of least action.
Teleologically, the free energy principle offers a normative account of self-organization in terms of optimal Bayesian design and decision making in the sense of maximizing marginal likelihood or Bayesian model evidence.
In summary, starting from a description of the world in terms of random dynamical systems, we end up with a description of self-organization as sentient behavior that can be interpreted as self-evidencing, namely self-assembly, autopoasis, or active inference.
Awesome.
Okay, let's go to the roadmap.
So this paper has a layout and it'll be awesome to hear from the authors about why they've laid it out as well as numerous other details.
So we're looking forward to those discussions.
In section one is an introduction and they wrote at the end of the introduction.
The remaining sections describe the free energy principle.
Each section, that's two through eight, focuses on an equation or set of actions.
The ensuing narrative is meant to be concise, taking us from the beginning to the end as succinctly as possible.
To avoid disrupting the narrative, we use footnotes to address questions that are commonly asked at each step.
We also use figure legends, captions, to supplement the narrative with examples from neurobiology.
So, there's a main narrative thread that's going to touch on sections two through eight, each of these being like a single or a cluster of formalisms.
And then, especially in the footnotes, which are formulated as questions, and in the figure captions, which are sometimes quite lengthy and include examples and citations and so on, more of the biological details and inspiration are added.
But the main line narrative is going to be touching on these formal areas.
So, we're going to next.
We're going to next discuss the keywords at an overview level and just describe like some of the broader topics that might lead someone to find this paper, be curious about it, or want to cite it in one of those domains.
And then, we're going to just jump right into the introduction.
Each of the nine sections will be clearly indicated which section we're in, and we'll be following the order of the paper, bringing in a few other resources as.
We saw fit in the preparation.
And we're just going to focus on some of the dots, connecting a few and leaving many, many for the dot one and the dot two discussions.
Again, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see this is where we are, we'll see
variational inference and Markov blanket so Brock tell us about Bayesian
Bayesian analysis um so it's basically a um yeah it's an analysis method for
determining the posterior probability which is basically your in inactive inference and this is
going to be something like your beliefs after having evidence added to your prior beliefs which
are something approximately like a hypothesis so you have the equation here and also this word
explanation that's essentially what I just said um so you're adding you know observation to
hypothesis and changing um trying to reduce the um trying to approximate the
uh this PHV here uh over you the press for your probability so um
is pretty foundational to yeah a lot of statistics and physics and other things
thank you yes totally agreed Bayesian statistics it's a big
topic and just like you said it's about how prior beliefs meet incoming evidence and how that is
updated to form posterior you know after the evidence beliefs versus before the evidence and
that can be done in this continuous cycle and a lot of the variables that we're going to be seeing and
um um we'll see all this is um we'll see all this is um we'll see all this is um we'll see all this is







example it might be a variable that represents a systems prior about something or something might
come in and that might be evidence so we're going to be working within a bayesian statistical
framework rather than for example a frequentist p-value driven statistical framework but we'll
come to these details along the way how about non-equilibrium this is a i think a much fuzzier
topic um like the tradition like historically you know science studied like equilibrium state
systems and non-equilibrium state systems are like more uh relatively newer things um and so
non-equilibrium is is um these are things that were mentioned in the paper it was like flows
of between transitions of between like finite sets of states having an attractor in a system that over
time the you know perturb perturbations in the system um still act as a set of characteristic states
to which the system is attracted over time um so again non-equilibrium being like a higher energy
level state that is you know to its local environment um but nonetheless distinct definite separate and
over time continuous so just looking at the animation you put here it's like the brick at some time scale
is out of equilibrium like the brick will also dissolve but for some model of a certain time frame hours
it could be seen as being spatially or just materially in an equilibrium and then looking at these two
moving entities it's kind of like two kinds of non-equilibrium there's like the low bar non-equilibrium
this mechanical bird on the right side the water dipper and so it is returning to these characteristic
states it's not just staying in one location it's returning to drink the water again and again so it's
not in spatial equilibrium but also there's like this stationarity or there's something about it that is
constrained and then the um ostensibly living bird i guess on the cartoon on the left is like non-equilibrium
of an even higher or more complex type because that bird might like fly away or do something else so
there's like a gradient from things that are like the ball at the bottom of the bowl
in equilibrium and then progressively mechanical systems that are returning to attracting states
and then what does it mean for biological systems to be or to be modeled as returning to attracting
states like sleep or a certain body temperature certain blood glucose any other thoughts on that or we can
carry on yeah just yeah there's this uh different like time scale set of states larger smaller and
uh navigating traversing those states yeah internally right and so i guess it just it depends where
you're drawing the the time scale awesome but they can be modeled differently like that right
how about self-organization i think this one like um maybe it sounds like uh just as complex but i think
this is like really familiar for most people they have a good idea of what this is um and like you know these
like examples here um of of uh non-equilibrium systems um that you know have some um symmetry asymmetry of
constraints that over time causes them to um take a particular path through that um you know set of
states towards one attractor or another um cellular meiosis and mitosis here um black hole mergers
nuclear fission nuclear fusion very large very small mezzo in between scales here um in the paper um
um referencing fep they were they said it was fep was about kind of turning on its head this traditional
what what must things do in order to exist framing of systems and physics to if thing if it exists
and what must they do and so this is saying you know we have now a bayesian evidence of black hole mergers
what must it be doing for that data now that new evidence to
um yeah exist like what how will how does nuclear fusion you know how does that turn into two atoms
turning into one atom what must it be doing instead of the other way around awesome yeah big topic many
angles on it but sometimes those inversions like axel constance paper that we discussed in live stream 34
with um it's about how you got there so conditioned on some thing which we're going to return to
existing being perceived being modeled what must that thing be doing in order to exist not what has
to happen for the thing to exist but we're going to come back to that and then um the last two
we'll just give a first coat of paint because we're going to see them in their technical glory soon so
what is variational inference about um i'm actually less clear on this but uh related to bayesian inference
it's about approximating that um posterior probability the um after um things happen
like but what you know um to what resolution can you kind of you know what precision can you
state about that and also trying to have a lower bound for the marginal likelihood of evidence of the
observed data so how likely are you to see um the data that would cause that to be that would lead to the
process of probability being what it is that was my understanding of this yeah awesome what is the
divergence um it'll be awesome to hear the authors and others perspectives but places where we've seen
variational bayesian inference before first off it's not an innovation of active inference
variational auto encoders and variational bayesian methods are being used in active inference with the
partial novelty of action being considered as a parameter rather than just sensory parameters but
it's used in situations where exact base is intractable and sampling based approaches like monte carlo are also
not tractable or not plausible and so variational inference is about minimizing the divergence between
q and p mind your q's and p's as they say up there and making sure that q is from a family
of distributions that is tractable and easy to optimize even if p is something that is challenging
instead a different distribution for example one that has a shape looking more like a parabola more
like a bowl can be fit with q and then there's still some detail like if p truly were bimodal would you
want the one that identifies and rests q on top of one hump and ignores the other hump or would you want
the q that is kind of centered at a place where neither of the p humps are but contains some density
in both so those are some detailed questions but in general it's about minimizing the divergence between
q and p as a means of approximating what exact base would be doing in the asymptote if the divergence were
zero you would be having the perfect approximation of q on p and then anywhere other than the divergence
being zero there's a monotonic way for you to get towards that and then markov blanket which we're
going to come to in multiple formalisms but just what comes to mind when you hear markov blanket and
what did you want to show here everything this one is like i feel like this is the most easy to understand
one somehow it's um like this picture here you can see is a bunch of dots that are different colors
right and you have um like a circular concentric circles here um and that's you know to that this
large inside the large square scale there's this like yellow line that separates all the outside dark blue
from the inside orange and red and but there's also an an orange inside circle these these yellow and
orange are kind of in a um in a relationship that keeps the dark blue and the red separate independent of
each other but you also have these obviously you know these smaller scale inside the red inside the yellow
inside the orange here right these other scale of of the same thing like that it is um in some sense
either recursive or fractal or um you know locally having this same kind of dynamic of two layers
conditioned on each other to keep an external um and an internal state independent
of each other um awesome yes which is everything i feel like it's every thing which we're going to be
going to yes mind the space and um it's an exciting topic and there's a lot of ongoing discussions and
developments here's a recent paper by casper hesp and there's many other valuable commentaries on
emperor's new markov blankets by yellow bernberg which was previously on a live stream so there's many
many technical and philosophical and implementation discussions around identifying markov blankets reifying
them and so on and we're going to get there so into the paper we go we're in section one introduction
the paper we go to the paper we go to the paper we go to the paper we go to the paper we go to the paper
it is said that the free energy principle is difficult to understand no citation who's saying that no one is
saying that this is ironic on three counts first the fep is so simple that it is almost tautological
circular reasoning indeed philosophical accounts compare its explanandum what it explains to a desert landscape in the
sense of quine a quinean desert landscape as per what clark wrote and we'll return to that in a second
a second reason for the irony is a tenet of the fep is that everything must provide an accurate account
of things that is as simple as possible including itself finally the fep rests on straightforward results
from statistical physics so one is it's not difficult to understand it's so simple it's circular
two is how can it be difficult to understand when everything is as simple as it must be including
the fep literature that's that's some high level irony and then the third reason is how could it be
difficult to understand when it rests on straightforward results from statistical physics and then i just
wanted to highlight this clark 2013 citation and the desert landscape because that seems like kind of like
an oblique reference um but here's what clark and also here's two representations of desert landscapes
so they're not all bad in fact but what clark wrote was um referring to radicalisms that might exist within this
framework in extending the models to include action action-oriented predictive processing which is very very similar to active inference
we might simultaneously do away with the need to appeal to goals and rewards replacing them with a more austere construct of predictions
so i don't want to do this or i'm not rewarded by doing that i'm just making predictions and expectations about what might happen and then fulfilling them or diverging from those fulfillments and so um that is this desert landscape vision there are neither goals nor reward signals as such
instead there are only learned and species specific so kind of developmental and evolutionary
expectations across spatial and temporal scales that are in control of perception action loops and so
what are we explaining or explaining away that's this desert landscape notion and that's how the authors are beginning the paper with a sort of preemptive
tripartite broadside dissuading one from thinking that this is going to be difficult to understand
before launching into the subsequent eight sections that might give you some
um evidence to the contrary but yeah any thoughts on that
i just thought yeah the desert liquidian desert landscape very apt description and um
yeah physical sort of yep it it lines up and yeah like i said that this uh
it does seem tautological like a lot of these concepts if you think about them
um from like the statistical physics it's like obviously but um
didn't there's just a lot of um area there to be covered right yes and also note that clark in 2013
wrote i remain unconvinced even if the austere description is possible this would not justify the
claim that this is the better tool for understanding the cognitive economy so it's it is intractable so
it's like yeah what yeah yep awesome so still in the introduction the author is right before starting
it might help to clarify what the free energy principle is and why this big question alert
many theories in the biological sciences are answers to the question what must things do in order to
exist and some answers but we could think of probably many others that people have raised
so if if you ask somebody what does something have to do in order to exist some answers could be like
well it has to resist dissipation it has to replicate or it has to reproduce or propagate
some way like there's stuff it has to do to be there the fep turns this question on its head and asks
if things exist what must they do more formally if we can define what it means to be something
can we identify the physics or dynamics that that thing must possess to answer this question the fep
calls on some mathematical truisms that follow from each other then they write much like hamilton's
principle of least action the fep is not a falsifiable theory about the way things behave it is a
description of things that are defined in a particular way and for more reading on this here's a 2018
interview with fortier and myself and with carl friston and here there's some discussion around
notions of falsifibility can the fep be falsified or what is the relevance of falsification which is
a frequentist idea in this bayesian meta bayesian post bayesian whatever epoch or mode that we're in
and just one really interesting quote is um from carl i would assert that the notion that a framework can
have the attribute falsifiable is a category error the notion of falsifibility is thus a very weak notion
because it's actually reflecting rejecting a null hypothesis in favor of an alternative hypothesis
that has some limitations um including the sort of uh the transcendental arguments on falsification
which is just that belief is rarely scrutinized using a falsificationist framework
and then dropping from the transcendental argument into a more uh history of statistics and science
when we move from frequentism towards bayesian statistics where the p-value and so on and the
parametric distributions are seen as like special cases but not the whole substance of the statistics
carl's suggesting that a better way to frame evidence-based selection of hypotheses
which is ostensibly what falsification is after as well is in terms of how much empirical evidence is
accrued by competing hypotheses and that's quite a different model than uh can and then falsify the ones
that aren't true let's shoot down the ones that don't exist so this is quite an interesting area um what
would you say or add to this there's a word uh verisimilitude i think that is exactly what he's um
describing here again just how much evidence is accrued rather than yeah i mean that that's in practice
how it works so i don't completely understand the notion of fossil fallibility is is it's really important
but um like like durac um had this notion of beauty or and and he's saying look if the equation's really
beautiful then maybe you check your experiment first um so like you were saying it's kind of like
um that's not falsifiable but then what do you mean by not falsifiable and that is that you're not
examining that claim it's kind of there's a you know infinite regression there of falsifiability that
makes it intractable which is why taking the opposite approach of just stacking up the evidence
is you know a way to make the same it's the same thing you know but attractable version kind of of it
right so awesome they're right um again picking up on that last quotation there that the fep is not a
falsifiable theory about the way things behave it's a description of things that are defined in a
particular way let's talk about utility is such a description if the fep is indeed a description is it
useful in itself the answer is probably no oh well then we can stop reading in the sense that the
principle of least action does not tell you how to throw a ball however the principle of least action
furnishes everything we need to know to simulate the trajectory of a ball in a particular instance
in the same sense the fep allows one to simulate and predict the sentient behavior of a particle person
artifact or agent i.e some thing this allows one to build sentient artifacts or use simulations
as observation models of particles or of those other mentioned types of systems
these simulations rest upon specifying a generative model that is apt to describe the behavior of the
particle or person at hand at this point committing to a specific generative model can be taken as a
commitment to a specific and falsifiable theory later we will see examples of these simulations so it's like
the linear regression concept is not even where you would want to focus the brunt of your falsifying
effort but if there are two different linear regression models we might ask which one is preferable or
which one is falsified by doing some subsequent perturbation or experiments but the linear regression
framework is like a framework hence not falsifiable in the way that people often expect and deploying a
specific generative model analogous to like a specific linear regression model but different that is where
there's a commitment to a falsifiable theory well i think the amygdala connects to this that way that
could be tested and that evidence could be evaluated within a falsification or bayesian base factor framework
falsifying the concept of generative models they would be have crossed that bridge and now could be
engaging in falsification and evidence comparison within some constrained space anything to add on that as we
close the introduction yeah just again what is a linear model versus a generative model of like
the the linear model will yield some approximation that's not a necessarily a real um possible observation to
falsify the generative model will produce many things that you might not observe possibly but um some that you
will and then could potentially be falsified like it gives specific examples so yes it's almost like it takes
this this this meso scale and it it separates the the milk from the cream and the fep um flies over
falsification and then once you're committed to a specific generative model it's actually written down
not just speculated that it could be written down then it's like oh well then it's trivial or against it
so we've kind of separated out the framework like language as a framework like dave just mentioned in the
chat how would you falsify a language you would not any more than you would falsify a conceptual framework
so one could not falsify a language like english but things that are said within english might be
amenable to being tested once they're actually said using that framework
very interesting evidence stacked up or not versus alternatives just like language or evolution awesome
so recall the roadmap we're now going to head into the next sections each of which is going to be
building on each other in this concise narrative however also semi standalone in their focus and we're
just going to do basically a first pass and some contextualization because we have a lot of time
in the coming weeks to discuss these topics in more detail so we're going to go to section two systems
states and fluctuations okay so they write we start by describing the world with the stochastic
differential equation pavliotis 2014. so this is um a citation to the book stochastic processes and
applications of diffusions processes um and uh just one preliminary note this is not the same sentence as
the world is a stochastic differential equation we start by describing the world with a stochastic
differential equation so leave your realism at the door we're describing models here they write why
start here the principal reason is that we want a description that is consistent with physics here's
some discussion questions what does it mean to be consistent with physics what does it mean to be
consistent with physics in theory or in principle or in practice and then they write this follows because
things like the schrodinger equation in quantum mechanics area a fluctuation theorems in statistical
mechanics area b and lagrangian formulation of classical mechanics area c three different mechanics
quantum statistical and classical can all be derived from this starting point so we're going back to like
the last common ancestor of those three different mechanics and then that is where bayesian mechanics
is going to also be initiated from in short if one wants a physics of sentience this is the place to
start why start where where are we going why are we going anything you want to add here
um no i think again just that yeah that at all these scale physics it's it's odd that you would be able to
reproduce you know derive all these things from something that's not fundamental or important in some way so
you know awesome they write we are interested in systems that have characteristic states this means
the system has a pullback attractor the sets of states that the system will come to occupy from any
initial state so the rubber band is going to pull back to its resting state if it's allowed to
you and formalism that stochastic differential equation describing the rate of change of the states
so x are the states the tau is the time and the dot notation is the derivative with respect to time
so how states are changing is equal to their flow f of x f for flow and random fluctuations omega so like a
signal and a noise term there's the the flow the ocean current and then there's the vibration that
isn't the directed flow and this separation of scales is going to come back again and again so dot notation
again means the derivative with respect to time so how things are changing with respect to time through
time this yellow means that time and causality are baked into everything that follows in the sense that
states cause their motion this equation is itself an approximation to a simpler mapping from some
variables to changes in those variables with time this follows from a separation into states and random
fluctuations implicit in formalism one where states change slowly in relation to fast fluctuations so if
this term the noise term is dominant then there will not be movements flow like movement on a manifold
there's some more details but things are changing in different ways
different kind of stochastic equations that are going to be presented here and in the book and in the
citations they help us see different parts of how we can use dynamical models to understand physics and
specifically the physics of particular cognitive slash sentient systems
then in the footnote they ask a question why is the flow not a function of time and that's what we're going
to return to in dot one how is time dealt with or not dealt with similarly or differently than other
frameworks or other physics and then just to stay on this formalism one and then please give any other
thoughts this last line of p of x equals question mark the next step shared by all physics so
those three areas that we described classical statistical quantum and bayesian is to ask whether anything can
be said about the probability density over the states the question mark in one so this is the common
grounding this is the last common ancestor of the multiple physics and now we're going to take it in a
different direction a lot can be said about this probability density p of x which can be expressed in two
complementary ways and this is going to introduce a very important distinction and dialectic here are the two
complementary ways left side blue density dynamics using the fokker-plank equation aka also known as the
forward koulmogorov equation here's formalism two the fokker-plank equation describes the change in density
due to random fluctuations and the flow of states through state space this is like a field model and then the
the second complementary way in orange on the right side in terms of the probability of a path through
state space using the path integral formulation and they write for formalism three conversely the path
integral formulation considers the probability of a trajectory or path in terms of its action so
what are two things that you can say or more about the probability density what are two complementary ways
that it can be expressed what are important similarities and differences between this fokker-plank
formalism two approach and the path integral formulation of formalism three are there other
complementary ways to say it or other ways to say what is here but this is just to introduce what's
going to be very important and going to be moved back and forth in the course of this paper which is
one representation that's more field-like continuum-like and then another representation that's going to be
more trajectory and path based what do you see in there um yeah we we discussed this like really briefly about
um you know like a continuous um space versus a kind of discrete or instantaneous space like there's
some um um mostly i guess metaphor there analogy um but when you just asked this question of what are
you know other ways to say this like it's it's um the action trajectory their uh path is like a
sounds like like a like a like an action density or an energy density like where the where is the kind of um
um you know path of of it the energy and the whole system gonna um you know events itself right so it's it's
it's like an action density gradient or something like this right um

um
yeah cool real interesting both the fokker plank and the path integral formulations the formalism 2 3
dialectic inherit their functional form from assumptions about the statistics of random
fluctuations in one so recall one with the flow and the random fluctuation term for example the most
likely path or path of least action is the path taken when the fluctuations take their most likely value
of zero so we're gonna explore this more but the path of least action is not using action in the same
way that active states are exactly path of least action does not mean the laziest or the least energetically
costly or the least mobile thing to do it's not that it is so that is what we're going to explore
what does it mean to minimize action in this framework the motion on the path of least action is just the
flow without random fluctuations so if the question were you're trying to run in a straight line forward
there's two forces there's the flow of you running forward and then there's your thermal vibrations
so in one limit the flow might absolutely be overwhelming the random fluctuation of least
action would be that person running forward conversely if that person was like the size of one molecule
they would be being buffeted by stochastic thermal vibration and so they would not be following
that path of least action the same way loose metaphor hopefully doesn't misrepresent but paths of least
action will figure prominently in the following sections of the paper especially when considering
systems that behave in a precise or predictable way we will denote the most likely states and paths with a
bold typeface so it can be a little subtle sometimes and so we'll try to clarify notation and get
assistance as we can but like this is like a bold x like a bold x through t is the minimization of that
unbolded function with respect to the action a of those states through time and that is going to be related to
the change in x through time being just only the flow so here it was like x dot of t equals the flow of
x plus a noise term here if the noise term is zero you can drop it
and then they write although equivalent the fokker-plank and the path integral formalisms
this dialectic that we've discussed the formalisms provide complementary perspectives on dynamics
did we mention that they're different but complementary the former deals with time dependent probability densities over states
the latter path integral considers time independent densities over paths the density over states at a
particular time is the time marginal of the density over trajectories these probabilities bayesian probabilities
bayesian statistics can be conveniently quantified in terms of their negative logarithms or potentials
leading to surprisal and action respectively so we'll explore the formalisms more but just to note that the fancy i the
fracture i is the joint distribution and it is going to be a negative log on the joint distribution p and then similarly a the action
is going to be on those same variables in a slightly different way being looking like a surprise
conditioned upon x sub zero the starting conditions and we're going to go into more detail in the coming
weeks any more comments on section two or we'll continue to three
no i yeah that's awesome section three solutions steady states and non-equilibrium
so far so sections one and two we have equations that describe the relationship between the dynamics of
a system and probability densities over fluctuations states and their paths this is sufficient to elaborate
most physics big if true here's where the for example we could use the fokker plank or the path integral
formalism so either side of that dialectic to derive quantum mechanics where the fokker plank becomes the
schrodinger wave equation mechanics one quantum we could focus on systems that comprise statistical
ensembles of similar states to derive stochastic and statistical mechanics in terms of fluctuation
theorems statistical mechanics mechanics number two finally we could consider large systems in which the
fluctuations are averaged away to derive classical mechanics such as electromagnetism and dot dot dot
general relativity classical mechanics mechanics mechanics number three all of these mechanics quantum
statistical classical acquire boundary conditions to give the examples the schrodinger potential in quantum mechanics
the heat bath or reservoir in statistical mechanics and the classical potential for lagrangian
classical mechanics at this point the fvp steps back i wonder what space it's in and asks where do these boundary conditions come from
indeed this was implicit in schrodinger's question in the famous article what is life 1944 where schrodinger wrote how can the events in space and time
which take place within the spatial boundary of a living organism be accounted for by physics and chemistry
and this is a bit of a um nod slash reference to the paper of ramsted et al in 2018 answering schrodinger's question a free energy
formulation formulation so this was a really impactful and relevant paper that started
a discussion around the fep and multi-scale fep and self-organizing complex biological systems and so on
so anything to add about these mechanics and their similarities and differences
mark off blankets i'll just leave it there
uh in formalism six
we're gonna go into it hopefully in the discussions but just um in live stream number 32
on stochastic chaos and markov blankets
just to show where these similar equations were
um represented we talked about how the helm holds decomposition could be used to take a field
and decompose it into multiple sections there's the divergence term which is like um or the gradient
term which is like you're on some landscape and the ruler that's the most angled just going straight up
the hill that's like the divergence term and that might be useful for going up or down a hill as fast
as possible then there's this solenoidal or curl flow term and that is like an iso contour
and those two are part of the classical holmholtz decomposition and then there's this capital lambda
which is the housekeeping term as it was referred to in 32 and we explored it a bit but it reflects the
way that that landscape is also influenced by movement so we wondered if that was like kind of like
walking around on a trampoline where you can't just snapshot the um topographical map and then do your
navigation on the fixed map but there's some change there um we'll come back to that later so that's
section three on solutions steady states and non-equilibrium now we're going to really get to mark off blankets
particles partitions and things in section four all right so what do you see in figure one
yeah i mean see uh these two inner red and green conditioned on each other that um
um keep these external and internal states on the outside separate um they still have conditional um
relationship between like the sensory states the external states and the active states the internal states but
not directly with each other right so awesome um so they wrote in the caption it's an influence diagram
i believe it's also apparently to say it's a base graph but we're thinking of the arrows as influence and the nodes like the circles as variables
the particles it's a particular partition of states particular is a pun because it's it's one specific
partitioning it's not the only partitioning but it's a particular one that we're sharing with you
and it's partitioning that into a particle into something that's like distinguishing figure from ground
and the four states that get partitioned are internal states and external states
that are separated by a markov blanket comprised of the sensory and active states
there's a lot that could be said and we're going to continue to explore but just to give a few more notes
the partitioning entails that all of these states come into existence in a model specific way at the same time
so it's not like there's some feature of the world that just is fundamentally an internal state
it's the relationship between an internal and external state conditioned on a blanket by which all of those
assignments can be made it's like an incomplete sentence to have one referenced without the other
also we have the names of the states mu for internal and eta for external and it's kind of like they almost
look like flips of each other then s for sensory states incoming info a for action active states outgoing actions
so we have eta external s sensory a active and mu internal states and then there's a few couples of states
sets of states that we are going to care about and the equations that describe them have super different
implications so one set of states that's interesting to compare together is the blanket states b is the set of s and a
and that's more aligned with the pearl 1988 formulation of the markov blanket or boundary where it was an undirected blanket
and friston and others have developed this notion of like a two-way partitioning so the blanket is the set of both s and a
the particular states pi not to be confused with pi the policy selection in the pomdp
the particular states are b and mu so the blanket and mu so the particular states are internal active and sensory
everything except for external so the particle is like the cell the boundary and the internal generative model
and then there's the autonomous states alpha which is just a and mu and one way to think about those states are like
if you were to design the system those are the states that you can control you can't directly control the sensory input
which is the only thing that differentiates the autonomous from the particular states
you can't directly control what photons hit the retina but you could control your interpretation
and your action for where your eyes move which might absolutely influence which photons do hit the retina
but the autonomous states are the ones that there's a degree of agency over in a way that is slightly
different from just the consideration of the blankets and the internal states
let's continue to talk about some of the formalism
the conditional independencies which are going to be
uh let's pull back one more in associating some of these equations of motion with a unique non-equilibrium
steady state or ness density we have a somewhat special setup in which the influences entailed by the
equations of motions place constraints on the conditional independencies of the ness density
these conditional independencies can be used to identify a particular partition of states
the external sensory active and internal states as shown in the figure this is an important move
in what space because it separates the states of a particle internal states and their sensory and active states
the particular states from the remaining i.e external states to do this we have to establish how the causal dynamics in one
underwrite conditional independencies this can be done simply by using the curvature or second derivative of
surprisal as follows so how is the second derivative of surprise related to causal sparse dynamics
in your own words what is the formal description of a markov blanket what's this sort of minimal
markov blanket this is a slide from live stream 26 on bayesian mechanics this is like an undirected blanket
we don't have s and a separated just b intermediating and partitioning making mu and etza conditionally independent
and what about the fristen blankets type with sense and action separated what about nested markov blankets and so on and so on
we don't have a problem but just to look at seven we basically have x u and v x sub u and x sub v
are conditionally independent conditioned upon b the blanket dot dot dot dot fancy i surprise
d squared of surprise partial derivative second derivative of surprise dot dot dot dot equals zero
what does it mean how is the second derivative of surprise related to causal dynamics and the
partitioning
but continuing with the sparse coupling notion sparse coupling means that any two states are
conditionally independent if one state does not influence the other tautology number five this is
an important observation namely that sparse coupling implies the non-equilibrium steady state density
with conditional independencies in turn this means any dynamical influence graph with absent or
directed edges admits a markov blanket so if your variables are all connected to each other it's a
fully connected social network it's a fully connected statistical model then i guess you could argue it has a
blanket with respect to some other things that you didn't model or you could get into that whole
question but within that model there are no blanket partitions to make if there are any absent edges
then there are some states which upon knowing them make some other states conditionally independent
they give some more technical details and then they raise a question in the footnote why does the
particular partition comprise four sets of states we'll talk about that in dot one
continuing on sparse coupling and formalism 9 we can define sparse coupling as the solution to this
equation in which all the terms are identically zero so what terms are zero what is the reading of this
equation meaning under what situations are they zero are they being measured and said to be estimated at zero
are they being dictated to be zero so what terms are zero what does that mean in nine sparse coupling
means the jacobian coupling states u and v is zero so on either side of the blanket is zero
i.e there's an absence of direct coupling from one of those to the other this definition precludes solenoidal
coupling with u that depends on v because h and gamma are positive definite sparse coupling requires
associated elements of the solenoidal operator and the hessian to vanish at every point in state space
which in turn implies conditional independence so what is being shown here but just to give one more
visual way of looking at it this was figure eight from live stream 32 and um we had basically uh six
six variables that were in two clusters of three and they were like two communicating entities and so they
were being coupled by this like one to four connection and so up here on the top left there's strong coupling
within nodes one two and three and then there's strong coupling within this click of four five and six
and then there was a sparse coupling between the systems with a one four and there was also somewhat
of a sparse coupling within the click because they're not all block squares so we'll return to this and
it's again on the theme of how is sparse coupling related to the particular partition and a bayesian mechanics
for particular systems they give some more formalisms in 11 about blankets and couplings and flow
we'll go into it later
and 13 is very informative the normal form means that particular partitions can be defined in terms of
sparse couplings perhaps the simplest definition that guarantees a markov blanket is as follows
as well as external states external states only influence sensory states and internal states only
influence active states this means that sensory states are not influenced by internal states
and active states are not influenced by external states
here's formalism 13 so recall eta external s sensory a active mu internal
so f is the flow and omega is going to be the noise and the subscript in something is here like
tagging it to be about that variable so we have the rates of change through time
here's like a vector or a tuple this vector is describing the four states
and it's how external sense action and internal states are changing function of time this just like formula one
is going to be unpacked where we have x dot of t equals flow plus noise here we're doing like four of those in
parallel and so it's like external states changing through time is a flow on external states
so sense and external states as a function of external sense and action plus the noise of external states is a function of external sense and action states
action states plus accompanied noise terms
whereas action and internal states are functions of sense action and internal states and so it's like
external and sensory states are not being caused by internal states that's the only missing guy here mu
it looks like nsa it looks like nsa it's not it's eta s a conversely the autonomous states the ones that we have more agency over
the odd one out the missing you know the dog that's not barking is eta so these autonomous states
are flows on sense action blankets and internal states so the bottom two rows are the autonomous states and those are defined as flows of particular states
functions of flows that are using the particular variables whereas
the external and external and external states are driven by external facing variables
how would you read that under the sparse coupling it's simple to show that paths show that not only are internal and external states conditionally independent
but their paths are conditionally independent given that path integral formulation okay any thoughts on these last few
um
yeah again i just feel like whether the math is landing for people and this um you know separation of the internal states
and the being the the internal flows being conditioned on the sorry the autonomous states right like um
um it's also it's just partially like tautological or just just makes sense in the simple the way the model is presented
um
a couple slides back i'm not sure if i guess this is the right spot to bring it up but um
i think a question that i have frequently about this is like where do they come from where do things
come from well they come from you know the separation and conditioning of you know particular from the
background and the blanket forming out of blankets form etc or where is what's the difference between the
internal state the external state the external like you said if there's you know this giant social graph
it's all everything's connected they're all connected then then there's no markov blankets um
just like two cells in the body how do they know
they know that they're not um
you know they both have their own markov blankets and yet they are both like external states that are
indistinguishable from kind of the rest of stuff to themselves right for each of them right um
um like over time that you know dissipates right and so yeah i just i guess i wonder like the over time
um dot notation here like how that um the dynamics of
how something becomes an internal state or an external state how that exactly happens because
you know it just seems like when you look at a lot of examples on you know our entropic physics you know
um anthropic like um state where we're right like everything is good for us um and everything we can
observe right it's it's like galaxies or something oh they're so far away they don't you know there's a
lot of intergalactic you know in space that's not affecting it's very external you rewind it a few
billion years like lots of interaction lots of markov blankets so it's like um yeah like
where does that begin and end yeah oh markov where art they sting yeah um formalism 14 and 15 are
further details on the entropy of internal and external paths and the conditional independencies of paths
that's going to conclude section four particles partitions and things which was about the markov
blanket partitioning of particles particular states and so on we'll move pretty quickly through the
following sections section five from self-organization to self-evidencing equipped with a particular partition
we can now talk about things in terms of their internal states and markov boundary namely autonomous states
and we can talk about particles particular states the next step is to characterize the flow of the
autonomous states in relation to external states in other words considering the nature of the coupling between
the outside and inside of the particle across its markov blanket it is at this point that we move towards
a bayesian mechanics that is the special provenance of systems with particular partitions
the existence of a particular partition means that given sensory states one can define the conditional
density over external states as being parameterized by the most likely internal state and we had several
discussions in live stream 26 on bayesian mechanics with lance d'acosta this is where variational
inference is going to come into play we will call this a variational density parameterized by the internal mode
q the distribution we control of internal states mu about external states eta is defined as p of external states
conditioned on sense
equation 16 means that for every sensory state there's a conditional density over external states
and a corresponding internal mode with the smallest surprisal this mode specifies the variational density
where by definition the kl divergence between the variational density and the conditional density over
external states is zero more formalisms more details inducing the variational density is an important move
it means that for every sensory state there's a corresponding active mode and an internal mode
this mode does not mean style here mode means like the most common value in a statistical distribution
the active and internal modes the active and internal modes constitute active and internal manifolds
we will see later that these manifolds play the role of center manifolds namely manifolds that contain paths
that do not diverge or converge exponentially the operative exponents the internal manifold is also a statistical manifold
because it is equipped with a metric and implicit information geometry
this is because movement on the internal statistical manifold changes the variational density
this is moving towards that dual information geometry perspective
what is equation 17 showing we're looking at the flows
the expectation of the fluctuation term the expectation of the fluctuations is zero
so we're able to drop those omegas with a subscript that we saw in 13.
so now we're going to be looking at the flows on different states as for the top two the external and the sense states
those are going to be about surprise fracture i fancy i for action
and internal states the autonomous states
that is free energy
minimizing surprise about external and sensory states minimizing free energy about autonomous states
what is that f the free energy in question is an upper bound on the surprisal of particular states
so in variational bayesian methods elbow and free energy are used to bound
the surprisal here we're bounding surprisal on a particular partitioning including action
to model the action perception loop so we've seen variational free energy several times
what do these different rearrangements mean what other rearrangements or restatements of f are possible
we've known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be known to be
My question is in relation to action and energy and the way this is being stated.
Like, what?
Yeah, what is the action version of this?
What is the easy to miss, like, oh, it's just energy thing that is...
in the way of, like, framing this here?
These are not the same thing, right?
Like, so, yeah, that's my question is just differentiating that or better defining which parts are action,
which parts are the energy components of that.
That's what I would, like, be interested in rearranging or thinking about, yeah, these equations.
Cool.
They write in footnote 19, is variational free energy the same kind of free energy found in thermodynamics,
like Gibbs free energy, perhaps?
The answer is no.
This entropy is distinct from the thermodynamic entropy of internal states.
We're going to return to this.
We're going to have...
Are we talking about thermal free energy?
Or are we seeing equations that look like descriptors of thermal entropy, but we're applying them in an informational setting?
We'll return to it.
We'll return to it.
As they had brought up before, one can formulate this along the lines of a center manifold theorem,
where we have a fast flow towards the center manifold and a slow flow on the manifold.
Going fast towards the valley ravine and then going slow on the river.
This decomposition can be derived simply using a Taylor expansion, Taylor series expansion, around the time-varying autonomous mode.
So here is a Taylor series expansion.
It's evaluating a function at a given point, usually zero, and then taking its first derivative, and then taking its second derivative,
using higher and higher derivatives to approximate increasing distances from the reference single point where that function was actually evaluated.
So how is the Taylor series expansion or other power series expansions related to time-varying autonomous modes?
What about that flow on the center manifold?
We know from 17 that the flow of autonomous mode can be expressed in terms of free energy gradients.
Those are the two Fs on the autonomous.
So this expression 20 unpacks the manifold flow in terms of accuracy and complexity parts of free energy,
where the accuracy part depends on the sensory states,
and the complexity part is a function of and only of autonomous states.
The manifold will look as if it is trying to maximize the accuracy of its predictions while complying with prior Bayesian beliefs.
Bayesian statistics.
These are all Bayesian variables.
Here, predictions are read as expected sensory states under posterior Bayesian beliefs about their causes,
namely variational density over external states.
The real temperature out there in the room, hidden unobserved external state.
Thermometer reading, sensory state.
And then states some sort of cognitive mirror or representation as modeled of temperature
that's conditioned upon the thermometer reading.
But there's some generalized synchrony across that thermometer blanket.
In footnote 21, they write,
Question, do particles minimize surprisal or free energy?
And we'll go into it because they say,
Minimization implies a teleology that goes beyond any claim of the FEP.
Whence teleology.
I thought we were like talking about teleology earlier.
So how deep in the desert are we?
What level of mirage are we engaging in?
But we'll get there.
And that takes us to figure two,
which is going to show two components of autonomous flow conditioned upon sensory states.
So I'll move us away.
We can talk more about the technical details, like how it relies on the Taylor expansion.
But here are the autonomous states
And the black line potentially can be read as like that manifold attractor.
And so there's a movement towards,
directly towards the attractor.
And then there's a movement that is perhaps orthogonalized,
keeping in mind the difference between the gradient and the solenoidal flow.
And together through time.
So this is not just like a hill.
Previously, like in 26, we saw like the hill and the particle makes its way to the top of the hill
as a function of gradient ascent and solenoidal coupling flow.
Here, we're not just ascending a hill.
Like we're tracking this moving point through time.
But we're converging in this spiral way.
And then we can maybe unpack that in relationship to manifold flow.
And how even if this black line is the manifold, then how is the entity staying on the manifold?
So we'll talk more about figure two.
Now they're going to summarize this section.
A particular partition of non-equilibrium steady state nest density implies autonomous
dynamics can be interpreted as performing inference particular kind.
It's not doing every kind.
It's doing a specific kind.
And it's a particle.
There's the fast flow towards the center manifold and the slow flow on the manifold.
The manifold flow can be interpreted as Bayesian belief updating.
And posterior Bayesian beliefs are encoded by points on the internal state's statistical manifold.
In other words, for every point on the statistical manifold, that synchronization manifold,
there's a corresponding variational density or Bayesian belief over external states.
These are internal states about external states conditioned on the particular partitioning.
And that can now be expressed as the variational principle of least action.
This is the basis of the FEP.
Put simply, but not too simply, I guess, it means that the internal states of a particular partition
can be cast as encoding conditional or posterior Bayesian beliefs about external states.
This licenses a poetic description of self-organization as self-evidencing.
We'll unpack it later.
Just wanted to mention it so we can continue.
In Figure 3, there are several different ways in which this self-evidencing is connected to various
theories.
For example, value, surprise, entropy, and model evidence.
And the schematic is illustrating how minimizing variational free energy
Wait, but I thought that minimization implies a teleology that goes beyond any claim of the FEP.
But minimizing variational free energy relates to normative theories of optimal behavior,
like value maximization, pragmatic reinforcement reward learning, Pavlov.
Surprise, novelty, infogain, infomax.
Why is the free energy principle here?
Isn't it like all of them?
Entropy and model evidence as well.
And then, just to conclude this section,
they ask,
Is it tenable to interpret gradient flows on variational free energy landscapes
as variational inference?
Or is this just teleological window dressing?
The next section addresses this question through the lens of Bayesian filtering.
In brief, we will see that autonomous paths of least action,
implied by a particular partition, are the paths of least action of a Bayesian filter.
This takes us beyond as-if arguments,
by establishing a formal connection between particular dynamics and variational inference.
So, to discuss, what are particular dynamics?
What is variational inference?
What is the relationship between particular dynamics and variational inference?
What would it mean for it to be as-if?
And what would it mean for it to be something different than as-if?
Okay.
Continuing on.
Lagrangian's generalized states and Bayesian filtering.
Now, say we wanted to emulate or simulate active inference.
What if that were the case?
We could find the stationary solution to the Fokker-Planck equation
and the accompanying Helmholtz decomposition.
We could then solve number 21, which is called paths of least action,
that characterize the expected behavior of this kind of particle.
However, there is a simpler way to recover the paths of least action,
by finding a path that minimizes Lagrangian at every point in time,
noting from 3 that the path integral of the Lagrangian is the action.
First, they're going to reintroduce generalized coordinates of motion.
So, we talked about that in number 26 as well,
but the generalized coordinates of motion are like the position, velocity,
acceleration, and higher and higher and higher derivatives of the coordinates of location.
So, it's taking like the xy coordinates and adding their first derivative,
and their second derivative, and their third derivative, and just having that in a vector.
So, that's what's shown here.
x through time, the derivative of x, x prime, is the flow, the second derivative,
the first derivative, and so on.
That's the integrator chains, PID control, and so on.
In the generalized coordinates of motion, state, velocity, acceleration, and so on,
are treated as separate generalized states that are coupled through the Jacobian.
So, if the first and the second are related to each other, and the second and the third,
and the third and the fourth, there's a sparse coupling in that vector.
This allows us to relax certain assumptions and gives a quadratic form.
We'll unpack this more. But there's a sparsity and a capacity to do modeling of movement in the
generalized coordinates of motion. Now, maybe three, maybe six are sufficient,
but this is like an infinite dimensional framework, but it may be the case that you
can go super far with just a few. Formalisms 23 and 24 describe that M can be read as a mass matrix.
That would be interesting to know what is meant there. And there's a suggestion that precise particles
with low amplitude random fluctuations behave like massive bodies. So, that's like the baseball on the
parabola. The air fluctuations and the thermal vibrations are not dominating its trajectory,
but the one molecule baseball, it is getting tossed and turned. In equation 25 and 26,
they continue describing using that Helmholtz decomposition, the divergence free flow, and the curl free flow
in terms of the gradient descent on a Lagrangian. That'll be helpful to learn what they mean.
And then, crucially, when that is minimized, the mode of the path becomes the path of the mode.
That would be something useful to understand what is meant. What's the difference between tracking the mean
and tracking the mode? For Gaussian distributions, like the Laplace approximation or any other second order
curvature, what does that mean? And then, just to close this section, the generalized free energy
is easy to evaluate, thankfully, given a generative model in the form of a state-space model.
Here it is. F, sense, action, and internal, is going to be decreasing some terms that we'll learn about.
And finally, one can simulate active inference by replacing the generalized flow of autonomous states
with a generalized Bayesian filter. So, here we have 27. Very similar, except notice that there's a lot more arrows
of the bottom two. And the bottom two, instead of 13, we now have these bottom two rows with the D on A
and the D on Mu. And some triangles have been introduced. We'll unpack more what that means.
Any thoughts or comments? Or we'll continue to 7.
No. Yeah. Awesome.
7. From statistical to classical particles. So far, we have a Bayesian mechanics that would be
apt to describe a particle or person with pullback attractor. But what is the difference between a
particle and a person? This speaks to distinct classes of things to which FEP could apply, molecular
versus biological. Versus? Here we associate biotic self-organization with precise and predictable
dynamics of large particles. So, as we described earlier, if we were talking about classical mechanics,
something bigger would be more resistant to, like, thermal fluctuation.
We could think about, like, that analogy to mass in the statistical setting. Where are the priors, like,
massive? And they're just on their own inertia, and they're not being buffeted by stochasticity.
Versus where is it a lightweight something that is getting buffeted?
So, here's going to be a distinction between statistical and classical mechanics in the setting of the
particular partition. It is often said that the FEP explains why biological systems resist the second
law, tendency towards disorder, and the natural tendency to dissipation in disorder. However,
this is disingenuous on two counts. So, is Friston 2013 disingenuous? Or is that paper combating the
disingenuity? First, the second law applies only to closed systems, while the free energy principle
describes open systems in which internal states are exposed to and exchange with external states through
blanket states. With lots to unpack there, what exactly is the exchange? Is it like an informational
exchange? Or are, like, nutrients crossing and becoming incorporated into the internal states?
And second, there is nothing so far to suggest that the entropy of particular states or of paths is small.
So, this is like the design language for particular states that might be totally buffeted by stochasticity,
or totally on the least action railroad, and everything in between. But nothing has been said to identify
one or the other, and so everything has high and low entropy densities. So, there's, you know,
two particles in two different rooms. One particle is equally traveling to all parts of the room,
the other particle is staying in one part of the room. So, one of them has a very ordered distribution
of space, and the other one has a very, like, disordered, you know, equilibrium gas flowing throughout the room.
Both of them are particles. So, what distinguishes between high and low entropy systems, e.g., between
candle flames and concierges, respectively?
28. We could have had a concierge.
And that is going to describe that, and we'll come back to it.
This suggests that precise particles, such as you and me,
respond to environmental flows and fluctuations in a precise and predictable fashion.
Well, I'm an unpredictable guy. Yes. In our regime of attention,
it is almost like tuned to some maximally confusing or uninformative things, or we could have some
cognitive experience of being confused, but someone's blood sugar through time has more predictability
than zero. So, it's on that continuum from totally buffeted to totally on the railroad tracks,
and it's more like the railroad tracks if you want to survive, or design high-reliability systems.
And then they're going to introduce figures four, five, and six.
Four is about the difference between generic and precise particles using an information diagram.
For precise particles, there's no uncertainty about autonomous states given sensory states.
Knowledge about action. Knowledge about internal states, like metacognition.
Is the behavior of precise particles sufficient for sentient behavior?
Perhaps. Figure five, the implicit computational architecture used in simulations of sentient
behavior. And six is reproducing an example from the academic literature with action and action
observation. So, figure four has to do with information gain and sharing
with generic and precise particles. Do you want to add anything? Otherwise,
we'll just take one look at each of four, five, and six. Okay. Figure five, Bayesian mechanics and
graphics summarizes belief updating implicit in gradient flows on variational free energy.
And six, sentient behavior and action observation.
So, this is like somebody involved in pointing or tracing or handwriting and also looking visually.
In summary, precise particles immersed in an imprecise world respond almost deterministically to external
fluctuations. Why might this behavior be characteristically biological?
Precise particles may be the kind of particles that show lifelike or biotic behavior.
So, let's think of those two particles in the two rooms. One of them, 24 hours a day, no matter what the
temperature is or what the light-dark cycle is, it's always equally covering all parts of the room.
The other particle, you find out that when it's light, it stays in this part of the room.
And then when it's dark, it stays in this other part of the room. Which one of those particles,
without knowing anything more, seems more biological? The one that's diffusing like a gas molecule?
Or the one that has this orderly distribution, especially one that's conditioned upon salient
external factors? So, the distinction between those imprecise and precise particles
particles, getting buffeted by thermal vibrations, or being like the classical, like the Kepler universe,
like the planets going around orbits totally unbuffeted by thermal vibrations,
rests on the relative contribution of dissipative and conservative flow to their path through state
space. One might associate precise particles with living systems with characteristic biorhythms,
and then they bring up many, many nested biorhythms from rapid oscillations that are multiple times per
second in neural systems, heartbeat, respiratory, circadian, seasonal life cycles, even pulling out to the
evolutionary angle. Turning this on its head, one can argue living systems are a certain kind of particle
that in virtue of being precise evince conservative dynamics, biorhythms, and time irreversibility.
So, wow, how are these all related to each other? Where does the time irreversibility connect?
And, their summary. The emerging picture is that biotic systems feature solenoidal flow in virtue of being
sufficiently large to average away random fluctuations when coarse-graining their dynamics.
And, figure 6 explores that more. Okay, final technical section 8. Path integrals, planning, and curious particles.
The previous section was focused on linking dynamics changes through time to densities over generalized states.
Internal states can be construed as parameterizing Bayesian beliefs about external states.
Internal states are about external states in this model. In what follows, we move from densities over states to densities over paths,
to characterize the behavior of particles in terms of their trajectories. So, Formalism 29.
We're interested in characterizing autonomous responses to initial particular states. Autonomous,
the action, and internal states. The ones that we control. Recall that when random fluctuations on the motion of particular states vanish,
there's no uncertainty about autonomous paths, given external and sensory paths, knowing exactly what to do and exactly what to think.
And there's no uncertainty about sensory paths, knowing exactly what senses will be observed,
given the external world and the autonomous paths, which is what one does and thinks.
If we interpret entropy as the limiting density of discrete points, figure 4, then the uncertainty about particular
autonomous and sensory paths, given external paths, become interchangeable.
Formalism 30. Formalism 31. Expected free energy.
Formalism 31. Expected free energy.
The autonomous path with the least expected free energy is the most likely path taken by the autonomous states.
Expected free energy.
How can we read it? What does it mean?
Why does it matter that we're focusing on autonomous states? Autonomous paths.
And how is it similar or different from other representations that we've seen and that we will see
expected free energy and free energy of the expected future and so on?
Expected free energy.
Where it can be regarded as a fairly universal objective function for selecting paths of least action.
Planning. Planning as Bayesian inference.
Equation 33. Expected free energy.
Expected action. Bayesian optimal decisions.
Utility. Pragmatic value.
Expectations of information gain.
Optimal info gain. Bayes optimal experimental design.
Optimal hypothesizing.
So not just falsification. Not to beat a dead horse.
But rather than constraining and then executing,
keeping this infinite game optimal design perspective open so that we can always be tier
of the balance between optimal decision making and optimal experimenting.
When simulating with active inference and planning afforded by path integral formulation, one usually works with discrete state spaces and belief updating over discrete epochs of time.
That's where the partially observable Markov decision process, POMDP, comes into play.
And plausible policies can then be scored, evaluated, based upon their expected free energy.
And the next action is selected from the most likely policy.
Policies are sequences of actions that can be taken.
In summary, we now have, at hand, a way of identifying the most likely autonomous trajectory from any initial particular state that can be used to simulate sentient behavior of precise particles that we have associated with biotic systems.
Expected free energy absorbs two aspects of Bayes' optimality into the same objective functional, which is a function with functions.
In other words, the information gain is optimal Bayesian design.
Bayesian decision theory is minimizing the cost function under a decision or choice and uncertainty.
As with the interpretation of variational free energy, this dual aspect functionality of expected free energy is an interpretation of a single existential imperative to possess a Markov blanket and implicit thingness.
In other words, teleologically, it's worth reflecting upon the differences between the generative models that underwrite variational and expected free energy.
For VFE, the generative model is a joint density over external and particular states supplied by or supplying the non-equilibrium steady state density.
For the path integral formulation, the generative model is a joint distribution over paths.
For the path integral part of the generative model is a joint density over the path.
Because consequences, the generative model acquires a temporal depth.
They then have several figures that continue on this theme.
Figure 7 is related to a DaCosta 2020 discrete state space synthesis paper
showing special cases of variational and expected free energy.
Like when there's no preference, there's optimal information gain.
When there's no ambiguity, you get pure risk-sensitive policy.
When there's no intrinsic value, you get expected utility theory.
And when there's no ambiguity or preferences, some recent work by Ramsted et al. have started to soft reboot the FEP and connect the principle,
which we're going to be looking forward to learning more about.
Figure 8 is about Bayesian mechanics and active inference.
Figure 8 is a simulation in which I-caccades are occurring.
And we can explore this more.
To the conclusion.
There are many points of contact between what we described and other theories.
Please, read the papes.
Discuss special cases.
They discuss the mechanics of synchronization, separation of time scale, and applications.
And then, in closing, they write about how
the developments are speaking to the shift in focus from the foundational issues addressed in this article to their applications,
learning and applying active inference and FEP.
It is quite possible that the foundational aspects of the free energy principle may also shift as simpler interpretations and perspectives reveal themselves.
That brings us to the end of the dot zero.
So, Brock, what would you like to add or say?
I would like to add that for the next dot zero, I will be preparing my answer to this part first.
I had a ton.
I don't know.
Just writing down a few things and thinking about
intractability and uncertainty and
possible kind of informational
information entropy kind of
questions that you could ask around that.
like what makes those kind of ultimate Markov blankets of intractability.
Like how action intensive is it
for information to cross?
Or for
external, for the external states to influence the
indirectly influence the internal states, right?

And another question.
How hard do you have to push on the blanket?
What kind of push and what?
So, yes, they're conditionally independent, but also they do influence each other.
The blanket.
So how hard you have to push?
Yeah.
And it just, it seems like, I guess what I'm saying is that
the scale
which we kind of, you're using the particle people and the baseball
analogy, right?
And we talked about that
yesterday or the day about like
just a large, you know, matrix, large space
of states of variables of, you know,
um, dimensions of, of what you mean by a Markov blanket in a particular,
you know, and the scale of that Markov blanket to the environment, right?
Um, having like a big
seeming to have a, like a big impact on
how hard you have to push there, right?
Um, the baseball's flying through the air, but the
particle is spreading out and, you know, being pushed around.
And yeah.
And I was like, are we
little molecules
trying to push the baseball or are we
the designated hitter who's way overpowered and able to put it wherever we want?
Or are we just doing the tiniest buffeting?
Maybe this is a design language that helps us frame both of those settings and recognize when
are we able to be guiding the path of least action and where might, no matter how hard we yell,
maybe we're not influencing it, like literally at all.
Or staccat, we're influencing it like stochat, like stochastically. It's not,
we can't kind of concentrate our action into one,
you know, path, right?
Um, one path, like, so
yeah, there's, I don't know, there's a lot of, um,
wonderings and questions that are like not, uh,
probably very well informed to just
read the papes on and continue reducing uncertainty.
Um, yeah.
Awesome work with this dot zero and thanks a ton for being a part of it.
Thanks everybody for watching and all the great comments in the chat.
And we'll see you in the dot one and in the dot two.
Bye.
Awesome.
Thanks again.
See ya.
Bye.
