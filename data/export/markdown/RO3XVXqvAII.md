---
title: "ActInf Livestream #052.2 ~ Geometric Methods for Sampling, Optimisation, Inference and Adaptive..."
category: "Livestream"
series: "Livestream_052"
episode: "2"
speakers:
  - "Geometric Methods for Sampling"
  - "Optimisation"
  - "Inference"
  - "Adaptive..."
duration: "1:56:25"
url: "https://www.youtube.com/watch?v=RO3XVXqvAII"
views: 137
exported_at: "2026-02-18T22:37:37.800920+00:00"
format: markdown
---

# ActInf Livestream #052.2 ~ Geometric Methods for Sampling, Optimisation, Inference and Adaptive...

Hello and welcome. It's ACTIMF livestream 52.2 on March 9th, 2023. Welcome to the ACTIMF Institute.
We're a participatory online institute that is communicating, learning, and practicing
applied active inference. You can find more information on these links. This is a recorded
and archived live stream so please provide feedback so we can improve our work. All backgrounds and
perspectives are welcome and we'll be following video etiquette for live streams. Head over to
activeinference.org to learn more about getting involved with projects and learning groups.
All right, we are back in livestream 52.2. In our third discussion on the paper geometric methods
for sampling, optimization, inference, and adaptive agents, we had a .0 background and context video
and last week Lance joined for 52.1 where we had a great overview discussion on the paper
so today we're going to see where it goes, see where our last week has taken us and how we're
thinking about it or curious about it. If you're watching live, of course, feel free to write
questions in a live chat. Otherwise, let us pick up on a mostly blank slide and uh just thanks again
Lance for joining. If you want to give any sort of introduction or recap opening here, go for it.
Lance
Lance
Lance

Lance
Lance



Lance


Lance





Male
Lance


