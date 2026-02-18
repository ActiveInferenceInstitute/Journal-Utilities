---
title: "ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary"
category: "ModelStream"
series: "ModelStream_008"
episode: "1"
speakers:
  - "Tom Ringstrom ~ Reward is Not Necessary"
duration: "1:48:59"
url: "https://www.youtube.com/watch?v=Fh1e4sKh3Vs"
views: 768
exported_at: "2026-02-18T22:37:37.737909+00:00"
format: markdown
---

# ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary

Hello and welcome. It's January 26, 2023. We're here in Active Inference Model Stream
number 8.1. Today, we're appreciative to have Thomas Ringstrom, who will be presenting on
Reward is Not Necessary, a compositional theory of self-preserving agents with empowerment gain
maximization. There will be a presentation followed by a discussion. So, Thomas, thank you
for joining. Really looking forward to this. Off to you.
Yeah, thank you very much. It's really nice to be here and talk to this group.
I'm a computer science PhD student at the University of Minnesota. My interests are in
sort of what are the computational properties that we would need to have agents which flexibly plan
in sort of high-dimensional product spaces of variables. And also, how do we get agents to
perform complex tasks in an intrinsically motivated way, especially in high-dimensional product spaces?
So, this presentation is going to argue that reward, and I know I'm talking to a sort of active
inference crowd, but some of the same points apply to active inference perhaps too. But
this presentation is mostly about how there's going to be some major problems, I think,
using reward maximization objectives. And by moving to sort of reward-free objective functions,
we can get really nice factorizations that help us plan. So, let's just start off with a sort of simple
picture, a simplified picture of an organism. So, we have a honey badger here. And so, this honey badger
has internal states. It gets hungry and it gets thirsty. And there's also an external world
that the agent lives in. And, you know, in order to sort of modify internal state spaces, the agent might
have to perform some complex tasks. It might have to get several items in order to, you know, eat an apple
or things like that. So, you could see that maybe some symbolic state space sort of mediates the connection
between things you do in the world and transformations that you make on some internal state space.
And, of course, real, you know, real world organisms and humans live in a high dimensional world. So, you
could imagine that there's an encoder and a decoder. And really, you know, there's a sort of high
dimensional physiological or interoceptive domain that is these sort of Y tilde with the dot, or Y tilde,
I should say, and Z tilde. And then there's, you know, a high dimensional world. You could just say that
the that's X tilde. And really, you just need to sort of map these down to some discrete state space
in which these domains can interact. So, yeah, here's like a simple encoder and decoder. And,
and so if, if an agent has a kind of simple ontology like this, you can imagine that it's sort of
generatively entrained to the world that it lives in, which is a notion that's probably pretty familiar to
sort of active inference people. So, you know, you have some encoder of these high dimensional states,
and then you have some operator PS, which is in the middle of the head here, and that just sort of
advances the latent states, and then you decode, and you'll get sort of expectations of, of the
high dimensional world that the agent lives in.
John P. And so the problem is, is that you can't really represent explicitly these latent space
transition operators that would dictate, you know, the dynamics of, of all these variables. You can't
represent it as an explicit object because the more state spaces that you keep track of in the world,
the larger this object PS becomes. So in order to handle this, you'd have to represent it in a sort of
factorized form. So you just would represent its factors, and you wouldn't explicitly sort of enumerate
all of the state vector transitions under, under this transition operator. And so what we really need to
think about is, you know, what are the sort of model based, or the sort of Bellman principles for
decomposing hierarchical state spaces, so that we can create the right representations that help us plan
in a flexible way, in a sort of time, time varying time dependent world of lots of lots of variables. So
this just means, you know, what is a sort of objective function L, calligraphic L applied to PS, or
its factorization that would give us, that would give us some factors here, eta and, and these omegas,
that could help us plan. And also, how, you know, given the fact that, you know, the state space,
the effect of product space that we're working in is so large, and there's many possible state
vectors that describe possible states of the world, how do you know what to do? I mean, if you're an
RL theorist, you would have to say, well, there exists some kind of reward function that tells you,
you know, this state of the world is worth this much reward, and the state of the world is worth this
much reward, but it's not really clear how you should define reward functions on huge product
spaces. So I will address this question from sort of reward free perspective. And the just to give you
a hint of what it's going to be like, what I'm going to argue is that what we really need are agents
that have a kind of structured core ontology that it needs to maintain, that is, coupled state spaces
that really depend on each other, in which the policies that you use maintain the sort of internal
integrity or controllability of the agent. So, and that's where empowerment will eventually come in.
So I'll talk about empowerment a little too. That's the controllability metric. So here, I'm just saying
what's a nice policy, or what's an objective function, F, that takes in some intrinsic motivation
function, which is this fancy V here, along with a nice factorization that allows you to plan in the
world. Okay, so just to recap things that I already said, we're in a product space of
state variables. We have internal and external state spaces, you know, hunger and hydration state
spaces can be dynamic as you do things in the world, you get hungrier. So how do we plan? How do we know
what a good goal is? And what I'm going to argue is that we should compute a specific representation
called a state time feasibility function, which is going to be an abstraction that's going to map us
from initial state times to final state times. And this will have some really nice properties that
allow us to sort of reason in this high dimensional state space. And I'm going to talk about this from
a just a dynamic programming point of view, there's there isn't going to be any learning.
Okay, so let's just talk about transition operator composition, because I said, well, we have this
large product space of state variables, and it'd be nice if we just represented it as a factorization.
So what does that mean? So imagine that you have Px, which is like a base state space to move around the
world. And you have some internal state space or secondary state space Py. And these are linked
by some function f. So here's your base state space. And here's the honey badger in the state space.
And here's the secondary state space, which is just like a, you know, your internal hunger space.
And so f, what f is going to be is called an availability function. And the availability function
is going to say, oh, this, you know, this honey badger is in state x, a, t,
and at time t. And given that it's there, what's the probability that this goal is available from this
state time state action time. And so this goal is formally going to be an action on the higher level
state space. So for instance, these green lines on the high level state space are going to map you to,
you know, the most satiate, satiated state, where you're not hungry anymore at all. And then these black lines
on the on the internal state space are just going to decrement you, you know, one state, if you're, if you're
not at the tree, so you eat apples at the tree, and that's going to map you to the top, and all other states
without a tree, you're going to get hungrier over time. Okay, so if we wanted to write a product space
operator, you know, PS, you know, y prime x prime, we can just represent this as a composition, where
lambda p is our composition operator, and it's just going to be defined as the product of your two
state spaces with f linking them, and then we sum over g. So we're getting rid of the goal variable.
And so we can represent the, the product space this way. And we can also just call the product space,
we can say that s bold s here is just the state vector for, you know, y x, or if we have more
variables that can be incorporated into bold s. Okay, so what if we have more features of the world,
we can drink water, we can get warm at the house, well, we will need to have a bigger composition.
So we can just create an operator called we'll just call PR, where bold r is just a state vector of w y
and z, and w y and z correspond to the hydration, the hunger and the temperature space. And so this is
just a product of the individual ones, the individual operators. And so this influence graph is connecting
p x to p w, p y and p z through f. And so we can just define the product space operators, a composition
this way. And if we do that, you know, you start to realize, well, this is nice, because the effective
state space, you know, exponentiate essentially, you know, as you add on more state spaces that you can
control. And so this influence graph is just showing, you know, you know, what is the sort of ontology of
the agent? What is what what constitutes it as its internal and external coupling? And you could imagine
that it gets more complicated, for instance, that if you hit, you know, w zero, or y y zero, or whatever,
that you, these skull and crossbones indicates that you die. So you can imagine being in a state
has a bi directional influence. So zeta here is, is conditioning the possible dynamics p x can produce.
So you could imagine that, you know, once you're in one of those sort of defective bad states that it
kills you, and you can't move around. So you can imagine, you know, sort of more complicated
structures like this, which essentially mean that you have to go out in the world and do things in
order to keep the system alive. So you don't want to hit w, you know, w w naught or z naught.
And you can imagine this gets even more complicated, you could compose sort of larger structures,
where p sigma is going to be some logical state space that keeps track of, you know, multiple
conditional events that need to occur to for say, you know, say, eat an apple or something like that.
So representing it in this form is very nice, we just represent the factors and the links between the
state spaces. And that's a sort of energy, a sort of memory efficient way of representing the space.
Okay, so if we have a homeostatic task, I'll eventually get to the sort of Bellman equations and
the model based form form formulas. But first, I'm just going to sort of build up an intuition in the
form of an example about how these state time feasibility functions are going to work. The
state time feasibility function being the representation that I'm arguing for in this talk.
So if we have a hiker, and it can go into the world and drink and eat and get warm,
the same as the goal variable. So if we have a goal variable, G epsilon, which is going to decrement by one
state. Then as the hiker moves around, you can represent this as a function. So imagine that the hiker
hiker starts at x g one, that's the house, and t s, which is the start time. And if the hiker follows a policy,
pi two. So imagine that you have a policy that is a goal, like a goal condition policy, pi g two,
that's going to take you to x g two. Okay, so it's a policy, it's like a shortest path policy or whatever.
And then that means that there's going to be some final state time x g two, t f, that you achieve this
goal, g drink, which remember is an action on the higher level space. So what this would look like is
that you decrement two, right, because that takes two time steps to get to the lake. And then once you get to
the lake, you take the state action that's going to drink, and it's going to bring you up. So there's
there's three total steps in this process of inducing the drink goal variable, and then the step after
drinking, which would look like this. And then you can imagine, well, the other state spaces
are not involved. And so they will all decrement three, because there's three time steps.
And so one way to represent this is, is to realize that if all of these goal variables, sort of
goal variables on the way to the, to the lake, are sort of the null goal variables, meaning that the
agent isn't affecting some other state space, then you can define that as a Markov chain. So if you set,
you know, all of the goals to be the epsilon goal, the null goal, then this py epsilon is going to be
a Markov chain matrix. And so that means that the time difference encoded in the state time feasibility
function, the TF minus TS is going to be the power that you can take this Markov chain to, in order to
forward evolve the, this, the internal state space, all the other internal state spaces. So you can define
a, an operator that does this in one step called Omega Y, which is just going to take some initial
state. So this green dot, or this red dot. Um, and it's going to take the time difference. So this is going
to be two to get from the house to the lake. It's two time steps. And so these, uh, gray arcs are just a,
an initial to final state map under this policy.
And so what this looks like, this is sort of looks sort of complicated, but you can build a jump
operator that jumps you from your initial high dimensional state, uh, for instance, Y X T.
And we're just considering Y for now. I don't have the other state spaces, uh, W and Z in here, but, uh,
this ADA over here is, is mapping you on the X space. The Omega Y is mapping you forward two in,
in the, uh, in the Y space. And then the P Y and the P X are just evolving by one step,
um, to update after you hit the goal. So after you hit the goal, you have to update by one step. So,
uh, P Y and P X do that for both state spaces. And then of course you can do this for all of the
state spaces. So a jump operator for all of the internal state spaces are where R is, you know,
remembers the vector of all your internal states, W Y and Z. Then this is similarly defined where,
um, Omega, Omega R is just the product of all of these other Omegas. So we defined Omega Y up here,
but you can just define this for all of your other state spaces.
So now that we've done that, we can, uh, continue our journey by going to the tree.
And so that's two steps away. So all of the other things decrement two and then an additional one.
And then if we go back to the house, that's four times steps away, plus the, the additional time step
of, uh, entering the housing and getting warm. Okay. So here is another route you could take,
uh, where the, uh, agent, uh, the hiker goes to the tree to eat. And then the hiker goes to the lake to drink
and then goes back to the house to get warm. And so this, this JS is a huge, it's important to keep
in mind that JS is a huge operator and we cannot, uh, explicitly form it in memory, uh, because it's,
unless we have, you know, a lot of memory on our computer. Um, but having this factorization allows
us to chain policies together and evolve a high dimensional state factor in these jumps. So we're,
we're, we're jumping a state factor around in this object oriented fashion where each state vector
is updated once you get to some key object of interest, such as the tree with the apple or the
lake with the water. So, um, also in this, uh, example, you can see that it, the, the agent went from the
lake to the house and, um, technically if Z it, it occupies the lowest state Z zero. And so technically it
should die, uh, at the skull and crossbones on the map, but we let it finish, uh, his journey. And we
haven't talked about this sort of bi-directional coupling yet, but we'll, we'll do that in the next
slide to, um, to make that concrete. All right. So if we have these defective states, we can define,
mode parameters E plus and E minus, which, um, are just going to be variables that condition our dynamics
and we can have a mode function that takes any vector R, uh, and so an R is any vector of blue,
green, and red squares in the space, and we can map it to a mode parameter. So we can define, uh, Zeta
to map to the good mode, the, the normal healthy mode. Um, if it's not occupying any of the defective
states, but if one, one or more, um, you know, defective states are occupied, then we can map it to
E minus. And so that means if we have some, you know, low level transition operator that's indexed by E,
that means we can split it into a normal dynamics P E plus and a defective dynamics P E minus. And you
just know, notice that the defective dynamics is this sort of identity operation. It just sort of
arrests your dynamics in the space so you can't move around, but the normal dynamics is just normal grid
world, uh, movement. Okay. And so what we can do is we can compute a set of individual feasibility
functions for each object of interest in the map. So in, in the previous example, we had, you know,
two trees, two lakes and a house. So we have five state time feasibility functions.
And then this eta hat is an aggregate function of, of all of these, uh, functions where the pi
is indexing the corresponding pi for that function. Uh, anyone can ask questions, by the way, if they have
any questions.
All right.
All right. So the full dynamics is going to be just defined like we defined it before where we, um,
we have, uh, these two state spaces, the base state space coupled to the internal state space through F,
but then we have the Zeta, uh, R here, uh, on the conditioning side. And so this is a sort of, uh,
a, uh, uh, an operator that you sort of have to, uh, you have to achieve goals in order to keep yourself
out of, uh, these sort of absorbing defective states.
And this is, and I showed this, um, influence diagram before, but this influence diagram,
uh, is capturing, uh, this coupling.
Okay. So, um, many of you will probably be familiar with the standard Bellman equations,
um, where, which are, you know, form it formalized this way where you have some reward function,
um, plus some discounted expectation of your future value. And so the value function in a sort of
standard Bellman equation says, how much reward am I going to get if I act, um, here optimally,
over an infinite horizon. And so the reward function is thought often thought to be a task.
It has that sort of semantics in, in RL, uh, land. Um, and then the optimal policy is just
going to return the action, uh, that corresponds to the best action that maximizes your value,
your long run, sum of rewards that you're going to get. So this is, um, a recursive equation. And,
but in this, uh, in my, my thesis is, is, is that we need to rethink the sort of model-based Bellman,
uh, formalizations in order to compute these nice factorizations that move us around high dimensional
space. Like we've been talking about on the previous slides. So we're going to formalize some
new Bellman equations called operator Bellman equations. And these are going to be, uh,
non-stationary Bellman equations, or they're going to be functions of time.
So instead of having a value function that says, you know, what's the accumulated reward that I get,
I'm going to have a cumulative feasibility function, kappa. And this is going to represent
what is the cumulative probability that I achieve a particular goal, where a goal, remember, is an
action on a higher level space. So this has a very similar form to the infinite horizon Bellman equation
that I just showed. But you'll notice that we have this availability function here for a specific goal.
So this is a single goal, G that we're picking out. So say the, uh, the eat an apple goal or the drink
the water goal, we're just choosing one. And so F is, um, returning the availability of G from any given
state and time and action. And then, so if either the agent achieves a goal now, which is what this
equation is saying, or which is the plus the agent does not achieve the goal. So one minus the probability
of achieving the goal is the probability that you, you don't achieve the goal times the expectation
that you achieve it in the future. So it has this similar recursive structure that the infinite
horizon Bellman equation has. Okay. So then we have the policy and this policy equation is a little
different from the last one, uh, because you can imagine that you can maximize the cumulative that
you achieve a goal, but you, you sort of do it at the last second. You have a lot of, you have
maximized certainty that you can get to the store right before it closes. So you have, you know, you,
you know, a hundred percent that you can achieve the goal of getting an item from the store, you know,
five minutes before it closes. Well, it might be if the store is open for some, you know, period of time
that, um, essentially you might want to get it as soon as possible. So what this equation is saying
is that we're going to, um, pick the action, which maximizes the cumulative, but from that set of
equivalent actions that maximize the cumulative, which is a star. So we're collecting the actions
that maximize the cumulative, and we're going to pick the one that minimizes the time. So this is a sort
of conditional optimization that says, you know, subject to the fact that we want to maximize the
cumulative. We want to get there, uh, as fast as we can. Um, and so normally there's just, you know,
with the infinite horizon development equation, there's the value function in the policy. Here we
have a third, um, uh, function, which is the state time feasibility function, which I've been talking
about. And the state time feasibility function says, given that I start at X and T, what's the
probability that I achieve a goal G at a particular state, final state in time X, F and T, F.
And so, um, you can compute this via dynamic programming as you're computing these other functions.
And, um, there's, uh, a relationship between the cumulative feasibility and the state time feasibility,
which is that if you, you can sum up the individual spinal states and times in that, uh, from your state
time feasibility, and that is the cumulative. So the cumulative feasibility is just summing over
the individual probabilities of a, of a given state final state time. And the nice property
is that when you move, when you use these operator Bellman equations on hierarchical state spaces,
such as the product space, um, of the agent's core ontology, um, it has a nice decomposition property,
which is that if you're just solving to go to a particular point in the world, then you can actually,
uh, compute eta separately from the high level space. So you just solve for, for eta, the state
time feasibility function on the low level space, but then Omega can be computed independently in the
high level space and they can be combined. So this decomposition property is really nice because we
never want to work in a product space. Um, especially as we learn tons of dynamics about how the world works,
we need to, we need to be able to compute representations in a factorized way, which is going to help us move
around, uh, in reason. So the, this means that, you know, when we compute, um, a bunch of, uh, individual
state time feasibility functions for each goal, I don't know why this little hat is here, but, um,
then if we have, you know, five of these and we have an aggregate feasibility function,
then we can use this aggregate feasibility function to move around from, uh, from feature to feature in
the low level world and update all of our internal and higher level states. And so
this is the object from the previous slides that, that sort of map us around the world.
So you can also do, and I won't talk about this much, but you can also, you know, do logical tasks
where instead of eating an apple, you might want to gather an apple. So if you, if you go obtain an apple,
then there could be a bit that corresponds to having an apple and you flip that bit to one once you go to
the tree, and then you go gather water at the lake and you flip that bit. And then you go to the key
and you, uh, obtain that key. And that might be a task where you have to do these three, you have to
obtain these three items, perhaps because you wanted to compose this task with something else. You want to,
you know, bring these items to another agent or whatever. So the point is, is that you can use
these factorizations to move around the world, especially when, you know, things in the world
have a sort of limited time period in which they are available. So, um, so yeah, I talked about
how we can plan in these high dimensional state spaces, uh, using this factorization.
And now, um, we get to the question, well, why should I plan to any particular high dimensional
state? And that's the intrinsic motivation question. You know, given that there's an exponential number
of state vectors in a product space, why is one, why is one state vector of the world, you know, in the
far off distance better than another? So that's where empowerment comes in. Empowerment is an intrinsic
motivation metric, uh, which sort of represents controllability. So formally empowerment is a
function of a transition operator. It's a, it's an intrinsic, uh, measure of an intr, uh, of a transition
operator. And it's, and you can also condition it on the states that an agent is at. So it takes two
arguments. It also has a horizon N, uh, which we'll talk about in a second. Um, so it's formally defined
as the Shannon channel capacity between your actuators or sequences of actions that you take
and the resulting states. So the channel capacity, uh, so here, you know, an open loop sequence of actions
would just be, uh, you know, go up right and up again, or up left and then down. Um, there's a whole
bunch, there, there are a lot of possible sequences of actions. So big A here is a random variable for your
sequences of actions. And so for a horizon N, you can ask, you know, what's, how much information can we transmit
from our actuators to the resulting state at time tau? So tau minus, uh, tau minus T is our horizon, uh,
N, which is this parameter on the empowerment. So it's just saying, you know, how much, what's,
what's the agent's capacity to affect the future with, uh, certainty or, or varying amounts of certainty.
And so the channel capacity is formally defined as the maximum mutual information given, uh,
distribution over these action sequences. Um, and the mutual information decomposes into the entropy of
the final states minus the conditional entropy of the final state random, uh, random variable,
given that, you know, given the actions and, and your starting state. So this means that there are two
sort of like extremes to empowerment. Um, if PX is a deterministic operator, and so anytime I'm at state
X and I apply an action, I get a deterministic output X prime, then, um, the conditional entropy,
there, there's going to be no uncertainty over my future states. So the entropy is going to be zero.
There's no uncertainty. And so that means that the conditional entropy has to, uh, cancel out. And so
empowerment is really just the maximum possible entropy given this distribution. And this just
reduces down to the log of the number of possible reachable states. So how much can I actually reach
in the world? Um, and so, you know, if my horizon is two, we can see that, you know, the empowerment here
is just log of 13. So I think there are 13 states I can get to, and I have perfect control. So I can
actually realize any of those 13 states if I want. Um, and the other extreme is if like, if PX is action
independent, meaning that any sort of state that I'm in, I have an action that maybe there's a, the same,
you know, distribution given that action, say a uniform distribution, um, then, you know, my conditional,
uh, my, uh, my conditional entropy given the actions is just going to be, uh, the entropy. And so
the empowerment has to be zero because this term is going to cancel out. Um, and so there might be a lot
of states you can technically reach because I can select actions and I'm just going to go random
places. So pink is all the states I could possibly reach, but I don't have any control over which state
I'm going to result, uh, I'm going to end up in. And so I can't influence my future in any way. Um,
even though there are a lot of possible futures. So empowerment in that extreme is zero. And then
there's, um, you know, an in-between zone where, you know, you take actions and there's a bias in one
direction or there's different distributions for each action. And so there might be uncertainty,
but you can sort of control how much information you can sort of control, what state do you want to end
up at? Okay. So what I'm going to define is a function valence. Um, and it's important to note that,
you know, there's, there's two arguments, uh, the states, and you can include the time too,
and the conditioning side. So you have empowerment, uh, and, um, so you can define a diff, uh, an empowerment
difference. So say you start at, uh, S and T and then you, um, end up at a future state and time
after you, um, execute some sequence of policies. So row here, uh, appended to the S and T is a sequence
of policies and S row and T row are the resulting states. Then you can compute an empowerment difference.
And this will be our valence function. So Q here is our, is a function that I'll talk about in,
in just a second, but we can see that, um, our, our jump operator that's moving around high dimensional
space is defined as this factorization. So we don't have to represent it. Remember that's an important
part. And so we can sample, you know, multiple policies from this or chains of policies. So if I
have policy one, policy two, then I'm going to have some resulting state R double prime X double prime
TF2. Um, and so Q here can just represent out the output of chains of policies. So you can imagine,
you know, a tree search of chains of policies and Q is just summarizing the final state of those branches
in a tree search of policies of chains of policies. All right. So we can use this Q, right? So notice
that this Q here is in the expectation over here. So, uh, it's linking our original state time to the final
state time. So it's the empowerment after some chain of policies. Okay. So if we have, um, um,
uh, so say we have a deterministic operator and this should be a P, um, then valence is empowerment
difference. We can have a simple sort of example here where we have two hikers that are considering
two different plans. And so if this tree here is like the space of, um, you know, two possible chains
of policies, then these hikers are just executing, you know, one sort of path through this tree. So the,
um, the, um, the hiker on the, so they both have the same empowerment cause they're starting at the same
state and they're both, uh, two away from starving. So they, if we just consider an empowerment
agent at the beginning, that's a log of 13. And if we chain together two, uh, two policies here, we can
advance our, um, internal state space and the agent will end up down at the lake. And so given that it's
at the lake, you'll notice that it's one state away from, uh, from dying so that there there's effect,
an effective range of what it can, uh, where it can go. So the empower, the final empowerment is
log five because there's five reachable states and we're assuming determinism to make this easy.
So the valence here, and this should be PS, uh, here, but I have T here, but the valence is just
log five minus log 13. And that's the difference between the final and the initial. And so that
has a negative valence. Uh, the, the hiker, the yellow shirt hiker is clearly in a worse position
that he started off at. Um, but we can advance the, uh, other hiker with, uh, PI G three to the lake and then
PI G four to the tree and updates his internal states. And we can see that he's three away from
dying. So there's a bigger effective range. Um, and so there are 25 states that he can get to. And, um,
so log of 25 minus log of 13 is 0.94, which, uh, means that, uh, he is, he's better off than where he
started. And so clearly, um, the second hiker is executing a better plan. Um, he has more freedom to,
uh, to engage with other tasks in the world. And so if, if we, you know, searched over this entire tree
of policy chains, uh, we could pick the best one. Uh, and then in this example, we're just going to
consider two, two of these, uh, branches and we'd pick policy, PI G, PI G, PI G three, PI G four.
All right. So there's also an, another interesting, so in, in this past example,
we're just sort of changing the structure. We're just changing the initial states. Um,
but since empowerment is also a function of a transition operator and our operator Bellman
equations are producing transition operators that map us from state time to state time,
then the output of those Bellman equations, the operator Bellman equations produce transition
operators so we can compute their empowerment. Uh, so that's, that's a deep connection between
Bellman equations and these intrinsic motivation metrics. So we can do interesting things where we
can say, well, if the structure of the world were different than the feasibility functions that I could
compute in different configurations of the world would be different. So if, if the honey badger gets a key
and it opens the door in the mountain pass, then it could, it could, um, potentially get through the
other side, but it's important to note that this is changing the, the structure of the low level state
space. So P E not is what we'll call the, the original transition operator in which we can't go through
the mountain pass. And that means that if we compute state time feasibility functions on this operator,
that means P P E here is going into the Bellman equation. Then we're going to produce, you know,
state time feasibility functions from those operator Bellman equations. That's this, uh, object here,
which means that we can use it to construct J to move us around high dimensional space. And so there's
a, an empowerment for this J, but then if we get the key and the key allows us to move through the door,
it changes the structure of the world, then that's a different, um, that's a different mode of dynamics.
So that means that all of this applies on the other side where we can compute, you know, feasibility functions
off of a different mode of dynamics in which we can move to the mountain pass. And so that means we can compute things,
you know, um, by, we can compute valence by asking, you know, is, is this configure configuration of the world
more conducive to the agent's core ontology? That is the agent's internal external coupling that needs
to be maintained, um, as a, as a sort of core object. And so we can compute valence just by changing J,
the structure of the agent's abstractions that it moves to go to, um, perform tasks in the world.
So by computing empowerment on J, we're sort of computing it in task space. We don't have,
we don't have to consider all possible states of the product space. We can narrow it down to,
um, to operators that move us around task space that induce dynamics on, you know, key other state
spaces that we care about maintaining, such as our physiological state, uh, state spaces.
Okay. So here, here's a simple example. Say, uh, the honey badger, uh, starts at the lake and has some
initial, um, empowerment, uh, just on the low level operator. So that's P, uh, five, zero. Uh, there,
there's 12 states that can reach, but it also has a task empowerment, um, which is actually zero because
there's only one task that it can in, in engage at, uh, in if you don't include getting the key as a task.
So, um, the circle here is saying that there's only one, one sort of task that can be done. And so if the
agent goes and gets the key, uh, that's going to, it's going to, uh, you know, reduce its physiological
states cause it had to travel there and then it gets the key and it, uh, conditions a different
mode of dynamics. So there's different feasibility functions associated with that mode, uh, which I
just described on the, on the last slide. Then, uh, the, the door will open and it can travel back to the
lake. And so now that it's at the lake, it can, uh, go, uh, eat food on the other side, right? So before
getting the key, uh, if it couldn't get the key, if there were no key, then it would just starve because,
um, while it could drink water and stay hydrated, it couldn't get, it couldn't eat from the apple tree,
but now it can cycle back, back and forth between the apple tree and the lake, uh, for as long as it wants.
And so it has, uh, a higher empowerment just on the, uh, on the low level state spaces, but also has a
higher task empowerment because there are, you know, just over a horizon of three and we're just computing,
uh, we're, we have to choose a horizon. So the empowerment in task space is eight because there's eight
possible branches in resulting states from, from where it is. And so that's very useful. Um,
so we can compute the, the valence, which is, uh, 0.5 just in the, in the low level space, but also
three in the task space. And another interesting question, which is, um, very important is to say,
well, what's the value of the key. And you can compute this too. You can say, well, given if,
if I just fix a state vector that I'm at, and I just alter the state phi that encodes the object
of a key, if I just alter that state and switch it between having a key and not having a key,
you can say, well, this key is, has this much value to the internal organization, the internal
integrity or controllability of the agent. So it's a sort of agent centric, uh, uh, judgment of how much
something in the world is valuable. And so the key can be not valuable if it doesn't do anything in the
world that helps the agent control its core ontology. So this is a way in which you can sort of bootstrap,
uh, value into the world. You can use it, you can use change in an agent's internal structure. It's
coupling between the internal state spaces and the external world. You can use the changes in that
structure to assign value to things. And that's very useful. Okay. I think we're approaching an hour.
And so I'll just conclude by saying, um, intelligent systems operate in high dimensional product spaces,
often with non-stationary dynamics, this, this introduces a lot of problems, um, especially
in artificial intelligence because people normally deal with structured tasks and non-stationarity by
training, you know, recurrent neural networks and things like this, which take, which contribute a lot
to sample complexity. And what I'm saying is that, you know, operator Bellman equations have this different
form, which produces transition operators, which helps you factorize, um, your representations for
moving around the world and predicting the resulting high dimensional state factor.
And these operators are composable. They compose with themselves, but they also compose with higher
level structure. So you can remap different transition structures to them. It's very modular.
And these are very nice properties that you, that you need, uh, if you want to, if you don't want to
recompute things and you want to have sort of modular structure come in and remap to your
representations that you've already computed. And then, so forward sampling, uh, can you still hear me, Daniel?
Okay. Just checking. So forward sampling is a good way of solving problems in high dimensional
state spaces without representing the product space. We can't really solve, we can't do dynamic programming in
a huge product space. That's not going to work. We can't sample low level actions. That's not
not going to work. It's the tree is too big, but we can, uh, we can work at the level of sequences of
policies and we can evaluate empowerment gain to justify our goal states.
Valence. And so valence sort of unifies a lot of distinct drives. Like there's a different sort of
subfield of RL called multi-objective reinforcement learning, which says, oh, we'll, we'll have a bunch of
different reward functions and then we'll have value functions for each of these reward functions for
like different tasks. And that'll make like a high dimensional value function vector space. Um, and
usually in, in like multi-objective RL, you have to like pick a policy that that's in that, you know,
that's does well, um, in that, you know, value function space, but normally you have to, uh, you have to
deal with the trade-offs by some weighting function. So what I'm saying here is that this allows a, because
valence is just one number and it summarizes an entire sort of control architecture that you don't
have to have introduce things like weighting functions or weighting coefficients to say, oh,
this objective is more important now, or this objective is more important now, now. Um,
so yeah, many latent drives is not necessarily multi-objective. It's multi-dimensional,
it's multi-goal, but it doesn't have to be multi-objective. Um, and I, and so, yeah, with
empowerment, you don't have weighted combinations of empowerment and valence, uh, depends on the
structure of the environment. So it's, um, it's, it's not just some static property of the world or
a static property of an agent. It, it, it incorporates, uh, agent world coupling.
And I thought I'd just, um, end with this quote from Terence Deacon, um, who wrote a great book called
Incomplete Nature, which I love. And I read it at the beginning of grad school and which inspired me
a lot. And Terence Deacon wrote a lot about, uh, teleology from a sort of thermodynamic perspective,
and it's really compelling. Um, and I just liked what he had to say about teleodynamics, the idea that,
you know, that an organism could be, or its behavior could be organized around realizing, you know,
something which is sort of virtual. And he says, teleodynamics is the dynamical realization
of final causality in which a given dynamical organization exists because of the consequences
of its own continuous and therefore continuance. And therefore it can be described as being self
generating specifically. It is the emergence of a distinct, a distinctive realm of ortho grade dynamics
that is organized around a self realizing potential, or to be somewhat enigmatic. It is a consequence
organized dynamic that is, that is its own consequence. And I think, I think that's relevant
to what I'm doing here because, um, I think empowerment sort of on a, an internal sort of structured
ontology allows an agent to say, there are multiple, there, there's a huge space of possible futures,
but I can evaluate, you know, a state of the world that's far, you know, far off in the distant future.
And I can organize all of my behavior around that because I can say, I can give an explanation
for why it benefits, um, my sort of core ontology. And so therefore it makes me, um, capable of acting
that way in the future. It's a consequence organized dynamic that is its own consequence.
So, um, with that, I will, I just want to thank the active inference Institute.
Um, and I will take questions and I'm very interested in, you know, what active inference, uh, theorists
think about the sort of potential for a sort of integrated view of, of empowerment. Because I think
uh, you all have a lot, a lot of experience thinking about generative models and things of, of that
nature. So I'd be very curious to know what you think. Thank you.
Excellent. Thanks a lot. Great presentation. So this will be a fun discussion. Those who are watching live,
please feel free to add questions in the live chat and you can unshare your screen and we'll begin.
I guess I'll take an empowering deep breath and ask a general question. And then I have some scattered
notes that I'll love to dive into. So how did you come to this area of research? What brought you to
control theory modeling and to the empowerment perspective specifically?
Um, hold on. I'm just bringing up the YouTube stream so I can see comments right now.
Um, what brought me. And general question. Mute that one. There we go. Yeah. I'll mute that.
Sounds good. Thank you. Yeah. So what brought me to empowerment? I've always been interested
in, yeah, how, you know, how, how could animals, uh, interact in a world in a, in a way that's so
sample efficient and especially like, you know, knowing that, you know, animals can, you know, like,
like a baby horse can, you know, get up and move around and interact with the world in a sort of
fluid, flexible way. You know, what are the sort of core representational capacities that are needed to
do that? And I didn't really see anything from the RL world. And this is before I knew about active
inference. Um, and so that's always been in the back of my mind. And another big influence was a guy named
Nishith Srivastava, who wrote an interesting paper about how you can basically have a sort of
relativistic decision theory that allowed you to make judgments between different items without recourse to
sort of hedonic utility theory maximization. And so he, he sort of argued that if there was something
like a latent acceptability function that you could, you could sort of measure, you could sort of
remember a history of item acceptability, and you could remember the context that you made decisions,
and then you could actually just do Bayesian inference over those memories. And you could explain a lot of
interesting things like preference reversal phenomena in decision theory, where you introduce irrelevant
alternatives, and it like changes the fundamental choice you make. And I thought that that, that sort of
initiated a lot of thinking into how could you have, how could you bring those kinds of intuitions into
sort of embodied planning? Like, how, how could it be that you have an agent assign value to things without them being
sort of attributed as sort of static, um, sort of static preferences or static utilities in the world? So I think that
was also a big inspiration.
Preston Pyshko, MD, Awesome. Okay. And then one short general question, why the honey badger?
Preston Pyshko, MD, The honey badger?
Preston Pyshko, MD, Yeah, my advisor showed me a YouTube video of, of, of a honey badger named Stoffel. And in my paper,
reward is not necessary. It's the, the opening, um, paragraph talks about Stoffel, and there's a link to this
YouTube video, but Stoffel is, is, is a honey badger in Australia. And, um, he, he, he's at some sort of like animal care center,
and he, he's really good at escaping from things. So the, uh, the caretaker of, of, of, of at this animal sanctuary
constantly has to build, you know, like elaborate structures to keep Stoffel in. So he has this sort of pen called Badger Alcatraz,
and, uh, Stoffel would do interesting things like, you know, find objects to lean against the wall and climb over.
Or, and if you took those away, Stoffel would pack, you know, mud into balls and stack them into like a little pyramid against the wall to climb up and things like that.
So, yeah, it got me thinking like, what is, what is a sort of good general intrinsic motivation function that isn't, doesn't just work on, you know, low level states,
but also in a sort of more conceptual hierarchical space, like there might be objects or mating opportunities or anything sort of outside Badger Alcatraz.
So that's a sort of way in which you could have an agent sort of think in a sort of abstract way in order to justify motivate its motivations.
So I, I, I encourage the, uh, the listeners to, to, uh, look up that video. It's entertaining.
It's like this general escape impulse.
Yes.
Extended into our open air context where we also want to maintain the ability to move.
And for mobile creatures, that's quite a good proxy for what we might want to care about, like living.
Right.
All right.
I'll go to a question in the chat from Alex Kiefer.
Fantastic work.
Maybe a naive question.
And I'm sure it's clear in the formalism, which I have only begun to look at.
But the idea is that actual agent environment coupling figures in computing empowerment, right?
If so, is there a fully internal proxy that can be optimized given information available internally?
Hmm.
Is there, let's see.
Is there a fully internal proxy that can be computed that can be optimized given info available internally in not part of the coupling?
Does he mean?
I, I suppose, I mean, I suppose you could compute empowerment just on the internal state space.
Um, but I don't know. I actually, I kind of want to say no, just because you do need to use actions to move around and influence other state spaces and things like this.
Um, I don't know how I would compute.
Yeah. Just to sort of internal.
Intr, yeah. Intrinsic motivation function that, that isn't a part of some coupling to some broader system.
What about the desire to think freely and to move in cognitive spaces broadly?
Yeah, I agree. That's that.
Okay. So yeah, I definitely agree.
If, I mean, if you have all of your sort of physiological, you know, needs met and there aren't sort of imposing themselves on you, you're sort of freed up to do other things.
Right. Um, so yeah, I think that this could work generally into very abstract spaces, maybe even mathematical spaces.
Um, and yeah, I think that there can be dependent, like higher level dependency structures in, you know, abstract thought or mathematical thoughts or things like this.
I mean, you think about, you know, faulty proofs that, that sort of like destroy an entire field or something like, uh, there, there is a sort of dependency structure in which you, that, you know, if, if you're working on mathematics that assume some proof is true and it turns out to be false, then, you know, perhaps that's disempowering from a sort of abstract.
Uh, perspective, I suppose. So that would be, yeah.
And when there are, again, you are. Yeah. Good.
I was just going to say, but again, yeah, all that mathematics is being done by, you know, some system that has to, uh, perform computation, which takes energy and stuff like that.
So it's always sort of constrained, constrained by that.
Hmm. Well, constrained by some kind of external internal coupling.
Yeah.
Many ways to go. Let's, let's swerve towards active inference and then see if we can come back to some other areas.
Um, you mentioned the generative model of active inference, but you took a different approach.
There's different model ontology.
So just broadly, how would you structurally contrast the coupling of the agent in the environment in active inference and in what you've proposed?
Because the representations that we see in active inference often feature the particular partitioning where a Markov blanket of a Bayesian graph is intermediating between internal and external states.
And then there's a mapping function between those internal and external states such that they can, um, engage in an adaptive coupling again, mediated through the blanket, which is interpreted as providing incoming sensory observations and outgoing actions.
So structurally, is that compatible, incompatible, or some other secret third thing with what you proposed?
Yeah.
Yeah. So I would start off by saying that I think the thing that makes my work different is that it's the structure of the, you know, the latent sort of discrete state space.
It's that structure that's under consideration.
And I think, and I think that in active inference usually encode things like homeostatic drives, right?
You encode them in a generative model, right?
Correct.
They're encoded as a preference over sensory observations so that the entity, uh, seeks out and selects ultimately policies that reduce or bound their surprise about those observations.
Like I expect and prefer myself to be at homeostatic temperature.
I'm not surprised when I'm in that range and I'm going to undergo actions so that I find myself in that range.
Yeah.
Yeah.
So I would say that that is a major difference.
Um, because the, because the state space in my case has this sort of self undermining quality where it's like bad, you know, starvation states.
It's not, it's not really a surprise, an expectation of receiving a particular signal or having a preference over some state of the world.
It has a sort of, uh, self undermining quality that affects your ability to control every, everything else.
So I think that I would, yeah, I think I would contrast it that way that usually the preferences or the quality of the states are sort of encoded in a generative model in the active inference setting.
And here I'm saying that there's a sort of structural coupling that's giving rise to these valence signals.
Hmm.
You mentioned the key being obtained as inducing this change in the agent's ontology and one that was ultimately reflected by increase in empowerment, hence increase in valence.
So how does it come to understand that this shiny object unlocks that door?
Yeah, I wish.
Yeah.
I mean, I think that, uh, throughout my career, I will try to make steps towards like, you know, actually, um, actually figuring that out because a lot of this would comes down to dynamics learning.
You know, if an agent doesn't know what a key does, right.
It's not going to know that it opens a door and therefore that it can move through the door and things like this.
I think there are a lot of sort of maybe like DINAA, like algorithms in which you sort of alternate between learning, learning things about dynamics or things like this.
But that, that is a sort of outstanding question for me is like, yeah, how would you take a key and learn exactly how it's changing the dynamics?
Um, but yeah, what I am saying is that given, given that you can do that, if you can do that, then you can really sort of make these value judgments to things in the world.
So I think that's really important too, because like consider money, right?
Like if I find a $20 bill on the ground, I'm just going to pick it up.
I don't think I'm doing a fancy computation, right.
Um, of, of like, Oh no, my, my bank account is $20 greater.
And so therefore I'm going to, I have all this new capacity or things like this.
I think, I think these sort of preferences for various objects, like a, a key or a dollar bill or things like this can sort of be, you know, stored and maybe, you know, maybe models with utility theory.
Who knows?
Hmm.
Okay.
Jumping around to some different questions.
I hope I'm accurate in saying you described empowerment as a Shannon information, theoretic channel capacity between the actuators and the realization of the state.
Yeah.
We might be familiar with hearing, uh, Shannon channel capacity in the context of bandwidth of information transfer or upload and download, for example, but this is kind of an action oriented Shannon channel capacity.
So what does it mean to, to get an intuition on that capacity between the actuators and the state?
Yeah.
So it's, it's the channel capacity is the maximum possible mutual information between the actions you choose and the resulting states.
So the channel capacity is sort of the maximum information that you can transmit from your actuators to possible states of the world.
It's, it's a, it's a form of optionality that says, you know, I can affect this many sort of possible futures.
So yeah, it's a sort of intrinsic property of an agent.
And so in a product space, this is going to be affected by a lot of different state spaces.
If they're interacting like physiological state spaces can, you know, kill you if they get too low.
So I think the interesting thing about this is that it sort of encourages you to think about cognition in a, in a, in this sort of interrogative way.
way. Because, you know, you're essentially trying to figure out, you know, what, what you can do,
but there are a lot of, you know, different state spaces that are hindering that information
transfer from, you know, your actuators to your state spaces. So I think, I think it's very useful
because it can sort of, it also sort of leads to like explainable AI, right? You can sort of explain
your intentions in terms of concrete state spaces, which, which have structure and explanation,
things like that. I think I got off topic from your, your question, but anything else on channel,
channel capacity that I should talk about? I think before we loop it back to potentially
expected free energy, you mentioned the AI topic. And is there any risk of an imperative that
features its own empowerment in terms of an AI being able to then select action policies that
might not be what anyone else expects or prefers, may not even be concordant with their own encoded
explainable AI priors, but rather something that takes an unbounding approach?
Yeah, I do think that that is a fear. I don't, I haven't thought that much about like
the alignment question. So I'd be very interested in, in what like alignment researchers think of this
perspective. I think that there's a lot of interesting work to do on sort of multi-agent
empowerment, especially with these sort of abstract transition operators that work on long time scales.
And, you know, you can see that how sort of socialization matters and things like this.
You know, if you're, you know, in a world of multiple agents, do you have, you know,
do you have to learn to respect all of the agents, you know, empowerment? I mean, they can also act
against you, right? So, yeah, I don't know. I do think it's a fear to take seriously.
I don't know how I would do it though, because it's, it's an outstanding research question to me.
Coming from an ant colony background, you mentioned the socialization and I immediately thought, well,
let's just say that the seeds take two or three nest mates to carry home. So in order to have one
nest mate achieve the maximum empowerment, they must also engage in a pro-social environment.
Because if anyone else, even if their model is like smaller and less empowered, if they just decide
not to play, then that individual, until it figures out how to carry the seed home alone,
is going to actually be kind of tethered to a social fabric that helps it actually obtain those goals.
So it puts the social imperative as a screen in front of potentially any other imperative.
Yeah, that's a great, that's a great thought.
You mentioned the decomposition of some function. I'll let you unpack what exactly,
what function was being decomposed and you, you, you justified that by saying,
we never want to work in the product space.
Yeah.
From a computational complexity perspective or however makes sense, what are the dangers or
what are the scaling features of that product space? And then what is the decomposition that
facilitates a more tractable form?
Yeah, I'll share my screen again and we can go back to that slide.
Thank you.
Let's see.
Here it is.
You can see my screen?
Yep. And maybe even a brief summary of what is a Bellman equation and how did you move from
the standard formalization of Bellman equations into this operator space?
Sure. Yeah. The standard Bellman equation.
I don't know the button for one slide forward, but okay. So the standard Bellman equation,
it says this recursive form and it's just the value of a state that you're at.
The, the, the optimal value of that state is the maximum, it's the maximum value that you can get
by choosing an action that rewards you and takes you to a state from which you can act in the future
to get more reward. So the Bellman equation, um, can be solved by dynamic programming, um,
in order to maximize this function V. So it'll, it'll, it'll result in a policy that moves you around the world, uh,
in a way that accumulates a reward that you'll find in your environment.
Um, so it has this recursive form, uh, you can, you can sort of unroll it into a sequence.
Um, and then the operator Bellman equation has this similar recursive form where now,
you'll notice that there isn't a reward function. There's this availability function and it returns
a number between zero and one. It returns a probability. And so that's significant because it
makes, it means that you can maximize the cumulative feasibility. And so F here is just saying this goal
is available. Either you achieve the goal now, or you take an action, you don't achieve it now,
but you take an action in which you'll achieve it in the future. So that, um, it has the same form where
you can sort of think of an availability function as a reward, but it's maintaining a probabilistic,
um, form. And that probabilistic form is important because it's what allows you to compute
the state time feasibility as a transition operator, as an operator that maps you from
where you are now, the state time you're at now, which is XT to the final state time and goal that
you achieve. Um, so under the policies, so it says, if I start at XT and I follow this policy and I'm
choosing actions that move me through this state space, then I'm eventually going to get to the goal.
And I want to know the final state in time, the probability that I, uh, achieve this at any given
state in time. And so the state time feasibility function is here as it's expressed is a transition
operator with one action, which is the policy. But when we aggregate it, I'll bring this up.
When we aggregate it into multiple possible feasibility functions that are centered around,
multiple sort of objects in the world, then all of the policies associated with each one of those,
these are goal condition policies that are going to terminate on achieving the goal of going to one of
these features and, and, you know, getting the apple for instance, then those pop, each of those policies
is an action for this transition operator. So there's five, five possible policies that are
going to take you around the world, uh, around the space. So these operator Bellman equations have this
probabilistic form, which retain this probabilistic structure. And you can sort of compare this with,
um, I don't know if you're familiar, but there's this concept in RL called the successor representation,
um, which is like often a hot topic in, you know, computational neuroscience and the successor
representation is sort of talked about, like it's this predictive operator, but really what it represents
is expected state occupancies under a policy. And those expected state occupancies are weighted by the
discount factor. So it's really a four, it's really a successor representation is really a sort of weighted
statistic. And it doesn't map from like an initial state to the state of achieving, of inducing an
event of, of achieving a goal. These are, so where successor representations aren't compositional,
you can't multiply two successor representations and get another successor representation,
but you can multiply matrices that represent state time feasibility functions because they're mapping
their, their, their probabilities. So of, of events. So you can, you can combine them just by multiplying,
you know, matrices that represent, you know, the state time feasibility function for a given policy
with another one for a different policy. So that will, um, retain, uh, a, the form of a probabilistic
function and that's what makes them reusable, composable, et cetera. And I think you asked me about the
decomposition and this decomposition. Yeah, I might've glossed over this, but the decomposition result is
that if you have, if you were to compute a state time feasibility function in a product space, okay, which has lots of,
uh, state, lots of states, lots of state vectors, which are each states, um, then, you know, you don't want to
do that because product spaces are very large and take a lot of, you know, memory to represent the operator.
Uh, so if, if this was not PX and this was PS and PS was the full product space operator that moves you around
this high dimensional space, well, you can't really represent that and you don't really want to, but if you did
and you computed a state time feasibility function in a product space, then you can, uh, under certain
conditions, uh, and I can say what those conditions are, but under certain conditions, you can decompose this
into a prediction of all of the higher level state spaces, compute, computed independently. So you
evolve the hunger space separately and you evolve the thirst space separately and you evolve the temperature
space separately. You can do all of those computations locally on those spaces. Um, and you can combine them
with a state time feasibility function that's only computed on the low level space. So, um, so this
hierarchical STF, the state time feasibility function is an intractable object for, for most reason,
reasonably sized problems, but you can implicitly form it by this product of these things individually. And so
this works when you're, when your goal for the, for the, uh, hierarchical state time feasibility function,
when you just have a single goal at arriving at a particular feature of the world, like a tree, um,
that's, that's the, that's the sort of, that's one of the conditions in which this decomposition holds.
So I think that, that answered your question about, you know, the burden of a product space.
Well, you need to, uh, you need to overcome it by doing local computations on individual state spaces
in a sort of network of interconnected state spaces that implicitly form a product space, but you, you
want to compute all of the representations separately in this network of state spaces so that you can sort
of move around this high dimensional state space under successive policies.
And so that's, that's what allows you to handle forward sampling in, in this high dimensional state
space. And that's, that's important, um, because I, I think, and just to, um, recall, uh, the sort of,
uh, presentation, I think it was a Val, a, a V E L who yes.
The front.
Yeah.
Just to echo that, that sort of sentiments that if you're composing, if you're creating new state spaces
or you're composing, you're not computing policies in a fixed world.
Um, you're composing things together.
Um, that's of course going to expand the product space implicitly of all the state vectors of the
system.
And the act of composing thing or bringing new information in is expanding the implicit product
space that you are in.
And so from an RL standpoint, um, it's not so clear, you know, what a reward function on that
product space is even supposed to be.
I don't think that anyone will.
I answered that question, but it's also not clear what, you know, what a generative model
should look like on that product space either.
And I think given that, you know, organisms or humans at least are so skilled at this,
at this sort of dialectical process of proposing theories and composing structure, um, as hypotheses
and, um, in interrogating what that means, I think that there, I think that value comes
from interrogating, you know, what it means for the structure of the world to be a certain way.
So if I, if I learn new dynamics of the world and I want to control dynamics on some new space,
it might affect other state spaces.
But, you know, from a normative perspective, it's not really clear, you know, once you compose
something and you're, and you're expanding the implicit product space, it's not so clear where
any sort of normative source of normativity should come from.
But I think the sort of flexible human reasoning that we sort of know humans to engage in, I think,
is in this sort of regime of composition and interrogation where you're always sort of saying,
oh, if the world were this way, then I'm sort of, I, I, then I could see how this state space
affects these other states basis in a way that I didn't anticipate.
And so I think normativity in a creative way has to come from controllability.
That, that would be my argument.
There's a lot there.
So a few directions.
First to our colleagues in reinforcement learning, RL.
The paper is provocative in that it includes reward is not necessary.
So is reward sufficient and, or what is necessary for what?
RL. Yeah, it's a good question.
Is, is reward sufficient?
I think I would argue this, you know, I think that the reward enough hypothesis,
which just to remind some of the viewers is the hypothesis that reward maximization
can account for all sort of artificial and sort of natural intelligence that all of the sort of
features of intelligence, the sort of capabilities, the structure learning and stuff can all sort of
arise out of some need to, there's some, some, some process of maximizing reward.
And from my standpoint, this, that's a frustrating statement because it's one, it doesn't,
one, it doesn't really address where your preferences for specific reward functions come from.
And in the paper that they will say, well, we acknowledge, you know, that there could be
multiple sources of reward.
And, but, you know, the process of deciding on what, you know, reward you should attend to or
care about.
That's, I think, is, is a deciding what signals you should care about is an important part of
intelligence itself.
And I think that reward is enough hypothesis as a hypothesis is sort of under constrained in that
whatever that mechanism is to, to that perspective, it's going to be maximized reward,
you know, under their paradigm.
And so, therefore, whatever, whatever shapes what that mechanism is, that, that, you know,
an agent should attend to this, or an agent should stop attending to the things that's always cared
about in, and attend to some new signal.
I think that that call, you know, I think that that forces you to sort of take the position that,
you know, maybe there's a meta sort of like a meta reward that tells that that directs this process,
because all sort of attendant processes of intelligent systems sort of are underlie the
process of reward maximization.
And also, you know, it, the reward, the reward is enough hypothesis is not being specific about,
it doesn't tell you what necessarily to compute, it just says that if you try to maximize reward,
it will, you will, you will compute the right representations.
And so I think that there's just a lot of like nuts and bolts about what it takes to be able to
reason in a flexible human way.
And what I'm proposing here with the operator Bellman equations is to say, hey, look,
these reward free Bellman equations that help you deal with the complexity of the world,
there's no reward in them.
And you could make the case, well, maybe you could just use these operator Bellman equations
to occupy states that are rewarding.
But I would argue that since the product space, the effective product space that we all live in is so vast,
and we reason about it in such a flexible way, I very much doubt that RL will rise to the challenge
of being able to justify motivations in real time in a way that humans can.
And so to get to the question of, you know, is it sufficient?
My hunch is no, I can't like, I don't have a proof of like, you know, reward is not sufficient.
But I also think that the information that a reward function is supposed to carry about what is good,
I don't think that that is, that is knowable or computable on the timescales that we understand
human intelligence to work at, to work on.
And so, yeah, in order to answer your question about what is necessary, I don't know
what is necessary, but I would just sort of make the point that I already made of that,
I think that we have to get to a point in which we sort of acknowledge the problems of product spaces,
and sort of reasoning dialectically in a product space that we can't explicitly represent.
And so I don't know, I don't know what is necessary, but I can say that it's not necessary
for simple self-preserving agents. And that's the claim of the paper.
Awesome. All right, in our closing segments, I'd like to take a journey to philosophy and then
connect this back to potentially relationships between the models that you've presented here
and active inference and maybe even walk to the edge of that cliff of the hybrid model.
So Aristotle proposed four causes. Material cause, what something is made of. The efficient cause,
which is the source of change. The formal cause is the essence. And the final cause is the teleology,
the end goal of the object. And your presentations,
the teleos, was Deakin's analysis of these different forms of teleology. And indeed,
within the model proposed, empowerment was that type of self-referential teleology.
When juxtaposing with active inference and specifically the expected free energy functional,
which has a lot of analogies with an operator, it's a function of other functions, the expected free
energy functional is predicated around helping the agent select policies that over expected futures reduce
their uncertainty the most about which sensations they receive. And that's what ties active inference
closely with perceptual control theory. That expected free energy is ultimately looking at a divergence
between preferences over observations and incoming observations. So that's kind of the sense side of the
coin. It's like, I want to stay in the game to be able to align observations with my preferences. And I'm
wondering if empowerment is the action side of the game. It is saying you'll be involved with, yes, repeatedly
sensing yourself to not be starving, not be dying of thirst, not be dying of cold. Like you'll be in your
preference vector by way of this single value, which is the empowerment. Whereas active inference kind of
comes from the other side saying you're going to end up having a lot of squares to move around in,
but first you need to make sure that you're reducing divergence between your preferences and your expected
observations.
Luke Gromeny
What do you think about that map or where would that take these intertwined models?
Luke Gromeny
Well, I think that there could be like an interface between the two concepts. If we consider that models
of how things work, like composed models of how things work, could induce
Luke Gromeny
particular generative models that you would want to use in a sort of active inference setting.
Luke Gromeny
And that would be the sort of dual nature between the two that there's a crosstalk between
the proposal of of some kind of generative model that would be conducive to the agent.
and if it is then it's a good then it could be a good state encoding which feeds back in on you
know controllability or empowerment and things like this so i mean there's a lot to think about
on this topic um but i guess i would just put put it that way that um that we still need to justify
where generative models come from uh in new situations for new theories of how things work
and things like that and there could be a dual process in which the action side the internal
controllability side is dictating what kinds of generative models that we that should be considered
very interesting and the reason i brought up aristotle's causes was because active inference
as a process theory seems to be describing that efficient cause it's just especially with a
variational free energy which is kind of the real-time version of the expected free energy
it's like one step at a time all going downhill and so variational inference is enabling incremental
unfolding optimization again oriented around reducing that sensory preference and outcome
it does everything but specify a final cause in a sense one might say that there's a local
final cause within the active inference generative model which is like to reduce the divergence
between the preferences and the observations but the generative model also
from the action selection side which is what makes active inference active inference it also needs
a final cause in that self-referential teleodynamic way and so there could be some very interesting
architectures where active inference picks up where empowerment leads like through a needle because it's such a small representation with the
valence and then one other kind of connection or maybe mapping between them is we've seen models of valence in active inference
such as the affective inference work where valence was associated broadly with whether things are going better or worse than expected in terms of statistical uncertainty
if you're reducing your uncertainty more than you expected things are going better than expected and vice versa
vice versa
so that is a very variance oriented
variance oriented
valence concept
where broader
uncertainties are associated with inferior valence
and tighter uncertainties are associated with positive valence
and it's just interesting that that's kind of like an orthogonal valence concept
from how much you can actually do that's the actionable valence
would you rather have a high precision around not being able to do anything
or high uncertainty about being able to do a lot or a huge amount
and so it almost seems like when we contrast those two
the direction that dominates is in the final analysis the ability to have empowerment
not necessarily to just have tight control over your observations

