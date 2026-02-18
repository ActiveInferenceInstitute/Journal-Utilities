---
title: "Active Inference LiveStream 054.1 ~ “...Compositional Account of the Bayesian Brain” (Smithe)"
category: "Livestream"
series: "Livestream_054"
episode: "1"
speakers:
  - "(Smithe)"
duration: "1:53:01"
url: "https://www.youtube.com/watch?v=fzFDvJhrn0U"
views: 325
exported_at: "2026-02-18T22:37:37.880257+00:00"
format: markdown
---

# Active Inference LiveStream 054.1 ~ “...Compositional Account of the Bayesian Brain” (Smithe)

Hello and welcome. It's June 7th, 2023. We're in ACTIMF livestream 54.1 discussing
mathematical foundations for a compositional account of the Bayesian brain. So, welcome to
the ACTIMF Institute. We're a participatory online institute that is communicating, learning,
and practicing applied active inference. This is recorded in an archived livestream, so please
provide feedback so we can improve our work. All backgrounds and perspectives are welcome,
and we'll be following video etiquette for livestreams. To learn more about livestreams
and other projects, head over to activeinference.org. And we're here today in ACTIMF stream 54.1.
We are in our first discussion with the author of the work Mathematical Foundations for a
Compositional Account of the Bayesian Brain. Today in 54.1, we're going to say hello, then be on with it
and see where it all goes together. So, we'll begin with introductions. I'm Daniel. I'm a researcher in
California. Six months ago, I was quite unfamiliar with category theory and have had quite a fun
journey with Ali and Dean and I guess Toby via Stigmurgic Proxy. So, really looking forward to
this discussion and I'll pass to Dean and then Ali. Thanks, Daniel. I'm Dean. I'm here in Calgary.
My goal in joining this group was to take the idea, as we got in the one of the previous slides,
the idea of practicing applied active inference. I see the potential through category theory of making
that even more accessible, more possible. And so, I'm really excited to have the author with us today and
maybe have a look at what that means. I'll pass it over to Ali.
Hello, I'm Ali. I'm an independent researcher from your run.
I'm a professor from your run. And as I said in Datz Zero, I'm quite excited to be here to discuss
this magnificent dissertation with its author. And well, I mean, in the past several months, we did our
best to understand and dissect it as best as we could. But obviously, we have many, many questions
that I'm looking forward to discuss them with.
So, Toby, thanks again for joining. Please lead us off with just any introduction and background
that's going to set the stage, maybe how the work came to be. And that would be great. So, thanks again.
For sure. Yes. Great. No, well, thanks, Dan, and all of you guys for hosting me and for having the
courage to read my thesis, which, as you noticed, it's a kind of strange mix of things. It's kind of
both the research work. And as I noticed, what are you saying in the previous stream,
it's at this kind of frontier of knowledge? And of course, it needs to be. But I also, because this
language is so unfamiliar to people, and because I think it will prove to be very useful across the
sciences, I really wanted to make it kind of legible to people. So, you know, for people to read the
thesis, but also like my research, and kind of understand what I was saying, effectively,
how it came about was, yeah, I was supposed to be studying interactions between frontal cortex and
hippocampal circuits in the brain. And at the sort of time of trying to get started with that,
obviously, I was kind of interested in the free energy principle and active inference and all of that.
But I found that there was a lot of kind of, you know, as I said in the thesis, and as you talked
about in the previous stream, and probably in discussions before that as well, there's a lot of
kind of, you know, each research group has its own language. And these different groups, you know, they
don't necessarily talk to each other in a way that is kind of an efficient kind of communication. Each
group of people is interested in their own thing. And one of the things I like about
the free energy principle and about active inference is that it's this nice sort of general framework for
adaptive systems. And so it is in itself a good place to kind of situate an understanding of systems
like the brain and other adaptive systems. But of course, it doesn't, you know, immediately resolve this
problem of, well, the problem that was for me a kind of confusion about like, what's going on in
these circuits? And how should I understand what one person says in relationship to what another person
says about, you know, this bit of the brain or this interaction. And so, in the process of kind of trying
to understand what was going on there, and to resolve in part, the confusion I had about predictive
coding itself, and the complexities of all these models I was encountering, I kind of resolved to
replace that confusion with another kind of confusion, which is, you know, what is all this crazy category
theory stuff? And, you know, so you might think, okay, well, that's mad, what's the point of that,
you've just made everybody's life a lot harder. It's kind of like that XKCD comic, where you've got all
of these different standards, and, you know, we decide to like, come together and, and make a new
standard. And in fact, this is happening, I think, and like, I don't know what it was in,
in cellular biology, maybe I had John Byers talking about this yesterday, but, you know, they have lots
of different standards for writing down diagrams, but describing like interacting, like biological
processes, and the kind of scientific community in that area has set up a kind of mediating body to
kind of try to, you know, form, like bring together all of these diagram languages. But they weren't
really able to do so. So they still, they instead of just coming up with one new standard, they came
up with three new standards to try to unify these things. And the trouble, you know, I had or have with
these different languages, or different sort of syntaxes for talking about scientific things is that
not only are they all different, but they're kind of all ad hoc. And so the reason why I feel that there's
promise in replacing this confusion of this, of so many different ideas, I mean, of girls, it's great
to have this kind of ecosystem of ideas about how these complicated systems work. But it's still very
ad hoc and confusing. And so instead of just coming up with a new ad hoc and confusing way of understanding
these things, I was kind of hoping to use a language which is maybe kind of universal in some
sense, like it's really about, or it's really capturing like how we think, and maybe also like
how the world is actually, you know, built up. But in particular, it seems to capture something of how
we think. And so, you know, the fundamental theorem of category theory says that you shall know a concept
by the company it keeps to adapt the kind of that that sort of motto of, I think, birth from
linguistics, that you should know a word by the company it keeps. That's really like at the heart
of how we come to understand things in the world. And I think the maths that is category theory captures
that very nicely and very precisely, and at the same time enforces a kind of discipline. And so I know it
is quite like hard going reading this kind of research work, this kind of introduction to all this new
stuff. But, you know, in part that's because, you know, when you're being disciplined is hard and
doing things very formally precisely does require a bit of, well, you know, a lot of dedication.
But that isn't to say that it's not worth it, or that these ideas even used a bit informally
somewhere down the line might not be useful, at least to sort of frame the way we think about things.
So I hope to be, you know, some use in helping not only sort of change the confusions that we have,
but also like modulate them in a kind of way that will be sort of useful for people.
Awesome. Great starting place. Ali or Dean, where can we begin? How can we replace some of our
prior confusions with a new and different confusion?
Ali, want to go first?
Ali, can I ask a quick question to Toby? Toby, when you were talking about when you actually saw
all of these standards, so you know, you were the sort of what you were the, you were the hub of all
of these standards you saw sort of all around you. Can you maybe speak to the idea of what you perceived,
or what you sensed was the stabilizing function of those standards, but also the searching function?
Because of course, you had gone out and realized there were all of these different standards at play.
I remember it in a previous professional life of mine, having to have chief financial officers and their
math, sit at the table with engineers and their math, and them talking right past one another,
and making no sense to each other. And I had to be kind of the medium between them, so that their math
would actually get a little bit sticky. And they'd be actually able to understand and interpret one
another. In your experience with this, how did that play out the both the stabilization through the
standards and the search? Well, I guess I should begin by saying that I'm, this is still, this is
still like ongoing, and nor am I an expert in all of these different standards. But the thing that I
kind of at least noticed, right, that was that people use languages like Bayesian inference or
reinforcement learning, or dynamical systems to talk about certain bits of the brain that I was interested
in. And they kind of just plug all these ideas together. And it's sometimes, and it's fine. So
you want to write a paper, and it's about a particular phenomenon. And it's great, you maybe come up with
some nice model, and you, you know, you put people in MRI scanners, and that the quantities in the, you
know, in the sort of bold signal correspond to quantities in your model. And that's, that's great,
it says that maybe this bit of the brain is doing that. I mean, we can argue about MRI at some other
time, but it doesn't really tell you about how that little model you've got interacts with the rest of
the brain or the rest of the world. And so if you care about like this whole complicated thing, you want
to know how do these parts actually talk to each other. And so I was just fortunate at this kind of
beginning of this, in some sense, to be in the right place, the right time. So I kind of knew there
were these different, you know, ingredients all being put into these different models. And, you know,
only, you know, I'm only sort of familiar with some of them, but I could still see that they had sort of
similar structure. And that was in part because I've been going to, you know, some applied category
theory meetings or talks and seen that say economic games, which are very closely related to
reinforcement learning, have this kind of bi-directional structure where an agent tries to
sort of effectively, in some sense, choose, they make an observation and they sort of do this kind of
forward projecting kind of thing of choosing an action at the same time as saying, okay, well,
if supposing I take this action, like what would the payoff be? And that's this kind of backwards
facing thing. And then you can sort of chain that process and think, well, if I do this in multiple
stages, like how does the utility I get at the end of this, you know, multi-stage process, like feed
back to the utility I'm going to get having taken just one step right now. And that's kind of,
that's a similar sort of bi-directional thing to what happens in active, or like in, well,
in predictive coding specifically, where like a little circuit is saying, okay, well, I need,
given the, my like high level beliefs about what's causing this like sensory data, I need to sort of
retrofit the actual sensory data to kind of come up with a new belief about what those causes are.
And so that seemed to me to have the same kind of structure. A similar thing also happens in
backprop in machine learning where you have, say, some neural network and it kind of, you know,
you feed forward some information through the network and it say does a classification.
And then you have some, some training system which says, okay, well, actually you have this error and
then you need to sort of back propagate that to update, you know, say some part of the model on the
basis of that. And so that also has this kind of bi-directional structure. And it just was fortunate
that at this time people were talking, talking a lot about these kind of bi-directional processes.
And, you know, so I was thinking about these things at the same time I was kind of thinking about,
you know, the application of Bayesian inference. And I kind of noticed that, you know, they had the
same structure and I kind of wanted to figure out what was going on there. Like really sort of pin down
what, what it was that made like this kind of predictive coding circuit have this kind of
shape in some sense, because as I think you've also talked about, and I kind of mentioned a few
minutes ago that, you know, individual predictive coding circuit isn't an isolated system, right? It's
part of like this hierarchical thing. And so you have one little circuit connected to another circuit.
And that whole conglomeration of circuitry is supposed to do something quite grand, but at the
same time, it's made of smaller parts. And I think that the main, one of the major confusions I had at
the beginning was, okay, so you have this like big generative model with lots and lots of factors,
and you go through it and you try to derive like the differential equations that give you the sort
of predictive coding dynamics by saying, okay, well, you know, we're going to minimize the free energy.
And you have this complicated thing with lots of sums in it. And it seems like very intimidating to try
to like come up with that differential equation, even though actually, when you sort of look at this,
the kind of the look at the process that you're doing is quite kind of mechanical because effectively
you're doing the same transformation to each factor of this model. And so that also hinted that there
was this kind of compositionality thing going on in these systems. Okay, you not only do you see that
these kind of this bit of the brain is has this kind of modularity, but you also get a sense of that
modularity in that derivation you're doing. And so what I wanted to do was to capture both of these
things. One is the kind of shape of the circuitry and the other is like how to somehow save the effort
of having to kind of re-derive everything for each different case. And that kind of formalization of
this process corresponds to a kind of functoriality you get when effectively the functoriality means you
preserve compositional structure. And so what you want to do is you want to say, okay, well, what's the
compositional structure of the thing that the functor starts with, like the process starts with, and
that's the compositional structure of Bayesian inference itself. And then you want to say, okay,
well, what's the compositional structure of the kind of dynamical systems, which is the thing you're trying
to get to, and how do you map from one to the other in a way that preserves that structure. And so that's
kind of what I was doing in this thesis is just saying, okay, well, what are the structures I need and how do I
relate to them? And, you know, it turned out that there were a lot of details that I had to write
them all down. But the kind of basic idea, I hope, is quite simple. It's just trying to say, what are
those kind of simple, like the kind of individual components, like the kind of Lego blocks, and how do
they like connect together? And how can I sort of, you know, relate this, the kind of Lego blocks of one
thing with the Lego blocks of another in a way that's kind of preserves the shapes. And so, yeah,
it's kind of this kind of mammoth thing. But the kind of fundamental idea is quite simple. And I think
it's kind of like how when, if you're like programming a computer, you can write in a high-level language,
or you can write in like low-level language. And if you wanted to, you could write in assembly language.
And category theory is like a language where you start with the kind of assembly language,
and you build up a high-level language within the language itself, in some sense. And so,
if you really want to start with, at the very beginning, like I did, with the definition of
category, and then build up to this big thing, you have to make a lot of steps. Because like, assembly
language is really simple. And it's, you know, it's just like single instructions that your
processor does. And so getting all the way to something like Zoom that can do a video call is
quite complicated. And so people don't, they start with the high-level language. But the thing that
people strive for in designing high-level languages is to set them up in such a way that they're sort of,
that the abstractions are quite nice or sort of modular. And so that's what I'm trying to do with using
category theory is to kind of find abstractions that are modular in a similar kind of way. And I know
on the previous call, Dan, you mentioned the kind of analogy between like, typing in this category
theoretic sense, and in the programming sense, and they're quite similar. The category theory sense is
kind of a much sort of more general, bigger idea, it has a lot, it sort of encompasses all kinds of
things. But you could imagine somewhere down the line, having a programming language, and that, you
know, people are trying to build these things, but having a programming language where you could express
anything you could in, you know, category theory, and, you know, I, to be honest, find it quite intense,
and quite sometimes mechanical and tedious, I had to prove that certain categorical structure
satisfies the coherence conditions that it has to satisfy, like, you know, lacks associativity or
monoidality or something like this. There are a lot of like, diagrams, you have to check commute or
something, and much of the time, that checking is quite tedious. And someday, I hope that we'll have
tools that we can say, okay, well, I'm going to spell out what my structure is. And the tool will just
check that it satisfies all the axioms. And so, you know, I know you guys have to wade through a lot of
that stuff in the thesis, but it's kind of manually necessary right now, but in the future, it might not
be. And then we can use this high level language in a much more kind of liberal way. I hope that'd be
great. Sorry, I've been watching all for ages. So I'll stop there.
Awesome. Great. I'll go to a question in the chat. Mark wrote, applied category theory and active
inference have tremendous promise. I confess I have not yet read this dissertation. It would be helpful
to describe a specific engineering application for the work. So what do you see as proximate and
and or distal engineering applications here?
So one of the things that I hope could be produced soon as an engineering application is a sort of
general modeling framework for building kind of complicated active inference systems that might
include lots of parts, lots of agents, kind of like
something that my colleague Jules Hedges wants in cybernetics more generally, something like
a kind of programming language maybe that incorporates
all of these kind of strange cybernetic structures I mentioned earlier, like reinforcement learning and
like back propping machine learning and Bayesian inference, they all have this kind of
bi-directionality. And so you should be able to have this kind of modeling environment which allows you
to incorporate all of these things in a kind of nice way. But I think before we get something quite as
grand as a whole new sort of modeling environment, I think just having tools to help us build
you know, approximate and active inference systems that are really nicely compositional is one thing that I
you know, hope to come out of this. To be honest, I don't know very well what the general tooling is like
for this kind of thing right now. I know that there's SBM, I know that there's like
PyMDP for certain kinds of problems, but I don't know how sort of general they are.
Another thing that you would get if you have this kind of toolkit, because of the kind of modularity of
category theory is you should be able to plug it into other things that exist already. So one of the
things that's particularly of interest to me at the moment is kind of multi-agent systems
and sort of building, trying to understand how we could build something like or simulate things like
you know, something like a corporation or some kind of, you know, some kind of society structure where
you've got lots of active inference agents coming together to pursue a sort of common shared goal.
How can you kind of effectively distribute that goal sharing across systems? They could be like little
robotic systems say or something like that or agent or like, I don't know if it's precisely, I'm kind of
like an abstract thinker. But yeah, I think like being able to kind of control or like modulate the performance of these kind of
distributed multi-agent like active imprint systems might be quite a cool thing to be able to build.
So that's kind of like, I can maybe
flavor of the kind of thing that this tooling gives you.
I suppose for me, this particular work was really about
trying to encourage people to use this language to understand things more clearly.
So yeah, there's a lot of stuff that I hope we can understand. Well, at least I can understand more clearly.
Awesome. Thank you. Ali?
Thank you. Yes. So in this paper by Krzysztof Wojtovich,
are there category theoretical explanations of physical phenomena?
He argues that category theory by itself does not and cannot provide any mathematical explanations for
physical phenomena. So the idea here is that category theory is merely a meta theory to kind of
do a kind of bookkeeping or householding of the physical theories and it's not a tool to construct
the mathematical theory of physical phenomena itself.
I'm not sure I agree with this argument entirely because
in one sense, some of the most profound
aha moments in the history of science obviously results from looking at
pre-existing theory or a model from a novel angle. And I believe category theory can provide such
such novel perspectives even when looking at some established and pre-existing models of theories.
So what do you... I'm curious to know your opinion about this. So do you think category theory
can actually provide mathematical explanations for... I mean either in cognitive science, neuroscience or
or even other areas, other scientific disciplines as well?
I think it's a it's a subtle question. Right now it's probably largely the case that the role of category
theory is kind of this... I'm not... I think it's like like bookkeeping but like clarification too.
Bookkeeping if you think of it in a very general way of like trying to account for the things you're thinking about very precisely
and not sort of miss details like if you your books don't balance you kind of miss some payment or some debt.
I think that's quite a nice analogy. But I think one of the goals of
quite a lot of people or not maybe I mean a fair chunk of the community, particularly that which comes
from a sort of more abstract mathematical side of category theory, one of their goals is to try to recast
a lot of how we think in kind of purely categorical language. So one of the things that category theory
allows us to do is to kind of formalize in some sense patterns that crop up all over the place
using the notion of universal construction. And the thing about universal constructions is that
you have like some little pattern and if you know that you can instantiate that pattern in your category
that you have like some object which kind of captures the essence of that pattern. And you don't need to say
be able to kind of write down all of the specifics of that object sort of a priori because the kind of
universality gives you a recipe for constructing it. It gives you it in some sort of unique way. And so
you know that if you have this universality you can always you can always like access this object. And
yeah so I'm talking very generally but because of that one thing that people try to do is to try to say
okay well what it you know we've got these things that we're interested in in say physics like you know
the principle of least action or like the nature of space time or something like that.
Can we express those things as kind of universal constructions? Or for instance in a completely
different realm like we may have some process which is something we're interested in on the computer
like the migration of data in databases. Can we write that down in a way that doesn't have any kind
of ad hoc ingredients? It only is built from universal constructions. These are things that we can just
write down kind of abstract sort of axioms in the language of category theory and that kind of gives us
the process or the structure that we want. This kind of line of work is often called like synthetic
something like synthetic you know probability theory or synthetic physics or synthetic topology or
something like that. And it means you sort of start from these kinds of very high level categorical ideas
and then you sort of end up with a characterization of the essence of the thing you're interested in.
In physics a kind of a simple example of this which I supply in a kind of relatively feeble effort
to say that it's not true that category theory doesn't give you a characterization of things in
physics. So there is a category of say topological spaces and the morphisms between them are continuous functions.
And there's a morphism a category rather of sets and the morphism between the sets are functions.
And of course underlying every continuous function is a plane function. And so there is a functor from
the category of topological spaces to the category of sets which just forgets
the topological structure of the spaces because every topological space has an underlying set of points.
So you have this forgetful functor. And this forgetful functor has two adjoints. And one of the things
the category theory teaches you is that adjunctions give you this universality. So adjoint functors are characterized
uniquely by their kind of satisfaction of this adjunction property.
So these two adjoints to this forgetful functor, one gives you what are called discrete spaces.
So if you take a set you can turn it into a topological space by thinking of all the points
as little islands in this space. So there's no like connectivity between them.
And that's called a kind of discrete space on that set. And the other adjoint functor
gives you what's called the indiscreet or sometimes co-discreet space where all of the points are sort
of collected into one big like island. So they're also connected together. So it's like a sort of fully
connected graph.
And of course, that's very different from the discrete space. And it's different from like the
space time or the space that you live in, which has a particular kind of connectivity, like you can't
walk through walls. And so, you know, people try to use these things, particularly use adjunctions to
characterize things like properties of spaces. Another thing that comes out of a jointness,
is something that I can let you read about later, because it'll take me the rest of the talk to try to
explain. But you might be familiar from logic that you have these quantifiers, you have existential and
universal quantifiers. And you can do things with these quantifiers, like you can say, you can sort of
compose them together. So you get things like for all x there exists, for y is such that this.
And you can think sometimes of these composites, or these compositions of quantifiers,
as like maybe like modal operators, like you can sort of decompose necessity and possibility in terms of
the compositions of logical quantifiers. But the kind of weird thing about quantifiers is that they
too arise out of an adjunction. It's kind of like they are left and right adjoints to substitution. So
if you have a proposition, you can like substitute a term into it. And the adjunction, the adjoint
punctures to substitution give you the quantifiers. And you can sort of take this another step. And then you
can think about like composing these adjoint punctures, and those give you the modal operators.
And so that's something that comes just out of category theory, but is really sort of fundamental
in sort of logic. And you know, we might think there's a kind of close relationship between physics
and computation or physics and logic. Or, you know, physics and information and information and
computation and logic. So I think it's not quite true that there's nothing to be gained from
thinking about kind of traditional mathematical things, or traditional physical things using category
theory. In some sense, they, you know, doing that really clarifies the essence of them.
Because it tells you what their kind of universal properties are, and you can then like instantiate
those things in different contexts. So one of the things that you could do is start to think about
these kind of logical structures in different contexts. And that's kind of like what type theory
is all about. And you could use it to think about the logic of like dynamical systems. Or you could use
it to try to characterize, say, like the universal property even of the free energy principle. And that's
something I like to think about sometimes. Like, how can we think about active inference systems as like
trying to achieve their goals? Is that is that related to these adjunctions that, you know, come up in sort
of foundations of logic when you look at them categorically? And if it is, then that's quite
profound, because it tells you that, you know, maybe the FEP does have this kind of universality that
people want to claim it does. So I think, you know, it is true that right now, because it's quite early days,
category theory is kind of mostly used for bookkeeping. But I guess that might be because
there's quite a lot of bookkeeping to do before we can make the most of this kind of move,
make the most of using these kind of universal structures. And maybe one day further in the future,
where people are more familiar with this kind of language, and we have this big library of categorical
tools. And yeah, our computer program, a computer sort of modeling environments and programming
languages, know how to like import stuff from this category just really easily. And so you don't have
to do all this kind of tedious manual stuff, maybe like in the future, in that future, it'll be much more
common just to say, Okay, well, we're going to start to model things using these universal properties,
you know, off the bat, rather than trying to sort of retrofit them.
Okay, awesome. Thank you, Toby. Ali?
Ah, yes, thank you so much for your detailed answer. And again, I have a follow up question to that. So
there's this view in philosophy of science that views scientific theories as not as a kind of monolithic,
I mean, phenomena or model, but rather, any given scientific theory can be viewed as a population of
models. So some of those models are more fundamental than the others. And, or in terms of Manuel de Landa,
there are virtual and actual parts of each of any given scientific model. So the idea here is that
the actual parts of scientific models try to capture the context dependent behavior of phenomena or any
physical system. But on the other hand, the virtual or more fundamental part of scientific models or
theories try to somehow capture its more abstract and abstract model of the phenomena in terms of its
topological invariance. So do you think category theory can provide a rigorous language to somehow unify
this view of science? I mean, and to see how exactly those context dependent part of scientific theories fit,
or at least can be compatible with the context independent part of scientific theories or the virtual part?
Because, you see, in the context dependent or actual models, scientists usually try to refine their models to fit the data
as close as possible, or at least approximately close enough to be useful. But for the more fundamental parts, comprising
principles, axioms and so on, they only try to capture the topological terrain or the, I mean, the topological
invariance of the models and how models can be compared in terms of their singularities and topological shapes.
Yeah, that does sound very familiar. I don't know this kind of work or idea in any, you know, I haven't come across this before, but it does sound something that be quite amenable. And in fact, you know, there seems to be, at least in my mind, some alignment between this kind of sense of virtual that you're talking about, and this kind of universality that I was talking about.
So you could think of, you know, a category of models of particular kinds as being like inhabited by all of those things which satisfy these invariants, and then you have different, you know, individual instances of these things, which would be like the objects of the category, and then the differences between them are the, you know, the morphisms.
The thing about morphisms in the category is that often they are the things which preserve the structure. In other bits of mathematics, they're called homomorphisms, and that's where the word morphism comes from.
And so you could think of those as, you know, ways of comparing the models or translating the models from one to the other, but preserving those invariants, you know, and so that seems to me to capture some of the idea that you were sketching.
I guess one thing which may or may not be useful, depending on how you look at it, the category theory gives you is it's obviously kind of a lot more general.
And so it allows you to talk about invariants of kinds that, you know, more than just, excuse me, more than just topological.
In some sense, like functoriality is a kind of, in like, it kind of captures the kind of invariance as well as saying, okay, well, we preserve this structure.
Each, I mean, just one way of like looking at a topological space is to take its, it's what's called its nerve.
And so that, like, that takes a topological space and turns it into a category.
And you could sort of think of the morphisms in that category as like the sort of like the paths in that space or ways to sort of get from one sort of part of the space to another.
And then, you know, morphisms, functus between topological spaces considered in categories like that.
They really are just things that preserve those topological structures.
And so, so you like this, this language kind of seems to encompass the kinds of things you're saying.
Yeah, yeah, it would be nice.
Yeah, I would love somebody to make that connection.
Oh, I'll just follow up on this.
And then Dean, it's a, it's a related comment from Roman in the chat.
Roman wrote, quoted you in this fractal quote streaming,
thinking about the FEP through category theory and relation to goals maybe allows to prove that FEP has the universality that people claim it has.
And Roman asks, didn't Maxwell Ramsted and Dalton Soctiva Devel already kind of prove this in the Bayesian mechanics, physics of and by belief work?
So you're talking about the role of generalization.
What do we gain with the category theorification of FEP beyond, for example, the generalizations that we've seen in Bayesian mechanics and G theory over the last year?
Yeah, that's a great question.
I think Maxwell and Dalton are doing a great job formalizing the ideas of Bayesian mechanics.
But as far as I'm aware, the job isn't done yet.
And so I haven't yet seen, you know, I mean, I have a particular aesthetic, right?
And I would like, I would like to see a really clear recipe of a way to take, of like, on the one hand, some like, or like some machine that takes in, that has like a particular shape, that is like input shape.
And it takes in, like, a dynamical system of a particular kind.
And it gives me back, like, the specification of an inference problem for that dynamical system is solving.
I think that's what Bayesian mechanics is saying.
It's saying, okay, well, if we have a dynamical system that is somehow kind of, that you could sort of look at it and say it has a boundary, it's a Markov blanket, that you can write down its dynamics as if it were doing free energy minimization, that is solving some inference problem.
But there's a lot of, and I, so I think that statement is true for certain classes of dynamical systems, but it's not, I don't think the story has been made, like, like, the questions for me are like, what are the classes?
And what are their, what's the essence of those dynamical systems?
So if the result might depend on, like, specific technical criteria, which maybe you think, okay, well, like, that, that's kind of like a distraction from this kind of abstract principle, which we're trying to get at.
And so it would be nice to sort of know what the actual, like, essence is of the problem that allows us to do this translation.
And then, you know, there seems to me to be, like, questions of, I mean, other fairly technical questions, but questions about things like, well, what is this boundary thing?
Like, how long does it persist?
And what does it mean to separate a thing off and consider it as having a boundary?
Most of the treatments I've seen of this idea have not been done, have not been explained or expressed in a, in this compositional way.
And so they just assume you're given a system and a boundary, and then that's kind of it.
But, you know, boundaries come in all kinds of shapes.
Like, the boundaries of the cells in my body are kind of all, like, glued together in a particular way, and they form me, and I also have a boundary.
And so how do the kind of local inference problems that are being solved by those individual cells, given their gluing, amount to the kind of inference problem that my whole body is solving?
And I don't think an answer to that is, you know, is anywhere near given right now.
And yet, obviously, we're, you know, we look at systems out in the world, and they all seem to display this property of free energy minimization, or at least something that looks a lot like it.
And so it would be nice to be able to relate those, those kind of inference problems to one another.
So I think there's still a lot to be done.
Just because we've kind of made some first steps doesn't mean that we're all the way there.
Obviously, given my aesthetics, what I would love to see is this kind of abstract characterization of this universality.
And I think I, you know, I think there's a way of stating, or at least the structure of that universal property,
using this compositional active inference language, of which the thesis is a part.
But effectively, it seems to be something like this adjoint thing that I was talking about earlier.
So you, on the one hand, you have like a, something like a functor that takes statistical problems,
and gives you dynamical systems that kind of solve those inference problems.
And so that's a function from like, you know, statistical, you know, what I call statistical gains into dynamical systems of some kind.
But of course, you have lots of dynamical systems.
And so, you know, what this Bayesian mechanics idea seems to be saying is that you can go the other way as well.
And maybe this mapping in the other direction is also functorial.
And that would be a way of characterizing this kind of gluing together of dynamical systems, like I was talking about cells.
And ending up with maybe dynamical statistical games that also have this kind of gluing property.
But there's still a fair amount of work to be done, even to get like the basic framework to spell out that story precisely.
It's work that I'm trying to slowly get on with at the moment.
But I think, you know, the ingredients to doing this in the kind of generality that I would like this starting to become clear.
And so hopefully we get there.
But I don't think it's, I don't think it's sold yet.
Awesome.
Yes.
Just so cool to see all these paths weaving together.
Dean?
I think it's awesome, Toby, that you in this conversation have kind of anti-captured a jointness and common jointness.
Because I think that's a huge part of your work here and reading it.
So here's my question.
I think, and I would like you to maybe comment on this as though you were explaining it to a very curious 15-year-old.
So on the sort of most basic level, when I hear under sort of a common jointness principle, the word bookkeeping, I immediately wonder, okay, so what is the partner?
What's the thing that's being glued to?
And to use your metaphor.
And so I would glue it to taking receipts, essentially where you have a stabilization of a record under bookkeeping.
So I get that part.
And then the taking receipts is the stabilization of the change function, right?
So we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this kind of competition, we see this
of being a tool or does it get under this column directly adjacent as a as a rule like that's the
part where i think the adjointness could be really really helpful in terms of maybe helping people
see the applicability and not just the abstraction what's what's your thoughts on that so i mean i i
i yeah so i think um david spivak talks about category theory as being like a kind of accounting
system um or accounting systems plural for um mathematics and i i think he's kind of quite
right then so the the way i the way i see it is like um when you you know when you're keeping books
um particularly if you're sort of using like this double entry system you're trying to keep track of
the stuff that kind of flows into and out of your account uh your company or whatever it is
um without sort of missing some bits you see where everything goes and so that's how i think of this
kind of mathematical language you have this stuff um and it's kind of like some like abstract collection
of things some like maybe mathematical ideas and well a functor takes that stuff and does something
with it and turns it into some stuff of another kind um but it's like this kind of double entry idea
that you know when you take something out of here you have to put it in here and so you have to sort of
keep track of all the details at least all of the details that are relevant to those two to that float i
suppose and so when you have an injunction you have a way of going from one place to another and back again
without losing track of some stuff um it's like a little bit kind of like you're allowed to lose track
of some stuff but you you know the stuff you've lost track of because you don't care about it like
you know it like you know you might you might allow for some you know have some like buffer there but you
know how big your buffer is something like that so like a little bit like more precisely like in a
junction it's a way to map from one category to another and and back again in such a way that like
the the two mappings are kind of like like ideal approximations of the inverse of some of each other
and that you can sort of measure the difference between between them um they sort of like give you
it gives you like an isomorphism of between the two sets of morphisms of some kind and that that kind
of gives you this nice kind of structure preservation property this kind of bookkeeping property um
i don't i mean so i know that there there are people out there um who have used
um category theory to um model stock flow diagrams and so these are used in economics to measure you know
stock flows of stocks and things like that but they also use an epidemiology to model
you know the transmission of disease because that's also like um a flow of some stock you have people
moving around um and so i you know it would be nice to sort of bring this idea full circle and have
this mathematical language of bookkeeping actually applied to bookkeeping um but i don't i i haven't
i don't know how that would go just yet but but like you know if we think of if we think of economies and
corporations as as adaptive systems or if we somehow kind of translate from flows of money to like flows of information
that there does seem to be like an analogy between that kind of flow and the kind of flows that we think of
in active inference explicitly um and you know another thing yeah one of the things i like about category theory is it allows us to make these analogies in a precise way
and so maybe we can you know relate these two things quite clearly i mean i you know it's yet to be done but i would love to see it
awesome
dean smiles when his keywords are buzzed during a response
okay
we'll go to another great question in the chat from matt n
matt wrote can you provide some ideas about the next necessary steps or milestones for categorical theory
to be effectively utilized across research and in subsequent engineering applications
and i'll just kind of append to that what do you think at the individual team and organizational scale
what can we do what milestones exist to realize some of these engineering applications and implications that you brought up
right so i think the main thing
possibly unfortunately for you guys who spent a lot of time reading the details i wrote is to kind of have this community
developed to develop to a stage where the tools that i mentioned that allow us to kind of use
these category theoretic concepts fluently without having to know all of those like boring and complicated details
um to develop those to a stage where people are actually you know able to use them without being kind of like mathematicians or category theory domain experts
um so this is i think starting to happen i guess you know as a result of the kind of needs of the pandemic
people have developed these tools for epidemiology i mentioned this stock flows stuff
and i think you know you can probably there's like some i can't remember what it's called unfortunately now
um so in the julia programming language there's this great framework for use for kind of building
systems using category theory concepts um but of course this doesn't satisfy the property of not having to
be a category theory domain expert yet on top of that people have built using compositional ideas about dynamics
frameworks for you know building compositional dynamical systems and like compositional models for things like
epidemiology and and stuff like that and you know hopefully you will get there also with um you know
statistical modeling and active inference and all that stuff but what you know once once you've got that
kind of lower level library people can start to build like user interfaces on top of it and and that's
the thing that's starting to happen now with the stock flow stuff um and i think that people involved in that project
uh i mean they know that there's like one kind of like major like proprietary tool for doing this kind
of modeling which is used for you know it's used by lots of different organizations for instance it was
used by governments for modeling during the pandemic but it's not like it's not very collaborative it's it's not
compositional so if you like have this huge model it's very hard to like deal with like to modulate just some
small part of it um and so these people are like i say it's very impossible i can't remember all their
names um or the name of the software but they're building this tool which um allows you to build up
these models just using this interface but it's built out of this compositional stuff um and so it has a lot
of the nice properties that come out of it and of course you if you if you want you can sort of delve
under the hood and understand like actually how it works and connect it to all this other you know stuff
and maybe down the line when we've got really advanced tools that that will kind of be able to
be done for free and some nice user interface but i think you know so if if people want to make the most
of this you know they can sort of get involved with that kind of effort or at least they could sort of
get familiar with the kind of basic ideas of you know categorical modeling or compositional thinking as
i like to say these days um but i don't i also don't want to like prescribe to people and they
have to know what like a monad is and all that stuff because you know there are it is technical it has to
be technical because it's about technical stuff but i mean it's also trying to be ergonomic and
yeah if if that's your thing you can try to help make it more so
awesome dean
no i i i i i i'm waiting because there's a there's a part of the paper that the belief updating and the
fuzzy of distributions and stuff i'm gonna want to talk about that later but i'm i'm done for now
all right i'll go to a question submitted by jr also who created the syllabus so thanks again jr for
that amazing work so jr wrote um in compositional active inference from may 17 2021 toby said i'm with
valeria on this i think we need to seek ai alignment for the artificial intelligences that we already have
things like corporations and social systems and we should be concentrating on those right now could you
speak more about how you envision this kind of application this is especially interesting in
light of what we spoke about in the 54.0 regarding sensor fusion and consensus what might this mean for
corporations and social systems toby do you mean that uh this between humans and things kind of like
artificial intelligences or machines and artificial intelligences in the context of companies and
societies yeah that's a great question and i think you know jr's done a great job with the syllabus which
i also had a look at um yeah yeah i think uh it's a good it's a good it's a good like list of um material and
concepts to sort of get get to grips with um but as the yeah ai alignment it's a very vexed issue of course
um i know i mean i put this to people who are involved in the um ai safety community and some of them
say oh well we concentrate on machine intelligence rather than corporations because there's like no hope
for making corporations safe like it's too late they're already out there so we can't fix that which
is obviously a very sort of defeatist attitude but maybe it's right um to concentrate on a matter where
they think they can actually have an influence um but i do nonetheless still think that corporations
are like super intelligences we they've been made out of code but the code isn't a traditional computer
programming language it's the legal programming language that makes up their contracts but those
contracts sort of determine how they operate and are executed on a thing which is a bit like a
computer like the legal system um you know you go in a court it processes the contract and it
explains what the outcome is going to be it's a it's like a computer but it's it's like made up of people
um and you know they have you know goals and desires and they take actions and they receive
information from the world and so yeah they're they're a lot like um well yeah ai systems but it's
nice because we can pun on ai and have it mean both artificial intelligence and active inference um
so yeah so that's like a long preamble um one of the things that at least as far as i know
right now the active inference literature doesn't talk an awful lot about at least not very precisely
is this notion of sense of fusion so you can have like two so you have like two yeah so if you think
about the brain again you've got like two like neural little neural circuits next to each other and
they're making predictions about two visual receptive fields um but those visual receptive fields they kind of
often overlap and so what we might want a system like the brain to do is to be able to kind of glue the two
inferences that those circuits make together over this overlap so that you get like this you know unitary
perception like we don't just see a bunch of independent patches of the world we see like
this kind of glued together thing even though you know it's the way it's been inferred is through lots
of like individual systems next to one another and so it's it's quite you know and you know it's quite
clear how to put two things next to each other mathematically you just take their sort of product
um that you just then you just do them side by side but when you need to when you want them to sort of
glue together in this way um you might encounter some problems like you might have one make one
inference and one make another inference and so you get like a disagreement and then you need to start
to say okay well what's what's going on there like what is the nature of this disagreement is it something
that can be resolved by like say you know passing some messages between the two systems or do we need to
just like ignore some of the data or is there fundamentally some like paradox which means that
we can't resolve this disagreement excuse me um and so in mathematics there's a lot of theory that's been
done about precisely this question in topology in an abstract way um related to the field of what's
called co-homology which is all about like measuring like obstructions to doing this kind of gluing
thing and sort of in this world of like applied topology people talk about um algorithms for resolving
disagreements and and things like that and they often have the flavor of like diffusion you can sort of
think of diffusion as like smoothing out disagreements like because you're just sort of like letting stuff
propagate um something there maybe could be said about like how these diffusion models work in
generative ai but i haven't really thought about that um and so you know maybe maybe there's something
to be done for you know political systems or corporations like maybe we can look at how
you know the mathematics says we can resolve these disagreements and implement better processes in our
organizations that are inspired by those algorithms or the kind of universal properties
and you know maybe that'll make the world a kind of more harmonious place or maybe it will just help us
build um you know systems in the future which resolve disagreements better and this is one of the reasons
why i was um talking about you know multi-agent systems before um i know this is a thing that sometimes
people think about in the context of you know blockchain systems and things like that which are actually
actively composed of lots of different participants um but i don't know yet how it you know might
all pan out i mean ultimately the question of alignment is really about do the goals of this other system
disagree with my goals and you know if the other system has more power than you then ultimately
there's probably not much you can do about it regardless of whether there's
whether there exists some algorithm that might help you smooth it out um so i i think
i i hope at least that by looking at how like the mathematics says we can optimally resolve disagreements
or smooth them out or patch things together or build kind of multi-agent systems that will help us
build things in the future in such a way that we don't get to a situation where the systems we're
working with are actually aligned against us say um but obviously we can't really guarantee it we
actually have to sort of do some work but it's nice that at least um the framework of active inference
allows us to talk about that at least right so you know we can say like oh i have these beliefs about the
world and this other agent has these beliefs about the world and then you know we can express these
beliefs in a mathematical framework which is amenable to using these tools from cohomology
and applied topology to be able to start to make use of that work that's already been done
um it's to me not so clear how you would do that if you're not working in this active inference world
and you're working say with just reinforcement learning um i i know there are similar questions
about how to kind of glue together preference functions in economics um and i think
for me the simplest way to kind of understand those questions is to kind of turn those preference
functions into distributions over states and then use this kind of um sort of more active inferency
language to think about it um so yeah again we don't you know we're just at the start of this process
but like it sounds like we should be able to you know make use of this wealth of tooling which has been
developed in other fields um because we're putting this into this kind of modular categorical language
we should be able to kind of you know put put these two modules together and make make the most of them
thanks i'm going to go to a different sort of question here i'm going to uh play dissertation roulette
but i kind of know where i'm going to go and uh i'm going to skip to a diagram it's a diagram at the
end of chapter six and it looks like this so what do we see here what happens in this graphical arrangement
it doesn't have to be ultra specific about defining every variable but does right what is what matters
here that's apology or the geometry is it an arbitrary visual layout but you're conveying something about
the connectivity or is it read from left to right or is there a certain way to understand or just
approach these diagrams which in slightly smaller forms or larger forms we see peppered throughout
category theory and your dissertation so okay yeah so here what i'm trying to do is say that
if you have a like hierarchical predictive coding system if you if you take like the formative two
parts that are sort of plugged into one another and this is the the g and the h
you like do predictive coding on g and you sort of plug that into h
and then you do predictive coding on h with that input it's the same thing as doing predictive coding
directly on the two parts as if they were one thing at the start so what i mean is
if you have so like here we've got like a hierarchical system again the the parts of the hierarchy of g and h
and we could do two things we could either apply predictive coding to the two parts and then glue those predictive
coding systems together or we could glue like the g and h together and then apply predictive coding
to gh the glued system and what this bit of this result is saying is if you do those two processes you get the same
dynamical system and that's that's saying that this predictive coding thing um at least with this sort of laplacian
scheme is functorial so in this diagram um it is read from left to right i mean in some sense you know you can
orient these diagrams however you want so you're clear about how you how the information flows um and if i
remember rightly what we're what we've got is we've got some like um um a yes we've got x and y so i think um
so we've got one system which is predicting x and one system which is predicting y and i'm
i'm not totally sure what p and q are but i guess they relate to x and y um and you've got some stuff
that's coming into the predictive coding system h of g and some other stuff which is coming in and going to
h of h and these give you like updated states so in predictive coding with this laplace algorithm what
happens is that you you know you get this new observation that comes in and you look at the error
on you know your you know between that observation and your prediction and you update your prediction
according to the sort of direction that error points you in and so that's what these hg and hh systems
are doing but because it's a hierarchical system this like second layer
which yeah yeah the second layer requires you to take in the prediction of the first layer
so if you sort of follow in the flow of information
h h takes in inputs from gamma gamma is the kind of um the predictive channel the predictive part
of g and so that feeds into h
and the update of g which is a sort of layer above h requires the the new this newly updated belief
from h right so that's going sort of up in the causal hierarchy
h of g
and so if you sort of follow the flow in as well into this g update function at the top h of g
you see that it gets an input from this sigma function
and that's the that's the new belief emitted by the h system in in this part of the proof at least that
was the notation i used and so this is a saying if you do predictive coding on these two bits it
it has this structure which is you know you do the forwards pass down through the system g and then h
and that gives you a prediction at the kind of lowest level and then you you know take your observation
which is i think the thing you get in here in z yeah that's what z is it goes into h you get an updated belief
that comes out in the form of the sigma
and then gets passed to the first level of the hierarchy
which is used to give you the highest level of belief
great well it's awesome because in so many papers we see what i guess people expect and prefer which
is you should be able to make a nested model here and have communicating agents here and do sophisticated
affective inference in this way and it's like we're already playing with the legos in a sense and
talking about it like it's a total play shop so to understand in a way that is worthy of dissertation
research some of that substrate it's basic lego research and how do you know when you're working you
describe this as a result how do we know i mean can i just draw a line from here to here or can i just
uh make a d and just have d you know connect to gamma what rules do you keep a guidebook or recipe on the
table what rules help us know what edges and shapes you can even draw and when you describe the manual
checking yeah are you looking for what right so yeah this is this is a good question um so yeah this
is like it is like a language so it has a syntax um and that syntax is like i mean it's like the
grammar right and it tells you what things make sense to say um
and so you only say those things don't we all don't we all no but that but it's it's it's that's
what i am laughing because often you want to like play with the grammar right and so sometimes you're
like oh well you know i'm it feels like i'm not allowed to like draw this thing like i'm not allowed
to connect this box to this other box in this way but like i really want to do that and it's actually
that's not a bad thing you shouldn't do it in that diagram where it doesn't make sense but you should
take that feeling and reflect on it and say oh but that's saying that maybe this language this diagram
syntax is missing something important and then you should like trust your intuitions there and say okay
well like actually what do i need to do to this diagram language to make it like allow me to do that
move that move that i wanted to to do to draw that thing i wanted to draw and so that that you know
suggests that there's like you know you're you're walking down you're walking through like a valley
and you can see there's a hill over here and there's something peeking out over it and you're like actually
there's something over there i need to be able to see and so you have to like move over towards a
different place to be able to get to that to that place um and so you should do that right then that's
fine but the reason why i said at the beginning don't just draw it in your diagram is because then
that means your diagram doesn't mean anything and that's that's worse so this is part of the reason
that it's actually requires using this kind of mathematical formalism really using mathematics
generally requires this discipline um because you don't you don't want to say things that don't make
sense it's kind of a if you have a intuition you should do it justice and and and like treat it
seriously and you know you probably get more out of it by figuring out what's missing so like you know
with this particular kind of string diagram language you can't just get used to reading them right so i
you know that these little black dots mean copy some information so you if you see the first one
or like all like the second one on why you know you go from why you go into this copier and you just
send the information to both of those outputs if you read like um bob cooker's work or say his book on um
um his book picturing quantum processes which is all about uh quantum theory using this string diagram
language um there's a lot of like there are lots of lots of different rules for like stuff you can do
with these languages languages like you have colored like spiders he calls them which are like colored versions
of these black dots and you know you there are things you're allowed to do like if you have two
spiders next to each other that are the same color you can sort of merge them to be a spider with like
as many legs as the two of them and if they don't have the same color then you can sort of split them apart
and like that's that those kinds of those kinds of moves are like you know part of the syntax
of this language but it's a it's a human language and so people developed it and they realized that
they could do some things and they realized that they couldn't do others and they tried to make the
rules of the game you know match the things they wanted to do and you know they ended up with this
language which is now used a lot in um quantum computing because it's a very sort of like natural
language for that problem um so as to like how do you know what kinds of things to draw well here like
i was trying to prove functoriality which is the sort of general property and it says the thing you know
it says in an abstract way the thing that i started by saying which is like there i was i wanted like h
of gh to be the same as h yeah see here if you see this line the update map of the composite system
you see i've got um h after hg well i want that to be the same as h just applied to h after g and so
that says okay well i want these two things to be equal and so what i do is i like draw the two diagrams
for the two parts and they okay you draw them out and they first of all they don't look equally
like oh that's annoying but then you stare at it for a bit and you reflect on the kind of moves that
you're allowed to make you think well okay maybe i can um maybe i can apply this move and it makes the
diagrams look a bit more similar and eventually you make the diagrams look the same you've only used rules
that you're allowed to use um okay i can see sort of skimming through to see if it looks like that
uh directly in the thesis but like effectively that's what's going on um it's just the rules are a little
bit abstract though that being said i know that um pavel soboczynski who's a researcher in category theory
at talon he's got a project um with a colleague of his to build a a mobile game which is all about
making string diagrams equal in this way um and so the idea is that in this game you have like
pictures like this and you've got certain moves you can do to manipulate the pictures
and that you know and the sort of aim of the game is to like transform one the sort of starting picture
into like the sort of goal picture just by applying these moves and as you go through the game the kind
of moves you can do become more complicated um but it's i mean it's the same kind of process i'm not sure
the game is at the stage now where you're allowed to like do this like human creative thing and say
actually i want to like make that be a new kind of move or change the diagrams or like add in a color
here or something like that's a really human thing and you know there's nothing to say you shouldn't do
that but i'm just trying to advocate for do that in a way which is also rigorous
that's awesome awesome awesome yes to speak fluently the syntax and the grammar whether
we're talking about natural human language or we're talking about the active inference ontology
we want the syntax to be unobtrusive if not compressent so that we can actually convey the
semantics because that's the real information flow the syntax is within the shannon signal entropy space
and then in live stream 17 and 4d and the physics as information processing with chris fields where
we've been exploring these semantic bayesian information flows that must out of necessity to
be enriched beyond the syntax have to include an individual or or shared context that flow necessitates
the proper syntax and so it's just um part of the learning and so it's exciting to see that there's
games and work like yours and others to help because um if we could play with those legos
and get the instantaneous feedback just like learning with a language tutor of like no these two pieces
they don't fit together and then it just it we kind of um would actively infer
patterns make our own rules and understandings but there would be certain compositionality of the
system itself and so it's interesting to think of like you described it as a natural language it is
technical and naturally arising and our natural language without going too much into the superior wharf
and everything like that it reflects the kind of subject object verb structure that we often want to convey
this is a natural language for science it conveys what we want to convey and so being able to do that
in a way that is both disciplined and rigorous also enabling low cognitive overhead fluency for some
individuals today but for more tomorrow that's just extremely powerful and the fact that it has
like such a beautiful and intuitive way to graphically represent it is um very promising because that may
tap us into a more holistic understanding and a visual field uh or a felt sense understanding that just
looking at this and someone says wait this is what we learn in active inference it's like well no that's not
not even the tip of the iceberg there's so much more to it and it's not only this and all of that but it's
one of the pieces that at this moment in time in our sort of early calculator phase or abacus phase almost
it's one of those things that that we're tackling but it's the wave that we're riding and i just can't wait
until there's more accessibility and the learning pathways to to end up the playgrounds to use all this
yeah i mean i i totally agree with with all of that and i i think um it was it was nice to see the jr in
this syllabus that included um references to eugenia cheng's work because she's done a lot of great work to
kind of make mathematics more accessible in this way um she had an article in the guardian like in the
last week or so even talking about mathematics education and how um it's often it often like
scares people because they're taught to like you just apply algorithms in this kind of blind way to do
like multiplication or calculus or whatever and and not really like play with the concepts in the way
that i was trying to say okay well you know you're drawing these diagrams and you know you want to like
play with them and it's it would be nice to see mathematics education take this kind of more playful
route to start with one of the things that um eugenia says in this article is that unfortunately that
would make things kind of slower because like you just want people to muck around you don't want
people just to you know be able to churn out this kind of computation but you know in this future where
our computational tools are so powerful maybe we don't all need to be perfect integrators or like you
know derivators and be able to like multiply numbers quickly and you know some people like doing long
division but i i don't even remember how to do long division why would i it's it's it's silly to kind
of drill that into children so there have been projects um to teach like kindergarten children um like
like a couple of projects not many some of the kind of rules of this string diagrammatic stuff
um in in this quantum um information processing world this um of book bob cocker and his colleagues
i think there was one um project by dan geeker in birmingham and maybe one by bob himself or at least
he was trying to get it off the ground i don't remember um but at least where it has been tried i think
they found that children very easily learn to use these these these kinds of languages um because
it's just playing with pictures they're kind of much more approachable than this kind of scary symbolic
language which is you know i don't i mean it it's a kind of fine language if you're used to like
typing on a typewriter or like writing by hand where you write in this linear way but you know if you go
to like a mathematics department and look at the you know the whiteboards or the chalkboards there
you know most of the time you see lots of pictures diagrams and things and that's how people reason
typically um and so a lot of what's been happening with applied category theory is trying to like
take using diagrams seriously as mathematics um and trying to like say okay well here's what we can do if
we do if we do take it seriously we can sort of recap sort of recapitulate some of these things which
people have found like abstract or abstruse or difficult in mathematics before and like make
them seem a bit more easy to reason with now and so i mean that applies to like abstract things like
stuff i've mentioned already like adjunctions like the laws of adjunctions you can draw them with
string diagrams i mean you know i haven't shown it in my thesis but like you can
if you sort of google around you can see you know adjunctions in a two category and they end up being
some kind of snaky picture and sort of you get a sense of like what's going on there from these pictures
like the flow of information in some sense um and there's a similar thing with like with like monads
the the joke for like functional programmers about monads is like oh like you don't know what a monad is
well it's just a monoid in the category of endofunctors and i i mean that's true it's not just a joke it's
true but the thing is if you draw what a monoid is it's like a thing which like like one of these like
you see on that picture you've got this gauss thing and then it's got a black dot and you've got
you got one wire and then it has a black dot and then two wires come out of it and i said this is like
copying well like a monoid is like that in the other direction like you've got two things that
go into a dot and that come out with one thing so like when people say monoid they mean something like
they often mean something like addition you've got two numbers that come together and they produce one
number we've got like multiplication you've got two numbers again they come together and produce one
number so like it's like the opposite of copying in some abstract sense which takes one thing and gives you
two things this is something that takes two things and gives you one thing and so you can just like
draw the the diagrams that define a monoid and say okay well what does this mean for like endofunctors
and you can sort of start to reason about it a bit more approachably i mean it's still quite abstract
because it is quite abstract but it makes it kind of less scary to use this kind of language i think
awesome yeah there's so much psychology and sociology and mathematics and just hearing about yeah on real
chalkboards people branch and they flow and they circle things and they put an x through something it's
like there's all these operations that can't be copied with a typewriter and as our uh cyber physical
and social niches develop and we have different affordances different metaphors different quantum
reference frames for working and being it starts to make more sense for uh having a natural language that
can express that um even if in some yeah no no go on i've said loads of stuff
it just makes me think of a turing tape where even if there is a linear representation
it can still in some other way characterize like a lisp program with nesting or hierarchical model even
though yes there's like a linearity but also there's a model so it's not that we can't represent
certain things with the bit streams or anything like that it's just that that may be more like the
assembly language and that when we actually want to do certain kinds of work we may want to just move
lightly and semantically with a high level way to think about math
yeah totally it's kind of it's notable to me that um like recently i mean i i've been giving you know
talks for a while you know using a computer whether or not like over zoom but like it could be in person
like you know have my like powerpoint slides or whatever but these days if i give a talk i just use my
like tap like digital tablet and i do everything like all the slides by hand i draw pictures and
it's nice now that we've got like technology that is starting to you know be a bit more human in that
sense and i think this is like a kind of mathematical technology which is like that although i think it's
also notable that um it's still in substance quite niche and i think i mean i don't i don't know but the
impression i've got from talking to people is that it's still the case that some mathematicians sort
of think of this kind of like mathematics of diagrams are somehow like not quite like real
mathematics because it's like it's too much like play in some sense um but i think that i think that
perspective is changing and people are taking it seriously i mean it is real work and there's a lot
of hard problems um and you know stuff actually gets done but i think it's it doesn't to me it doesn't
really matter what like a handful of mathematicians think it's just what's useful to people that
matters um and so i mean i i hope that you know these tools continue to develop and like you know we
can use them in all sorts of different domains um i don't know you know i've never really
it's it's no it's like notable to me as well that like human vision is kind of like two and a bit
dimensional really it's not really like three-dimensional but you've got a bit of three
dimensionality and i've never really played much with like three-dimensional diagrams but maybe i
will one day have some tools with my like you know vision pro or less not pro thing or whatever it'll
allow me to to do things even more like naturally like actually like plug together some stuff in some
abstract space um who knows who knows yeah the diagram being two-dimensional or or planar gives
us this kind of classical screen holographic screen that information can be written on that then quantum
cognitive agents can unfold into the imaginary plane with the wick rotation but also the boundary just like
you said earlier can come in many shapes many dimensionality so we could have a four-dimensional
boundary artifact that still becomes rotated into a higher dimension and uh that's not the framing or the
mathematics that most of us have learned up to this point there's a really crystallized would be a
complementary way to say it but um codified or fossilized sedimentary understanding of math education
its role in broader thinking and what we learn along the way and the progressions get reified with who
makes it through the pipeline so i think that's like that's like the the unknown unknowns here the known
unknowns like we all know that we struggle to understand this but then what but but then that's the real
jumping off when it when it's not just us adapting into a new regime um of learning and doing but when
the new regime is the new regime and the new regime is the new regime that we're trying to do this
in our last um sections here um dean or ali another question or um what what are you looking to
bridge or gap into the dot to
uh dean okay okay uh well yeah i actually um i've written down a number of questions but uh they may be
quite specific and i think uh uh they're perhaps uh best um suited for the dot two discussion uh but i
wanted to thank uh toby for uh i mean i literally had goosebumps the entire time so uh it was really
fascinating and um quite enjoyable and i uh learned a lot and i hope to uh i i also have some additional
questions in my mind i hope to uh get to get to some of them uh in the second discussion uh so uh yes
thank you again it was really really great thanks dean with the penultimate thoughts what are you um
what do you see us heading into yeah well what if it's if it's okay i'd like just to read a really brief
piece of the paper because i don't want to launch this on toby in the dot two without giving him a
chance to think about this a bit under seven four you've got fundamental theory and you say future
work connected to this thesis need not only be in applications a number of purely theoretical questions
raise themselves too and i love seven four one this this one paragraph it's not it's it's for me i call
it a really have to slow down and enjoy the moment you're today toby i don't know if you're a
distance runner an endurance athlete of some kind but your stamina has been phenomenal but this one
paragraph to me would be like a refreshment station where they offer you a milkshake and a piece of
battered fish like it's yummy but you but you yeah you need to wait you have to pause and kind of go i
don't know if i want to do that but it really ties in nicely with the syntax stuff that danny was talking
about and i have a question at the end of it so i just want to read it though the mathematics of belief
belief so you basically said belief is theoretical that's fantastic is a large part about replacing
definite points with fuzzier distributions over them independent type theory we've replaced points
with terms non-dependent terms are exactly points so a type of theory with belief should somehow
encompass fuzzy terms just as we can replace points with distributions we can replace dependent points with
the dependent distributions however the standard replacement moving from a category of functions
to a category of stochastic channels obscures some of the universal categorical structure and underpins the
rules of type theory this standard replacement also misses something else while it does allow for
fuzzy terms it omits a model of fuzzy types we might well want to express beliefs about things whose identity we
are not quite sure and then you say in the next sentence there seems to be a couple of related
resolutions to this puzzle my question for you is this and it's not for today it's maybe for next time um
it seems to me we have to grapple with this idea of making fuzzy clear and making fuzzy precise and you
started speaking to that and my my wonder coming now with a strong a much stronger active inference set of
priors is there has to be something more to this than just a gradient descent and i think you started to
speak to that in this section and so um i'm kind of curious do you think that this is a feature
the fact that we can do this we can do fuzzy clear and fuzzy precise and not necessarily see that as a contradiction
but actually the way category theory kind of gives us permission to examine that so again it doesn't have to be
answered today and maybe i'm maybe i'm misinterpreting what you were trying to say there so i'm i'm open to being
redirected but i just think that this opens up a world of possibilities and when i first read it um
i i i don't know what ali's goosebumps looked like but i was just i was just like oh man i really want
to ask you about this so yeah i mean yeah i yeah so the thing about fuzzy type yeah so i do i gotta start
by saying i agree that the kind of that what some of this is seeking is something like thinking clearly
about thinking fuzzily in some way it's kind of weird right um it's like having some certainty about
uncertainty um but it's definitely the case that still now like i think a notion of like fuzzy type theory
is not well developed though i am aware of people various people having thoughts about this and
people thinking about it at the moment um and of course i've got my own ideas about it um but it
seems natural right like we often you know think we know what to think like we can recognize a thing
but like um maybe you're not quite sure and so like you know you're not sure if it's this or that or
you see somebody coming down the street towards you and you kind of recognize them as somebody you
know or you used to know and then like as they approach that their identity becomes a bit clearer
but you're not you know you weren't sure for a while um and i think you know there's nothing to say that
you know we shouldn't be able to you know in some sense like types are a kind of element of some
bigger space and so we should be able to apply all this maths to it and it's kind of really about
figuring out what the rules are that makes the kind of language of type theory kind of align nicely with
the language of probability um and it's a research effort but i'm happy to talk about it like more
next time i'm also like happy to talk in any detail about any of the actual like specifics
of the stuff in the material in the thesis or whatever else in category theory you might be
interested in like i'll promise to be expert and everything of course but i mean i'm happy to try my
best particularly if ali it sounded like your questions were maybe over like a more technical
nature maybe not if i i don't know if i got the right sense of what you're saying but if they are i'm
happy to like talk about the details of that thank you and also like to to like review any of the stuff
like to to try to like say because you're right that there's a lot of like detail in the thesis
um because you know you make a flame and you're supposed to substantiate it and that means you have
to give a proof and sometimes the proof is quite like complicated um but like structurally i'm i'm i want
this to be simple or at least to have like a simple like framework and so i would like to be able to
like clarify some of that if that's um if that's you know if there's time for that or if it comes to it
yeah that sounds amazing in dot two we will uh return perhaps any questions that people submit as a
comment on the video or as a message in the category theory channel on our discord we'll curate those
questions we'll re-watch and digest and then we can begin with ali asking some um taking us on a little
bit of a technical journey and toby thanks again for the incredible work it's uh defined our 2023
in many ways so it's been a joy and we look forward to next yeah thanks for plowing through um i think
yeah there's also the stuff i i think we talked about before that that we haven't really touched on
this time and obviously i didn't really touch on much in the pieces about like how do you actually
fit in like action into this framework and like how do you like start to talk about this like multi-agent
stuff we can you know if there's time we can talk about all of that two of the pieces just to share
that that gave us some of the most laughs were um first we didn't get action and and we're like
it's i mean just the the the it wasn't an anti-climax it was a climax of its own and uh and then also we
had had so many discussions over the months of time and the treatment of time backwards and forwards
ringing the bell unringing the bell um all of these different concepts and then in your limitations
you said we we really have to work on getting a dynamical treatment oh yeah but i actually think
that depending on like what you care about it may not be too hard so that's fine but even that you
would say it that way just having dealt with time oh yeah yeah and then to be like well i mean it's like
i thought that's what dynamical modeling was involving time no no no so that that you're right
you're totally right that so all i meant at that point was so the the the kind of like statistical
framework that i've been working with until then it just seems you have like a prior and like a way of
make generating predictions but like the predict there's no like nothing to say that the prior
data has any like data about how stuff actually evolves in time or the predictions have any data
about how like the sense data evolves in time it's just like i believe that there's this on the screen
and that makes there be this like stuff coming to my eye and that's it this is like a snapshot
and so like when you want to include time evolution in those beliefs it things become a bit more complicated
awesome well thank you again toby we'll see you um in a week and a day
it's been a pleasure thank you for having me bye thank you so much bye
thank you
















Thank you.