principal literature and active inference are used to because here the goal of inference is about
approximating expectations as opposed to just approximating distributions in of themselves
it turns out to be these two perspectives turn out to be dual but i guess here we want to develop
notions of divergences and discrepancies that are a bit more general than the kl divergence
and that can use to solve problems that the kl divergence cannot and i guess the overall
picture for what we want to do that is the kill divergence turns out to have a lot of really nice
properties that we can discuss one of them is that if the kill divergence is reduced it means that that
the two distributions in play are more similar in terms of information so there is this idea of
information monotonic monotonicity where the kl divergence sort of yeah given ordering as to
what extent two distributions quantify i mean so if you have three distributions and you compute the
kl divergence between them and now kl of a b is lower than kl of ac it means that b is more closer in
terms of information to a than c is to a so you have this really nice thing that is captured by the kl
divergence with which makes sense when we're dealing with information the kl divergence also has so many
other nice properties um it it's not a distance but it turns out to behave a bit like a square distance
so you have this kind of like really nice pythagorean theorem um and i won't get into the exact statement
but it's like if you have uh a b and c distributions then kl a b plus kl a c equals kl b c if you have like a
rectangle triangle if abc define a rectangle triangle in information space um you have other properties
like the kl divergence gives and so on um so the kl divergence is in general i would say the distribution
the divergence of choice but it turns out that in many cases you just can't use it for example when
you have samples and you want to approximate some samples with a distribution then the kl leverage just
is not going to worry there so you need to derive some other things so this is to say that we're
considering statistical inference a bit more generally than what we do in active inference in general
and so this speaks to why the uh the section here is a bit different from the standard uh inference
literature that that we usually consider and then i think that the well then this section 5 which is
about active inference and i think we should discuss that a little bit more because the formation of
active inference that's presented there is to my mind the most general and also the simplest concept
conceptually that's been out there i mean we sort of like recap the derivation of active inference and
also like the properties of the expected energy properties of active inference and also how to scale
active inference and so on and we do that in just seven pages or five or five pages i mean it's just very
short um so it's dense sure it's like a really concise summary and actually from there you can really
derive a lot of you know uh technical papers on active inference it's like to me it's the most general and
if if you as a reader can understand that section then you can sort of really understand what active
inference is about um so yeah this is kind of the overview for today um i would really like to be
discussing questions because last time we really discussed about most of the papers so but yeah
whatever comes up awesome all right great well let us uh talk about some of the more foundational pieces
of the points that you raised about the kl which generalized inference beyond how it may have been
brought up in other act inf and then we can spend most of the time in section five and looking at some
of those figures connecting some of the intuitions about the ball rolling down the bowl to the person running
so sounds good on hamiltonian monte carlo where do you want to pick up sure i mean so i mean donian so
last time we discussed a lot about the problem of sampling and why that's a difficult problem
and we arrived at the conclusion or or i presented like monte carlo methods how they work so you're
basically running um a stochastic process like a random random motion and sort of the this
distribution defining the process is going to convert to a target distribution which means that when you
run the process long enough then every point that it's going to be in is going to be like a sample of
the distribution that you want to sample from um now there's a lot of issues with that um i mean
conceptually it's not so difficult but actually when you want to implement this in practice it turns out
to be really hard because if you just implement the simplest stochastic process to sample your target
distribution um it's going to be extremely slow and i think that's the main bottleneck when
developing monte carlo methods monte carlo sampling in in general is slow and that's also one of the
reason one of the reasons why one might want to do variational inference instead of sampling
um so something is slower but it's also more accurate it can approximate our distributions that
are completely arbitrary so if you care about accuracy then and you have time and computational
resources then for sure go for sampling if you care about speed about doing things online and you
don't care about accuracy so much then the right no inference is the way to go at least that's my
understanding right now so um let's say you wanted to sample a distribution in a continuous space so it
could be um just as last time let's imagine the state space is the desk where where i'm at and you sort
of had this distribution which could be like multimodal uh very weird and you just want to take samples from
there um hamiltonia monte carlo is probably the state of the art methods method to do that there's a
lot of other methods out there but hamiltonia monte carlo typically just works very well um and in a
wide variety of situations and so the idea of hamiltonia monte carlo is you're gonna augment the state space
with um so let's let's say that the original state space you start with are the positions
and so you're gonna augment that with a velocity state space so you kind of if your original state
space was euclidean space of n dimensions you just end up with a nuclear space of two n dimensions
so you double the size of the state space and now you say okay well um the distribution that i want
to sample from actually defines an energy landscape um so it technically technically it's like if you take
if you have distribution which is p then minus log p is an energy landscape so um points where minus log p
is low are points where p is high and so these are points that you want to sample a lot from
and contrary wise um if minus log p is very high then p is low and you don't really want to go there so
much because these are points of low probability so i think this minus log p actually there's many reasons
why minus log p is is meaningful in physics but just note for now that minus log p is just like a function
and the minimum of the function of the of that function at a high probability point and uh these are high
these are high energy points where you basically don't want to go to go there so much um so let's call
this minus log p potential energy and so this is what this really is in physics if p technically in physics
p would be gives measure um what people call an equilibrium distribution um last time we saw like
soft max of minus something the something is the is the potential energy um anyway and so minus log p would
be the potential energy and then if you if you add kinetic energy on your velocities um then you get
what's called the hamiltonian which is the sum of the potential and kinetic energies so what is exactly
the kinetic energy the kinetic energy is like velocity squared pretty much so if you add remember that your
state space is position and velocity if you add and you take a point in state space the uh so you would
have um kinetic energy which is velocity squared and a potential energy which would be minus log t
now if you add the two together what you get is a hamiltonian which is the sum of the kinetic energy and
potential energy and this is just standard physics hamiltonian is a sum of kinetic and potential energy
and it gives us the total energy of the system um so why we started with the problem of sampling and
here i just told you something very complicated where we get a hamiltonian there's actually a good reason
why we want to do that and it comes back to the idea of geometric integration that we talked about last time
which is that um typically maybe i have a process that i know would will give very efficient sampling
but actually when i implement it on the computer in discrete time i just lose all the all the properties
that make that something efficient so actually it turns out that most people working in monte carlo sampling
they're working on efficient discretizations of continuous processes as opposed to on the continuous
processes themselves really the bottleneck and the difficulty here is is the implementation part
uh implementing process on on a computer like you and i had in such a way that we retain all the good
sampling properties um so one very powerful idea is that of geometric integration which is of preserving
geometric properties of a system i mean geometric integration is the field that develops um computational
methods of uh numerical integration and numerical discretization in such a way that they preserve important
geometric properties of the system here in the gym the geometry in play is the hamiltonian and so you
might think well that's pretty weird i mean a hamiltonian is an energy and here we're talking about preserving
the geometry and preserving the hamiltonian how do these two things fit together and so it turns out that
the presence of a hamiltonian and the fact that we have a state space that has positions and velocity
technically in mathematics what what we then get is what people call symplectic geometry so symplectic
geometry is just arises when we have those state space that comprise positions and velocity and when
where you have hamiltonians so this is just like a way of explaining why the hamiltonian uh why the hamiltonian
is like closely and intimately related to geometry so geometric integration enables you to um to yeah to
discretize processes in such a way that the hamiltonian is preserved now when you think about the hamiltonian
the hamiltonian gives you the energy of a particular point in state space and so if you simulate trajectories
that preserve the hamiltonian what you're effectively doing is sampling from the contours of the probability
distribution contours that have the same probability so you're basically going around let's say for example in
circles um in a region that has the same probability when we want to sample we want to go everywhere i mean
we want to sample regions of high probability low probability and want to be able to go from one to the
other so what geometric integration allows us to do is to simulate dynamics that are going to preserve the
contours of the probability distribution and they're going to do so very well the advantage here is that
when we use geometric integration to simulate hamiltonian dynamics which are conservative and again
stay in the contours um what geometric integration allows us to do is to take time steps that are very long so it enables us
to travel very far in the landscape while still preserving the hamiltonian so you don't need to take very small
time steps to remain accurate and preserve the hamiltonian but actually geometric integration allows you to you know
take very long time steps and still preserve the hamiltonian so now we have a dynamic that's hamiltonian
preserving that's just very good because you can take very long time steps and that enables you to go around
the contours of the probability distribution so what you want to do next is you know to change contours you
want to go to contours that are of higher probability contours of lower probability and you want to do so
in a way that the contours of high probability are sampled much more and much more often than the contours of
lower probability so what you do is that you augment your hamiltonian dynamic with what people call a
velocity refreshment or a momentum refreshment and so this is how it works how it works um so you're gonna
yeah simulate your hamiltonian dynamic for for some time and then after after a while you're gonna be
like okay well now i'm gonna i'm gonna change the velocity at random by by just drawing a new velocity
from a gaussian distribution and so by drawing a new velocity from a gaussian distribution you're just gonna
change contour completely and then there's what's called um and and then there's the constraint that i
just talked about which is you want to change contours of the probability distribution in such a way that
contours of high probability are visited much more often than contours of low probability so you want to
preserve that you want to do that um proportionately in a way so the third ingredient of hamiltonia monte carlo
comes in which is uh metropolis hastings and so metropolis hastings is this accept rejects that that we
discussed briefly last time and so metropolis hasting is just super clever and it enables you to to say um
um to it it just tells you whether this um this momentum refreshing step is actually a good one
or a bad one and should be rejected a momentum refreshment is good if overall your sampling is gonna
remain um is gonna remain faithful to the target distribution but it is bad if it remains unfaithful
useful so actually um running this metropolis hastings except rejects that allows you to change contours of
the probability distribution in a way that remains faithful to the target distribution and so there you go
that's basically hamiltonia monte carlo so to recap you augment the state space by adding velocities
uh this allows you to build a hamiltonian by declaring that the original probability distribution gives you
potential energy and you add a kinetic energy on the on the velocities which is just velocity squared
because you have a hamiltonian you can um you can use geometric integration to simulate hamiltonian
dynamics very accurately and with very long time steps the very long time steps is a crucial thing
because it means that with very low computational cost you can sample very far so it means that you
don't get stuck in a region of the probability distribution but you can actually visit it much more
fast and efficiently so that's the first part um the problem with those dynamics again is that they
remain on the contour of the probability distribution and so you want to sample the whole probability
distribution so what you do is every once in a while and i think that's a hyper parameter in your in
your sampling algorithm let's say every 10 iterations of the hamiltonian dynamic every 10 time steps of the
hamiltonian dynamic you're going to sample um you're just going to randomly take a new velocity so you
you're going to change contouring the probability distribution and the crucial point there is you want to
change contour in a way that's faithful of the probability distribution and that's faithful of the
sampling problem that you want to do there comes the last thing which is metropolis hastings which
ensures that the momentum refreshment will be uh good for sampling i mean will preserve your target
probability distribution so with that you just get a very efficient um sampling algorithm and so it seems
a bit convoluted right um the and one bottleneck of course is that you need to double the dimension of
the state space and if your state space is already extremely large that could be a bottleneck um it could be
the case that actually doubling the dimension to add velocities uh it could be a computational bottleneck so that's
a problem um but still in most cases that's not a problem and um so again hamiltonian monte carlo is
convoluted but the overall take-home message i i would want you to to take from this is that it is a method that
that remains faithful to the probability distribution that i want to sample and this is crucial
and it is also a method that through geometric integration it enables you to take time steps that
are very long and still get accurate sampling so this is the the really cool thing um if you
you could come up with a whole bunch of other methods that did not require to you know double the
dimension of the state space or that didn't use geometric integration the problem that you would
probably run into is that the over that that the thing that you came up with when you implement it
in the computer it doesn't exactly preserve the the the probability distribution that you want to sample
and so the problem with that is that this would lead to biased sampling and by a sampling by something is like
you're going to you're going to you're going to you're going to sample a different probability distribution
which might be just a bit different but still um a different probability distribution than what you
really want to sample and this would bias your your predictions so the really cool thing of
hamiltonian monte carlo is that you're actually able to have unbiased sampling through the metropolis hastings step
um and this is the crucial thing so it's computationally implementable in general there's no computational
bottlenecks apart from this doubling of state space and it leads to unbiased sampling and it's also
relatively simple so this is why this is really used all over the place there's um there's another few
perspectives that might explain why it works so well so in in the paper in in section in the last subsection of of uh
of section two which is about optimization um so the the section on optimization is about how to accelerate optimization
how to derive an optimization algorithm um yeah yeah 2.6 yeah that's the one so the whole thing about section two
is about deriving an optimization algorithm that accelerated in a physical way and by mean accelerate
what i mean by accelerated it's not about just going faster but it's about having acceleration
um which means that um so if you go slightly up in the paper on the figure
i think this figure is great and by the way i wasn't the one who who came up with this figure but i
think i think this figure is great it really gives a lot of intuition for what acceleration really is so if
you if you look at the at the green cup i don't know how you call this at the green well on the left
uh this would be like um a ball rolling down uh the well in like uh and the well is filled up honey to
to like a certain level and so there you get a lot of friction so your ball would just roll down very very
slowly and the speed of the ball would be proportionate to the slope of the well
um so this is not accelerated because there's a lot of friction and so the speed is just proportional to
the slope of the well and this so this is actually what grade in the sand does but now if you go on the
right you get what people call in physics on underdamped system which is also an accelerated system a
system that's meaningfully accelerated so if you replace the honey in the well by some water then
there's going to be way less friction and your ball is actually going to accelerate and overshoot the
minimum of the well and then sort of stabilize but the point here is that this um this bowl is just going
to get so much faster to the minimum now um so let's say that we just um i mean so this optimization this
idea for optimization is is just extremely powerful and um and by the way on the right hand side in the
graph you can see the improvements that you get when you when you implement these sort of ideas so this
was on um i'll come back to to sampling in a bit i promise but this is actually very well very related
you you can see on the graph on the right what kind of improvements you get when you go from a under
that first order system grading the sand system to a what when you go from an overdamped first order
building the sun system to an underdamped second order accelerated system and so you can see the curve
right um so the black slash orange curve is overdone there's no acceleration it's very slow um the the last
curve the the blue one it's accelerated and it's just super fast so you can see it sort of gives you like
um quantitative uh data as to how many improvements you can get by implementing this um acceleration
in a physically meaningful way could you describe the axes of the graph and also what the lee group is here
um so the lee group is um so in in the figure legend in the fourth line you see the lee group is so n
n so that's this um technically that's the special or orthogonal group of dimensions n and so if i if i
remember correctly these are all the matrices all the square matrices of size n by n that have a determinant
equal to one so the determinant is just like um a function where you give it a matrix and it gives you a
number the fact that um the fact that the determinant is equal to one means that here we're just taking
matrices which are um which produce trend not translations but um changes of coordinates that
preserve the geometry in a system so so so just to to elaborate on this a little bit because
for people who are not intimately familiar with matrices it might seem a little opaque so when you
have a matrix a matrix can multiply vectors so a square matrix takes in the vectors of size of dimension n
and it outputs vectors of dimension n by multiplication so if you have a square matrix
matrix it just induces a transformation of your state space because each each vector each point which
is a vector gets converted into another point which is another vector now um the so there's a lot of
i guess properties there right you could have all sorts of translations of state space or rotations in state
space or transformations of state space if the determinant of the matrix is equal to one it means that the
transformation of state space that the matrix induces uh will preserve the geometry of the six places it
will preserve distances if you and it will preserve crucially orientation as well because if the if you only asked
um the determinant to be equal to one or minus one then you would the the matrix transformation would preserve the geometry but it would not preserve the orientation it could like mirror things
um so if you only asked the determinant to be equal to one or minus one you would get a lee group that's called the orthogonal group which is usually denoted o of n and here we we require the
the determinant to be just equal to one and so you get the special orthogonal group and so it's this group of matrices that have this property
now this is not um really i mean this is not really important for the example here because you could have taken any other d group and got something similar
uh and got a similar difference in performance but but um yeah i guess it's just interesting for its own take
um and so the graph though the k is the number of iterations so the number of time steps so that's the x-axis
and the um the y-axis is how close you are from the minimum
um and and it's in the log scale so as you can see the the blue curve is going to get like in 100 iterations
it's going to get basically a 10 to the minus 4 10 to the minus 5 distance from the minimum so it's like
super super close it's basically gets there in 100 iterations uh when you take the other normal gradient
descent methods where you see that it's going to take so much longer um so yeah this is really the
advantage of using second order methods and what i mean by second order methods is that by second order
means that you actually double the state space to introduce velocities so that you not only have a
dynamical system over positions but you have a dynamical system of velocities and so it means that you have a
a physically um a physical notion of acceleration because acceleration is a movement of velocities
um and so if you double the state space by saying this is position this is velocities and you say i have
a motion in this like a state space that's twice as big then you have a meaningfully a meaningful notion
of acceleration and this is really powerful and so you can see already a parallel here which is
that Hamiltonian Monte Carlo also has this notion of acceleration in some way at least just intuitively
because we we also uh double the size of the state space to introduce velocities and so it turns out
that this intuition is actually uh you can make it into a formal correspondence um and this is i think this
is something that quite interests me to be honest um so if you if you remember if we come back to the
intuition for sampling the intuition for something through Monte Carlo methods is we have a target
distribution that we want to sample from so we're going to run a dynamic a random dynamic towards that
towards that distribution now what makes sampling efficient is that the distribution that characterizes the
process because again the process is random so each time it is at a random location that is characterized
by a distribution what makes sampling efficient is that the distribution characterizing the process just
converges as fast as possible to the thing that you want to sample from so there is this is to say that
you can think of sampling as an optimization on the space of probability distributions you want to
move your probability distribution of the process as fast as possible to your target and so you can see
from there that sampling is actually not so different from variational inference um it's just the same idea
only variational inference you're typically gonna like um yeah take a parameterized family of distributions and
approximate the target while here you have a non-parameterized family that's given by your dynamic that's going
to perfectly match the target um so so again so so with that i want you to have the take-home message that
sampling you can think about it as an optimization on the space of probability distributions in the sense that
you have a target distribution and you want to get there as fast as you can with the process now
let's suppose and so here is the crucial connection between sampling and optimization in in the way that we've
described it here
let's suppose that you run this accelerated optimization scheme on the space of probability
distributions
then the the process so you would get the dynamic on the space of the probability distributions that has a
meaningful notion of acceleration um through through the accelerated method that that was shown here
shown here so if you look at what that what kind of dynamic this really gives you it gives you a process
which is given by a stochastic differential equation that is known as underdumped langevin dynamics
um so there's an equation for it in i think section subsection 2.8 but the point is underdumped langevin
dynamics is a stochastic differential equation whose density or probability distribution
stoles this accelerated optimization problem on the space of probability distributions
so just from there you know that underdumped langevin dynamics is going to be a very efficient sampler
because it meaningfully accelerates and gets to the target i mean quite fast the problem is underdumped
langevin dynamics you cannot simulate it accurately well you can simulate it accurately but you cannot simulate
it exactly on your computer in practice so this comes back to the numerical integration problem that
that we discussed just before um and so you have to to find a way to to discretize or or in other words
implement underdumped langevin dynamics on your computer in such a way that you retain that the
thing that you implemented on the computer retains this meaningful notion of acceleration and so it turns
out that you can see on Hamiltonian Monte Carlo as a faithful numerical discretization or numerical
implementation of underdumped dynamics that's going to preserve these acceleration properties and therefore
these this efficient sampling so this is all like um yeah a lot of interesting connections but basically
what what i want to get at is you really have this notion of acceleration that permeates well i guess physics
but here it permeates sampling and it permeates optimization and so the method that was
shown here about optimization and Hamiltonian Monte Carlo they're just the same in a way only one is
applied to optimization the other is applied to optimization on probability distributions of aka sampling
the other is applied to a higher level and so the other is applied to a higher level and so the
shadow Hamiltonian is what is the shadow Hamiltonian and why does it sound so cool
i know right yeah it's uh it's really cool um it's a recall name so the shadow Hamiltonian is um okay so
so let's go back to the Hamiltonian um so we have a Hamiltonian and we want to simulate the dynamic that
preserve the Hamiltonian we want to implement that on the computer we're going to do that through
geometric integration geometric integration gives you a bunch of algorithms to preserve the Hamiltonian
i mean a bunch of algorithms they can implement on the computer and they're going to preserve the
Hamiltonian um do they actually really preserve the Hamiltonian it turns out that no so what i what i said
before is a bit of a shortcut like um because the numerical integration or that you get through any
any numerical method including geometric integration is not going to exactly preserve the Hamiltonian
but it's going to preserve what people call a shadow Hamiltonian which is almost the same as the
Hamiltonian but with extra terms that sort of vanish if the if the time step is very is very
short um so this is to say that your numerical dynamic uh implemented through geometric integration
is going to exactly preserve the shadow Hamiltonian and approximately preserve the true Hamiltonian
and so there's um in the papers we show um i don't know if it's well it's probably algorithm
independent um but basically depending on the algorithm that you choose you you want to show to
what extent the shadow Hamiltonian truly approximates the true Hamiltonian the the virtue of geometric
integration methods is that actually the shadow Hamiltonian turns out to be extremely close to true
Hamiltonian which means that you can take very long time steps and still be very good at approximately
at preserving the true Hamiltonian so here you don't when you implement these methods you don't exactly
preserve the true Hamiltonian um but you do you still do it pretty well and so in Hamiltonian Monte Carlo
the momentum refreshment and metropolis usually the metropolis hastings actually accept rejects that
step is going to correct it is going to correct for those failures of of truly preserving the Hamiltonian
so even though you have some you don't you don't exactly preserve the Hamiltonian in your numerical
integration in Hamiltonian Monte Carlo the metropolis hastings accept reject step is going to correct for this
inaccuracy. And so this is really the true beauty of Hamiltonian Monte Carlo is that even though
you get a lot of things that are not exactly preserved when you implement things on a computer,
thanks to Metropolis Hastings, overall your sampling is going to be perfect in the sense
that you're going to truly preserve your target distribution. So this is really the key. Now a
follow-up question to that is, okay, well, if Metropolis Hastings is just so crucial and it
just gives your dynamic the property that it's going to preserve whatever it does, even if it
samples really badly, if you add Metropolis Hastings, it's still going to preserve your target
distribution, then why can't you just come up with an average process, like whatever kind of process,
and add Metropolis Hastings at the end. And so you can do that, you can take any kind of process.
And after and to let's say you take a random process, it could be the worst in the world, let's say
you wanted to sample from a Gaussian, and you actually take a Brownian motion. Now this is clearly not going
to work because Brownian motion just goes all over the place, it could go infinitely far Brownian motion,
and it's just like random motion, right, completely random motion. No, there is structure to it, but
there's no, the structure in Brownian motion means that it's such that Brownian motion is just going to
just spread really, really far. So Brownian motion is not going to preserve your target distribution.
So it's going to, and it's also going to be very slow, by the way. So it's not going to be a good
sampler. If you add Metropolis Hastings on Brownian motion, which is you integrate Brownian motion. So you
simulate a step of Brownian motion on the computer, and then you do Metropolis Hastings to use to know
whether you should accept or reject that step. Metropolis Hastings will tell you whether you should do it or
not, you either accept and you stay and you keep going from that new position or you reject and you
start from where you started from and take a new sample, accept reject. If you accept, you keep going.
If you reject, you go back and you sort of go like that. So if you do Metropolis Hastings there,
your stumbler is going to be exact. So it is going to preserve the target. And so you're going to have
accurate sampling. And so this is crucial. This really highlights the importance of Metropolis Hastings.
But there is a big but your your stumbler here is going to be extremely slow. And it's going to be
extremely slow, first of all, because Brownian motion in and of itself, it doesn't at all preserve the
target distribution. I mean, just goes all over the place. And you just want to sample a lot around the
mode of the Gaussian, for example. So it means that Metropolis Hastings will reject a lot of your steps,
because a little of your steps will try to go further away while you want to stay around the mode,
typically of the Gaussian. So you're going to do a lot of steps for nothing.
So you're going to do a lot of steps for the sample. And also, Brownian motion just does not have the
qualities that make a sampler efficient. And so the reason why Hamiltonian Monte Carlo is so good is
because it's able to integrate Metropolis Hastings and still preserve a lot of other properties that make
that make the sampler efficient. So if we remember Hamiltonian Monte Carlo has this geometric integration
that does not exactly preserve the Hamiltonian, but it does still does it pretty well approximately by
preserving a shadow Hamiltonian. So this means already that that integration step is going to be
really good. So there's going to be a lot of acceptance in the Metropolis Hastings.
So and also the way the way the scheme is set up, there's going to be a lot of acceptance step in the
Metropolis Hastings. So it means that most of the samples that you would draw will actually be used
instead of being rejected and you have to start over again. So that's one advantage. The other the
other advantage of Hamiltonian Monte Carlo and this is a crucial one and we kind of discussed this last
week is that one crucial thing to be a good sampler is this idea of time irreversibility. And so I'll
emphasize it again because it's really crucial and there's a lot of literature on this and it's
something that we reviewed also in the paper. So a sampler that is time reversible even if that is time
irreversible. So what do we mean by this? A sample is time irreversible. If and only if were you to play the
dynamics forward or backward there will be yeah so yeah so so going on your bullet point here a sample
is time reversible is time reversible if you were to play the dynamics forward or backward in time
so forward in time and then maybe you would play them by reversing the movie by playing the movie backward
if you were to do that then you then the the two movies that you would see would be qualitatively the same
and statistically the same. So a process is time reversible if and only if the process if you're
running forward or backward it's basically statistically the same. Now what does this mean in practice? Well
if your process is time reversible then it's going to backtrack very often actually
So it means that you you would be somewhere in the probability distribution just sampling there and
you will go forward and then you probably go backward and so on and you kind of get stuck in a region
until you go somewhere else but it's just going to be very slow to move around and so it's going to be
very slow to get you know good sampling because it's going to take you a long time to visit all the regions of the probe into
distribution. In other words the distribution characterizing the process it's not it's going to move very slowly to the target
distribution that's another way to look at it. If the process is time irreversible on the other hand
then it's a lot less likely to go backward during the sampling process so it means that it's going to visit
the target the target distribution a lot more I mean it's just going to go around imagine if you're not
allowed to go backward just as a human being and you're walking around you're just going to end up in
many more places than if you were allowed to go backward and if you were and if you were just going
backward all the time to where you started then you wouldn't be able to to do a lot of visiting so it would
be a bad sampler so so I guess there's some like straightforward intuition there so one idea is
in sampling is we want to optimize the extent to which a sampler is time irreversible we want to
increase time irreversibility as much as we can to force the sampler to just move around as much as
possible so that's an idea and and it is explored currently I guess it's a bit of an open problem of
how do you really do that and how do you implement that on a computer in a way that you know works and
preserve all the properties but the point I want to I wanted to get to is that metropolis hastings is a
blessing and it's also a curse it is a blessing because when you add it to any kind of process
you will make your sampling unbiased so it means that you will sample the right distribution even
though you're implementing this on a computer and there can be a lot so many issues with the numerical
numerical integration numerical approximation and so on but it's also a curse because whenever you've had
metropolis hastings um on on a process it's going to make it time reversible
so actually yeah if you if you just took a random process and added metropolis hastings you would get
something that's inevitably going to be quite slow and so now you get to the you know the problem or the
conundrum where what what do I do do I go for unbiased sampling do I care about accuracy
and then I should add a metropolis hastings or do I not care about accuracy so much
and then I should not have metropolis space hastings and it's going to go faster generally
and so Hamiltonian Monte Carlo actually has the blessing and does not have the curse and this is
why Hamiltonian Monte Carlo is just so good and again it's also complementary to all of the things
that we've been discussing and the reason why Hamiltonian Monte Carlo is blessed and not cursed is
because the momentum the how do you call this the metropolis hastings is just done on the momentum
refreshment step as opposed to being done on the overall dynamic so because if you remember you do
geometric integration to simulate Hamiltonian dynamics now every once in a while you will take a momentum
refreshment and then do metropolis hastings on that momentum refreshment as opposed to doing metropolis
hastings on both the Hamiltonian dynamic and the momentum refreshment and so it's not
it's not something that I can really explain how how that works but it turns out that by just doing the
metropolis I mean Hamiltonian Monte Carlo is a way of having metropolis hastings in a way that you preserve
uh the unbiasedness that's so that your sampling is accurate but you don't sacrifice the time irreversibility
and so and so you get both um and this is because the metropolis hastings is just on one of the components
and not on both
so to kind of connect that to an example as we move into active inference
here we have some probability isocontours
some we have the high probability carpool lane and then we have some lower probability lanes
and uh we can go different speeds in these lanes and we want to have a full accelerated model here
it's almost like the mh is is refreshing our velocity just asking when we want to change the lanes but
it's not our full self-driving car metropolis hastings algorithm but we're able to use our position and
acceleration when we're in our lane to take full advantage of the acceleration following the shadow
road not necessarily the true road but the shadow road is close enough or the shadows on the road and then
lane changes are these computationally costly and reversible but still super useful propositions
exactly and they actually they're actually not computational league costly they would be if you
were to reject many samples uh but here you in Hamiltonian Monte Carlo typically you don't get to
reject many samples so yeah you that's such a i mean that's such a great picture so the car follows the
shadow road by just doing geometric integration and following the shadow Hamiltonian every once in a
a while you get a momentum refreshment a velocity refreshment which is oh um now i move to the
first lane or the second lane third lane and so on and you get a metropolis hastings correction step that
tells that says do i accept this proposition proposition proposal of lane change or do i reject it and so on it goes
so how does this connect to active inference
well i mean great question uh so inactive inference inactive inference proper you don't have any sampling
inactive inference uh whenever you want to scale active inference to implement it to solve any kind of
problem in the world you want to do something because there's a lot of computations that are not
going to be tractable otherwise and so one um one cool example is when it's in the figure after this actually
so um when you want to for any kind of decision making inactive inference you need to approximate
the expected free energy and so uh no the one just before here uh yeah perfect um
um so if you look at the second equation there you get this minus log p of an action sequence
equals expectation of something this minus log p of the action sequence is our notation in this paper
for the expected free energy um so the expected i mean you probably all know this the expected free
energy is given by the expectation of something now um typically and when you have a very high dimensional
model which happens in in most applications i would say you get a very high dimensional expectation
what is an expectation an expectation is an integral with respect to a probability distribution
how do you compute expectations while you do that through sampling or at least um sampling is the way to
compute high dimensional expectations that's the most efficient in statistics and this is the reason why
um something is studied in statistics it's because that's how you solve these problems i mean
expectations just come up everywhere um just like so many things about machine learning
bow down to computing expectations and so here in particular the expectation that is very dear to
to us very close to our hearts is the one that gives you the expected free energy the expected
free energy is the expectation of something so how do you compute that in a high dimensional model
uh where you have to use something and so there comes uh the usefulness of hamiltonian monte carlo
if you have a discrete state space model you're not going to be able to use hamiltonian monte carlo because
hamiltonian monte carlo is on continuous state space models um it's on continuous state space right we talked
about continuous positions continuous velocity i talked about something a probability distribution on my desk
which is a continuous state space so you're not going to be able to use hamiltonian monte carlo
if you have a partially observed mark of decision process and you're doing active influence there
but if you have for example i've been talking recently to ryan smith um who who does a lot of active
inference and and he's really leading a lot of the modeling work with active inference and real data of
patients of all sorts um many medical data and also using active inference to model psychological
experiments and um one of the things he told me about well is okay well i have a bunch of data and
partially observed mark of decision process is just not going to do it why is it not going to do it because
the data that he has is lives on a continuous space i don't remember exactly what it was but let's just
say for the sake of example that that data was you know the temperature in the room and and people had to
the the subjects had to infer the temperature in the room based on their sensations so that's a continuous
state space problem now imagine that you asked you asked someone to infer the temperature in a room
then maybe you would change the temperature in the room or not and you would ask them again change the
temperature or not and ask them again and so on in when you have this sort of setup you have a discrete
uh you have a phenomenon that unfolds in discrete time because you just repeatedly ask some question
and sometimes elapses between the questions um but you also have a state space that's continuous
when you have this sort of data then the kind of model that you want to use is a partially observed
mark of decision process that like we know and love but the state space is going to be continuous
instead of this week the time is still going to be this week um now when you have this sort of model
and i just want to say it as an aside or as a yeah as an aside that for the moment a lot of the
modeling work and and simulation work in active influence uses discrete state space on the piece
partially observed mark of decision process just because it's been sufficient and when you simulate agent
is often like in great worlds and when you maybe have a state spaces in experiments they often by design
discrete because it's just easier to handle but that's not something that that's not an assumption
a simplifying assumption that we're gonna have that we're gonna be able to keep for you know that much
longer i mean there's just so many things that you cannot account with these sort of models so one
other model that is interesting to have is a partially observed mark of decision processes but with a continuous state space
so with those you get the problem of you know estimating the expected free energy
which would be then an expectation or in other words an integration an integral in a continuous state space
and so how do you do that efficiently if you are in a high dimensional state space where you use
an Antonio Monte Carlo i think this would be really the the best method so this is how you join the dots
in this paper we didn't talk about sampling in discrete space because the methods are quite different so we
had we really had to choose what to focus on there's of course a lot more methods in the literature than
there are in this paper we just wanted to sort of review what were the main ones and what people really
used in practice but you know when you have the expected free energy in a discrete state space
computing the expectation that defines the expected free energy can often be a little bit easier because
it comes down computationally to a bunch of matrix multiplications matrix vector multiplications
which generally is doable unless i mean the state phase is enormously high and then we'd have to think of
sampling methods in discrete space um but as soon as you move to a partially observed markup decision
process in with a continuous space which i argue and ryan smith argues and i'm sure a lot of people
have run into this um as soon as you have this kind of model well um yeah you just have an integration
problem in continuous space and so Hamiltonian Monte Carlo is the way to go there
awesome and your 2020 paper was a synthesis on some of the discrete state space formalisms of active
so it's very interesting to see how you're now talking about where continuous time continuous state
spaces can come into play and how interesting that active inference has uh the capacity to do
deal with discrete and continuous state spaces and sometimes we lean on one leg or the other leg more
but it spans the gap in a way that's actually like a value adding not like there's some sort of missing
piece from one side or the other yeah yeah definitely i think active inference is great because it's so
flexible in the sort of models that you can consider um but but yeah i mean historically the first models
to be developed were continuous space and continuous time and then it works quite well because you
can take gradients of the free energy and just minimize them over time um so you could you could get
around basically everything by doing a gradient descent on free energy and then after that around like so that
was like 2010 and then around 2015 uh people started thinking okay well how do i model um discrete time
decision making with active inference and um and typically the decision making tasks at least the simple ones
that are studied in neuroscience in behavioral neuroscience just to make things simple um the the number of actions that you have is discrete
uh so you have a finite number of actions you have also and which is pretty small you would also have a finite number of
things which would be pretty small and then and then people started to think okay well how do we use active inference to actually account for that
um and so yeah and and so that's how the whole expected free energy and partially observed mark of decision processes
uh came into play and now the community has grown a lot and there's more and more data that we want to account for
there's more and more projects that are going on and with and you know people are realizing and i think
i mean it's an obvious realization it's just not um it's not surprising at all that these two models
developed in 2010 2015 they're just not going to account for everything and to think about other kinds of models
and it really depends on what kind of data you have at hand
and then one important and obvious type of model would be partially observed mark of decision process with continuous space
and actually um this is not a new thing i mean people have been using these kind of models
um in reinforcement learning and control for a long time i don't know to what extent they've arrived
at practically i mean they've sure arrived at practically implementable algorithms i don't know to what extent
they're used to what extent their state of the art um but the point is they it's something that it's a
kind of model that you know has existed for a long time um and so this sampling is would be a way
to actually practically implement this and scale it when you want to put that within active inference
so i think yeah it's an important thing to think about
awesome yeah thomas parr also recently in a discussion on the textbook was sharing some timelines
and it's just so interesting how these things have been developing and from continuous through
this is kind of ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail
representation in the figure of the running person and then how do the variables and the
processes described in this figure relate to all of this you know five hours of talking about
shadow hamiltonians and all of this right um yeah that's a broad question we might need
another 10 hours you know to answer that in detail but uh just very short um well so the active
inference section was meant to be as complete as possible even though it was very short and by
complete by completeness i mean that we started by deriving active inference and deriving active
inference from first principles um so this is really what the free energy principle does even
though we weren't able of course to you know review the whole free energy principle in like one or two
pages but we what we focused on was deriving the expected free energy from first principles and
then from there you get the full active inference algorithm so proactive inference algorithm i think
you just went past it's just below um if you go slightly below i think maybe page 29 or page 30
yeah uh still i think next yeah realizing adaptive agents yeah so this is the inference algorithm like
0.1 to 0.3 or something so just from a duration of the expected free energy um you actually get as a
corollary from there the active inference algorithm that we know and love this is actually a more general
version than what people use and um i'd be excited and i'm actually talking to people to actually
implement that um but this is actually the most general version that has been established in the
literature and it is more general in a meaningful way in the sense that all the beliefs all the
probability distribution they are over trajectories or sequences of events so it's not only so so it means
that all the computations they not only consider um events at a particular um time in the future for
example but they consider trajectories so sequences of events and so this is a equivalent to considering
different events at different points in time and their kind of dependencies and dependencies between them
and so this is just to say that if you take if you would take then this algorithm and you would perform
a mean field approximation over time which is saying that all the things that you see in the future are
sort of independent of each other at different points in time then you would recover what people
typically use in in the literature which is um easily implementable the the point i want to make here is
that you can actually not have that limitation and have things that are a bit more um yeah a bit more
complex that they are able to capture more complex relationships in the time series and input that
they might be receiving like the kind of sensory data that they might be receiving and the kind of genetic models that
they would have um so anyway this is the active inference algorithm the most general one we derive
that from first principles by deriving the expected free energy from first principles and so this relates
us to to that figure that you just showed so that that figure that you showed um with s o and a is the
starting point of the free energy principle described in this paper and so the point is that
the world the point is that we want to describe decision making uh we want to describe actions as a function of sensations
and so and we want to come up with the most general description of actions as a function of sensations
to be able to account for everything that's kind of the idea of the free energy principle
um so what do we do is we consider a world and a world in which there is an environment and an agent
and so the environment here is denoted by s and s is a stochastic process why stochastic process
because a stochastic process is the most general type of dynamic that exists at least as far as i know
um it's really a random dynamic and it could be random in all sorts of ways it could also be non-random
we sort of take the stochastic the random aspect as a extra ingredient just to include a lot more types of
scenarios and things you can be confronted with so you partition the world into the agent which is o and a
and the environment which is s and the agent then you subdivide it into two more components which are o and a
o are the what we call the observable state so these are like the sensations of the observation that you
get at any point in time also a stochastic process and finally you have the autonomous states or you
think about it loosely as the active states they turn out to be the active states in the implementation
but so the active states they're really um you know like the muscles the things you can actually
activate and make and then activate to you know influence the world um so we just partition the
world into these three sets sets of states that interact and and evolve in some way they're both
pretty stochastic processes that interact and then the goal of the free energy principle at least when
applied to decision making is that you want to describe a as a function of o because what so what
happens as an organism you can you have control over a you have access to o but you don't have the
right control of o or your sensations and you don't have access to s because that's the environment and
beyond beyond the mark of blanket beyond you beyond your envelope so you don't have access to s you know
o and you can control a a is what you can choose from and so the free energy principle just answers the
question okay well um if i take this very general description of the world
how what is the equation of a as a function of o how can i describe a as a function of o
and so it turns out um there's some mild assumptions in this and these assumptions uh they're they're
guided by physical considerations about how humans are and how humans interact with the world but they're very mild
but whenever you take these assumptions you get that the active states or the autonomous states
minimize expected free energy so so this is like a very succinct um derivation of the expected free energy from first principles
we start with the partition of the world we describe active states as a function of observations and so it
turns out that the expected free energy is what describes the active states as a function of observations
um and so and and so the basic active inference algorithm which everybody uses and which we have
also in the paper is about it's all about computing the expected free energy and then selecting actions
that minimizes expected free energy to the expected free energy as we saw i think it's in the next figure
so the one with all the panels was within it a couple times already it's um it's an expectation with
posterior distributions in it um what i mean by posterior distributions here is that that these are
distributions conditioned on the history of the agent so on the observations that he has already seen
and on the actions that he has already taken in any case um in any case so you have the expected
free energy is an expectation with posterior distributions within so it means that to compute the
expected free energy you have two problems you have computing posterior distributions through bayes and
inference bayes rule and you then once you have them you can plug them in into this equation and then you
need to complete the expectation and then you get the expected free energy so the first thing is about
computing the posterior distributions now what has been proposed in the literature uh so far is well how do you
do you do approximate inference how do you actually approximate distributions you do that through variational
inference or approximate inference by minimizing free energy the the treatment here uh the derivation and we
our aim was to do that provide a derivation that was as conceptually simple as possible
actually it highlights that the free energy is not the most important thing here
the important thing is really the expected free energy the free energy is just a tool to approximate
the posterior distributions to then get the expected free energy but you could actually use any other type
of divergence the free energy is just like a KL divergent plus some term that makes the whole thing
tractable and so you can minimize the KL divergence to approximate the target distribution but actually what
what this view highlights and by the way i'm not at all against the free energy i think it's really cool
and whenever and there's so many methods to minimize free energy and if you can do that then fine and sure
go for it like way to go but imagine you could not do that it would not at all be a problem because you
could use any other kind of divergence uh to solve those inference problems um so so that would be the first step
you're going to approximate those posterior distributions by doing some kind of approximate
inference which would be through minimization of the energy or through minimization of something else
and then you have the second step which is computing the expectation now either you're in a low number of
states discrete states from dp like thing and it's all a matter of vector matrix multiplications that are
tractable whether you have a very very high number of discrete states and then you need to think about sampling
in discrete states which we didn't discuss in this paper
either you are in a continuous state space and then you have an expectation in continuous state space
and then you want to think about an alternate Monte Carlo for example
so now with these two steps you have now an estimate of the expected free energy which gives you the quality
of any action sequence and so it's not only the quality but it's actually the negative log probability
of any action sequence regarding in this formalism because if you remember the one of the premise of all
this was to describe actions as a function of sensations in a physical system in not even a physical system but in interacting stochastic processes
um and so the answer to that was well the expected free energy gives us you know gives us how actions relate to sensations
um the expected free energy and this is why we use the letter we use the we used minus lock p of a as opposed to g to emphasize that the expected free energy is
not just like a function of action sequences but it is really the negative log probability of an action sequence
given some sensations um and so once you have computed the expected free energy you have this minus log probability of an action sequence
if you take the exponential negative of that the exponential negative of the expected free energy you get
um you get the probability distribution over action sequences um and so um by the way this exponential negative of expected
free energy is what we use all the time you might recognize this as the soft max of negative expected free energy
this is just all the time um kind of fundamental thing in active inference models um so i'm really talking about the same thing here
um so once you take the soft max of negative expected free energy you get p of a which is the distribution of
reaction sequences and now you have two possibilities either you want to stimulate the most likely action sequence
in which case you want to simulate the the action sequence that maximizes the probability distribution
um so in effect you have an optimization problem you out of all um yeah you need to find the action sequence
that is going to maximize this probability distribution that's given by the expected free energy or
or you want to simulate a typical action so what do i mean a typical action a typical action
action sequence is just a sample from the distribution and so if you want to sample from i mean if you want to do that
then you have a sampling problem where again you need to sample from from a distribution uh over action
sequences given by the expected free energy so this is really how how all these methodologies connect um
um yeah i think i think that's kind of it yeah one last thing is um typically when we simulate active
inference we never do the sampling at the end we always take the action sequence that minimizes expected
free energy in other words um in in other words the action sequence that maximizes that probability distribution
is the action sequence that um and this is because when we simulate things we it turns out i mean this
is how people have done in the literature people are more interested in the most likely action sequence that
um that an organism or an agent would produce but if you want to model data if you want to use active
inference to model data then you actually want to not just simulate the most likely action sequence but simulate
any kind of action sequence that would fall out of this and so this is really the case where you need
to sample from that final distribution as opposed to do optimization so depending on the use case you
either have a sampling or an optimization problem after you've um you've computed the expected free energy
so this is how these whole things um fall together and and so you might be asking okay well you talked
about sampling and optimization there's also a section about inference where does that fit in and so it
fits in to uh it fits in on on the remark i gave that you know we have these posterior distributions
within the expected free energy how do we compute them how do we approximate them one way is by minimizing
free energy another way is by minimizing any other kind of divergence and in that section over there we
just reviewed some kind of divergences that are very popular in the in the statistical inference
literature mainly because they have desirable properties and and so if you weren't able
um to use the variation of free energy for some reason or maybe something to be explored and something to
be explored is just to use another type other types of divergences and and just see what happens
um so the the open problem to be explored is whether we can get better performance by using different
kinds of divergences and and see what we get uh maybe there's particle algorithms that are out there with
these other types of divergences that we can make use of to do better performance to get better performance
um can we actually describe and quantify the improvement in performance that we get by using these
other types of algorithms when would these be appropriate and useful and these are all open questions
um another open question that i think is interesting is can we model maladaptive behavior um by using
different kinds of divergences that would not work as well as the free energy and there's um there's an
interesting paper on that by uh newer sejid i think and colleagues i think it's called um basin brain brain
basic brains and the rainy divergence it's been published on neural computation i think last year or
or the year before and so in that paper instead of using the variational free energy to
approximate all these posterior distributions um she used uh the rainy divergence which is
which generalizes the kale divergence in some way and show that for different rainy divergences you
get different types of approximate posteriors and she basically um looked into yeah what kind of
differences you get from there in terms of perception in terms of decision making and she showed that for
that particular divert divergence i think the conclusion was that you basically get different
phenomenology you get different behavior uh so just something to be explored i think the option was that
maybe i don't remember how far the paper went in this but i think kind of the the goal was to model
maladaptive behavior using some kinds of rainy divergences that did not work as well as the free energy
so this is to say so this is an interesting work um one could examine other kinds of divergences and see
whether you actually get better or worse performance than with the free energy uh one thing one word of
caution though is this the free energy is is just so good in the sense that it uses the kl divergence
and as i mentioned at the beginning the killer has so many properties and it's just so fundamental
so um it's not straightforward to see that when you first come up with it but i guess the more i read
in different disciplines and the more the kale divergence comes up and the more the more i see
properties of kale divergence in different disciplines that just make it so interesting like for example the
kale divergence in statistical physics is the relative entropy so it quantifies the amount of entropy that a
distribution has with respect to another entropy as we know is just a very fundamental thing in
information theory the kale divergence quantifies the difference in information between two distributions
the amount of bits that you would need to i mean um if you take two distributions a and b uh the kale
between the two between the two quantifies the amount of information uh that it takes to go from one to the other so now you might object and say okay but
kale a and b is different from kale b and a and so how can it be that you know it quantifies the amount of information
um they need to go from a to b or b to a because it's not symmetric um so the answer is it's either
kale of a and b of a and b that has this meaning or kale of b and a that has this meaning and i just can never remember which direction
but it's one of them that has this uh interpretation in terms of uh the difference in information
um anyway um so kale is just like um something it just comes up everywhere and it's just um so useful
and it has all of these nice properties which makes the free energy really um a construct of choice
um but that said there's other divergences one of them which we describe a bit in the paper called um
the maximum mean discrepancy which i think also has nice properties it's not necessarily well it's a
bit different it's very different in terms of how you construct it from the kill divergence but i think
my current understanding right now and um my current understanding right now is that if you cannot use
scale then maximum mean discrepancy is just like really nice um but but yeah so the word of caution was
that probably most divergences out there are not going to do as good of a job as a free energy uh but
some clever ones might and it's an open problem of you know determining which and and yeah so this is how
you know we get the link between all these different sections so to to do perception we need inference
to do decision making that is computing the expected free energy we need something
typically and then to do action selection we either need sampling or optimization and also inference is
uh an optimization of beliefs sampling also as we've discussed is also an optimization of probability
distributions you can see that as an optimization of beliefs as well so it's all very tightly interconnected
wow thank you lance that's very informative
brings up a lot of
ways to go and it it really shines a different light on even what learning active inference or
learning free energy principle it was a roller coaster just listening when you describe the figure of
the running person and the new generalized representation here which is so sparse it looks like it's
pseudocode but it's actually basically necessary and sufficient to describe it is
it's pseudocode yeah it is pseudocode and it is also exactly like this is really what active
inference boils down to and that was kind of like where we got at we're like okay well we have this
mess of papers of active inference not that they're actually a mess but you know there's so much information
and we're you know really thinking reading all this the latest free energy principle literature that i've
also worked on a lot and also the active inference literature and really thinking okay well how do we
strip all that of the neuroscience how do we strip all that of the cognitive science how do we just
retain the math and present it in the simplest way possible that would be appealing for a mathematician
and also hopefully for a computer scientist it turns out that we got a way simpler perspective than
anything that's anything that's out there i think um and really yeah so this is the active
inference algorithm in pseudocode and in detail also in in a way so i totally agree again thanks for the
work and for sharing it this way because it is the fewest pixels for the highest resolution picture so
so then to describe the fundamental cybernetic challenge as a partition an axiomatic partition which
one can then say also has grounding in the spatial temporal boundaries of the world or in geometric
boundaries in informational spaces but the particular partition is used to separate
the map not necessarily making claims about the territory and the actual nature of the objects
and their articulations or anatomy but on the map which we get to construct we make it in a way that's
amenable to the particular partition which is not too much more than the separation of figure from ground
or agent-based modeling it's just a separation of some autonomous entity from some external process
then the task of the free energy principle applied to decision making as you said was to describe action
as a function of observation and everything in between is broadly considered cognitive but for any given
system it's going to play out in this immensely nuanced way with a lot of bespoke mechanisms and why do we
take that particular partition step well it's kind of like read write access in a computer system there's
things we don't have access to hidden states and also the reverse of that which is we can't access hidden
states nor them influence or affect us so i think of that as like no telekinesis no telepathy you can't go
directly across the blanket you have to intermediate through the blanket of observation action and
then with respect to our particular states our blanket and internal states we have access to observations
but not direct control nor necessarily would we want to because if we had the lever to change what we
directly received then algorithms might learn strategies that basically self-deceive so that
the observations look good look good look good until the whole system crashes so we want access to
observations but not direct control and then the autonomous states are what we in the optimal ideal
situation have total control of which is like our mind and our body what we think and what we do
it turns out through the pragmatic turn and the inactivist insights in cognitive science that a lot
of action sequences have to do with changing what observations are sought after like epistemic affordances
so there is an enmeshment of action but it's also really important that we have access but not control
of observations we don't want to have like our control on the thermometer but we want the best
possible thermometer and then we want to control the best possible interpretation that's like signal
processing and the best possible action sequence which is like decision making and control theory
and then free energy principle is addressing that question what is the equation of action as a function of
observation but then it was quite a roller coaster when you said that the free energy wasn't even
necessarily the only way to do it but it's absolutely true it's the properties of the free energy are
inherited from one of the terms being the kale divergence any other having the ability to
basically ignore in certain relative expected free energy calculation contexts so then in that situation
differences in free energy do come down to differences in the kale which does have all these properties
but that doesn't mean that the free energy is itself axiomatically posited
it's actually downstream of the particular partition to use free energy or anything like that at all
and other discrepancies may have other properties in different ways
exactly and and so there's a bit of a nuance in the sense that here we presented the stimulus
version of the free energy principle just describing decision making as you as you summarize so describing
a as a function of o but if we and and by the way about that so we're we didn't even talk about markov
blanket in this paper um i would i would say that the markov blanket is under the hood because we're
saying okay well these are the states that you have access to and these are the states that you do not
the states that you have access to are a and o the states of the agent the states that you do not have
access to are the environment so in some sense there is a markov blanket but we didn't even mention we
didn't even have to mention that in the paper it's just you partition the world into three sets of states s o
and a um that are by definition a um and you just yeah just from this tripartition you want to describe
one as a function of another ignoring the third um and so that's yeah that's how you derive expected
free energy you see that um action sequences are described by the expected free energy and these
this is a function of sensations um if we went further in the and so this is just what you need
crucially this is just what you need to derive the active inference algorithm if you if we went further
in reviewing the free energy principle then we would see the fundamental role that the free energy
plays um and so actually when you know reading the latest papers on the mathematical theory of the
free energy principle the role of the variation of free energy is pretty clear um but here the point is
that if we just care about decision making if we just care about the normal active inference algorithm
then we don't even need the variation of free energy so sure uh the free energy should be preferred why
not uh if it is available but if it is not for some reason then there's no reason why not to use another
kind of the kind of the evidence
so very interesting it's making me think about linear regression and the sum of squares the l2 norm
is one approach that's often used to fit a regression line because it has good optimization properties
there's good software packages there's good education there's good communication around it and so on
but one can select other norms and choose to fit a linear regression with an l1 norm or with an l3 norm
and so that entire question of fitting the linear regression is a degree of freedom how the regression is fit
that's downstream of a commitment to for example model a system in a generalized linear modeling framework
and so analogously the upstream commitment or the first principles which yes can be understood as
axiomatic and also have some empirical status in terms of this partitioning a figure from ground the
particular partition can simply be accepted axiomatically which is to say without appeal to evidence
or somebody might have another upstream axiom and choose to model uh things according to a particular partition
from there just like we could have chosen the l123 norm there are different discrepancy criteria
data or measures that we might want to use and some of them apply better or worse or not at all
depending on what software hardware data set and generative model we have and so it makes sense to
that pull pull pull back into the the upstream understanding of active inference as a process theory
for particular partitioned systems and then for those who want to engage in the modeling to have that
uh discussion about the garden of the branching paths well you could use a discrete timer you could
use a continuous time and then from here you could do this sampling or you could do that one and if we
have this computer access we can do that but if we have to do it this way we'll do it like that
and that's all operational and logistical but it's actually all under the umbrella or under the auspice
of the theoretical or conceptual commitments that are actually not being questioned once one is in that
modeling discussion just like you could have the l123 norm conversation and maybe a reviewer asks you
why you chose the two norm versus the three but it's a broader level of questioning why one took on the
linear modeling framework at all and our analogous upstream bottleneck not in terms of rate limiting
but just in terms of like eye of the needle is the particular partition
yeah definitely and i just want to add something actually about the choice of divergences uh or the
choice of discrepancy that you might want to use to solve the inference problem i think the analogy
would linear regression is a really good one um when you do linear regression yeah you can use all
types of norms and it's really a design choice and here in the algorithm you also have that design
choice are you going to use kl so free energy to do these inferences uh by the way the inferences are
really uh equation 43 and 44 which are approximate um actually you had them in the slide already
oh 43 and 44 oh oh here got it yeah yeah um which are approximate um you know some posterior distribution
with an approximate posterior distribution so you can do that with the free energy which is the same as
the kl divergence or you could do that with a whole bunch of other divergences one that i mentioned and
that i think is particularly interesting is the maximum mean discrepancy and so um here's the difference
between kl and maximum mean discrepancy at least like i guess a important conceptual difference so the kl
when you look at distributions that are very close to each other it's going to measure it's basically going
to become symmetric when the distributions are very close and it's going to measure the amount of
information that differs between them the maximum mean discrepancy when you take two distributions that are
very close it's going to it it reduces to what people call the earth movers distance also called
like the vast time distance so here is the intuition if you take two distributions that are very close just
imagine distribution a as a pack of dirt and distribution b as a pack of dirt or or a stand with
some shape uh the maximum mean discrepancy is gonna tell you the amount of work that you need to put all that dirt
from distribution a and pile it in the shape of distribution b so of course there's so many different ways in
in which you could take all that dirt from distribution a and remodel it in distribution b but you're interested in the
minimal um the minimal energetic cost that would take so like the optimal way of doing that movement people
call that optimal transport um now if you if you're familiar with optimal transport you know that the
the vast time distance um is a distance between probability distributions that regardless of how far they
are is going to measure um like the it is going to give you this um cost of optimal transport so the
energetic cost of moving all that um you know pack of dirt from place a to place b in the optimal way
um so the vast time distance is something that we could use here um but maximum mean discrepancy it has
a lot of very nice properties and basically reduces to the vast time distance when we consider very close
distributions so uh this is not something that just a mathematical curiosity but it says that when one
builds when one builds a distance out of a divergence what one does is one takes you know very close
distributions measures the divergence between them at which point the divergence is pretty much symmetrical
and then you basically keep adding divergences along a trajectory until you get to the final one
and this way by aggregating divergences between very close distributions and doing that and you know adding
that along a trajectory you get a distance a meaningful distance between you know distributions that could
be very far if you do that with the kl divergence you get what's called the fisher information distance
which measures really the um really um yeah the the amount of information that took you from go
to go from one distribution to another distribution regardless of how far they are
um if you do that with advanced search time distance you will get the optimal transport cost so the amount
of energy that you need to put all that dirt they say to place me in the optimal way if you do that
with the maximum discrepancy you would also get that you will also get the optimal transport thing so
um i just so the yeah i just want to say that the maximum discrepancy meaning discrepancy between two
distributions that are far away will not coincide with the Wasserstein distance which gives you this
optimal transport cost but when you actually derive a distance from these divergences the distance derived
from the maximum meaning discrepancy and the Wasserstein distance will end up being the same and um
this distance that you actually get or the topology that is derived from the distance so by topology
a topology is really a notion of closeness um and so to understand closeness you need to understand you
know infinitesimal distances um so the infinitesimal distance is derived from Wasserstein or MMD they're the same
the topology that results is the topology of what people call weak convergence which is the standard
topology that's considered in probability theory um so MMD and Wasserstein they are very natural in that sense
in the sense that they they they uh they people say that they met rise with conversions like they give
give rise to the standard topology between probability distributions um so coming back to the choice of
divergences if you're interested in approximating distributions in the sense of approximating their
information content then KL is very natural but if you were for some reason and maybe would not be in this
kind of application but another kind of application if for some reason you're interested in approximating
distributions for the sake of how close they are when you look at them uh then then you would use MMD or or
best of shine wow great information and i'm just thinking about we're switching lanes on the highway
we're trying to get from here to there yes we want to know about the informational closeness of this tale of
two densities but we also want to know about the transport closeness because we have a schedule and a
budget and decisions to make and there are trade-offs so being able to move the earth optimally while
we're switching lanes and accelerating and slowing down i know this is mixing many angles informally
we want to have a lot of options for how to think about that challenge of moving dirt between the tail of
two densities and make sure everybody is driving in the right lane at the right time
definitely and yeah it's a it's a design choice and it's an important one because it depends on you
know what kind of properties we want to preserve and um yeah so all these all these divergences some some
are not so useful i guess but um some of them they're they're just very natural and the westerstein and
mmd they're very natural in that sense um so yeah very important to keep in mind um and not only for
active inference uh but just you know in general for any kind of inference problem
well let us each have a closing round or reflections any thoughts or any next steps or any suggestions or
other information you'd like to provide um it's hard to say i feel we've you know we've covered
so much already um there's still i think to me what's most exciting about is um scaling active
inference right now um because you know you get this active inference algorithm in the paper uh that's
derived from first principles and just from the derivation you see okay well there's actually so many
things i mean the assumptions are so small that there are so many things that you can model with
this active inference algorithm and basically you will oh and all the heavy lifting is done by the
genitive model so if you use one derivative model you will get one behavior if you use another genitive
model you will get another behavior but all the equations will remain the same um so so it speaks to
generality now in in having something that's very general you get something that's also very non-specific
and i guess for for neuroscientists and people who are interested in intelligence you just um
generality comes at a cost of being you know non-specific and non-specific about the brain in general
um so really the big question to me uh long term is what kind of genitive models do we need to simulate
brain-like behavior because really this is really the interesting behavior or the most interesting
behavior um so it speaks to a big research program that a lot of people are carrying and have been
carrying for a long time but you know um it's about what kind of representations do we have
of the world what kind of priors do we have what kind of uh can we identify the priors
that we are born with there's a lot of research on um computational or just playing cognitive science like
normal cognitive science just studying babies and seeing what kind of priors what kind of you know
basic information they have when they come out of the womb there's a lot of things that they can already
do there our genetic code is preconditioning us to operate efficiently in this world and be able to
flexibly adapt to any kind of situations that might arise in the natural world and so it's a huge research
program to you know understand and model these priors and um yeah and not only the priors but also the likelihood all the
representation all the state spaces so i think that's the way forward the green energy principle is very elegant because it gives you
you know a very succinct description in terms of a giant model that enables you to simulate pretty much everything
but we're not interested in simulating anything we're interested in simulating brain-like behaviors so
now we need to you know drill down even more onto the kind of genetic models that that would be amenable to that
be a great great my closing reflection i feel like i know less about fep but more about something else
for what we've discussed earth was moved bayesian mechanics were called in decisions were made
and it's been a really great series so i'm appreciative and thankful that you suggested this paper in our
correspondence as one to discuss you were absolutely right that it is relevant to bring to the attention of
the act inf community and i hope that everybody who reads or listens this far has
interest in this kind of ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail
Thank you.
Thank you.
