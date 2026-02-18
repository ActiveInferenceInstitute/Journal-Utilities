---
title: "ActInf Livestream #038.0 ~ Brain architectures for predictive coding and active inference"
category: "Livestream"
series: "Livestream_038"
episode: "0"
speakers:
  - "Brain architectures for predictive coding"
  - "active inference"
duration: "1:11:42"
url: "https://www.youtube.com/watch?v=cOo4juE_zcI"
views: 376
exported_at: "2026-02-18T22:37:37.864000+00:00"
format: markdown
---

# ActInf Livestream #038.0 ~ Brain architectures for predictive coding and active inference

Hello and welcome to the
Welcome everyone. It's ActInfLab livestream number 38.0, February 10, 2022.
We're going to be discussing the paper, The Evolution of Brain Architectures for Predictive Coding and Active Inference.
Welcome to the Active Inference Lab. We are a participatory online lab that is communicating, learning, and practicing applied active inference.
You can find us at some of the links here on the slide.
This is a recorded and archived livestream, so please provide us with feedback so we can improve on our work.
All backgrounds and perspectives are welcome here, and we'll be following good video etiquette for livestreams.
It's going to be a solo stream though.
Go to activeinference.org if you want to learn more about how to participate or contribute or get involved with any ActInfLab project.
And check out this Coda link to see past and upcoming livestreams.
The page looks like this. So you can see events that haven't happened yet, like 39, 40.
And then also you can look back and you can see who is participating and read the papers and all of that.
So, check it out.
Today in ActInfStream number 38, the goal is to learn and discuss this cool paper,
The Evolution of Brain Architectures for Predictive Coding and Active Inference.
The paper is by Giovanni Pizzullo, Thomas Parr, and Carl Fristen from December 2021.
And just like all videos, it's just an introduction to some of the ideas.
It's not a review or a final word. So go check out the paper to learn more.
And there's going to be an overview with first names and claims, abstract, and roadmap.
All right, I'm Daniel. I'm a researcher in California.
The big question that this paper is getting at is,
what is the evolutionary neurophysiological basis of cognition and how do complex cognitive phenotypes arise?
So, how do things develop and evolve?
How they think and how does that change over evolutionary time?
And shown here are three images representing three scales of analysis.
of looking at ant cognition.
So, on the left is a representation of the synapse with the glia wrapped around it,
and the molecules and some of the mechanisms, because changes in those mechanisms can influence cognition.
Then, in the middle is a 3D representation of an ant brain with the different brain regions,
like the central complex and the optic and the olfactory lobes.
And this represents the level of regional or micro or meso-anatomical variation.
And that definitely changes over evolutionary time, just like the synaptic level.
And then there's this behavioral ecological level.
And that's where the ants are engaging in collective behavior and stigmagy.
And so, how does this all work?
How does this all work in today's ants and how has it evolved?
And then expand that to other species and other questions.
The paper was published right at the end of 2021 in December in the Royal Society of Publishing.
And just to go over the aims and claims of the paper, this is in the author's words.
There's growing consensus that the brains of humans and other phylogenetically derived or advanced organisms
operate in a predictive manner across perception, predictive coding, and action control, active inference.
Yet, the ways in which our advanced predictive abilities may have arisen during evolution remain unclear.
The goal of this article is to sketch an evolutionary history of brain architectures for predictive processing.
A central tenet of our proposal is that although prediction is often characterized as a complex cognitive function,
it is not a late evolutionary addition of advanced animals like us.
Rather, in distinction to a late-stage cognitive argument like saying language is what makes us an advanced cognizer,
or semantic language with certain types of syntax.
Rather, our complex predictive abilities, e.g. planning and imagination, emerged gradually, e.g. via phyletic gradualism,
smooth changes through evolutionary time, or punctuated equilibrium, sharp changes through evolutionary time,
but punctuated at one scale is smooth at another.
From simpler predictive and error correction loops, e.g. motor and autonomic reflexes,
that were already part of the brains of our earlier evolutionary ancestors,
and were key to solving adaptive regulation problems.
So just like Mike Levin's paper was addressing the question of basal cognition from the bioelectric perspective,
the bioelectric perspective here is going to be more of a predictive processing and action inference perspective,
on the functional aspects, not on the mechanistic.
So the bioelectric was down here at the level of cells.
This is going to be approaching it from a little bit of a different perspective, but we'll find out.
Here's the abstract.
This article considers the evolution of brain architectures for predictive processing.
We argue that brain mechanisms for predictive perception and action are not late evolutionary additions of advanced creatures like us.
Rather, they emerge gradually from simpler predictive loops, e.g. autonomic and motor reflexes,
that were a legacy from our earlier evolutionary ancestors,
and were key to solving their fundamental problems of adaptive regulation.
We characterize simpler to more complex brains formally,
in terms of generative models that include predictive loops of increasing hierarchical breadth and depth.
These may start from a simple homeostatic motif,
and be elaborated during evolution in four main ways.
These include the multimodal expansion of predictive control into an allostatic loop,
its duplication to form multiple sensory motor loops that expand an animal's behavioral repertoire,
and the gradual endowment of generative models with hierarchical depth,
to deal with aspects of the world that unfold at different spatial scales,
and temporal depth, to select plans in a future-oriented manner.
In turn, these elaborations underwrite the solution to biological regulation problems faced by increasingly sophisticated animals.
Our proposal aligns neuroscientific theorizing about predictive processing
with evolutionary and comparative data on brain architectures in different animal species.
And just looking ahead, here's a figure that we're going to get to.
Here's the ancestral state.
It has this structure.
It's a model.
And then it's going to undergo a set of different types of discrete operations that change it structurally.
And that's structured learning, and it's going to happen over evolutionary timescale,
and it's going to be tied to functional architectures for predictive processing.
Okay, how do they go from here to there?
This is the roadmap.
After the introduction, they introduce predictive regulation and control.
Perception, cognition, and control, action, as basic design principles of the brain.
So kind of taking that embodied approach, but making it very operational and functional,
so that it can be studied from an evolutionary function perspective.
Introducing the brain as doing structure learning in generative models over evolutionary and also other timescales.
They then give three examples of simple predictive motifs in ancestral brains,
which is the homeostatic control, the allostatic control, and the simple behavioral learning.
Then they introduce that figure that we just looked at, and that's the evolutionary algebra of structure learning.
Just like you can multiply and add, these are kind of like operations on evolutionary spaces.
They then discuss a few finer points related to behavioral switching, temporal depth, hierarchical depth,
and then take a phylogenetic perspective at the end, giving an example, and there's a discussion.
Okay.
So, to go into section two and just sort of deal with the keywords and themes as they are needed,
here's figure one.
In figure one, the reason why we can even jump in here without going to any keywords is it's biology we're talking about,
and we can jump in, why not, as good of a place as any to go in at the action perception loop,
and then connect it to some of the analytical or mathematical formalisms of active inference and the free energy principle.
So this is figure one in the paper in section two, the action perception cycle and predictive regulation.
So here's our entity, our agent on the left, and here is our world state on the right.
The entity is engaged in prediction while they're making observations that are being emitted from the world.
And in the result, that's resulting in some discrepancy.
Either things are exactly as expected or not.
So an example would be in the visual field, the brain is generating a prediction of what is in the blind spot of the retina.
And then if the eyes were to move there to use action, changing the world in terms of the stimuli coming in through ocular motor action,
that would result in a different perception that could either confirm or deny, confirm with a low discrepancy,
or be very surprising with a high discrepancy, what was expected about what was in the blind spot,
which would confirm accuracy in a visual model.
So in this partitioning of action and perception, which is just very descriptive,
it's not quite the Bayesian graph that we're going to get to later.
It's kind of like a flow model.
And there's probably other flow models that could be used as well.
But it turns out that this partitioning or this way of thinking about flow, at least conceptually, leads to in the active inference proposal,
this idea of using a free energy minimizing function over some math that we'll get to a little bit more formally in the next figure,
and using a kind of combined metric that has two parts, the red and the blue,
to make decisions about perception as well as action, because it turns out that perception and action and cognition and metacognition
are all part of the entity's model that it's doing inference on in certain cases.
So just to kind of throw back to not so long ago, here we have the f of q,
that's the distribution that's under the entity's control and y.
And so it's as a function of beliefs and data, there's going to be some term.
And so just looking back to 37, we looked at the variational free energy and how that relates to perceptual inference,
where there's a penalty for overfitting as well as a penalty for failing to explain the data.
So it's kind of making a visual model or a perceptual model that in that snapshot,
given the priors and precision and all of that, is not overfitting, but it is fitting the data.
And it's kind of existing on that frontier.
And then it's using variational inference to solve that in a really tractable way.
And then when action comes into play, a few things happen.
First, the agent has to incorporate their own preferences, because why care about action if you don't even care why it's going to happen?
So they have to incorporate their preferences, which is a non-arbitrary in a sense for action selection, but it's arbitrary in a higher level,
as well as incorporating the fact that there's uncertainty over the consequences of action or just future states of the world,
not just like sensor measurement as in other cases.
So we have to take this variational free energy calculation that was just like snapshot perception and expand it a little bit to the expected free energy.
So here's F in the background.
And now there's this expected free energy term G, which is over also an action selection policy Z.
And now there's kind of similar like resonating or rhyming terms, but rather than overfitting, the imperative on the left side is to satisfy preferences.
On the right side, the penalty for failing to explain the data is kind of transposed into this failing to surprise or failing to minimize expected surprise of future data.
So this is like fitting the expectations well on the right side and blue and then living up to your preferences and expectations in an optimistic way on the left.
So it's kind of like realism on the right and optimism on the left.
And that is what we talked about in 37.
And that's the partitioning that's being done basically here.
The authors are setting that up as the action perception cycle and predictive regulation.
Just wanted to kind of view 37 really quick because it was a fun discussion that we had.
It also really sets the stage for how is that similar or different than other action perception partitionings or models.
Does evolutionary psychology or evolutionary cognitive studies, do they have a fundamental action perception model at the root?
Is that a good thing? Is it a bad thing?
Section three goes into section two again was just about how this single slide and represented in figure one about this predictive.
So anticipatory, but also embedded, etc.
Infinity loop cycle is the basic principle of the brain.
We can't take the basic principle of the brain to be some lower level, like just information transmission amongst cells, nor do the authors jump in at a higher level, like the fundamental unit of cognition is linguistic tokens that are being modified, not discrepancies with multiple different kinds of things that are being predicted.
From this functional description of cognition, they move to section three, formalizing brain design as structure learning in generative models.
So what is the structure of this model?
And then what does it look like to do structure learning in that model?
And why is it generative?
And then how is that formalized?
So here's figure two, the generative model and the generative process.
So the first word is the same.
Second word is different.
So they're different words.
And the figure on the left side has the entity.
The figure on the right side has the world state.
So it's the same action perception loop we saw in figure one.
And now this sort of conceptual flow, single edge model, like just only one arrow here, no extra anything, just sort of first pass.
It's compatible with this, which is actually a Bayesian graph.
But how do they describe it?
And what are all the variables?
We still have the same things happening.
We have the observations coming in to the cognizing entity.
That's the observations coming in.
The entity is going to infer some action policy based upon the observations coming in, which is going to result in some change to the actual underlying system, which is the generative process.
So that's like the actual birds and the bees and the sun and stuff.
Allegedly.
It does get into a little bit of a gray area with the realism, instrumentalism and the structural realism, but we're not even going to go there in this discussion.
Right now.
The generative process is the one that's handing out the observations as modeled.
The generative model to close the loop is the entities inference.
And so here is X, the entities prediction on hidden state.
And then here is X star, which is like the actual hidden state that is being alleged in the world.
And we've had some other discussions about how that's the sigma function.
That's like mapping between the two X's.
That's what's being minimized.
If the discrepancy is low, there's other notation.
How did the authors describe it?
The difference between the generative model and the generative process.
Nodes correspond to probability distributions and edges to their statistical dependencies.
So this is like a Bayes graph.
Mathematically, a generative model may be formulated as the joint probability density, P of Y and X of observations Y and hidden states X of the world that generate those observations.
I think it was just a copy error.
The latter are referred to as hidden or latent states as they cannot be observed directly.
The joint probability distribution can be decomposed in two parts.
The first is a prior, P of X, which denotes the organism's knowledge about hidden states of the world prior to seeing sensory data.
The second is the likelihood, P of Y given X, which denotes the organism's knowledge of how observations are generated from states.
So that's the perceptual model.
And then they go on to describe how there's a difference between the entity's inference on hidden state and the actual hidden state, which is the generative process versus the generative model distinction.
And then they introduce action and say action U, that's this node that influences the hidden state, even if zero effect is generated based upon the inferences made under a generative model.
Action is shown here as part of the generative model.
Sorry.
Action is shown here as part of the generative process, making changes to the world, despite being selected from the inference drawn under the model.
So action is actually making influence.
Again, the edge could be zero in some respect, but it's making actual influence in the world.
It's like the active states interpreted in this statistical way.
So what does that have to do with structure learning?
So the entity is going to either whether you're a realist and saying the entity is doing structure learning or you're instrumentalist.
It is possible for us as researchers today to model that entity as doing structure learning because it's computationally efficient or elucidative or you go full utilitarian.
You just say disregard that whole realism, instrumentalism.
It's a useful approach and I'll follow utility wherever it goes.
For any number of those reasons, you might want to model the cognition of different entities without going into just the philosophy of what its cognitive process actually is.
And so one approach that's going to get taken is using inference either from the outside, describing instrumentally or realism as if it were happening, maybe with anatomical evidence, as if the hidden state could include not just parameters that were continuous about the world, but also structures of models.
However, it's difficult to imagine that that type of cognitive or even extremely metacognitive thought or action selection could happen, for example, in some early protocell, however simple it may have been.
And so how do we get from that flagella changing bacterium to all the other kinds of cognition that we see today?
Or should I say bacterium like entity?
Or should I say bacterium like entity?
Relative or ancestor of today's bacteria.
So how can we think about this model, which is often described in the context of parameter learning and then approach this as if it were maybe about parameter learning sometimes, but also could be about structure in terms of the good regulator and the requisite diversity, that kind of requisite variety, those kinds of models.
Okay, the next several sections are where they get to the specifics and some of the contributions of the paper that I think will be really cool to continue the discussion on.
Section four is just short, and it's saying we're about to go into three examples of simple predictive motifs in ancestral brains, because one of the main claims of the paper is that these motifs are very ancestral.
They're old motifs, they're not Johnny come lately to the cognitive scene.
These are features that one can think of as who knows how far back or how simple these cognitive mechanisms have existed, but we'll evaluate that maybe when we get to talk together.
But first, we'll just kind of go through how they define them and use them.
The three predictive motifs are homeostasis, allostasis, and simple behavioral control.
So first, five generative models for the homeostatic control of interoceptive variables.
They write, the generative models shown in figure three, which we'll look at after this slide, afford the homeostatic regulation of a single interoceptive variable, which we call here body temperature for illustrative purposes.
Much like a thermostat, this model maintains the requisite body temperature by reporting the discrepancy between predicted and sensed thermoreceptor activation, given Bayesian beliefs about temperature, triggering an autonomic reflex U, resulting in, for example, vasodilation, which resolves the prediction error.
So if the life of the organism were just to hang out on the beach and vasodilate to off heat when it needed to, and then to constrict and to save more heat when it needed to, that's the physiological task that this is going to be describing, which is just one facet of an organism's biology.
But there are experiments that sometimes only measure temperature.
And so thinking instrumentally, this single factor model, this single variable model on body temperature may be sufficient for some experiments, or it may be useful in certain cases.
So just because it's a simple model doesn't mean that it's not going to be very educational and provocative, but also even be sufficient in a lot of cases.
But no one's even claiming it's realism.
That's why it's written this way.
They say, see citation 20 for a fully specified example.
And that is a citation 2, Chance et al. in March 2022, so still in the future.
And they write, we start from the premise, and this is in the paper that, again, is from the future.
We start from the premise that the goal of interoceptive control is to minimize discrepancy between expected and actual interoceptive sensations, i.e. a prediction error or free energy.
Importantly, living organisms can achieve this goal by using various forms of interoceptive control, homeostatic, allostatic, and goal-directed.
So there's more details in this paper.
But here in figure 3 is where they're going to show it.
So keep in mind this generative model structure.
And now these are going to be in a different form.
And here in the caption, I'll describe what they say.
This is that homeostatic, the first, most ancestral, or just the simplest possible, just go, make it darker if it's too bright, and make it brighter if it's too dark.
Make it warmer if it's too cold.
Make it colder if it's too warm.
That kind of first-order cybernetic loop.
This generative model includes an interoceptive thermoreceptor, Y, observations, and a belief about body temperature, X.
So that's the beliefs about how the body should be.
And that's, again, the beliefs playing that dual function that the paper 37 drew out,
which is that on the left side of this equation, failure to satisfy the preferences is dealing with this P distribution as a preference.
But then on the right side, P has to do with expectations that are being either fit well or poorly.
And so this is where active inference has a slightly different architecture, perhaps, than some other theories.
The beliefs are about body temperature.
It's not an estimate merely of the external body temperature.
Crucially, the prior over X is kept fixed, and hence it acts as a cybernetic set point.
Well, you can't just expect what's going to be best for you.
You'll die.
Right.
If you die, you die.
But if you enact policy such that your expectations are realized, then you persist.
That's why we're studying things that are persistent.
Any discrepancy between the predicted thermoreceptor activity given beliefs about X and the measured Y is registered as a prediction error that is canceled out by an autonomic response.
For example, a thermoregulatory response.
This is shown as an illustrative plot of the expectations of prior and posterior observation and autonomic actions over time.
So here is like the action policy, which is like be at the baseline level of thermoregulation and then kick in some sweating or cooling mechanism.
And then here it describes how the observations start at about 37.1 and then they steadily start climbing.
And then the belief, which is initially like things should be 37.
The posterior, the after evidence estimates starts creeping up.
And then it hits a certain value and it engages a critical threshold that turns on this thermoregulatory response.
And then that cools the temperature back down.
So this is a basic architecture for doing first order cybernetics and that kind of first order logic.
Here in this figure, the red circles represent the expected values of X, which are used to make predictions about Y.
These are subtracted red arrow with the rounded end.
So this one.
From the measured Y to form a prediction error.
Dark blue circle.
Epsilon.
Which is used to update the expectation and drive action.
Light blue circle.
U.
Here's U.
That changes Y such that the prediction error is resolved.
What if it doesn't do it?
Well, then the system dies.
So we're talking about evolution where we've had, like for the ants, 120 million years, allegedly, for that to get pruned out.
And even longer at the cellular level.
Note the lateral modulatory connections in the allostatic network, which we'll get to in a second.
So just to take one little discourse, they say C24 for details.
What is Pape 24?
It is Friston, Par, End of Rise, 2017, The Graphical Brain, Belief Propagation, and Active Inference.
Let's just look at a few parts of this awesome paper.
So first, they have a table with definitions of the technical terms.
So just to kind of read a few, but it's kind of awesome to see the authors do this.
And this is a great paper as well.
So how do they define generative model?
Generative model or forward model.
A probabilistic mapping from causes to observed consequences data.
So from hyperparameter to the parameter.
It is usually specified in terms of the likelihood of getting some data given their causes, parameters of a model, and priors on the parameters.
So it's all relative in nested models.
But this is generating data, like kind of cranking out like a music box, possible or plausible data sets with similar summary statistics, like similar mean and variance of some distribution, or similar parameters if there's a whole vector that describe it.
And then the recognition model is related to learning where new data are coming in and discrepancy is being minimized.
If the generative is outputting the exact same mean and variance that incoming data are having, the discrepancy is low, the predictions, which are about preferences, are being realized successfully.
Action policy is working well or better than expected.
Flip everything and you have the opposite situation.
And then just to give one more definition here, because the next slide will feature it, though the others are also good to read.
Factor graph.
A factor graph is a bipartite graph, where two distinct sets of nodes are connected by edges, representing the factorization of a function, usually a probability distribution function.
Formulating a Bayesian network or model as a factor graph enables the efficient computation of marginal distributions through the sum product algorithm.
What does a factor graph look like and how does it relate to the kinds of Bayesian graphs that we've been looking at?
So on the top is not the Bayes graph that's distributed across this slide, but another variant that we've seen a bunch of times, which is the partially observable Markov decision process.
So G, expected free energy minimization, pi, policy selection is influencing B, which is how S, the latent state in the world, is changing through time.
There's D, the prior on the hidden state, and then A, the mapping of how the state is related to the observation.
And so depending on how the model's framed, those can be learned or not.
But it turns out that because of how this is relatively sparsely connected within a time frame, as well as across time frames, there's a way to use this bipartite construction called a factor graph.
So it splits up those unlabeled edges, which are statistical dependencies, and kind of interweaves functions, which have a slightly different representation.
And it turns out that by interleaving these functions into the variables, it's possible to make what's called a factor graph.
And that gives an order of operations to arbitrary or within a certain set, any kind of Bayes graph, but it includes this one, importantly.
And so here is the one, two, three time points, and two policies are being selected.
And that's what this graph represents.
The organism comes in with a prior, time step one, two, three, there's two actions.
And then here's another figure from the paper, where at each of those three time steps, one, two, and three, a little bigger.
At time steps one, two, and three, there's the inference happening on time steps one, two, and three.
So time step one, that's like anticipation and planning.
At time step two, it's like short-term anticipation as well as memory.
And time step three, it's like memory.
And it's always now casting as well.
And so one can imagine that this is a really useful format because it's extremely composable on one hand.
So just like they said, okay, well, we kind of have this motif with the three time steps and the connectedness.
What if D from the top level came down and was S at a lower level?
And we've seen that taken to a really elaborated extent as well as interpreted in, for example, the paper on mental action in Livestream 25.
And so factor graphs are awesome because they're basically needing to only be specified in the Bayes graph format.
But then it provides not just a mesh connectivity, but a process algorithm and a heuristic approach that's actually tractable.
So we get the composable, analytical, and graphical component that's an tractable algorithm.
The next section is generative models for the allostatic control of interoceptive variables.
So this is going to be the first real modification of the homeostat that's introduced in three.
This is going to be the base case, but it could be something else other than body temperature.
The homeostat is simple but limited, as they write.
It can counter sensed changes of body temperature but cannot anticipate predictable changes of body temperature or other variables.
In nature, there are several regularities, e.g. night-day or seasonal alternation,
that can be easily incorporated to extend the above generative model as, technically speaking, empirical priors.
The obvious advantage of predicting how our bodily and interoceptive variables will change
is being able to exert some anticipatory or allostatic control.
And so this is kind of getting into the second order or anticipatory cybernetics,
also related to Rosen's anticipatory ecology.
So here's figure 3c.
In A and B, there was just the homeostat returning us to a set point after something got triggered.
And now there's going to be the affordance for anticipatory control.
This generative model, sketched out with the same scheme as the previous slide,
this generative model extends the homeostat by including a second set of exteroceptive variables
that correspond to light intensity, y2, and a belief about sunrise, x2.
That's the sun visual side on the right.
Furthermore, like the visual system, and the left side is still the temperature interoceptive system,
furthermore, the model includes a predictive relationship between sunrise, x2, and body temperature, y.
This edge isn't saying that the sun warms the body,
it's saying that in this model there's an edge reflecting a statistical dependency,
and that's where there's the degree of freedom with respect to the realism and instrumentalism, etc.
In this way, inferring a sunrise can trigger the autonomic response, u,
of thermoregulation in an anticipatory manner,
that is, before the sunlight actually increases body temperature.
The upper part of A and C are Bayesian networks,
highlighting that y is conditionally dependent upon x with the directed arrow between the nodes,
with more than one x and y in the model for the allostat.
The lower parts show the form of neuronal message passing that could be used to solve these generative models.
So, the Bayes graph is represented on the top,
and then there's the message passing with respect to the neural population.
So that's kind of the second aspect of figure 3,
which is just bringing in multi-sensory integration,
or even it could be like two pixels, for example,
with beliefs about each other, or something like that.
But that's what allostasis is going to be enabled by,
is just by this duplication of a column,
and then this connection in a different way.
And then here's the third section of 4, 7,
generative models for simple behavioral control.
And so they write,
The homeostat and the allostat permit the control of simple forms of swimming,
locomotion, reaching, and other movements.
One biological example is provided by the Zebrafish Virtual Reality Study 30,
which identified the neuronal underpinnings of error correction during escape behavior
in the animal's telencephalon, it's a brain region,
an evolutionary conserved set of brain circuits involved in action selection in other vertebrates,
including mammals, such as the corticobasal ganglia circuit.
So that's about the evolutionary homology of the brain region.
And then here's just some pictures from the paper.
By Torigo et al, 21.
Zebrafish capable of generating future state prediction error
show improved active avoidance behavior in virtual reality.
So they did a learning task that involved the fish being able to differentiate a signal
and then they studied the role of anticipation in that.
And the authors in this paper use that as an example.
Maybe we could talk about that or other examples in the dot one and the dot two.
Section eight.
Here's where we get to the very interesting operations that are going to bring this sort of descriptive model
of different kinds of homeostatic, allostatic, and intermodal,
and then behavioral regulatory elements into the evolutionary context.
So, our central argument is that evolution proceeded via gradual elaborations of the predictive motifs
illustrated above, under genetic constraints and opportunities,
and the selective pressure of novel problems to be solved,
such as the control of more sophisticated bodies in the presence of richer ecological niches,
e.g. when vertebrates began to establish life on land some 400 million years ago.
So, over successive generations, generative models can remain stable or be elaborated along four key dimensions,
strongly limiting the space of what is evolvable.
So, what are the four kinds of dimensions that are going to be changed?
That is going to be discussed in terms of the changes that can happen to the specifics of the generative model.
We have introduced the first kind of elaboration,
from the unimodal homeostat to the multimodal allostat.
So, they kind of secretly introduced this transformation between figure 3AB and figure 3C.
So, that was secretly like one of the transformations.
A second kind of elaboration is the duplication of predictive motifs,
which enlarges the animal's behavioral repertoire.
The third and fourth dimensions equip the generative model with temporal and or hierarchical depth, respectively.
These two expansions enable richer predictive motifs that endow a cognitive sophistication,
such as the possibility to plan or consider events that change on multiple timescales.
So, it's the evolutionary algebra on structure learning,
because we're outputting a structure, this graph G,
which is going to be like as if the species over evolutionary time
is going to be implementing some graph in terms of the structure of its model.
Like, if there's a case where the ant is not integrating the polarization of light with the olfactory system,
and then there's some change in the model that actually integrates them,
and then some relationship is learned,
whatever that means from a realist or instrumentalist perspective,
and that is going to be like an evolutionary algebra.
So, it's not going to be like 2X minus 3X,
but it's going to be more like that than not,
because there's going to be operations and they're going to happen in order.
So, here's figure 4, where they represent their evolutionary algebra.
Figure 4, the five main dimensions of elaboration of generative models introduced in the paper.
So, it was, you know, four dimensions, then it's five dimensions.
There's evolution in 4D by Jablanka and Lamb.
That would have been good to add to.
The five main dimensions of elaboration of generative models introduced in the paper,
illustrated as operations of an evolutionary algebra.
So, here's the five operations.
And so, we're starting with, on the left side, that homeostat,
that simple, corrective, calibrative, first-order cybernetic model,
either what the system is actually doing or model of.
Then, there's going to be five transformations that can happen,
and then it's showing there's a second round.
Like, once you go H, you can go H, T, A, I plus I, or I.
So, you have five discrete options at the first time step,
but one of them is no change.
So, it's kind of like no change or four different layers of excitement of the electron,
like four quanta, but they're four discrete operations,
like a deletion or an insertion in genomics.
And then, from there, it's just the state for the next time step of the model,
and then something else happens.
So, what are the operations?
The bottom is I, which is the identity operation.
That leaves the generative model as is.
So, that can be interpreted as like a non-mutation or just a conservative mode,
which is how most inheritance works.
Then, the second one is the duplication operation, I plus I.
So, it's like identity remains the same, but then there's a duplication.
Literally, it's like a genomic duplication, but in this functional space.
Replicates existing predictive motifs to form parallel sensory motor loops.
A is the operation that was described in figure 3C, the allostatic operation,
endows the generative model with horizontal predictive relations between different modalities.
And so, the duplication would be like going from one sensilla,
like one antenna to two antenna,
or going from one photoreceptor to two photoreceptors.
But the actual architecture of the column of the photosensory transduction cascade
would basically be computationally or statistically unchanged.
And then the allostat is actually bringing in this horizontal aspect.
It's not just two duplicated systems next to each other.
Now, there's actually connections between them.
And of the possible kinds of connections across columns,
one of them is like this classic allostatic motif.
Then, there's the ones that we haven't gone into as much, which are T.
The temporal depth operation extends the generative model
with separate variables for past, present, and future states.
So, it's kind of, from a graphical perspective,
what we looked at in the difference between the first factor graph,
which did take action at three time steps,
like the thermostat does,
to the one that actually has either prospectively looking anticipation
about future time steps or retrospectively looking memory.
But that's how the factor graph comes into play.
That's temporal depth.
Then, the hierarchical depth operation H
extends the generative model with separate variables
for states of affairs that change at different timescales.
Faster timescales at the bottom levels
and slower timescales at the higher levels.
Hence, modeling narratives such as music and language
where nested timescales are relevant.
So, to kind of split that idea of temporal depth into two pieces,
there's incrementing the number of steps you're looking in the model.
That's increasing the time horizon on policy selection
and increasing the temporal depth within a level.
And then there's this notion of nesting levels within each other.
That's the nested generative model
and therefore nested Markov blanket discussion that we've been having.
And that is going to be connected to cognitive activities like narrative.
And the reason why they're very similar
is that the timescales can kind of blur into each other.
And so, it's all about the model's structure as stated.
Like, this one is hierarchical and it has a depth of three.
It's a two-layer model and it has a depth of three.
Three time steps are included and it could be different.
If there was always looking two ahead and always looking two in the back,
then the model in the computer would need like a minimum of, you know, five time steps.
But the entity's model could still be restricted to S minus two, S minus one,
and then S plus one, S plus two.
So, those are the two ways that it can expand in these two temporal and hierarchical ways,
which is to nest hierarchically or to become temporally deeper with a longer horizon
given the nesting structure.
So, these are all structural changes.
That's why there was the whole piece about structure learning
because it's as if or actually like over evolutionary time,
there's the structure learning happen.
And then if we use this partitioning and Bayes graph approach,
then hypothetically, any kind of evolutionary starting point,
if we go back far enough, and then final state,
if we have all the transitions,
could be modeled within like a native active inference framework.
Section nine, they're going to go into a little more detail
about duplicating predictive motifs and enabling multiple behaviors.
So, they write, how does this,
they're writing on how does this duplication of the model,
looking at it from the outside,
it's like as if they're acting as if there's two models.
Looking at it from the realism in the inside,
it's kind of like thinking about the real duplication of a cognitive function,
that's functionalism,
or like even a neuroanatomical region,
like the earlier examples with the retinal cells,
and that's like an anatomical realism.
So, generative models can expand by duplicating simple predictive motifs
to form a larger repertoire of species-specific behaviors,
such as approach avoidance,
the control of the vibrace,
and visually guided grasping.
Classic.
The operator, I plus I, in figure four,
illustrates a generative model in which the same predictive motifs
are duplicated and specialized
to form a behavior-based architecture composed of multiple parallel sensory motor loops.
So, they're suggesting that because these are your affordances,
your operations in your evolutionary algebra,
you can go from this starting point,
it's kind of like Goethe-Lecher-Bach,
starting point,
and then doing operations to it.
Because you have the starting point and the operations to it,
it allows you to get to even relatively advanced motifs,
like approach avoidance, etc.
But a key piece is duplication,
because duplication of something without changing it
is how you are able to build more land to experiment in,
so to speak,
build more space.
And, um,
I copied some images from genetics,
specifically in the relationship of how gene duplication and divergence
in the early evolution of vertebrates,
this paper.
Um,
and there's a huge amount of genetics and genomics works
on the duplication and divergence,
and the neofunctionalization,
the sub-functionalization,
because if you have like an enzyme or a essential gene A,
not to go into the whole gene thing,
totally another time though.
Um,
you could have the function of the second copy in the genome be lost,
and then there is still like a continuous line of function.
So if you only needed one copy of A,
then this would be sufficient.
And then other times when you have A,
and it's dual functional,
like it binds to two different,
not exactly similar molecules,
then when there's a pyralogy,
when there's this duplication,
it allows sub-functionalization
or new functions to arise.
So that's how people talk about it
and link it to realism in genomics.
And this is kind of approaching that from a cognitive perspective.
Um,
there's probably more to say,
but we'll talk more about the duplicating of predictive motifs.
So how is duplicating predictive motifs
enabling of multiple behaviors?
Okay.
They write,
from a structure learning perspective,
duplication is an efficient way of building generative models.
And that's what it's all about.
In the sense that the dynamics are conserved
over different sensory motor domains.
This conservation is mathematically akin to factorizing probability distributions
on the generative model
that has been discussed in terms of modular architectures
and functional segregation
as a principle of functional brain architectures.
In Bayesian statistics and physics,
this kind of factorization is ubiquitous
and known as a mean field approximation.
Indeed,
the free energy bound on model evidence
is defined in terms of a mean field approximation
that affords an accurate and minimally complex explanation
for sensory data.
And so what are some of these citations?
44.
Modular architectures for factorization
of probability distributions in the generative model.
Par, Sajid, and Friston.
2020.
Entropy.
So here's kind of a cool figure.
Nice graph.
And then there's the message passing.
And then citation 48.
The mean field approximation.
What is it?
Here's a paper from 2001.
And they wrote,
algorithms that must deal with complicated global functions
of many variables often exploit the manner
in which the given functions factor
as a product of local interactions,
each of which depends on a subset of the variables.
Such a factorization can be visualized
with a bipartite graph
that we call a factor graph.
Dot, dot, dot.
A wide variety of algorithms developed
in artificial intelligence,
signal processing,
and digital communications
can be derived as specific instances
of the sum product algorithm,
including the forward-backward algorithm,
the Viterbi algorithm,
the iterative turbo decoding algorithm,
Perl's 1988 belief propagation algorithm
for Bayesian networks,
hashtag Markov blankets,
the Kalman filter,
and certain fast Fourier transforms,
FFT algorithms.
So it was 21 years ago
when this was happening.
And now we're here.
Okay, section 10.
Endowing generative models with temporal depth
supports perspective and retrospective inference.
So, just like we looked at with that factor graph,
giving this operation over evolutionary time
enables that factor graph to arise
from something with a lower time horizon.
The generative models discussed so far
only consider present states and observations.
However, they can be expanded
into temporally deep models
whose variables explicitly represent future
and past states and observations.
And so, this is what the operation looks like.
It takes XT and then at XT plus one or tau,
depending on how it's written.
And then now there's another time step appended
to the end of this model,
either actually or as if.
Here's something cool that they wrote.
They wrote,
various researchers have speculated
that a major driving force
for the development of deep temporal models
was foraging.
So, why would this happen functionally?
Which is to say,
why does the mutational spectra,
which does allow for this as an affordance,
end up selecting for and retaining
and enriching for temporally deep models?
Otherwise, we wouldn't observe it to exist.
And they're connecting that to foraging.
Intriguingly, this is a vertebrate example.
The same hippocampal circuits
that support spatial navigation and foraging
are also involved in prospection and imagination.
This has led Boussaki and Mosser
to propose that prospective functions
have leveraged cognitive and predictive maps
in the hippocampal and torrinal system,
and hence mechanisms of memory and planning
have evolved from mechanisms of navigation
in the physical world.
So, what are the cognitive demands of foraging?
How about information foraging?
How about mental foraging?
Here's some awesome papers
by Hills and Cousine and others,
Foraging in Mind
and Foraging in Semantic Fields,
How We Search Through Memory.
So, what about mental foraging?
What about individual and collective foraging?
This is an awesome paper
by Feynerman and Corman in 2017,
and they talk about the continuum
and the complementarity
of individual and collective approaches
to cognition,
and so implicitly like foraging as a phenomena.
Some of the affordances
and the neurophysiology of foraging in ants,
it's the same materials and mechanism
that any other insect that's not eusocial has.
So, the detection of light,
the intensity, the wavelength,
the polarization sometimes,
the ability to do chemo sensation,
like taste and smell,
mechanoreception, etc.,
and the same action affordances too,
like movement.
And so, there definitely is
Nestmate-level cognition in ants.
But also, there's things that are
of a few different interesting types.
One of them is mesoscale,
like small group,
dynamic stochastic teams,
and larger scale, like colony,
and even colony niche,
stigmergy,
and ecological scale cognitive processes,
like these two ants are interacting
and modifying each other's foraging behavior,
mechanistically and statistically,
but also it wouldn't happen
unless the niche were exactly this way,
which they have also,
in their extended selves,
established for themselves.
So, how do we think about
individual and collective foraging,
and stigmergy,
and complex systems,
and mental foraging,
and cognitive demands,
and cognitive security?
What about section 11?
Endowing generative models
with hierarchical depth
affords multiscale inference.
So, now we get to the hierarchical operation
that is going to give
that multiscale inference.
So far, we have described
generative models
that can deal with aspects of the world
that unfold at single timescale.
So, plus one, plus one, plus one
timescale is temporal depth,
but you're getting still only
one extra per transformation.
However, they can be expanded
into hierarchically deep models,
whose variables at different hierarchical levels
encode latent states
that unfold at different timescales.
One example is a song.
Melody remains the same
even though the notes we hear or sing
change rapidly.
And speech.
Similarly, a movie or narrative
remains the same for several minutes,
scenes remain the same for several seconds,
but visual stimuli can change
over hundreds of milliseconds.
Such models permit
hierarchical models
permit modeling of narratives,
songs, movies, and other events
that change at different temporal scales.
By encoding variables
that change more slowly,
e.g. melodies or movies,
at higher hierarchical levels,
and variables that change more rapidly,
e.g. notes or visual scenes,
at lower hierarchical levels.
Two neurobiological examples
of hierarchical organization
are visual areas in mammals
and areas that control vocal gestures
in birdsong,
which has been studied
in active inference several times.
And so here's another quote
from the authors.
In more advanced animals,
the hierarchical control of action
may have expanded
into sophisticated forms
of cognitive control
and executive function.
layer one scare quotes,
which help prioritize distal goals
while inhibiting immediate affordances.
So it's not just about
seeing deeper within a timescale,
but it's about being able
to pull up to a higher timescale.
And then from there,
after the H operation,
it can be followed up
with a T operation.
So here's the minute scale.
And then there's a hierarchical duplication
that allows for the hour scale.
And then that can go into two hours
and now two minutes.
So now there's a two hour
and two minute long model
instead of a one minute.
And it was just two mutations.
But if the two mutations had been,
or the three mutations
had been just going deeper
within the minutes,
it would be a different outcome.
How is that functional?
So what is the function
and the cost of temporal depth?
Just instrumentally,
when we're studying
diverse cognitive systems,
how can we detect temporal depth
and slash versus hierarchical nesting?
Then what is the meaning
and the role of narrative in cognition?
How does this relate to
narrative information management?
All right.
Section 12,
getting towards the end.
In the above,
which was, again,
the description of the simple motifs
in four, five, six, seven,
and then the evolutionary algebra
in eight,
and then several of these
finer scale discussions
on nine and 10 and 11.
We then get to 12.
In the above,
we formalize brain designs
in terms of generative models
that include predictive loops
of various complexity,
red,
and then discuss
the five main ways
in which generative model designs
can be elaborated,
green,
or the five main operations
of an algebra
of evolutionary structure learning,
figure four.
This means that one can describe
the evolutionary trajectory
of brain designs
in terms of
a limited number
of mutational operations
over generative models,
blue.
So,
here is
a phylogenetic tree
on the right side
with a
tree of life,
one of the tree of lives.
What are alternative,
complementary,
or traditional ways
to think about
phylogenetic trees?
In evolutionary biology,
are phylogenetic trees
interpreted instrumentally?
Are they interpreted
under a realism framework?
Is that what really happened
to those species?
Or is it
our model inference about?
What is the relationship
between active inference
and the free energy principle
and evolution?
Okay.
They have figure five,
which gets at their
phylogenetic model.
So,
this is a phylogenetic tree
of generative model designs
and putative correspondences
with animal brains.
So,
here's the implied
ancestral state,
and then
I
is going to be
the identity operator.
So,
here,
the orange species
has not mutated at all.
Now,
sometimes this is
conflated with
simply being an outgroup.
Just because it is that way
doesn't mean they're
making the conflation,
but sometimes people
will make the conflation
that because a species
is an outgroup
to some other clade
that has been included
in the analysis,
that it is the basal
or primitive form.
And so,
it does happen
to be that way
in this example
that the basal
is the so-called
least derived
or most primitive
or basal form,
but
my personal
thought is that
it should not be described
and
Tim Linksfair
and others have
awesome writing
on that evolutionary fallacy.
So,
in the rest of the tree,
which is being focused on,
different kinds of operations happen.
So,
here's that
I plus I duplication
and then
there's no change after that.
And then this one has
A and so on.
So,
just like you could trace
the phenotype
changing through time
on a tree
inferred from
trait or
genomic data,
which is just another trait,
this maps up
to certain changes
that are seen
neuroanatomically
over vertebrate evolution.
And it reminded me
of this paper,
which was
Chakraborty
and Jarvis 2015.
And so,
that is the paper
Brain Evolution
by Brain Pathway Duplication.
So,
they don't connect it to
in the exact same way
the neurocognitive
and the functional
and the active inference
and all of that,
but this paper does get at
some of the very similar ideas
about the functional duplication
arising as a result of
pathway duplication.
Um,
they have
a section on
brain complexity
and pathway evolution.
They talk about
some alternative hypotheses
and then talk about
distributed and
duplicated morphological
structures.
So,
it's a kind of
interesting paper
from about seven years ago.
Another paper
that's very related
to this idea
of doing like
an evolutionary algebra
with combinatorics
but also a path dependence
is this paper
pretty recently,
just a couple days ago
by Ryan Smith,
Maxwell Ramsted
and Alex Kiefer.
The paper is
Why Bayesian Brains
Perform Poorly
on Explicit Probabilistic
Reasoning Problems.
So,
look at this tree
that they have.
The starting point
and then three actions.
So,
here it's like
divide,
divide,
multiply,
divide,
add,
divide.
And then they study that
in the context
of Bayesian Brains
and doing calculations.
Why is it hard
to multiply numbers
together sometimes?
So,
then the authors
of the paper 38
write,
Interestingly,
the mutational operators
are commutive.
The same generative model
design can be obtained
by executing
the same operations
but in a different order.
The commutative property
of mutational operators
potentially sheds light
on the convergent evolution
and the process
by which unrelated organisms
evolve similar traits
independently
and via different
evolutionary histories
when they need to adapt
to similar ecological niches.
That's pretty cool.
Alright,
so just the discussion
and then a few last points.
So,
discussion
and the authors
summarize it.
In this article,
we suggest that
brain structure
or design
could be formalized
as generative models.
Agree?
Disagree?
That the brain generative models
of our evolutionary ancestors
included simple
predictive motifs.
Agree?
Disagree?
And that the evolution
proceeded via successive
elaborations of these
predictive motifs
into more complex architectures
that we observe
in advanced animals.
They then talked about
the ways that that can
change through time
functionally.
And then they write,
while the evolutionary
trajectory of designs
for predictive processing
proposed here
is certainly tentative
and incomplete,
we consider it
a first step
towards the alignment
of predictive brains
in evolutionary studies
of neuroanatomy
in different species.
So if this is the first step,
where are we headed?
And why do we prefer
and expect ourselves
to be there
or go there?
Just a few more topics
that we could talk about
like in the dot one
and in the dot two.
First would be,
they write that
the error correction mechanisms
!
In their view,
encompass the simple
and the complex forms
of adaptive behavior.
Hashtag integrative theory.
And they're going to argue
that that differs
significantly from
prevalent perspectives
in psychology
and neuroscience,
which tend to
separate sets of mechanism
for sensory motor processing
and simple cognition.
So,
how is active inference
similar and different
to other frameworks
for behavior?
What are the building blocks
of adaptive behavior?
What are the basal blocks
of just any kind of behavior?
Where does sensory motor
integration come into play?
How about mental functions
and cognitive functions
like memory,
anticipation,
counterfactuals,
etc.?
Okay,
another point to kind of
think about
or write your questions down
and reflect on
is the perspective,
which is still speculative
and not unchallenged,
suggests that the complexity
of the ecological niche
determines the level
of complexity
that the brain needs to have
in order to be
Bayes optimal.
In other words,
brains only increase
their complexity
with sufficient
ecological demands.
So,
not necessarily
just that mutational
direction
and intensity
will go towards
increasing brain complexity
from ecological demands,
the so-called
anticipatory evolution
that cognitive entities
can have
through self-modification
and niche modification,
but even for those
that aren't actually
doing anticipation,
still it could be the case
that when the ecological
demands are such
that a behavioral model
increase in complexity
is selected for
and retained,
then evolution
will go that way.
This is because
having a more complicated
brain does not help
if you live in a simple niche.
So, that's like
a very costly model
that's not giving you
any more return
on investment.
They then talk about
how the social brain
hypothesis
states that
the necessity
to predict and deal
with sophisticated
social dynamics
was a main driver
of the evolution
of large brains
and sophisticated
cognitive abilities
in our species,
people.
In short,
the gradualism
expressed as a
progressive increase
in complexity
rests on the
circular causality
implicit in the
modeling of an
eco-niche that is
itself constituted
and constructed
by increasingly
complicated phenotypes.
So, because it's
so important to think
through other minds,
first, just how you're
going to materially
avoid a spatial collision,
but then,
so the social brain
hypothesis goes,
includes increasingly
recursive levels
of game theory,
market theory,
and all this
kind of stuff
and related
indirect cognitive
phenotypes required
like memory
and recognition,
narrative understanding,
rhetorical understanding,
governance, etc.
That is being
posited as
compatible
with the models
the authors have
written and a
hypothesis that
others have written
about, not from
an active inference
perspective, though,
in most cases.
So, what is the
cognitive niche
for social entities,
our material niche
and our social
cognitive niche?
What is the social
brain?
What is the
eusocial brain?
How are they
related?
So, for example,
the social brain
is saying that
the more social
things are,
the more sophisticated
the brain has to be.
Well, you need
more narrative
understanding
and more memory.
But what if
in the eusocial case,
the brain is
simpler on board?
For example,
it's more role-based
or temporal
polyethism has
allowed more
reduction in
each phase of
the life cycle's
brain.
So,
does social
lead to eusocial?
How does eusociality
arise?
And how does it
elaborate?
How do different
kinds of sociality
arise and elaborate?
And how is that
associated with
the different kinds
of models
structurally changing
that we've been
discussing in this
paper?
and then just
genomics,
all the other stuff,
gene expression,
and then just
one last point,
which is the
closing piece
of their paper,
too.
Finally,
it is important
to acknowledge
that brains,
design,
bodies,
ecological,
and cultural
niches co-evolved
independently.
Not sure if that
was what they meant.
It's kind of like
they are co-dependent
in their co-evolution,
but they co-evolved.
They were alone
together.
Given that here
we were interested
in the evolution
of brain designs,
we assumed
a brain-centric
perspective
and conveniently
focused on
generative models
in the animal's
brain.
Hashtag realism.
In the brain,
not modeled
as in the brain.
However,
cognition does not
need to be confined
in the skull
to be extended
outside it,
to cover,
for example,
tools and social
dimensions.
Epistemic niche.
Niche modification.
Digital stigmasy.
Furthermore,
the body design
and not just
brain design
plays an important
role in solving
control problems.
Acknowledging that
cognition can be
extended and
embodied,
and encultured,
et cetera,
all the E's,
all the other letters,
suggests that not
all aspects of
control need to be
solved by or
represented in a
central generative
model.
Tale of two
densities.
All the discussions
we've been having
about representation.
And so it was
X and X star
in the simple
version that was
presented in this
paper,
where it was
actually trying to
track X star
in the world
with the internal
inference.
But this is the
discussion that
we've been having.
Do those
representations have
to structurally
resemble the
world?
And there's other
papers that we've
discussed in the
last several weeks
that really touch
on that point.
So how do we
think about
generative models
and factor
graphs for
extended cognitive
processes?
So a couple
books to check
out about
extended mind
and embodied
cognition.
And then here's
a nice figure
from touch
points with
the brain,
the organs,
and the body,
the world,
and the tools,
and the epistemic
niche,
and the computers,
like a calculator,
and time,
chronos,
and food,
and then other
people,
social.
So that's like
cognition.
It's like a
holistic integration
of all these
features.
What does
embodiment,
this perspective,
have to do with
realism and
instrumentalism,
and utilitarianism
and other
philosophical
positions?
Are people
really taking
those positions
or is it just
as if they're
taking those
positions?
And then what
else are you
really curious
about and
motivated to
explore?
And how will
you modify and
improve your
epistemic niche?
So hope you
enjoyed this kind
of solo dot
zero video.
I think it's
been a little
bit since the
solo dot zeros,
but just
want to close
as always
with what
might a good
understanding
enable?
What are the
unique predictions
and implications?
What are the
next steps for
free energy
principle and
active inference
research and
application?
What are the
goals of this
research?
And what are
you still
curious about?
We're going to
be talking about
this paper in
the coming weeks
on February
16th and
February 23rd.
And so if
you'd like to
participate in
those discussions
through live
chat or by
joining the
discussions live,
just get in
contact with us.
Hope you read
this paper because
it's very thought
provocative and
interesting.
So enjoy the
pape and
work through it.
Hope to see you
in other
active lab
activities.
Thanks for
listening and
your regime of
attention.
Goodbye.
Bye.































Thank you.
