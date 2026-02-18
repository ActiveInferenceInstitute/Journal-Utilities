---
title: "ActInf MathStream 008.2 ~ R Servajean: Intro to Bayesian mechanics: paths-based formalism (part 2)"
category: "MathStream"
series: "MathStream_008"
episode: "2"
speakers:
  - "R Servajean: Intro to Bayesian mechanics: paths-based formalism (part 2)"
duration: "1:22:34"
url: "https://www.youtube.com/watch?v=S-6qpCNq4uA"
views: 339
exported_at: "2026-02-18T22:37:37.802620+00:00"
format: markdown
---

# ActInf MathStream 008.2 ~ R Servajean: Intro to Bayesian mechanics: paths-based formalism (part 2)

Hello and welcome everyone. It's February 2nd, 2024, and we are returning for Academies Math
Stream 8.2 with Richard Cervajon, Introduction to Bayesian Mechanics, Free Energy Principle,
and the Paths-Based Formalism. Thank you, Richard, for joining for this part two. Looking forward
to your presentation and then discussion. I have a weird echo. Wait. Are you in general
synchrony with yourself on YouTube? Wait, let me see. Okay, perfect. Sorry.
Okay. Great. So, hi everyone, and thank you again, Daniel. So, today I'm going to present
the Path-Based Formulation of the Free Energy Principle. And I'm going to start by a brief
reminder of a couple of things we discussed last time. However, if you're not acquainted
at all with the notions of synchronization map, of variational inference, or longitudinal equations,
it can be a good idea to watch the first video. And if you do so, please check the comment I
posted below where I precise and correct a few things. So, a quick reminder of where we started
and where we... So, basically, if you consider such sparsely coupled random dynamical system,
where mu corresponds to the internal states, eta to the external states, and a and s, the blanket
states, to respectively the active and sensory states. And they form together the so-called
Markov blanket. And just a bit more vocabulary, A and mu form together the so-called autonomous
states. And finally, if you add the sensory states to the autonomous states, so you consider
the whole Markov blanket plus the internal states, you end up with the so-called particular states,
pi. And the particular states defines or constitute a particle, an agent, bacteria in my schematic,
for instance. So, if you consider such sparsely coupled random dynamical system, you can interpret the
dynamics of the autonomous states in terms of perceptual and active inference. More precisely, you can see here,
in the bottom of my slide, that the autonomous mode minimized a free energy function, which is defined under a
generative model, which is typically the nest density, the non-equilibrium steady state density of your system.
So, more precisely, the internal states, mu, parametrizes the density, q mu over external states. And if you look at the path of the internal
mode, it is so that the free energy associated with your variational density is always minimized. And this licenses an interpretation in terms of Bayesian inference.
And about action, because you can see here that the active mode is also minimizer of the free energy. In fact, it minimizes the surprise term within free energy, so that you can see the particle as actively sampling unsurprising or preferred sensory states, sensory inputs, which is active inference.
And yeah, if you remember well, we saw that the generative model encodes the preferences of your system. So that was basically where we started and where we ended last time. And today, I want to relax a couple of hypotheses. So, first of all, no steady state is assumed.
We could be a steady state, we could have a well defined nest density. But we do no, we don't do any assumptions here, there is no steady state assumed.
So it extends in a way the scope of free energy principle. The second thing we do is to relax the white noise assumption. This means that we don't deal anymore with infinitely rough fluctuations, but we have
fluctuations which are smooth. So basically we deal with colored or correlated noise. And this means that the fluctuations become differentiable up to a certain order.
So basically, instead of dealing with x and x prime, let's say, you have x prime prime, and so on and so forth. You have higher dynamical orders, if you will.
Note that this vector x here, which precisely corresponds to x, x prime prime prime, and so on, is called the generalized states. And the shifted vector, this one, where the first component is x prime, we refer to it as the generalized motion.
And we also say that we work in so called generalized coordinates of motion, not to be confused with generalized coordinates in analytical mechanics. So a lot of words, but we just, we are just saying that the fluctuations are smooth now, and we can differentiate these fluctuations up to a certain order.
And this order. And this order is the order of generalized motion. And it tells you how large the correlation length of the fluctuations is basically.
I also want to introduce the notion of generalized state space. So basically, you can augment state space with generalized motion.
So instead of just looking at x, the state of your system, you look at x prime, x prime prime, etc. And so basically, we consider the so called generalized state space.
Okay, so a lot, once again, a lot of words just to say that fluctuations are smooth now. So if you look at the equation below, it seems that there is a dots and primes here, which and it seems a bit redundant.
So in fact, what we call x dot here, you can view it as the actual time derivative that you can evaluate anywhere, for instance, at t equal to, and the x prime here is just the second component of the momentary generalized states of your system, for instance, at t equal to, so that if you evaluate your time derivative at t equal to, it equates indeed x prime.
But the distinction between the two will become more clear later in the context of generalized filtering.
So the cool thing here is that if you perform a Taylor expansion of the state of your system, so you have an equation like that, you can see that generalized states constitute the coefficients of your expansion.
Indeed, indeed, you can see that you have x, x prime, x prime prime, etc. So basically, you do a Taylor expansion around equal to, basically, and the coefficients of your expansions are generalized states.
So in a way, you can see generalized states are as encoding a path, as encoding the future of your, of the state of your system, thanks to this Taylor expansion.
And that's basically what I wrote here. A point in generalized state space corresponds to a path. That's exactly what I just said, in virtue of this Taylor expansion here.
So the consequence of that is that if you look at the surprise of our generalized states, the negative log p of vector x here, and we call it the generalized Lagrangian.
Lagrangian, it plays the role of an action, scoring the likelihood of a local path over the correlation length of fluctuations.
So let me break down a bit this idea. Once again, here, the, the, the order of generalized motion depends on how smooth the noise is.
So basically, when you look, you do this Taylor expansion, the, the time scale considered here corresponds to the, the correlation length of your fluctuations.
The more correlated your noise is, the more dynamical orders you have, in a way, the larger the path encoded by generalized states.
And the corresponding surprise, the corresponding generalized Lagrangian, negative log p of vector x, is a quantity that scores the likelihood of this path in virtue of the correspondence between points in generalized state space and paths.
So a last, a last remark I want to, to do in order to be sure that everything is clear here, is the following.
You might be a bit confused, especially if you have a physics background, because Lagrangian's and actions are two different things.
So let's take a, let's take a step back and ask, I have a path, trajectory in state space, if you will, and I want to compute a probability density associated with a path.
How should I do?
So the first thing to do is to discretize time.
So basically you discretize your Langevin equation.
So for the people acquainted with stochastic calculus, just notice that it means choosing your alpha discretization, either Ito or Satanovic, let's say.
And from your discretize Langevin equation, you define an infinitesimal propagator, just like for path integrals in quantum mechanics.
An infinitesimal propagator is just a transition density between one state to the next during a time window dt.
Then you multiply the infinitesimal propagator.
And then you go to the continuous time limits.
And so in a nutshell that how you proceed to compute, to write down a density associated with a path.
And if you do that, for instance, in the simple case of a Vener process where the noise is the Gaussian white noise, you end up with the density of a path being proportional to the exponential of minus something.
And this something we call it the action.
So the smaller the action, the more likely the corresponding path.
And this action, in fact, corresponds to an integral over your path of something.
And we call this something a Lagrangian.
So a Lagrangian is defined at any point in time while the action characterize the path as a whole thing.
So conceptually speaking, Lagrangians and actions are two very different things.
But here, the key move is to kind of leverage the idea that a point in generalized state space encodes a path.
So that the surprise over generalized states, this negative log P of X, which is defined as a generalized Lagrangian, plays a role indeed of an action.
Once again, scoring the likelihood of a local path over the correlation length of fluctuations.
So that's really the core idea underlying the path based formulation of the free energy principle.
So basically, now that we have introduced these ideas, let's look at the generalized Lagrangian over autonomous states.
So I just want to point out that throughout the presentation, in virtue of this correspondence between points in generalized states and paths, I will call generalized states path.
For instance, here I would say the Lagrangian of autonomous path.
I use these words in an interchangeable way.
And similarly, when I am dealing with an autonomous path minimizing a generalized Lagrangian, I will be talking of the path of least action because Lagrangians play the role of an action.
So be aware of this terminology.
So if I'm looking at this generalized Lagrangian of autonomous path.
So negative log P of alpha.
The cool thing here is that if I remove fluctuations noise on particular states or path.
So basically the particle respond deterministically to its environment.
I can rewrite this Lagrangian like that.
And this formula coincides with unexpected free energy.
So what this formula is all about?
Well, we can reorganize it.
And if we do so, you can, for instance, write it that way.
So what it means is basically that the path minimizing this Lagrangian.
So the most likely autonomous path, average over all possible sensory path, has to minimize these two terms.
And these two terms are very interesting because the first one, if you look at it, is it is an expected Lagrangian over sensory path.
So minimizing this Lagrangian means this expected Lagrangian means following an autonomous path, which yields unsurprising or preferred sensory path.
And therefore it can be viewed indeed as an expected cost you want to minimize.
And if you minimize also the second term, this negative expected information gain, you can see that it is just an expected KL divergence between two density.
And these two densities, the difference between these two densities is just that the first one here is conditioned upon S.
So basically these two densities are different if the sensory path is informative.
So maximizing this expected information gain means following an autonomous path yielding an informative sensory path.
For instance, let's say you are in a dark room where there is an ambiguous mapping between the hidden latent, the hidden external states and the sensory stimuli, let's say.
You can turn on the light and then this action would yield informative sensory inputs.
So that's the idea underlying the maximization of this expected information gain.
So this quantity is very rich.
And in fact, you can do connections and links with many established ideas.
For instance, you can speak of optimal Bayesian decisions and optimal Bayesian design or of pragmatic value and epistemic value, etc.
The whole idea here is that this quantity entails the preference seeking imperatives of the particle, that's the first term, and the information seeking imperatives of the particle, that's the second term.
So the path minimizing Lagrangian kind of constitutes the best direction of travel, the optimal direction of travel for the particle, so that you can view the particle as constantly engaging in an optimal behavior.
Okay.
So now, having said that, I want to go back to the whole idea of synchronization map we talked about last week.
So, in fact, in this setting, everything is exactly the same.
We just augmented state space, if you will.
But you have mu parametrizing the density, everything is the same.
And if we consider the internal path of least action, so the internal path minimizing this Lagrangian here, the corresponding parameterized density over external path coincides with the density over external path given sensory path.
So that if you write down the corresponding free energy, you have the first term which vanishes in virtue of this above equality here, and free energy reduces to surprise, if you will, to this Lagrangian over particular path.
I'm going to, so before using this to derive directly the free energy principle, I need to briefly introduce the notion of generalized filtering.
So, in a nutshell, let's say that you have some data, you have the vector s here, a sensory path, let's say, and you want to compute negative log p of s.
That's the quantity you ultimately want to evaluate.
But it's intractable.
Let's say that computing this p of s would require a monstrous marginalization and you can't directly compute this guy.
Instead, you define a proxy, you define an upper bound, this variational free energy, which is parametrized by mu, by vector mu.
And you just want to minimize this free energy so that it coincides with what you ultimately want to compute, namely, once again, negative log p of s.
So in order to minimize, indeed, this free energy, you just follow a recognition or filtering dynamics, which is, in fact, a gradient descent on free energy.
In fact, the exact dynamics at play here is this equation here.
So you could ask, but why don't we just have the gradient term here, nabla f?
Why do we have a second term here, this d mu?
By the way, about this d mu here, what is it?
Well, the matrix d here is just this matrix with ones here in this line.
So basically, if you have a vector x, let's say, x, x prime, x prime prime, and so on, and you want to get from this vector a shifted vector x prime, the motion, if you will, you just have to apply this matrix d here and on x, and it gives you, indeed, x prime.
And so basically, you can use this d mu here as being equal to mu prime, basically.
And the idea is that you, when, once you, the gradient term here is minimized, when free energy is minimized, so we look at the stationary solution of this equation, if you will, mu dot coincide with d mu.
And let me just explain why we don't just have the gradient term here.
If we only had the gradient term without the d mu here, we would go down on free energy until a minimum is reached.
And basically, we would have the first component of the vector mu being non-zero, but all the higher dynamical orders would be zero because we are at the minimum of free energy and we don't move anymore.
But here, it is a wall vector mu, which parameterizes free energy, and we don't want all the entries to be zero.
And we want an equation which guarantees that, so that we add an additional term in the equation.
So that's basically, in a nutshell, what generalized filtering is all about.
And by the way, note that if you consider the path of least action of some process x, you can write it in a very similar fashion.
The only difference is that here, the quantity minimized is just the generalized Lagrangian here, whereas it was free energy in the context of generalized filtering.
And by the way, we just saw before that if we consider the path of the internal path of least action, the corresponding free energy here associated with the density, the internal path of least action parameterize, it reduces to the Lagrangian.
So that's when we write down the equations here, verified by the autonomous path of least action, you can directly identify free energy to the Lagrangian.
And we basically have the same equations that in generalized filtering.
So basically, if we look at the autonomous path of least action, you can interpret the dynamics of the internal path of least action.
So in terms of Bayesian inference, which takes the form here of a Bayesian filtering scheme.
And note that if we remove fluctuations on particular states or paths, that's the definition of dealing with a conservative particle.
The autonomous path will coincide with the autonomous path of least action.
And note that ignoring fluctuations might be relevant when it comes to very large particles, where you can.
So to very large particle, you can coarse grain.
You can coarse grain.
And you can check these papers here where they try to average out fluctuations using a renormalization group approach.
So in the end, we find the free energy principle just as before.
But the difference is that here, the Bayesian inference takes the form of a Bayesian filtering scheme.
But otherwise, we still end up with a variational principle accounting for the perceptual and active inference that the particle do.
So, okay, now I want to do a bit of zoology, of typology, let's say.
I said last time that this sparse coupling architecture here was a canonical sparse coupling architecture, but it was not a definitive feature of the free energy principle.
And that we could look at other sparse coupling architecture.
And I want now to look at various sparse coupling architecture.
So the most simple ones you could imagine is one like that, where you don't have active states.
So basically, the Markov blanket is only made of sensory states.
In the end, you can still write down the internal path of least action like that.
But it will the idea that the particle encodes beliefs about its external environment, it will not manifest to an observer, because by definition, an observer has only access to the Markov blanket.
And that's what this quote is all about when it says that whether internal paths of least action parametrized beliefs about external paths, and therefore minimize operational free energy, can only manifest via active states, that is, in active particles.
And, of course, no one would attribute any form of agency or sentience to a simple piece of rock, for instance.
So if we move to the realm of active particles now, we basically have the equations we studied before.
But the difference here with this sparse coupling architecture is that the active states do not directly interact with the external states, and the sensory states do not directly interact with the internal states.
This sparse coupling architecture is quite interesting because it reminds, I would say, it reminds the way a bacteria is coupled with its environment.
Because you would have, like, the outer membrane with all the transmembrane proteins, the receptors, whatever, which would correspond to the sensory states.
And then you would have the underlying cortex filaments which mediate many aspects of biotic actions.
So I like very much this architecture here.
So I like very much this architecture here.
But we can even go further in the sophistication and consider the so-called strange particles.
The only move here is that we don't have any arrow from S to eta, but more importantly, we don't have any arrow from A to mu.
So the active states do not directly influence the internal states.
And this is interesting because it means that now the internal states alone are independent of both the active and the external states when conditioned upon the sensory state.
So from the point of view of the internal states, the active states become a latent cause, just like the external states of the sensory states.
So basically everything is the same.
You can write down a variational density parameterized by the internal states or path.
But now it is over both the external and the active path.
And so we have this free energy here.
We call it the generalized free energy G, but everything is the same.
It's just a variational free energy associated with our recognition density, which is over both external and active path.
So that's in the end, we have this equation here where you have in the equation of the internal path of list action, the gradient on G here.
So it's very interesting because it basically means that the internal path.
In fact, in fact, cause the its own action, the its own action, which then cause its sensory inputs.
So, and I'm quoting here, the paper, which introduced the notion of strange particles.
You can view the active particle, the active path, sorry, as realizing the sensory consequences of the inferred action.
So basically such a particle kind of author its own action, its own action.
action.
And so the idea here is that the particle kind of infer its own course of action, which will yield preferred sensory outcomes.
So it's really a form of planning of inference.
Strange particles do planning as inference.
So that's, that's quite cool.
And in fact, we can even go a bit further and assume a certain level of sparsity within internal states.
So you would have this mu one here, which influence mu two, but not the other way around.
So from the point of view of the world internal states, everything is the same.
You have a, it parametrized altogether density q mu.
And by the way, under a mean field approximation, you can write it that way, where you would have q mu one and q mu two here.
But the very, very cool thing here is that from the point of view of mu one alone, well, mu one is independent of mu two, a and eta when conditioned upon s.
And you can view mu one alone as parametrizing the density over mu two, a and eta.
And we call it that way with the over script M.
So basically q mu one is a density or a belief about mu two, and therefore about q mu two, so that you can view this q mu one M as a metacognitive belief, because it constitutes a belief about a belief, because it's a belief about q mu two.
So that's just by assuming this simple architecture within internal states, we end up with a minimal Bayesian mechanics, let's say of metacognition.
And it also introduces the notion of metacognitive particles.
So I think that's what Bayesian mechanics is all about meaning translating cognitive abilities in simple physical term.
It constitutes in a way a physics of cognition, if you will.
So having said that, thank you very much.
And especially thanks to all these guys here, which who helped me a lot understanding the free energy principle and especially the path based formulation of the free energy principle.
Thank you.
All right, awesome.
Great.
A lot of ways I could start, but it's so interesting that.
Um, how smoothly the path based continues on.
So maybe, could you give a remark on just the timeline in the literature, which one of these state and path based were developed just roughly like in which ordering was one first or how did that happen?
Yeah.
So I'm not an expert on the story of the free energy principle, but I know that thinking in terms of path and in terms of generalized filtering has been around for forever.
In fact, in the literature, but about the most, I would say, definitive formulation in such terms, I would say that the most important paper is
well, I have it here.
It's called path integrals.
Well, where it is.
I can't see it.
Well, first in physics of life review, 2023 B.
Yeah, exactly.
Yeah, exactly.
This paper here, path integrals, particular kinds and strange things, which is also the paper.
So we, which introduced, um, all this typology of particles and it kind of really, uh, formulated the free energy principle that way.
Um, so I think that's pretty much a very, very important paper.
And actually the one which introduced the notion of metacognitive particles.
So one of, uh, Lenz and Lars, um, this one towards the Bayesian mechanics of metacognitive particles.
The last one, it is actually a commentary, a short commentary, very easily readable of the path integral paper.
We just mentioned, um, and also I would say that in the 2022 paper, the free energy principle made seem simpler, but not too simple.
Uh, published in 2023, actually.
Uh, it is mainly, it mainly focused on the state-based formulation, but it's, it also, uh, talk about, uh, paths and generalized states.
Um, so it, it, it's, uh, also a very nice, um, very nice papers and it kind of derives the whole thing from scratch.
So I think this paper is also very, very important.
Um, and yeah, I think basically in the last two or three years, there have been many papers, uh, reformulating the free energy principle or grounding it in, in, in, in solid math and so on.
So it's, I think currently, and let's say the, the few years, which followed from the 2019 monography of Carl Freiston.
It has been very important.
Yes.
About, uh, when it comes specifically to Bayesian mechanics and the actual physics underlying the free energy principle.
Thank you.
Yeah.
I'll just restate that.
I think there's a few great points to explore.
So even as early as the early two thousands, there was the notion that there was like physics of consciousness, physics of cognitive systems, a free energy principle for the brain.
There were physics based equations in the 2010 Friston paper.
There's a big tree with all these different inference algorithms.
However, they were all just kind of branches on that tree, little bit more evocatively or, or aspirationally, but not formally.
Then dot, dot, dot, dot 2019 free energy principle for a particular physics and the reading group and all the work around that.
And then, especially in the last year since then, um, I think that the, the decision and the move that you made to lead with the state based.
And then almost nothing had to be said today.
Of course, it was a great presentation, but you said it all that we point to find the path.
We make paths into points in a given space.
Um, and so I was thinking about like being in a car and then there's one path where like my first derivative is one for two seconds and then it stops.
And then that was that path.
And then there's another path where my first derivative is one for four seconds.
And then I stopped.
And so all of those different paths, which do take the car to different locations, they are also just points in this generalized space.
And then there's this interpretation of those coefficients as the Taylor series expansion, but it just shows how versatile the formalism is because it can take points in arbitrary state spaces, which means, yes, you can imagine arbitrary state spaces that correspond to Taylor series expansions or potentially other kinds of constructs.
What do we get from paths?
So in fact, I think there are, um, a couple of things which, uh, motivated such a formulation because when, uh, I mean, about the usual, uh, state-based formulation.
We talked about last time, there was, uh, many critics, many, I mean, it was, there was many debates, for instance, about the question about the nest density being a steady state.
Is it really, uh, relevant when it comes to real system to real biological systems, for instance?
So there was many, uh, things which are now, um, addressed by the path-based formula formulation.
Uh, because as we saw, we relaxed a couple of hypotheses.
And also the second thing, which is very, very much at the core of the path-based formulation, as you said, is, I mean, the, the, the fact to move from, um, states to path, to path, which are in fact encoded by generalized states.
It allows you to, to, to, to speak of the future, uh, to the, in, to speaks to the future path, so that you can develop a physics of particles planning, for instance, which was not at all, uh, the case with the previous formulation.
So having such extension of the scope of the free energy principle, it allows you to, to literally describe the Bayesian mechanics of particles planning.
Uh, and, and so it's, the fact to think in terms of path as opposed to states, it allows you to develop a physics of, let's say, higher order cognitive abilities, I would say.
Uh, so it's, it's, it's definitely very, very cool and, uh, uh, a great achievement.
Let's say.
Responding to that.
Um, I would say planning is possible in the state-based formalism.
It's just more of a brute force tree branching engineering problem.
So it's almost like in the state-based formalism, there was a physics of the perception action loop.
And then there were classical computer science ways to deal with the branching of planning, just like a chess algorithm, like how many depth deep in the time horizon.
And then there's all these secondary strategies for branching, uh, and pruning that search tree.
But there's kind of like few to none in terms of the guarantee of the, um, time horizons of policy.
You just kind of had to enumerate all the possible options.
Um, but the real time kernel was physically grounded and beautiful.
And then planning had to be a little bit enumerated, but when we have the path as a atomic entity, um, then we can kind of extend the, the elegance or the simplicity that we were dealing with states in the moment.
But now our state in the moment is like a Taylor expansion.
And this comes up a lot in the distinction between the discrete time and the continuous time models, like figure 4.3 in the textbook, where in a discrete time model,
if you want to plan a hundred time steps in the future, there's some variable, you know, T sub 100, like you literally are making a prediction and, but you have no prediction for T sub 99.5.
You're just making discrete predictions.
Whereas a Taylor series, even a Taylor series for a super complex function, and you're only going to go two levels of differentiation in, you will have a prediction even for any points.
It might be radically wrong, but you get the whole support from negative to positive infinity, basically for free without guarantees of it being accurate.
But it's like, you've kind of pinned yourself to the timeline.
And then every single derivative that you take is giving you a better handle on that path.
For sure.
You'll never do worse.
And so that is like, so similar, yet also very different setting.
It's true that I said that the timescale considered was basically the correlation length of fluctuations on the number of the order of generalized motion.
But in principle, your Taylor expansion applied to, I mean, it's infinite.
But of course, above, beyond the correlation length of fluctuations, it becomes wrong.
And I also want to say about what you said in the beginning about the state-based formulation.
Yeah, it's true.
And actually in the papers of energy principle, simpler, but not too simple.
They, so you can write down the action of a path.
So here we have a Gaussian white noise.
Everything is, is, is, so we are really in the state-based formulation of the FEP.
You can write the action of a path.
And you realize that it coincides with an expected free energy as well.
So you don't need to be in the path-based formulation to, uh, go to, to, to get to the expected free energy thing.
Um, which equates the action of autonomous path or here in our path-based formulation, it equates a generalized Lagrangian of, uh, autonomous path.
So, so yeah.
Could you come back to where there was the generalized Lagrangian?
So this is a, um, okay.
Maybe a, uh, one before this.
Yes.
Okay.
Okay.
Thank you.
Yes.
Okay.
Thank you.
But those of us outside of the non-active physics world, how is action used?
What does action correspond to in physical systems when we're talking about action as generalized Lagrangian?
Is this the same thing as what we're talking about with policy selection and movement and embodied action?
How is this physics concept of action being used?
Okay.
So first of all, I would say that there is, I mean, it depends on what we're talking about.
Um, when it comes to actions in Lagrangian, we are, we usually think of, um, analytical mechanics, but here it would be more in the context of stochastic calculus.
And in the context of stochastic calculus and path integrals in stochastic calculus, the action is just a quantity which scores the likelihood of the path.
So if, for instance, the density of the path is, uh, the exponential of minus something, you would call by identification, this, uh, thing, the action.
And basically the smaller, the action, the more likely the path, because the higher the density of your path and vice versa.
So, by the way, when we were saying, for instance, here that the action is equal to, I mean, we define it as negative log density of the path.
In principle, if the density, I mean, when it comes to the usual definition of the, of the action, if I write my density as a normalization factor times the exponential of minus the action.
Then, if I take the negative log density, I would have the regular action plus something.
And usually this, uh, constant is, this is, this guarded.
We, um, we just don't consider it so that the action reduces to negative log density of a path.
But conceptually speaking, this action is very different from the idea of Lagrangian because basically the act, I mean, usually speaking, the action is the integral over time, over your path of, um, of, uh, a quantity called the Lagrangian.
So at every point in time, there is a quantity defined, and this is the Lagrangian, which is defined at any point in time, while the action is a quantity which characterizes path as world thing.
So conceptually speaking, actions in Lagrangians are very different things.
Lagrangians, once again, are defined at any point in time, while the action is the quantity.
Lagrangian was defined at any point in time, while the action.
Okay, I'll wait a few seconds for Richard to rejoin.
If you're watching live, please feel free to write questions in the chat and we'll look at them.
We'll look at them.
You're back.
It's all good.
Yeah.
Lagrangian is defined at every point in time, and then the action.
Yeah.
And basically, um, so in order to just, uh, answer what you, well, uh, here.
Yeah.
When you said that, is it different from the notion of action when in the active infrastructure, for instance, and so on.
Here we use the word action, uh, but it has nothing to do with the notion of action, like acting in the world, etc.
So yeah, for the people who never, um, meet this concept.
So it can be super confusing.
I guess when you, uh, when he, when you read patient mechanics papers, you, you don't really know what action is, uh, we are talking about.
But yeah, they are very different.
I know it's funny.
Like each path has an action value, the negative log density that in a way summarizes what we could say are the actions that that path entails.
But yet the actions are the affordances that are taken on that path that are summarized by the physics action.
Um, so there's, yeah.
Um, also, yeah, very, um, cutting edge with reviewing the typology of particles and the DaCosta and Sanved Smith metacognitive particle.
Um, that shows, I think a few things.
One that often there are implicit concepts and qualitative concepts that are built up.
Like long have people said that there is a continuity of modeling between rocks and societies, for example, popes and plaintiffs and plankton, all these other funny things that, that Fristin et al say, but not until this paper.
Um, did we see the simple, the conservative and the strange.
And then with that target article, just with the DaCosta and Sanved Smith work, they kind of take that in another level and like compose off to the side.
And now we can go into a metacognitive depth, combining back to like the hierarchical nested meta awareness work of Sanved Smith from 2021.
So it's just very cool how there's like a kind of earlier first pass qualitative intuition.
And then the empirical research question is like, where can we build the high speed rail lines?
And this is like the blueprint for the high speed rail now.
And then the next level will be like actually making the simulations or whatever it is to kind of show that this is not just something that you can make in PowerPoint.
But this is actually something where the rabbit is going to be evincing some kind of behavior that it couldn't otherwise.
But it's kind of like, that's like, in a way, it's not the only way, but it is like an agenda between the intuitive to the sketched.
And just it builds forward in these ways that are being reviewed pretty clearly and changing on a month by month.
Yeah, and I think I mean, this agenda of translating concepts like cognitive abilities and stuff in simple physical terms is quite interesting.
And I mean, we discussed it on by message on Discord, but it's it's it would be cool and it's it's coming, it's happening, but it's it could be cool to for this patient mechanics, this field to be more known and recognized by the physics community.
Because if you meet like regular physicist working, for instance, in the physics of complex systems or in biological physics or biophysics and stuff like that.
It I mean, you have like a 0.999 probability that he never heard of Bayesian mechanics.
While we have a world agenda to to to to to to following is that I think there is way more to to be done.
It's like the the down of this field of this agenda, let's say.
So I think the next years are quite exciting in that regard.
I totally agree, like one meme or theme on that for me is like the base graph on the screen on the table.
It is what it is.
And then there's the second level where we annotate or assert that graph with cognitive phenomena like, well, this graph.
Reflects attention or awareness of attention or metacognition or regret or whatever we're modeling.
We kind of make an assertion about the base graph.
And like you said, it's the dawn.
This isn't the answer on metacognition.
This is like one very snappy, very following in line way of modeling metacognition.
Yeah, there is no end.
There is no end to that question of how do you model metacognition?
And so then it's just like every time in a psychology paper or any we see like a cognitive phenomena, which can include everything from anticipation, you know, past, present, future.
That's like our keyhole to bridge with this generalized unifying perspective on cognitive systems.
Yeah, I totally agree.
This work is really, this work here on the slide is very like a first work.
But I mean, when it comes to metacognition, for instance, I mean, I'm not an expert at all, but there are many concepts.
I don't know, mental actions, cognitive effort, whatever.
There are many things, many layers.
And the, I think, like translating all of these concepts of these phenomena processes, whatever, into natural Bayesian mechanics is really like what's coming in fact, I think in the next years.
So, and yeah, we'll see.
And, and as you said, beyond the analytical work, there is also the simulations, worked examples, whatever.
So, yeah, I think there are many, many works to, to be done and which are coming in the, in the next years.
I totally agree.
Yeah.
A kind of analogy that brings to mind is like early in the periodic table, not saying that we're studying, but we're not going to be able to do that.
Not saying that we're studying material phenomena or even like elements or material phenomena, but it's kind of like, well, the rabbit has vision, taste and hearing.
So if we've identified a memory in vision and taste, there's like a missing element for maybe it's not there.
Maybe the memory for hearing is zero, or maybe it's something very complex, but it's like, but there's a space there.
It's like, there should be a rare earth metal in the fourth row.
There should be an attention variable on this.
And so it's kind of like a higher dimensional periodic table where, because we know about certain patterns that are either kind of convergently arising in the real world because of what is life.
Or they're convergently arising because we choose to model things a certain way.
So then that brings a huge amount of concordance and juxtaposition, like to the field of chemistry.
Whereas previously there might've been air chemistry and water chemistry and fire chemistry.
And then there'd be like, oh, but what happens when you throw water on a fire or what happens when the air in the room burns out?
There'd be like these edge cases where it's like, oh, we don't do that.
But that's what's happening when we don't have the unified model for cognitive systems.
People will kind of study one phenomena or character of a system to its limits, but the limits of any phenomena in our highly woven life forms, like you don't chase it to the end.
If you're studying foraging in the ant colony, it's not like there's a, okay, that was the end of the rainbow.
So foraging is over.
Foraging is over.
It's like, oh, well, foraging is related to nursing.
And then that's related to this and the weather.
It never just simply terminates with the inquiry.
And possibly that could reflect the extremely early stage of this formalization.
Possibly there are fundamental unknowns and adjacencies in our epistemic situation.
Yeah.
And I think, I mean, a few years ago, the idea of kind of extending physics to, in order to have an actual physics of cognition, it would be like crazy, like the Holy Grail.
And the fact that we have these early works is quite an achievement.
And I would also say that what's interesting here is that we already do have formal models of many cognitive phenomena.
For instance, you were talking about the paper of loss about metacognition.
So we have very precise and formal active inference models, for instance, of many different phenomena like metacognition and so on.
So in a way, we kind of already know what we should end up with.
And the idea is how to do, how to play, for instance, with the sparsity within internal states in order to go to get back to re derive or refine what people are already modeled in a different literature earlier.
So that's kind of the dynamics, I think.
So yeah, we'll see in the next year how it goes.
Yeah, that's a great point.
A few more thoughts on that.
Like a lot of the adjacencies and generalizations, mathematicians and physicists and statisticians, they're experts in this.
Like if it was a fixed number, see if it could be variable.
If there wasn't a variance, see if you can add a variance.
If it was this kind of distribution, swap it out for like, there are these kind of syntactic moves that barely require much more than just like, yeah, these are the swaps.
We make like this is what it looks like to generalize a theory.
It's like we could add a variance on it, you know, all.
So those kinds of familiar moves.
And then so much can be explored on this topic.
But when we think about a physics of cognitive systems or a physics of cognition, sometimes I feel like I have one foot like is it's like I'd or somehow trailing with the reductionism.
Like it's hard to escape the material basis.
And it's also not clear if we want to escape the material basis because of physics of cognitive systems.
On one hand, it might address this kind of like thermo, info, negantropic, Schrodinger, what is life question about persistence and order of kind of quasi crystals.
So, or leave all that mess separate mess and beauty.
The pure Bayesian mechanics, if we just say, okay, now we're in the map, we're leaving the territory behind.
We're not going to talk about the actual calories and the thermodynamics.
We're just on the map and a massive prior with a little attention is like a piece of sand hitting a mountain.
And a very loose prior with a highly attended to data point is like a bowling ball, you know, smashing through a small little heap of sand.
So, it's like there's a physics to the collision of incoming data and prior, which is the Bayesian setting.
So, it's interesting that there's a sort of map, Bayesian mechanics, that kind of non-controversially describes the collision of priors of different mass in a way.
And then the tantalizing question or connection is whether that is like one in the same or an enabling factor or a downstream factor of this actual thermo-informational autopoiesis for living systems.
If I may add something, I think here, I mean, an interesting point is that if you have, for instance, I mean, I don't want to go there really, but if I have a software which can be implemented by many sort of hardware, for instance.
And this idea was actually a lot debated when it came to functionalism and stuff like that.
But anyway, here, such Bayesian mechanics, in a way, it's the physics of how the overall system should behave.
So, there is, for instance, the minimization of this free energy functional, but we are not saying how the...
Here, we do not explicitly say how the system actually does the computations.
We just say that a sparsely copper random analytical system has somehow to do that stuff.
And in a way, it is neutral about what the actual system is made of.
It's like when we say that the free energy principle is more a framework than a process theory or stuff like that.
But, I mean, I don't know very much about these questions.
I think that's a great point.
It's like that's why a program or an operating system can be run when a different processor is brought in, just within a kind of classical computing setting.
As a cognitive mapping or cognitive modeling framework, like, we don't know if that rabbit is a real biological rabbit.
That rabbit might be a deepfake rabbit.
And we're interacting with it through a video channel, and we think that we're doing behavioral research on a real rabbit, but it's just a really convincing synthetic data rabbit.
We don't know because we're only getting the observations that we're getting, and then we can tell any number of possibly compatible stories or interpretations about the data we're getting.
And to say more or to go further, like, that's stepping past the boundary of the actual observations we're making, which is great.
Like, we want to propose hypotheses for what we're not directly observing.
That's the whole point of latent states and everything.
And yet there is this line where it's like you can kind of falsely push the known knowns beyond where they really are.
And it seems like one example of that is going down and specifying the actual mechanistic basis of a given computational function.
And that that's, if that's important to specify, then the work itself is to specify it.
However, at the framework level, the framework's absence of that kind of a material substrate, like, that's the feature.
That's not a lacuna in the framework.
That is like, there's the USB stick, and then there's where you can plug it in.
That is the plug-in to any system.
And if there was something already pre-plugged in there, like, well, it has to happen on Turing computer, or it can't happen on Turing computer.
That would have just hobbled the scope of applicability by welding together what doesn't need to be welded.
And I mean, if anything, this is a journey and a challenge about proper articulation and about how sparsity and nuancing, which are connected to what, brings us cognitive phenomena.
So it's like, many things to learn and reflect on.
Yeah.

