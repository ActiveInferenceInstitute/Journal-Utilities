---
title: "ActInf Livestream #037.0 ~ "Free Energy: A User's Guide""
category: "Livestream"
series: "Livestream_037"
episode: "0"
duration: "1:29:27"
url: "https://www.youtube.com/watch?v=chpbMBgDR84"
views: 419
exported_at: "2026-02-18T22:37:37.865726+00:00"
format: markdown
---

# ActInf Livestream #037.0 ~ "Free Energy: A User's Guide"

Thank you.
All right, it's January 28th, 2022, and we're here in Actonflab livestream number 37.0, discussing the paper Free Energy, a User's Guide.
Welcome to the Actonflab. We are a participatory online lab that is communicating, learning, and practicing applied active inference. You can find us at the links here.
This is recorded and archived livestream, so please provide us with feedback so we can improve our work.
All backgrounds and perspectives are welcome here, and we'll be following good etiquette on livestream.
Go to activeinference.org if you want to learn more about anything happening in Actonflab.
All right, so today in 37.0, we are going to learn and discuss and introduce and provide some background for this paper, Free Energy, a User's Guide, by Stephen Francis Mann, Ross Payne, and Michael Kirchhoff.
And just like all the dot zeros and discussions, we're just going to introduce some ideas, give a little tip of the iceberg, and kind of warm up to talk about this paper in the coming two weeks.
And so today we'll be going through a lot of the background and some of the key formalisms in the paper.
And in the coming two weeks, we'll be discussing the paper, so let us know if you want to join.
So first, there's this comment in red.
Is this yours, Dean?
Yeah.
Do you want to go over here?
Pardon me?
Do you want to describe it here or in your intro?
Yeah, in the intro.
Great.
All right.
Well, we'll each just go around and say hello.
And then I think we can just say one reason why we're excited to discuss it.
I'm Daniel.
I'm in California and was just enticed by the title, short and direct.
And I think it has some great solidifications and perspectives and implications on multiple levels.
So how about Stephen?
Hello.
I'm Stephen.
I'm based in Toronto.
Yeah, I was interested by another sort of way to surmise the free energy principle and active inference type approaches.
in relation to the philosophy of biology and cognitive science.
I thought that was interesting to see how that pitch was being made.
Over to Dean.
Hi, I'm Dean.
I'm in Calgary.
And anytime I see the word guide, I'm always curious because of my background in setting up programming where people were going into novel situations.
So the authors kind of had me at that word.
And then I wanted to sort of learn more about what they had to say.
What are some key features of guides or things that guides should keep in mind before we head off on this journey?
Yeah, well, for me, I sort of adopted the term wayfinding.
Kind of as a blanket, not just a mark of a blanket, but as a way of maybe describing what that path could turn out to be without necessarily constraining people.
So, and there, I'm sure there are other descriptions and definitions of the word guide, but that's the one I tend to, to, uh, gravity towards.
All right.
Steven.
Yeah.
And there's also what kind of guide we end up inhabiting.
So, you know, this biological grounding, it feels like, uh, there's a desire to get into our feet and into the soil somehow, uh, as well as the cognitive science.
So I feel it's a bit like I've been stretched up and, uh, pushed down into the ground.
So there's something there.
Okay.
So one big question, probably not the only big question that could be raised, but just the question that approached us to this paper in some way is how can we learn and apply active inference?
And then Dean, do you want to talk about what you wrote here?
Well, I just like to kind of read it out.
I don't.
Yes.
Okay.
So assuming that making moves, which we could describe as behavior now has effects on what happens next and that those moves are at least.
loosely based or inferred on evident and the, and the, and the authors use the terms, probabilities, predictions, and fitness.
So that's in the paper.
Then how might we begin to look at energy applied?
Okay.
And in calculating out our best guess is measure, measurable as or of what we think or believe will happen next.
Step one, that road to prediction matter expertise.
Now prediction matter expertise is a term I coined and brought up with Dr. Friston.
Um, but I think it might, if we're guiding, we might think about that in the background.
The other part was they talk about models and blast in our last live stream set.
That's all we were doing is talk about modeling ourselves.
So it seems like a natural extension.
Now it's talking about models, models as inference and action models, as selection models, as extenders, i.e. tools.
And then how does a model curate, curated, rundown, help us get outside the guide when using energy in ways beyond guide explication and interpretation?
Do we need a user's guide for the user's guide?
Which is something that I used to ask all the time, uh, the kids that were participating in the program and that I was setting up.
Um, because they were going out with their background and they had sponsors who had a different background.
And we often wondered whether or not they would have to give a user's guide to somebody who is necessarily more experienced with the field, but not necessarily experienced with bringing young personal.
on. So that's why I think that when we're talking about how can we learn and apply
inference in this guide theme, those are things we might want to keep sort of at least partially
in our thinking. Thanks a lot for sharing that, Dean. A lot to say, but that's what the dot one
and the dot two and beyond are for. So the paper is Free Energy, a User's Guide by Stephen Francis
Mann, Ross Payne and Michael Kirchhoff. It's from The Last Days of 21, I believe, and it is
on the PhilSci Archive. Okay, so here are some of the aims and the claims of the paper.
Over the past 15 years, a novel explanatory framework spearheaded by Carl Fursten has inspired both
excitement and confusion of philosophy of biology and cognitive science. Active inference, whose
most famous tenet is the free energy principle, purports to unify explanations in biology and
cognitive science under a single class of mathematical models. So not math under biology, but biology under
math. There are broadly three reasons why the active inference framework is difficult to understand.
In the author's words, first, the mathematics are unfamiliar to many philosophers and even to
biologists and cognitive scientists and mathematicians and all other kinds of peoples. Second, the framework
was developed rapidly by a small but dedicated group of researchers limiting its accessibility while
expanding its scope. Hashtag recent history. Third, the framework makes claims across both mathematical
and empirical domains and the dialectical relationships between these are unclear. So what is the math,
bio-dialectic, bio-dialectic? Who's nested within who? Yes, Stephen.
Stephen. Yeah, I think this, the way these three kind of points are made is useful for seeing the rationale
for this paper. I think there's seen as a desire to come at these questions as if it was coming from
people less steeped in all the math. Because previous papers might have come out which had an awful lot of
particular, you know, particular information that comes from this dedicated group of researchers.
I think by trying to speak about it from the perspective of people arriving, it gives those core
researchers of which I know for sure Michael Kirchhoff is, you know, been part of, a chance to clarify the sort of
framings or misconceptions that might end up being placed in other papers by philosophical philosophers.
And I think has become a little bit of a vicious cycle of distraction at times. And I think they're maybe trying to reclaim that ground.
So that's just my own strategic guess, but it looks likely that might be why this paper's been put together.
Well, great and helpful feedback. Thank you. Then the last parts are here. We attempt to redress this situation
by targeting each source of potential confusion. So they're going to identify three frequently asked questions,
frequently raised concerns, underpinning frictions, and then redress them. And their aim is overall, we aim to
increase philosophical understanding of active inference so that it may be more readily evaluated. And maybe we could
even add applied and developed. Okay, so would either of you like to just read the abstract?
I'll go for it, Dan. Okay.
Over the past 15 years, an ambitious explanatory framework has been proposed to unify the explanations across biology and cognitive science.
Active inference, whose most famous tenet is the free energy principle, has inspired excitement and confusion in equal measure.
Yes, it has. Here we lay the groundwork for proper critical analysis of active inference in three ways.
First, we give simplified versions of its core mathematical models. Second, we outline the historical
development of active inference and its relationship to other theoretical approaches. And third, we describe
three different kinds of claim, labeled mathematical, empirical, in general, routinely made
by proponents of the framework and suggest dialectical links between them. Overall, we have to increase
philosophical understanding of active inference so that it may be more readily evaluated.
All right. Cool. So nice and funny abstract. We all laughed. So the roadmap, how do they structure this
guide? Is it meant to be read linearly or do you flip to a different page? I don't know. But we have added the page
numbers on this slide. It's on the bottom right, but it'll be on the bottom left. And that's what page we are
in the guide. As if it were in paper in our hands. And it starts with an overview. And then there's a
discussion on first the inference of perception or observations and hidden states. And then action comes
into the loop. Section three gives a brief history of the free energy principle. And section four discusses
the aforementioned dialectic of free energy and its rhetorical ecosystem, we could say. That's the
part we're not going to focus on in this dot zero, but hopefully we're going to be able to go into each
of these really important troikas in the dot one and two. Then there are some concluding remarks.
Okay. So first, how is the word model being used here? It's really good that the authors included
this warning because we hear about modeling all the time, not just the photography kind,
the mathematical kind. So they write, let us begin with a warning. The word model takes on two distinct
senses throughout our discussion. The sense more familiar to philosophers is what we call a scientific
model, a representation of some possible or actual system, which a scientist uses to reason about or
discovers features of that system and related systems. By contrast, in the active inference
literature, a narrower sense is typically meant. What we will call a generative model. That's what
we're going to be specifically talking about. This is a mathematical object with applications in
statistics and various sciences. Our simplified models of the free energy principle are scientific models.
So models is a big category, but we're going to be talking about kind of a narrow sense of statistical
models like linear regression models, but instead of a linear regression, it's a different kind of model,
not at the exact same elevation of the linear model or taxonomy, but like in that category. And then
note further that some scholars opt for a deflationary stance on generative models, using them only to
describe the dynamics of agents. So descriptive modeling. It is an open question whether this
kind of model building precludes any form of scientific realism about the relation between the
model and the target system. These issues are discussed in section four and also have come up several
times, including with most recently Majeed Benny, but model based science and what does it mean to use and
make models and maps and territories and all of that. So any thoughts on models? Because that's going to be one
of the key terms going forward. What would either of you say would be the best way in layman's terms
to show the difference between what they mean when they talk about an empirical model and what they talk
about in terms of a generative model? What sort of real physical material things could we use to make
clear the difference? Because in the last stream we did a good job of taking columns and showing how they
were discrete. How would you guys describe this? Yes, Stephen.
I think one of the ways this distinction comes about is the difference between
the difference between most systems type approaches and non-linear dynamical systems.
Generative models are tend to be coming from a sort of a swarming, it's like a swarm of bees
creating and evolving as compared to something which has been given a perspective and drawn out
somehow in our environment as in a scientific model. Now the fact that generative models are being applied
in the kind of scientific way, inverted commas, or are they? Are they being used in a more instrumental
stroke philosophical way and they can never be fully science is another question. But I think that the
difference there between this kind of biological generative sort of process and something which can be
given a perspective on and drawn out as a defined type of model is where there's a kind of a clear
difference. I don't know how others see that, but I think that that also might be useful.
All right, Dean, here would be my answer would be two that are on the extreme end of the yellow type
scientific model would be like the standard model in physics or a working model of renal function,
like kidney function. So it's like very transdisciplinary and includes a huge number of domains and kind of
logical motifs and has axioms and a specific history and software toolkits and all of that.
And then we're going to be talking about a kind of model that's basically a parametric statistical model.
So like a Gaussian model takes two parameters, the mean and the variance, and that can be written
analytically, like with equations, or it can be done computationally, but it's only ever going to take those
two parameters and it only ever outputs a certain family of distributions. And so it's like parameters
in distributions out and the parameters can reflect like the connectedness of a graphical model too,
but you get parameters in, which can include model structure and then some type of output, but it's
it's closed-ended within that paradigm versus the model of renal function is like this open-ended question.
And I think you hit on something really, really critical there. It's distributions out, right? So
something falls out when we're talking about a generative model. Whereas when we're talking about
something empirical, we tend to keep the focus stabilized, right? Like this, so the process
is fundamentally different. And so again, when we're talking about in sort of layman's terms,
what the difference would be, I think you hit the key word out of that, which is something that's in
and stays in versus something that may start in one place and fall out in a completely different place.
With is that an expectation we should have as a difference between these two?
Yeah. Just one thought then Steven would be both modes are so important. It's like
yin and yang or left and right hand or convex and concave. And our discussions do move regime of
attention from like the generative model to the bigger question. And in some ways it maps onto
instrumentalism and realism too, but we really need to know when the pendulum is swung one way and when it's
swung the other way. And so we can keep an open mind and they're all happening all the time. That's
both eyes open. Like you're always saying Dean, but we also can't go too hard on just one side. So Steven?
Yeah, I think I love what you said there, Daniel, about the axioms. I think in generally in science,
you try and have reproducibility and you have tolerances and you say how much accuracy and
what's this tolerance is on something, but there's a general recapitulation of similar types of results
again and again and again. And the same sort of thing comes up. It has been there in psychiatry and
psychology, you know, with, with, and that's where the, the idea of syndromes being classified as
opposed to symptoms, which must be much more fluctuating, more variable. So you could run a
generative model and it can come up with different results with the same input and that. Now there will
be some kind of characteristic patterns that generative models do reveal, but that there is a point where
it's quite different. And I suppose when, when that difference, I think there's almost paradigm based
difference, but maybe there is some point where they blur. I don't know.
Yes, Dean, and then we'll go onto the paper.
Yeah. So at the end of the last live stream, one of the thing comments that one of our colleagues
blew me was that we have to be able to hold two things up at once, which sang to me because I think
that's what you're saying, both of you're saying right now. I think if we look at, if we, whether
we're looking at a starling or a murmuration, whether we're looking at an ant or a colony, we can keep
something in, inbound, or we can have something fall out from that because it's basic research.
Like we weren't expecting something repeatable. That's, that's how I would distinguish it. But
again, I just, let's get onto the paper, but I think that's important that we get
that established first. If we're talking about guides.
That was the big epistemic disclaimer, and that's what they put in their paper. So we allocate our
attention as well. Okay. So onto the details of the paper. So in 2.2, they introduce this
simple model of inference with W and X. So this is figure one, there's W for world. That's the hidden
world state. And then there's X, the observed data, like X marks the data. And you can think about like,
where do you estimate where the sun is in the sky? That's actually unobserved, but then there's going to
be all kinds of observed data coming in, or we'll talk more about the coming in versus the generative
model later, but the observed data are what are being modeled as being observed in that sort of
sensory way. So figure one is the basic model of inference. The inference problem addressed by the
active inference framework. What other kinds of inference problems exist? What problems do or don't
have this form? What happens if there's no line with W and X? So of course it can get more elaborate,
but within this exact format, like W might output X and Y. And that'd be like getting two numbers back
in the computer program instead of, or generating two numbers in the computer program rather than just
returning one. Or you can imagine X is like a vector, but we're within that specific model framework.
We're not in the realism of agent environment. We're just in the statistical framework of hidden latent
variable, observable variable X. The unobservable state is assumed to cause observable data. And so
this is a little bit of a connection with dynamic causal modeling, because statistically we call that
causing just like the proportion of variance explained by a PCA. It's like given very active
terms. It's, but it's actually not causal in the mechanistic sense. And that of course has been to no
ends of confusion with how statistical conclusions are interpreted as mechanistic
conclusions about the world. And so is it cause in the sense that we mean it in one sense,
or is it associated in a causal model? And that's kind of the causal in dynamic causal modeling,
that's functional connectivity. So that's the realm that we're talking about, not within the world
environment interaction. Stephen?
Yeah, this is, this is actually interesting. They've gone back to a pre-Markov blanket kind of
formulaism. And it raises that question then of what does it mean to infer? And it can be that we
infer things because that's what we get data on. So it talks about, well, what is it that we can even
use to understand? And what are the assumptions about what's actually important to read? And those two
things, I think this leaves both of those things open. And that, that, that, that actually is a bit
of a bridge between the scientific and the generative processes.
Cool. So if we were modeling like height is not measured, but we observed weight, and we're going
to do some regression of like the unobserved and the observed, that is the type of model that we're
going to be talking about loosely. And someone could say, oh, but this other factor influences too.
Yes. That's the realism claim. This actually matters in the real world and it very well may,
but we're talking about measured models relationships, Stephen.
Yeah. I think this is also really helpful to be able to look at paradigms because there's a difference
between say the paradigm of psychology from the perspective of looking at classification and problem
identification and treatment and coaching psychology, which is about not so much trying to diagnose what's
there, but what sort of actions someone's trying to take and how you might help them with those actions
to reach outcomes, which may vary moment to moment. And I think, you know, in some ways that, that,
that's, this is maybe the level you have to go back to because otherwise the noise just swamps the discussion.
It goes deep on both ends, that action orientation, the pragmatic turn ecological psychology is going to connect deep.
And this is going to be deep, but in a sense, narrow, because we're just talking about statistics here.
So take statistics courses and learn it because this is kind of where it comes from here.
Okay. Onto the example of active cat friends. That's, that's not actually what they called it,
but that's the cat example that we're going to be discussing.
We're going to imagine that you have a cat animal that spends its time in either the kitchen or the bedroom.
When it's in the kitchen, it often meows for food. When it's in the bedroom, it often purrs loudly.
Okay. Suppose you tally the proportions of the times your cat is in each place and making each noise.
The results might look something like, okay, but the cat also goes somewhere else. Okay.
Not in the model or this other factor or this other sound. Okay. Change the model, add another column.
It's totally fine. It's a fork on the GitHub or the discussion, but that's the difference between kind of
modifying the model structurally and using it parametrically within the narrowest sense of
model and then keeping the discussion alive about that broader sense. Like what Steven is talking
about, like a model of psychology or a model of complex adaptive systems. So one thing to note is
that this idea of setting the prior in a Bayesian sense from observed data is called parametric empirical
Bayes. So parameter, parametric, we're setting parameters, like frequencies of things happening.
And it's empirical, which means observed. It doesn't mean like the only truth. It just means the measured
values. And then it's Bayesian as we'll talk about. So let's just say 10 or a hundred or 10,000 measurements
were made and they come out to these numbers. 60% of the time they're in the kitchen and 40%, the cat is in the
bedroom. And so that's like summing across that's called a marginal probability because it was in
the margins of papers and they marginals have to sum to a hundred percent because something has to happen
in the model. Oh, but the cat can be in the roots. Okay. Yes. But within the model, it has to be this way.
Then that's what makes a probability. Then 50% of the time there's meowing and purring, but as the numbers
show the location and the sounds, they have a statistical association. There's some divergence
that could be tested for statistical significance, depending on the number of observations. But that
is what the numbers in this table are reflecting. And both columns and rows sum up to a probability. So
they're all like proper probabilities. Then how do you infer about this? Like if you were to
observe the room, how could you reduce your uncertainty about what sounds you'd hear?
And then if you'd hear sounds, how could you reduce your uncertainty about the room?
Many philosophers will be familiar with one famous method for solving this problem, Bayesian
conditionalization. This method can be stated as a principle saying how an agent using a model,
P of W and X, W world state hidden X observed data ought to choose their beliefs Q of W,
Q, that's the one we control upon observing data X, what to believe now conditioned on incoming data.
Okay. Any points on that?
Just, they did a really good job of explaining it.
Yeah. I'm waiting for the next slide.
Yeah. Okay. Please continue here.
So from the, from the actual paper, the table describes a joint probability distribution,
which we've just explained, where W ranges over possible cat locations, either the kitchen bedroom
and X ranges over the possible cat sounds. Again, very clear, straightforward. From the next side,
usually the science, scientist, not the person who is trying to build a generative model aims to improve
the accuracy of a generative model of some real world, world phenomenon, which would mean improving
the accuracy of PWX. This learning task is relatively difficult. So I wanted to kind of parse what relatively
difficult meant. And I'm not going to read all of that stuff there in red, but essentially what I want to
kind of state is they, the authors here said, this is simple. Don't, don't go to that place of high
complexity quite yet. Let's just see this for what it is. So that what Daniel said 90 seconds ago, which was
go take a bunch of statistics courses. Doesn't have a bunch of people running off and screaming into the night.
There is, there is a complexity to this, but it's not the kind that will swamp you. What they're basically
trying to say is let's just slowly work our way into this without every hit, all your historical
grievances around statistics trapping you before you even really set out set sail.
I'll add one note on that. This is like learning how the horse moves in chess or learning how the castle
moves in chess. And so it's possible to get super connected to your internal life narrative and the game of
chess and people who would have no problem losing in connect for or checkers will feel very engaged
emotionally affectively by chess. It just something I've observed empirically. Somebody else might have
different priors on that. And so this is a way of just starting with how the pieces move. And then as we're finding out,
we're going to figure out how the pieces move and then we're going to connect them and do all kinds of fun stuff.
Steven?
Steven Yeah. I think like you say, having the ability to stay with the pieces, do lots of fun stuff and look at the
the way things are generating with that data is different, for instance, to saying, oh, the meowing cat is an
assertive cat and the purring cat is a docile cat, which could be this kind of imposed higher order model.
And then everything's trying to fit to is it a docile cat or is it an assertive cat? But it's flattened out all of this,
you know, it loses this ability to generate.
Steven Professor Helen Longino has a book called Studying Human Behavior and Aggression in 2010.
That's like, once you define, oh, there's a significant difference between these two groups, or in the count of this
behavior per minute, and they've been pre labeled, it passes the modeling in the broad sense into modeling into the narrow sense.
Steven Professor Helen Longino has a big difference between the groups. So this is reifying our understanding of those categories. So it's really important. So this is going to be where the base enters the picture.
Steven Professor Helen Longino The posterior, which means afterwards, is calculated about how should the distribution P be updated as new information comes in. So just like the last sentence in red, what's the difference between the groups?
Steven Professor Helen Longino The posterior, which means that the last sentence in red, what's a belief now conditioned on incoming data. So now that is going to be symbolically or graphically described. So probability, the P distribution of world states conditioned on vertical line, new data coming in. And there's Bayes theorem.
Steven Professor Helen Longino Theorem. Other videos and other channels and groups will cover Bayes better and more comprehensively. But here we can suffice to say that first we can write it in words. Like what's the distribution Q that we control? The probability distribution of us thinking that it's in the kitchen.
Steven Professor Helen Longino Theorem That is the prior probability of it being in the kitchen conditioned on it or it's conditioned on it meowing. So how likely is it to be given that it meowed? And then the numbers that we just looked at can be plugged in to that verbal equation and a number is going to come out.
Steven Professor Helen Longino And so we heard meowing. And if we just looked at meowing like four times in the kitchen, one time in the bedroom. So four to five times it was in the kitchen, not the bedroom. And then here's an equation that does literally that. It just looks at the column and it does the conditional likelihood or the posterior of the world state after the data come in.
Steven Professor Helen Longino And then there's, I think, did anyone want to say anything here? There's this, it's
Steven Professor Helen Longino Learning task is difficult. I think we already kind of mentioned that.
Steven Professor Helen Longino Yeah, and the whole thing is, is that most people, I think, I'm not going to say philosophers, most people don't automatically go to being able to figure out what the probability is. But I think what these authors are pointing out is,
there's a way of being able to show that there is a probability in play, if you are not certain. And this is how you might split those probabilities out. That's all they're trying to do.
Steven Professor Helen Longino Okay, so now we're going to go from, as we've seen in other papers, the sort of exact Bayesian approach. Most similar paper to this, in this sense, is probably Axel Constance, number 34, with a bacterium.
Steven Professor Helen Longino We first looked at the Bayesian bacterium, and then we looked at the variational Bayesian bacterium. And then in both cases, we looked at how basically, sometimes new data could come in, you could still make wrong decisions.
Steven Professor Helen Longino Whether you're doing exact Bayes or variational inference, you can still make bad decisions as data come in. So this isn't a Pangolossian paradigm. This is like a statistical tool that's already been detached from the philosophy, or at least sort of docked at shore. And then now also we're breaking the assumption that it must go the right way, or that it will model real world systems, especially.
Steven Professor Helen Longino So again, back within the narrow sense. Sometimes the specific distribution of the world states conditioned on data coming in is intractable, so that distribution cannot be calculated.
Steven Professor Helen Longino This usually happens when the state space is continuous rather than discrete, which came up on model stream number 5.1. If there's only two decisions left and right, all you have to do is do two calculations and then compare which one is preferable.
Steven Professor Helen Longino Whereas if there's a steering wheel or a trim tab, then there's an open ended number because 87.1 degrees and 87.11 degrees might be very different in their long term consequences. So continuous state spaces are very challenging from a sensory as well as from an action perspective.
Steven Professor Helen Longino In these cases, what is needed is a way to choose q of w, the distribution we control on the world states to make it close to p of w conditioned on x.
So p of world states conditioned on data is the hard one to compute exactly, and this is going to be choosing a distribution that gets close to that other one.
Steven Professor Helen Longino When the problem is formulated by statisticians, we usually begin with a family of possible distributions q and search for the member of that family which lies as close to p w conditioned on x as possible.
So just like a linear model, it's like conditioned on this being a linear model, we're going to find the best linear model or conditioned on the quadratic form, we're going to find the best quadratic form.
Steven Professor Helen Longino This is like a little bit more general conditioned on the family that q is, we're going to do basically linear regression fitting, but not exactly linear regression.
How do you make those distributions converge or align as best as possible, we can do this.
Also, given that a structure has been chosen.
This is the fitting part.
This is not the structure learning unless the parameters about structure.
We can do this indirectly by using a measure of inaccuracy.
Active inference employs a measure of inaccuracy called variational free energy labeled f.
Because it is a measure of inaccuracy, smaller values are better than larger values.
So it's like Frisbee golf.
And the lower the value is, the lower the difference is between the actual p that you would have calculated perfectly and q, the way simpler, lower dimensional model that you can control and can save in RAM.
So that's described here.
Variational free energy captures two sources of inaccuracy that we're going to go into in the next slides.
In belief and dictates how they ought to be traded off against one another.
The two sources which we're going to explore are overfitting and failing to explain the data.
So those will be introduced and discussed soon.
Steven?
Steven?





















































