---
title: "ActInf Livestream #024.0 ~ "An empirical evaluation of active inference in multi-armed bandits""
category: "Livestream"
series: "Livestream_024"
episode: "0"
duration: "1:28:51"
url: "https://www.youtube.com/watch?v=Fx7xWUU1MlI"
views: 161
exported_at: "2026-02-18T22:37:37.739269+00:00"
format: markdown
---

# ActInf Livestream #024.0 ~ "An empirical evaluation of active inference in multi-armed bandits"

hello
everyone welcome to actin flab live
stream number 24.0
today is june 16th 2021
and we're going to be talking about this
paper in empirical evaluation
of active inference in multi-armed
bandits
i'm daniel and i'm here with blue hi
awesome welcome to the active inference
lab everyone
we are a participatory online lab that
is communicating
learning and practicing applied active
inference you can find us
at the links here on this page this is
recorded in an
archived live stream so please provide
us with feedback so that we can improve
our work all backgrounds and
perspectives are welcome here
and we'll be following good video
etiquette for live streams
here at the short link you'll find all
of the live streams
and different series that we do in the
communications unit of actin flab
and today we're going to be
contextualizing in the dot zero video
for two upcoming discussions in the
second half
of june 2021 on the 22nd
and the 29th when we have discussion
24.1
and 24.2 on this paper and hopefully
with the authors joining
today in actin livestream number 24.0
we're going to be trying to set some
context and give an introduction
to the following paper an empirical
evaluation of active inference in
multi-armed
bandits by the authors listed here
and the video is just an introduction to
some of the ideas
it's not a review or a final word it's
kind of like a three-way
intersection we have people who are
maybe within the active inference
community and looking to be
exposed to some different areas like
bayesian statistics or machine learning
the second road is those who are coming
from bayesian statistics or machine
learning approaches
and curious about active inference and
then of course we hope that this will be
exciting and interesting
even if you're unfamiliar with active
inference or machine learning
we'll hopefully try to connect it to
some broader questions
in behavior and decision making more
broadly
we're going to walk through the aims and
claims of the paper the abstract in the
roadmap
covering a few big questions and then
we're going to go through all the
figures
and some of the key formalisms of the
paper so that whether you read the paper
or not
you'll hopefully be in a good spot to
ask questions and learn more
and of course in the dot one and dot two
in the coming weeks we'll be discussing
this same paper
so save and submit your questions and
let us know if you'd like to
participate or contribute in any way
here we are on the paper itself which
has a screenshot of the cover on this
slide i'll uh read the aims and claims
and then blue you can
give a first thought on what you thought
were kind of cool pieces about
what they aimed for or claimed in this
paper
we provided an empirical comparison
between active inference
a bayesian information theoretic
framework and two state-of-the-art
machine learning algorithms
bayesian upper confidence bound ucb and
optimistic thompson sampling in
stationary and non-stationary
stochastic multi-armed bandits we
introduced an approximate active
inference algorithm
for which our checks on the stationary
bandit problem
showed that its performance closely
follows that of the exact
version and hence we derived an
active inference algorithm that is
efficient and easily scalable
to high dimensional problems so what was
cool about that or what made you excited
to
make this dot zero this paper was really
awesome
it um it shows how active inference can
be used
to solve problems that are sometimes
computationally
intractable and really pretty difficult
so i think that the authors did a great
job of
deriving this active inference algorithm
and proving that it's
useful agreed and they did an awesome
job bringing it analytically like with
equations
in line or at least being juxtaposed to
other approaches in machine learning
rather than appealing to a qualitative
body of theory
which is also great this is definitely
one where the
claims are specific and exact and that's
what we'll be
following up on
so the abstract i'll read the first half
and then you can go for the second half
a key feature of sequential decision
making under uncertainty
is a need to balance between exploiting
choosing the best action according to
the current knowledge and exploring
obtaining information about values of
other actions
the multi-armed bandit problem a
classical task that captures this
trade-off
served as a vehicle in machine learning
for developing bandit algorithms that
proved to be useful in numerous
industrial applications the active
inference framework
in approach to sequential decision
making recently developed in
neuroscience for understanding
human and animal behavior is
distinguished by its sophisticated
strategy
for resolving the exploration
exploitation trade-off
this makes active inference an exciting
alternative to already established
bandit algorithms so it's kind of
awesome
first few words it's about sequential
decision making
under uncertainty and the bandit task
was
made to explore that machine learning
has already
gotten so much value out of pursuing
algorithms for approaching
this multi-arm bandit problem and then
enter
active inference which was developed to
uh initially
cover human and animal cases of behavior
but as we're seeing it also it goes
beyond
that and so that motivates studying
active inference
in the context of multi-arm bandit
problems so go for the second
part here we derive an efficient and
scalable approximate active inference
algorithm
and compare it to two state-of-the-art
banded algorithms
bayesian upper confidence bound and
optimistic thompson sampling
this comparison is done on two types of
bandit problems
a stationary and a dynamic switching
bandit our empirical evaluation
shows that the active inference
algorithm does not produce efficient
long-term behavior
in stationary bandits however in the
more challenging switching bandit
algorithm
or switching bandit active inference
performs substantially better
than the two state-of-the-art banded
algorithms
the results open exciting venues for
further research in theoretical and
applied machine learning
as well as lend additional credibility
to active inference as a general
framework for studying
human and animal behavior so this is
really nice because it's
it it takes like active inference as an
approximate way that
humans deduce reason balance this
exploration exploitation
paradigm and it programs that into the
framework
so it just shows that you know it's it's
getting closer approximating human
thinking
in a machine it more and more i think
yes and there's sort of a pair of pairs
that we're going to return to
a bunch of times in this discussion the
first is the two types of problems
the stationary and the dynamic bandit
which
one of them is static one of them is
changing we're going to talk more about
that
and the other pair that it comes up
often is the bayesian upper confidence
bound and optimistic thompson sampling
we're also going to come back to that so
they're kind of doing a pair of pairs
approach and then the results are just
really fascinating and we're going to
unpack that
that actually in the simpler case we see
that the active inference algorithm
doesn't do perfectly but in this more
challenging dynamic
case it does better than state of the
art so what do you call something that
goes beyond state of the art
here's the roadmap for the paper and of
course
as with these.0 videos if you're curious
about
how it was specifically stated in the
paper or you want to dive in
for more and you want to see how they
cited or how they built up a claim you
should go to the paper itself
this is just the road map for it they
start with an introduction
of the multi-armed bandit and cover the
two kinds of bandits that they explore
which is the stationary and switching
versions and talk about how you evaluate
performance
in different versions they then
introduce the algorithms that they're
going to
utilize and talk about this variational
smile approach which we'll cover just a
little bit of but
look forward to hearing from the authors
about what it does
then there's results for the pair of
problems that they explore stationary
and switching bandits
and then have five figures which we'll
go through showing some results and
hopefully
even if the algorithms or the formalisms
were a little bit hard to follow the
figures are really clear
and they show how the algorithms perform
through time and close with a discussion
that hits on some awesome general points
for the active inference and machine
learning communities
here are the keywords that were provided
with the paper so as usual we're going
to
use these keywords as jumping off but
also
jumping in points for those who might be
familiar with sequential decision making
aka life but not be familiar with
bayesian statistics and we're going to
start from sequential decision making
and then
go on to talk more broadly about
bayesian inference
multi-armed bandits so it's totally fine
if you've never even heard of the bandit
problem
then we're going to talk about those two
different algorithms that they're going
to be exploring
upper confidence bound and thompson
sampling and then
see how they talked about active
inference which is going to be a really
distinct way
relative than a lot of approaches we've
seen previously
so let's go to sequential decision
making
blue what would you say about this so
sequential decision making is dependent
on
time t right so one time step you have a
state of the system
you perform an action and that alters
the system
right so that at the second time step
the system is now in a new state and
then you have another decision to make
about what you're going to do
with the system so this is like driving
a vehicle
managing a stock portfolio playing a
game of chess sequential policy
decisions
and so like to kind of juxtapose what is
a not sequential
problem so that be something like image
classification is not sequential like
you can just classify all the images
parallel or at once
at the state of the system doesn't
depend on how you classified the
previous image
awesome so definitely all kinds of
organismal behavior in decision making
that happens in time so think decisions
you're thinking
usually sequential decision making
especially when the decision
influences the future those are all the
kinds of problems
that we're going to be talking about but
also to even make it broader than that
some non-sequential problems can be
framed sequentially
so let's just say that we had that
classification problem where it's one
blob one big data set and so there's no
temporal sequence
we might want an algorithm that treats
it as if it were sequential
so that we could just start reading in
examples and then after 10
okay got it so then by looking at it as
if it were a sequential problem
and we were solving things through time
sometimes we can approach non-sequential
problems that way because in the
computer it is going to be sequential on
the processor
so it's for things that actually are
sequential in the world
or they're for things that we want to
act as if they're sequential
one big tension that comes up with all
kinds of modeling
is the explore exploit dilemma slash
trade-off and this is an awesome 2015
paper of
hills at all exploration versus
exploitation
in space mind and society
so it's pretty cool because it talks
about multiple different domains
here in the table 1 there's animal
forging
visual search information search memory
search
searching and problem solving and social
group learning those are like
all of our favorite topics blue and it
gives just a little bit of a visual
example how
in different domains what does the
archetype of exploration
look like and what does the archetype of
exploitation
look like so some of these are
very uh related to kind of a physical
movement
like patch forging exploration moving to
a different tree
exploitation staying on the same tree
but also visual focus
exploration scanning around exploring
exploitation having a fixed gaze and
staring at
something and then also we can think
about
even in word association like memory
exploration
is doing big jumps from different
semantic neighborhoods
whereas exploitation might be like all
the livestock animals or animals with
the same letter there's different
ways that you might exploit because
there's different dimensions to the
semantic landscape
but there's still this trade-off between
jumping far
or staying relatively close in the
neighborhood
so it's a big trade-off it's studied in
animal behavior
it's studied in all kinds of
decision-making tasks
anything to add on that only that i
got to interact a lot with peter todd
last summer who's the second author on
this paper and
it was so fun cool and also
ian cuisine has done awesome collective
behavior work
so it's exciting to think about how
these algorithms
are able to apply to individual agents
but also maybe
groups and that's hinted at multiple
times here like role assignment and
social connectivity
as we heard about in the abstract of the
paper that we're discussing today
they went right from sequential decision
making under uncertainty
to multi-armed bandit is
a way that we can study that and from
the paper
this is where we're introducing that
that uh double problem the two problems
are solving
we consider two types of bandit problems
in our empirical evaluation
a stationary bandit as a classical
machine learning problem and a switching
bandit
commonly used in neuroscience so we're
gonna go into more detail about
how those are technically defined but
let's just start with what are people
getting at with multi-arm bandit
why is it something that so many people
have addressed
this will make the presented results
that they're doing here
directly relevant not only for the
machine learning community
but also for learning and decision
making studies in neuroscience which are
often utilizing
the active inference framework for a
wide range of research questions
so there's all these different areas
here's a multi-arm bandit deciding which
area to study
computer science machine learning
economics
neuroscience these are all areas
that the multi-armed bandit is like a
bridge amongst
so now we're sitting active inference
right at that nexus
we've talked a lot about connecting
computer science to behavior
or connecting neuroscience to economics
what if we could all
meet at a common nexus what if that were
active inference
these are the kind of fun things to talk
about
but it's not just a nexus of conceptual
connection the multi-iron bandit and
active inference
there's a lot of really specific use
cases and a lot of the algorithms that
power our experience online are actually
trained
and fit with multi-arm bandit problems
so here's a few fun examples that we
came across
while researching here on the top left
is showing how you have a
multi-arm bandit playing a role in music
recommendations
so it's like the the arm that's which
arm is being chosen
that's the song so it's thinking about
it from the point of view of the music
platform
it's sending a song and then the target
user
which is the bandit machine here gives a
payoff back to the algorithm
thumbs up or thumbs down and then the
algorithm sends you another song
and then a payoff is given so it's
sequential decision making
and it's that same relationship that's
shown
graphically the goal is to maximize the
sum of the ratings versus maximizing the
sum of the payoffs in an abstract
problem
here's an example of website a b testing
testing versions of a website
so in the top there's four versions of
the website
and then they're each being allocated to
a quarter of the users
and then each of the users are staying
on the site for a certain amount of time
or staying for different amount of times
in the standard a b testing for the
whole duration of your test
you keep that one-fourth for each site
but in the multi-armed bandit you start
with a quarter
but then very rapidly we see that this
blue one starts performing better
and then we keep exploring and having
some time allocated to these other
colors but we see that the blue pretty
steadily
dominates and then that black line ends
up staying
higher so overall a higher number at the
end of the epoch so you're sort of
earning while learning because you're
able to
be making exploration while you're also
exploiting
and there's papers specifically on that
like bayesian bandits
in the context of online personalized
recommendations
any thoughts on that blue
cool so these are yeah these are
algorithms that are in use
every single day and they power a lot of
our experience
and a lot of decision making support
here's where we bring in some of the
bayesian algorithms
they're going to be using these two
types of bandit problems stationary and
switching
and here's the second pair of terms
they're going to be empirically
comparing active inference
to two other state-of-the-art banded
algorithms from machine learning
so those who are familiar with machine
learning will have seen these two
algorithms a lot
the first is an upper confidence bound
algorithm
ucb and the second is a variant of
thomson sampling called
optimistic thompson sampling and then
they note here
the two algorithms the ucb and thomson
sampling
reach state-of-the-art performance on
various stationary bandit problems
achieving regret which is the difference
between actual and optimal performance
will return to it soon
that's close to the best possible
logarithmic regret
and in switching bandits learning is
more complex but once this is accounted
for
both of the algorithms exhibit
state-of-the-art performance
so you can never play perfectly but
you're approximating about as good as
you could play
with these algorithms what does that
look like before we go
into the technical details of what these
algorithms are
so on the top left we're going to be
thinking about again whether it's
deciding which version of a website
we want to be presenting or which songs
we want to be presenting
or just keeping it kind of abstract on
the top left we start
with zero trials so this is before we
have any information at
all and then as trials
occur and payoffs are observed and the
trials
count count after 28 trials
we've reached a very markedly different
set of distributions
and so what this overall looks like is
you show up at the casino and you don't
know the payoff of
any of the slot machines and then you're
going to be
choosing some policy some way of
approaching
those slot machines and switching
between them as needed
some approach that's going to hopefully
result with you
getting the most money and so in this
case it's sort of like as you
get more and more information you're
fine-tuning your estimate
of what the distributions look like like
we can see how the red distribution gets
tuned as it gets tried more and more
and similarly for the other
distributions so that's kind of
what this algorithm does is it starts
with
no specific bias towards a given slot
machine
and then it tries to develop a strategy
for staying with slot machines that are
known about versus trying new ones or
ones you haven't tried in a while
in order to get the best possible
outcome and as you can imagine
if there's a static one then it's an
easier problem
if it's dynamic you have to keep the
rate of change in mind
any thoughts on that good good
explanation
okay so bernoulli bandits are
the uh class of bandits that they're
going to constrain themselves to
so they say we're constraining ourselves
to a well-studied version of bandits
the so-called bernoulli bandits for
bernoulli bandits
choice outcomes are drawn from an
arm-specific bernoulli distribution
bernoulli bandits together with gaussian
bandits are the most commonly studied
variant of multiarm bandit both in
theoretical and applied machine learning
and experimental cognitive science so
you can fit any kind of distribution
for the rewards underlying each of these
slot machines
but it turns out that if you use the
bernoulli distribution
the math works out nicely which makes it
easy to study that's why there's been a
lot of study in the bernoulli and the
gaussian
so a gaussian distribution reward would
be like okay
you get five with a certain you know
bell curve
of how much you might win bernoulli is
going to be a different shaped
distribution
but just the idea is that you're going
to be learning the parameters
that describe the reward returned by
that arm
so it's just the sub category or the
function that underlies the reward
payoff
on these machines
let's talk about the two algorithms that
they're going to be discussing a lot
and then also where these algorithms
come into play in terms of strategy
so again you're sitting there at the
slot machine at the casino
and how are you going to decide
how to stay or leave a given machine
stay in the casino though that's that's
where you want to be
this is from a nice blog post from 2019
data scientists have developed several
solutions to tackle this problem
and the three most common algorithms are
epsilon greedy
then upper confidence bound and thompson
sampling so epsilon greedy is
not given in this paper because it's not
the best performing algorithm but it's
really
a nice sort of starter algorithm it's
the simplest algorithm to address the
exploration exploitation trade-off
basically during exploration or
exploitation sorry
the lever with the highest known payout
is always pulled so
whatever the running best estimate of
the top performing slot machine is
defaults there however from time to time
some random fraction epsilon with some
fraction
five percent of the time or one percent
of the time select
another random arm to explore the other
arms
with an unknown payoff so you're
sticking with the one that has the
highest point estimate
and then just some fraction of the time
you flip to a different one just to
check
and then you update your estimate of how
each of them are doing
so that's one strategy now here's two
strategies that
do better than that those are the ones
that we're going to be contrasting with
active inference
one of them is the upper confidence
bound which is sometimes referred to as
optimism in the face of uncertainty that
sounds like active inference
it assumes that the unknown mean payoffs
of each arm will be as high as possible
based upon historical data so we don't
know the payoff
of each arm but we want to assume given
what we've already gotten from the data
which is as far as we can speculate we
want to assume that it's as good as it
could have been
which is why we see the upper confidence
bound on the top of this distribution
and then thompson sampling is
fundamentally a bayesian optimization
technique
with a core principle known as
probability matching that can be summed
up as
play an arm according to its probability
of being
the best arm so in contrast with epsilon
which says just go with the one that you
think is best
and then ten percent of the time do
something else
thompson sampling is like you kind of
have a pie chart with a relative
performance
of different arms and then you pick them
based upon
how big of a pie it is so you do rarely
choose ones that don't have high payoffs
just to sort of check in on them
but then if you check back on one and it
got does really well then that slice of
the pie starts growing
and then the whole point of training
these algorithms is how fast should you
be
re-weighting in the dynamic case etc so
just
laying it out like that is not the
solution but this is getting at a few
ways
whether optimism in the face of
uncertainty or this sort of conservative
probability matching
these are two ways that as we've seen
are state-of-the-art because they
basically perform as well as possible
and so we're locking it down with upper
confidence and a lower confidence bound
it's a pretty nice choice of algorithms
they're brought up as an instructional
pair all over the machine learning
educational space so nice choice by the
authors to juxtapose it so
clearly to active inference
so is thompson sampling then pessimism
in the face of uncertainty
nice things couldn't be better than they
have been in the past
let's go a little bit more into detail
into the two
different uh algorithms and then talk
about regret
so here's from another blog post lillian
wang's blog
talking about bandit strategies so
again it's about explore and exploit
even though
active inference is going to help us
reconceptualize
of explore exploit which we can maybe
get to at the end
but we don't want to be exploring
inefficiently because
we're kind of spending our time playing
on losing machines
while we know that there's a better way
to play so to avoid such inefficient
exploration
one approach is to do epsilon sampling
and then in the case of a static set of
payoffs
you decrease that parameter epsilon in
time so again how fast should you
decrease it
still have to fit parameters but that's
just one approach
the other approach to sort of prevent of
this inefficient exploration so avoid
pain
is to be optimistic about values that
are
optimistic about options with high
uncertainty and thus
prefer actions implicitly for which we
haven't yet had a confidence value
estimate that's why this is optimism in
the face of uncertainty
in other words we favor exploration of
actions with a strong potential to have
optimal value so that's exactly what the
ucb
upper confidence bound algorithm does is
it measures it with an upper confidence
bound so that the true value is always
below
that bound and then we are trying to
push up the upper bound knowing that
somewhere below it
hopefully not too far is the true value
and then the ucv algorithm does
optimization with this arg max
selecting the greediest action to
maximize that upper confidence bound
so as it's laid out in the blog
basically you can do
no exploration that's just sort of
pick the first one you sit down at stay
there you can explore at random
that's epsilon greedy or you can explore
smartly
with a preference for uncertainty so
we're just kind of building on that
epsilon
idea of sticking with the one that
usually we like
but then spending sometimes elsewhere
how much time spending elsewhere and
which ones should we choose well don't
just go to any old machine if you're
going to select somewhere else where
let's choose ones that still have a good
probability of having a high expected
payoff
so that's ucb any comments on that
no so in contrast we have thompson
sampling
from a nice slide deck from agrowall
columbia and thompson sampling goes back
to 1933
so like many other algorithms the
classical variants
are pre-computational sometimes they're
even just thought experiments
and in the slides it's talked about how
thompson sampling it's a
natural and efficient heuristic that
maintains belief
about the effectiveness which is the
main reward of each arm
we're going to be kind of tracking how
well we think each arm is doing through
time
and basically the way it works is we're
going to observe feedback
then update our beliefs about different
arms in a bayesian manner
and then pull arms with a posterior
probability of being the best arm
so not the same as choosing the arm
that's most likely to be best
this is like again a pie chart that is
the proportions
of how well they're performing and then
we choose based upon that proportion
and the pseudo code looks like this
we start we initialize the model
with a prior as well as the family of
distributions that our rewards are
expected to be drawn from so this is a
gaussian
case but this is where you could see a
bernoulli bandit come into play
and then the algorithm is as follows
first there's a sampling of a
mean with an estimate from the posterior
for a given arm i then the
arms are played according to the
probability
of them being the best arm
the reward is observed and then
everything is updated so it's like
sample
from your posterior from your prediction
then
act then observe and update it's sort of
like that closing time
song you know every every every
beginning comes from some other
beginnings end
and it's called a posterior in bayesian
statistics you know
prior gets updated the posterior but
then that posterior
is the prior for the next round so it's
not like it's just a one
round learning the posterior feeds back
into the model which is why we just talk
about continual bayesian updating
so it's kind of like ooda like
observe orient decide act these kinds of
action loops which
of course include active inference is
what
makes these models really similar or at
least in the same neighborhood
and then this paper that we're
discussing brings them into alignment
analytically with the equations and
through simulation and juxtaposition
that's what thompson sampling is though
any comments on thompson
just how well it plays into the
sequential decision making process that
we were talking about earlier right so
it's you have a next time step and you
update and you update and you update
yeah so again like even for those
non-sequential tasks like the image
classification you brought up
you could sample from your big database
then update your model and then once
you're sampling and you're like i'm not
really updating my model that much
you might not need to look through the
entire data set
and so by framing that non-sequential
problem sequentially
you get big computational speed up
and then of course for sequential
decision making then you need an
approach like this
how about regret learning regrets i've
had a few
haven't we all right um so i think you
put this in here the introduction to
regret and reinforcement learning which
is
um a medium post correct
uh so if you wanted to learn more about
regret you can check it out there but
regret is
um just the the difference between the
optimal performance how good you could
do
and the actual performance and so you
see in this little image here
um you can see that the best policy is
the red dotted line and then the choices
that the agent makes
this is like the logarithmic performance
logarithmic regret and so
they're they're converging the idea is
to converge with the best
possible policy based on your previous
decisions right
exploring exploiting um and then the
authors here use
regret when they're looking at the
stationary bandits
they use regret as a measure of
performance but then they use regret
rate when they're looking at the
switching bandits and so regret rate is
just
the regret over time and they use the
rate they said it was
had been illustrated to be a better
estimator of this
logarithmic regret in the dynamic case
awesome and the big idea of regret
is looking back over your history
so either for all of history that's
cumulative regret which applies really
well to the stationary problem
or recent history which applies well to
the dynamical case
because if things are always changing
you're kind of more interested in how
well
you're doing recently rather than
over all time you don't want some
fluctuations early on to be
playing a role in your cumulative value
because you don't want to fit your
strategy now
to reducing regret from a different
epoch which can happen if you don't do
it this way
so looking back over history again
whether all of history
cumulative regret for the fixed case or
recent history for the dynamic case
update your strategy so that you would
have minimized regret to xero
by playing that strategy all along so
you know
looking back at the bitcoin price what
strategy
would have been no regrets
those are the big questions or just in
the last little window of time
given what i recently have found out how
could i make my rate of regret
gain as low as possible so
it's a way to look back and then
optimistically
think about how you could have performed
by reducing regret to zero and we see
this
all the time in computer science like
maximizing something
you do it by minimizing whether there's
a negative thrown in there
or whether there's a natural log thrown
in there or whether it's
one over something or it's just framed
in an opposite way
a lot of times if you know that you're
bounded at zero something can't go below
zero
then you want to go as low as possible
or
if you want to maximize something it's
sometimes easier to do one over the
maximum and then try to get that number
to zero
rather than this unbounded maximization
like okay i'm at 5 million should i stop
you don't know maybe that's nowhere even
close because there's no highest number
so that's regret learning and that's how
they're going to be calculating their
performance
let's get to active inference so one
thing
that you'll see on this slide right away
is we're not seeing
a sensory motor loop we're not seeing an
agent in an environment with arrows and
nodes
we're coming at active inference from
this point of view of sequential
decision making
under uncertainty and so in this section
which is a great title
three two one active inference
they write that the exploration
exploitation trade-off can be formulated
as an uncertainty reduction
problem where choices aim to resolve
expected and unexpected
uncertainty about hidden properties of
the environment so already we're seeing
that active inference formulization
there's hidden states in the environment
which we don't directly have access to
but we get admitted outcomes from
decisions
this leads to casting choice behavior
and planning
aka planning as inference as a
probabilistic inference problem
as expressed by active inference so
action
and inference our inference is about
what actions we're planning and about
the hidden states of the world given the
outcomes that we're receiving
sensory data using this approach
different types of exploitative and
exploratory
behavior naturally emerge in active
inference decision strategies
behavioral policies are chosen based on
a single optimization
principle or yesterday i think it was a
what was it a functional
a common functional footing or something
like that the single optimization
principle
is minimizing expected surprisal about
observed and future outcomes
that is the expected free energy so it's
kind of cool like
the backwards looking approach
is to minimize regret like how
would i have performed best in
given what i know about the past how
does that
change the way i act now and then free
energy minimization expected free energy
in the current and the future moments is
like
given the state of my model for now
and moving forward how can i minimize
expected free energy
because regret is not anticipatory
regret is only looking back at it
which is why it's really easy for
training and then here's something
that's looking forward
so it's kind of cool how like the
current moment is this handoff
between the retrospective regret
learning
and then the prospective free energy
minimization
that's how they frame active inference
here any general comments or what do you
think was kind of cool about that
so i just i'm thinking back to like alex
chance's paper that we did way back i
think that was number eight but
um i i still always go back to that when
i'm looking at these computational
frameworks because he broke it up very
nicely
into like the reward the pragmatic value
which could be like in this case
the minimization of regret can be seen
as like the pragmatic value or the
reward
and then the epistemic value right so
you have both of these things that play
into
um giving the system how helping this
the agent update
relevant to the system cool and i'll
look forward to
hearing from the authors were they
studying active inference and then
approached bayesian decision making
appro
uh algorithms were they coming from a
non-active inference computer science
background and then
found active inference as something that
was exciting how did they
converge upon this approach
shortly after introducing active
inference they turned to
an approximate active inference and they
described that as saying
active inference in its initial form was
developed for small state spaces and toy
problems
without consideration for applications
to typical machine learning
problems so that's like when there's two
decisions in sort of a two by two matrix
and two outcomes in the world
and two decisions you can make this has
recently changed
and various scalable solutions have been
proposed i think one of these citations
would be that
chance at all uh scaling active
inference active stream eight
in addition to complex sequential policy
optimization
that involves sophisticated deep tree
searches so that's sophisticated active
inference with these tree rollouts
followed by tree pruning approaches
therefore to make the active inference
approach practical
and scalable to the high dimensional
bandit problems typically used in
machine learning
we introduce here an approximate active
inference algorithm
definitely will be cool to hear from the
authors like what
exactly are we approximating what else
could be approximated
and still have it active inference or
what can't be approximated
but let's look at how and why they
approximated active inference
so this is so kind of yeah so to kind of
speak to the why you and i have both
done
um you know tree construction in in
terms of phylogenetics right in the tree
switching and the switching of nodes
and that can get really computationally
overwhelming
like can run for days and days and days
so um it's it's really
nice to see such a sweet clean
implementation of approximation here
yes here
we're not going to go into depth into
formalism 16 and 17 but we'll look
forward to the authors describing it
but here is the key piece the exact
marginal posterior beliefs over reward
probabilities
theta can be expressed this way okay
just looking at that you go okay it's
gnarly how
are we going to win if that's what we
have to solve
so the exact beliefs over uh
the exact correct beliefs over reward
would look this way
and then they write the exact marginal
posterior in equation 17
will not belong to the beta distribution
making the exact inference analytically
intractable
so there might be a way to numerically
approach it and simulate it or calculate
it but
if we want to be looking through big
data sets and doing it fast
without massive amounts of computational
effort we need a different way
however constrain if we constrain the
joint posterior to this approximate
fully factorized form
and we've seen factorization of
variables before factorization of
variables is kind of a
big topic uh so we're not going to
totally
go into detail here again it'd be
awesome to hear from the authors how did
they derive and factorize
but one way to think about it is that
constraining a big open-ended long
equation
into a factorizable form reduces the
solution space
a lot and that enables certain kinds of
optimization to become tractable so for
example
for linear regression we have least
squares
which is a way where if you constrain
the problem to saying i'm trying to
solve the sum of squares
not the sum of cubes or the sum of some
other function but i'm just trying to
solve this one
then there's computations that scale
really well
and so that is what is happening a
factorization and another way to think
about factorization
is if you have a bayesian graph where
the nodes are the variables
and then the edges are like the
relationships between the variables
you could just dump it all into a
parameter fitting framework
with all the edges possible that would
be like an unfactorized model
so the number of edges that you have to
figure out the
exact values for is going to be a lot
and it's going to increase exponentially
with the amount of parameters you want
to fit
but if you factorize things you go okay
variable a
only is associated with b and b is only
associated with c
and a all of a sudden you're reducing
the amount of edges that you have to fit
which helps you get to hopefully
a solution that is attractively reached
but also
approximately accurate so that's like
probably probably approximately correct
and approximate bayesian computation but
we've seen that factorization a few
times
won't go into too much more detail here
but what they do is they take this
factorized form
and they use variational calculus to
recover the following
variational smile rule which we'll go to
in a second
and so they get to a different set of
formalisms we'll hear from the authors
about
what's different about those formalisms
and
then what's kind of cool is that for the
stationary bandit
where you can change the parameters to
like zero for the rate of change
it corresponds to the exact beijing
inference over stationary bernoulli
bandit problem
so that was just kind of interesting how
the exact
form of an algorithm solution might
uh how active inference might be doing
something
exact in the asymptote
what is smile here's the smile paper
variational methods as a prize to
surprise minimization learning
so that sounds like a lot of things that
we do with variational methods
variational base
and surprise minimization and the pseudo
code
is presented here for the exponential
family
this is just a question for the authors
what is the smile
doing how does it help us approximate
active inference
what else can we use the smile for
so that's this approximating active
inference interlude
they take a big messy form
and then by constraining how variables
can be related to each other
and using variational methods on that
factorized representation
it's possible to get an approximation
that is going to be effective
so it's interesting that um you know
there's this direct
correspondence for the stationary uh
bandit case
because the in the stationary case like
we didn't see
improvement right using the active
inference algorithm that totally
explains why right
yep and they have a few more pieces on
that i think in uh
bigger figure four or something like
that
okay let's go to the two
problems that they tackle and then the
results for those two sections
so we'll cover first the stationary
bandit and then the dynamic bandit
so here's the definition and where they
work through
the stationary bandit so a stationary
bandit has a finite number of arms
uh it has uh k arms
and then it's going to be playing
through
t time steps and then it's big k
big k arms and then each little little k
k is the set of little arms little k
yeah k is the action
so here's how they define the stationary
bandit and
again you can think about t and time
actions
and uh arms and then in stationary
bandits the reward probabilities
theta sub k are fixed for all trials so
theta is just like
it's funny it's like the parameter that
means just like variable
sometimes i guess a lot of them do but
data especially
so just a fixed reward value
the fixed yeah reward probability so
that's why it's not stationary
in the casino this would be like one of
them pays out
um on average one to one one of them is
pays out fifty percent one pays out two
hundred percent but they never change
so here's a sort of visual
representation of that with
here's the multi-armed and then the
mouse is getting the cheese
and each arm has a different fixed
probability
but those don't change so the
probability of cheese
does not move
here's figure one so in figure one
we're going to see regret rate analysis
so the regret rate you can imagine uh
is we'll get to the second but the
regret rate analysis for the stationary
bandit
and then we're going to be comparing
approximate active inference in red
to the exact active inference in blue
so that will be cool to talk to the
authors about
what was the relative change in how much
time it took to compute
we'll find out and what they do is
they are showing that
the blue and the red are always kind of
tracking together
so that suggests that the approximate
form does
a really good job because it follows the
behavior
of the exact form pretty well
and then just to sort of how to read
this
uh graph so there's four columns
corresponding to k equals 10 20 40 and
80 arms
so that's changing just the number of
arms
then there's the rows which are
for uh epsilon
being the the so this is like the
differential between the arms
so kind of how easy the um task
is i believe and then that's
point one point two five and point four
and then
within each cell
there's lambda uh which is
a function of precision over prior
preferences
and then r sub t
which is the regret as a function of
trials
and the dash black line denotes the
upper bound on the regret rate
corresponding to the random
agent so this is
i guess as bad as you could get
and then we see that active inference is
performing
better like there's it converges upon a
lower
rate of regret than
0.1 or around 0.1 which is the amount of
regret that's accumulating
for the randomly behaving agent
so so just to footnote that um
which i thought was interesting and made
this more meaningful for me that lambda
parameter the precision
so it says when the active inference
agent has very imprecise
preferences so lambda closer to zero
it engages in exploration for longer and
reduces the uncertainty
that way at the expense of accumulating
reward so just
um just to kind of footnote that in
there
interesting and that's definitely going
to come back when we talk about
active inference and how we rethink
explore exploit
so what is this showing it's showing
that
as you uh though they're
that as a function of precision you're
getting
different behavior in the active
inference agents
but the approximation is basically
always working pretty well
and then also the dotted lines are fewer
trials and the solid lines are more
trials
so we can see like in all these cases
the dotted line and then the dash and
then the solid
you're always doing better with more
trials that's what we
kind of see like if you only have 100
trials so just a few trials on 80 arms
your regret is almost as if you're
playing randomly because you've barely
tried every arm once so you're kind of
not able to do so well but
if you're in the right area of precision
not too much precision
but still um in this area down here and
you have
10 000 trials even with 80 arms
the regret rate can drop to very very
low so playing like
almost optimally even on 80 arms
given the trials and given a significant
enough difference between the
outcomes so that's what figure one shows
which is that
active inference can learn to reduce its
regret given the right parameters
the things that we'd expect to make the
situation harder like more arms
or less differentiability amongst the
arms or
super high um or low precision vari uh
rates those are the things that
influence active inference algorithms
um and also they said that they found
the minimal regret rate
um at around lambda is 0.1
so that's why they fixed the the regret
rate for the upcoming trials or for the
upcoming tests because there's there's a
bunch of
knobs to tweak and so they do
their best to do parameter sweeps and
show like here's for
you know the whole distribution of
lambda
for three different sampling regimes for
four different arm styles for three
different difficulties like already
the combinatorics get really high and if
you were going to be using this in an
industrial situation
you would optimize it with all these
parameters in play
and then um they write that they're only
going to consider
this approximate active inference
variant for the between agent comparison
because it was doing pretty well in
figure one so they're just gonna
follow up with the approximate but it's
something we can ask them like
what is the difference in computation
time for the general
or exact all right figure two so we're
still
thinking about the stationary bernoulli
bandit
here is going to be a slightly different
plot
it's a comparison of the cumulative
regret trajectories for the approximate
active inference that's aai
optimistic tops and sampling that's ots
purple
and bayesian upper confidence bound in
the teal
so those are the three lines and that's
the legend on the top left
and as blue just said the prior
precision is fixed to point one
which is what they found from figure one
like this sort of dip
that they all have at near point one
that seems to be a good
precision variable setting so they're
just going to roll with that instead of
also sweeping across positions
and here we see a similar columns and
rows
where k different number of arms in the
columns
and then different problem difficulties
in
the rows
and then the cumulative regret
so you want lower regret that
makes sense that's the whole thing that
we're training on um
what do we see there's a lot that can be
seen because there's so many
combinatorics of viewing at it but what
do we
see right off the bat well as the number
of samples
increases beyond say a hundred in
almost all cases the red line
approximate active inference
is below the other ones
so you're getting less regret with
active inference
on the stationary bandit for many
parameter combinations
okay but there's a few interesting
pieces
so one of them is that sometimes active
inference
early on has a higher regret so maybe
it's like a little bit more exploratory
in the beginning that's one thing to see
in that bottom left corner
there's a few other ones where it's sort
of like this elbow
early on but then there's this very
interesting behavior that actually shows
a lot
on the very top left so it's not always
the case that you can just
set your model to some parameter
combination and draw a really
generalized conclusion
but this is an awesome point by the
authors
so they're looking um
at an ensemble of agents so here it's a
thousand
agents like they're sort of running a
thousand uh
of each of these and then taking the
average which is why the lines are
smooth
and so what we see in the very top left
is that
the active inference asian's doing as
well as the other algorithms then it's
doing better right lower regret
under those lines but then the error
bound
increases that red shading and it starts
to head really far
up so that's pretty fascinating what's
happening and they write
this divergence is driven by a small
percentage of the agents in the ensemble
that did not find the accurate solution
and were over
confident in their estimate of the arm
with the highest reward probability
so that sort of pie chart of which arm
you should choose
it got off to a bad start and then their
precision was such that they just sort
of
rolled with that and they kept on seeing
the information they were getting within
that way of
setting up the problem and so they ended
up for a small
fraction of the agents kind of getting
derailed with continuing to regret the
decisions they were making
because they were locked in the
divergence is not
visible in the earlier setting easier
settings
with larger i'm not sure what variables
must see there
as one requires larger ensembles and
bigger number of trials to observe
sub-optimal instances
it may appear surprising that the
divergence is evident only for the
smallest number of arms considered
because that's supposed to be like the
easier
problem however the reason for this is
the smaller the number of arms is
the more chance an agent has to explore
each individual arm for a limited trial
number
so it's almost like it's easier to lock
in your beliefs
and maybe even false beliefs for a small
social group
rather than a party with k equals 80
people
it's like there's so much to learn that
you're less likely to get locked in
early but then at the smaller party
some of these active inference agents
are getting locked in
really early to what they think the most
rewarding arms are
and then they end up not sampling
efficaciously
so they end up implementing regrettable
policies so it's pretty
fascinating so i just want to footnote
here also
um so you're looking at this top left
where k
equals 10 and then this epsilon is 0.1
the top left is the most easy and then
the bottom right is the most difficult
where k
is the number of arms and then this
epsilon factor
is the difference between the arms like
so
it's the it's the outcome difference if
i go to an arm that has a reward versus
an arm that doesn't
yeah i think well point one is harder
because there's less of a distinction
between a better and a worse
um so it's the smaller number of arms is
easier but then point four is a bigger
contrast
so point one is harder than point four
okay
so then it's the bottom left that's the
the
that would be the easiest well depends
on what you mean easiest i mean all
things being equal
fewer arms is easier and then all things
being equal
the more contrast between good and bad
arms
the easier so got it so then the bottom
left would be
the easier yes the fewest arms and the
biggest contrast and
interestingly that's where we see the
biggest um elbow of active inference
like the biggest
um initial regret so it's like when the
game is easy and there's few arms active
inference stays
exploring a little bit longer but then
it ends up locking in on what's right
and then especially when there's not
that big of a difference between arms
all of them have this slight uptick and
then the variance
increasing with this shading that's
showing us that it's not like
all of the ensemble is behaving
differently but
perhaps again that a subset are getting
deranged
and then yes that's why i think the
bigger epsilon would be the
more difficult but we'll we'll just have
to save that one for the authors i would
think that the less contrast would be
easier so i guess that's
it's like not super clear so we'll just
have to ask
yeah so this is a cool
outcome and it's almost like it's a
qualified critique that makes a bigger
point about where active inference can
really succeed and where it might still
need challenges which we're going to
return to
so that's stationary bandit
let's go to the switching bandit the key
difference is that at each time step
any uh particular arm has a maximum
expected reward
and this reward probability is going to
change with a probability so there's
some probability
row um which is uh
is it p or is it row yeah uh with row
that is the probability of the reward
changing so now you can't just learn it
in any old order because things are
changing through time the probability of
the cheese is time dependent
section 2.2 oh yeah go ahead blue oh i
don't have anything no that's it so
you did it it's good so 2.2 is where
they
give the formalism for the switching
bandit and so
in contrast to the stationary bandit
problem outcomes are drawn from a time
dependent bernoulli probability
distribution
so that is provided and um
those who want to look into the details
can
do so but the key difference is that
there's some probability
that things change as you're playing the
game
so so i i did have a question here for
the authors
and uh looking forward to getting to ask
them so it's
the probability is the same and then it
just suddenly changes so like after
20 time steps or 50 time steps like it's
the same the same the same
and then it suddenly changes or it's the
it's changing at each time step i feel
like it's
because it says it it changes with some
probability but it's otherwise constant
so i'm curious as a constant like across
all of the arms is that the probability
that's constant or is it always changing
i don't know
good question
here we get to the between agent
comparisons of different algorithms in
the switching bernoulli bandit
with a fixed mean outcome difference so
epsilon equals 25.
so they're setting epsilon fixed so now
it's going to be a different row and
column situation
so in this figure the three columns are
row equals 0.01 02 and o4
so that's the probability of changing so
here on the left column
it's a dynamic environment with one
percent of time steps there's a change
here it's on the right side it's up to
four percent changing
so all things being equal the more
change the harder it's gonna be because
it's gonna be like
changing um faster and then the less
change it's more like the static
case and then the rows now are the arms
so k
10 20 and 40. so all things be equal
it's easier when there's fewer arms
because there's fewer decisions to make
and then we're going to be looking
within each cell
as the regret rate
this r sub t with a tilde regret rate
through time where again you want to
have less regret so lower is better
as a function of the samples so up to
several thousand
samples and then here are the algorithms
that are being compared
active inference in red bayesian upper
confidence in blue
optimistic thompson in purple and then
random control in the black dashed line
so the random play is um as is a good
it's um it's not the uh adversarial play
so it's not like you're you're choosing
to lose but this is the random play
and what we're seeing is that it
accumulates a static amount of regret
rate it kind of starts the same value
the purple and the teal algorithms
they also converge upon a regret rate
that's
lower than the random play so they're
playing better than random
but we see in essentially all cases
the active inference is lower than these
other
algorithms so when we say like oh active
inference has better performance
on this task than some other algorithm
this is kind of what it looks like this
is
saying that as time goes on octave
inference
is acquiring regret at a lower rate than
the other algorithms it's just
performing better it's implementing
better
policy then we can see that for the
less less changing and fewer arms
on the top left so that's like easier
we see that the the difference between
random play and the algorithm
is significant and active inference does
like
super well whereas when you have a very
dynamic environment
and more arms you don't get
that much of a regret you're still doing
relatively better and still active
inference outperforms the other
algorithms
but it's like imagine if it was changing
every few time steps and there's 100
arms
you would just you you would never be
able to sample
enough to make a meaningful update to
your model
so that's why the faster things change
and the more arms there are
the more the overall performance of any
machine learning algorithm is going to
converge to random play
whereas the more static the problem is
and then the fewer options there are
then better and better strategies
are going to perform better and better
relative to random
so this is just pretty cool that they
they do simulations they do
um i guess a thousand simulations
and then the switching schedule is
generated randomly for each agent
instance within the ensemble
so they do a full simulation a thousand
times for each of these cases and then
average it out
and yeah well done active inference
pretty cool to see that it is doing
better
on the switching bernoulli bandit for a
wide range
of situations and it sort of it rapidly
figures out
a good way to work and then it stays at
that low rate of regret accumulation
any thoughts on three super cool
yep now um in
four we're gonna fix the number of arms
so now we're at k equals 20 arms in the
switching bernoulli bandit
and then we're going to be comparing
these algorithms again so here
the columns are just as they were before
with less changing row equals 0.01 o2
and o4 on the right
but now as we kind of saw on previous
figures we have epsilon
which is that differential between the
rewarding and less rewarding arms
as the rows so we uh we can think about
the less changing
and the most contrast between rows
is where you see the most
um gain relative to
random play whereas when you're in the
more dynamic setting and when there's
less differences between which choice
you make in terms of the outcome
then there's less of a regret rate
differential with the algorithms
but again broadly across the board
active inference is performing better
than these other algorithms
so as sampling increases
active inference locks into a pretty
good spot by around
200 or 500 samples
and this is for the 20 arms so it's kind
of like
it's visited each arm probably a few
times
maybe some more than others but again
they're always changing
and so active inference is able to
cope with that and also it's interesting
that especially this teal
one it almost has a lower
regret rate and then it actually creeps
up
whereas at least just visually we're
seeing active inference kind of flatline
but not creep back up and so that's
something that can happen
with all kinds of algorithms that
they'll get locked into an aberrant
precision
regime and
um so there's just another way to slice
it in figure three
they fixed the epsilon the difference
between
the more and less rewarding arms and
then they explored how the number of
arms was associated with how dynamic of
a problem was being solved
in figure four we fixed arms
so that we could explore how rho the
dynamic
changing probability and epsilon the
differential
how those change performance
and then um
okay good
now um okay figure five
here it's uh yet another similar looking
figure
we're going to have similarly the row
for the column so less changing and left
column more changing on the right column
and we're going to have the number of
arms just like figure three with 10
20 and 40 but there's going to be a
non-stationary difficulty
and the difficulty of the problem is
non-stationary as the advantage of the
best arm over the second best arm
changes with time
ah yeah so epsilon is varied
yes exactly so switching changing
epsilon to time
and they fix the precision over
preferences to lambda
equals 0.5 so that's a different lambda
than they used
elsewhere and this is just sort of
showing
i mean the the variable values they
choose
clearly work because they're
outperforming the state of the art but
here they chose a different variable
yeah blue the lambda of 0.5 they used in
all
of the switching graphs oh yes figure 3
figure 4 and figure 5.
and they changed it to 0.5 in the
switching because they just optimized
for that but didn't show
that variable optimization okay thank
you
and so here we can see that
um yep active inference the red line is
on bottom
and it doesn't have this sort of
secondary
increase in regret rate so for even
dynamic on the right and many arms
on the bottom right we're seeing active
inference perform
well so figure three four and five
really make a super compelling case for
active inference outperforming
state-of-the-art algorithms nice
work and that's something that we're
really excited about
let's go to the discussion and just
spend a couple minutes
on the discussion and the closing notes
and then we'll
look forward to the dot one and dot two
they open the discussion by uh
rehearsing
what they have previously mentioned that
they're comparing active inference to
two state-of-the-art machine learning
algorithms the bayesian upper confidence
bound
and the optimistic thompson sampling
that's the pair of algorithms
in the pair of problems the stationary
and the non-stationary
stochastic multi-armed bandits their
contribution
among other things was the introduction
of the approximate active inference
algorithm
and then they perform some checks to
show that it's performing
again as well as you could do exactly
so they derived an active inference
algorithm that's efficient and easily
scalable to high dimensional problems
leading us to ask of course where could
it be cool
or useful or important to apply active
inference
and we know that there's many thoughts
on this
and hopefully will be many more but
we'll just note for those who are
listening at the right time that there's
been recently announced a net hack
challenge and we're going to be starting
work on this
in the end of july or the beginning of
august 2021
so if you're interested in applying
active inference to
a video game performance challenge we
hope that having a collaborative team
make an entry for this challenge
will be an awesome opportunity to really
demonstrate to the world what active
inference can do
but we'll also look forward to the
authors and all
guests sharing what kinds of questions
they think might be interesting to
explore using
approximate active inference type
algorithms like this
here's a really nice point that speaks
to
that um again in figure two
where we saw that sort of runaway regret
on a a small fraction of the agents
that were just getting locked into
extremely regrettable decisions
in that k equals 10 case
so what what do they say about that
to our surprise the empirical algorithm
comparison in the stationary bandit
problem figure 2
showed that the active inference
algorithm is not asymptotically
efficient
the cumulative regret increased faster
than logarithmic
in the limit of large trials so in other
words even though it's not
all agents that get deranged the ones
that do
are dragging down the group in a way
that's
damaging this cause for the behavior
seems to be the fixed prior precision
over preferences lambda
which acts as a balancing parameter
between exploration and exploitation
so this is a pretty interesting piece
instead of like
two modes explore and exploit and then
we're gonna have a parameter that flips
us one way to the other like a light
switch
or we have one extreme explore mode and
one extreme exploit mode in the model
and then we're going to have a dimmer
that goes between the two in active
inference
the knob that kind of does that is
actually the prior precision
over preferences so if you have no
if you have no preferences aka you have
no precision over preferences you're
going to act in the maximally
exploratory way
if you have an incredibly strong
incredibly precise prior
over your preferences then you're
going to act in a very exploitative way
like if there's two restaurants
and one of them you like you know 60 the
other one you like 40
if you have no preference you're going
to go to them 50 50. that's like
explore but then if you have a super
high precision over your preferences
you're always going to go to the one you
that
you prefer even if it's only slightly
preferred
an analysis of how performance of the
algorithm depends on that parameter
showed that parameter values that give
the best performance decrease over time
suggesting that this parameter should be
adaptive and decay over time as the need
for exploration decreases
so start with low precision over your
preferences
and then you learn
and you update so that eventually you
increase your precision later
attempts to remedy the situation with a
simple and widely used decay scheme
we're not successful
so the logarithm of time so you just
make the precision
directly a function of time like you
know one
over the number of trials just that kind
of thing it's like that's a
function that scales with the number of
trials so here
you scale it with the logarithm of time
this indicates that it's not a simple
relationship and a proper theoretical
analysis will be needed to identify
whether a scheme exists
so that's pretty interesting like how
are we gonna
pull back a level okay we think that
active inference architecture
is gonna be a really productive way to
model learning under uncertainty
but we're also just pushing the problem
up a level which is
okay how uncertain should we be and then
how should we change that uncertainty
over preferences moving
through time so nice point there
and then um one
last thought is in the non-stationary
so the dynamic switching bandit the
active inference algorithm generally
outperformed the bayesian upper
confidence bound and the optimistic
thompson sampling
this provides evidence that the active
inference framework may provide a good
solution for optimization problems that
require continuous adaptation
active inference provides the most
efficient way
of gaining information and this property
of the algorithm
pays off in the non-stationary setting
cool points that it'll be awesome to
hear the author's perspective on
so how do we compare active inference
framework algorithms
to machine learning more broadly
and then especially for problems where
informed
foraging is helpful like
not that epsilon greedy just sometimes
look away from the best and pick
randomly
and not even just the thompson sampling
remember pick each arm according to how
likely it is to be the best arm
we could have an even more informed or
empirically
better performing scheme for doing the
trade-off
for earning while learning you know
earning while learning doesn't mean that
you're
learning optimally or earning optimally
or
how are we going to balance that out and
it seems like octave inference is going
to be a strong contender
in the coming years as more and more
people in the machine learning community
start to
get keyed into these results tune the
regime of attention
to what these authors and others are
doing and it starts to become
more broadly understood that hey rather
than just
having more and more parameters and
billions and billions of parameters in
our model
and training in on larger and larger
networks of you know computers
what if we just had a curious agent who
learns how to learn and prefers to win
it's sort of like a ground floor
reinterpretation
of these problems and i think hearing
the author's
views on where the active inference and
machine learning
communities and fields are heading will
be
for sure informative for us what do you
think about that blue
i just i'm thinking about problems like
um like the mountain car problem
like we're actually learning is winning
right like when you have to
if you have to explore you want to go up
the higher you want to go up the hill
so that you can get back up to the other
side of the hill and the flag
so like what other problems are out
there like that that
doesn't don't necessarily that have like
a reward that's uncoupled to
ex uncoupled from exploration so i i'm
thinking about that and i don't know
just where is where is learning winning
great
question it's almost like in the
mountain car the altitude
is in some senses a reward heuristic you
want to get to the top of a hill so
it seems like altitude would be the way
to go but then the way that the problem
is set up
you could also optimize the bounds and
say i
seek to be expanding my bounds laterally
more
oh yeah well of course we're changing in
height you know we're in the mountains
but especially for cases where we focus
on exploration
like innovation or maybe other areas
it's cool to think about how active
inference can perform well
so what are the next steps for the
authors and
for us an important next step
in examining active inference in the
context of multi-armed bandits is
establishing theoretical bounds
on the cumulative regret for the
stationary bandit problem
because as we saw it kind of diverged in
an unexpected way
that made sense but still wasn't quite
the behavior that
was initially expected and a key part of
these theoretical studies will be to
investigate whether it's possible
to devise a sound decay scheme for that
lambda parameter
so how rapidly should we change
our precision over preferences that
provably works
for all instances of the canonical
stationary bandit
what would that enable that's our
favorite question this would lead to the
development of new active inference
inspired algorithms
which can achieve asymptotic efficiency
these theoretical bounds would also
allow us to more rigorously compare
active inference algorithms to the
already established banded algorithms
for which regret bounds are known
moreover we would potentially be able to
generalize beyond settings
we have empirically tested here future
work
may also consider an information
theoretic analysis of active inference
which might be more appropriate than
regret analysis
also kind of a cool idea like
regret analysis was performance oriented
it's saying you're calculating your
regret based upon
the difference in performance between
optimal versus what you did but another
way to look at that
is using information theory and looking
as a function of
information being gained perhaps through
time
which just like you brought up it really
helps us focus on
exploration because if the whole project
is framed in terms of performance and
reward and value
it's almost like favoring exploitation
off the bat
because exploration is always going to
have to get couched in terms of
successful
exploitation like this basic research is
important
because later on we'll be able to apply
it which is fair
but when we have an information
theoretic analysis not just a regret
performance analysis
there might be a way to have exploration
for exploration's sake and what that
might enable
or even exploitation can be
thrown in in in terms of surprise uh
surprise minimization right like if
we're going to frame active inference in
terms of minimization
of surprise think about something like
the stock market problem right like this
is very much like a switching bandit
problem like
everything's changing all the time like
it's the same for a little while
like you're you're your stock that's
gonna win
so it like you know you're surprised
when you deviate from
say the s p 500 so you want to track
with the s p 500 and surprise happens
when you deviate from that
one more thought there on the
information theoretic analysis
and how it might say something different
than regret
let's go back to picking a restaurant so
we often hear about like controlled
novelty
you want surprise but not too much
surprise
so this gives an explanation for why
people might like their favorite
restaurant
it doesn't even need to be thought of in
the context
of maximizing reward like the 60 likely
to be the most rewarding restaurant
it could be like i'm trying to reduce my
uncertainty
so i'm likely to choose a place that i'm
familiar with
so that maybe i'll choose a different um
meal or maybe i'll choose the meal i
always order
but it's like the choice was driven by
reducing uncertainty
not even per se by maximizing reward
which is something that we come back
all the time to the difference between
value driven
reinforcement learning reward learning
and implicitly regret which is regret
about reward and reduction of
uncertainty
which puts us in a whole different space
yes we're able to enter that whole
physics of information flows area and
where we get the pragmatic
um straight components and then the
solenoidal the flow the iso contour yes
we access that whole area
in the information theory reduction of
uncertainty world
but also we just get qualitatively a
different story in a different
explanation for behavior
again you don't need to grasp for why
somebody's maximizing reward
with why they went to that restaurant or
why they ordered that one thing
when a lot of times just it stands alone
as an
uncertainty reduction and prior
preferences
understanding rather than needing to
make it about some sort of
maximization one one i'll flip the last
slide and then we have a
awesome question so um alex v
wrote is there connections between
exploration on epistemic value and
exploitation for pragmatic value
i think that's related to what you were
just speaking about
um which is that we're putting it on a
common
footing with active inference in terms
of the reduction of the expected free
energy
which has this epistemic or knowledge
gain component
and this pragmatic or functional
component
so the epistemic is like learning and
the pragmatic
is earning so we're we're learning while
we're earning
or the other way around we're
acquiring epistemically valuable
information
while we're also acquiring pragmatically
valuable information because the
decision making
of expected free energy minimization
conditioned on policy we're choosing
policies
based upon a function that
looks at both of those jointly and so
that
is one of the ways that we're rethinking
exploration and exploitation
by thinking okay that's not really the
duality
of policies that you want to talk about
because explore exploit makes it sound
like it's two behaviors that the bird
can be doing
and so here what we're doing is we're
kind of taking that idea
of sometimes you want to be doing a more
exploitative act
other times a more exploratory act and
then we're asking
given the policy of which a whole
spectrum might exist
of different policies how is each policy
contributing to epistemic and pragmatic
gain and then which policy
is going to have the best combination of
the two
maybe there's strategies where you're
maximizing both and maybe there's
strategies where you're maximizing
neither
but if you're only looking at one or the
other then you might uh
choose one that's like a poor
combination
well so a perfect example is like you
know so
your policy is based on your previous
chance of of
reward of minimizing surprise so i have
a policy that i'm not going to
eat a meal i've never had before in a
restaurant i've never been to before
because i
like i don't know what i'm getting into
that's like way over there right so my
policy would be to order a new meal in a
restaurant that i like
or order a meal that i'm used to
in a new restaurant so that would be
like the policy
in that just to continue that example
cool well what a fun discussion
i hope this was useful to those who are
familiar
with active inference as well as uh
bayesian statistics machine learning or
not
it's all chill because your questions
will
really help move the whole project
forward the parts that do and don't make
sense
and the parts that you want to explore
more i think that's how
our ensemble is going to proceed in
these transdisciplinary areas
is by welcoming those who have different
backgrounds so
whether you're really familiar or not
you're totally welcome to participate
in our live discussions or just to ask
questions or
participate in some other way
thanks blue for the awesome help with
preparing the slides and for this
conversation and we'll see everybody
another time
bye bye