And if I may add a related remark about the question of having a top-down approach, as opposed to bottom-up approach.
I think, sociologically speaking and historically speaking, it's very interesting that the people who started developing Bayesian mechanics are people who are not, like, supposed to be professional physicists.
Because I think, when it comes to super-emergent kind of phenomena, like cognition, whatever, the people who were training is precisely to learn about cognition, about agencies, the people who kind of know everything about what it takes to be an agent and so on.
These guys are neuroscientists, basically.
So they, because they know what agency entails, they can be the good ones to propose an actual Bayesian mechanics, which is a very top-down approach.
Whereas, if you go to the labs in physics of complex systems lab and stuff like that, people are pretty much bottom-up.
They will, for instance, oh, I want to study the brain, so I'm going to write down the upfield model, for instance.
So a kind of Ising model, where up is an activated neurons and down a non-activated neurons.
And so I will have this very, this very much bottom-up approach, and I can, which is super interesting and super important.
But when it comes to this very much emergent behavior, the very emergent phenomena of the brain, metacognition, blah, blah, blah.
I can study for like five centuries the upfield model.
I will never get any insight about the emergent behavior of the brain.
And so I think here, you have to have a top-down approach.
You have to write a very generic Langevin equation.
And because you're a neuroscientist, and because you know what it takes to do an inference, to be an inference machine,
you're like, ah, conditional independency is very different, is very important, sorry.
So let's try to inject in my Langevin equation some level of sparse coupling.
And then, boom, you have the free energy principle.
So even though, sociologically speaking, what's happening here might be super weird.
Like, these guys are not supposed originally at least to be physicists, and they are supposed to, like, kind of generate the next chapter of physics.
How weird is that?
But in fact, in fact, I think there were precisely the good people to do that.
So yeah, it's quite interesting.
I think there might be, oh, that's a great point.
There might be a fun history with physician, physician heal thyself, and the alliance of medicine and physic.
That's one point.
Another point is low road and high road.
And sometimes the disciplinary or the in-group conversation is, like, very low road.
And then the idealistic and aspirational is, like, high road.
It doesn't exactly map to those, but I'm thinking of, like, somebody says, like, I want to drive somewhere.
I want to travel somewhere.
There is no material basis for that travel yet.
They're not there.
There's no path.
There's no car.
Again, in the mechanic shop, it's, like, we have this tool, this object, we're so surrounded by the low road that it supports this incremental research agenda using the tools and approaches that we have and their materiality.
Whereas someone from outside the field comes to the ant researcher, it's like, have you had the ants build this new thing?
And it's like, well, we weren't even on that path, but now that's like a new North Star and that can now draw work in that direction.
And so it's kind of like the low road building out and then like the kind of the draw of the adjacent possible and the imagination that the high road kind of grounds in.
All right. I'll ask a question from the live chat.
Susan asks, what can one equation contain?
I'm imagining how to interpret and translate self-modeling, how to approach foraging resources and opportunities.
Can you repeat, please?
Yes. It's an open-ended question. So feel free to however you like.
What can one equation contain?
I'm imagining how to interpret and translate self-modeling, how to approach foraging resources and opportunities.
So I could not answer the second part of the question, but if I can pick up on about the question of what these equations are all about, which is a bit what you asked last week, like what works, does the framework do, what these equations contain or whatever.
If you actually simulate a sparsely coupled random dynamical system.
And actually there are already are examples out there, for instance, in the 2021 paper called Stochastic Chaos and Markov Blanquets, if I remember well, with Thomas Pohr and Carl Freesten and others.
They simulate a sparsely coupled Lorentz systems, if I remember well.
And if you do simulate such systems, which verifies such sparsely coupled architecture, you observe the behavior which is described by your equations.
And if, for instance, you remove fluctuations on particular states.
So, well, your simulation, which follows the path of list action, which is given by your equation.
So it's it's it's it's it's it does really work in the sense that it does describe indeed something.
It's really a physics, in fact, of such sparsely coupled systems.
Great question.
I think we can explore more on what an equation can contain.
But I'm just kind of struck by that.
There's like a latent large set of.
To be clarified, axioms and conclusions and so on.
And when we see like one equation written here, it's kind of like we're just seeing like one glimpse or one facet.
It's not like the other equations aren't in effect, but sometimes it's a little unclear which equations are relevant.
But in an equation.
And.
We see a symbolic expression.