yeah i think this also if we just to connect it to that scientific standard models and this type
of work is this is looking at contextuality it's like it's like what's based on where
the starting point is that the probabilities are being picked up on you start to roll out
the um statistical results i what sort of meowing is actually happening and as opposed to a model where
you're modeling a car engine and you want to know what energy it's going to give out a particular
moment it's going to do that whether i'm watching it or not it's just the same basic model applies
independent of the observer so i think that's uh also useful here yes like getting the model to
this stage like depersonalizes it in a sense because that model can be just transferred
and used in a like another instrument okay so here's those two sources of inaccuracy that they
described the first that we're going to discuss is overfitting the cost of overfitting they write
can therefore be measured by checking how far q the one we control on world states diverges from p
the first term of f free energy is a measure of that kind this expression two is also called the
relative entry entropy or holbach liber or the kl divergence so this is like the first half of the
two-part equation that will constitute f and it looks like this graphically symbolically but here's um a
kind of cool way to think about it if you were trying to fit a single hump into this two hump model
in the empirical distribution um so you're fitting a family that is going to get sort of coerced into
one of two extremes either it's going to end up fitting one very closely like the higher one if it's like
mode seeking and it will have no probability density the blue line onto the other hump or it'll
conflate them in a sense into two um uh kind of subpopulations blurred together and have a
solution basically that kind of goes between them um kale divergence is a way to fit distributions
optimally given this kind of challenge which exists for the one hump fitting two hump it exists for the two
hump fitting three it exists for the one fitting 50 it's a general statistical problem and kl is a method
that helps bring that blue line as well as it can on a trade-off frontier into alignment with the black one
okay stephen yeah i suppose this also gets into the reason when this is useful is when you're in complex
uh non-equilibrium situations where things are fluid then you're going to hit these situations and
overfitting is quite common social science is being one of the areas where we see these problems where it's
equilibrium based and it's fairly clear then you don't really have it's not really as applicable so it
sort of speaks to where this type of approach is applicable i.e where there's this kind of fluid
ambiguity in in in the situation okay thank you how about the second source of inaccuracy that is failing
to explain the data mathematically they write explaining the data means assigning high probability to events
w that make the probability of x high the penalty for failing to explain data is captured by the second term
of f which looks like this um higher terms of the actual value are matched with high value um with high
values on the distribution we control q to keep this term low so this is kind of like if it were a linear
regression and all the data points were lined up and the line just went right through them then it would
be doing really well on explaining the data and that would be given a low score here whereas if that
weren't the case it'd be flipped dean so when i was doing my work i didn't have access or maybe i wasn't
looking hard enough for the kl divergence so i can remember even on here and some of these live streams
saying i have no idea what that even means i have a better idea now but it's one of the metaphors that i
tried to use was in terms of avoiding overfitting or failing to be able to explain the data was so all
those horizontal and vertical lines creating a mesh acting as a filter how far apart do we set those what
gauge do we set our mesh for in terms of what we want to have stay above the mesh and what's passing
passing passing through now again maybe that's not sophisticated enough for a lot of philosophers but
to get the basic point down that's the kind of example i had to provide to be able to give people
some sense not just that these lines are now rigid and the 20 is on this percent and the 40 is on this
percent and never tell shall the two pass again but the lines actually move
thanks a lot so you're so right about that the example with the active cat friends and the
variational cat friends is like discrete by discrete is four quadrants so in some ways that's like the
simplest model right it could be two continuous variables it could be like the volume and then the
cat's position on the x-axis in a room now imagine if it was the x and the y is continuous or something
like that but just even two continuous variables and you're totally pointing out where it's like
you're gonna put the points around whether you put them right in the middle of the four quadrants
or whether it's more scattershot or something in between and then there's two parameters there's like
a linear regression through the points and then there's how fine the mesh is and you're observing like
pixel densities and doing a regression through the pixel densities and so you could have a super
continuous situation it is a continuous variable inside the bedroom but then in the model we just
looked at it's in one quadrant and we talked about that when we talked about um serval's paper and how it
was just the park and the cafe and yes there's locations within the park but they weren't within our
model so we didn't deny the reality of that physically we just were modeling statistically something
specific okay steven i mean this the filtering could also be relating to the sort of temporal sampling rate
because if you're measuring every millisecond if it's meowing or not it becomes pointless there's a kind of a
making sense rate at which the um the entropy is being converged at and and as we know in the brain we seem to have multiple
levels of that okay awesome next few ones we're going to go through just kind of quickly and
specifically so let's put those two terms together this is the overfitting and the over and the failing
to explain the data variational free energy f the non-metaphysical version is the sum of the penalties
for overfitting and failing to explain the data it's those two terms that we just described added together
so that the best explanation in a sense is the lowest on both of them it's not overfit it fits it well and
it doesn't do it any more than that so you know simple as possible but no simpler any other number
of quotes that's kind of this equations it's not the only way it could be written it's not the only thing
that fulfills that process but it's something that can be used and it's very tractable
as it turns out um this free energy has tractable computation 13. page 14. so now it's possible to
actually use that tractable approximation and do decision making and here is where they have the
decision making um here argman means choose the distribution q that makes the following term as
small as possible so this is where f goes from kind of being like a um a set of pipes with nothing really
running through it to a specific finite set of tested alternatives those are affordances in the case of
action selection they're discrete in the case of a discrete inference like is it in the bedroom or is
it in the kitchen it's continuous in the case of a continuous inference problem like how bright is it
outside on a continuous scale but even for continuous things sometimes we just do one through ten or one
through a hundred or one through a thousand and twenty four so discrete state spaces are really important
even if there is a continuity to the world so those are the kinds of computations that variational
inference helps perform it takes something that's descriptive and moves it into a decision making
imperative just like the l2 norm or least squares is like a decision making imperative for linear
aggression this is like an imperative for model fitting in this framework um the free energy principle
the form here inference is the same as that of bayesian principle discussed earlier in both cases you
perform a calculation and set q of w equal to the resulting value the difference is that bayesian principle
counsels a direct calculation via bayes theorem in contrast free energy principle counsels what might
be called an indirect calculation happily in practice this can be done by trial and improvement
rather than trial and error so that's axel constants bacteria the bayesian and the variational bacterium
combined with going to the bottom of the bowl on the smooth gradient descent landscape with a straight
arrow utility and the solenoidal epistemic component various algorithms for finding q the distribution we
control are available depending on the details of the generative model classic citation that gets referred to a lot
one of the developments that prefigured active inference was the implementation of such an algorithm in a
neural network first in 2005. old citation classic we're seeing that again in model stream 5 in alex
chance's work and of many others that this format even long before active inference brought it onto the scene in
our little side stage using neural networks to fit variational bayesian methods was a common technique in
machine learning stephen so when we say trial and improvement rather than trial and error it's basically saying
that the error can be used and utilized in an ongoing way it's not like you have to start from scratch and
come up with another attempt from scratch you're you know you're using what the same basic architecture and just keep running
it's so true i never really thought how demoralizing trial and error was like how should we get stronger oh well you're
going to try and then you're going to fail when error is perceived as a failure naively but trial improvement would be like we're going to
try and we're going to improve so yes of course error is implicit in that dean yeah and i'm glad you used
the bowl analogy because one of the things that i read and i was actually the one to highlight a
trial improvement thing because for example if you had the bowl filled with water and a ping pong ball
floating on top and you had to drill a hole because you wanted the ping pong ball to settle at the bottom of the
bowl at a certain time you could you could continuously improve by adding more holes of a certain diameter
until you were able to get that flow rate and have that ping pong ball arrive at the bottom of that bowl
at the particular time at the discrete time that you were looking for that's not an error thing that's
just uh we'll continue to get a little bit closer and closer we'll we'll figure out what the dosage is
and i agree with you a lot of people think it that the basic research part of it is oh i failed no a
lot of this stuff is i test it and then i test it again and then i oh i came really really close so now
the difference is really low which is what these authors are talking all right i'm just going to
continue on because we do have a ton more to do so that's still on the perception side we're not talking
about where we're going to go walking we're talking about the sound of the cat and where the cat is
located in the inference and so we're still within this empirical variational catference area this is
the bowl this is fitting that distribution the conjoint distribution that's the free energy
distribution and that is the one that's bull like so here is the variational free energy the black line
and it's basically the composition of two factors penalty for overfitting and the penalty for failing
to explain the data and each of those have a certain distribution underneath them in this setting so
their combination is like f plus g of x it's like h of x it's just adding functions together so it's just
another cost fitting function for the really specific kinds of models that we're talking about
here let's bring in action so now it's still the same case of w and x going to the agent now notice
that the agent wasn't drawn in the previous model it was just w to x so that was um probably a graphical
as well as somewhat of a conceptual uh simplification like i mean these measurements it shouldn't matter who's
observing them right oh wait quantum it does but now the agent can also take action z so z is going to be
the whole question of control theory and cybernetics and action the previous section dealt with inference
rule how to choose q of world states beliefs on world states this section is about acting now suppose you
can perform an action z that will place the cat in one of two rooms by changing the hidden state w
you can indirectly change future values of x or at least change their proportions or their likelihood
so decision rules stem from measures of preference because if you don't know where you're going you're
lost or if you don't care about the two things then it doesn't really matter one of the confusing
aspects of active inference is that it treats the statistical model p the one that is the actual
distribution we're trying to get close to and this is like the key point that we'll be returning to
for our whole life that model p is a measure of both probabilities and preferences at the same time
and that's going to be what we continue to talk about because it's one of the most important points
that this paper makes clear in a way that other papers um haven't really perhaps harped on in exactly
the same way let's look at figure three again look at the yellow part active inference employs a
controversial dual interpretation of p of w probability of world states and probability of
observations as probability distributions and preference distributions over hidden states and sensory
states specifically dean with the red text again i don't want to take up a bunch of time but this
we're having one of the authors or a few of the authors on we can probably pull this out a little
bit but for now that when we when we introduce preferences and probabilities it isn't just a second
it isn't just a second consideration it can almost run away from us really really quickly if we're not
really careful in terms of pulling back on the reins a little bit and really thinking about what does that
imply so i'll just leave that for there for now great point thanks for sharing it succinctly
they write recall that free energy principle inference counsels choosing beliefs by minimizing a function
that measures the cost of inaccuracy and that's because the free energy calculation includes both of
those very uh features the overfitting penalty and the failure to explain penalty action selection is
governed in the same way as inference remember we were talking only about inference when we were talking
about the variational methods now there's going to be a twist a slightly different cost function
called the expected free energy so that's why we were previously just talking about the f
variational free energy now we're going to be talking about g expected free energy labeled g
the definition of g is closely related to that of f the interpretation of the two penalty terms changes
as the formalism is updated to reflect the fact we are now making measurements over expected future
states so this is not just measurement error there's the fundamental unknowingness of the future since
future states have yet to be observed the agent must average over them to obtain expected values
the penalties are associated with failing to satisfy preferences and failing to minimize future surprise
overfitting preferences failure to explain surprise expectation preferences preferences when now or then
let's look at how those play out in this sort of action selection through variational free energy
through time aka the expected free energy formulation and how those two pieces satisfying preference failure
and failure to minimize future surprise look now but this is sort of the elaboration or the cousin of this one
this is like snapshot inference and now we're going to be looking at expectations through time
okay so first feeling to satisfy preferences so again keep that simpler version in mind this is going to be a slightly different one in six
they even write compare equation two
um this is make i hope failure feeling to satisfy preferences given a clear enough term but it totally brings in something different which is
something about the agent as dean wrote so there's big implications of course because there can't be a non-preference driven action selection
in any useful sense whereas the variational one was just like given the scatter i want the best mesh and regression
that one it does embody implicit assumptions about the world and so on but this takes it to a whole another level
and here's where that controversial dual interpretation comes into play not only is it unusual to treat p as a preference distribution
it is unusual to treat the goal of decision making to produce a distribution that matches that distribution rather than maximizing expected utility
so you don't need a preference distribution other than more for reward learning whereas here
we're trying to realize our preferences and match distributions rather than maximize for minimizing the divergence from
these realistic but optimistic expectations so perhaps it is best to keep in mind that preference in this sense
might mean something different than utility in the traditional sense
the difference
steven
yeah without going back into that but the whole point of having this matching distributions rather than
expected utility which effectively again becomes kind of like equilibrium states places where things settle and can
be measured and they're kind of stable you're in this kind of realm of a more fluid flux type process
um so i think that's that's one thing and i think the other one is um this focus on the future the focus on
predicting and things going into the future and how to make sense of that rather than looking back
and trying to which is often what science is doing is and explain retrospectively
in the same way psychology is often trying to explain what it sees before it and coaching psychology is trying to
see what can be done to get closer to something that's more suited great point thank you it really embodies
the forward-lookingness rather than the optimal reward or prediction on previous observations all right so failure to
minimize future surprise this is the other term failure to satisfy preferences now failure to minimize future surprise
formalism seven one of the tenets of active inference is that agents should act this is in the normative
stance to ensure that future data are not too surprising and so here is the formalism as written
this is the failure to minimize surprise in addition to conditionalizing on z z is action so we know that
the vertical line is conditioning on and then z are the affordances like the action states in this simple
example we're not going to go into the markov to the policy into the action state yet this is from the
simpler cybernetic or sort of agent environment framing that doesn't distinguish that as clearly
but z is just an action
that the agent engages in
the failure to minimize future surprise is conditioned on z
so it's not that there's some sort of world that we're not altering and then we're doing some strategy in that in
alterable world
leading to this total
ad hoc way of integrating the outcomes of action into the niche
the world states in the future have expectations that must be calculated as expecting on policy selection
so it's not just that some policies have effect and some don't it's that the inference of
the future failure to minimize surprise is conditioned statistically in the algorithm on the choices
the future of the future
so that is one of the cool parts about this calculation
um and then
this expected free energy okay steven yes go ahead
that also brings in an element of this contextuality it says it's what sort of choices
were made then in context x or well let's not use that context right it's important and uh
it changes things and you can't do that if you're taking averages um and sort of pre-built models
okay so now just like we kind of looked at the two parts separately and then summated into
f the variational free energy and then looked at those two parts here we've gotten to equation
eight in the paper which is g which is a function of those two distributions p and q as well as action
and here are those two pieces that we just discussed and then they write the third input to g
g is z rather than x so not observations but action as mentioned above this is because we are
calculating the expected value over possible future sensory states rather than inferring on
the basis of a sensory state that has just occurred okay so that's exactly what stephen said f is really
good for sensory inference it's about given the just observed sensory data what the estimate of the world
should snap to but action is totally different not just because it entails preferences like dean raised
but also because the consequences of action and the future are unknown so the distribution for
planning as inference for action as inference rather than for perception as inference needs to require
conditionalizing on action not on sense even though sense does come into play it's a little bit like
hidden away here's that what we're getting at which is the sensory distribution noticeably not here
but on the right side only and then the function that we're minimizing on is action inference active
inference as with f the measure g suggests a principle free energy principle in terms of action not as
inference is minimizing the free energy on action selection that can be read as an approximation of not
optimal bayesian sensing but optimal bayesian design of experiments and optimal bayesian decision theory
dean
and i think right here is i'm just pausing for one second i think that we're going to get into some more
evidence of this but i think this is the first moment when we can say active inference and free energy well not free energy
and this is the first moment of the time that we can say active inference does not necessarily constrain itself to being just a framework
it's actually a filter as well because of the active part it's not stable it's constantly being updated because of that active piece and the preference piece so we could call it a framework but i don't think we're doing it justice there's a framework aspect to it and there's a filtering piece to it and so that's why i talk about search fields all the time
so i just want to drop that seed now so that when the authors come on we can talk about that a little bit more in terms of the context that stephen mentioned about guiding
awesome thank you so now we're going to return to the active cat fronts so let us present a solution to the cat example for the problem to have a determinate solution we need the conditional distribution world states condition on action z
that means that the consequences of action have to be estimated if we put the cat in the kitchen it usually stays there so this is again the two pieces that action introduces into the puzzle is the question of preference otherwise why bother and the question of the consequences of action so the red is a statement that's empirically observed from observed data about what happens what happens when you are estimating location and the consequences of action is the question of the consequences of action and the consequences of action.
so the red is a statement that's empirically observed from observed data about what happens what happens when you are estimating location conditioned on action this is that q of w conditioned on z and so you can see when it goes into the kitchen it stays in the kitchen nine out of ten times whereas if it puts in the bedroom after some period of time like steven brought up not one millisecond later but one hour later one minute later it's model specific so that's a
it's time scale friendly it's time scale friendly it's not time scale free and then you can compute numbers having to do with action selection within this model it is worth restating how unusual it is to interpret p as a measure of both probabilities and preferences but i mean it's the letter p there's nothing wrong with treating a distribution as a measure of preferences distributions don't demand to be interpreted as probabilities after all
but what is unorthodox in what church and in need of justification is giving the very same mathematical term two different interpretations within the same equation so that's the two eyes at once kind of looking back and then they go into a little bit more detail about what that actually means we are not aware of proponents of active inference taking this interpretive line but it appears to be a viable option so just awesome
and clear writing and clear writing and drawing something out through the re-understanding and the communication which happens synchronously and asynchronously
one of the ways proponents of the framework turn to this unusual interpretation to their advantage is by casting action as a form of inference so here's from a buckley citation and that's why it's called active inference
and we just kind of a mechanism underlying minimizing expected free energy is formally symmetric to perceptual inference
formally symmetric overfitting failing to satisfy preferences failure to explain the data failure to minimize expected surprise on future data that's why it's the only one that has the x in there
rather than inferring the cause of sensory data an organism must infer actions that best make sensory data accord with an internal representation of the environment
statistical representation not the debate on whether organisms have representations
2.4 simple model of selection this is where the markov blanket is going to enter in our model x and z are the inputs and outputs of the agents x observations z actions
the set x and z is the agents markov blanket the term is derived from judea pearl's work on inference using bayesian networks
pearl 1988 classic citation other live streams we talk more about markov blankets so we're not going to go into it too much more here
but it's definitely the tip of an iceberg if you want to check out more but here in the sense required here
a markov blanket can be understood as the set of nodes that screen off the agent from nodes considered external to it
screen off the agent or screen off the internal states of the statistical model
another toy model will help illustrate consider an agent whose service temperature x can safely lie between negative 4 and 4 units
temperature is continuous okay but it's a discrete model
and so here death is coming into the picture on either end too hot and too cold
so this is going to be like variational catference but now it's a freezing and a burning end of the room
and the cat or the robot cat is going to be making decisions about what to do
so the external world state is w the temperature and then the perception is going to be x the observation
notice that the value of w does not affect the agent's preferences
so the preferences for living or for homeostasis or whatever regardless of the observations in that snapshot moment
but not precluded over longer time scales
all the agent directly cares about is its surface temperature denoted by x
that's why the two rows are identical
so these are sort of the observations and the different actions that can be taken to move
between one end and the other perceiving only the temperature
the agent tries to guess how to act how to stay within its expected range
and then this is sort of the intuitive pseudocode
when the temperature is high you want to go towards the lower end
when the temperature is low you want to act to go towards the higher end
and so here is like the simple example this is kind of like the bacteria that has the right priors
versus the one that's just deciding randomly or without any resemblance of relationship to the other observations
and so here is the smart agent that's just keeping its free energy every time it gets up as it moves away
it acts to bring it back down into alignment
and then here's um the agent's control over its external state is 95 accurate
so five percent of the time it slips and then that's what they say it's grasp slips
the optimal control the handle has been lost because of a motor ineffectuality
but that can be recovered whereas the randomly acting or just sort of like the sort of brownian
walk diffusion process ends up dying
okay dean
all i was going to say here is is did it create did a great explanation
and if this was your first encounter with the w and the zed
and the x you'd have to really really slow this down
because the first time you encounter it it it it takes more than one pass
you might have to go over it a third and a fifth and a seventh time for it to actually make sense
because there is we all have a certain capacity in terms of the amount of variables we can juggle at once
and i was when i first looked at this it it made sense to me but i could sense
from somebody who's maybe coming from a philosophical background
and not necessarily having the same degree of statistical
um hands-on experience as maybe the three of us do
this would be a moment where you'd really want somebody to hold your hand
that's what community and act in flab is for
because then it can be like an interaction and every question is welcome
so as long as there's attention in the game
everybody's going to make it steven
so this also does give an indication that
with variational free energy having some sort of perturbations can be useful
particularly if you have multiple um parallel kind of sources of information
being integrated
so having some noise is a good thing right it's not it's actually gives you a way to start to
make inferences one question is there
that on the left there's no real learning happening
no it's just but it still makes it even without the learning component it still is more stable
um yes it's not doing parameter updating
it's just like um a previously learned association
between the temperature and the direction to move
and also notice like the observation of sensory is assumed to be perfect here
so there's many layers which can be brought in
but this is kind of like the kernel motif
okay
the correspondence between high values of f
and life-threatening states lead to a third form of the free energy principle
so we had inference and action
perceptual inference
then we had action selection
and here is free energy principle selection
any system that survives long enough
will act so as to appear to be minimizing f
that's the first time we got any discussion of
far from equilibrium
thermodynamics
of anti-dissipative systems
resilient systems
anticipatory systems
except indirectly through action
but this is the sort of selective
darwinian side of fep
okay
of course there's a ton that could be said here
this is not a normative principle
not a suggestion to agents
regarding how they should perform inference
but a means of describing how agents behave
axel's paper
minimizing free energy is not living
alone
but living systems will be those that appear as if they've minimized free energy
and then here
i think someone wrote
i just wrote that in there because
yeah
that's going to tell you what your autobiography is going to sound like
given that you're still alive and can write one
yep
my last words are
ah
in recent work
friston gives a deflationary interpretation
on which agents
do not in fact minimize anything
but perform acts
which can be interpreted as minimizing f
so
see
live stream number 34
0 1 2 3
that is the reason
for the emphasized phrase
so as to appear to be minimizing f
that's
deflationary instrumentalism
highlight
despite this deflationary approach
there is a link between this and the earlier principle
agents subject to the free energy principle of inference
perceptual inference
ought to minimize f
so if this is ought
is tied to their survival
then the normative principle
has the same underlying justification
as the descriptive principle
so this is sort of
i don't know if it's been
noted before
but basically it's equivalent to saying
the evolutionary ought
is and is
so it's kind of like
not from
the fitness
side
the
malthusian
darwinian
side
but from the
anti-dissipative side
this is how things
have looked
it's like saying
fitness isn't necessarily
um
being projected
into the future
but if you do
do the computations
fitness can be assigned
to like
different single nucleotide polymorphisms
that have had different success
and you will only see successful ones
but it's a bit more complex than that in the moment
so
here are the three
piece
the tale of three piece
we had the tale of two densities
what other
what other jokes have we had
in each of the three examples
discussed in a section
there's been a distinct role
for the distribution p
and a distinct interpretation
of each model
narrow sense
in our first model
p was a generative model
employed by an agent
it was therefore interpreted
as representing
probabilities
like where the cat is
but now
in order to introduce action
in a meaningful way
we had to have preference
like I want the cat
to be in the kitchen
so when we brought action
into the game
we had to
introduce preference
what makes active inference
similar
but also different
from other frameworks
probabilities and preferences
are represented by p
in addition to representing probabilities
in the second model
p measured the desirability
of certain future states
over others
I expect you to go to school every day
that's something having to do with action
if it's serious
it was therefore interpreted
as representing preferences
in our third model
p tallied the historical frequencies
of a set of hypothetical ancestors
fitness
it was therefore interpreted
as representing the fitness
of different states
so
supporters of the framework
often point to the third role
fitness
p h
to explain how p
can simultaneously
fulfill the first two
it's like
if that thermal bacteria
is
rocking its niche
it will have high fitness
okay
so
that is
where the three p's
get us
here's just a brief
look forward
so for any of these next slides
we're not going to go into
the actual
very nicely fleshed out
arguments themselves
but
Stephen or Dean
just raise your hand
if either of you have anything
to add on like
each of these
section headers
so
um
section 2.5
is extensions to the model
more things to learn
more ways to act
we've seen
adjectives added to
active inference
deep
sophisticated
contrastive
affective
what other adjectives
have we seen
that's sort of this
section of the guidebook
it's like
there's your um
usb port
what can you
have
added into it
or how can it be developed
and so
that's where we see
sort of the adjectival
family
of something
active inference
maybe even
n
active inference
coming more to the
philosophy side
but also
there's all the
elaborations that we've
seen of the actual
parametric model
in the narrow sense
sometimes
it's in both
camps
like affective
inference
has to do
with
a model
derivation
or metacognition
as well as
something about
like the model
in a bigger sense
but
we
can recognize
both those
lanes at once
Stephen
yeah I mean
one other one's
inactive
inference
uh
reciprocal
active inference
there's a couple more
like that's definitely
uh definitely
true
just one thing I was
going to throw in
I noticed they talked
about this
and it's I know it's in
the quote but
they talk about any
system
I always wonder whether
that's a bit of a
that a little bit of a
piece of a paving stone
waiting to be tripped
over
um
because I kind of feel
like
you know
if you're going to
say it maybe
any non-linear
dynamical system
or nested
systems
of systems
or things
I just always
think that
that can be
a little bit
of a
hazard
yeah it inherits
a lot of the
legacy
ambiguity
around system
like you've brought
up a bunch of
times
so it's really
helpful
so
in section
three
notice how
the history
brief history
of the free
energy principle
comes after
what we just
spent the last
hours and pages
on
so it isn't
a history of
science perspective
but it is being
recognized as
important
and so the free
energy principle
is a modern
incarnation of
ideas that have
been raised
sporadically
over at least
the five
decades
it combines
traditions from
physics
biology
neuroscience
and machine
learning
and other
areas
especially
the modifications
and increasingly
the applications
and it's a
bi-directional
freeway
it's not just
two lanes
in both
direction
it's going
both ways
so this is
sort of the
history
which is fun
because it's
a recent
history
in some
parts
okay
section four
moves from
the historical
to the philosophical
so section four
dialectic
the free
energy principle
and related
claims
mathematical
empirical
and general
claims
section 4.1
this is where
all that
mathematics
groundwork
pays off
because in
the author's
words we think
a great deal
of confusion
can be overcome
by considering
three kinds
of claims
first there are
mathematical
claims
those were the
ones that were
just brought up
in earlier
sections
so that's
the theorems
the scientific
models and the
statistical
techniques
in the more
narrow sense
and by doing
good scholarship
we show that
the core features
absolutely
predate
active
inference
and there's
less
controversial
than some
might suspect
however
Fristin colleagues
have since
introduced many
novel mathematical
elements
like the
perception
and action
interpretation
on the
Markov blanket
importantly
claims in this
category do not
need to be
interpreted as
statements about
real systems
in order to be
evaluated
so part one
is
it's
instrumentalism
part two
is
separate the
parts that
predate active
inference from
some of these
more recent
derivations
even within
the only
technical
area
second area
of confusion
or the second
way that confusion
can be overcome
by considering
another kind of
claim is
partitioning off
you know we can
add like a line
here from that
mathematical
everything that
was in the
section that we
just discussed
plus stuff that
was more recent
like 32
there are
empirical claims
about cognitive
and biological
systems how
brains and
bodies actually
work
these are the
remit of
cognitive
neuroscience and
biology so
those are
empirical
biological
claims
third are
general claims
that typically
abstract across
a wide range
or by class
of empirical
claims so
that's like
the sort of
everything
nested systems
collective
behavior angle
so separating
those and maybe
there's more
is really helpful
because sometimes
people say well
this general
claim is true
because look at
how this
in the skin
works well
what about the
skin well
that look at
how the math
works
and why does
the math
work that
way because
of the
general
claim
is that
an argument
what is
the justification
and the links
among these
dialectical
categories
well if there's
three kinds of
claims
mathematical
empirical
and general
then there
are all the
edges of that
triangle
if you had a
fourth one
you'd have all
the edges
of a tetrahedra
and then you'd
almost have a
model
the mathematical
to empirical
direction
invites
philosophical
analysis
due to
novel
interpretations
of scientific
model terms
so how can
math be used
to justify
empirical claims
why does
equations
have anything
to do
with what
people say
about the
brain
and the
body
and the
niche
why is that
justified
at all
other than
just other
people in
their epistemic
authority
have done
it or it's
how it has
been done
Stephen
instrumentalism
also
it gives
a kind
of a
bridge
between
realist
science
and applied
science
and it's
kind of
sitting
somewhere
between
the two
so I
think
that's
quite a
useful
piece
that this
adds
to
the
equation
nice
and then
the last
two
edges
of that
triangle
are
how can
mathematical
not both
directions
on each
edge
you could
add
but how
can
mathematical
claims
justify
general
claims
well how
could you
say that
about
nested
systems
about
nested
markov
blankets
the
math
okay
that's
important
to
investigate
and how
can
general
claims
justify
empirical
claims
how
could you
say that
about
the
ants
well
fitness
or
dissipative
systems
so how
can
general
systems
claims
justify
anything
about
empirics
so those
are some
of the
edges
of these
three
kinds
of
claims
and
there's
also
claims
and
sub
claims
which
is
why
it's
really
important
to have
rhetorical
ecosystem
mapping
and an
ontology
for active
inference
so that
we can
actually
learn and
apply
across
languages
and through
time
Stephen
yeah
and I
think
also
we can
think
of
this
as
structural
and
functional
insights
being
gained
rather
than
necessary
repeatable
measured
outcomes
every time
being
gained
so
there's
an idea
that
these
insights
might
reveal
something
about
the
structure
or
the
functionality
of
the
dynamics
knowing
that
no
one
simulation
may
ever
be
repeated
quite
the
same
way
yes
so
the
concluding
remarks
the
active
inference
framework
is
incredibly
ambitious
is it
the
framework
or the
people
in its
explanatory
scope
from
humble
beginnings
as a
theory
of
brain
function
it
is
now
positioned
as a
framework
for
understanding
life
itself
there
is a
critical
tradition
in
the
philosophy
of
biology
inspired
by
Richard
Levins
with
regard
to
such
ambitions
many
then
will
approach
active
inference
with
skepticism
healthy
skepticism
is a
good
thing
but
healthy
skepticism
is
informed
skepticism
unfortunately
getting
one's
head
around
the
details
of
active
inference
is
no
small
task
our
goal
in
this
introduction
has
been
to
clarify
the
basic
mathematics
history
and
internal
dialectics
of
active
inference
in
that
order
those
were
the
sections
and
draw
attention
to
some
key
concerns
with
these
details
on the
table
philosophers
of
biology
are
in
a
better
position
to
critically
evaluate
the
framework
we look
forward
with
interest
to
seeing
the
results
classic
future
looking
last
sentence
so
that's
the
final
lines
we
have
a
ton
of
things
to
discuss
in
37.1
and 2
it'd be
awesome
to have
any
of the
authors
as well
as any
other
people
who just
want to
jump on
for a
returning
or a
first time
discussion
but we'll
close
under the
buzzer
in the
third
period
I know
that's
how they
count up
there
Dean
so
any
final
comments
on
just
what you're
looking forward
to
discussing
Dean
first
because you
never get
the last
word
at the
end
Steven
yeah
I don't
want the
last
word
so
one of
the
things
I want
to talk
about
in the
point
one
is
the
general
claims
because
I get
to trot
out one
of my
favorite
parables
that I
made up
which is
three
functions
walk
into
a
bar
and I
want
to be
able
to
because
I
get
lots
of
mileage
out
of
that
and
whether
it's
three
functions
or
probability
preference
and
fit
the
same
holds
true
it
can
be
great
taste
and
less
filling
so
I
want
to
have
a
look
at
that
because
I
think
that
really
tags
onto
the
idea
that
what
they're
talking
about
here
in
terms
of
a
guide
could
also
set
us
up
really
well
for
creativity
and
then
I
also
want
to
be
able
to
say
that
that
creativity
isn't
because
we're
framed
in
but
because
we
especially
if we
speak
to
the
authors
these
first
principles
of
hidden
states
and
inferences
and
which
ones
are
selected
and
which
data
is
available
to
actually
make
inferences
on
can
be
used
particularly
for me
the example
of
psychology
versus
coaching
psychology
and
that
type
of
paradigm
shift
awesome
yeah
I really
appreciated
both
of your
perspectives
on this
paper
it really
shows
how
different
life
experiences
can be
in
conversation
with
some
of
the
technical
details
so
thank
you
both
and
for
everybody
who's
watching
and
participating
see you
around
the
lab
see you
in
the
upcoming
weeks
for
.1
.2
peace
thanks
guys
bye
!

















Thank you.