yeah i agree
lots lots of interesting avenues for hybrid theories
well what a very interesting talk
i guess one more question on the model and then we'll close which is the time horizon
is it an infinite time horizon
or what is the treatment of time and can time be continuous or is time always discrete and is it finite or infinite horizon
it's uh so the operator bellman equations are formalized as a finite horizon
i suppose they could be extended to infinite horizon
and infinite or continuous time i suppose that's possible too
but as they're formalized now it's discrete state discrete time finite horizon
um
but yeah i mean i think that there is there's alternative forms that could be could be made
um
is that was there another question too in it i can't remember
let us close with your time horizon
what are your next steps with the research and how would you imagine
an ecosystem of continuation of the work
yeah i'm i'm interested in getting this work into computational neuroscience
um uh because there's a lot of i think alternative models that need to be considered
especially given some of the themes that i've touched on in terms of justifying what to do in a product space
how do you represent control in a distributed system etc
um
and so i think that there's a lot a lot to do there in computational neuroscience
on the ai side i want to put this in a world model
i want to uh
get good you know
auto encoders kind of like how i had on the on the first slide
where you have a high dimensional you know agent in a high dimensional multimodal world
how do you how do you have nice world models and put this in in something like that so that's that's the ai future direction and i'd like to do both of them so
i have a lot of work to do
awesome well in closing i'm just going to read some of the more statement like comments from the live chat just so that they're included in the active inference journal
so dave douglas wrote
with regards to deacon's consequence
galileo may have gotten in trouble
less from insisting on a heliocentric universe
than from insisting that purpose value and meaning
be banished from science as connecting
explanatory principles
the galileo tolerated
remaining connecting principle causation
may have reached the limits of its explanatory power
sometime between newton's and four years day
where all respectable principles of explanation must ultimately rest on invocation of either rigid rods or on elastic bands
the galilean program of sola causa
attained its absurdity in carnapp's insistence that meaning value counterfactuals must be judged as strictly and literally as meaningless
have we passed the point
when the galilean program
must be simply abandoned and meaning value and purpose must be restored to science as irreducible explanatory principles alongside causation
i find the mysticisms of both bohm and heisenberg's quantum completeness and of pauli and jung's synchronicity to just be too fluffy to be very useful
in a word
in a word it has become a tradition of science as funded
to insist that causation and causation alone must found our enterprise
this is a tradition of men
not a feature of ultimate reality
meaning and value also have their place
not reducible to cause
i like it yeah
excellent well thomas thank you again for joining you're always welcome back and really looking forward to seeing how this all continues
me too and thanks again for having me i've been very impressed with how much work you do for the discord and uh
it's it's it's a it's a great community i can everyone's very very nice and enthusiastic so i was excited to see it i just sort of randomly stumbled across it so i'm glad uh i'm glad uh i introduced myself to to the discord so thank you
excellent all right till next time thank you
great thank you
great thank you
thank you