Within a given quantum reference frame.
Other.
Otherwise, the Q and the A wouldn't mean anything like within a semantic reference frame.
The equation is just kind of like a check.
It's like if it's like it's there's probably many ways that we can kind of explore what it does.
But it's true that, I mean, I think many peoples who.
In addition, don't necessarily have a mathematical background or whatever they have been.
I mean, I'm not an expert in the history of the free energy principle, but a lot of people have been confused, especially in the early steps where it was.
As as Lance say it many times worried when it was even more nutrition than solid framework properly grounded in solid math.
So people.
Did get a bit confused, I think by with the math, but now it's we have more and more worked examples simulations.
Solid math, etc.
So it's it's quite quite nice.
Okay, in closing, we have explain it like I'm a 10 year old.
Now that that response may reveal more about what somebody thinks 10 year olds are like.
But now that we've been on this two part journey.
You know, dot zip it and close it, Richard.
So explaining you mean about what I just said like before.
So just both sections or just our whole projects.
Now that now that we can look back at all the incredible quality summaries that we've provided.
How do we just cap it and move forward with a child?
Yeah.
So I think everything we did here.
So both in this presentation and the previous one is.
So basically, we can.
So if I, I, I would.
So in order to say it in the most intuitive and simple ways, I would say that.
Very simply put, a system is just.
It's just.
It's just some things interacting, let's say.
So it's literally corresponds to a system as we use this for you know, in a daily basis.
Pen is a system.
An organism or any piece of any collection of things interacting with each other.
So I can say this is a system.
I just have to precisely delimitate and say what are the boundary of my system.
And given a system which has a certain dynamics, certain laws, physical laws telling you how your system behave, how the things move around and so on.
And now, so my system can be alone, like an asteroid in space, let's say, or it can be connected to each, to other things I recognize as other systems.
Two things can collide to different things.
Systems can collide with each other, etc.
For instance.
And now, if I assume several systems which are connected, meaning that they causally interact with each other in a certain sparsely way.
So basically, in my schematic, you would have, for instance, a system on the right, a system on the left and a subsystem in the middle.
So you have many subsystems causally interacting in a sparsely way.
For instance, mu doesn't interact with eta.
If I take a bacteria, for instance, it does move around and interact with other things outside the bacteria.
But at the same time, within the bacteria, under the outer membrane, there is also stuff which do not interact, cause they interact with the outside, let's say.
And so if you have such sparsely coupling architecture, as we say, and in a more technical term, we would say that the inside is independent of the outside when conditioned on the intermediate system, let's say.
Okay.
So if we have such sparsely coupled system, we see mathematically speaking, we derive the fact that your system has to behave in a certain way.
And in fact, when you do have such sparsely coupled dynamical system, you realize that everything appears to, I mean, if you look at, for instance, internal states mu here, the dynamics of this system can be interpreted in terms of Bayesian inference, meaning that this system can be viewed as encoding a density over its external states, for instance.
And if I had to define in a very simple way, what it means to parameterize or to encode a distribution, I would say that the various parameters which define your system, for instance, I said earlier that a system could be anything.
A pen, a pen, an asteroid, whatever, there are variables which specify its state, for instance, temperature, pressure, shape, whatever.
I have a set of variables.
I can view these variables, these numbers, literally, as I can take them and manipulate them as parameters of a mathematical quantity I can deal with.
And yeah, so I'm not sure if I failed in trying to put it in a very simple terms, but I hope it makes sense.
It was awesome, Richard.
Thank you for working to bring us these twin gems in the distillation work and really helping consolidate and sediment on one hand, a long history of dynamical systems and physics.
And on the other hand, papers coming out two weeks ago as well.
So hopefully we'll continue the adventures and see you around.
Yeah.

And thank you for the chat, the questions on the chat.
Cool.
Peace, everyone.
Bye.
Bye.
Thank you.
Bye.
