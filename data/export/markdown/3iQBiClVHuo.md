---
title: "ActInf Livestream #018.2 ~ The predictive global neuronal workspace: A formal act inf model"
category: "Livestream"
series: "Livestream_018"
episode: "2"
speakers:
  - "The predictive global neuronal workspace: A formal act inf model"
duration: "1:57:41"
url: "https://www.youtube.com/watch?v=3iQBiClVHuo"
views: 135
exported_at: "2026-02-18T22:37:37.683704+00:00"
format: markdown
---

# ActInf Livestream #018.2 ~ The predictive global neuronal workspace: A formal act inf model

hello and welcome
to the active inference live stream this
is the active inference lab and we are
here in
active inference live stream 18.2 on
march
30th 2021 welcome everyone
to the active inference lab this is a
recorded in an archived live stream so
please provide us with feedback so that
we can improve on our work
sorry the video just changed a little
bit there we go
um all backgrounds and perspectives are
welcome
here and we'll all be following good
video etiquette for live streams
today we're here in session 18.2 on
march 30th
having the follow-up discussion with the
authors and other participants
on this predictive global neuronal
workspace paper
and today the goal is really to follow
up on the last
week's discussion continue discussing
and learning about this very cool paper
and why the authors did what they did
and what are the implications for
different areas
so today we're just going to go through
some introductions
and warm-up questions and then we'll be
able to walk through
the paper and the slides and ask a few
questions to the authors and get a few
different perspectives
so for the introductions we'll just go
around and introduce ourselves
and then pass it to somebody who hasn't
spoken yet
i'm daniel i'm a postdoc in california
and i'll pass it to
alex
thanks hi everyone i'm alex watkin
i'm a researcher in systems management
school
in moscow russia also i'm a corner
of co-organizer for active inference lab
and i pass it to steven
hello i'm stephen i'm based in toronto
and i do a lot of work with social
topographies
and landscapes for social drama
and i will pass it over
to dean
hi i'm dean uh i
am retired i'm hanging out in the uh
loft of
my cabin which is not very well lit
uh i'll pass it to ryan
um yeah um so i'm ryan smith
um i'm a investigator at the laureate
institute for
brain research i'm in tulsa oklahoma
um yeah i mainly work on computational
modeling
of uh empirical behavior and different
psychiatric
disorders um as well as some theoretical
work on
emotions and emotional awareness and
interception
and i guess um i guess i'll send it to
chris
hi i'm christopher white i'm a phd
student
at the university of cambridge in
england um and i mostly work
on active inference or computation using
active inference with computational
models of
cognitive control but
a lot of my previous workers kind of
focused on visual awareness
so i'll pass it to adam
hi uh i'm adam i'm a
post-doc at johns hopkins school of
medicine
um center for uh psychedelic and
consciousness
research i'm also a research fellow at
the kinsey institute
and i'm in consciousness free will too
that everyone cool does anyone want to
raise their hand
and give a thought on one of these
warm-up questions
which are just what are something
they're excited or curious about today
or something that they liked or
remembered about the paper or
last week's discussion to sort of
jumpstart where
we were at um or maybe
really quickly at the beginning
christopher wanted to clear up something
so yeah and then we'll kind of go into
questions so maybe everyone could write
down a question and then christopher go
for it
yeah sure so i said two things that like
just false
um last time i just made mistakes i kind
of wanted to correct them so the first
one i was in specifically referenced
someone asked a question about the
thalamus
and its involvement in consciousness and
i kind of referenced a whole body of
work
from matthew larkham's group and i think
i said the medial dorsal nucleus and
it's not it's
central lateral nucleus and thalamus um
i think like 99 people wouldn't care but
anyone who knows anything about the
thalamus would have been like pained by
that
um and the second thing was i was
talking about king and
hans like uh
bayesian model of conscious access i
think i described the model as
univariate gaussian
that's also not correct it's a
multivariate
um like gaussian although you can
extend the same model um
to a univariate case anyway doesn't
matter
but i just wanted to kind of correct
those two things
thanks for the correction so if everyone
could raise their hand and first
um we'll go with adam and then stephen
um i was uh curious about uh
what chris just just said so like medial
door so that would be
what thalamus for interior singular in
the frontal lobes
kind of like the gateway to um like
amygdala at all
would that be right and then like so the
central ladder like who's that looping
with i forget
i think central lateral would be looping
i was specifically thinking that like a
loop between layer five pyramidal
neurons
and um central lateral thalamus
so if i could ask a question there just
why
are we identifying brain regions or what
would it mean to be
identifying brain regions one way or the
other in humans or some other species
um so this particular body of work
not to go too far on a tangent but
there's this really impressive body of
work that basically has identified
both level of consciousness and content
of consciousness
with burst mode firing in layer five
of cortex i think most of this at most
of this evidence is from a mouse model
though so interpret that as you will
yeah adam or you can use the actual
jitsi bracelet
but yeah go on um i mean for me
um it would partially be
what systems might contribute to
wakefulness or different aspects of
consciousness depending how we want to
carve the joints on it
in different respects so um let's say
uh stimulating the medial dorsal was
like more important
well then that might implicate like the
specific relays
um its ability to form phlegma cortical
loops or
flammable striatal core like the whole
uh
what it helps to bind together
functionally
and other functions uh it would tell you
what processes
might be involved so um maybe action or
salience that might be important or
maybe it's like
frontal lobes as hub but like which part
of the frontal lobes
is it the parts that are like a general
topologically central hub or does it
look kind of like
a motor bits or does it look like
something else so
i'd be trying to look for like fish
around for clues about what's important
in what ways
but it might mean but it's easy to tell
stories
okay cool so stephen and then anyone
else who has a question
so yeah i'm just uh really excited about
the
when i when i listened uh last week you
talked about temperature
being used in the models and like you
had different places where you used
different amounts of temperature
in i think it's in the soft map function
to to show
um different types of
model scenarios so i'll just be curious
i'm just excited about
maybe um just the general way that you
use your thinking to build the models
to inform how you start to look at
consciousness and the way the brain
works as much as
the way that you find the results from
the models
so that i'd be interested in that those
sort of two sides
so so i mean one one thing i just want
to make sure this
is clear is that you know like
computational neuroscience
borrows or has been historically ended
up borrowing a lot
from um terminology and physics and
engineering and things like that
um you know so there's some of these
sorts of terms that can be a little
um a little funny right so so like
temperature like a temperature parameter
or typically an inverse temperature
parameter
um there's something that's borrowed
from physics that just kind of has to do
within the physics set
in the physics sense kind of how how
much
uh you know with how much energy
particles are kind of bouncing around
against each other um
and um you know in a very oversimplified
way of putting it
um but but so it just means essentially
there's more kind of
randomness right in the in the system so
in the context of um
of this um you're just applying that
same equation
to describe essentially the amount of
noise in decision making
so uh a higher temperature in this case
just
is just a parameter in an equation that
controls how deterministic versus
stochastic decision making processes are
so i just want to make sure that it has
i just want to make sure it's clear to
anyone listening that it has nothing to
do
with actual like physical temperature
like being hot or cold it's just a
parameter that
just that kind of modulates how random
decision making is
um so i just wanted to make that make
that clear so
in this case it's just it's just
controlling
so so for example if if the temperature
parameter is really low or the inverse
temperature has a really high value
then that just means that say even if
the model was only like 51
versus 49 confident in one thing over
another it would always
choose the action associated with the 51
um whereas if the temperature value
temperature parameter value is high or
is low
um or is high or the inverse temperature
parameter is low
then um that means that the
like for instance uh that with 51 of the
time
it would choose the um
the action associated with 51 percent
proper with 0.51 probability
you would choose that one less often
than it would if the probability would
say 0.7
um you know and less probability than
that than if it was
if the probability was 0.9 so
essentially just
um having a a low inverse temperature
parameter
value just allows the probability of
choice
um the actual choices uh that's our
frequency of choice
um to kind of scale in some sense with
the actual
probabilistic beliefs over the different
um states in the model
thank you ryan we'll have christopher
then adam and
anyone else who raises their hand
so just to kind of contextualize that a
little bit um
so a soft max function is exactly the
same function as a boltzmann
distribution from statistical physics
so often if you have a you'll just use
the same terminology because it has
and in the physics case it has like a
literal physical interpretation
in this case it doesn't um so that's
kind of why
there's that overlapping technology um
in terms of deciding
why or on those parameters or actually
building them in
it was really just kind of came from
thinking about what perce what attention
does
so what we're trying to modulate there
was a tension and
signal strength and both of those things
in some way modulate the strength of
feed forward input
so when you think about that you then
kind of think okay what part of the
model corresponds to that well
it's the likelihood matrix that maps but
that decides the precision of the
mapping between external observations
and first level hidden states and so
both the idea is is that both
attention and kind of external signal
strength where or
it might be something like contrast
whatever
um will jointly determine the precision
of that mapping
um and then there's lots of different
ways where you can kind of cash that
out if you actually want to get into
kind of the neurobiology of it like the
normalization model of attention or bias
competition or something like that but
kind of extracting away from that detail
basically it just modulates the a matrix
the computational level of analysis
so that was kind of the thinking that
went into it
very interesting adam then stephen than
anyone else
okay adam can you be ready to speak but
go for it yeah sorry about that
oh um it's kind of off the current topic
but from before
so some quick googling uh turned out the
central
lateral um seems to be looping largely
with parietal and temporal association
areas
so that's potentially interesting in
ways that
indirectly could like speak to debates
on the physical substrates of
consciousness like
the the brouhaha between iit and gnwt
said more like the front of the brain or
the back of the brain and
in which senses do they mean
consciousness
but it's interesting i actually i'm
having trouble finding an image
of like a diagram of the thalamus
actually shows the centro
uh lateral nucleus it's all just like i
see central medial but not central
lateral
it seems like they might be kind of like
tucking it in with the pulvinar
whatever that means stephen
yeah just say thanks for that that
feedback that was really useful i think
also i because i've got a background in
chemistry i keep thinking about the
gibbs free energy where it talks about
um temperature times change in
entropy in that term so it's like um
that that the temperature is multiplied
into the amount of entropy
change there is to make it more
significant so that would
kind of mirror why it's a bit like
you're putting in noise or entropy so
uh that that's quite useful um so yeah
thanks
yeah welcome blue you you um
you or anyone else can raise their hand
but one chemistry
metaphor and again ryan as you brought
up it's not
always like a literal uh meaning but
thermodynamic versus the kinetic
alternative for a reaction
so like the thermodynamic outcome for
the candle is to burn
because it has all this pent-up energy
but it doesn't spontaneously combust
because the kinetic barrier the
activation barrier is too high
and then when there's like an enzyme or
a spark of energy
then at in the right situation the
product can go all the way down
the big delta g to the kind of ultimate
thermodynamic
least energy versus the more kinetically
accessible
and so that's kind of like information
foraging there's sort of the perfect
citation you would find
if you had the right search and it was
that low temperature or
something analogous but then if it's too
um kinetically constrained then it's the
attention is drawn
away i'm not sure if that will map
directly
in this whole active inference mode but
it's just kind of another
chemical informational distinction
well i mean it depends i mean it depends
how you're using it like in this in this
case
there's not really much of a connection
because we're just essentially we're
just using
a temperature parameter and a softmax
function to control
the precision of a mapping well in a few
different places
for attention and for stimulus strength
we're just using it to change the
precision of the mapping between
states and observations at the first
level
um so it just it just controls
essentially how how
strong a sensory signal ends up updating
beliefs
um posterior states at the first level
um
and then modulated by a second
temperature parameter that does the same
thing
but that accounts for attention so these
sorts of things
jointly um control um
essentially how much evidence sensory
input provides for posteriors over
states at the
at the first level um you just we're
using it for that kind of thing and then
we also use it for
controlling deterministicness or the uh
choice
at the second level of the model in
terms of in terms of uh
action selection um so in in all those
cases i i don't personally see a
direct relationship between that and the
kind of thermodynamic
um thermodynamic aspect of temperature
of getting over
um you know energy barriers and things
like that um but
i mean it could be i could be uh i could
be just not thinking through it all the
way
stephen then anyone else
yeah i think that makes a lot of sense
what you're saying and i suppose the
nice thing with the modeling
is that you've got this potential to i
know you're using it like you say is
this
way to bring in noise or soft max but it
gives you that way to
increase and decrease it which in real
life when you do empirical work it's
hard
to to do that so it's it's one of the
strengths of
the modeling that you can change that
parameter and see
it seems to be one way that you really
get insights into
the dynamics of the system
um yeah i mean in terms of just being
able to modulate
modulate the uh or mimic the influences
of attention on modulating the
background perception of the signal
yes stephen or uh dean and then stephen
yeah i just have a quick question here
um
and maybe this is far too oversimplified
but
when you guys were doing this work i i
started also looking at the uh
um the effect paper that i think the two
the two together gave me a better sense
of
some of the work that i was doing around
helping people walk into these
novel situations pre-reflectively and
there is a tendency to want to commit to
want to pay attention to
want to give over whatever you have in
terms of processing power to
figuring out what's going on but we had
to spend quite a bit of time on
helping people get the idea that there
is this channel there's this kind of
sweet spot and when you were talking
about degrees
it brought it up for me again the idea
of
how to help a person know when they're
over committing
when they're over correcting and when
they're over compensating
so when they're trying to do this
estimation
how do they know that they're not seeing
the moon walking bear because
they're so committed to counting up the
number of basketball passes i wonder if
you guys had spent a little bit of time
looking at the other end of the of the
channel
when people can actually readjust back
in and i know that's that's probably
where the degrees part comes in but i
was just wondering about that
so i mean are you imagining are you
imagining in some kind of like clinical
scenario where a person yeah
like biased attention away from
something that could be
say aversive if they were to focus on it
yeah exactly
um yeah so i mean i mean there's there's
probably
a mechanistic relation in a sense just
in the broad sense of
you know how we think uh attention is
implemented
right so so for example if you if you
think that
you know a person um is avoiding paying
attention to something
because it would be aversive right
then then you can end up with this kind
of implicit reinforcement of
attentional policy selection which we
don't directly have
in in this model right the agent is
choosing what the precision is
associated with the tension in this
model
but but that's something that can be
added and something that we have
actually added in some more recent work
that we're doing right now
um but the idea the idea there or one
way to think about that would be that
when uh whenever a person essentially
starts
to pay attention to the thing that would
be aversive then
they start to feel it starts to feel
aversive right so then if they pay
attention
away again then the the choice of paying
attention away
actually ends up being negatively
reinforcing because the bad feeling goes
away
right so then what that ends up doing at
least according to this kind of
reinforcement learning account
is that that ends up assigning higher
value to the
policy of attending a way right so over
time the probability of attending a way
just ends up getting higher and higher
because it makes you feel better every
time you do
um so then this sort of avoidant
attention can become really kind of
habitized
um and and uh so you know
that's one way of thinking about it and
so you know and like in like
you know in in the clinical setting
right you you want to help people
potentially
you know like start to you know
gradually
you know expose themselves to to you
know pay attention to this thing that's
aversive
um in hopes that if they're able to kind
of do that
in a sustained way then over the long
run
the aversiveness will go down as they
kind of learned a better deal with the
thing that they've been
avoiding intentionally um you know so so
that's um that's
um yeah fairly tangential to right the
kind of thing we're trying to do
here but um you know but there's a
there's a connection in this very kind
of broad sense in that if you can
control attention
and choices of what to pay attention to
can be
reinforced then that's one way you can
kind of end up with this
this kind of thing where person might
not even know right that they've
developed this strong
habit you know not to pay attention to
something it just becomes very automated
um you know the same way the same way
any other behavior can be habitized via
repeated reinforcement um but here just
it would be a
kind of a cognitive action as opposed to
a a
a more overt behavioral action okay
very interesting thanks for that
question response
adam and then anyone else who raises
their hand
i guess to come out of left field um
and what you're just describing it seems
like
that could have um some relation to
maybe
grounding like psychodynamic-like
concepts
in terms of if these patterns of
attentional approach and avoidance can
move from your c matrix to your e matrix
you can
end up finding yourself in these sort of
like garden paths of attending
and coming to uh inferences for reasons
that you might not even understand just
on
the way your policy selections of
attention have been shaped for
conditions that are might be too uh
numerous and varied for you to track and
so
yeah yeah i mean there's i mean we've
written you know we've written a few
papers on this
right like or i have with some
colleagues i mean again you know my
focus
um you know is largely in you know in
terms of
and psychiatric conditions right and i
wouldn't um
i would say it's a way of of recasting
the sorts of behaviors that
psychodynamic approaches
are trying to capture but to do it in a
way that doesn't um
actually posit the existence of these
sorts of
repressive right like you know like
unconscious like there's no unconscious
agent
right there's no id right that's being
positive that's
sitting there keeping these things out
of awareness but somehow they're
still present unconsciously right
there's nothing like that
right it's just a very simple story of
um
having reinforced patterns of attention
that um you know so it it's a it's a way
of capturing the the phenomena that that
i think psychodynamic approaches are
often trying to capture but
it doesn't posit a lot of the kind of
like ontological
um a lot of the entities that are
positive in psychodynamic
um so yeah it's like yeah i'm
not saying like you're freudian but like
yeah you're actually finding like the
baby in the bath water
rescue eyes rescuing it cleaning it up
contextualizing it
like why did people have these
intuitions to begin with like what was
the grains of truth
um i'm wondering if through this this
could lead to
um like this kind of uh patterns of
attending
some of which you're not tracking this
could be like an account of what would
lead to potentially uh mismatch or
discrepancies
between things like stated and revealed
preferences
or a thing like um your actual affective
disposition with respect to thing and
then what you
think is going on and then those
potentially go across purposes in ways
that could be different difficult to
explicitly model and potentially have
like
problematic sequela or not but i'm
wondering if like this could lead to
like a mismatch or across
purposes of uh
attracting states at different levels
um i mean i probably need more concrete
examples to try to figure that out i
mean that's probably something i'd have
to think about more
i i guess one quickly would be like um
implicit affect tests or something like
that like
you say like um uh i'm not racist
but then it turns out no no you are and
like if you actually look at the
reaction or something like that or
i am really happy in this relationship
but then like i measure your heart rate
variability and its crap or
things like that um just this your
actual affective state
might end up being different than what
you think it isn't there could be like a
lack of self-awareness
like a difficulty coming to coherent
modeling of yourself because of these
like
shaped paths of attention like you might
like miss the mark about you because it
was like difficult to see
something like that i mean i mean i i
would i would think that you know
i mean perhaps there are sort of some
instances of the sort of thing you're
talking about
to be captured by the um the kind of
mechanisms that
you know we're talking about here or the
kind of tangential extension of them
that we're talking about here um but i'm
not confident that all of them
could i imagine there's a number of
mechanisms that you might feel to
describe some of those things like
um you know implicit yeah like i mean if
you're talking about like implicit
associations on like
like an iat right or something or
something like that that's probably
my intuition is that's probably
different from um yeah it's more kind of
like a
like like uh like us right which i know
chris has actually been working on
models of street tasks um
but um right which is which is probably
pretty different
from um um some of the other examples
you were given
but but yeah i mean like i said i'd have
to taking a particular example i
probably have to think it through a
little more
um to see think about what sorts of what
kind of generative model would be able
to reproduce what kind of behavior
you're talking about
um or or you know most likely there
would be multiple generative models that
could reproduce it and then you'd have
to
do some kind of experiment right to do
model comparison and see which one
actually best accounts for it
um but again i wouldn't feel really
confident um
you know saying what that might look
like um
you know just just in the very kind of
abstract general
you know description we're talking about
right now
nice nice thank you for the response
stephen
yeah i'll just bring in this sort of
this point with this model that's now
sort of maybe getting into the model in
part is i think that's interesting with
the awareness base there's a lot of work
with awareness-based systems change and
looking at awareness
and i i like the um i'd be interested in
your thoughts on
how we can move beyond being trapped
in a psychology of the individual and
you know
pathology of the individual and it moves
into the inter-subjective
multi-scale so like you talk about tasks
but you it also could be used in
task scapes you know organizational
contexts or
groups of people so i just think that
there's um
because the the it's not nailed down to
like a psychological model of the
person's
thoughts and feelings but more a general
model of the attentional
structure it has like a you know ability
to move beyond
between scales and context so um
i just think i'll put that out there as
something that seems quite interesting
um i mean there's more i mean
um so
i think the utility of models like these
is to identify a very specific
phenomenon
and that namely having conscious access
to some content and not others
um so i have conscious access to what's
in front of me my visual field at the
moment
if i direct my tension around my body i
can bring up
all sorts of like i can suddenly become
aware of different kind of
some other sensory bits of information
and all of these have very specific kind
of
neural signatures as it were what we're
trying to do
is really propose a model at a
computational level of analysis
and algorithmic level of analysis that
explains these
and i outside of that
i'm not sure to what extent
actually talking about awareness
into subjective awareness is at all the
same thing
as talking about awareness
as someone who works in like
neuroscience of consciousness for
example
they might be but i don't see any
evidence that they are
pretty interesting because it's in the
title of the paper so
many people might think of it
differently
as i mean it's just an interesting
question right
sorry what's in the title of the paper
um just
the idea that the uh
visual consciousness is involved
well but i mean but again i mean this is
a model of a particular visual
consciousness
past right i mean so it it's meant to
account for things that are seen
in the visual consciousness literature
um you know there is the structure is
abstract enough that
you know we would and we say this in the
discussion that it ought to apply
to cases of having access to one
bit of information versus another um in
other domains
right like an auditory domain or you
know something that i've been working on
you know with a bunch of colleagues at
um you know at libra where i am
um you know it's trying to see if the
same sort of thing
it looks like it's present in the
interceptive domain for example
um you know so so i i think it's right
to say
that you know we would we would hope
anyway that it's abstract enough that it
can account for
any any piece of information
that you either gain access to or not
you know when it's being represented so
much so right so
whether it's you know right now as i'm
talking to you i'm not necessarily aware
of what my heart's doing
but now i choose to pay attention to it
and all of a sudden i can kind of
feel that it's beating at a certain rate
i believe i believe
i believe that i feel i wasn't conscious
of that before
despite the fact that my brain was
unconsciously tracking
you know what my heart was doing that
whole time right so it could apply to
being aware or not aware of any stimulus
so i mean to the so only to the extent
that
when we say something about
intersubjective awareness only
to the extent that that means something
about a piece of information
that you know before i was attending to
it i didn't know
you know was there but now that i'm
paying attention to it that i do so for
example like if i happen to
notice that a person's smiling or
something
like that um even though they were
smiling at me the whole time you know
maybe my brain had
picked up on the fact that they were
smiling but um i wasn't aware of it
until i focused my attention on it
or something like that right or even
maybe more abstract than that
you know when my brain sort of had
unconsciously
detected the smile there might even have
been some further inference that that
means something about them being happy
right so so there might even be a case
where
um i either do or do not gain access to
this unconscious inference
or this posterior belief that the person
is more likely happy than unhappy or
something like that right
but uh but i mean these are sorts of
cases they would have to be
tested in their own in their own right
my broad point is just that
it's an abstract structure where all it
is meant to account for
is when your brain is representing
something and you either become aware of
it or not
i mean i mean if i could just kind of
build on that slightly
so i think
one it's very tempting when we've got
computational models that are
real when we've got lots of equations
sitting in front of us to kind of think
that i think it's easy to get an
illusion of rigor where there is none
um the thing that makes these models
meaningful is that we can we're tracking
some real world phenomenon
um in terms of the abstract model
structure
it may be the case that say
you have group dynamics where there's
some group that some aspect
of that maybe the individual behavior of
individuals within a group evolves at a
really quick time scale
and then the decision that group
decision making evolves as a slower time
scale
you may be able you you could in
principle
fit a two-level partially observable
mark of decision process to this
as a model of that behavior but that
would be very very diff i think even in
that case even when we're fitting the
same model
i don't think that those are at all the
same phenomenon
although there may be similarities
across them
um i would be extremely resistant to
calling one visual awareness
or but a group has visual awareness
interesting and of course a parallel
debate in the ant world
is there a colony awareness or a single
six-legged
ant awareness or how should we think
about
distributed systems and aren't we all
kind of just distributed systems all the
way down
so adam and then stephen
um so this would be related to i guess
uh different types of uh
interest subjective or yeah interest
objective awareness that you might
believe is a model for
um i recently um uploaded a preprint
after some conversations with people
from the brain institute at chapman
university
basically trying to do the beginnings of
like an active inference account
of la bay phenomena and readiness
potentials that are
a little bit less deflationary with
respect to
uh volition and uh conscious causation
and so like in like essence i was
thinking of like
um the actual uh
moving your hand being like an
accumulation of
model evidence model evidence with
respect to
a proprioceptive pose and it might be
some sort of like conjunction of like
um also like and hum like
whether or not your like will or feeling
of urge was part of it you could think
of that as like
um inference over your affective state
and that if these things are in
what kind of alignments could help to
explain whether you're like aware
of readiness potential activity or
whether this awareness is actually
feeding back and contributing to it
and so i feel like your model could
potentially like
provide like a very precise
contextualization of this
really subtle what's going on uh then
i would like to collaborate so so i mean
just just just again
brad just to make it really maybe that
could be the case i have no idea
but it could only potentially be the
case if
what you're talking about right like
what you're you know motivated to
do or what you're you know in the
process of about you know being about to
do or you know whatever aspect of
um you know action or action tendency or
you know anything like that
um the only way this could apply is if
you think that
that information about what your
you know what you're motivated to do or
or something like that you know whatever
it is
and only if it's the case you think that
is
a represented piece of information um
that you can attend to or not um and
that then you could sort of
um gate into the higher kind of people
deeper temporal level of the model
that would inform um verbal reporting
and sort of other goal directed
uses um so it'd only be the case i guess
my point is this
is if the the representation associated
with action that you're talking about is
in some sense formally equivalent to a
representation of something visual
um that that you can attend to
that makes sense so it's um so the
preprint is like
it's like a three i think like a three
page more of a promissory note
but if i could uh like pick your brain
later about like
if you think there's like a way we could
actually get some like empirical
traction and like
nailing down the specifics along the
lines you're saying so well if you
haven't
i mean if you have a task and that task
involves people paying attention to
the aspect of action that you're talking
about um
then in principle you could have people
you could have people you know in some
sense cue them
or prime them or something like that
that that engages that
sort of action bias or action motivation
um and again you can they can either
attend to it or not or report on it or
not
in that case yes but otherwise probably
not it's a little tricky i think in
terms of like
the action that would be attended to
would be of a couple varieties but
none of them through them would be um
directly observable so it's like
you could say like it's the action of
the neural activity in terms of like the
ramping activity like do they have
access to that but the
i was thinking it could also be like um
the action of like mental acts and like
rehearsing like
imagining a kind of sophisticated effect
of infant sense like
am i gonna move my hand or not what
would that be like
and then that being contributing to
that signal um but and where like
actual awareness of this like fictive
meant this fictive action could be part
of what would contribute to
uh whether or not you feel ownership of
it like it's
it's interesting like some people don't
show readiness potentials they just act
other people do
um like schizophrenic patients they tend
not to show readiness potentials before
they
spontaneously raise their hand but it
would be hard to get this
um the action is internal
and so i don't know what you should do
with that yeah it just seems it just
seems like you have to have some kind of
behavioral readout that can be fit um
to unlock to to a model of this to be
able to say
that this explains the ability to
consciously
report on it or not right so
i guess could you use like like
right before leading to like the action
there tends to be like it starts out
like
more bilateral and then the ramp
activation tends to go lateral and then
the hand moves
could you use like that sort of signal
as the readout like the ensemble
activity
so in principle you can use you know you
can fit models to neurologic neural
activity
and you can fit models to anything that
the
generative model generates but
but i'm not necessarily all that
confident that
you'd be able to justify the claim that
um
because the because the model in one
case
generates you know like a readiness
potential signal
that that has anything to do with having
conscious access to something
any of the other problem like if you're
using like the ensemble activity it's
still the interpretation like
awareness of what like what
what are we even talking about with the
awareness the whole point is to try to
like contextualize what those signals
mean
and so yeah yeah i mean i mean
in the majority of cases you know either
directly or indirectly
you know like verbal report right is
still
kind of gold standard for whether
someone has access to something
right even in no report paradigms you're
still later
right asking them to report what they
were experiencing at the time
um and so it's i mean in the yeah the
issue is that in some sense all
kind of supportable or accepted
sort of evidence for being consciously
aware of something
um is always ultimately and chris you
can correct me if he thinks is wrong but
but i mean
i think that it always ultimately comes
down to verbal report or some reliable
correlate of verbal report
whether or not yeah i agree with that so
i think
i'm not an expert no report paradigms
but to my to my knowledge
all of them the reason we trust no
report paradigms is because our
measure whether that is a particular
mode of eye tracking
or it is just like incidental memory
afterwards
um all of those things correlate really
really well with report and that's the
thing that kind of like
makes us trust them as measures of
conscious access independent of report
um yeah i think it's always reports are
foundational
unless we have really really good
evidence otherwise i think we have to
take them kind of at face value
cool we'll return to the stack so blue
and then stephen and then anyone else
who raises their hand
so adam always brings me into this like
metaphysical
like thought space whenever he talks um
and i just was wondering uh you know in
terms of this like
visual model there's you hear the
expression that people see what they
want to see
right and so have you thought about
maybe testing
like you know like there's the the idea
of paying attention to something
and so we thought about testing like
whether you know people
can deceive themselves in this visual
process right like some self-deception
or even like the you hear of like the
power of manifestation like can people
bring into their awareness something
because
they simply want it to be there i mean
have you thought about this or testing
the model in this way
yeah i mean if you go to a figure um
maybe
scroll down is it which one so we have
it we have us
actually i'm not sure uh so that's the
erps
yeah that the tax of the extended
taxonomy
so we start with this kind of four-way
taxonomy between which tahan proposed
um along with some other colleagues of
the kind of factors underlying
whether you'll have conscious access to
a stimulus and you kind of broke it down
into
whether attention was weak or absent
present or absent
or whether kind of just how strong the
signal strength was with the streak
um weak or strong and then we extended
this by adding in
prior expectations so the extent to
which you expect a stimulus to appear
um and there is now like a one of the
big motivations this work is that there
is an enormous body of work
now showing that expectation does play a
fairly fundamental role
i think in determining the contents of
visual awareness
um so as for whether you can voluntarily
bring something into awareness i'm not
the answer is i think that's more to do
with attention
i suspect but say for example if you
are looking at a bi-stable image
you can attend to one part of that image
and then have the if it's a i think it's
called a neca cube
you can have the cube flip versus if you
attend to another part it'll flip back
and you can do kind of similar
deliberate moves of attention with a lot
of bi-stable images
um so also i think there's some really
cool there is some interesting kind of
back to the
expectation thing expecting seeing what
you expect to see
a lot of that depends upon how strong
your bottom up evidence is
if you are much more likely so there are
paradigms that kind of distract people
but basically condition them into
expecting
a stimulus to appear um
and you can get kind of accidental
hallucinate or you can basically
induce people's blood what is
essentially a hallucination in those
cases
or mistakenly report something that we
know as a fact
the experimental as experimental as they
weren't there i think there are two
examples that what i have in mind at the
moment is a really clever set of studies
by john aru but i know ryan and maybe
you can talk about this
there's also a lot of work on
conditioned hallucinations from
a group at yale who i know you
collaborate with
yeah so yeah i know that was yeah
something i was actually going to bring
up
is and this is this is not yeah because
i mean i agree with chris and in most
cases i think it's going to have to do
with some kind of like motivated
selective attention
um that kind of like biases say
different possible uh interpretations
that you have posteriors over states
for the posterior to the first level um
but um but yeah definitely you can have
these expectation effects although i
don't necessarily
think of those as being um voluntary
right i'm not sure that
um like like selective attention is
definitely a kind of
controllable cognitive action whereas
shifting
uh prior expectations i'm less confident
that can be cast that way
um but but um priors definitely have a
an influence right on what your
posteriors of our states are
given some stimulus especially like
chris said when the stimulus strength is
fairly
low or noisy um you know so so some of
the work that um yeah al powers and
his group at yale and then that i've
been we've been collaborating to build
active inference models for this stuff
um is uh yeah these sorts of condition
hallucination paradigms in people's
psychosis
so the way these paradigms work is that
you um you start out
always showing people a light um and
that
is always coincident with a tone that
appears in some white noise um
and so on the first several trials
there's a fairly strong tone
that plays in the white noise every time
they hear a light or every time i see a
light
and it's thresholded so that they would
perceive that tone
uh 75 of the time um and then
and then after several of those trials
um there starts to be cases where
um the the tone is still present but
it's
weaker so they only would detect at 50
or 25 of the time
and then there are trials where the
light comes on but
no tone is played and there's just white
noise um
and what um what they have found
is that um people with psychosis um have
a higher probability of reporting
hearing tones when the light shows up
even when there was no tone
um so let's just say kind of expect so
they build up this expectation to hear a
tone of every single light
and somehow those prior expectation that
those prior expectations that the tone
will be there um have a stronger
influence over
whether they hallucinate the tone or not
um
that influence is stronger in people
that have hallucinations
than in people that don't have
hallucinations which has kind of
led to this idea that what's what's
going
you know part of the computational issue
and people with psychosis that are more
likely to have hallucinations
is that um prior expectations are in
some way
really precise and therefore going to
dominate um perception
um and that could be that could be
either because the prior expectations
themselves are really
precise or because beliefs about the
actual sensory signal
are those are believed to be uh very
imprecise
um but in either case the relative
precisions
um are supposed to are thought to kind
of favor prior expectations and
psychosis to a greater degree than
people without psychosis thank you
can i just follow up really quick yep
yeah so it's interesting that you
brought the auditory
um thing into this but the auditory
hallucinations and i wonder if
it's a visual cortex thing or if it's
involved more with the auditory cortex
because even when chris was talking
you know you think about like people
have seen like when you have two things
played simultaneously auditory tracks
that like it's like listen for the phone
number and then you hear the phone
number but then if you're not listening
for the phone number
you're hearing something else so it's
interesting that the auditory system
like the
the selective attention in the auditory
track really is
is much more apparent like where you see
the blue dress versus the
white dress or the gold dress or
whatever color it was like the two
dresses
is not so selective it's like look for
the blue dress or look for the white
dress
if you set up that expectation in the
visual system it's not as
um prevalent i think
yeah i mean i will agree that
it's definitely harder to switch the uh
interpretation from the blue to the
yellow when i've tried that
i can i can get myself to do it but it's
way more effort for you right
um and uh yeah i mean i don't know
chris if you have any ideas about why
exactly that would that would be
i mean i know cases of like you know
attention
playing binocular rivalry and things
like that in those cases i think
there are cases where i think selective
attention can play a bigger role
like the neckercube for example um
that's maybe a little more analogous to
the
kind of like uh multi uh
channel auditory input i think it just
depends on how you set the task up i'm
not sure
if the comparison is really a fair one i
suppose i think you can very i think you
definitely can
set up a lot of
expectations play a huge role in the
visual system i think is one thing to
say
um whether you have voluntary control
whether those things come under the
purview of like voluntary attention is
another thing um
but i still think there are lots of
cases depending on how you set up the
problems i think binocular rivalry is a
good one
or even something like actually
literally like where you move your eyes
i know that sounds trivial but whether
your eyes are moving around
a page or not kind of determine
determines uh some
different types of visual illusions so
if you think about um
maybe illusion isn't even the right word
but what's the where sorry we're working
on the project about this right now
what's it called again
tom's power is a paper on this run do
you remember what's trucks were fading
yeah yeah yeah if you google troxler
fading i think that's a really powerful
example of where just kind of
selective attention has a really major
role
on whether you perceive something as
present or absent
yep very interesting it's almost like
there's ambiguous and non-ambiguous
stimuli in different domains
and maybe even interpersonal variation
one person being really good at picking
up on something subtle in one domain or
not
so we'll do steven then dean then adam
i think this ties in actually to what we
was mentioning earlier
um about you know when you scale things
up and like and i agree with what you're
saying when you scale things up
it may be useful to think about how
someone facilitates the attention
of people in a group and how you take
them
and how they you think about taking
their attention it doesn't mean that
whatever they
consciously have inter-subject together
is now read by the model you know so
it's usefulness may be
in how people's attention is taken and i
think
it ties to this hypnosis thing as well
because i think your your model speaks
to top down and bottom up
happen at different level there are
different scales because often we think
top
down we think executive function and
like executive functions telling me what
i think
but like you say you can have a
subconscious level
of trying to think what something is
even if it's in the subconscious you can
and hypnosis is doing that hypnosis is
playing the game with someone um so they
they um or with these optical illusions
you say to someone
this you're looking at this cube from
above or below and it flips
but it's not that you you're being told
it's this type of cube
and your executive function's pushing it
it's it
it's still top down but it's it's
happening at
a um a more subconscious what we might
call a subconscious level and i think
that's quite interesting
so if i could just speak to that i think
there are a couple of things going on
there so
i would talk about executive function
well i mean i think it
one thing that this is a bit of a try
point but
top down is a very ambiguous term um i
think what where
so you can mean kind of that can mean
anything from basically like recurrent
loops
from higher chords from cortices that
are higher up the cortical hierarchy
um to something like top-down attempt
like a voluntary control of attention
via executive like fronto-parietal
networks or something like that
um so those are just different different
phenomena um
i think in our model control of
attention
would presumably be at if if we were to
build a model of this would be at this
you you would put the dorsal attention
network
at the second slower time scale of the
model i think
maybe ryan you can we can speak this as
well i haven't really thought about this
much
um i would have been a little more uh
like executive control network um sort
of thing i guess
would have been a little bit more what i
would have um thought about just kind of
off the top but
um yeah you're probably right i mean
visual i mean visual attention
right i mean obviously right the dorsal
attention network is
you know kind of defined or originally
yeah like linked specifically to
uh uh yeah like visual attention and
things like that or
or kind of quote unquote top-down visual
attention but
um in terms of the kind of directing
right visual attention in a
goal-directed way um
then i think i think that would be um
more executive control network for that
i mean on the hallucination point i i
did my undergrad at macquarie university
and they have a whole
hallucination group there within the
cognitive science department and so
i i just feel like acutely aware of the
fact that i don't know
anything about it um and it's also an
extremely complicated phenomenon you can
use
hallucination to like as a model of
various delusions like you can uh induce
is it called like mirror basic like
mirror agnosia where you don't
no longer recognize yourself mirror
self-agnosia or something where you no
longer recognize yourself in a mirror
like it's a really powerful tool but i
have absolutely no idea how it works and
so i would be very
kind of i think it's very tempting
as kind of modelers and theorists to
kind of go into various experimentalist
domains
like hey here's how my overarching
framework explains your thing
um and i i kind of want to resist that
um i know a little bit about visual
consciousness and how expectation all
that stuff works there but
hallucination is such a hairy topic i
just don't know
yeah i mean i would also i would also
say i mean i mean a few different things
have been brought up here right but
i mean in terms of uh it's not it's not
clear for example but
the um kind of auditory hallucination
um story that i was talking about
earlier
with um um in terms of having
relatively you know more precise prior
expectations
um you know creating a stronger tendency
for auditory hallucinations
and it's not it's not clear at all that
that kind of story
mechanistically is generalizes to other
domains
so i mean actually in the individual
domain there's this whole other body of
work
where it looks like people that have
delusions um
again as part of the sort of as part of
psychosis
right actually show the opposite
weighting
in the visual system right so where they
actually
um assign too much
precision to low-level bottom-up sensors
bottom-up visual signals you know so
they end up as these interesting cases
where they end up um
if you look at eye tracking they end up
doing um people with uh delusions
um end up actually or psychosis
schizophrenia um
end up doing uh better at certain
tasks than healthy people um but worse
at others
so like one example of this is um if you
have people
just kind of try to follow just visual
tracking fall a little kind of moving
target um then if that target switches
directions
really quickly um then
[Music]
the people with psychosis end up
actually
following uh following it better
um than healthy people um because
healthy people kind of continue to
follow it for a little bit
um after the turn and the kind of
predicted direction
um right so prior expectations are kind
of playing a stronger role
um so they actually do a little better
whereas if instead you have something
where the um
where the target temporarily kind of
moves behind
some kind of barrier um then healthy
people do better
whereas people with schizophrenia kind
of you know lose it because prior
expectations
don't do enough um to keep them kind of
following
what the trajectory would have been
right as it goes behind the
visual occlusion and there's there's
lots of other cases
um for instance in like the
proprioceptive domain where people talk
about the same kind of thing where
people with um schizophrenia actually do
um better for things like force matching
illusions
and stuff or yeah um force matching
tasks
um um and i made it this more to the
story there um but but um but people
have tried to link that to like um
delusions about agency
um and things like that so that's a just
general point being that
um that the the way that uh kind of
computational mechanism is um you know
looks like it happens in in one say
sensory domain
um can still operate very differently in
the other sensory domain even
in the same um in the same disorder
right in the context of the same like
psychosis
um so so these things don't
don't necessarily they shouldn't be
expected to to generalize
across the cross domains um is one
one point and the other the other point
was um
you know in relation to you know things
like hypnosis which
um i don't know a lot about um as part
of a
textbook chapter um i was
asked to write a paragraph or two on
hypnosis so i kind of
looked into that literature a little bit
um and it's actually pretty messy
they're
very different there are multiple
different theories about hypnosis work
um and i mean one of them you know can
relate to this idea that um
that um you know if if the
hypnotist repeatedly like gives
suggestions
that are set up such that um
they will be confirmed right so it's
like
hold out your the hypnotist says hold
out your arms and then he says
um your arms are going to start to feel
heavy and then they'll start to fall
right obviously anybody who holds out
their arms they'll eventually start to
feel heavy and they're they'll you know
heavier and they'll start to drop just
as a result of your muscles your
shoulder muscles getting tired
right so if you do a number of those
things and the kind of uh
things the hypnotist the predictions
made by the hypnotist are confirmed then
you know it could be that you're just
coming to assign
a really high reliability to whatever
the hypnotist
says right so so in that case
um if if the hypnotist just comes to be
assigned really high precision then you
can just prior expectation
adjust prior expectations in a way that
just kind of dominate
um or can end up having a much stronger
influence on what you
do and that's that's kind of one you
know one idea but again there's there's
um
several other theories of hypnosis that
just have to do with kind of like
conforming to
um kind of social roles and things like
that that you're told to um
that you're kind of told to do and i
mean anyway so
i wouldn't necessarily feel that
confident um saying much about
about how this relates to hypnosis other
than that in a broad sense
it can involve manipulating um sort of
tricky ways of manipulating for our
expectations in other in other people
but again i mean even that is pretty
speculative
i mean so if i could just quickly throw
something in another complicating factor
so even within the visual system
having a strong prior in one domain or
doesn't generalize to others this is
really great paper that just came that
came out i think last year
in cognition where they looked at
representational momentum
moony images and um
goodness i think there was one other i
think was illusory contours
and they had one other
top-down expectation kind of paradigm
and
there were large individual differences
between all of them and there were also
large individual differences in kind of
the effect of prior expectation
across those different tasks um
so i think there's just kind of a lot of
complicating fact
like moving parts and a lot of this
stuff that we have to deal with when we
talk about these things
okay we're going to return to the stack
and go to dean and then a question from
the chat and then adam
so i'll go back and be ambiguous um so
when i was looking at your
diagrams and one of the things that
really i wanted to ask this question but
we ran out of time last week
um do you think we can say that if a
person says
i see this or i do not see that
see this the or yes or no
um can we can we apply
an idea that there's a certain amount of
acceptance
and a certain amount of letting go and i
i kind of
bundle that under we reconcile or is it
something completely different i mean
how do you
how do you look at this now when a
person's actually
looking at something and going okay i do
not see the box
is it just is it that simple it's a
simple yes no or do you think there's
something more built into it
um so
how to there is a whole cottage in this
cottage industry i feel like college
industry might even be an understatement
on how to collect
verbal reports um and the proper ways of
doing it so
there's like a perceptual awareness
scale where you in some sense have
a description of the content so you have
i didn't see anything
i maybe saw something but there was no
specific content
like you have a vague feeling you saw
something but it was a bit blurry and
then you had like a full lived
experience that's one way
you can have people place bets
that's another way you can have people
do confidence ratings
lately there's been some incredibly
clever work basically looking
at so just give a shout out to people
who whose work i really admire like
hakun lao
and um megan peters have a really great
paper in e-life
where they basically look show that
people seem to have
optimal in the sense of like bayes
optimal introspective access
to their own performance so basically
when they are they will
people never behave correctly um
without kind of knowing that they
behaved correctly as it were if you
do these like very tightly controlled
experimental situations
um so yeah i think maybe i was a bit
flippant
before when i said you have to take
reports as foundational i stand by that
statement but um
there is like years and years and years
of like careful psychophysics they've
gone into being like yeah these things
are reliable
um and basically it comes down to
i wouldn't believe some if if someone
said yeah i see something
but they were getting like 51 like 50
on a forced choice task about the
orientation of gabor patch but they were
claiming they would say
i wouldn't believe them generally
speaking you would expect if you see
something your performance should
also go up that is not to say however
that you can't have um before
increased performance without awareness
there is some convincing evidence
showing that those two things dissociate
and that's kind of
what we were trying to show here right
right yeah
okay so hopefully that answers the
question yeah it does
nice yeah i noticed on this extended
taxonomy the bottom right it's like
consistent prior
high attention strong signal it's the
perfect storm
and then it's 100 seen 100 correct and
then
again kind of taking it loosely mapping
to our experiences with other
attention phenomena like if you're sure
about seeing
in it of course the way that you tuned
prior or inconsistent
prior uh these are variables that are in
the model so people can play around this
isn't like a specific
yes no but just examples of how
rich the phase space is in terms of what
the model
can do and what it can capture so here's
the question from the chat
and then it will go to adam so the
question from the chat is
any thought about the possibility of
using this model
to investigate lucid dreaming related
phenomena
like the failure of implicit
metacognition while dreaming
thank you so how about dreaming or
lucid dreaming so that stuff is super
interesting
i mean i don't think this model captures
that at all except in like the very
in like a computational sense i don't
know what task would be modeling
specifically but like we can
if we're being a bit metaphorical about
it um
so presumably i don't know anything
about lucid dreaming i presume it's a
case where basically you
are dreamings you have kind of you're
not just asleep you have kind of a
experience that goes along with it and
also you are aware of the fact that you
are dreaming
um that's really interesting i think it
would
have to come back to the
i don't know how we one would capture
metacognition in this framework
i think that's one thing to say i don't
know what it would be maybe ryan you
have some thoughts on this but it would
relate to basically
how how one thinks about metacognition
in these deep temporal models
yeah i mean i mean i mean metacognitive
itself comes in a bunch of different
flavors right
i mean so there's kind of you know
beliefs about
uh how good your memory is for example
right it can be
kind of metacognition it's you know it's
like beliefs about your beliefs or
beliefs about
patterns in your attention or there's a
bunch of
bunch of different types of
metacognition
right it's just sort of beliefs or
operations over
representations of your own cognitive
processes
so i mean the the tricky part is that
you kind of have to have a higher level
that's treating
what you chose to do uh you know in
terms of a cognitive
voluntary cognitive process that
observes that
and then infers
something about it um and um you know
the way that that
ends up influencing the
the the cognitive the cognitive
operation level
below right the way that that higher
metacognitive level ends up
um setting priors on the lower level um
i'm not sure the right way to think
about
that i mean you'd have to look at
literature on the way metacognition
affects
you know performance and cognitive tasks
um
which i'm not um i'm definitely not
one thing to say just very briefly would
just be in the discussion section of our
paper we discuss alternative models
um i think probably the model that's
closest to ours in the literature would
be
steve fleming's higher or the state
space model
um and i think there he explicitly
discusses
ignition related phenomena and
kind of metacognitive inferences about
the presence or absence of stimuli so i
would say if you're interested in that
kind of stuff and how to think about it
in a basic framework look there it's a
really great paper
yeah i mean another another one i mean
that comes to mind i know is that um
there's a paper by um where the first
author is claus stefan
um from 2016
where he talks about um the way you can
apply
um active inference models to model um
homeostatic and allostatic
control processes so basically like
anticipating for example that
your temperature is going to drop and
therefore
increasing temperature body temperature
a little in advance so that when it
subsequently drops you stay in a um
within a kind of survivable homeostatic
range
um i'm just using temperature here as an
arbitrary example of any kind of
variable internal bodily variable by
like glucose levels or or hormone levels
or anything like that
um but um they do
talk about this level a metacognitive
level that you can add
above the allostatic regulation level
that more or less tracks the
the efficacy or the kind of success
of the allostatic level um and how
if the allostatic level repeatedly fails
to keep homeostatic variable or keep
bodily variables within homeostatic
ranges then
the higher level can basically infer
that allostasis will fail
um and they show how that can possibly
lead to certain sorts of symptoms of
depression
and you have low beliefs about the
efficacy of your own allostatic
uh processes um so i mean that's a
that's a paper that i'd recommend
looking at for one example of the way
that you might might apply
one type of metacognition on top of the
basement
i also just remember the paper came out
yesterday
i shared i i sorry i forgot about this i
just shared it i shared it on twitter
yesterday if you want to
look um it came out of mike allen's
group um
i've gotten the first author's name i'm
really sorry about that um
but uh they explicitly discuss
like predictive processing and active
inference theories of consciousness in
relation to introception
and metacognition and they have a whole
discussion of this type of thing so if
you're interested
maybe just like check my twitter page
or at mike allen's twitter page
sounds good um we'll go to adam and then
anyone else who raises their hands
hi um perhaps tying a few of these uh
things together
um i was wondering if with respect to
hallucinations and
psychosis and forms of delusions if
maybe
um some of it you could potentially
model it in terms of um
not having access to
mental acts so which might have like
associated efforts copies
that could potentially like be adjusting
precision
and or also having uh different
components of
the associated mental act which you may
or may not attribute to you like some so
like
aspects of enteroceptive inference that
could lead to senses of like
willing or ownership but then
by not having access this potentially
where the access itself
uh of the action generation
could um basically adjust what you're
how you're attributing um
what sense you're making of the
associated perceptual
events so it's like um how did i say
this so it's like
if you're uh talking to yourself in
thought or something like like thought
is in her speech like vygotsky
uh let's talk about like well if you
don't have access to like
the generation part and for some reason
i don't know how much it can be
separated but then like the voice might
just like appear to you
in a way where you don't have a sense of
ownership if there's not like the right
type of like
maybe intercept of coupling to the
genera generation process or just like
a lack of metacognition to contextualize
it um
anyways yeah i really like this idea i
mean one thing
and one thing to keep keep in mind here
is that you know the
the the sort of thing that you're
talking about
when people have sort of different
experiences
of or were there a different contents
and experience i mean basically that's
where you're talking right different
contents
that can be inexperienced those
those are just in a model like this
going to amount to different sorts of
state spaces
that you can infer posteriors over
right so you know you can have beliefs
about
how much ownership you have over your
body or you can have beliefs about
something going on in your body
interreceptively
and all those things are just gonna be
you're gonna have
some sort of afferent signal and you're
gonna
have some prior expectations obviously
and then you're going to infer some
posterior over whatever the contents are
of the thing in question right so so
anything along the lines of what is the
what is the
content of one thing versus another is
just going to amount to a particular
level in a model
that infers posteriors over particular
contents
right so none of that is going to have
to do directly with
our model other than the fact that given
posteriors over any content
um you know if our model were applicable
to that
you could just treat those contents as
the lower level right so you'd have
inference over
some content and then our model would
say something about
um the processes that make that content
conscious or not
right or consciously accessible or not
so so the only thing that our model
might be able to say is
if you swap out the you know
square versus squares versus lines in
our model right uh whatever the beliefs
are
at the lower level you swap that out
with representations of some other
content
whatever whatever it is you're
interested in you know something about
the body or something about um what uh
you know what a pattern of what sequence
of the
speech right that you're hearing or
anything like that right what
what word you just heard um you know
swap that out as the content of the
lower level and our
our model might be able to say something
about the processes that determine
whether you
whether those contents become accessible
or not but beyond that our model doesn't
have much just that
yeah i mean if i could say something on
that as well i i really like the idea i
think just
along similar lines to ryan because it
just casts like
decisions about ownership is just having
access to some content or another and so
for me
like the essence of any type of
conscious access
or awareness process is basically
whether it's
integrated into this temporally deep
representation
and in doing so available to all of
these sub-processes
our global workspace theory um
and so i think this kind of relating
this to kind of the metacognitive point
i think this is actually a spot where
maybe this is a difference between
owl theory versus an active inference
theory
that gave an explicit role for
metacognition
um so for me it's just the fact that you
can be aware that
it is you're aware of it because it's
integrated into this representation
right
um whereas maybe higher order person b
no you have to also infer
that you are seeing it or that i am
seeing it or something like that
um and so i i
um i think there's actually like really
interesting empirical questions that
you're
what i'm going to say um but i i hope
that we can kind of
i don't know maybe it would be nice to
see
a discussion of kind of active inference
theories of visual
of metacognition versus active inference
theories of like visual awareness in
general
yeah i know if you i know you've written
a lot about kind of different theories
of consciousness adam so i know if you
have any thoughts about that
i mean i know that um you know there's
this preprint um
by um the first the first authorism is
smith
lars um well i can't remember
uh uh his first first name but
but uh but his last name is smith um
that
that um does propose a a type of
model of medic dog mission cognition
there's
in theirs attention works a little
differently than in ours but
essentially you do have a second level
that controls a precision parameter
on the um on the first level and then
there's a third level in there
that infers things uh about um
control of uh the control of the
temperature parameter at the first level
um if i'm remembering right um and they
use it
as a way of the way they talk about it
is a way to think of um
like meditation and mindfulness and
things like and things like that
um which i'm not you know i don't
remember enough detail to
to say a lot about you know my my
specific feelings on that but
that is a an example that i'm aware of
uh
again it's just a preprint at this point
but um
of another attempt to try to model um
something like metacognition
cool interesting questions adam did you
want to say something else yep go ahead
um yeah so um
i basically want to throw your model at
everything
but um in terms of uh metacognition and
what i've worked on in the past mostly
i've been focusing
on like trying to cross-reference
various theories to see the points of
like overlap and non-overlap
mostly considering like accounts of
dynamic modularity that might apply to
a global neural workspace architecture
or like integrated information theory
where you can think of their
complexes of integration those modules
as themselves being like
do an iit handling of those and seeing
like where's the overlap basically
trying to give semantic content to iit
um
via like gnwt is like an architecture
for bayesian model selection
and the whole thing kind of being
adjudicated by energy principle
and mostly an active inference not
nearly the technical depth that you have
i'm only beginning to move into things
like metacognition
and uh like higher order forms of
consciousness
and the ideas are like really uh
speculative like so like one idea is
that like
as you're like um let's say
um imagining like enacting something
you might start out from like generating
like experience from an egocentric
perspective
but then this enactment would
auto-associatively
also have third-person allocentric
representations like
from like the ventral visual stream or
something like this like you've seen
people or yourself doing similar things
and so you might then like be able to
get access to in the mind's eye this
like third person point of view on you
with some unfolding
like some sort of like moving back and
forth between
a first person like i guess and the
models i'm working with like
phenomenal consciousnesses all and and
accessible consciousness
there's a sense in which like in a
rudroff um uh
projected geometric modeling it's always
from this first person essential point
of view but then the idea is
you then are looking at an objectified
you
and this would be part of metacognitive
awareness and contextualizing you
in terms of like you doing actions and
then this third-person
little homunculus doing actions that
you're seeing in your mind's eye and
moving back and forth
that's like the basic space i'm moving
into i don't know how much of that's
going to work or
or how you would model that well i mean
like one thing
just kind of kind of kind of um i mean i
mean again just to just uh i mean when
you think about this
kind of informal terms right then then
and
if you're in some sense um
if you are the content you're describing
as a belief
that you are doing something right
um so that's just the content in the
state space right
so same kind of thing right swap out our
lower level
with the state space that is beliefs
about what i am doing right
then it's just the same thing right you
have a representation about what you are
doing
and in our model you would either
um you would either gain access to the
representation of that content or not
via its integration with this deeper
temporal level
um granted beliefs about what i am doing
you know or not is already right pretty
pretty temporally deep um but were
those sorts of contents to apply to our
models and that's what it would say
it would say that um those contents
need to be integrated with this deeper
temporal
uh model that is able to form
posteriors over something that
incorporates that
um and uh so again i mean at the end of
the day really it really just comes down
to this distinction about the content
being represented
and whether or not the posteriors
associated with that content
get integrated with the with the higher
with the higher level
that does the sorts of things that the
higher level
described here can do
so so it's just a question about whether
something like that is the content
that you want to be uh using in a goal
director we are recording
um or or or whether
just uh just representations of the of
the lower level kind of
visual content right and that being
integrated with this level is
is what's is what's involved so it's me
again this just has to do with different
levels of representation and what the
contents are
that you're becoming conscious of um so
oh and by the way i just just uh
um i just mentioned i looked up the
paper i was mentioning
um so it's it's called towards the
formal neurophenomenology of
metacognition and i'm the first author
is lars sanbed
smith um just to um
do justice to uh uh remembering who the
first author's full name was in the name
of the paper i was talking about so
um sorry i think i think you started
saying something at the same time chris
yeah christopher's then adam
i was going to change the topic very
slightly but i i was wondering
so how you think about phenomenology or
phenomenal consciousness because to me
it comes down to the nature of
the representation that you're gaining
access to so to talk about like
you talk about the projective
consciousness model which is really cool
work
there this perspectival nature of
consciousness comes from
the structure of the generative model
and the fact that they're using this
projective geometry and that's built
into the structure of the generative
model
i'm just curious about how you think
about this and how that kind of maps on
to iit because at least as i understand
iit like phenomenal consciousness is
kind of a
i i've never really been clear how the
content of consciousness fits into iot
for me
like it's all uh
um anyway yeah i'm just be interested to
hear your thoughts how it all fits
together with like global workspace
theory
like um yeah i would say there's some
kind of giant begged questions in iot
um i think though it's not nothing
that they start from um axioms of what
they think should be part of
phenomenology
and then work their way to this sort of
way of handling systems
in terms of i think it's a decent prior
for like what we should look for in like
physical substrates
i wouldn't like completely like throw it
off but they then would say
if you have these axioms that
characterize experience some
intrinsic existence uh composition
information uh integration exclusion if
you have these uh
different properties then it is
sufficient
to bring about phenomenality because
they started from phenomenality
oh no i don't think that follows at all
um that being said
um i think it does potentially like give
us some prizes and trying to think about
physical and computational
substrates of consciousness so that
would be like the cross-referencing
and then the other part would be like
how do you think so if you're thinking
of
global neural workspace as like
potentially like a trading off
of modularity as being part of the
physical implementation
well then the question's like so when do
you have like larger big modules
functioning as like
dynamic cores or workspaces and when do
you have like more fragmented like
local processing so like in theory you
could get like um
bayesian model selection with like
discrete updating with like a bunch of
like
small beta complexes close to the
modalities
or it could be like this big sprawling
alpha complex that's like
going that's multimodal and all these
different ways
but then like you're moving back and
forth between these like degrees of
synchrony
seems like iit could potentially be
useful there for
describing that so that was one of the
ideas of that in a relation
um in terms of like kind of bringing it
to rudroth
like for me like the object i would want
that would be like potentially a
minimal condition for phenomenality
would be some sort of
um joint uh distribution over
your body pose and visual spatial
awareness
um as like the minimal thing for me at
least for human-like consciousness and
like
a series of um basically
roughly at alpha frequencies a series of
estimates of that
and and and then and thinking of this as
iterative bayesian model selection
via a global workspace architecture but
not necessarily one where there's like
access
that's like a more sophisticated kind of
consciousness in terms of you wouldn't
necessarily
i would call it like it's pretty darn
global you have something like spanning
all the posterior cortex
but it's not the kind of work space
you're dealing with where you're
actually having knowledge
and access
thanks adam so if anyone else
wants to they can raise their hand
otherwise
i think there was a very good request
just you did just ask them so let's
mix it up but um there was a very good
request actually if
uh ryan or christopher you could just
look at this part of the figure which i
know is a structure we walk through in
the model stream as well
and just kind of map some of these
bigger ideas that we've been talking
about
to some of the letters just in a way
where people can now look at this
outline say okay the experiment i'm kind
of on the page we talked about a bunch
of visual and interreceptive
kinds of experiments just where did it
map in this
paper so that people will always be able
to go back to this paper
look at the code and then kind of map
some of these
bigger metaphors to the experiment that
you did here
um do you want to take this ryan or john
i don't
mean either either way it doesn't
doesn't matter to me
[Music]
go for it um so
how how detailed you'd like me to go do
you like me to explain what the little
square what the d's and a's and b's and
s's are and all that stuff
let's go for all the letters on the
right side and maybe even some on the
left
all right so this is a
partially observable markov decision
process and it's a hierarchical one
so at the let's just focus on
essentially
let's start at the bottom
o's are observations
and s's are hidden or latent states
and what the a matrix does is it
provides a mapping
between those two things so circles are
random variables
and the squares are essentially fac uh
functions
in this case probability distributions
that map between those two things so
the a little arrow going down just says
that that's essentially a
with that little a superimposed on arrow
is basically saying
this that's expressing a conditional
probability distribution saying that
o observations depends upon the hidden
state
now as we start to evolve through time
we need transitions between discrete
hidden latent states in the world
and those are what's described by b so
this is something like
what is the probability that at time one
uh what's the probability of each hidden
state at the next time step
and it will describe kind of s at t
conditioned on s at t minus one
now then what's special about
the hierarchical models is that you have
another layer
on top of that um where
state hidden states at the first level
are now being treated
as observations by the second level
and so the posterior probability at the
first level
is basically acts as an observation
um for the second level a matrix
um and then kind of at the second level
there should be a d at the first level
too but
that's fine um basically what this prior
what this
second level hidden state does is it
provides
a prior over that first level
and then at the first level you can then
have basically we just have one time
step at the first level
um but you can have any amount of time
steps as you want
so if you imagine the metaphor that's
often used is like
uh the minute versus the hour clock on
the hand
they're evolving at different time
scales um so you could in this diagram
we show that the second level evolves at
two time steps for every one time step
at the first level
at the second level sorry um
at the second level there are again
transitions between these latent states
and that's also where we have policy
selections that's why we put it up there
so policy selection is essentially if
you imagine
a whole series of hidden markov models
this is my favorite way of describing
policy selection so these hidden markov
models are basically just
a partial observable markup decision
process without the decision
aspect if you imagine a whole series of
basically these graphs
and you are deciding what graph kind of
is going to be my future
you are trying to find the graph with
the highest model evidence
that is what computing doing policy
selection does
so you are choosing the transitions
that will take you to basically the
graphs of the highest model evidence
uh i know that brian you want to kind of
clean up some of that explanation
we're at the shoulders let's
go to the last few variables yeah
i
just like chris said right close it's
just your distribution over
policies um g is the um
expected free energy um so that's the
essentially the the function that
decides
right which um what the value is you can
think about it about each
each policy and that is with respect to
c which is um your preference
distribution
which is which is essentially the the
thing that specifies which observations
you want and which observations you
don't
um now um somehow i see
that an e has been placed with an arrow
down to g
um and that's not correct um e should be
e should be going you should be going
straight to pi
um if you're going to include e
um i don't think we did anything with e
in our model so i don't think e needs to
be there
um but um but e if it's
used is just a kind of separate prior
policies that can encode something like
habits um
so it competes with the expected free
energy g
over policies um to infer what to when
you're inferring what the posterior
river policies
is um so uh
so yeah i mean otherwise i feel like
chris uh i feel like chris described it
well i mean you know it'd be a little
it's always a little easier if you have
like a
you know the if you're in control of the
pointers you can actually
you know point to uh
i think you also asked us to relate this
to an experiment to her paradigm
so if we maybe briefly click down to
figure two what you've labeled as figure
2 there so we can just look at that so
the idea here is that there was
a forwards mask
at the beginning of the paradigm this
was just a series of lines and there
were these kind of stimuli on the
outside
at the second time step in the task the
original like simulated task
they on some trials the square kind of
was
self-organized the sum of the lines kind
of self-organized into a square
so i either in our discrete state space
model a square was present or it wasn't
and in the third time step it was just
replaced by more lines
and then afterwards we asked the agent
to construct a report
of that so basically at
you can think of the first level of the
model as
being all the features of the stimulus
and also the location
of attention so this might be something
like saliency maps in posterior parietal
cortex which are directing where
attention is being pointed to
you might have and then you might have
the features of the stimulus which are
represented in various places
at the second level we now have our this
is basically our fronto-parietal
cortices
this is tracking the evolution of states
at the first level so it's
tracking that at the first time step
there was
lines presented at the second time step
there was
a square presented maybe it maybe it was
maybe it was present maybe it wasn't
and at the third time step there was
more lines and you can imagine in like a
real task all of that unfolds in a space
of about a second
yeah so you can think about it i mean
like
yeah the second level is really the the
content in question that it's inferring
is
is the sequence right it's not whether
the square
it's whether it was lines square lines
or just lines lines lines
um and so it's another
and so if you're thinking about where
experience lives obviously we don't
experience a sequence right
i think and i think ryan i've been
chatting about this a lot lately because
it relates to work we're currently doing
but i think what's going on is that what
we experience are essentially like
the updates to our second level beliefs
and that's really crucial so the reason
why it's crucial is because
we know empirically that kind of what
could be
we might describe as brain processes
they're at the first level
of the model these can be either
conscious or they or not
um and contents that are
conscious when you are conscious of
something it has all of these really
important functional consequences
so here it might be kind of being able
to see it for report
maintain its report but also if i see
something i can then voluntarily
maintain it in memory for as long as i
want as long as i don't get distracted
like there are limits on like human
psychology um
but that that's kind of a really
important function that's enabled by
being conscious of something
right and that allows us to do things
like construct reports of our experience
or even i i think by report i just mean
something very general
it could be in this model we kind of
have the toy thing of being able to like
put a sentence together
but it could also be more more
empirically real
um in terms of empirical paradigm will
just be like hitting a button
or doing a confidence tar doing a
confidence interval or something like
that
cool thank you for that interesting
answer
we'll have um stephen and then adam and
then anyone else who wants to raise
their hand
and also any last questions from a live
chat as we kind of
slowly land the plane
yeah um i was just going to ask in
relation to those lines and the way that
the square
appears like you said so this this is
actually like a graphic representation
but when someone looks at it
there's probably some special device
that you've got that represents this is
it like
that the lines rotate um to be
and at some point and it just happens
they rotate such that they line up and
then they un-rotate or
and just one other question is why
didn't you use negative space
like you like say they line up to make
you know like a
a negative space square i just wondered
whether that
relates to the choice of how it pops in
and out of
perceptual punch sorry phenomenological
awareness
phenomenological consciousness or access
consciousness
um so basically this is just a very in
our model
we have discrete hidden states which are
categorical distributions
which are lines or squares
and external states which are red and so
this is kind of just a graphical
representation of a way to think about
that but it has
really nothing to do with how it works
mathematically um
then in terms of actually the empirical
task
like this is this is a task that we
basically like borrowed from michael
pitts
um who's a really done he's a cognitive
neuroscientist on a really important
work in the area of visual consciousness
and as for why they chose to kind of
have these i guess the i think
from memory there are videos attached to
this paper from memory i think the lines
just kind of
they jitter around and then occasionally
a subset of them
will all line up into a square and then
go back to like jittering
um as to why they did that versus other
methods like
i don't know really they definitely are
subtle things you can do to a stimulus
which have major impacts on whether
you're
conscious access to it or not but the
phenomenon of the inattentional
blindness is super general
like these are you can have people so
the really famous example is
that everyone gets shown in like
undergrad psych is the
ever up there's you have your tracking
whether a group people playing
basketball and you ask how many
how many times does someone like a white
shirt get past a ball or something like
that
and your attention is distracted so kind
of consumed with that
that uh a bear or a gorilla
can like walk into the middle of the
screen being the dead center of your
fovea
wave at you and then walk away and then
about 50
of people don't see it at all um and
that's really well replicated across a
bunch of
um or they don't report seeing and i
think i should say i think there's some
there's some debate about whether this
is a memory phenomenon or any of that
there's lots of subtleties there but
um so hopefully that answers the
question yep oh
also one advantage and one rationale for
these pure
modeling papers that we're discussing
today is
the space of the possible human
experiments or even any other kind of
real world experiments
is very limited it's very limited what
you can actually have
a real set of humans do and so
it's great to have tools that help us
explore
some of the patterns that we're looking
for and understand
how variability and do statistical
uh calculations like how many
participants might we need of a given
uh variability range if we want to
capture such and such an effect without
distorting it this way that's critical
information and if you don't have the
model
then the experimental design phase is
totally blind
and it's a very um shot in the dark and
so this helps
inform structures for even thinking
about
how to design human experiments for
example
as we're talking about here with visual
awareness but it could be for other
kinds of experiments
so adam and then anyone else who wants
to make a comment
see you later alex bye adam
uh hi um i'd be curious in uh
knowing more of your thoughts on the
potential i guess uh
richness or lack thereof of experience
so like at one point like
could consciousness be phenomenal or
access
more experience as a series of snapshots
that are like static sequential but we
don't know it like a flip book
or is it more like a continuous stream
like
if you're getting this discreet updating
are these updates over like
like the agent and like motion like if
you take like a camera sometimes in your
phone there's like a little brief like
forward head like look ahead and back
but like
what would be the nature of these uh
discrete updates
yeah i mean i know the like i'm trying
to remember
i know um and i remember reading um
dana hans uh book um a few years ago
and there is there is some work i think
showing
you know there are kind of there's like
a minimal time for like
essentially updates to the um to the
content
of consciousness to have some kind of
discrete character to them i don't um
i don't remember what psychological
refractory period
yeah do you know what that do you
remember the actual like milliseconds i
can't remember
like 50 milliseconds or something like
that yeah i don't i don't remember a fan
but there is
there is something you know like that
maybe might be
you know like similar to like a refresh
rate or something like that
um but i yeah i don't remember too much
about that off hand
um but but i mean one thing you know one
thing to say
is that um you know because you know
there are these sorts of discrete
updates in our model but i mean it's
also good to remember that the
the higher level representation is
specifically about this
um sequence right um which is
integrated in a sense that the
hypothesis is about a whole sequence
that doesn't necessarily need to be
thought about as having sort of discrete
chunks to it right it's just this tingle
uh just a single hypothesis about what
the what the
whole sequence was and so you might
think about that
right as having a more kind of
continuous character to it despite the
fact that
it's it is updated in some ultimately
discrete
fashion you know and kind of these
really fast bins um
you can think about it that way um but
uh
but and in terms of richness i mean to
me i mean i just think of
i i just tend to think of rich as
meaning
there are more precise features right
there's more features that are more
precise
um at the at the lower level right
so instead of just you know a lines or a
square
right at our you know in our example
um there could be a ton of different
lower level representations
about color and shape and size and you
know all these sorts of things
um that are represented
in some sort of joint way right and
become accessible
um and and so i mean that's one way to
think about richness is just what
what are all the things being
represented that become access
that become accessible um together um
but i don't know they used to ask a
question actually there about the
continuous modeling
is it possible that active inference
could have a continuous
mode um i know that it would get rid of
a lot of the discrete benefits and the
sequential message passing or maybe
other
heuristics but could there be a
continuous format continuous timer space
yeah there are continuous state space
models and there are also mixed models
um you know mixed models are kind of
especially nice and probably a lot more
realistic
here um you know because visual visual
input
a lot of the things that are represented
by the visual system are continuous
right like uh motion for example is
continuous
brightness um you know all these all
these sorts of things
um and so those can be those can be
um perceived and represented
in a continuous scale at the lower level
but still get
passed up to dispute representations at
the higher level
um we didn't do that here for simplicity
but you could
sorry um i was just to clarify
i was in scaling active inference we did
talk about the continuous state space
i was just wondering if it's possible to
have a continuous time
active inference model rather than a
discrete time model of t123
just just bringing it up okay but then
christopher and then blue
so yeah three things so just quickly to
answer your question daniel
um so hidden markov model is just like a
super general thing it's basically just
when you have a markov chain
and but you have but each state of the
markov chain
links to some outcome those outcomes can
then both the outcomes
and the latent states can be continuous
when you have a discrete latent state
continuous outcome you end up with a
gaussian mixed
with like basically what ends up being a
mixture of gaussian's model
um and when you have if you have
continuous states you end up with
uh i think you basically end up with a
kalman filter
and you can stack those on top of each
other and do all the same things it's
just
yeah for all the reasons you say things
get really complicated when you start to
move to continuous time
and um
but i completely agree with ryan i
actually i think there are
computational there are functional
reasons
to think that decision making is
discrete and so at the decision making
the level of decision making
computationally speaking we should use
discrete state space models
i also think that at a certain level
we need continuous state spaces
obviously we represent
continuous quantities and i think thomas
parr we've chatted about this before in
the model stream but thomas par has a
really nice paper on kind of the
discrete continuous interface and that's
something i'm actually really interested
in i'm not sure
i don't know to what extent we should
take these things as
idealizations or as um general kind of
neurophysiological predictions i think
that's a really
i'm super interested in that in other
words but i don't know
another thing to say though is that it's
not as though
only um only
action you know only action selection
has to do with
um discrete state spaces there there are
possibly a lot of
higher level um representational things
that are also industry so for instance
like concepts
right like i can i can have a bunch of
continuously represented lower level
visual features
but i can use those to infer something
discrete as well like for instance
that those features correspond to my
concept of a dog
right or my concept of a banana or you
know whatever
right because we do have these discrete
categories that we map on
patterns of continuous features too um
and i mean that's a that's a kind of
whole another discussion i think we
talked about abruptly last time right
gaining conscious access to the visual
features versus gaining conscious access
to the fact that it is a dog
right so those are different levels of
representation that
can be attended to and you know may be
able to kind of
uh independently or semi-independently
be accessible
um separately um
so but that's just i just want to point
out that not everything
not everything is going to be continuous
um
in in perception when when sort of
passed probably
and that's where yeah in fact as you can
see that's where a lot of category
theory discussion
comes into play let's do blue then
christopher for
final thoughts so
i i know like we operate under the
assumption that uh the visual like we
perceive
things continuously in visual space but
i mean really the input is like 60 hertz
right so
i mean theoretically like this thing
this object is consistently a dog but if
it's like flashing back and forth to a
cat
at sub-perceptible levels like we
wouldn't know right so so i mean
i think anything can be modeled in
discrete um
chunks if you break the chunks small
enough pieces
yeah yeah i've sometimes seen people
like
make be a bit smarmy about this when
they
um someone says like oh discreet state
space is unrealistic and the comeback is
always like mate like
you can always discretize things up to
some arbitrary level and then discrete
state spaces work fine
um i know i actually think that's a bit
of a dodge to be honest because the way
we're using these discrete state space
models is in like an ultra discrete kind
of way right
so i think that if we had like if we had
a hidden markov model
where we had like
six a 60 hertz equivalent or something
that would just be ridiculous like you
should just work in continuous state
spaces at that point like
the the the computational and conceptual
advantages of working in a continuous
discrete state space are gone it's
so much it would be so difficult it's a
really nice
question though and it's like if you do
make it a finer and finer granularity
you keep some of the really big benefits
of splitting and sometimes it's actually
easier to even do like a protein folding
they'll do a time step of the tiniest
tiniest amount
and do millions of time steps are tiny
because it's still
easier to fit that ultra rich
discrete time model with actual time
steps that can be
clustered on different computers rather
than
re-write the whole base to do continuous
modeling so i agree
it's not like continuous is simply
better and
it really relates deeply to how we think
about the continuum and the
infinitesimal
and so it's really an interesting area
for active
so steven and then any other closing
comments
yeah i suppose if we also were to go
back into the physics of it
you know with active inference as a way
of like if vision is
feeling the surfaces out there
rather than it being an input signal
even if we have these brain waves some
of that might be an artifact of
cognitive science which has got like the
input process
output at some level it's it's
extracting like alex constant talks
about
extracting you know information
from quantum noise noise
you know random fluctuations and all
this sort of stuff so
you know there's it could be it could be
that discrete
state space is kind of you know
sort of also because there is quite
choppy what's coming in
and at some point inferences have to be
made that makes it more like a signal
if that makes sense now i'm just i'm
just putting that out there just to
that as another layer at the lower
levels of the retina and stuff like that
good any last comments otherwise this
was super
interesting i guess a closing question
for the authors would just be
when when's the next uh episode in this
paper saga
or what's the next what's the next thing
you're excited about here
um we have we have another paper that's
kind of i don't know maybe like
three-quarters done or something like
that that's kind of the
next
yeah so they're done it's an expanded
model that
does a lot more with um so it allows for
a no report
paradigm and um selected selective
attention and working memory maintenance
are our explicit
policies um in the updated one there's a
number of other advantages but
you know it's coming soon yeah i think
it's a matter of uh
me riding it really sorry
wow too real but
thanks everyone for joining this is
really fun for
18 overall and we look forward to
probably seeing you again for 19
and beyond thanks to all the
participants you can
fill out the survey for feedback in your
events
calendar invitation otherwise
we'll uh be talking through other
channels so thanks everyone
see you later thanks
