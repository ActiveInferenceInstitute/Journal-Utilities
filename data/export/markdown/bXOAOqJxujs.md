---
title: "ActInf MathStream 008.1 ~ R Servajean: Intro to Bayesian mechanics: state-based formalism (part 1)"
category: "MathStream"
series: "MathStream_008"
episode: "1"
speakers:
  - "R Servajean: Intro to Bayesian mechanics: state-based formalism (part 1)"
duration: "1:24:04"
url: "https://www.youtube.com/watch?v=bXOAOqJxujs"
views: 723
exported_at: "2026-02-18T22:37:37.857998+00:00"
format: markdown
---

# ActInf MathStream 008.1 ~ R Servajean: Intro to Bayesian mechanics: state-based formalism (part 1)

Hello and welcome everyone. It's January 26th, 2024. We're here in Active Inference Math Stream
8.1 with Richard Sarajevon. And we're going to have an interesting presentation and discussion
today on Introduction to Bayesian Mechanics, Free Energy Principle, and the State-Based
Formalism. This is part one. So Richard, thank you for joining. Looking forward to this presentation
and discussion. So to you. Hi everybody. So yeah, my name is Richard Sarajevon. I'm French working in
Switzerland. I'm a PhD student at EPFL in Lausanne. And just to bring a bit of context, I'm not working
on Bayesian Mechanics. We are, we do have a physics background, but we are interested in
modeling bacterial evolution and ecology. And what happened is that something like, I mean,
the free energy principle was always in the corner of my head. And one year and a half ago,
I decided to really read about the free energy principle, especially if I wanted to transition
to the field and I do want to transition to the field after my PhD. And so I started to
ask many questions to the people from the FEP community. And I'm so grateful. Thanks for
them. And also on the discord of the of the Active Inference Institute. And at some point,
I said that I was preparing a lab meeting about the free energy principle. And Daniel proposed
to have this discussed on the live stream because there isn't such material to specifically learn
about Bayesian mechanics and the actual physics underlying the free energy principle. And so
here I am. So once again, I'm not an expert on the matter. So always refer to the original
papers. But hopefully I'm gonna I'm gonna do a decent job. So without further ado, let's let's
start. I'm not going to tell you what we where we are heading what questions we would like
to to address or whatever. I'm rather going to start building the framework right away.
And at some point, what we're doing doing will become clear. So as you may know, there are
two formulations or formalisms of the free energy principles, the so called state based formulation,
and the so called path based formulation. So today, we will focus on the state based formalism.
It's not like the old versus the new formulation. In fact, thinking in terms of path, or so called
generalized coordinates of motion, I've been around forever, but in the literature, but
it kind of came back to the front scene of the Bayesian mechanics literature, I think. Anyway,
today, we will focus on the state based from formalism. So the very starting point is to write
down a large my equation, a generic large my equation. So it's literally like saying, let's consider
a random dynamical system. Very briefly for the people not acquainted with such an equation.
X here is the state of your system. So it could be a simple scalar if you are considering a one
dimensional process. But in general, X would be a vector. For instance, if I don't know, you
want to model the 3D diffusion of a Brønian particle immersed in a liquid, X would be a 3D vector,
whose components are the coordinates of your Brønian particle. And you can see on the left hand side,
that we have dx over dt, the time derivative of the state vector. So that such an equation really
describes or specifies the dynamics of the system. So many things can influence indeed the dynamics of
the system. If I stick to my Brønian particle example, maybe it is subject to an external force.
So whatever is relevant here, you put it in F, the so-called deterministic term or flow. We will refer
to it as the flow for the presentation. However, in some cases, there is stuff you don't want to
explicitly model. For instance, if I stick with my Brønian particle example, it is constantly hit by
the molecules of the medium surrounding it, hence its Brønian motion, right? And it would be,
so if you want to take into account these thermal fluctuations, it would be mission impossible to
explicitly model every single molecule of the millions, if not billions of the molecules
surrounding it. So a convenient way to still take into account these fluctuations, which are literally
thermal fluctuations in my example. A convenient way to proceed is just to add a noisy term to the
equation. So Omega here is a random variable, which value changes with time with the appropriate statistics.
Okay, so two brief remarks before moving on. If you assume that the state of your system changes slowly
compared to the time relaxation of your fluctuations, you can write the autocorrelation function of the
fluid of the noise like that, where gamma is the diffusion matrix and delta is the delta Dirac function.
So what it means, it's just that in that case, your noise is super rough and it's not correlated in time, basically.
Also, second remark, you can, I mean, you can use the central limit theorem to argue that
that it is that that it makes sense to assume that omega is normally distributed. So that in the end,
the noise is a Gaussian white noise. But note that in the next live stream where we will
discuss the path based formulation of the FEP, we will relax the white noise assumption. Anyway,
the flow F is a vector. It has the same dimension than the state vector because each component of the state
vector has its own Lagrange equation, if you will. And you can decompose it into a solenoidal and a gradient
of the same direction. So, we will be able to see that in the second term. So, before telling you what this decomposition is all about, on a technical note, just notice that first Q here is the so-called solenoidal matrix.
Gamma is the diffusion matrix just as before. And the I here, with the Nabla I, this I of X here,
is a negative log of a density. So, it's a self-information or surprise. We will refer to it as a surprise throughout the presentation.
And the density at play here in this negative log density is the steady state or NESS for non-equilibrium steady state
density of the system. So, we assume that there is such NESS density that exists so that if you, from a given initial
initial state, you let your system evolve, it will reach at some point unique, well-defined NESS density.
And second remark before telling you what this decomposition is all about, note that usually in the papers, the divergent terms here and here are put together
on a, in a third term, which is, which is sometimes called the housekeeping or correction term. But actually, if Q and gamma are not state dependent,
these divergence terms vanish anyway, and we end up with the two remaining terms, which can be nicely factorized like that.
Also, a last thing I want to say is that if you, you consider the solenoidal term, the first term,
the first term, it is indeed a solenoidal term, you can indeed write it as the rotational of some potential.
I'm saying that because sometimes people get confused when they see a gradient in both terms.
Anyway, what this decomposition is all about is quite in fact simple. Let's consider this nice 2D
single modded NESS density. Okay, so the flow, and more specifically, the gradient component of the flow,
which is here, the vertical flow, will drive the system towards its mode while fluctuations kind of push it away.
But it's not the only flow, there is also the solenoidal flow, which is here,
the horizontal flow, which will make the system kind of converge to its mode in with ever decreasing cycles.
And so if you want to get some more intuitions on this solenoidal flow, what we can do is to remove the fluctuations.
So all the entries of gamma, the diffusion matrix, go to zero. And this means that we would not have any gradient flow anymore,
we end up with only the solenoidal flow. And if we do that, the system will just follow an isocontour circulation on the NESS density.
That's the bottom right panel here, where the solenoidal flow kind of drives the system on this circulation here.
So a small remark about this solenoidal flow, because it kind of drives the system in this simple example,
in either clockwise or anti-clockwise direction, in an irreversible fashion, irreversible in the statistical physics sense.
So it breaks detailed balance, and so on. People sometimes view this solenoidal flow as underwriting the symmetry breakings ubiquitous in living systems.
Anyway, okay, so before using this decomposition of the flow to do some cool stuff, I need to introduce some stuff.
So I will have to go through a couple of things, of notions, one after the other.
And afterwards, we will put everything together and actually derive the free energy principle.
So the first thing I want to introduce is the notion of sparse coupling.
So let's say that in my state vector x here, I have a subset of variables, this mu here we refer to as the internal states.
And they specify the state of some subsystem called mu.
So I mean, you get the idea, the idea is that we have like an organism, an agent, the bacteria in my schematic.
And these variables here literally specifies the internal states of my bacteria.
And this bacteria is in a given environment, niche, whatever.
So there is this other subset of variable we refer to as the external states, and which corresponds to the external world, the external states of the bacteria.
And the idea here is that these two subsystems are not connected to each other.
So when I'm saying that two variables are not connected to each other, I just mean that their respective flows do not take the other one state as arguments.
So they do not influence each other, basically.
In fact, they are indirectly connected to each other, thanks or through a third subsystem we refer to as the Markov blanket, so that these guys here are called the blanket states.
And we will see in a minute that it really corresponds to a Markov blanket in a statistical sense.
So we have this architecture, this path coupling architecture here.
And in fact, we can even go a bit further and assume that within the blanket, there are two more systems, the so-called sensory states and the so-called active states A.
So basically, the idea here is that the external states A, they influence the sensory states S, and these sensory states S influence the internal states mu, but not the other way around.
And the internal states mu, they influence the active states A, which influence the external states A, but not the other way around.
So it's really a sparse coupling architecture inspired by the so-called action perception loop.
However, you could ask questions like, why do the sensory states influence the external states?
Or why do the active states influence the internal states, etc.?
So we don't have really time to discuss this.
I guess you can think of some qualitative example in biology.
But I just want to point out that even though this architecture is quite canonical, it's not a definitive feature of the free energy principle.
And in fact, in the next time when we will discuss the other formalism, we will do a bit of zoology and we will look at other sparse coupling architecture.
Okay, so on a technical note, just notice that such sparse couplings are encoded by zero entries in the Jacobian matrix of the flow.
Anyway, so thanks to this sparse coupling architecture, we have this system of four coupled Langevin equations, which respectively describes or specify the dynamics of the external states eta, the sensory and active states S and A, and of the internal states mu.
Okay, so I want to say here about the Markov blanket thing that under some conditions, I'm not going to discuss here.
So for the people acquainted, it involves having no solenoidal couplings between autonomous and not autonomous states.
But anyway, I'm not going to go into this.
Let's say under some conditions, the external state eta and the internal states mu are conditional independence.
So they are independent when conditioned upon B, which makes sense because all the information kind of transit through B.
However, note that when I'm talking about conditional independencies here, I'm talking about conditional independencies in the stationary density.
So basically, if you fix P and you have this joint conditional conditional stationary density here for Xi and XJ,
if these two guys are conditional independent, it just means that you can write this joint density like that.
And so that such conditional independencies are encoded by zero entries in the ASEAN matrix of surprisal.
Okay, so now just a bit more of vocabulary before moving on.
Note that if we put together A and mu, so we consider the couple active states and internal states, we refer to these guys as the autonomous states alpha.
And the cool thing about the autonomous states A and mu or alpha is that they are conditionally independent of the external states.
So autonomous and external states are independent when conditioned upon sensory states.
And if you add the sensory state S to the autonomous states, so you consider the whole thing, the whole Markov blanket and the internal states,
we refer to these guys as the particular states pi.
And pi constitutes a particle, a particle in a generic sense, of course.
So an organism, an agent, whatever, a bacteria in my schematic.
Okay, so here I just want to make a point to make a bit more clear what we are doing, what this approach is all about.
So basically here we kind of define what it means for something, a bacteria, whatever, to exist in the sense that it has its own internal dynamics statistically separated from the external.
It does have a mark of blanket, it does have its own physical integrity.
So we have no clue of how it maintains indeed its integrity in the sense that if you're considering real systems like an actual bacteria or a human being or whatever,
it does survive in a given timescale.
Right, for instance, this playing, I don't know, like active processes, contouring dissipation, for instance.
Here we don't say anything about how it does survive.
It just does.
We do have this sparse coupling architecture.
And from there, from the starting point, we are going to derive the necessary consequences of such sparse coupling.
So basically, we kind of ask or answer to or try to answer the questions, if things exist, what must they do?
And so if you're a bit confused, don't worry, we're going to go back to this idea later.
But I just want first to show you this quote here, which tells you many theories in the biological sciences are answers to the question, what must things do in order to exist?
The FEP turns this question on its head and asks, if things exist, what must they do?
But once again, we are going to go back to this idea later.
But that's kind of the idea of this approach in a nutshell.
So as I told you, I still have a couple of things to present.
So I will have to go through each of them one after the other.
And finally, we will put everything together.
And finally, derive the free energy principle.
So the next thing I need to introduce is the notion of synchronization map.
So very, very generally speaking, I'm not specifically here talking about our random dynamical system.
If you have a linear map, G mu here, which gives you mu from B, and G eta here, which gives you eta from B, then if G mu here is injective, so that basically you can go back to the pre-image from the image, you can use the pseudo-inverse of G mu.
So that from B, you can go back to the mu, and from B, you can go to eta.
So the successive application of the pseudo-inverse of G mu, and then of G eta, is called the synchronization map.
And it basically allows you to directly go to eta from mu.
Okay.
So now let's try to use this idea in the context of our system.
So B here corresponds to the blanket state.
So if I fix the blanket state, I have a corresponding conditional densities for mu and eta.
I have P of mu given B, and P of eta given B.
And their modes are bold mu and bold eta.
So in virtue of this synchronization map, I can go back to the external mode from the internal mode, thanks to, once again, this synchronization map here.
And I'm going to give an example in a sec, which is going to clarify a bit more what we are doing here.
But first, I just want to say that in this nice paper by Lenz da Costa about this synchronization map, basically everything was Gaussian.
But sometimes, I mean, if it is not the case, a Laplace approximation, which is literally a Gaussian approximation, might be necessary to derive a synchronization map of closed form.
But don't worry, we will go back to this idea of Laplace approximation later.
Just remember that we have this synchronization map here, which allows you to go to the external map, external mode, sorry, from the internal mode.
So for instance, if given B, given the blanket state, the corresponding P of eta given B follows this nice normal distribution where bold eta here corresponds to the mode.
So then, in virtue of the synchronization map, I can view the internal mode mu as parametrizing a density.
I write it that way, which is equal to this nice normal distribution, where the mode is just the synchronization map applied to the internal mode to itself.
And by construction of the synchronization map, it is equal to the true external density.
So you can view the internal mode as parametrizing a distribution over external states, basically, thanks to the synchronization map.
That's why what the synchronization map is all about.
So just a small point, because maybe some of you are a bit confused here because we're talking about modes as opposed to actual states.
So we will talk about that later.
But indeed, I mean, if I take the actual internal states at a given time t, they are not necessarily equal to their modes just because of fluctuations or whatever.
So that if I apply the synchronization map on the actual internal states, it might not give you the true external mode.
But anyway, we will discuss this a bit more later.
So that was the notion of synchronization map in a nutshell, basically.
So last thing I want to introduce before finally putting everything together and actually derive the free energy principle is the notion of variational inference.
So very simply, let's say that you have some latent variables or hidden variable or some latent generative process.
So you have a prior P of eta over the state of these hidden causes of data.
And you are also equipped with a generative model, which just designates this joint distribution here, P of eta and S.
So you can view it as a model of how the latent variables cause the data.
So the idea is the following.
You sample some data S and you want to compute the posterior distribution P of eta given S.
So in a way, you want to refine your belief about the hidden cause of data thanks to a new sample data.
So it's very simple in principle because you just have to apply Bayes theorem, right?
So we need a method.
However, in practical settings, the denominator here, P of S, so the marginal density over sensory data usually requires a monstrous marginalization.
So it's just not tractable.
So we can't just apply Bayes theorem.
So we need a method which given some variational distribution Q, also called recognition density,
gives us, I mean, we want a method that makes it as close as possible, if not equal to the true distribution we want ultimately to compute,
namely P of eta given S.
And this two density, so Q, our variational distribution, and the true distribution P of eta given S,
are equal or are more or less equal if their divergence, KL divergence here is zero because this quantity here, the KL divergence,
basically measure the difference between two distributions.
So that's what I wrote here on the top of the slides.
Finding an accurate distribution Q in the sense of finding a Q as close as possible, if not equal to the true target density,
is equal to minimizing this divergence.
However, this divergence, I mean, there is the target density appearing here.
We can't do anything directly with it.
We can't compute it or whatever.
We need a proxy for this target divergence.
And there is a proxy called variational free energy F in green in my slide here.
So F is equal to this divergence here between Q and the generative model.
And the idea here is that you can decompose this divergence into the true, the target, sorry, into the target divergence in red here, plus something.
So it is indeed a proxy for the target divergence.
And note that, interestingly enough, the second term here is the surprise over sensory data or negative log P of S.
So that F can be viewed as an upper bound or lower bound, depending on how you define it, on surprise.
So what I just said here is that minimizing the target divergence just means minimizing F.
So that's basically what variational inference is all about.
And note that, usually, algorithms require Q to be Gaussian or require a mean field approximation or whatever.
And if Q is required to be Gaussian, even though the target density is not Gaussian, we would end up with the best Gaussian approximation of the target density, basically.
And in practice, it would mean working with a so-called Laplace encoded free energy.
Okay.
So before moving on, I just want to say that this quantity, the variational free energy, is in itself a quite rich and interesting quantity.
So you can decompose it in many ways, and each decompose provides interesting interpretations.
For instance, if you look at the second line here, you can see that minimizing free energy means maximizing this accuracy term here.
You basically want to explain the data, but at the same time, you want Q to differ the least possible from a prior distribution.
So that's an interesting quantity.
Anyway, now let's finally go back to our sparsely coupled random dynamical system and use everything we talked about.
And finally, let's derive the free energy principle.
So here is our system, and we have these four Langevin equations.
And the first thing to do is just to apply the decomposition we talked about in the beginning.
So basically, the flows of each of them can be written like that.
So I just directly applied the Helmholtz decomposition we talked about in the beginning.
Okay.
Okay.
So now let's try to understand how it works.
Let's talk about the dynamics of the system.
Let's say that there is a momentary instantiated sensory state.
And let's fix, let's say that the sensory state are fixed.
And there is a corresponding autonomous mode toward which the autonomous states are going to converge and stay in the vicinity of their mode, in the close vicinity if fluctuations are not too large.
Okay.

