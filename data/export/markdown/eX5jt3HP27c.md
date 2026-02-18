---
title: "ActInf Livestream #028.1 ~ “Towards a computational phenomenology of mental action""
category: "Livestream"
series: "Livestream_028"
episode: "1"
duration: "1:51:00"
url: "https://www.youtube.com/watch?v=eX5jt3HP27c"
views: 298
exported_at: "2026-02-18T22:37:37.873963+00:00"
format: markdown
---

# ActInf Livestream #028.1 ~ “Towards a computational phenomenology of mental action"

hello welcome to the actin flab live
stream number 28.1
it's september 7th 2021
welcome to the active inference lab
we are a participatory online lab that
is communicating learning and practicing
applied active inference you can find us
at the links on this page
this is recorded in an archived live
stream so please provide us with
feedback so we can improve our work
all backgrounds and perspectives are
welcome here and we'll follow video
etiquette for live streams
today on september 7th and next tuesday
we're going to be discussing this paper
on computational phenomenology then we
haven't set the paper for 29 yet and
then we have a few papers set for
october
today the goal is just to
learn and discuss this very cool paper
towards a computational phenomenology of
mental action
modeling meta awareness and attentional
control with the parametric active
inference
and we're really appreciative that lars
the first author is here to discuss with
us
so we're just going to
start wherever we start and go from
there i guess i think each of us here
probably brought some questions and
anyone who has a question the live chat
can ask it
so let's just
introduce ourselves um
[Music]
and end with a author and go from there
so i'm daniel i'm a postdoc in
california and i'll pass it to dean
good morning i'm dean i'm
retired i'm in calgary i'm in canada and
the work that i do
ties in nicely with this idea of being
able to
bring some precision to how we learn
so
i will
say who can i pass it to so dave um
david
he's usually on mute yeah he might be on
text-to-speech mode which is fine
right but um
welcome dave and we'll pass to lars so
lars welcome to
this discussion and just thanks again
for joining we're
happy to hear any introduction
and then we'll go from there
yeah sure well thanks excuse me thank
you thanks for having me i'm kind of
excited to be here it sounds like a fun
couple hours ahead of us um uh
just sending regards from the other
co-authors as well obviously like a lot
of these papers this has emerged in
collaboration with uh other people and
they couldn't make it here today so
um but i'm glad i'm able to be here so
my name is lars um i'm based at my
affiliation is with the university of
lyon in france i'm doing my phd there
and my focus is
explicitly on meditation actually
and that's
what i'm interested in is what brought
me into academia i had a first stint in
academia in physics
a while ago and kind of left it and went
into corporate stuff for a little while
and then it was drawn back in by i'm
disinterested in in meditation sorry
there's a bit of background noise i
don't know if you can hear it
but um
yeah i'll i guess i'll leave it at that
the the kind of genesis here
was from that from that angle through
meditation and ending up in in carl's
lab and
and asking questions around the tension
and and meta awareness
um through that lens of of practice and
that's where this kind of paper emerged
from so
we'll get into that a little bit more
detail
and where did active inference come into
play
was it from something you were learning
about from
that practice perspective like you
mentioned or a theory driven perspective
or did a collaborator bring it to the
table
it was a collaborator so i
i i sort of came into
computational neuroscience
um looking explicitly to contribute to
the field of meditation research and so
i'd reached out to a lab in lyon
one of the co-authors um and uh joined
the lab there and they had a like an
ongoing
uh relationship with uh carl frisson's
lab
because jeremy matu is one of the
co-authors here uh did his postdoc over
at ucl
and so they had a bit of an idea for an
attention project um uh using active
inference and i kind of came in not
really knowing very much about it um but
you get to learn and then i was sent off
to
london with a pretty open
blank check as it were of like see if
you can figure out how to apply this to
meditation and attention and we had some
some some directions that we were
thinking about but then what ended up
emerging was this uh hierarchical sort
of deep parametric uh um stuff
ooh interesting how it kind of came to
yeah
it really was right right right place
right time they were looking for
somebody
the physics background with an interest
in meditation and uh computational
neuroscience and i sent them an email
and
that was pretty much the extent of the
interview process and off i went
cool well welcome steven um dean or
steven if you have a question you can
raise your hand or of course anyone in
the chat
um
maybe dean did you uh want to talk about
a crosswalk or something like that that
yeah i want to do that later but i don't
asking so it's fantastic to get the
background about the meditation piece
because
when i before i picked up the paper what
i was wondering about was how
precision plays a role in learning and
especially when you're moving from novel
contexts and trying to familiarize
yourself with something
and so for me
my
my curiosity was around the idea that
when you have the simple model
and then you move to these um
more nested paradigms you're kind of
moving from the unplanned because you
can't plan your perception to the plan
the idea of being able to think about
your thinking
and so that transition was what really
fascinated me so now that you brought up
the idea of meditation i wonder how
meditation goes from the unplanned to
the plan so you've opened up a pandora's
box for me because now
my original question is kind of now i've
been taking down this tangent so i'm
curious right well i mean i can speak to
that a little
a little bit um
the
the the the idea for me going in here
was to
um
see i mean just intuitively as soon as i
got familiar with active inference there
was a
um a resonance there in terms of how
the maths seems to echo a lot of
the
kinds of ways that people talk about
practice in general there's this sort of
balance between
um you know attention
and the the
the
that our perception is this this
combination of prior and observation
you know that idea and like how these
two things are balanced and and getting
into um the optimal space there is very
very
close to you know if you start thinking
about mindfulness obviously is a way of
paying attention and increasing the
impact of the sensory observations but
then also things like
um
don't know mind beginner's mind uh this
kind of fresh
kind of uh stance that is very common in
zen but in other in other areas as well
and so already there's this kind of like
oh there's something there's something
here um and
so i arrived at
carl's lab and and what i started out
with was just getting familiar with the
attention literature
because that's
at least you know the a good way in for
meditation because at least in the very
beginning that's what it's all about and
in some ways it's about that right to
the end but um so the question was uh
you know how do we
uh talk about paying attention um within
the
already and i was really fortunate
because i was kind of coming into the
space
uh when all the scaffolding and the
maths i needed to start talking about
this in a more
practice related way or a metacognitive
way was already there
all it really needed was somebody to
come in and ask a question that was for
me phenomenologically driven
which was
in
meditation
you are
paying attention for sure right you are
deliberately paying attention to some
object you know traditionally the breath
but really the aim of the game
is uh or an an additional part of that
which is really really important is
being able to monitor where your
attention is
so in other words being able to pay
attention to attention
and so that's where that kind of shift
happened right you mentioned like
thinking about thinking it's like well
okay so if we know some of the maths
about you know what it means to pay
attention
um
what would it mean to pay attention to
attention and what would it mean to be
able to have control over the
intentional states and how would this
how would we
make that an allowable thing within
within the framework
um yeah so exactly the deep affective
framework kind of set the set the scene
for that um and casper casper tells work
sort of gave the gave the hint and that
was on a different precision in the
model and here we're just talking about
likelihood precision and then that kind
of created this
this um
opportunity then right that then becomes
almost generalizable across and that's
and we can get to it a bit later but
really what i'm more excited about in
this in this
uh whole work and
paper really is what we start to hint at
at the in the discussion
at the end um pointing to the fact that
we could generalize this across
precision throughout the model that
could then be interpreted in as
different forms of mental action and
what that might mean for
understanding
yeah i mean
it gets broad at that point yeah
awesome thank you for the summary and
welcome blue at all
at feline
so stephen with a raised hand and then
any live chat or anyone else with a
raised hand
yeah welcome um
yeah i was i'm really curious i like the
what you're saying about the
generalizability or the potential for
generalizability and you're
sort of extending beyond neuro
phenomenology
to phenomenology in general i suppose is
a name
i'm curious how how you see action
potentially coming in with meditation
because you talk about sort of
reflecting on mental states
like breathing is an action i suppose
but in many cases
they use
meditation because you're
reducing the amount of action that's
happening in the amount of visual
stimulus because of often the eyes are
shut you know bodies contained and
um and now i see that you know okay so
how does this then come back into an
action state and i know that there's a
kind of in between with like i know
vipisana type meditation on the body
senses or
like you mentioned the breath but i'm
curious how you see
that kind of
inactive piece starting to come in
through this
no thanks for the question and it's a
really central one
um because
i mean i guess to give a little bit more
history to
the this paper there was this is also
building on a little bit of some of the
intuitions of previous work by
antoine jeremy and another collaborator
giuseppe pagoni um and they wrote a
paper called
on the epistemic value of inaction
uh which speaks to this this point
um i think
to
in the begin off from the from the
outside we can kind of separate you know
mental action and over action
and meditation you know you're putting
yourself in this situation where you you
know deliberately don't have that much
over action right you're sitting still
um and yet you're doing things you're
definitely doing things with your mind
um even sort of
do nothing meditation is still a kind of
doing in a sense um
although it gets a little bit sticky um
but the
for me
to answer your question
the
the cessation of
overt action
puts you in this
highly epistemic
state because now the sort of
self-evidencing side of the equation
you're putting yourself in a situation
where
that is harder to
access so that
um
you
you no longer can fulfill your
expectations through you know action
acting in the world right so like um
if you were to sit down and start
getting um
agitated or bored
rather than the sort of fulfilling the
expectation there that you shouldn't be
bored by going and doing something you
have to stay stay bored and there's a
certain discomfort that can arise from
that and then
the role of mindfulness or acceptance in
that moment it becomes central but then
what it allows then for is that that
your model has to update right if the
model can't
be sort of you can't find evidence for
it well then you gotta you gotta update
it and there you get to this notion of
vipassana right which is like inside
clear seeing inside right is that you're
learning something through through that
that wasn't available to you the moment
the moment before
and like apologies to everybody out
there who's like maybe very into the
meditation that like this is very sort
of hand-wavy way i'm talking about it
especially kind of like matching it over
to the over to active imprints a very
sort of loose way but that was kind of
the
the the gut
um intuition anyway coming into it and
remains remains the the intuition and i
think there's
this really
for me anyway and where i'm kind of
seeing my my
[Music]
career with this going just is the very
beginning of an exploration of how to
how to
articulate
meditations
different practices what they how they
might cash out in terms of um precision
dynamics different forms of learning
different forms of optimization and what
that might
mean you know for us so i think that's
why i wanted to start with attention
because it's pretty uncontroversial as
it were and just start building up the
building blocks and be able to start
making
more and more interesting
inferences about what it might mean to
be doing other kinds of of practice
awesome answer thank you
so
blue
or
yes go for it blue
hi so i don't know if you had a chance
to watch the discussion or like the
preliminary um discussion we did
yesterday but something that came up was
um
in the idea so daniel can you flip to
the circle about like uh tension and
attention
um
here the cycle this one
yeah that one so something that came up
there
uh
when we were discussing this figure was
like the
the discrete steps between like
distracted awareness of distraction
redirection of attention and focus
like you know there's kind of like an
intuitive um
feeling that the the
distracted awareness of distraction and
redirection of attention back to focus
is like discrete but like there's a
transition that's kind of muddy going
from focused to distracted and something
that i thought about was like you can
become so intensely
focused on something and like the
example that i'll give you because
you'll relate is like going down a
scientific rabbit hole like we're
chasing reference after reference after
reference and so you're still on task
and you're still correctly paying
attention to what it is you're supposed
to be paying attention to but like
you're so focused that you're finally
off task right because you just start
getting interested in other things
and so it's kind of a gradual transition
from focus like you're still focused but
you're you're like focused on the wrong
thing and so i just wasn't being like
where in this model do you think that
kind of like focus until you're so
focused you're not paying attention like
where does that like
come into this or how would you think to
model something like that
yeah thanks for the question so this uh
model that we're seeing here is of
course
a bit of a caricature right it's it's
it's a
it's an intuitive sort of description of
what's happening because you're right
there's degrees of distraction
and you know meditation we talk about
you you actually can classify these you
know those when you sit down to try and
pay attention to the breath there are
times when you've totally forgotten that
you were even meant to be meditating and
you were like gone right you're thinking
about something completely different and
then the timer goes off and you become
aware that you were completely gone but
then there's other things that are much
more subtle right this like
maybe you notice some sound in the room
or you know some sensations in the body
but still somewhere in your awareness
the breath it remains present but maybe
less and more in a background foreground
kind of situation and so like are you
distracted then or not
and to what extent
um and all these things and kind of
everything in between right
um so in terms of how that would cash
out here
the first thing to kind of point out to
is that the the precision parameter that
we're talking about is a continuous
parameter and so it doesn't have to be
um relating to discrete states and we
could have been free to um
grand euro like make more granular the
attentional state so it's not just
distracted or or focused um and sort of
have
grades of of focus
would have been possible but then the
other thing that isn't modeled here
is
what are you distracted by
um here distraction was just uh not
paying attention to the thing
but in reality distraction is your
attention being grabbed by some other
stimulus
um and for some particular reason
and
that is not uh shown in in this way
that's something that we're hoping to
start to work on in the in the future
part of the reason
why
uh we didn't go down that direction here
in detail is because
there's still a
i think a really central
part that is is difficult to tease out
still at the moment which is attentional
resource
you know in in some ways you could
you could run this simulation and given
the preferences on wanting to be
paying attention
if you put that preference on a bunch of
different observations there's nothing
stopping the agent just
paying attention to all of it right
maximally and having really high
precision observations across the board
now that doesn't seem to be what we're
able to be there seems to be like a
a finite um
something finite about it and so when
you're paying attention to one thing
it's at the exclusion of something else
and maybe part of practice and part of
you know what you're getting in
meditation is that that you know is
softening a little bit your ability to
sort of pay attention to more than one
thing or have more allocation resources
there in some way that might be learned
over time but that's not
um that's not shown shown here which is
why you don't get that
um
what you're talking about that kind of
intuitive
organic
uh feeling of what it means to be what
it really means to be distracted
awesome i have a
question and then blue so we've talked a
lot about how
spatial goals are set and even how some
symbolic goals are set like sentence
structure
but how are cognitive goals set
so are they reducible to sensory
preferences if so just the preference
for you know some salt and sugar that's
not going to really reduce your options
in the city so how do we set those
higher level and these increasingly like
abstract
and ephemeral cognitive goals
yeah no thank you for that daniel um
this is the the question i'm working on
right now actually and on a follow-up
paper where
i'm trying to take this model and and
and
specifically model uh focused attention
meditation
and
in that and in practice in general the
the question of motivation and goal is
really central and where where in the
model are you actually putting
like how are you driving
the attention behavior or meditation
behavior
um
one of the
ways the way that i did it here
was to say that in this kind of setup
that the agent is given an instruction
hey i want you to pay attention to this
stimuli and that that then translates to
them wanting to see themselves
um in an in the attentional focused
state and so the way that the dynamics
here are driven is by having a
preference on that attentional state um
and observations of that state so the
kind of like metacognitive observations
of seeing yourself paying paying
attention
here yeah thank you so oh
to
there um we put a preference
on
uh those ones exactly
um and uh
just as a side note there you might
think like oh but do those observations
uh exist really are they sincere
observations what kinds of observations
are these
um and i think that's a valid valid
question and something we talked about
for a while but
my
intuition here is that you know if i
were to ask you the question
um what are you paying attention to
right now
right
and you're gonna be able to give me an
answer from having observed something um
and so there's some kind of an
observation there that you're able to
make that you can
use to infer uh what attentional state
that you're in so anyway that's where
the preferences is is uh
there
you know i prefer to observe myself
paying attention
exactly so then
the question is what is it that drives
uh
you know like a practice and i've been
inspired by some of the work
by
um
uh mirza and colleagues on sort of scene
um
classification or scene as a foreseen
perception
we're there there seems to be this
attentional
driving of attentional
policies given another kind of
preference which is to
resolve a scene which is to clearly
perceive a scene
um and that's actually the way that i'm
i'm i'm starting to think about um at
least in a practice context in like a
meditation context because in reality
when you're meditating it's not so much
that you're trying to pay attention to
the breath although we talk about it
like that it's more like you're trying
to be continuously aware of the breath
um so you have some kind of a
preference on
um
perception or being able to be sort of
being able to resolve um a hidden state
and that that is then what
drives the kind of dynamics behind the
scenes
that's pretty interesting thank you for
the response blue
sure that kind of slides in nicely to um
what i was gonna ask so as a follow-up
to my question earlier and also to
daniel's question daniel can you flip to
the mind wandering side yes
thank you
so
i had a question here um and these are
two different models the one on the left
specifically is from the mind life
institute
by a
phd who works with um you know
meditators right and so and then the one
on the
right i'm not sure if that's an explicit
uh meditation task but i just thought
there was an interesting context here
so this paper on the right which is the
neural model of mind wandering
so you have like this paradigm where
you're on task which is like in the
meditation context say focus on the
breath or i mean maybe it's not focused
on the breath but i just i think about
meditation as you know being present in
the in the present right being in your
in your body aware of your hands feet
breath etc yes
so there's this model where you're on
task which is like focused on what you
should be focused on in present and and
then mind wandering they talk about as
the pursuit of internal goals which i
thought was interesting but i think
about that
in terms of like thinking about your
shopping list or all the things that
you're not supposed to be thinking about
while you're meditating right like just
going off and pursuing your own internal
goal oriented thoughts and then they
have a separate like category for being
actually off task
which is like where you're not thinking
about anything you should be thinking
about was just thinking about like
random like whatever nonsense um and so
i just wonder like do you
or could you think about making those
kinds of distinctions in this kind of
like and it goes from from being focused
on the right thing to focus on the wrong
thing like where does this off
task come into play i'm just curious if
you have any thoughts on that
um
i'm not exactly sure how they talk about
off task but what i could just talk
about here is the distinction between
um
to me the the distinction here comes
down to the meta awareness piece
right where
on task is pretty understandable
off task you could imagine just doing
something else but aware of that fact
you know like i've just decided to
change and start focusing on something
else but there's sort of a metacognitive
awareness of the fact that you are doing
something else
whereas mind wondering is this
uh slightly
or at least the way that we're talking
about it here um different situation
where you're distracted or you're paying
attention by when i said distracted just
been paying attention to something you
hadn't intended to pay attention to but
also not
aware of that fact
right you haven't updated the fact that
you're that that that's happening um and
that's the crucial piece here that we're
trying to regulate right with uh
practice or or whatever in in an
intentional in an attentional task
and
for that distinction i think i think um
active inference kind of
you know it almost gives you that for
free in a sense to kind of show you
where where that phase
would be and that's what we were kind of
showing in the results is that that
period of of updating of where your
attentional state
is
when you sort of think it's one but it's
actually another um so you think you're
paying attention or you're somewhere you
don't really know where you what you're
doing but you're pa you're distracted is
then how we would sort of
express that or
cash that out
computationally blue is that a quick
follow-up yes
in terms of active inference
um so it is so i just wonder is
like off task or am i wondering like i
had never thought to split those two
apart until i saw this this paper and
maybe check it out if you have time at
some time but
but really like i think about this mind
wandering is this like epistemic
exploration is is that like i mean is it
exploitation when you're on task and
you're focused on what you should be and
then is it you know we think about
active inference in terms of optimizing
exploration and exploitation uh is there
a room and a model for that epistemic
exploration or is it always like a bad
thing
is it always a bad thing
you know i don't have a i don't have a
good answer for you to be honest this is
what we kind of want to
go towards when i was saying you know
what are you distracted by and what's
the why behind
you know the default bone network
basically like what is what is the
value of that on the one hand
i could imagine that yeah there's a
there's sort of like an epistemic
wandering through state space and future
possibilities and just sort of
monitoring of potential negative
outcomes in the
in the future
um with
for which there's obviously value um
and i don't think it's necessarily a bad
thing i think when
when i
you know in a practice context anyway
it's like that
that action can also lead to discomfort
now and anxiety now um because you're
sort of simulating future bad events and
there's actually a great paper casper
wrote a good paper on that
um deep i've read it yeah yeah the
simulated future events well and so
often meditating like frees up space in
your mind i mean i don't know if you've
had the experience but like where you're
not thinking about
some
other problem but like you'll be
meditating and like whoa have this like
brilliant flash of brilliance or like
key moments of insight right like be
possible so there's just like ins but
it's maybe not insight into like some
internal like deep spiritual discovery
but it might be like insight into some
external problem that you're having so
there's
there's that and so i wonder like that
might be the difference between off task
and mind wandering like if you're off
task it's like maybe a non-beneficial or
like there's no excuse for
it's just like doing blah blah whatever
and then mind wandering might be like
exploring your neural space and in like
a recombination phase and think about
that so anyway it's just something to
think about going forward
interesting
interesting i think the the the notion
of insight
and
the
kind of why practice leads to that
is really exciting place to start
thinking about like what is it about
paying attention in a particular way
that leads to these moments of
aha
right
thanks i'm going to read a question from
dave
dave wrote
a practice i've been following based in
naropa institute's shamatha practice but
not much stress there is to attend only
intermittently say
permit mind wandering during the out
breath but attend during the in-breath
there are two effects obsessional
thoughts are disattended without
intending to disattend to any content
the motion of this attention dis of the
transition from disattentive to
attentive
occurs many times the usual
return gently to resting the attention
on the breath
happens several times a minute rather
than several times per hour does anyone
else do this
or discuss it maybe to warn against it
close parentheses hyphen to your
knowledge
i like that i didn't know i haven't
heard
of a practice like that before but in
the way that you're describing it i
could see a way that would be really
really
powerful and really useful because
one of the pitfalls
i can tell how this conversation is
going to go more and more into
meditation
but but i'm i'm i'm i'm up for that i'm
game um but one of the one of the
pitfalls of course in in
in practice is
is all the subtle ways in which
resistance can come up towards our own
minds
and if we are paying attention and we
start to see distractions as things that
are stopping us from paying attention
and that we don't want
right then it creates this tension and
is actually counter to what we want to
be going for and i could see how by
deliberately letting mind wondering
happening and coming back it sort of
cuts that tendency to have resistance to
to thoughts which actually just ends up
perpetuating them or giving them um more
uh potency in the mind whereas really
the aim is to pay attention to the
breath and it's funny because when we
say pay attention we think like it's
this like
focus you know thing
in reality 90 of it is relaxation and
letting go
and letting go of
the
resistance to distractions distractions
come and then we come back back to the
breath and that's what kind of does does
the work so i would love to um
i'm gonna look into that a little bit
more detail that style of style of
practice would be interesting to see
when we have a more fleshed out version
of this like how
um different approaches to practice
might lead to different kind of learning
outcomes at different rates etc
that topic of distraction it's like if
somebody were a captain and they cited
something very subtle that wouldn't be a
distraction that'd be on task
so then there's this aspect of the
multiple levels like there's the eye
circading
and then there's higher higher and
modeled in this paper greeting scott
at slower and slower kind of clicks of
the model
and uh so it's just interesting yeah
what a distraction implicitly says that
it's not on task
because if it was even something that
was unexpected that drew the regime of
attention that way if it were relevant
for the task
then it would still be considered not a
distraction part of the relevant stimuli
for the task but the exact same stimulus
might be off task in a different context
like five minutes later
yeah yeah completely i mean if
somebody's trying to
talk to you and you know share something
with you you
only paying attention to the sensations
in your hands is not very helpful
um but
i think
what we're kind of flirting with here as
well is is this notion of task and goal
and on task and off task
and
i think in a
i mean in a meditation context that's a
really
you know um
difficult difficult thing to define
there's a big difference between
somebody who comes into practice because
they want to
um
you know sleep a little bit better or
not be so stressed or have a little bit
you know more ease in a relationship to
somebody who comes in
and says you know i'm in it
for
really understanding myself and who i am
and what i am and for you know questions
deeper questions of like awakening and
um you know expanding awareness and
these kinds of things and those
intentions and motivations are you know
these task priors that you're setting
over this whole thing and are driving
the way that you practice
and you know traditionally
what
is sort of said again and again and
again is that
defining that is pretty important in
terms of what you're going to get out of
the practice because to pay attention to
the breath
to just pay attention to the breath
without really understanding why and
where it's leading to leading is um is
one thing
whereas having it within a context of
you know a wider
program and goal is is a completely
other other
situation now modeling those in active
inference is interesting right i would
say that the the latter
sorry about the background noise here
but the latter example
there of you know thinking a bit more
broadly is is having some kind of a
preference on
um
your own happiness right like your own
um
model
fitness ultimately you know if we kind
of go on the affected inference
kind of view of you know casper tell
that like
affect
in some ways related to how well you're
doing and how and how well your model is
is predicting
and so to have that as the as the
intention
rather than just paying attention to the
breath but seeing how paying attention
to the breath can can lead to that
ultimately is a different kind of goal
goal statement than than the sort of
narrow attentional task itself
thank you lars
dean and then scott
yeah i like to think you're i think like
no i'm on okay i think you're taught i
think your topic lends itself to wanting
to gallop ahead because it gets people
so excited about this idea of moving
from subliminal
to liminal
to kind of a limital like a precision
around edges right so that transition
gets people excited because now they say
oh i can think of a ways that i can use
this
in whatever it is that i'm trying to
figure out um so at
some point
that transition pulling that transition
apart but not breaking it
is is going to have to we're going to
have to sit down and really parse that
with you because
it feels to me like we're doing a a is
are we 28 or 29 we're doing the 0.2
right now because everybody wants to
really get this thing going because it
because it's uh
it's kind of exciting stuff right like
you've given us this this backpack of
stuff and we're like opening it up and
it's all this candy and we're
but i'm still really kind of interested
how that how that goes from subliminal
which cannot be planned and cannot be
thought out because we're talking about
act sensory inactivation
to
thinking about thinking because when i
when i see the diagrams themselves
they're there but it doesn't really help
me understand that any better because i
still think that's a really really
tough bridge to build yeah you know what
i'm saying i know it's there but it's
still hard for me to get my head around
i think i think i know what you mean
being what you're referring to which is
like where does the
where does the structure come from in
the first place is everything yeah well
we know where it comes from in the first
place and we know where it ends up it's
the transition in between it's those
casper got us to the third layer
now we've gone to a deep transitional we
generated a context we're thinking about
our thinking it's metacognition
it just appeared it just emerged so how
does the con how does the math
work on that
this
i i think i think what you're getting at
there i mean
there's kind of two ways that you could
think about
a model like this is like either you say
well the structure's in place
and what's changing through learning is
the
the precision on observations
essentially like you become aware of it
it becomes something that can factor
into your perceptual uh belief updating
um that's one way around or you can say
that there's something about
human development and maybe the
evolutionary process that sort of leads
to this or structure growth and learning
um and then the question is well how
does that come about
um
the first question is a little bit
easier to answer than the second
question because
obviously structured learning with an
active inference is still an ongoing
area of you know investigation
research and and how exactly that comes
about
questions of neuroplasticity and things
is quite it's quite difficult to grapple
with and then how why do particular
practices and you know different paths
in life lead to certain things than
others but then
to take the other stance or the other
way to talk about this which is i think
what you were saying correct me if i'm
wrong but like let's assume that the
structure is here that we have some
kind of a deep hierarchical
um you know parametric structure that is
giving rise to to metacognition how do
we go from being uh
not aware at all of the contents of our
mind to being aware of the the contents
of our mind
right yeah it's kind of contradiction
right because the way it's set up is
it's a bridge to everywhere it's not a
bridge to somewhere and then somehow in
that bridge to everywhere metaphor we
select out a particular and we give it
our focus or our or our attention
and so i'm not saying
that the that the math doesn't work i
think the anchor piece is that at the
basic level nobody's going to argue that
we have a markov blanket and we're going
to we're going to statistically move
closer to what we think is going to
happen next we're going to update it's
the it's the last piece which is we're
now thinking about our thinking that
just seems to pop out
and make itself available you know
because we've now built up a set of
priors but we i don't i i'd like to see
how the math explains that
that's what i'm because it's still it's
still a distributed set until it
collapses to what we focus or attend on
and so
it seems like a contradiction
and maybe that's what it is maybe that's
what the math
is trying to explain to us
i'm still not sure if i've completely
uh grasped the
the point of interest here what what
what all that how the transition works
again i'm sure you'll be able to explain
it but what i'm seeing is a transition
to
first starting up being very open
and then the mind is able to
buckle down for lack of a better
expression and get its attention on
something it starts out open and then it
moves to something closer what i'd like
to see is how the math explains that
that make sense i think so i think so
dean maybe one way just saying it would
be just looking at figure five like the
lower levels are certainly outside of
our control and the higher levels are
moving towards phenomenology whereas the
lower level in traditional neuroscience
would be seen more as like sensory
processing and yeah it's indeed similar
kinds of models so how do we kind of
bridge not just the um science
humanities gap but like the parameter
experience
gap and then what is that
sort of marsh
between them and is it really the case
that just by nesting this model that we
know and love
we ended up getting the or a structure
of cognition is that the or a structure
does that exist as part of a broader
family of related models
is it just about finding patterns of
nodes that explain variance in multiple
components of phenomenology and
physiology
that's the question
well i for me it all comes down to
precision
uh within the model uh then that's kind
of how i
been thinking about this is that
you know at the sensory level that first
level
there
are multiple places that
you can
start to
identify
just patterns you know statistical
patterns and then start to layer on top
of that a confidence or precision over
that which you know we have evidence for
you know how that's mediated in the
brain for various various places but
the precision then itself itself becomes
this thing that you can layer on top of
your entire sensory experience and gives
you this kind of
um
internal
flexibility as to how you're how you're
interacting interacting with the world
and then the modeling of how those
precisions are being driven
you know
without your awareness is then what what
those states that that be the b matrix
at the second level would be would be
encoding is you're starting to learn
ah okay so this you know my attention
gets grabbed by this or that or like
these are the kinds of and here we're
talking explicitly about attention but
there's other precisions around that you
can start to understand how they are
evolving
and then also learning where you're
where your reach of control is like how
much of how much of this can i control
and and influence
and what does that mean and what are the
impacts of that
um
it's kind of what
i find exciting about exciting about
this because you can kind of see how
different
forms of precision control and awareness
would lead to different kinds of
model optimization and
you can
calculate the free energy you know based
on on how different precision profiles
are
defined and evolving and kind of
over time that's something that you
would hope to be able to learn
and then the question is how do you
actually learn that well
by paying attention by paying attention
to how it's changing um and that's not
always easy um and sometimes things in
life you know make us pay attention to
it you know start to notice like i'm the
kind of person who gets yeah thank you
exactly this figure here that gets
impacted in these ways but
i think there's a really important thing
to say around the role of a teacher in
this as well somebody who can point
these things out
and
in doing so direct your attention in a
way that you wouldn't have thought to
previously into noticing like hey
there's this
pattern in my mind that i hadn't thought
of as a pattern i just thought of as
well i hadn't even thought of it it's
just happening and then as soon as i
start to see it as a pattern it's
something i can start to model and then
you get this kind of emergence of a of a
higher level
structuring or understanding or grasping
or modeling expectation over these
patterns that were previously
unconscious
thanks i'm gonna just read a comment
with uh no response needed from the live
chat and then go to scott
so joshua benjamin wrote
all psychic ability seems to be
subconsciously driven oneness of the
active and subconscious mind would be
magical to say the least people that
already have their active and
subconscious mind working as one also
seem to have identical palmistry between
their left and right palms
interesting observation scott
yeah thank you i'm sorry i was delayed
in coming in but i'm always thrilled as
soon as i drop into the conversation
it's like being with family so this is
so wonderful what a great conversation i
wonder if you could comment a little bit
on
the attention versus intention
it feels like part of what we're talking
about now let me let me comment on that
a little bit and it's following up on
dean's
um exploration there
i was thinking i always talk to people
about the aha moment if you know the if
you know the um punchline to a joke and
someone tells you a joke it's just not
funny because you know the punch line
and so the aha moment is the same as
that moment of eureka when you get out
of the bathtub and run around yelling
eureka but you do you understand
something it's a paradigm shift like
thomas kuhn in the structure of
scientific revolutions talks about that
you shift from not knowing something to
all of a sudden knowing it
so those i'm an addict for those moments
i love ignorance as a result so i wonder
if you could talk a little bit about
going from attention
to intention
i am coming to the belief from working
with all you folks
and others in similar explorations that
the mind actually doesn't exist at all
in the brain the mind is always in
society and in language always
the brain gets tuned
into a local mind by exposure by
perception
and then that become the attention turns
into intention you adopt like a bauer
bird you adopt nascent models
from the externality there's no onboard
feral consciousness in my assertion here
so you develop it and cultivate it based
on your exposure to the environment
as you build it up
the attentions your teachers out there
in the world whether they're formal
teachers or informal
can help you convert attention to
intention because the models get
developed based on
their their explanatory power of your
environment right if they they get cast
aside if they're not as helpful in
closing free energy gaps for instance
so
i just wanted to throw those things out
there and following up with dean to me
the paradox
of the frizzle between consciousness and
unconsciousness is not something that we
can resolve it's something that we can
observe and
maybe manage in some ways with these
models but the paradox is one thing i
always told my kids is the only time you
see reality is when you're seeing
paradox and anytime you're seeing the
absence of paradise you are seeing a
model
and when people say they want to resolve
paradox it means they want their model
to win
here it feels like as dan was alluding
to that there are multiple models that
are in play simultaneously
and the multiple models maybe can give
us a sense of the shift from attention
to intention anyway your comments are
welcome
thanks scott
thank you for that lots of interesting
points there
um
i'll just pick out one of the things you
said there around
insights and these aha moments
and from
and this isn't present here again in
this work encounter falling into a
dean's trap here a little bit of um
running forward with it but
if you
imagine
here that what what's being afforded by
you know paying attention new ways the
dynamics and and precisions you know
within our generative model and how and
how the all these things are evolving
you know we're gaining in model kind of
structure and
complexity ultimately
and
one of the
bits of work that i find really
interesting from carl and other
colleagues is around you know insight
and they've been talking about it in the
context of psychedelics
specifically as these moments of
model reduction
um invasion model reduction whereby you
lose a bit of
model structure and there's this
liberating aspect of that and there's
this sort of knowing aspect of that too
and it's not that you've sort of learned
something new you've kind of unlearned
something and in that
you you
gain in model fitness as well you know
there's this kind of um
improvement of the state of affairs by
by doing that and so
you could imagine a scenario whereby
um in
playing this game of paying attention to
how things go and how things are in the
mind specifically your model structure's
kind of gaining complexity but you're
also identifying places that can be
reduced and you get this sort of
cyclical
growing of complexity and reduction
which matches on really
really nicely and i have to be really
careful sometimes to not try and like
recapitulate
things that i um like from sort of
practice theory into science and really
be you know grounded in in in the active
inference but nevertheless there's you
know my heart kind of wants to say that
kind of nicely matches to the cycles of
practice too these cycles of of insight
and
growth that does come in this sort of
non-non-linear and cyclical way
thanks lars
blue
so this isn't really like a question but
it's more of a comment so scott was kind
of talking about converting attention or
intention to attention but i think that
that's also something that's cyclical so
you can convert attention to intention
and intention to attention you intend to
pay attention attention
gives you an intention um sorry that's
like way tongue twister but like
where does imagination come into play
there right like there's attention
intention but where's the exploration
the creativity and does active inference
allow for maybe this component on
attention intention and imagination
cool question um i think of imagination
a lot in terms of uh generative
practices so like state generation
practices like loving kindness gratitude
forgiveness these kinds of things and
for me the way that i think about that
is you are using your imagination to
generate
um
the
goal observation the goal state
right which then allows you then to set
a prior over that to aim for so if you
evoke in your mind the
a you know may you be happy so i'm
imagining a situation where you are
happy and now that is a a possible
future state that i can put prior over
and
once i've done that then the machinery
of active inference starts you know
coming into play to achieve that kind of
goal and
that's a very very hand waving very
loose and again like i can i can sense
that people out there might be cringing
to this kind of way of talking about
about these models but
you know an answer to the question
that's kind of how i how i think about
um
at least that form form of imagination
that's some point two stuff thinking
about how our cultural environment
scaffolds our preferences and our telios
our end directedness
which is something that came up in
navigation now it's coming up in
cognitive navigation
and setting of these higher order
parameters scott
i just wonder why is it cringy
from the math perspective the right
because i'm a humanities guy and i'm the
math always freaks me out so i want to
understand though what is it about the
you're a math person steeped in the math
what is it about what you just said that
makes you uncomfortable with the math
and how might the math be why is it
stretching the math or how might the
math be extended
to to accommodate that cringiness
problem yeah no thanks scott that's a
good question
um the reason i say that is because
these
models can pretty much model anything
right you can you can adapt them to make
almost any point that you want
um and so you know if i
start saying
oh this is how it is and this is what
imagination is and does well then i can
sort of ad hoc um
play with the model until it until it
until it makes that point um and what
i've really tried to do here in this
paper
is be very careful with that
and to allow the
dynamics to emerge intrinsically from
moves in the mathematics that are
um
like
allowed and and and
don't make many assumptions
because really all we're doing here is
is having a higher level that is
parameterizing precision on the lower
level and then we're just running it and
seeing what kind of dynamics emerge and
interestingly the dynamics that emerge
are aligned with the expectations but if
i go too far the other way which is
really easy to do with this right
because you have especially in a
practice meditation context there's
really detailed phenomenological models
of
all kinds of uh mental dynamics and it'd
be very easy to say
you know just gerrymander active
inference to describe all of that and so
that's why i'm trying to just be a
little bit careful on how i talk about
it
one just to follow up the one of the
things
so
this may be uh rationalization but so i
was i'm a lawyer so i was a rhetorician
and so when we have incommensurables in
the law we use rhetoric to glue them
together and it's not crazy glue crazy
glue doesn't fill gaps its rhetoric is
epoxy
right it
glues stuff together and fills the gaps
right crazy glue just sticks stuff
together
and so the reason i'm talking about that
is is it again i asserted before that
the mind actually exists in language
that's very weird and loose language i'm
using there the mind exists in language
it exists in material culture we're born
feral
and we get our brain gets tuned to a
local mind let's go with that for a
second as a posit
so you you have nothing on board when
you're born would is it i guess another
way of asking the question can the math
construct consciousness from a feral
mind with no social exposure
that's my question and i am
beginning to believe
that nothing
yes there's imagination of course
there's a lot of lateral thinking but
all the things are borrowings from the
externality is my assertion now that's
not the imagination you can mix and
match them different ways
but if you're isolated and have no
question is i guess will the math
generate a consciousness
without any external input
and i think the answer is no
and so therefore it feels to me like the
brain is a
mind instead instance
and the mind actually doesn't it's
paradigmatically weird and different i
don't maybe there are people who say
this i don't know i just don't know
enough about the mind studies
but
it feels like
we can allow ourselves to
um
not feel cringy
about the extension the math now again
i'm not the math guy i'm the cringy on
the cringy side of this but
by if we recognize that the source
of the mind stuff is external
maybe that's okay
and it's processed in the brain anyway i
don't know if that's something he's
responding to but it's to me this is
very interesting because this is that
metaphysics jump
and is it metaphysical or not i don't
know
i
i the i mean i i don't i don't uh have
much resistance to what what you're
saying there i don't think these things
happen in a vacuum and i think
um you know
just intuitively uh you know the that
kind of a cognitive structure would not
emerge without some kind of you know
societal or back and forth multiple
nodes in the network you know working
working together on this and
you know anecdotally a line that always
sticks with me and um
from the buddha of all people is uh you
know there's two things that are
required for awakening there's wise
attention and the voice of another
and it kind of speaks to that need for
interaction
now the reason the reason i the reason
i'm
what i really meant when i'm saying
cringy is that
i think there's actually a huge
advantage
in just going slowly and methodol like
and systematically through this because
what it allows us to do is be very very
precise in what we mean with our words
because i can talk about attention
and that might mean several things to
different people but it almost doesn't
matter what the definition is of it i
can just point here in and say well
whatever this is what i mean by this
word
and i can keep doing that building up
the complexity of it and i can start to
have very detailed descriptions and
articulations of mental dynamics that
don't rely on interpretation of the
words because they are referring to
something quite um specific
thanks um and it is really important to
have that uh perhaps
carl firsten would say a deflationary
view
so the deflationary view of this figure
12 the generalized deep generative model
of mental action it's like
i mean big if true
the deflationary view would be that just
like a linear model like a linear
regression bayesian modeling can be used
on any kind of data so just because
there's a word that you may or may not
have familiarity in front of it like
frequented statistics bayesian
statistics it doesn't get around the
fundamental problems of data modeling
and it actually has a lot of
similarities with hierarchical gaussian
models of control which are common at
least related to this idea of nesting
slower levels of policy inference with
some
again tricks that are really interesting
like free energy calculation all those
other things that we talk about other
times but that kind of model never took
on a philosophical or metaphysical
baggage even when it did appear to
correlate or even have predictive power
for example predicting what somebody
would buy
and um
it just it's a choice that we make what
is our cultural priors what are our
personal preferences over connecting
that metaphysical jump that scott
mentioned maybe some people they um
think it's a six-inch jump and they can
jump 20 feet and other people they have
a belief that it's a bigger jump so
that's why it's such an interesting area
to talk about because there is some
hyperinflation going on
and then there's some extreme deflation
and there's everything in between as
well
yeah and if i could just uh yeah yeah
larger than scott
um the
i
thank you yeah for for articulating that
so well
because um i know i'm also guilty of
this in my own mind when i'm thinking
about this privately of just sort of
running running this forward and losing
track of
of of what uh these sort of ontological
commitments in
in this whole discussion and i think uh
maxwell
one of the co-authors he
sometimes refers to you know hard for
estonians and soft fristonians and that
kind of speaks this deflationary and
inflationary inflationary point but for
me in this in this work
um what i'm most excited about isn't so
much a
an ontological
um
proof or
um
conclusion of hey this is what it is and
this is what the mind is doing this or
or anything that's strong what i'm more
excited about when i think is more
relevant to our times
is that
even if this is a
a facility or a a kind of
uh loose description or a
um you know
what am i trying to say approximated
framework of something that's going on
if it allows us to
articulate intelligently like how these
mental dynamics are going on
it really
helps you know because i teach
meditation as well and one of the big
obstacles that you come up against is
like yeah but why should i do this like
how does it work and what what what
what's the point and if you have
something like this that
allows you to articulate
why and how and the dynamics and what's
going on
then that breaks down that barrier and
allows for in a conversation that's at
least grounded in something closer to
um
you know biologically inspired
computational you know neuroscience
rather than
a
phenomenological report not that there's
space for that but for a lot of people
this is what would get them through the
door
thanks lars scott and then anyone else
with a raised hand so i just wanted to
go back that's this is fascinating and i
wanted to go back just that rule the
idea of rules of general application
like
is this reducible to
it is
our elements of this that are
interesting reducible to formulas is
what i'm where i'm going with this query
now and i wanted and it made me think
about you have this society you have
different societies with different
standards different music
scales different recipes of food and
things that people are familiar with
right they're raised in that context so
chinese food is and music are familiar
to a chinese person if you're born in a
different culture you don't those are
unfamiliar to you so i wanted to talk a
little bit about rules of general
application because in law so i come
from law
and law you know we've got technical
specs now and here we got fristen
analysis and trying to find general
rules of general application that's fine
that's good stuff and they and the one
of the things that's interesting about
rule of general application is how
general they are
so in in law you have this thing called
equity which corrects the rules of
general application i just want to read
you this aristotle quote that guides me
a lot here aristotle said the source of
the difficulty is that equity though
just is not legal justice but a
rectification of legal justice the
reason for this is that law is always a
general statement yet there are cases
which it is not possible to cover in a
general statement hence while the
equitable is just and is superior to one
sort of justice it is not superior to
absolute justice but only to the error
due to its absolute statement
this is the essential nature of the
equitable it is a rectification of law
where law is defective because of its
generality the reason i'm raising that
here is you know
we can find general rules they don't
have to work in every edge case
right and if we find edge cases that
undermine the general rule it doesn't
mean the general rule is no good
right it just means we need some
tweaking at the edge cases or something
right and one of the things that's funny
in equity the idea is you have to bring
in someone a judge or someone
who can come in and say what did they
mean when they were coming up with the
original law not what does the original
word say but what do they mean to do the
substance of it right and similarly here
what i guess i'm arguing for
is the social aspects of the mind
probably don't need to be divorced from
the model entirely
the hand-waving aspects of the mind the
metaphysical aspects of the mind because
they are
they i think
are always the foundation of the
possibility of a mind
right we come into social you you've
come in life feral and then you are and
then you learn that there's a society in
other people and you have self another
you learn that
as a child now maybe you would learn it
out in the wild maybe not
i guess what i'm saying though is we the
model it feels like
doesn't ultimately have to be
mathematically 100 percent rigorous
because the borrowings in the model that
are made from society intrinsically
have caused leakage into into that model
being affected by the externality so i
guess both the perception and the
other model contents feel like they're
unavoidable
anyway just a few
ruminations there and and do with do
with what you should with that with the
cud that i just served up
i mean i think this what you're speaking
to here is a pretty
um big topic in the active inference
community in general and this idea that
you know the map is not the territory
um and
depending on
who's speaking we kind of get lost in
that a lot of the times like are we
agents with generative models or
are agents
generative models and to what extent is
this a description and to what extent is
it
um
you know that's
i'd rather not wait in there to be
honest no i get it and i like your
statement the math is not the territory
it's nice because really that's nice
where you think the math is the tool
to understand
the
journey or whatever but that's a nice i
like that statement you just made about
the math is not the territory because it
often feels like and that may be
something that is helps with the
invitation you know the space can be
threatening to non-math people
because it does need a rigor i get it
but there are things that are being said
by the math that need to be conveyed to
non-math people you know they're
important things when i first dropped
into the space i said oh my god all the
contracts i ever made are synthetic
markov blankets
they are i'm creating a there there that
wasn't there it's not an observation of
a biological system that's natural it's
an artificial
of creation of a thing a place where
these rules apply for internal and
external operation right it's it's an
artifice so and we do that a lot in the
world but so that was my first kind of
impression but i don't i'm never going
to understand the math enough to have
the rigor to be able to
delve into that and understand the
implications of active inference math
for the law it just won't be available
to me
so if and to the extent
that without going to metaphysics we're
able to create narratives that are
honest to the math
realistic and also available to the
non-math people that's going to be
something that will
lead to a lot more
both understanding and misunderstanding
i get it but but a lot more
awareness and adoption
of the models i think which will lead to
more um i think better systems better
policy because there's a lot to be
learned from this and it's the same
thing as an engineer knowing how to make
a nuclear power plant work and then
other people down the line knowing how
to sell power but they don't know how to
make the new nuclear power plant work
right you need you need all steps of the
supply chain
of this to be delivered as a social good
i guess is what i'm saying so that's a
big i'm putting it all on your shoulders
you guys yeah but i mean that's the hope
here i mean that's i think what's at
stake a lot of the time is that you know
i i think about this stuff in terms of a
practice in a practice content sharing
and communicating on how how best to
you know improve our mental well-being
given given what the the insights that
this might afford and given the the
structure in terms of communication that
it might allow it's already impacted the
way that i teach it's already impacted
the way that i practice personally um
but then there's a whole field of
computational psychiatry as well which
is which is very closely related to this
i mean the kinds of well-being i'm
talking about or the kinds of
dysfunctions that the computational
psychiatry people are talking about so
there's there's a lot of hope to that
and it doesn't take somebody to
understand
um you know how to do a gradient descent
on free energy to be able to benefit
from that
definitely typo but this is a slide we
had from the dot zero
just like
there's so many directions
that this area verges towards
and um
just
how we even
make sense of this field where is active
inference going to connect the the
pieces just i don't know any of these
elements on the list that was
interesting to you and give a thought on
um
or anyone else could just raise their
hand
oh the hype the hyper scanning
piece is really fascinating because
there's a there's a obviously a deep
tradition of
you know these kinds of things being
learned in community and in interaction
with other people um and that
is not obvious how that how that happens
and i'm looking forward to
you know that whole space developing a
little bit and being able to
model you know what it'd be like to
learn
you know what's the difference between
learning through an app and learning
from a teacher
cool
very interesting so um i see scott's
hand and then anyone else
so the other place is just in in the
crafts world of markets you know you
have information differentials are
differentials
and the markets are driven by
information differentials i've asserted
for a number of years that cardo's
equation and thermodynamics the hot and
cold differential is necessary for a
heat engine to function
the that that is equivalent to the
differentials in information
differentials and markets you don't have
market action if everyone has the same
information and that's that idea that
markets generate information price
information availability things like
that
so
the crass part of this and that tends to
make things get swept away in the world
of craziness when you get things into
markets because anything goes and you
know it's just a big mess
having said that
the impact of this kind of analysis will
be very appealing in markets because it
does have a scale independent aspect to
it
and so it allows for insights at
different levels of different markets
and meta markets and related supply
chains
that if everyone is doing this analysis
then it leads to a certain kind of
interoperability
because you have a
um
risk
and risk evaluation interoperability
right and so the value in markets if
everyone started doing active inference
style of risk analysis
you'd be able to
make observations about at different
scales because you'd have data coming
out of every scale that was generated by
models that were similar
right so that kind of aspiration it's
what i'm looking at with the i'm working
with banks now etc and i'm not talking
about active inference or carl fristen
but i'm starting to set that up as best
i can in the early stages of it because
it feels just like a natural thing we
are biological systems our markets and
our institutions are ultimately doing
reproductive and nutritional
opportunities at large scales
you know and so there's a lot of biology
that's still bound up in what we do as
organisms in our scaled structures
and so
it's exciting to watch because this
thing is going to come out of left field
and it's like quantum computing everyone
thought there was a thing in the lab for
a lot of years and now people are like
oh geez here we go that's going to be a
big deal in other things like business
and governments and
and i mean you just imagine legislative
activity informed by a
active inference style of model where
you really do probe
and we get feedback right what if we had
feedback from legislation every year
saying this is good or not good more
this less of that right i mean that's
the kind of thing there's been
aspirations that for years
putting lobbying aside that would lead
to a great efficiency
in things like legislative activity and
enforcement activity things like that so
i'm very excited that these things are
going to get
taken in the directions where they
weren't intended
and i think it behooves the people who
really understand it early on to set up
some nice chunky
solid
notions and paradigms so when they're
adopted they don't drift too far
from where they should be right because
the things get picked up and taken in
all sorts of wacky directions out in the
world
so it's kind of that's what i'm talking
about simplifying in a way that still
does justice to the to the
what's going on there and as a person
teaching meditation that's exactly the
same kind of mindset you need going into
these crazy markets right is something
of common intention because the markets
have different agendas and intention if
we want the active inference intention
to be carried forward we need to make
sure that we have robust
presentation of the model so when it's
picked up that model can withstand the
abuses that happen out there in the
rhetorical markets anyway again more
just load on your shoulders
any thoughts there blue or dean
or dave
i didn't mean to bring things to a
screaming halt sorry i can go in a
different direction
no
all good um
um what's a um figure or a
word that you might like to go to lars
or when you're communicating this to
different
audiences like more from the maybe
non-active infant side what is your
entry point is it one of the key words
here or one of the figures here or how
do you enter do you show the action
perception loop do you just go straight
to the
you know
bayesian graphical model
um yeah good question um i think this
this this card is a a particular one but
um i think i when i talk about
this paper i kind of do it in in two
steps starting with figure
um well when we make
when we
look at precision so early on in
in just talking about attention so yeah
exactly here
um
and
just starting here because it's quite
straightforward as a model of of
perception
and attention ultimately and you can
kind of see here
um intuitively what this precision is
about and and
we can yeah let's do this let's kind of
build it up and we'll go straight to it
we'll go up to figure 12 which is where
i'm really excited about
and going in the future which is this
kind of generalization of this this
across and what it might mean and the
game that we have to play here a little
bit is
a little bit dicey in that in that
we're trying to
make
intuitive phenomenological
interpretations of
maths right
and
that's
not not easy and requires a lot of
discussion back and forth but that's why
we started here with attention because
it's the one place where
it's
less controversial and more widely sort
of defined and so we're starting with
the tension here just the precision
on you know the likelihood matrix and
you can kind of see
just intuitively i mean maybe this
depending on who you are listening to
this is like that's already kind of
obvious yeah um you know higher
precision on the likelihood matrix means
you know uh is related to attention but
just to kind of motivate that a little
bit more subjectively um
you
can tell that um at the center of your
vision you know as opposed to the
periphery you're a bit more confident
about what you're seeing like if you see
a glass on the table at the periphery of
your vision
you might not be sure if it's a glass or
a mug right but you can still see it and
then when you look over to it
um then you can be more confident in the
causes of your sensory observations
right or in this case
just lost lars for a second but
just to sort of
while he's reconnecting
that's one sort of experiential
urine degenerative model type thought
experiment or really commands for covert
action for attention which is to realize
that the color detection outside of the
center of vision as well as the
resolution is very low
and that there's a significant blind
spot so there's three features of your
visual field
for healthy vision
that make it so that the visual field is
not just seen homogeneously
like a sort of silicone light detector
light detector device in the camera so
just a starting point for saying okay
something else is happening
such that attention isn't being paid
it's being normalized in some way
to
not just increase the resolution outside
of the high resolution detection zone
and colorize it in many cases but also
to normalize the absence and paste over
the blind spot
so then that can be extended to other
sensory observations
so
what do you mean by normalize the
absence and pain over the blind spot
that part like it feels normal
to
wha was being perceived under just
again this is the whole interesting
question about what is perceived as
normal at what scale
oh it's weird there's a door here
how weird what about the door
so
i don't want to be so i don't want to be
normative with the way that i'm talking
about the mental states but there's
different ways that that uh anomaly can
be detected and there's certain sensory
illusions that are really illusions
because the alternate perception which
turns out to be factually different than
the actual sensory o
that is different but that difference
structurally or inaccuracy or around
resolution
is just
seen as part of not salience but not
salient part of the organism's
experience phenomenologically
not to say unimportant at a nested level
of analysis
hey lovers welcome back we're just
talking about um
generative model
vision so
continue on too perfect thanks thank you
no hopefully it doesn't drop out again
um so that that's kind of motivating the
the
the
phenomenological translation let's say
and then and then the next step is to
then say well okay we are somehow in
control of that precision and here i
leaned um on existing work by jakob
blimenoski and fristen and others
whereby
that notion of control and mental action
um
then
you can you can talk about that as a
deployment of precision it's some kind
of a
a precision um
modulation
is the word i'm looking for and so
then
then the natural
the kind of next step there is to
you know
make that possible within the active
inference framework in the same way the
other action is also possible and that's
where the second level comes from
um in figure four i think it is
um because then this is what then allows
that to be the case and
really all that were all that we've
done here is to say
okay attention is this kind of thing
this is this kind of precision um and we
can motivate that in all kinds of
different ways both sort of
computationally and intuitively and we
know we can control it so what would it
mean to be able to control it well the
same thing that it means to control
anything within this framework and then
here you go this is what kind of makes
that makes that possible
um and again luckily i'm really standing
on the shoulders of giants here and in
that you know a lot of this stuff was
already worked out you know casper
italian
effective inference already had this in
place they just didn't have a policy
policy set over this higher level yet
um and so this is cool but
uh like i said in the beginning
uh the the real aim of the
game or what really allows for um
attentional freedom in in the kind of
practice context is not so much
um uh
the attention itself right but it's your
awareness of where the attention is so
then
then um the question for me was well how
do we pay attention to attention but
once we have this this this structure
well then that becomes kind of
straightforward and not straightforward
i mean you have to make a little bit of
a leap but then you say well we pay
attention to it in the same way that we
pay attention to the sensory states and
that's where you get the third level
um and where these states now are the
degree to which you are aware of your
attention um and you know if i just ask
you
you know how where are you of where your
attention is right now um
when i asked the question probably not
so where just afterwards probably a
little bit more aware and so there was a
transition there that that happened in
that higher level state which is then
modulating the precision of the lower
levels now
this kind of uh this kind of a move
computationally mathematically
is
internally coherent and allowed but it's
also not unique there's no reason why
you can't do the same treatment to
other precisions in the model the other
ones that we're most familiar with from
the literature are
the precision on g model precision and
the precision on b
which are usually which is usually
related to sort of volatility beliefs
um
sort of um
unexpected uncertainty i think if i'm
saying that right um and um
just as a side note we made the decision
to kind of change the notation here uh
just because we're talking about so many
different precisions in the literature
up until here precision on a
was
zeta i think a precision on b was omega
whereas here now we've just called all
precision as gamma and with a subscript
based on which which parameter they're
referring to
gamma previously was was really just
referring to
the precision on g so in case that's
causing any confusion
um
so
the the idea then
uh and what i think is exciting is to
then think about all right well if we do
the same treatment right what does it
mean to have this higher level state now
s1 s2
as superscript 2 which parameterizes
other precisions within the model
because that now goes from an
attentional state to something quite
different
so we can talk about these individually
and
from a
practice perspective this is what this
is what i'm
most enthusiastic about because
there's a lot more to meditation
practice for instance and also just sort
of cognitive
mental or catalog of mental action than
paying attention
you know there's lots of other things
that we're doing so for example
um
the notion of acceptance or
equanimity
um would be the technical term
where does that live what was it what
does it mean to be in a state of
equanimity
right and here we could uh define that
as a as an s as a factor of s2
stay which is modulating the precision
over our preferences
gamma c
right
to kind of give an idea here of how we
can start talking about this so a state
of acceptance would be you know or state
of sensitivity would be the opposite is
to what degree are we allowing our
preferences to impact our
um
actions effectively
uh and so
you know in the in the example uh that
you said in the beginning there dean of
like sitting still you know how
important is that i think yeah that came
from you then
a big part of that is acceptance right
is being able to be okay with the
discomfort that's arising from you know
whatever whatever is going on
and that's also something that we're
explicitly teaching that is a that is a
instruct that is an instruction
um
that is important and a big part of what
makes it all work and when i say it all
work
it's leading to
happiness right like it's leading to
well-being
um and so you can start to
you can start to do that game with these
different different preferences you know
if you outside these different
precisions and see what it would mean to
affect a policy over them and then you
have to do this like i said kind of
um delicate work of translating that
into you know a phenomenological kind of
uh interpretation but i don't think
that's impossible and i think a lot of
it lends itself quite well intuitively
to be able to do that because of this
sort of bayesian
um space that we're in of beliefs and
beliefs of beliefs and different kind of
forms and the way that we talk about
precision and sorry preferences and
habits
and
the point there for me is that
you can start to figure out
what is causing or what a kind of
instruction you would need to alleviate
different kind of um dysfunction or
um unpleasantness so for example
ryan smith um put out
and colleagues put out a great paper
recently on gut inference
um and the point there is they're trying
to
develop a model for
um
you know the ways in which inferences
from the gut could go wrong and try to
see if that could be related to
overeating and one of the one of the
things that's come out there is that
the
one of the ways in which um people's
you know well-being is effective comes
from this
tendency for priors to get frozen or
like not be updated very well
and
in in that context it means that you
know people are
um
effectively
i mean the reason for that is that
you're you're selecting attention away
from uncomfortable sensations of hunger
right
so if you are continuously selecting
away because you have a preference
against hunger sensations then over time
the priors around hunger and your
behavior and hunger gets frozen because
you're not updating updating those with
any new observations
so what's the solution there right like
how can we actually help somebody in
that situation and well this this gives
us a bit of a hint is that maybe what
needs to happen there is a training in
mindful acceptance of sensations of
hunger because that's where in this sort
of precision
dynamic and cocktail of interactions
things are going wrong and if we can
kind of translate
practice instructions or internal
instructions into into this this
framework then it gives it gives uh
avenues for
alleviating different forms of um
different ways in which things can go
wrong here
thanks just one comment thanks just one
comment then scott and then could you
mute lars
speaker set up for different speakers
set up for you yep
you said about instructions that might
alleviate some non-preferable state and
that really recalls our discussions on
instructionism and interactionism
and how active inference lets us think
about
one extreme with the instructions like
the cues and then on the other extreme
who knows how many ways it goes with
what it looks like to interact and
co-develop
based upon
a total model
or even parts of a total model
rather than to up
high level x in blood that means you
need to take the x blocker or if it's
too low you take the supplement like
that could be approached here oh
parameters too high lower it
it's that sort of biomarker driven
approach
that maybe we can move beyond when we
have a rich generative model
and then we can underlie
go into underlying factors
informed by information rather than just
trying to follow up on mathematical
parameters and um constrain people that
way
so
um if you want to say anything or scott
okay scott
so um that last part in the equanimity
brought me back to ecwid the equity
thing again i was reading from this book
the aristotle thing before and it's it's
interesting because in a way it's a
correction
to too much
um sensitivity i guess and
you know or the correction of the
general rules and aristotle's words and
it got me thinking
you know
and and this is something we may have
talked about i'm just trying to remember
the phrasing
it feels like what we're talking about
there is that the models themselves are
engaging in a peer-to-peer discussion
with each other
to refine each other right so the models
yeah
it's never one model it's right i always
tell people if i'm trying to explain
active inference i say if you're in the
woods and you don't have a flashlight
and it's dark you're not gonna run full
speed ahead you're gonna stick your hand
out that's the active part and feel if
there's a tree
and if there's a tree you're not going
to run forward straight into the tree
you so you now you change your model
there's a tree in front of me that's how
i maybe that's a bad way to explain it
but that's how i explain but this the
thing is it's not just a tree there's
also a model of the rain and there's a
wolf chasing you and there's and you and
you're hungry there's 17 things going on
so
what it feels like
is in intention
we bring our models to bear in a
peer-to-peer discussion internally
and do we do we already use active
inference to model the internal model
discussion among models has that already
been something we've talked about in
earlier session i don't remember but we
know we have a zillion different things
going on that are agenda in our heads
that motivate behavior right and so when
we're trying to correct behavior or
address behavior or become aware of
behavior
we bring the other models to bear to let
us do that now again they're all
borrowed ultimately from the externality
but once they're on board can active
inference or does active incidence
already has it been brought to bear to
that internal discussion among the
models that then informs the decision
making thanks
i believe the closest that we've seen
one example is this nesting which we'll
get back to when we return but it was
mark miller at all with their discussion
of happiness with the drives for like
low thirst you know low overwhelmingness
for one stimuli versus another there's
like a sort of domain-specific
optimization and then there's this
cross-domain
optimization that has to do with this
like eudemonia well-being component
whereas the sort of hedonic drive is the
domain specific that's the department of
thirst department of hunger and then
those are being optimized in potentially
recursed levels as well so that's one
way it's gone was that mapping onto
classical philosophical concepts
of
well-being success and then um another
direction has been
also linking it up a little bit more
graphically i think in this type of work
but nice insights scott
just one on that just a response to that
when the imp of the perverse which is
that edgar allan poe notion that people
act against their own self-interest to
show they have power
it's called the imp of the perverse
and the idea is that people don't take
vaccines because they want to show that
they have efficacy or whatever so the
it's interesting what you just said
explains that nicely because the state
that they're seeking is a state of
perceived
efficacy
and it may and it is overwhelming
perhaps some other things like the
health thing or whatever so that's kind
of an interesting notion we just raised
all our today is just that it we always
got to keep that realism instrumentalism
she said there's 17 things going on well
not if you didn't model them
that's a claim about how it quote is out
there and that's a second order question
so if it's if it's an allusion to some
causal process inside of some people's
head
that's different than saying i fit a
model that has this hidden variable and
that is
this intersection of
mathematics and qualitative experience
that
is so tantalizing and so important to
how we think about it and frame it so
it's nice insights though blue
so what scott just said made me think of
um you know scott scott was talking
about how our own models interact with
one another right like the desire for
thirst or hunger or you know to regulate
temperature or whatever
um but but really like
where can we start to model each other's
models
because i think that that in this like
collective kind of dynamic and that was
something that i brought up in the dot
zero like this collective phenomenon
like my
model of daniel updates every time i see
daniel he is as i expect him to be but
then you know suddenly like if he were
to be you know purple or something then
i would have like the mismatch right so
our models of each other are constantly
interacting
and and where where can we start to
maybe
look at this or think of this
in what aspect
i love that point
because
what
what break what comes to mind for me is
is in this context of as you are
i mean to respond to both of your points
really like the
what we're talking about here is a model
of our model right as you move up in the
hierarchy you are modeling your own
model you're getting some beliefs over
how the precision in the lower levels
are
are evolving and so you've got a model
of your
your model as you go up but what you're
also learning there is
the
how your mind works and how
um
you know different
states lead to different
like affect for instance and as you
continue to do that right as you
continue to learn how your own mind
works and you get more and more
awareness of how things go in your mind
well then naturally that you
you are also learning about how other
people's minds work as well
and
there's always this kind of tension
between
um
sort of compassion in practice and
awareness in practice or tension there's
this kind of duality between the two and
they kind of seem to come come together
out of a model like this whereby you're
training in awareness of your own mind
and what you end up discovering is all
how difficult it is actually sometimes
for things to go well and
fundamentally that the one thing that's
driving it all is your own desire to be
happy
as you learn that as that really becomes
part of your own model then that
naturally projects onto everybody else
and you kind of get this
rebound of oh but then everybody else is
also trying to be happy and it's hard
for them too and
you get this kind of natural
compassionate
response then that comes that comes as a
result
that i think also is related to this
idea that scott was talking about before
which is that none of these things
happen in a vacuum like my own
well-being is very so so
intertwined with your well-being
and so all these things kind of
grow then
together
nice it's almost like in in scots forest
one element is there's other people and
maybe non-people entities in the forest
and then another aspect would be like
you can modify your niche you can you
can walk different ways you can use
technology and it's sort of that
tension between how sort of slam dunk it
is for a very constrained case
wanting
and sort of hinting that it could
generalize that more because of the ease
at which it can integrate not just
within a domain like the mountain car or
just thirst but across domains
especially in a way where all the
benefits of the first level relatively
speaking like the computability and the
interpretability of parameters if one
believes that then it exists also at the
second level and higher levels so like
figure five you have the three layers or
six but then twelve the generalized
model like you only had two with it i
guess implicit hint that you just do it
again
yeah yeah it's just yeah so pretty cool
dean
d
i mean just to just to speak to that
point i mean um
you you can and i have um and you can
start to think about
you know the the third
level
the sort of third level equivalent of
attention was sort of awareness of
mental states
right so now it's like you're not you're
not just aware of where your attention
is but you're aware of how much you
you know to what extent do i want here
to what extent am i certain about my
environment to what extent am i happy to
what extent am i um doing things
automatically to what extent am i being
influenced by my memories and priors
right that to go through the whole
gambit there but then you could do the
same thing with
b
at the third level gamma b that's okay
so what is what is that state telling
you
and so well to what extent is my mind
volatile
so how confident am i about the
transitions of my mental states
right and let's say you take a
psychedelic or something and all of a
sudden your mental states are all over
the place well then maybe that precision
at the third level would drop because
now you don't have the ability to
predict how your mental dynamics are
moving
or see you know to what extent am i
am i wanting or not wanting particular
mental states um as opposed to sensory
observations
you know like how much how how much
attachment do i have to joy and fear
right now um is what you'd be inferring
at that level and you can kind of keep
keep going keep going through that
thanks
dean
yeah so
i know we're getting close to the end
here and i just kind of wanted to bring
this up so
my history just a little bit of context
was that i i was
a context generating programmer for
uh high school kids and i wanted to take
them
from a place of subliminal to liminal to
understanding what the edges were what
the limits were
so my my basic job was unnesting
learners having them transition but
having them take a model outline along
with them so they weren't
kind of going naked into the forest
so what one of the things that we used
to talk about in this transitioning
across basically the deep generational
transformation was
using a street metaphor
starting with perceiving
so which is which kind of is unplanned
and moving to thinking about thinking
which is
plan and attend and attend and plan
and then this was the critical piece
realizing the inside the lines
versus the outside the lines and with
the example that we use is that
there's a kind of a crosswalk logic
calculation problem
so you use logic to push the button that
it gets the flasher going before you
enter the crosswalk
you stay inside the lines you even
have perfect gating and balance
so that you can look at your phone while
you're crossing the street through those
lines of immortality
and now you're dead because there was a
car a driver driver in a car who was
also looking at their phone and then an
accident occurred so
the question you had then was did you
follow the logic did you use the rules
and the answer was yes
and were you aware of the free energy
gap and the answer was well not anymore
because logic tends to point at the
jaywalker and ask what are they thinking
i mean come on they're taking the risk
here
they're prob those jaywalkers are
probably thinking about the opportunity
that there's no cars coming at me right
now or on the street they're not present
so they're thinking about the context
and the directionality
of the transition and they're also
thinking about the rate of travel how
fast can i get across the road and will
i get a ticket will there be somebody
who's going to catch me in
and pull me over
all together who's making a decision
based on more information from which to
update and i think this is the big
question around precision
after all our parallel lines in the
street and in the mathematical
operations context
supposed to represent logic and
precision i think they are
and in this case and based on this slide
right here this is why i liked you
talking about
math is not the territory
math does allow for the sketching out of
territory and sometimes we can get
inside the lines
and think that we are using the logic
when in fact we're actually going to be
more precise
and actually use
what i would think to be logic based on
more information once we get outside
those lines so when i think when we get
into the point two of this
i think that's going to be a really
interesting point because steven talked
about it was steve and you were
wondering
lars who was the person who's talking
about being really still
that was stephen before he had to take
off i wanted i'm kind of wanting to
think about this as being really active
and being really contemplative and being
really precise and then be able to sort
of tie that in with the um
the metacognition piece because i think
it's the transition here
that all of us are trying to parallel or
trying to sort of piggyback on your
paper and i think it's i think it's i
think that's the real value in this
conversation i also think that we can
get outside the lines and learn more
than we often do while we're inside the
lines because you know i'm immortal now
i've got these two white lines
protecting me
and that's not always necessarily the
case
yes yes exactly i mean this what you're
talking about there
for me speaks to this
power of
um
suspended belief or uncertainty in our
own
maintaining a sense of uncertainty or in
our own model so that no single belief
can become so rigid and enshrined that
it's resistant to updating in the future
and if you spoke to inesh and mark
miller recently you know there
there is kind of down the same line that
a lot of a lot of dysfunction a lot of
um low states of well-being comes from
that rigidness and that freezing of
of beliefs that then you know leads all
kinds of afferent behavior um afterwards
because you're trying to fulfill the
expectations of belief that isn't being
updated
the the
what's on offer here is a mechanism to
describe
how you might remedy that solution by
deliberately controlling
uh or inquiring about the the
metacognitive belief so gamma b in this
case uh over my priors and if i can
control that state transition well then
it gives me the opportunity to relearn
that b matrix at the bottom because i've
injected a little bit of uncertainty and
now i'm more able to sample information
that is counter to what i know
um
and allows for you know just better
optimization ultimately
yeah take the model along
thanks dean and
awesome insight there so just in the
last couple minutes to dave any textual
questions live chat any final questions
and then scott and then blue if you'd
like to make a last comment
so go ahead scott
so that um dean what you were just
saying there goes to that what i was
trying to fuss with on that equity point
before where it's the rules of general
application and what i realized while
you were saying the reason the equity is
so fascinating to me is what they did in
law and equity is they said okay the
rules of general application don't
always lead to the right result
and what they've now done is collected
all the remedies for the bad results and
can characterize those into groups
so you may have a rule of general
application and then there's something
out there in equity called unclean hands
which means if i did something wrong if
i'm a burglar i can't sue you if i trip
over your coffee table right that's
unclean hands right or the doctrine of
um unjust enrichment means if i find
some money and or if i get some extra
money you pay me too much give me an
extra 20 bill i say i keep it because
you you gave it to me but it wasn't
meant to be it's unjust enrichment so
equitably you should give it back where
i find someone's wallet all this stuff
right so the reason i when you were just
talking made me realize you know
it may be
that we apply the rules of general
application
and then we find some exceptions
and then when we start or some ways they
don't apply the right way in active
inference and maybe we start to cluster
those
bad results let's call them or
unintended results or something start to
cluster them and characterize those
like they did in equity so that's what i
was groping for before is the rules of
general application can have great value
and they need those corrections and
those corrections themselves may have
clusterings and groupings that
themselves can be
managed
thanks great discussion by the way thank
you so much lars is fascinating stuff
yep thanks scott blue
yeah i'm looking forward to more next
week hopefully if you're available um
and maybe kind of probing the different
types of meditation and i'm not sure how
familiar you are with
different kinds of meditation but i've
done a bunch and highly variable and
maybe whether or not they all fit this
model or not is something i've been kind
of thinking about and i'm gonna think a
little bit more about that um over the
next week so thanks for the great
discussion
cool
thank you
thanks blue i think it will be good to
um
see if anybody who's listening in the
intervening week wants to join or if
they just want to
watch along next week so they can ask
questions
and uh i think exploring that aspect of
group
active inference agents by design or out
there in nature that we've been
discussing a lot you know when is it is
it can we model it that way and then
asking well can't we have nested
metacognitive models of groups
what does that mean is it a different
philosophical bridge is it two exits on
the same freeway
what is going to be the relationship
there
so
great times thanks lars and if you have
any final comments otherwise we'll end
it
no thank you this has been really great
i had a really fun conversation thank
you for your kind of openness and great
questions and i just really enjoyed the
energy here it's not been a
at all if you see what i'm saying so
thanks awesome
peace out everybody see you next week
