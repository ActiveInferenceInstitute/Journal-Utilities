---
title: "ActInf Livestream #019.1 ~ Deeply Felt Affect: The Emergence of Valence in Deep Active Inference"
category: "Livestream"
series: "Livestream_019"
episode: "1"
speakers:
  - "Deeply Felt Affect: The Emergence of Valence in Deep Active Inference"
duration: "1:58:45"
url: "https://www.youtube.com/watch?v=SMQvRspIzpQ"
views: 268
exported_at: "2026-02-18T22:37:37.805400+00:00"
format: markdown
---

# ActInf Livestream #019.1 ~ Deeply Felt Affect: The Emergence of Valence in Deep Active Inference

[Music]
hello everyone
welcome to the active inference lab and
to the active inference live stream
this is active inference live stream
19.1
on april 6 2021
welcome to the active inference lab we
are a participatory
online lab that is communicating
learning and practicing
applied active inference you can find us
at our links and contact information
here
this is recorded in an archived live
stream so please provide us
feedback so that we can improve our work
all backgrounds and perspectives are
welcome here and we'll be following
hopefully video etiquette for
live streams such as muting when there's
noise in our background
and raising our hands so we can hear
from everyone who wants to speak
you can go to this shortened link to see
the upcoming streams of different kinds
today we're in 19.1 on april 6th
and we'll be having a follow-up group
discussion next week
on april 13th hello steven we're already
live
so today in active inference 19.1
the goal is really just to learn and
discuss about this really awesome paper
deeply felt affect the emergence of
valence in deep
active inference by casper hesp ryan
smith
thomas parr mika allen carl fristen and
maxwell ramstead
and we're really appreciative that
casper has joined us today and
any one of these other authors are free
to join us next week or the following
in 19.1 we're gonna go over
the various parts of the paper in any
order that people want to
raise them and we can just start with
some short introductions and warm-ups
that will be culminating in casper
and giving a little maybe just
introduction or a background
and um that will be great to start with
so
i'm daniel i'm a postdoc in california
and i will pass it to sarah
i'm sarah i'm a person stuck in berlin
because i can't update my visa
uh next
hello i'm stephen i'm in toronto and uh
i'm very much in looking forward to
learning more about
effect and it's a relationship to active
inference and i'm going to pass it to
day okay dave douglas
i'm in the mountains of the philippines
retired from
information technology including natural
language
processing and machine translation
background in process philosophy
whitehead especially and cybernetics
and i will pass to dean if he hasn't
spoken yet
i'm dean i'm from calgary um
retired but really interested in this
stuff i don't know who i can pass it to
other than maybe casper i'm not sure
sure yeah my name is uh casper i'm
a phd student at the
university of amsterdam i'm currently
doing
yeah um kind of being co-supervised by
two professors at the university of
amsterdam and um
one being at the university of uh
college london so that's uh
the one you probably all know called
kristen um
it's like my um
external uh supervisor
and this paper was developed
under his um yeah in his lab
basically with a bunch of really
wonderful people actually
my co-first author is not here today but
i am aware that he has been brian smith
has been with you on many of these
sessions
and yeah so i
think i'll just go into the intro
of the paper and
i guess it would be interesting because
you can read in the paper itself
in a kind of formal motivation
i will tell you a little bit more about
the story behind how this
how this came about when i first entered
the group
there was most of the modeling that was
done
was with single layers
and there was already some preliminary
work on deep temporal
modeling and
that's essentially working out the
implications of
this kind of hierarchical models that
start to look more like um the one that
might have come across some deep
learning research
but now with the bayesian beijing flavor
and one of the things that i was missing
personally
was a meta cognitive
aspect that
[Music]
moves beyond just estimating
uh confidence it's one one aspect
but then reflecting on that confidence
estimate
[Music]
to give you an idea of something that
can
regulate other parts of the system
so we ended up
going back and forth on this topic with
uh with carl and
thomas farr and was a huge help there as
well
and he's also on the paper essentially
thinking about these action models in
active implants
and i'm not presupposing certain degree
of familiarity but i can
suppose i can quickly read that
essentially the way i've presented it in
paper
is really meant to be something that
you start from zero knowledge
about active influence and i kind of
build it up in steps
so that people are not super familiar
with it yeah i guess it's like
yeah these these steps essentially
the the point is that these diagrams
have a very mathematical meaning um a
very specific mathematical
and when you just present people the
whole diagram
at once what we call directed acyclical
graphs
it usually is pretty overwhelming
so for this paper i decided to kind of
go back
and just give the viewer the reader
a very stepwise kind of
incremental primer we call it
and we start with um these first two
states
that are being linked is the the types
of states is hidden
states and sensory states
and that's really the kind of core and
what's interesting is that it's very
modular so if you go to the next
slide
yeah so
don't if you just ignore the maps for
now but the nice idea here
is that these graphs are entirely
or it's kind of like a lego box
essentially so once you understand
the first um piece of the puzzle
in m1 where it's inferring
hidden states based on sensory states
you can basically understand all the
other graphs as well
to a certain degree i mean at some point
we introduce
um links between continuous and discrete
state spaces that's where it gets a
little bit more
complicated mathematically the one thing
you can keep in mind when reading these
figures
is that down stream on the arrows
is always about prediction
so here for example the prior overhidden
states
on the top d predicts um
the hidden state below that s
so downstream on the arrows we're
talking about prediction
upstream we're talking about inference
so in this case you have
you start from the prior make prediction
about what the hidden states are a
priori
and then moving from these hidden states
make prediction about
what the sensory states are
and that's where the likelihood nothing
comes in and then so that's one crucial
aspect so downstream prediction upstream
inference
then there's another crucial part that
you need to know in order to interpret
these figures is that
um the circles are variables
and the squares are parameters so
in this case hidden states and sensory
states those are listed in the circles
the s and the o those can vary over the
course of the simulation
and if you set it up in this very
simplistic way then the squares are
fixed so the values in the prior and the
likelihood method
are fixed in this very simplistic
section
once you understand this you can start
hooking
these things up to each other so we can
once we link
another circle to a square then this
uh the mappings become
variable as well and you will see that
coming back later
but it would now generalize this
reading of the figure to the second and
so m2 here exactly the same
maps is applied to this way the states
evolve over time and so generative model
anticipation
is using current states to make
predictions about future states
that's where we come to the third part
of these kinds of
graphs that's pretty important to know
is that to right it's supposed to be the
temporal dimension
so s1 is used to make predictions about
s2
and base if you have knowledge about s2
you can make inferences about what s1
was the most likely state
in the past as well so it works both
ways
so that's perception and anticipation
and obviously
entirely reduced to the most sim
yes simplistic
kind of form that you couldn't come up
with essentially
something often these models are
criticized for being too simplistic well
i think that's kind of the beauty in the
sense that
we obviously start with these
components the lego blocks so to speak
the
individual blocks are pretty simple but
once you start hooking them up to each
other
you get emergent dynamics
that are pretty uh hard to already
create yeah pretty
quickly become hard to
wrap your mind around so that's why
we're presenting them in a stepwise
question
i would say if you're really interested
in the maps then
um you would
probably want to go into one somewhat
the tutorials for example that
ryan smith recently made i can actually
send
a link to that
right now
because he works through the actual
equations
in this step-by-step session
cool you can put any links in the
youtube live chat so that everybody can
see it otherwise only we'll be able to
see it
yeah cool thanks for all these
clarifying points on
figure one and i agree it'd be awesome
to have um
ryan uh these have been on a few times
so yeah
um okay question related figure one
stephen
yeah just one question when you
mentioned the predictions and
inferences do you tend to think about
like the downward predictions
across all the components and then the
inference is more
although it's happening at all
components more in terms of like the big
block
jumps between like what m1 and m2 is
inferring in relation to each other so
you tend to
think about it more that way so you look
at each piece as a
as more of smaller ideas
predicting down and linking and then the
inference is more
thought of in these you know broader
sense of something that you could get
your head around
as a human so to speak
um it depends on which level of
description you're currently focusing
but um in the sen in a sense the answer
is yes
that um once you
kind of stick another layer on top of it
so to speak
that layer can start to um it's
basically perceiving
uh in a weird way you could see say it's
trying to perceive the perceptions
and then that allows the system to
report
on these perceptions so that's like a
kind of meta
and meta-level
representation that gives the system
this capacity to reflect on its own
on its own inferences on the lower level
we have also worked on
paper where we apply this to the
precision on the likelihood
and should probably not get into that
too much for now but
it's if anybody's interested so let me
just i
found i've gotten access to the live
stream now let me just post
say hello and then i'll make you a mod
so that you can post links
but yeah thank you for adding links to
the live stream
anyone else have a question on figure
one
otherwise it'd be nice to i think
continue this incremental
unrolling of the model and then we'll
definitely get to
a lot of different topics i think in a
broader discussion too
i'm in the live chat right now so
here's the paper by ryan smith
and then there's
now you're a moderator so now nice
okay steven question on finger one or
broader question
uh yeah just building on what was just
mentioned a second ago with figure one
is
you know thanks for that clarification
and
um so like you say this this this idea
of like a meta
level of inference is useful and i think
and this
came up in the previous um live stream
with ryan smith that there seems to be
something about the updating
between so as well as like going from
one chunk to the
next chunk so to speak of m1m2 and
giving that as a way to get a handle on
an inference
there's like something that can be done
with whatever gets message passed
up and so from what my understanding
that looks like the two ways into the
inferential piece so
great yeah so that's where um
essentially one of the core innovations
that we present in this paper is
something
we like to call deep parametric active
inference
um where you're making inferences about
the parameters of
lower level models
and then that is guiding your your
expectations
and we're going to get into that more we
once we go down
this path and let me see
so i've managed to get access i think so
what does the
moderation help me oh
you could post links i think people who
are moderators cannot post links but we
got your links
so the tutorial paper and the meta
awareness paper are
in the live chat so thank you yeah good
okay
cool um yeah so
i just to illustrate the point i think
it makes sense to go
to go further um because
essentially what uh i think it was dean
was mentioning or was it dave i couldn't
see
and it's my own site but um
um anyway so
and what was mentioned is that yeah you
have these lego blocks and you start
building your hierarchy so to speak
and one of the things that was
had already happened by the time i came
around was this step presented here
where again the circle here with the pi
inside is a variable
and the simple act of connecting this
variable
to the state transitions on the lower
level so basically
the variable pi which stands for policy
starts to dynamically
control your beliefs about how to stay
how the states of the world equal all
the time
yes so this is um
then controlled by the prior
um and this is a really a little bit of
a funky
aspect of active inference in that
formulation
because the prior on this on these
policies
is informed by a the expected free
energy
the expected free energy i call is funky
because it recapitulates the entire
generative model
down below the expected free energy
includes the expectations of the
organism about the world
[Music]
so there's this thing that carl
and thomas bar had called and
the generalized free energy where they
reformulate this
and impact what's inside the policy
variable and in terms of a whole kind of
a generative model that mirrors um the
perception
aspect um don't get need to get too deep
into that that's
essentially unpacking what uh the
expected free energy here does in the
model
um it's very
important because the expected free
energy is what introduces
the what i call the phenotypic
or phenotype congruent action model
it's also going to be answering one of
the questions that came up i watched the
previous live stream that you had on
this paper
and we'll get to that in a second but we
can use it to answer one of the
questions that came up about
um whether the effective charge
uh why it depends only arises when there
is a difference between the prior and
posterior
objection we'll get to it
so the expect free energy you can think
of it as
recapitulating the entire action model
with one big difference
namely that it's biased by
phenotypic outcome practices so
it's essentially the phenotypic outcome
preferences basically
bring into an active inference
what the reward function does in
reinforcement
it does this because it's essentially
biasing the way the agent behaves
towards the world
and trying to match make naked match
its preferences that are specified here
purely in probabilistic terms so
[Music]
the phenotypic
preferences can be something that can be
engrained that can be learned
it's not really it's pretty agnostic
where it comes from
um that's because there it has this
hierarchical nature so i have models in
which these preferences themselves are
state dependent
so let's say you're hungry um
when you're hungry your preference uh
factor for um for food
is then is up regulated essentially it
makes um more uh a stronger driver
of your actions essentially when you're
tired
then you have a stronger preference
against exerting effort
so there's these kinds of um these
preferences themselves can be made state
dependent if you just add another lego
block on top
and you start having inferences about
how hungry you are how tired you are and
you can
have an organism that's managing its
energy resources
then there's this last component that we
discussed is the e
here the e matrix
you can think of it as a kind of
habitual
prior or what they call in mobile in a
reinforcement
and they call it model 3
it's just counting the number of times a
particular action
occurred it's not evaluating it by any
any like by any rewards
or something like that it's just um
i mean i would i actually don't like the
term model 3 because
in essence it is still model it's just a
model that has a separate parameter
for every possible action right so just
counting
it's kind of like when you took your
drivers
lessons and i remember repeating
mistakes
not because i liked to make those
mistakes but just because i made them
before
my body and brain kind of
stored that information and i ended up
repeating those mistakes just because
this pathway has been explored before
okay so that's like a little bit of
unpacking here and
the way you can read this diagram
is again from left to right so you start
with the action model
and the expected free energy guiding
the a priori expectations and this is a
kind of
crooked scientist i would say it is
biased towards not what you believe
the world to be exactly but more towards
what you would like the world to be
like and or what's if you are
currently doing well what you would
expect the world to be
so it's pretty um
it's it's an intentional but yeah like
the bias is introduced in that site
and then if you look on the other side
you get the perceptual evidence
it's the free energy you can think of
that as a kind of reality check
so i can have lots of
expectations about what i want the world
to be like
and where i want to end up or what i
want
my shoes to be like when i buy them i
remember this example from last time
um but then i need perceptual evidence
to actually see if the
shoes actually fit after i bought them
let's say
um so
this perceptual evidence gives a very
it's a very crucial
component of how
how the whole the kind of perceptual
feedback
without that your your agent would be
living in a fantasy world
right so we can if there's unless there
are any questions we can move to the
next
slide anyone uh can raise their hand
otherwise stephen question on this
figure or a broader question okay go for
the question this figure
just want to ask you one question there
with your action model
because with expected free energy you
often have the risk
ambiguity and pragmatic gain as three
terms
on one side so is it like that the
pragmatic gain is is built into the
action model
implicitly so it's kind of
you you've rearranged it slightly with
that in mind so that all action
has some sort of pragmatic game built
into the phenotypical
morphology of the animal or something
like that
yeah so here in the pragmatic part so
that's the kind of the see the outcome
preferences
like your preferred observations
essentially is built into
its part of the phenotypic risk so if
you look at
the equation on the left and so the
right hand side to the left term
for phenotypic risk you see there you
take the the
difference between the logarithm of your
expected outcomes
minus your preferred outcomes
then in in terms of units of nets so
information to your experience so what
you're essentially the risk
here is just quantify in terms of the
the difference between your preferred
outcomes and the expected outcomes
given a particular action
that makes sense cool and
it's also interesting it's the natural
log of o sub
pi so it's conditioned on a policy
so it's not like some sort of all by all
chess boards all strategies all
situations it's
very constrained with respect to what
actually matters which are
in the end the affordances in the niche
of the actual agents
in the in its scenario so it's really
cool to see how that gets baked into the
model
not like a secondary pruning or a
heuristic
yeah so this this just falls out of
calculating
and the expected to energy under a
certain um
policy and so this g is conditions on
policies in that sense
um and one interesting aspect here is
that if you make the generative model
more
sophisticated then this g is going to
become more sophisticated as well
so you can add if you add
learning or parameters of let's say the
likelihood then the aspect of your
energy
also expands accordingly and it ends up
having a term for
active learning so your agent can
anticipate
basically that exploring the environment
can allow
uh to reduce uncertainty about these
perceptual
um mappings so then
you get an agent that's intrinsically
curious about the world
you can do the same with the b matrices
or the transition matrices
so you get an agent like a child who
kind of just
experiments exploring different states
of the world
and then starts picking up on
different kinds of control that it has
and can even at some point can even
learn to anticipate
that if it's um
experiments in a certain way it might be
able to learn new
things about these methods so
this is this is currently in not in this
particular model because
if you remember to do that you need to
add
variables to the particular methods
and the nice thing about this lego box
of active inference that speaks that
you're
completely free to just to add um
to make anything variable as long as
you can yeah as long as you specify
certain the probability
distributions you can do the same trick
again and again in different on the
street in continuous state spaces
so i think this is a nice segue into
oh here you first introduced in table
three
some of the equations
um here we have table three up on the
screen or do you want figure three
no i think we can go on to i mean unless
somebody wants to go
deeper into this but i i think you
already kind of discussed this
[Music]
yep it was really helpful to see the
table anyway laid out this is work yeah
this is actually not the way i delivered
the table to the journal
it's just that they have three i mean
it's crazy you pay them this
money to fix it you know but then they
make it worse so like basically they had
like a new what
layout and their webplay items and
messes up the
most of the figures and
so when you want to read it i would
really recommend downloading the pdf
and not using their web
oh yes this is their web layout it it
definitely makes sort of a false
equivalence
or a way of making it look like there's
something missing on one side or the
other
yeah so just read the pdf and
it's unfortunate because it's supposed
to be their job
well here we are on figure three and so
we have just the figure three and then
we also have
that part with the ac if you want to
kind of highlight that because i know
that's something we really want to
understand
yes so um just we're going to continue
our our
um building this um
different we're adding these different
blocks together and
now what we add on top of it is we have
g
this is the recapitulation of the entire
action mode
we add a variable on top of it that
modulates
the extent to which i rely on this
action model
and so the precision gamma can take any
barrier
value between 0 and infinity and
and it just tells me when i
predict what's going to happen in the
world and i
anticipate what's going to happen um
how much can i rely on my action model
that's biased by my preferences
so this is not the same as
um i mean yeah
that's kind of where it comes into into
um
story why and it's this effective charge
that we're talking about
ends up being depending on the
difference between
pi and prior and the posterior
so essentially what this precision is
tracking
is tracking the match between
the predicted value you can say of g
or predict for the actual policies that
i end up selecting
um the actual state transitions of the
worlds
and how well they are predicted by my
action
and this is my crooked scientist model
right so it's like the max
action model that's trying to realize
preferences and
effective charge is essentially the kind
of um
we call it like that because later on
it's getting a special role
and when you go to hierarchical setup we
add one more
lego block on top of this but
essentially um
whenever my um
whenever um so if you unpack
this effective charge equation you see
that
it's calculating the difference between
my prior policy vector that's just based
on my preferences my action model
um and the posterior
and that's the one that happened that i
have after i integrate perceptual
evidence so
and then that difference so that's where
it's a little bit hard to imagine maybe
but
basically um the difference between
these two
is kind of like the rate of change you
could say
over time of my beliefs
and then you take the dot product of
that with the expected free energy
and what what you essentially want to
know is
um after integrating perceptual evidence
did they get closer to
matching the expected free energy the
distribution anticipated by that
or did i get further away so that's why
i call this
phenotypic progress if i get
if the expected pure energy is a bad
predictor
then this term ends up being uh negative
if it's a good predictor it ends up
being positive
and i mean there's like a little bit of
a play with signs there
and we just define it in a way that it's
positive the
positive value is a good thing
[Music]
that's like always a little bit
confusing because in some
different fields they use there's even
fields where the
free energy is defined in the opposite
way
so the whole story clips on his head
that's why you always have to be careful
how you
how you define it locally in each paper
and yeah when you come from a different
field you have to
you know make sure that you've got your
signs
in your signs in a row so to speak um
yeah so if i can say that one major
field there difference is that
physicists
often go downhill gradient descent
optimization we're going to minimize the
loss function
and biologists often talk or think about
hill climbing
and fitness peaks and optimization
maximization and congruence in the best
possible world that kind of pangolos
world
so totally agreed and especially when
there's a lot of natural logs
and negative signs and differences and
divergences that can only be positive
and things that are strictly negative or
bounded but when
it's something where it really needs to
be walked through slowly because
it's so easy to get tripped up in how
these things flip back and forth
so yeah really important notes to kind
of just go slow and
really make sure that we're using the
right tools
to establish that we're connecting the
right qualitative ideas
with these variables because it's not
just like you throw up the equation and
then it's going to be
easy to define what each of the
variables are for real systems
yeah and on that note
we basically yeah we have um interpreted
this comma as
uh in the paper as a type of subjective
fitness
and that's because literally is tracking
the degree to which your
um preference biased action model
is fitting with the actual perceptual
evidence
that you're getting back and and
that's why the effective charge can only
be non-zero if there's some mismatch
between your prior and your posterior
beliefs about policies
because um
there's only when there there's some
mismatch between what you expected
when you got and it makes sense to talk
about
updating your beliefs about procedure
and can be in a positive direction or in
a negative direction so
my fit can be actually better than
expected
and or worse than expected that's why
why describe in the in the abstracts
that this lens is assigned
to these predictions essentially
because if you think about just in terms
of predictions it's kind of
well prediction is either wrong or very
wrong
okay so then i mean if you want to know
um if you go to this meta level where
you're estimating how wrong
am i so is my prediction getting better
or worse
that's that's where the sign comes into
into the story and where you can
talk about um improvements or
uh improving or worsening
state of the world speed and state of
yourself
and this really applies to any kinds of
states by the way so it
can um
it can be about internal states tracking
and as i said hunger
and fatigue but it can also be about the
objective states of
other specifics so um
this kind of subjective fitness can be
linked to any
arbitrary state that of interest
and if you go to the next level then the
state
of inference can be an observation
for the next level so that's
hierarchical trick
and is i think the power of it
is that yeah we have freedom to
do what we want to do with our lego
blocks
depending on this system of interest
but we try to keep it simple while we're
still just demonstrating
possibilities but then the implications
get
really really big once you start to
release the simplicity constraints
and you just go wild on constructing
models hierarchical models with
different
you can have expect your energies at
different levels you can have these kind
of
precision terms at different levels so
you can have competing
um affected charges
you can have the effective charge from
your lower level let's say
you're trying to fight your addiction or
something like that
the lower level parts of your system are
like kind of great
and generating this crating and the
higher level parts are like trying to
generalize and generate this kind of um
self-actualization or something like
that where you basically end up having
conflicting drives
and so i mean that's where where we can
go
but to get there we need to
move to add states on top of this
[Music]
and i think and that's there yeah
if there are questions yep i'm gonna ask
a question from the live chat
and then anyone else who has didn't
spoke yet or asked a question
and then we'll ask a question about um
anything else we've talked about steven
so um in the chat someone asks
can we relate affective charge with
motivation
as motivation can also affect policy
so where do we how do we think about
motivation in this kind of a model is it
an affective charge is it effective
charge
yeah so um
motivation in that sense is a very i
mean kind of fuzzy concept right but
um if you think about the
gamma term here it's modulating the
extent to which you're
relying on your action model
and the c the preference factor
kind of modulating the um
[Music]
the extent to which you're driven by by
your preferences
and combining them together essentially
means that um
you're if you have um
let's say a high and yeah
you need high confidence in your action
model to be
actually allow it to influence your
your expectations so in that sense
there is definitely a link with
motivation but then again you also need
preferences that motivates you to move
towards them
right so what's kind of interesting is
if you take away the preferences
then you can have an agent that's
motivated entirely by
epistemic family
[Music]
so i suppose
to some extent um
it's kind of interesting because you get
the
precision starts to modulates
curiosity and so that's a different kind
of motivation
anyway i can say much more because it's
such a fuzzy concept
but very true i reward motivation
curiosity motivation
there's expressivity in the model to
actually talk about motivation
with respect to specific framings of it
yeah and and um
the way i've recently thought about it
is also that
if you add a higher level and you
connect it to
this preference matrix um
you can basically modulate the extent to
which
you're motivated by different kinds of
outcomes
and that means that um you're if you're
more
like a monitoring on a higher level to
which extent you're currently satisfied
for example um so you're
you're hungry so you upregulate your
preference for
eating food and then you get your food
and you get feedback intercepted
feedback that you're you're
you're satiated and then
you're open for um more for
epistemic drives let's say so um
there's an extended yeah a sense in
which
the various types of motivation have to
be balanced
by a higher level this current
figure that is not able to do that in a
way
if i mean our whole lego box can
definitely do that
but the current figure i think is still
um doesn't have dynamic preferences
i think that's what you need to get a
more satisfying account for
motivation in general thanks for that
awesome response all right stephen and
then anyone else who raises their hand
just one question you mentioned dot
product with expected free energy and
just
just if you could just clarify that a
little bit because i think
you've got something to do with the
precision you've got the
the larger free energy piece so if you
just clarify that would be helpful
um yeah so this effective charge term is
not something we came up with
right it's something that comes out of
the maps when you start with um
this uh gamma distribution um
sorry the capital gamma distribution is
um particular
mathematical um yeah
shape and exponential natural exponent
based on natural exponent
and when you use that as a probability
distribution
so it has this kind of tail
that runs goes towards infinity um
the expectation value of this tail is
regulated by
what's called here the temperature
parameter and
also called the rate parameter in other
contexts
but essentially the temperature
parameter kind of regulates
um how um how
strongly this yeah the distribution is
shifted towards zero
and essentially
what's what happens is that this when
you use that as the probability
distribution and you try to optimize
the best this better parameter
to best fit what's happening
your you can do this for energy
minimization
to do that and what you get out of it
kind of for free
and once you write that down in
probabilistic terms
you get this objective charge there and
what
i was talking about is essentially an
interpretation
of what okay this is what we got out
when we took the generative model
minimized let it minimize variational
free energy
on these this battery parameter then
we just it just kind of spits out this
effective charge too
and i was
yeah then it's a matter of interpreting
like what does this term mean
in mathematical sense and essentially
what it's doing
is taking dot product between two
vectors
one vector on the left is um
the difference between the prior and the
posterior over action
and the other vector is um
the expected free energy for each policy
and essentially if the two vectors are
pointing
in the same direction for an organism
that's bad news
right because um if
my posterior is um results in larger
expected per energy
then that's uh that's bad because i'm
trying to minimize it
and then wait let me turn the light
because it's looking good
um dark room solved
what's wrong just solve the dark room
and yeah so
the the idea is basically that the
expected free energy you can think of it
as a kind of landscape
across the domain of potential actions
and
what i want to know is that um after
integrating my perceptual evidence
and did i get close like did
what that vector look like on the left
did it match the original vector i had
in terms of the expected energy um
that's why if you look closely it's the
prior minus the posterior
because that's the negative rate of
change right it's
the posit like the actual rate of change
would be the posterior minus the prior
but we flipped the sign there such that
you get
um you can interpret the effective
charge as like being positive
when the precision goes up being
negative when precision goes down
is that does that answer your question
satisfactory
yeah i think that's very helpful thanks
one
one example that came to mind was like
you're driving and you're having a
maps application tell you it's gonna
take one hour
and then as the estimate gets worse it's
like it's bad
if you want to get there if your
preference is to get there on time now
if your preference was to get there
later
maybe it is more neutral but then as the
update is changing and your relative
policy it could be like oh it's going to
be 18 more minutes because of this crash
up but then this speed it up this way
and so we're always in a really specific
situation
conditioning on policy and the
information we're getting and so we're
not doing the whole
traffic city flow this is about like the
person getting the info from the screen
and then making decisions about oh maybe
i should get gas here or not
not every possible decision they could
be making so very
very interesting way to frame this
variable
and this dot products and the way i
don't know
how many people here familiar with the
way this kind of vector calculus
uh tends to work that essentially you
can just think of it as the dot product
kind of
match yeah calculating the
degree of overlap between the vectors
and if they're anti
uh if they are exactly in the opposite
directions
then the dot product is very negative
they're pointing in exactly the same
direction than this maximally positive
um but
and are these yeah what are the
dimensionalities
so you're talking about them as vectors
but are they scalars there's just one
entry in the vector or are there
potentially multiple or
how do we think about are these one
number or is it a list of numbers like a
long vector
and so in this order formulation of
the expected energy it was like one
value per policy
essentially so every policy has
which is like an action sequence and
so every policy has a total kind of sum
of the expected free energy associated
with that
so then it's a vector in the sense that
every policy has its own
element in the vector but more recently
we've actually extended this in the
sophisticated
sophisticated inference paper because
um i mean anybody
who's worked with um policy spaces
and knows about this problem of
combinatorial explosion
that once you start considering
um courses of action in time
then every time every point in time you
expand it
further uh the more um yeah
the more untenable and intractable the
problem becomes
but in a more recent iteration we
actually sub yeah divided further in
terms of the
actions components
in turn yeah instead of having one
single
policy vector that has to regulate do
all the machinery
we have every time step has its own
action variable
and your performing impedance
doing inference on that on every time
step and
this makes the problem prevents you from
having to integrate everything right
away
the end result of that is again an
integration but because here
it kind of allows for parallel computing
let's speak
anyway but that's that's a different
paper i i can actually also post it
i i think we actually read it but you
know it all blurs together
but we did read sophisticated inference
i think at one point
oh yeah yeah nice yeah you tweeted lots
of papers yes
that's why you have them catch up we
gotta catch up you're leaving them as
fast as we can get to them
i mean i made uh more recently uh in a
paper
on called sophisticated effective
influence where
um so you have another thing to catch up
but it's essentially combining this
effective inference story that we're
talking about today
and combining it with this article
research
and which allows
you to simulate an agent that
responds has an effective response to
imagined
futures it would be cool to
maybe at some point to come back to
discuss that one as well
cool all right so dean uh with a
question and then anyone else who raises
their hands
casper when you um go from a
2d m1 m2 to a 3d
action is that
have you thought a little bit about the
sort of the less about the integration
more about the
deflation and and inflation
that happens when you go from
fewer dimensions to to to more
um yeah so that's
kind of one of the motivations for going
to new
types of generative models because
this policy variable here can explode
pretty
quickly once you get to multiple steps
in the future
and you need somehow to reduce the
dimensionality
of the state space that you're
considering and then
what i kind of what kind of one thought
that kind of suits me when i build these
types of models is that
even though um as we say all models are
wrong but some are useful
right but even though that's the case
and
we know that the organisms that we're
trying to model have exactly the same
problem
that we have namely they're trying to
make something that's generally
intractable
tractable so the simplifications
when we're trying to build a model of
their model of the world
and you can actually justify the
simplifications
in the sense that they are trying to
deal with
they have to do oversimplifications as
well to be able to make sense
any sense at all with their empowerment
and
i mean i don't know if this exactly
answered your question but this was
part of it came up in response
this year had an interesting point about
the dimensionality increasing
one thing that kind of happens is that
you basically have to stimulate
potential futures internally once you
start conditioning
these days on your actions that means
every possible action has a
parallel kind of process of inference
that's happening um to predict what's
going to happen in the future
in every dimension you add on top
[Music]
can potentially um
make the whole thing interactable so
we're always
kind of facing that challenge
yeah dean and then that's quick
follow-up so
so sometimes you hear the expression oh
well
that problem is going to require some
outside the box thinking
and of course that's so ambiguous nobody
really knows what that means but what
you've done here i think
is giving people an opportunity to
get out of the spatial envelope get out
of the
i'm an agent and enveloped by the world
around me and you've given them
a bit of an eyes of this perspective
they can actually
get outside and see how
as an agent they're perceiving the world
how they can then potentially act on the
world but as you said
they're constantly updating a lot of
this stuff isn't
front of mind as they're doing it um
but i think that's one of the big things
about going from 2d to 3d you're not
just
zooming in and zooming out you're
you're not just now you're able to look
down on something but if you hit the
button on the
google map and you suddenly see it 3d it
doesn't
it doesn't stay at one position it
actually circles
around the thing that you're looking at
and i think that's what this provides
people is that sense of
not just being inside of something but
actually being able to step outside of
it as well
i mean that's something that um
yeah actually does happen in this type
of model
is when you add this um pie let's say in
m3 and
you end up expanding the whole thing and
it's is like you said like stepping from
two to three 3d in a sense
because you you're
you're expanding the whole number of
possibilities basically
and in the same way it's kind of hard to
wrap
your mind around it and i think that's
part of what makes these figures
hard to read for people especially when
you present the top level right away
it's like asking somebody to step from
one from one dimensional to
three-dimensional
right in one go you kind of have to go
through the the
increases in dimensionality step by step
so this is also part of what motivates
this
incremental presentation
thanks awesome question thank you dean
so blue
so we read this sophisticated affective
inference like a long time ago and i
always think about it and i think that i
brought it up in the dodge zero live
stream actually
but i thought it was the big five paper
i think we read them like right at the
same time and they they're very
different
but this um sophisticated active
affective inference was really
um like prevalent with anxiety like the
future
time steps the further out you go in the
future like the more
like you can't predict what's gonna
happen and so that's like the underlying
basis for anxiety and i thought about
this
and i also thought about um the question
about motivation and it made me think of
tony robbins has like
this um like theory that there's like
six like driving factors that like
influence people or motivate people
through life and like you know depending
on personality type or whatever and
um they're like uh certainty is one of
them
um uncertainty is also one of them like
people who like variety or
um then there's like growth and altruism
and i can't remember like all of them
but what they
all are but it's interesting to think
about like the motivation
what underlies like what's an underlying
motivation for people and how that
relates into this type of model
as well as like those driving forces
through life like how
you might start to model those things
like um you know someone who's driven by
uncertainty versus someone who's driven
by certainty that like the
the uncertainty driven people might
place more of like an epistemic value
uh than an actual um then an actual
um action reward value so it's just
interesting to think about that
yeah i mean there's like a paper in the
works that got
installed unfortunately but um i think
where we're trying to do something like
that where you're
talking about um the way the big five
um have kind of emerged as
apparently a pretty strong factorization
people's behavior people's behavioral
tendencies over long periods of time
so their personalities
and why they tend to factorize like that
and
and to which extent you can capture them
with
something that looks like this and with
at least one more layer i would say
but to some extent yes you can
capture this tendencies towards
exploration
a kind of exploration drive
versus so risk aversion and risk
[Music]
basically risk seeking behaviors
um cool blue that was really interesting
and it reminded me about how people
prefer let's just say to read
different amounts and to read different
topics so for some people
historical fiction versus fiction
science fiction
all these different genres and
sub-genres it's related to maybe what
their regime of attention
will latch onto and that's something
that's different as you age
uh and it's in cultured and it's
embedded as well so it's kind of an
interesting example that we could go
into
and then we did a live fact check
active11
way back when in 2020 we did do
sophisticated
uh affective inference the simulating
anticipatory responses paper
and that was way more anxiety driven
no it wasn't just because it was 20 20
and then also the first one of
this year with adam saffron and colin
deyoung
was the big five cybernetic big five
kind of free energy inspired
or based as well so um yep it's just
it's good you know you you you did say
we're kind of going through them fast
but
there's so many to read and just to even
get a little bit of a grasp
on it it's it to read 25 in a year
or one every two weeks it's kind of a
pace that we have to
hold up to but i'm sure you read more
than one every two weeks
so yeah yeah i i guess i did um
i did read it somewhere and i was like
whoa you um
i wasn't sure i didn't remember whether
it was like sophisticated inference or
sophisticated affected intensive but so
what is the effective one
it was just the conference proceedings
though so it was very
short um yeah it's a little bit too
minimal i think to really
um it was more like a technical note
yeah it would
be hard to really get it just based on
if you're not yeah so familiar with the
modeling
and the actual like nitty-gritty you
know like
it's like in that sense confidence
proceedings are
just a way to communicate to some uh
people who are just in the exactly in
this technical
part domain not best for communication
to broader
scientific audiences yep well
kind of on that point and anyone can
raise their hand i
move the slide to the additional
information where there's
the code and um maybe just
what would you say about the code what
are the inputs or the outputs what would
somebody
need to run this code or like what could
they do with it
and it's really cool that you did
provide all this information but to kind
of bridge that
gap that you just mentioned what does
this function do or what do these
different scripts do
um yeah so
essentially you first need spm 12
is that contains the core functionality
for um
yeah that it's based on and then
these scripts are like additional
or like adaptations of scripts in spm-12
and the only thing you need to do is run
spm mdp pbx emo
app um
so that stands for emotions factorized
which is something i worked on at some
point and
but yeah in the in the rest of the
so let me see
sorry that's
of course not enough to
for you to
and then you just get the model that we
already have
uh re-run generate
here yeah the one that's on this uh
slide before
so this yeah this one yeah and the
one above it
so let me just it's not by now it's so
long but i would have to
um this is cool but um
we're in the process of um what i would
recommend actually in the future
i mean i don't to be honest i don't like
mob at all
um the only reason i worked with it was
that
the existing spm
and active influence modeling was
part of the existing spm package
but there's a lot of yeah
important work has been done by alex
chance and connor heinz
and a few others and to
transform everything to python and
to do computational optimization while
we're at it
so there's this github page called
interactively
yep here we are on it pymdp
infractively is the github repo
yes so um instead of
trying to get um
trying to get motlop running on your pc
i would recommend
just working with five and then
in the future um we'll have a module in
there that
can do the same as what we did in this
paper
um awesome so that's something i think
is much more sustainable for the future
we're working on integration with gpus
etc
to make things that can be simulated and
scalable in scalable way can integrate
with tensorflow so you can even
do um kind of
hybrid modeling with what they call
amortized active inference it's like the
learning models that are connected
to components of these lego
lego boxes that i was describing
but if you want i can i mean i can run
you through this
mdp in motlock it's just that i'm not a
fan of
myself so it would be i think it would
be a little bit of a yeah
i think yep let's uh definitely have a
model stream for the python because i
know that will be something a lot of
people
are interested in because the matlab it
has a
certain charm to it but i can see how
you might want to develop with other
approaches
even though when christopher and ryan
walked us in the model stream through
the code
just seeing how the matrices multiply
there's something nice about how it was
done
in matlab but it's not interfacing with
all these modern
tools like tensorflow that you mentioned
so
um yeah um anyway but
uh let me see so
i think we can yeah we can move on
but uh i think what i should do
basically based on your feedback is
write um
a little bit of an explanation of what
to do with those codes
if you want to run it let's say you do
want to use mobile if you want to run it
what you should do and that's actually
useful
feedback yeah
the reason i added these codes was
mostly for
yeah reproducibility instead in case
other technical
folks want to look at what i did but
and it's not really out of the box in a
way that
anybody not familiar with it
could easily use it
yep my advisor she would always say
make it so that the anthropologists from
mars will know what to do with that
spreadsheet
because even for people in the field or
even yourself
months later it's like wait what that
was my research
yeah yeah i mean the proper
proper practice is to add like a how to
like a
read me page on the github
it's in my mind the kind of
transitioning away from what
i kind of felt like but i do agree
should round up that part of the
documentation
well yeah yeah um
blue or steven uh either of you raise
your hand
um just just one point about
the effective charge piece that you
mentioned before
can i just check is is that like an
in-between
um level between
one inference layer and the next
is it so that is that correct
that's entirely correct once you go to
figure um
[Music]
i think it's figure six
um let me see here
seven sorry yep
so um essentially
now we connect um
what's happening in a higher level
connected to inferences about
our sort of predictions about what's
happening on the lower level
and that's when the effective charge
basically becomes like
an ascending message that informs the
inferences
um so
there is an equation in the manuscript
i don't see because it was a
separate table oh this part
we split figure seven yeah this is just
this these are the prior so this like
um doesn't describe the posterior
beliefs
the effective charge basically factors
yeah comes into
yeah i i understand there's many figures
in the paper
you didn't include that one but if you
go
to
it's in in multiple places
[Music]
essentially what we call effective
evidence on page
files page 420 but
the actual page is 23 you know with pdf
but
okay um just for
here we go yeah answer your question and
yeah yeah so
just to illustrate what's happening uh
or to explain
and in this paper use bars to
illustr to indicate posterior beliefs
so here the bar is on the left
the bark s is like posterior believes
at time capital t so this is the
cross trial time steps a large um
yeah large yeah cross trial time
essentially
a subscript the superscript here is
indicating the effect
effective state so um
state the posterior effective state on
the higher level is
a soft max function of um
that consists of the prior
belief which is the logarithm of
the previous posterior from the previous
time step
multiplied by the transition matrix
so that's the where the prior comes from
and then this term that
you see after that comes from what we
call bayesian
model reduction and it's what you need
to what
happens when you want to connect a
discrete and continuous state space
modules
and it drops again this term drops out
of
the derivations that you can do
based on this um formalism
bayesian model reduction and in this
case this sort of free energy
minimization
assuming that changes are small enough
locally are small enough to
make this connection and then if you ask
what's small enough well
that's something you would have to test
in in the world
and see if this approximation holds and
essentially what you see here
is the effective charge coming back to
haunt you so to speak
but now as a message that this passed
upwards
so the higher level state
is consists of
two um kind of extremes and so the
the extreme positive side so beta plus
and the extreme negative side beta minus
and at any point in time the organism is
somewhere in between
it's never extreme it's not it's never
like
at the exact extreme it's it's beliefs
just like you can never have 100
certainty about anything
because down downwards in the
hierarchy we make predictions that's
where we do beijing mobile averaging
and upwards you have to gather these
messages so that's what i call
effective techniques that's where we use
bayesian model reduction
yeah so that's essentially a very long
answer to your question
but yeah no thanks
just just one other thing with that is
this then gives a way
for somatic kind of processes
um you know in every day or even in
trauma to be
integrated in a way because it could be
that
non-cognitive processes could be at play
in adjusting this effective charge or
keeping a score of that
um and then that could then be that
could give a way for that to influence
perception
or action model selection
yes and and this high-level state is not
constrained in any way
in terms of what you you can add other
types of evidence from other
action models and other
components of your system can add their
own effective charge
so um that's at some point in the
beginning we mentioned this affected
workspace theory
so like
we call this effective charge because
it's essentially a pretty domain in
general
it can be gathered from any kind of
action model it can also be used to
model the way
and when you're listening to music your
attentional
action model has is kind of being played
around with
and with congruence and this congruence
and you can kind of um
create mismatches and matches
and you can create fluency
and this this fluency and this will
create some kind of effective
rollercoaster so to speak so these ups
and downs
um can be gathered from an
action model that would be guiding your
attention
states um so
the question of what to attend to when
you're listening to a piece of music
could be something that generates
effective
effective charge and then informs your
balance state
it can also be purely associative so
[Music]
um it doesn't exclude purely associative
types of valence
so there can be certain things and that
comes back in the contextual evidence if
you go a little bit down
anymore i think it's here
oh yeah oh yeah yeah
so you can also gather evidence from
in this case we just talked about
contextual states in terms of whether
the food is on the left or on the right
but um you can also have contextual
evidence
being passed back up and
that can generate some kind of top
poplopian learning
where you just learn to associate
particular contexts
with particular positive states or
negative states
so there's also space to include these
kind of um what i think
are computationally a little bit less
interesting
types of valence uh paleons experience
because they're just kind of happy and
learning in a sense
and but it doesn't make them less
important for
um or experience so these
purely associative
relationships also come actually we
discussed that
in the there's in the discussion section
see how far we get nice
i wanted to ask actually about figure 10
what were you showing in figure 10 or
how could we read this
and does it apply to your model only or
future models
other categories of models
and everything that's happening here
from the orange
orange level downwards let's say is is
what we implemented
but everything that's in the grade is
basically something we presupposed
so we presupposed for example that this
rat already learns how to how the mace
works
and we presuppose that they have some
perceptual capacity
or instance some action control over
let's say where their body is you know
like
um so
all the things that we needed to
presuppose in order to actually do
the simulation demonstration or uh
yeah are in kind of the great great part
of this um
box um but the nice thing is that once
you so what if you follow the arrows
um these gray parts so evolution
development
and learning are it's also
comported in terms of time skills right
so
um and the nice thing is that it's
always a circular
story so you get um
these different nested time skills that
are all
influencing each other recursively
and once you get down to our actual
computational experiment
you you are at the point in time where
and you
enter basically yeah on the left this
grey arrow that points into the affected
box it's kind of yeah you can think of
that as
the one that initializes the simulation
so to speak so this gray arrow is what
initialized
everything that allowed us to even
simulate
it and then we explore the dynamics
of what happens within that and all the
other arrows
are basically illustrating that so
the orange arrows provide
priors for the precision for the action
model
for the perceptual state so that's all
the orange arrows
[Music]
then from the meta minimal according to
cognition level
again there's this arrow pointing down
to perform action jointly
the effects end up informing perception
and then it kind of passes through in
the way that you described also last
time
in the last session and that's where it
kind of connects to the world
[Music]
and then it passes back up again
and that's where this kind of perceptual
integration
happens and it trickles upwards into all
these layers
we could have simulated learning as well
so that's where
this orange arrow puts points back up on
the right
to the posterior phenotype
we didn't simulate learning because it
wasn't the focus of the paper
but we have yeah we have the machinery
it's in our lego box
to add that um and that
actually i think will make the story
much even more interesting because
then you can think about um
active learning and how that influences
affective states
so how people can enjoy learning just
for the sake of learning
or how they can learn to associate
affective states and contextual states
and how that time recursively yeah
influences their their system there's
one simulation that i've been
preparing where we
have a setup like this and we actually
simulated the
yeah the development and learning as
well
and the idea there is that you have a
child you kind of simulate the child
and it has this um hyper parameters
that influence different parts of its
lower level model
but in the beginning these hyper
parameters are very unstable
and then there is a kind of parent
simulated parent
that labels the states like
um like basically kind of reflecting
um and giving the system
labels to work with
and in the end what's the idea here is
that the labels
end up stabilizing the inferences
and this kind of to simulate the idea
that
as we know that social interaction is
crucial to develop any kind of emotional
control emotional self-control and
so there's these famous stories right
about children growing up with
involved something like that and then
never really reach a level where
they can exert this
um type of
self self control and reflected
that's the communicative capacity
that we have anyway so that's another
tangent
very very interesting one yes
very interesting stephen and then anyone
else with a question
and and in this diagram you mentioned so
you mentioned minimal metacognition and
then you've got
effect and context um so would that
minimal metacognition be
a sort of phenomenological consciousness
the kind of
the the the the the awareness that you
can't necessarily take a perspective on
and and it goes up into affect and
context
and that's where it's consolidated
enough to be able to
sort of take a perspective on it would
that be correct or
and that's how i do tend to view it to
some extent i mean
um the actual representation
of these precisions um is often
uh assumed or hypothesized to
be to occur in in a localized fashion in
the brain to some extent
in this trade and that's that's just a
hypothesis that can be tested
and it's actually an interesting part
and that
other systems other biological systems
can have entirely different kinds of
representations for this kind of
this precision term so
daniel works with ants colonies they
might have their own
way of encoding this type of
reliance on action mode and that maybe
has to do with weather conditions or
something like that there can be some
kind of shared
very minimal way of
encoding that reliance
it doesn't
it doesn't necessarily it's not in that
sense pretty agnostic on how it's
represented
and you can just test hypotheses and how
it works
and also um it's really interesting how
we can draw out
that link to qualitative concepts or to
phenomenological experience but
that's not part of this model this is a
claim about
a modeling architecture that lends
itself to certain
kinds of calculations that maybe
previously would have fallen within the
domain of
information theory or just control
theory or cybernetics
or just bayesian inference or just
multi-scale systems modeling
and i know that those are some of the
areas that you've drawn on
in your work casper which is why you
could kind of see that there was kind of
like
one two three but not four five six for
where the
active inference model was going because
you even
discussed how before some of your recent
papers
the active inference model had less
temporal depth and less
metacognitive depth so it's just
really cool to hear about how it kind of
remaps
where the questions and the modeling
approaches fit in
with respect to maybe previous
disciplinary approaches
so dean and then anyone else with a
question
oh you're meter dean
yep um so because you've got that
the time flow from left to right and
that's pretty much
consistent and you've got the parabolic
introduced from top down and then back
up
can you see casper the the idea that
around perception around action around
minimal metacognition and around effect
and context
there could be a counterclockwise spin
um because i actually saw that in the
way that
people were working not even aware of
this model
but that that's kind of the direction
where you've got the
flow across the bottom and then the
introduction of the parabola
from top down and then back up and
that's where you could get
actually get people looking through
both directions that's why you have the
effect of valence
that's part of where the charge came
from
or am i sort of confusing
the matters because i when i looked at
that figure i actually saw how people
in that flow state were able
what direction the spin was actually
going around
the middle the middle of your um
the middle of your of your figure
yeah i mean this figure is is more like
yeah it's not
it kind of moves away from the very
precise um mathematical
meaning of the other graphs right that
direct exactly progress but it's a
little bit of the same ideas here
like you said um in that sense it
doesn't really matter
where they're moving
i mean the reason that i put the upwards
arrows on the right is that
in temporal sense um
it's it's representing the posteriors
right so you're moving from the prior to
the posterior
but then if you would um because it's
nested
every next level means that you already
cycled
from basically yesterday's posterior is
tomorrow's prior earth
like yesterday's for serious two days
prior in
some way right so um
the capacity to integrate to the next
iteration
can also be itself a problem
so you see that a lot with people with
traumas
that actually integrate an experience
too strongly in the way they work
and this actually comes to very
interesting questions where it's like
functional forgetting
something like a lot of
maybe a lot of these meditative
practices actually
are able to do it's like help us forget
the relative the irrelevant bits or
the things that we shouldn't take to the
next iteration
right
the counterclockwise spin is just
essentially
making it expressing reflection and so
sometimes you choose to reflect on
something
sometimes you over reflect on it which
is what you're describing but
all i'm saying is is that when i saw
this it was
it was just more confirmation of yeah
i think it's i think it's correct
that's not just one yeah it's a nice
idea
and how it's uh i mean the reflection
part
and kind of becoming aware
of the things that you want to
so how you want to learn basically
um it's something that we
we did try to capture in
and it gets very interesting you start
to be able to simulate processes like
meditation
and what's happening in the mind when
you develop
control on these attentional processes
on a higher level
um anyway but i think stephen wants to
say that
yep yep just even go for it yeah just
following on from that and this this
what's interesting is how this brings in
this idea of
effective representation and how we
think of representation normally as
something as a thing
in the head as opposed to maybe objects
in the niche which we
act on or create or interact with and
now you've got an idea in st
of st2 i suppose of this kind of
what could be stored in an accessible
form
where the prior phenotype may not be
entirely accessible except
through science you know is is this
effective representation i just wondered
how you see because we've had quite a
lot of conversations about this
is what what do you see representation
being
in all of this all the possibility for
active inference and representation
yeah so um what i like about this
approach is that
we basically don't have to um pin down
exactly
and what the effective
state means as long as we we're just
figuring
trying to figure out what it is yeah how
it can be purged
or an organ and the organism can use
very limited
cues to infer that and then you have
like a whole kind of
organic
state of the system that that will
correlate with that inference
to some extent but just as the organism
is doing is doing that internally
um and usually we think about this in
terms of animals but
it's interesting to think about more
abstract types of representation
and three just in the end the
statistical concept
so i
work with models where you add a layer
on top of this effective
contextual layer so like here just in
terms of um
to link it back to verbal expressions
and if you ask me
what does the representation mean in
this case
it just has a very specific
computational effect on how
you can think of it as a generative
model generative models
so each effective state will be
correspondent with
certain modes of cognition
and action and
all the way down to the lowest level
the model doesn't have to
[Music]
integrate or like specify all of those
details
as long as you know how let's say the
connections from each um in each
level happen
the rest becomes like an emergent hole
and i think
i've tried to be sensitive of the way in
which
the internal representations
can be are not necessarily the same as
the actual effective state
if you look at all the
[Music]
different layers combined and
that's when you think about that that
then you start to get into really
interesting
domains like this disconnectedness
between your beliefs about your
effective state and
the way your system is currently
behaving and
the different kinds of affective
disorders you can start thinking about
[Music]
basically hallucinations or like self
green forests
and anxiety as indian one of those
papers
i guess i don't really have a very
concrete answer because these
representations
are are meant to be abstract
until you start to model their them in
specific context
and i think oh yeah you want to
yeah now i think that that that makes a
lot of sense and also
if our represents if
what i see as being a representation or
models that we
people think is in people's heads are
actually always something in the niche
that we work with so to speak so what we
know
is the action model for how to act and
perceive
to recapitulate it just feels like we
have that also in the brain but if it's
actually
to some extent this would be the most
concrete model
is the emotional imprint that helps
then undertake the interaction with
the models that we work with but those
models don't need to be in the brain in
that
representational form but you might need
some affective
code isn't it possible to know how to
and that ties in a lot with some of the
work with micro phenomenology
and some of the work with um working
with mental space
psychology so it's quite interesting um
yeah yeah so um thanks for this
yeah i mean um what motivated me
actually to move in this direction is
something that's not really included in
the figure that much here
that's super important it's the social
dimension
and then once you think of this
effective state
like kind of internal representations
that are inferred on any number of
queues
and any number of
arbitrary number of sources of data
you can also think of the facial
expressions of micron specifics
as being informative my effectively you
start
having a very natural way of modeling
things like contagion
and just in general this kind of
empathic responses
and where if you're also
kind of tracking the group
effect and that has
places priors on your in your individual
experience basically have a very natural
way of moving
from the connecting kind of the bodily
uh interaction with the world in the
niche as you
described to this abstract social
relations that we're tracking
all the time
so i'm involved in a project right now
that's um
forging like primate foraging and it's
really interesting to think about
the group dynamic versus like seeking
out your own
epistemic knowledge right so this is
just foraging and it's you know
agent-based modeling project
but i i wonder to what extent like
instead of
knowing which trees have fruit for
example like if i could just
follow a group member right like so i
wonder you know i mean just what you had
said about the social dynamic
is this kind of interchangeable like
just following the group like i mean
we're modeling contagion
and so forth so following the group is
that like interchangeable
for um you know epistemic knowledge
really um
so there's there's different things you
can do i mean
one one of the ways you could factor
that in here it's like
where um something that has been worked
out in the active influence communities
in terms of beyonce queues
basically queues that other specifics
give you
to kind of indicate what context you are
and then your action model specifying
for this particular context
what is the appropriate action
so a very simple
thing can be like in uh
whether you are in a context where
you're following another
specific or not it can be something that
i think bees have their kind of dance
that they do
to indicate whether other bees should be
following them
so there's like a kind of way in which
these levels can talk to each other
through signaling basically the
appropriate
what the context is and then from that
inference about the context you can have
the whole
action model kind of rolling out on the
lower level
and i think the following the behavior
that you described
does have a pretty direct um analogy to
our innate tendency to
um synchronize objective states
with our specifics
even with not non yeah even with
other animals that's actually pretty
interesting
something that we that other animals
also seem to be able to do to pick up on
nervousness across species right so
stress markers of stress we seem to be
able to kind of pick up on those
kind of cross cross species
generalized fashion
it's like endless number of we can go
down
here's here's one more little rabbit
hole looking at this figure
it reminded me of concurrent programming
languages
like golang and the idea of having
nested
processes that were defined by
interfaces
so we've been talking a lot on the
interfaces
as markov blankets or holograms with
crisp fields but
interfaces are also programming patterns
that make nested processes that can be
effective or tractable or run on
distributed computation without
halting or spiraling out so uh
in addition to the python potentially
there could be something like
a concurrent implementation and then it
relates to this question about
representation
like is the representation a static
object
is it a dynamic process and uh
i don't know what the formal answer is
but it reminds me of what we did talk
about with chris fields
with the types as processes and the two
spaces
so maybe by defining these interfaces
with the right
dimensionality or bandwidth or structure
however the screens are defined
then there will potentially be model
ability
not philosophical clarity on whether oh
is the group is the party conscious or
the person or the part of the brain
it's like the ant question those are
gonna be potentially
perennial debates but the model ability
of the ant colony evacuation
is going to be more akin to the model
ability of these other higher level
processes because of how
abstractly but also excessively defined
the interfaces are
yeah i think in a similar way the way i
see
these representations i'm kind of
playing with just thinking of them
entirely
as implicit and just just descriptions
of
um of something that
implicitly occurs
in the system basically like a kind of
tool essentially
um and if you make it explicit it
yeah it ends up being amenable to
modeling
doesn't mean that there's ever this kind
of explicit representation in the system
actually and all we're doing is making
these things explicit so we
can actually compute things
i'm pretty happy with being agnostic
about whether
there's anything and i pretty
uh i have no doubt in the fight of
representationalism
versus um like an activism i think
they're
they're both pretty i mean they both
have
points and i'm pretty happy with the
models being agnostic on this
question because cool models now speak
for themselves in the end
cool it's almost like you're putting up
your code and your model
as in evidence and if they want to
prosecute the case
if they want to have their debate and
debate whether your evidence
is supporting their notion or this
notion or some future notion
it's a second level question and the
first level is actually what you're just
laying out here
and how the variables are linked to each
other and then there's alternate
architectures that are possible yeah
every
every model is in that sense um just a
very elaborate hypothesis
and you can just test it
and like doing empirical work
yep and then every architecture has uh
yeah that has a can be compared to each
other
once you have um
and to do that you need to go explicit
and that's the only part i think where
we're doing being rejected
to make it uh to get a computational
grip
on it's a scientific grip you could say
actually i i have been working on
getting more observational
constraints in these types of needs but
there's such
an amazing
richness of things to explore by just
even just capturing the phenomenology of
our
that we already have accessible for in
the first person
[Music]
that's often you can already get very
far
by just making sure that whatever your
model is going to be
it has to be able to
recapitulate our lift experience
that we have directly accessible
it's actually one of the more recent
paper that i could share is
from generative models to generated
passages
i don't know you are familiar with
this kind of work by varela
if i can ask one question on this figure
casper so
you mentioned that models are hypotheses
which might be really interesting to
people because they might think about
the model as generating hypotheses which
it also can do
but actually you're talking about how
the architecture and the way that the
variables are connected
is itself not some authoritative claim
or final
uh description of the system but it's a
hypothesis
so it makes me wonder if somebody says
well i think that there's you know
letter um you know insert your favorite
letter here and i want to hook it up to
e
i want e to be influenced by a new
letter
r or something like that is that
going to um keep
this nice mathematical tractability are
there certain kinds of wires that if you
cross them
just the script is going to die is there
certain
pieces where we know that we can build
the legos really well or are there
just how do we know which pieces can be
tinkered with
and what structural changes could even
be done or is it like all
all by all
um well one of the constraints
is this basically the way it works
is that you can have only local
interactions
and that's the markov blanket
so in the end the way it's kind of
kept at least close to biological
plausibility is by assuring that
a certain thing that you only specify um
local interactions between variables
and that's what these errors do
so one kind of
forbidden thing to do would be to
connect
this policy variable directly to the
observations
because then you're breaking the market
as the policies are
directing in this case the relations
between hidden states
and the hidden states are generating
or like based on the hidden states
you're generating observations
predictions about them um
so there are certain kind of forbidden
things in these directed basically
graphs that being said
it's pretty universally i mean
as i said whenever there's an arrow it
actually implies bi-directional
interaction and you're completely free
to add a
higher level state that modulates your e
matrix so the
yeah the sky is the limit so to speak i
mean in the end
you should be able as long as you keep
this markov blanket structure intact
so you ensure that it's biologically
possible what you're doing
[Music]
then you can do yeah you can make any
number of states connect to each other
and
if there's like redundancy in your model
that should show up
because the free energy can be
decomposed as accuracy
minus sorry complexity minus accuracy
so any increase any increase in the
number of states in your model
will result in increasing uh increase in
uncertainty about
the parameters
and that's the complexity so like
occam's razor is built in
to the way these models work
so yeah in some
yes you're free to do almost anything
here but
if you look at the the model evidence in
the end should
we punish you with your major model and
necessarily complex
thanks for this awesome response we'll
have a question from dave
and then any closing thoughts and then
that will be it for 19.1
so dave go for it yeah two points
about the point of local interactions
only
they're kind of at odds with one another
first
is that actually the definition
of locality whatever interacts
immediately
is by definition local
second in one of the computer
simulations that was put together at the
fristan lab several years ago the dots
on the screen where he's trying to get
up
i know it's i assume a simple model of
how market microphone blankets work
he found that the distant portions of
the simulation
were more accurately modeled than the
nearby ones
and in my mathematical illiteracy i cry
out
oh so it's all working holographically
the intermediate entities are
focusing the more distant ones
yeah so this is really interesting that
you picked up on this because
and this is why we kind of um
we start with this markov blanket
criterion
but then when you start um when you kind
of go into the way
these dynamics work actually it gets
more interesting
once you're able to predict things that
are
um outside of your system
and the further away the harder it gets
usually um but
like you described um in this
so i think you're talking about the
markov blanket the kind of
soup the emergence emergency
the emergent life paper
and in that case
for some reason it also has to do with
the way you set up the state space
system
but the way he identified the cro
basically he did it just in terms of
cross-correlation
between the states of these chemical
particles
and the locations of the state of the
particles outside
and it was an emergent effect i'm not
sure i think it has to do with the
particular simulation setup
but if you if we kind of abstract it a
little bit away from that particular
simulation
when you go to deep temporal models
actually
and what you're trying to do is
you're trying to you could call it the
hologram i guess in some way you're
trying to create
an image of what the future looks like
outside of
the current blanket
[Music]
and that's why they call these the
temporal models instance semi-markovian
so lots of these interesting cognitive
phenomena actually emerge when you start
to
hack your way out of your blanket so to
speak
and you're trying to get a grip
on what's happening outside and that can
be
spatially it can be temporary so
temporary will be in the future
especially with the
places you can't reach
[Music]
so yeah that's a very interesting
question i think um
the seminar open aspect it's
something that has been actually
discussed recently
i think it holds an important key to
the way our cognition works is that
by kind of absorbing
information over time
and combining with the right priors and
the right so nature and nurture have to
be like kind of coalescing in a way that
gives you a grip on things that are not
immediately
accessible anyway
so that's a very interesting question
that i can't directly answer
because it's um we just know that for
any physical system to
like a biological system to work
we can only assume local interactions
and then the rest of the story is trying
to figure out
how far you can get it's just local
interactions
to create those what you call holograms
i guess you could call them lego
[Music]
is there a particular literature you're
drawing on can you use that term
i think chris field actually talked
about holograph specifically dave what
were you thinking of
holograms okay well i got that
from the chapter of mark solms
book that just came out in the last
number of weeks
uh where he first is talking about
actually
visiting uh carl fristen
but he doesn't use the term holographic
the only place i've seen that
in this kind of context is a some
discussion
of um using interferometry to see around
corners uh this is something that
presumably
people can't do but instruments can that
the
there's a holographic or holograph like
effect that um
allows both either with sound or with
light to
[Music]
image objects that can't be seen visibly
but
you have to have a corner as long as
there's a corner evidently that
induces the kind of self-interference
that allows distant
uh perception but
you know more more relevant probably is
the way that con specifics
in flocks and so forth uh convey
information mediated information
sorry i don't have anything more
specific awesome
awesome points steve thanks for sharing
it um
it's time and that was an awesome
point one discussion really appreciate
having you on here
casper and everyone else who's joining
live so we kind of just close with
little
you know pause the video or pause time
whatever your affordances
think about these questions see you and
um
thanks for organizing yep oh for sure
and just fill out the feedback form in
the calendar
invite uh we'll see you next week so
just
keep thinking about the paper and other
topics we'll be back for a follow-up
discussion on the same paper
next week so bye everyone
bye