But in fact, sensory state with time changes so that the modes of the autonomous state move as well.
And in fact, it moves on its corresponding autonomous manifold.
So I'm not going to go into the details, but just have in mind that the autonomous mode moves on a so-called autonomous manifold, which can be viewed as a statistical manifold and which can also be viewed as a so-called center or center manifold.
So if I kind of rephrase what I am saying here is that the flow of the autonomous states can be decomposed into an off manifold flow and an on manifold flow, which corresponds to the path of the mode itself on the manifold.
Okay.

Okay.
So just to be a bit more clear, let's say in my bottom right illustration diagram here, the autonomous states are here.
And I'm interested in the off manifold flow.
So basically I have this component here, which corresponds to the gradient flow towards the manifold, towards the mode basically.
Here it's pretty much like what we discussed in the beginning.
And at the same time, there is here this orthogonal component, which corresponds to the solenoidal flow.
So that's basically the way the autonomous states are going to reach their mode here.
It can be viewed as this ever decreasing cycle towards the manifold on which the autonomous mode move.
Okay.
So that's a bit dense, I guess.
So I recommend to check the papers of free energy principle made simpler, but not too simple, which kind of discuss all this, this ideas about center manifolds and stuff.
So here, the interesting point is that if you assume a separation of timescale between the fast flow of the manifold, as opposed to the slow flow on the manifold, basically the autonomous state always are always in the vicinity of their modes.
And if you want to characterize the overall dynamics of the autonomous states, you can focus on the autonomous mode and the path of the mode.
And in the next slides, we will indeed focus on the autonomous mode.
And by definition, as we already discussed, the autonomous mode is or corresponds to the autonomous states, which minimize surprise here in the last two large-var equations, because the autonomous mode corresponds to the least surprising autonomous states.
Before moving on, I just want to say something we can maybe discuss afterwards because I'm not sure to fully understand.
But basically, if I'm here in my bottom right schematic, and so I have this gradient flow towards the manifold and this solenoidal flow parallel to the manifold.
And if I remove fluctuations, so the corresponding entries in the diffusion matrix go to zero.
As we saw in the beginning, it means that there is no gradient component anymore.
And what the system will be doing is kind of orbiting or oscillating around the point which moves on the manifold.
So that's interesting.
And I guess that if we do the exact same reasoning, but starting already on the mode, then the world flow reduces to the on manifold flow.
And I guess that in that case, the autonomous states follow and in fact coincide with their mode.
But anyway, maybe we can discuss about that afterwards.
So, okay, so let's use the various things we talked about, and especially the notion of synchronization map.
As we said, the internal mode parameterizes indeed a distribution over the external states.
So mu here parameterizes a distribution which by construction coincides with the true distribution P of eta given B.
And in fact, thanks to the conditional independence between external states and autonomous states, you can just drop the condition upon A and you just have Q mu equal P of eta given F.
And equivalently, you can write it P of eta given P.
And the idea here is that you can view Q mu as a variational distribution.
If you want, you can write its associated variational free energy.
So you have this formula here, the free energy.
And because Q mu is already coincide with the true posterior distribution, if you will, the first term here goes to zero.
And so that F here reduces, if you will, to the surprise over particular states.
And surprise over particular states, they appear here in the equations of the autonomous states.
So we can do this identification and we realize that the autonomous mode not only minimize, not only minimize surprise though, but free energy in general.
And the way mu, the internal states will be updated when the sensory states will change will always be so that this divergence here is zero.
So that mu is always keeps track or synchronize with or in fact infer the external states.
So that you can interpret that under a generative model, which is here P, the nest entity, the internal states can be viewed as performing inference over external states.
And so in fact, it's not only this divergence, which is minimized, but it's also surprise.
And it's not only, only the internal states which minimize free energy, but also the active states.
So let me give an example.
Let's say that the actual instantiated sensory states are likely sensory states or unsurprising sensory states.
And by definition, in general, the instantiated sensory states will be likely sensory states.
So mu will, the corresponding mu will be so that this divergence will be zero as we just discussed.
And at the same time, the corresponding active mode will be so you can see composition with the first term here, I of A given S and mu.
A, this active mode will just be the one the most consistent with this in intensiated sensory states.
And in fact, you can view it the other way around and say that the active mode is the mode which gives unsurprising sensory states.
So that the particle can be viewed as actively sampling unsurprising or likely sensory states.
Or equivalently, you can say that the particle kind of accumulate evidence for its own generative model.
And I'm going to say something about the generative model in a sec, but I just want first to, so yeah, this sentence here just sum up what we said.
Mu is updated so that q mu is always the best distribution of our external states.
And we refer to this as perceptual inference.
And the idea to, in addition, trying to minimize surprise for action is called active inference.
So a brief note, we said earlier that in order to have a synchronization map of closed form, it could be necessary to work under a Laplace approximation.
So that in that case, q mu is just the best Gaussian, for instance, of the target density.
So that's the divergence here would not be zero, but it still would be minimized.
So that the identification here between the two gradients still hold and nothing change.
Nothing changes with respect to our discussion.
So here I just want to say something about this, what we are doing here.
Basically, we assume that we have our agent or organism that survives indeed, exists or persists in a given environment, let's say, at a given time scale.
And we end up with the fact that our particle must be equipped with or must be must embody a generative model, which may or may not exactly coincide with the true generative process, and which encodes the causal structure of the world under which it tries to perform inference and to minimize surprise to perform perceptual and active inference.
But the interesting thing as well is that, and I think that's something fundamental that people tend to misunderstand.
And what we are going to understand is that, and that's something that we are going to do with the generative model.
And what we are going to do with the generative model is that the generative model also encodes the preferences of the system.
And let me explain why.
And let me explain why.
If I tell you that an organism manages to survive, to exist, to persist, etc.
And so it means that such an organism manages to stay in its homeostatic, life-compatible states.
You would be, of course, it almost sounds like a tautology.
Survive equals staying in its homeostatic states.
That's obvious, right?
And that's exactly what we are doing here.
We assume existence, survival, so that the likely state in which the particle will persist are preferred states per se.
So that, for instance, if I'm considering the prior of my generative model over sensory inputs, P of S, sensory outcomes as associated with high P of S, so likely or unsurprising sensory states, are preferred sensory states.
Hence, when I'm saying that the active states try to sample unsurprising sensory states, it means trying to sample preferred sensory states.
And so basically the particle appears to kind of actively accumulate evidence for its own existence in a way.
It kind of sample life-compatible data, if you will.
And that's exactly the definition of self-evidenting.
So I think we touch here something fundamental about agency is that agents are self-evidenting creatures in that sense.
Okay.
Anyway, so basically, I think that's the most interesting thing of the free energy principle.
We start from existence, and we end up that such a particle, which is coupled to the world in that way, must embody a generative model, which encodes the causal structure of the world, and which encodes its preferences in terms of what is life-compatible, if you will.
Okay.
Okay.
So just to sum up what we did here, this idea that free energy is minimized, you can write it that way.
And this is in a way a variational principle for self-organization.
That's a free energy principle.
So here I just wrote what we just discussed.
The agent keeps tracks and acts on its external milieu through perceptual and active inference.
And note that interestingly enough, you can write such a principle as a principle of least or stationary action where the Lagrangian, which is constantly minimized the longer path, is variational free energy.
So here are some concluding remarks.
I'm not going to through all of them.
But the first one is basically what we just discussed, this idea that the generative model encodes preferences.
If an agent maintains existence, its likely states are its preferred ones per se, hence the notion of self-evidencing.
And I just also want to point out that this new approach or chapter of physics, let's say, consisting in describing physical systems as encoding probabilistic beliefs is called Bayesian mechanics.
Okay, so having said that, thank you very much, and especially thanks to all these guys who helped me so much, especially Len.
And yeah, thank you for your attention.
I'm coming back.
Thank you, Richard.
Okay, well, while we're settling back in, and anyone is asking questions in a live stream, what is your PhD research?
And if this is your side project, what is your main project that this kind of relates to?
Yes, so, well, in fact, I kind of read about the free energy principle in my free time, whenever I had some time.
And what I'm doing in my PhD is, so we have a couple of projects.
The first project we did was really modeling bacterial evolution through, so basically we model bacterial evolution as a bias random work on genotype space, with successive mutations and successful fixations.
So that's what we are doing.
So that's what we are doing.
It's not related to the FEP at all.
And the second thing we have been doing is modeling.
So basically, we had a system where you have bacteria which can kill each other, thanks to a system which is called the T6 secretion system.
And they kind of have needles with which they can go through the membrane of other bacteria and liberate toxins.
And they can also bind to each other.
So there is like a prey predator kind of dynamics.
And we did like a lattice gas modeling of such systems.
So basically, that's what I'm doing in my PhD, which is not related to to Bayesian mechanics, but I would like to transition to the field afterwards.
So yeah, we'll see how it goes.
Awesome.
Awesome.
I remember when I thought my PhD wasn't related to active inference.
Okay, cool.
Well, the work built to an amazing crescendo that in its simplicity, even though you highlighted it, it's easy to fly by, which is the coincidence of the preferences and the expectations.
So could you maybe give a little context?
How else has that nexus of preference and expectation been approached?
And is the FEP only and simply and always that coincidence?
Is that coincidence upstream or downstream of some other commitment that we make?
Like, what are the commitments that we really make?
And is that alignment the commitment or a resulting commitment?
Yeah.
So, so first of all, I think the notion of self-evidencing might be a bit refined with the next formulation.
But anyway, it's, I think that's a crucial point about the FEP.
And usually it's kind of confusing because when you're reading the papers and people are starting to write that the system sample evidence for its own existence, you're like, what?
I mean, I'm not sure to understand what's going on here.
But in fact, yeah, it's, I think the way I introduced it, this idea that by definition, a living thing is a thing which, which managed to sample life compatible.
So, I think, you know, sensory data is really what allows this alignment between surprise and preferences, basically.
And this idea that actively sampling unsurprising data is in fact, and it's not like a tricky wording, in a way that's really what's happening.
It is sampling, it is sampling life compatible, or preferred in that sense, data, hence the notion of self-evidencing.
But, yeah, I think the whole idea here is that we start from existence, we start from the sparse coupling architecture, where the particle managed to maintain its physical integrity, managed to display a Markov blanket, which allows the agent to have its own internal dynamics separated from the object.
So, somehow, is the ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail
all about and actually last remark um in a machine learning street talk interview of maxwell ramstad
he it was titled the fvp as a physics of survival if i remember well and i think that's that's very
very much what what it is all about in a way awesome how would you relate what you just
describe to reward or to reinforcement type learning schemes yeah so i i mean i'm not um an expert at all
i could not uh make the bridge here but i know that um lance dacosta made several uh works and interviews
about the subject and actually i think there is a very new paper called active inference as a model
of agency you just shared actually today um so i yeah i recommend the viewers to to check them out
and as far as i know but here i'm just i'm just uh saying what i heard is that um any reinforcements
learning algorithms can be um can be framed in terms of active inference so i think active inference is
is a very um uh fundamental scheme but yeah yeah it's all good like the reason i ask just with how
you presented it is what kind of observations do we want to sample that could be the sensory embodied
interface between the agent and the environment or you can take more cognitivist approach and sample
internal observations but those are just external some other internal so what do we want to really
sample well if you're even in a position where you're talking about sampling from like a utility
or a reward distribution you've already specified a distribution why not just specify the existence
distribution the actual attractors and stationarities of the measurements and then um
it's simpler because there's no proposal of a secondary intermediate between the temperature and
how good different temperatures are by going and just saying it's not rewarding to be at 37 homeostatic
temperature it's just expected and likely and the ball rims downhill it's actually a lot simpler and more
general yeah i and i i think that um it's way more simpler to i mean the idea here is that the agent has
a kind of world model which as you said uh specified what are the the expectation uh with regards to
just existing in a way and as opposed to uh designing explicitly um um um uh objective functions um
with the which incorporates the notions of utility and so on so yeah i'm very much agree
um earlier when we were looking at the flows and we had the breakdown of a flow um could you maybe just
um
what animal are you thinking about or what scenario can help us understand like what's the solid black line
what's the small red line what's the spiral what's like a physiological setting that we could associate
here to help us understand that kind of complex movement yeah so uh generally speaking the first thing
i could say is that this notion of solenoidal flow so it's like in the schematic schematic in the first
slide where you have you had this either contour circulation on the nest density or here the the
the component of the flow which creates this sort of spiral here it can it so that um it's this sort of um
oscillations are i think uh the sort of oscillations or cycles that are ubiquitous in living systems um i mean i'm not
a biologist but you can uh or not really a biologist uh but you can think of the circadian cycle or or
anything in any sort of systems there is this thought of of of um attractor where you're circulating along
and so here specifically to this to this um schematic here i think the idea is that um
um um you have so you have you you basically let's say that uh for a given sensory states you have a
corresponding autonomous mode and the when the sensory state change the autonomous mode mode uh changes as
well and in fact move on its so-called manifold so basically i guess here you have the mode moving
uh on its manifold and now if we take uh the perspective of this autonomous states here we uh converge to the
the manifold to the mode uh and because of the solenoidal uh component of this flow the way we will um reach it
uh and uh and um i really recommend here the free energy principle simple paper you have the the flow on the
manifold it's just the path of the mode itself let's say and you have the flow of the manifold
the flow of the manifold was gradient component is the flow towards the manifold in fact um so basically so
that's basically how autonomous states kind of um react to to to sensory data which change the autonomous mode
and i think the world uh an important idea here is to assume that the flow of the manifold is fast as opposed to the flow
on the manifold so that basically the sensory state are always uh in the vicinity of their mode and move with their mode
and um sorry and um and um and yeah i think that's pretty much the the idea here okay so let's just say that the black line
is um our homeostatic body existence life compatible ph oxygen blood sugar and yeah we are that light blue dot
that's off that manifold of course if we were far enough off to be dead it would be a moot question but
we're off but within a life um scaffolding a compatible zone and now as time pushes us down into the right
um there are different slices that we can trace um we could take the shortest path
the gradient flow directly towards the manifold so as that plays out through time it would look like a linear line
converging to the thick black line or
pure solenoidal flow would just stay equally far away from the thick black line and continue to spiral so that would look like a corkscrew
uh through time and then here when you have the combined character
of the linearized convergence towards the manifold and the corkscrew out through time
we get this kind of winding spiral so it reflects on me that the gradient flow is pragmatic
the gradient flow is a pragmatic value in that it aligns future observations with preferences and the solenoidal flow has
an almost epistemic character in that it circulates amongst a set of equally valid outcomes
the same factors yet here we're not looking at the pragmatic plus epistemic decomposition of the expected free energy
policy selection strategy like equation 2.6 in the 2022 textbook so is that just a concordance or where do you see some of those topics connecting
um i'm not sure maybe uh but having said that on this on the the meaning of the solenoidal part here
i know that on the on the uh i don't remember if it's in the free energy principle simpler paper or
or someone else but there is an analogy i mean they discuss the meaning and the role of the solenoidal flow
where they say that it it it kind of help um it kind of helps mixing systems uh the systems and you can
view and they discuss the metaphor with where you want to dilute your um your um your coffee for instance and you're going to have
this sort of uh motion in order to reach the the as fast as possible the steady state where everything is diluted but i
i i um i'm not sure i didn't think enough myself to provide any sort of interesting insight
all good just to have composed it is very insightful um well you made choices assembling things like what
do you feel like would have been background maybe a course or a skill what background do you feel like
like you kind of conditioned upon that somebody might want to check out and then what do you feel like you would have
wanted to include in the state-based formalism
um because to bring it into a under one hour timing is very
concise so where do you feel like somebody could
fill in some background to pick up with you at the beginning and then what else do you think would make
a fuller presentation
i think i mean there are a few aspects and details i didn't really uh like fully uh discuss um
well first of all all these um things which in here which involves like center theory
a center manifold theory and stuff like that uh we we kind of played uh qualitatively with it we didn't
really go into that and also if we want to be like full really full formally speaking um
let's see maybe um
um uh well there are a couple of things where we that we kind of accept without really checking all the
assumptions and also the revive derivation and i'm especially thinking of the of the helmer sauer
the composition of f because of course you need um a steady state an s density to exist to in order to
have such uh a decomposition so here i think it's it's there is a lot of stuff to to check and i mean
there is a nice uh i think it's in the appendix b of the bayesian mechanics of stationery process
paper by lance where it he he derived the helmotts decomposition uh so yeah there are quite a few
things we kind of state without um derived so it can if people are interested in in going further i think
that's kind of interesting formal uh directions um
um and um um um yeah cool i think it'll be a really fun collaborative project to axiomatize and
formalize and modularize using the act in fontology and understand a lot of these um relationships and
then the other piece that that made me think about is like what work is any of this math
doing at all just kind of like the ultimate existential question here um and when we condition
upon existence we've kind of like off-sourced a lot of cognition we don't need to make the jump or the
walk or the miracle from axiom to embodied existence or to even measured hypothetical existence so that
is left unaddressed the margin was not big enough but it wasn't even addressed and maybe there are even
advantages to leaving the um what happens before the conditioning
you don't want to take it with you after you condition upon it that's the whole markov like
concept like if you're like well i'm conditioning on five years ago
in the present but also i'm carrying five years with me today well then it's like well then it wasn't
conditioned upon so to really condition upon measurements is an extremely radically simplifying
maneuver that may change the scope or the applicability of the framework
relative to a conception in which what the free energy principle does is describe how things come to be
however yeah this rather conditioning upon it opens up that discussion and more circumscribes
this very analytically tractable setting of the agent and the environment across a conditional interface
yeah but by the way about about the conditional thing there is now the notion of you know weak markov
blankets that dalton introduced which cannot lose the the the approach let's say and and um because indeed
there is a question on uh i mean does it apart from the the the the formal setting we have here can we
really apply it to real systems and stuff like that and um and also i think it's the physics of survival
uh in itself uh at a given survival at a given time scale there is uh at if i have at a given time scale we
survive indeed in the sense that there is indeed this partition or conditional independence between the
internal and external here is the physics you have to comply with but we it didn't tell you tells you how
the mark of blanket uh rise or whatever it's it's it's it's just not what it it is designed to um to explain um but um
i think generally speaking it's it's really informative uh because for instance if you are considering the
um i mean just the sort of approach in general i mean for instance if you consider the pendulum
um effect where you put pendulum oscillating on the table and they are going to synchronize with each
other and i think that kuya isomura did a paper about that recently um in order to understand what
is going on and why the pendulum synchronized at some point you just have to recycle all this line of
reasoning with the synchronization maps that's very what is at play and what explains why the pendulum
synchronized when they are both on the same table so yeah i think it it really it is really informative
to in order to understand what is going on when we are talking about synchronization phenomena across
uh sparsely couple systems and also it gives you i guess the sort of recipe to understand what it what it's
um what it takes to be an agent if you want to design your uh an intelligence system um and uh
uh but uh yeah the question of how much useful it is uh beyond the fact that it's just some nice formal
framework it's it's an interesting uh interesting discussion yeah and i i i um i i just two things
first i would like to go back to your previous question about what sort of things could be could be
uh discussed further i think an interesting uh point we didn't really uh discuss fully is the notion of
synchronization map because uh we didn't necessarily really discuss the the the hypothesis and stuff uh about
the synchronization map and i in fact i think there is um much things that can be said uh for instance
because we assume injectivity thanks to the rank nullity theorem uh it's kind of constrained the
dimension of the internal manifold here with respect to the blanket manifold here and it kinds of
constrained in order to have injectivity thanks to the rank nullity theorem and so it kind of constrains the
the the the in order to say it in a qualitative fashion it kind of constrains the complexity or richness of the
internal states uh which speaks nicely to uh other frameworks like um uh like ashby's laws of requisite
various variety where you want the regulator system to to be as um as sophisticated or as rich to the
regulated systems and here you need the internal states to be enough uh complex to uh or to constitute
the sufficient statistics let's say to parameterize the sufficient statistics let's say to parameterize to be able to
parameterize the density indeed um and this um and this uh richness let's say is constrained by the the cardinality of your
uh uh the cardinality of your sensory uh uh channels if you will uh because basically you need the internal
manifold to be to have the same dimension than the blanket manifold or the sensory manifold to be to have the
the same dimensions that the autonomous manifold um so i um i mean i think there is many things to discuss about
this um this aspect here um and and the last thing i i would like to say about your uh about your last question
about the applicability of the framework and how much it's useful as opposed to be a simple elegant
formal framework i think so you know there is this um these papers about um uh about like the mark of
blanket trick and stuff like that uh about how much difficult it is like to identify what states
corresponds to the mark of uh blanket or whatever um and and i i'm personally i'm not really convinced
by this um these critiques um because to me it's like to me it's like saying to newton yeah i mean it's um
i'm not sure that i can do anything with your framework it's it's complicated if not impossible to model
systems with clearly identified and separated roads and masses let's say uh okay fine but we're talking
about newton mechanics here so i mean i think it's the the same here it's if you have a sparsely coupled
random dynamic systems that's the sort of behavior it will display it tells you fundamental things
about the nature of living systems and the idea that when it comes to a specific system it can be
quite tricky to to model it that's another question um um
um and indeed when it comes to the art of modeling complex systems it's it's it's interesting and and
we can discuss about how much complicated it can be to apply the framework um yeah awesome i love that
it's like the art of the science and the art of the modeling and and the and the craft especially in the
kind of early hand-built largely custom stage like one thing i even wondered looking through these slides
um what fraction of these representations and formalisms exist only analytically and do or is
there a code representation of this exact scenario or you know are some of these areas
known as equations that is known as equations that don't have
code realizations they're just pure existing equations
so i mean i think um more or less everything here can be um
can be simulated even this synchronization thing here you can perform simulations where you can really literally see within the simulations the synchronization.
And I mean the whole thing here can be you can simulate such particle random medical systems and kind of interpret the dynamics indeed as the way we frame it.
But yes that's also an interesting aspect.
It could be cool like in the github repo in the journal for this transcript or something like that to curate together the simulations that demonstrate or a minimal specification for it.
Yeah.
Because it's actually there is.
Yeah, and actually there is a, I mean, I think it's in the in lens paper about synchronization map, the Bayesian mechanics of stationary processes paper.
There, there are some simulations where he shows that.
I mean, he shows that.
I mean, he shows the synchronization map at play, and it shows that basically you can't go back to.
I mean, if the map between the blanket states to the internal states is not injected.
And you apply the synchronization map to the actual sensory, to the actual internal states, it gives you like some natural oven things and there are some nice plots from simulations.
So that's definitely a paper to check out.
Cool.
So where do we land?
And then how do we leap, exercise, relax to prepare for part two?
Yeah, so I think here's the world point was, I mean, this world formulation is in a way about the momentary, the short term, and the momentary response to autonomous states to sensory stimuli, let's say, if there is this, this, I mean, the kind of instances of the
differentiated active states are so that outcomes, whatever.
But in the next video where we will look at the path based formulation of the framework, the world idea would be to ask what about path and what about future path and what about the long term behavior?
And what about planning?
And what about planning?
What about higher order cognitive abilities?
And we will kind of extend the scope of what we are doing in that sense.
So, yeah, I mean, I think from a formal point of view, here, I kind of introduced many things, variational inference, synchronization map, etc.
One after the other, before actually deriving the free energy principle.
Next time, I think we will, it will be more straightforward.
But the main concepts to which will be at the core of the of the framework and which can be confusing if it's the first time you you look at it is the notion of of generalized coordinates of motion when you relax the white noise assumption.
And that's something that can be confusing, especially for the physicists, because when you're starting saying, yeah, the generalized Lagrangian, it plays the role of an action or whatever they are like.
No, but Lagrangian is not an action.
What are you talking about, etc.
But when you get acquainted with the world construction is very elegant, but that definitely something people can start to look at before prior to the live stream.
Yeah.
Awesome.
Yeah, well, it was excellent.
You brought a lot together and a lot of trails leading off this trail and the citations and previous papers that that also brought things together.
Lance's work and others.
And it's going to be awesome to see part two.
So thank you, Richard.
Thank you very much, Daniel.
Thank you.
All right.
See you.
Bye.
Bye.
Bye.
Bye.
