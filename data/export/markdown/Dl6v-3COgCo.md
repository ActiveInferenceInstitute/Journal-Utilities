---
title: "ActInf Livestream #042.0 ~ "Robot navigation as hierarchical active inference""
category: "Livestream"
series: "Livestream_042"
episode: "0"
duration: "2:06:53"
url: "https://www.youtube.com/watch?v=Dl6v-3COgCo"
views: 361
exported_at: "2026-02-18T22:37:37.729784+00:00"
format: markdown
---

# ActInf Livestream #042.0 ~ "Robot navigation as hierarchical active inference"

All right.
Hello and welcome to ACT-INF livestream number 42.0.
It's April 16th, 2022.
Welcome to the ACT-INF lab.
We're a participatory online lab that is communicating, learning, and practicing applied active inference.
You can find us at the links on this slide.
This is recorded and an archived livestream, so please provide us feedback so we can improve our work.
All backgrounds and perspectives are welcome, and we'll be following good video etiquette for livestreams.
And Sid, thanks a ton for joining.
Really looking forward to this conversation.
If you want to learn more about ACT-INF lab activities, check out activeinference.org.
Okay.
We're here in ACT-INF livestream number 42.0, and we are starting to learn and discuss this paper,
Robot Navigation as Hierarchical Active Inference, in the journal Neural Networks, October 2021.
It's by Ozan Katal, Tim Verbellen, Toon Van de Malle, Bart Dote, and Adam Safran,
and some of whom we're looking forward to speaking with in the upcoming weeks.
And this video is an introduction for some of the ideas and just some background and context
and rapidly assembled fun and memes that we'll go through.
So it's just an introduction of a discussion, and we hope that if you're watching live or later
that you can still contribute to this.
And we're going to go over the main aims and claims of the paper, then the abstract and roadmap,
and then walk through some cool keywords and context, which will be great to hear.
Sid's perspective from working with robotics, which is an area that certainly I've never actually been
involved in.
So going through some of the more applied work that we're going to see with robotics, and also some
of the more formal aspects from active inference, and then this third vector that maybe we both share,
which is some of the biological basis of navigation.
So we're going to just go into the introductions first.
I'm Daniel.
I'm a researcher in California, and I'll pass to Sid.
So Sid, I'll walk through your slides, but yes, let's hear it.
Yeah, let's go to slide nine.
And before I even address myself, I would say that we need to address the elephant in the room,
that this is live stream number 42, which is one of my favorite numbers.
And the favorite number for a lot of people, because it's the answer to life, universe, and
everything.
So this is the first time that I am coming to an active inference live stream.
And I'm actively inferring the whole idea of active inference itself.
I'm very new to the field.
So yeah, I'm very excited to learn a lot of things.
And yeah, just as we are on this slide right now, 42 has a lot of other references that you can check out on that Wikipedia link.
Okay, moving to the next slide.
So I usually document like the many things that I've been up to at this particular link.
And in the next slide, I highlight like the few places where I have had the fortune to be at.
So I formerly have studied computer science and design.
And I've like meandered by accident and by intention in a lot of different places that you can see here.
So I studied computer science at a university in India, which practices a lot of hands-on experience.
And that's where I got my start in robotics and a lot of other things.
Then studied further through various participatory workshops and internships at space organizations, media labs,
and then spent two years at financial services to understand how money works.
And was introduced to robotics mostly through open source software in the bottom most thing that you see here.
That's the Google Summer of Code program.
And I would go into more detail about how that robotic journey even started.
These days, I'm very much interested in how coordination happens and how we can think about security of countries and communities in general.
And more importantly, all the emerging aspects of society.
That's technology, economics, culture, and policy.
So I know that active inference is a study of autonomous behavior.
And we are moving into this era where decentralized and autonomous organizations are gaining a lot of popularity as well as mainstream acceptance increasingly.
So it's very interesting to see where this new field of study that's active inference, that is a field that is invented in our lifetime.
Like it's very rare to see that you get to explore a field that is so recent and has a long history, like through connections to other fields.
So it's definitely an evolving area which can help explore other evolving areas.
And that's what I find very fascinating about applying active inference in the way that it's applied in this paper as well.
So I'll try to explain like the history of robotics in a way through the lens of my experience with it.
So one of the first things that I did when I started studying.
So as you can see, I started studying in 2012 and immediately jumped into like all the robotics labs that I could get my hands on in university.
And one of the first tasks that was very appealing to me was like multi-robot teams.
Like how do teams operate?
Teams have been like a constant like fascination for me throughout life, like human teams, teams of biological organizing, like organizations and organisms such as ants and bees.
And then teams of like robots.
And we derive a lot of like inspiration as well as a lot of like biomimicry kinds of techniques in multi-robot exploration as well.
So the specific topic that we were studying is in the next slide, which is multi-robot terrain exploration.
So if we go to slide 13, these were the different like techniques we were studying, like just like ants leave pheromone trails and different signals for other members of their colony.
We tried to model these kinds of similar techniques like recency, like how recent was it that a robot that was covering a particular terrain that has been that hasn't been explored before?
How recently was that covered?
So you can imagine this as like a grid.
So a two-dimensional grid.
And you see the green squares.
Those are the multi-robot teams.
So the green square represents a robot.
And they are trying to explore and map out this entire area as a team.
And the assumption is that they can communicate amongst themselves.
And in certain cases, they cannot.
So the red squares represent obstacles.
And you will see a similar obstacle map in this paper, which in which they use a warehouse.
But we were using similarly configured different obstacle maps, both in a simulated environment as well as a physical environment.
So we explored different approaches back then, which is things like just representing them as an automata, like giving them very simple deterministic rules, which they can follow.
And those could be imagined as simply as Conway's Game of Life, like the glider pattern or similar patterns that you might know.
And then we moved on to more animal-inspired or bio-inspired techniques, which is a technique like recency, in which the robot leaves pheromone trails in each square.
And each square has like a countdown timer.
How recently was it visited by any other robot?
So this can be understood as ants leaving trails, which decay over time.
And this gives other ants an idea of how to map that surrounding region effectively.
And then there were very simple approaches, which were more suited for the digital world, such as simply node counting, that how many robots have visited this node before.
So every time you visit any square, you just increase its count, visit count by one.
So that helps the robots in understanding, okay, this area has been visited five times and the surrounding squares have only been visited two times.
So I should maybe explore the unexplored regions first.
So these were different techniques that were used.
And we moved on, published a few papers and were also inspired by military organization techniques.
The typical OODA loop or the observe, orient, decide, and act, which is kind of applied active inference in a way.
So we did explore that, like clustering approaches and different ways of conquering the whole map.
So this was an exploration and exploitation problem that I had the opportunity to study in second and third year of my undergraduate computer science.
And then I went on to, like, fancier things, thanks to the Google Summer of Code program.
So this was a project with the Italian Mars Society, which reports to the European Space Agency.
And here it was more about autonomous navigation working with a human.
So this was a robot and a human team working together.
And the next slide shows, like, how it actually happened.
So if we go to the next slide and play the video, we will see that it is meant for an astronaut who is safe in a Martian habitat.
And the robot is a rover, which is exploring the Martian terrain outside in a more dangerous environment.
So every movement of the rover comes from the astronaut's movements, which are mapped from an omnidirectional treadmill that the astronaut is walking on.
And similarly, there is feedback received from the rover's camera, which feeds into the astronaut's virtual reality headset.
So do note that this was back in 2015 when headsets were clunky, when things moved very slowly.
But Kinect was all the rage, like mapping body movements, mapping, like, robot movements in unexplored territory using 3D cameras, which is a technique that this paper also uses, using RGB and depth cameras.
So those were the techniques which still are very popularly used even today.
So this was my introduction to understanding how different, like, robot and human teams can work and how telerobotics and telepresence can work.
So my responsibility in this project was to do the entire networking architecture and ensure that there's no latency or there's no feedback in which a robot can enter a dangerous state just because the astronaut did not receive the information on time.
So this is how we began.
And the operating system that we used in that particular experiment is on slide 16.
So whenever the video is done, we can move to the next slide.
So in slide 16, you see a husky robot.
So these are open source robots that are very popularly used with the robot operating system.
And we'll keep coming back to this particular framework of ROS.
So ROS became extremely popular.
It gained its reputation from the earliest DARPA challenges in which a very popular car just crossed through an entire desert terrain navigating autonomously.
So ROS was an open source robotics library, which was built out of that.
And you see many different sensors and actuators on this particular rover.
So you see a lot of symbols which will be repeated in this particular paper as well.
So the task of a localization technique is to gather all these sensor inputs, fuse all those inputs.
So the sensors can be understood as IMU or like measurement units, inertial measurement units, such as like accelerometers and speed and all those measurement metrics.
Then you have camera, which is similarly RGB, that's red, green, blue colors of the visible spectrum.
And then you have 3D sensing in the sense of the connect sensor that you see on that particular robot.
And you would see a similar setup in this paper as well.
They use a turtle bot to wire robot, which we will get into, which is also using ROS.
And it uses the same concepts as we used in that particular paper.
So all these different attributes such as GPS, 3D sensing, odometry, camera, and IMU are inputs to the robot localization technique.
And all of this together is meant to estimate the three-dimensional surroundings of a particular robot.
And all these techniques do not use active inference.
They used probabilistic methods, which we will slightly refer in the paper.
So it's very promising to see that if we are inspired so much from biological ways of navigation, we should rather use a technique which organisms have evolved to be so effective at over so many years.
And as humans, wayfinding was considered a survival skill for a long, long time before we entered the era of Google Maps.
And we just totally lost the technique of finding our way around rural, urban, and natural settings.
So wayfinding and navigation and localization and mapping was a technique which is very familiar to anyone in their 70s or 80s.
If you ask them, how would you find your way around a city block or the jungle?
They will have their own ways of navigating that.
So they will either use natural cues like wind direction, the way the sun is setting, the map that they have already covered, asking people around.
So these kinds of techniques are built in our human brain.
And it's very natural for animals to use that as well in urban as well as their own natural environments.
So this paper goes into these many big questions, which is in the next slide, slide number 17.
So over to Daniel, where he illustrates all these wonderful connections.
Thanks for the innovation on the live stream format.
A lot of fascinating backgrounds.
And it sets us up really well to discuss some of the big questions of this paper and some of the big questions in general.
So one big question, just the kind of thing that would bring somebody to want to even read this 2021 paper or future work is how do biological, like evolved and human created mathematical, statistical and robotic.
So several different kinds of human created entities.
How do biological and human created entities engage in actionable, tractable, adaptive navigation in complex, conditional and changing landscapes?
And that's a question that one could ask about everything from the organismal level to the colony level, arguably also an organism, but in a little different way.
And all manner of biological systems.
And then here is a really nice slide from this Bill Ant Robotics Project, where they did a direct side to side of the harvester ants anatomy and also their robots anatomy.
And that's kind of like a bridge that takes us into a different space first with the walking around the warehouse.
And does it stay standing when it gets pushed?
And can it localize when somebody turns off the light in the room?
And these sort of basic, though still relatively advanced, but also relatively basic tasks and settings.
And then off on the right side here are some of the visions and representations that people use for when those low level activities are such that if a robot can resist being pushed over, then how does that have complex feedbacks with society?
So it was just something that you also impressed upon, like the very holistic nature of this area and also just how to keep a lot on the table talking about it.
So that's what will be fun to talk about.
What do you think?
Yeah.
I think before we enter into the paper itself, I would want to understand from you, like what has been your learning from observing ant behavior and studying their actions in such an environment, like in natural as well as artificial environments?
I can hopefully accurately relay an anecdote for my PhD advisor, Professor Deborah Gordon.
And she would often talk about how there would be at a conference or some type of competition.
And this is something I've observed, but to a lesser, smaller extent is there'll be a presentation of an algorithm or a robotics implementation of so-called swarm algorithm or ant colony algorithm, ant colony optimization.
We see it on the pure optimization or computer only, but also a lot of bio-inspired robotics design.
And one common feature of these algorithms is that there's some like underlying map that's shared.
Like when you mentioned the grid counting, of course, there has to be like a mesh network so that the robots kind of have basically either telepathy or some kind of common signal, even if it's asynchronous or something like that.
But there has to be some sort of like updating of the grid in their mind.
And being in the field and also drawing upon what we know about what we know about ants, the nest mate, when it's deciding to forage or not, it doesn't know how many seeds the colony has, how many seeds are out there, what the right decision would be.
So it must use stochastic interactions that it receives locally and cognitive constraints to make its decision.
And then once it's out there, there's no telepathy amongst the ants.
There's no queen control.
There's no forager groups that all like tell each other orders and all of that.
So that navigation is also multisensory and related to their cognitive constraints, but also their finesse in a certain niche and a harvester ant is not going to forage well in the Arctic.
And so understanding how it's that interplay between the nest mate and the colony and the variability of the environment, it's a really rich area and it's easy to bring in other modalities that humans can use like long range communication and understanding how those novel affordances for decentralized systems design do or don't relate to some of the ways that biological systems work.
That's a really fascinating area.
Yeah.
Yeah.
And the reason I think that this paper is relevant, first of all, because it's based on active inference, which is like the study of how the human brain would react in certain scenarios, but more broadly, how a biological organism or an organized colony would react in those kinds of situations.
And just like you said, the map may not be shared in certain cases.
The map, the team might be decentralized.
Communication might be unavailable.
These are extremely realistic situations, even for groups of robots today.
So you can imagine these as robots who are exploring the fallout of a nuclear situation, like when a nuclear plant needs to undergo maintenance and humans cannot enter that area.
So you cannot assume 100% communication when the robot is mapping out that area.
So this is one of the important reasons why some amount of cognition and some amount of active inference of the terrain is extremely important.
And our infrastructure in robotics as well as communication is only now getting there.
Like with the new standards introduced in 5G and 6G networks, we will start getting into scenarios where robots become parts of our daily lives and they already have.
So I'm based in Singapore and it's very common to see cleaner robots and teams of helper robots moving around, like in university campuses, as well as airports and shopping centers.
So these robots have covered the entire terrain already.
So they use like very basic approaches of obstacle avoidance and trying to clean the entire area and complete their objectives.
And there is very little stochastic action going on there because most of those tasks can be completed in a hard coded map that is shared among those robot teams in a very specific, highly connected way.
environment.
But when we start moving into more urban environments where this cannot be guaranteed, we definitely need approaches like the one described in this paper.
So, yeah, with all that context, we can jump into the aims and claims of this paper.
Awesome.
So just to read some of the aims and claims, which we're going to revisit a bunch.
The paper is Robot Navigation as Hierarchical Active Inference.
And some of their main claims were that they are going to first propose a hierarchical generative model casting navigation as minimizing expected variational free energy.
So that is what brings all of these areas of navigation and robotics under the umbrella or drawing an edge to active inference framework.
We show how perception, localization, mapping and navigation naturally emerge from optimizing this hierarchical generative model under active inference.
So that's sort of the theory and background and some of the formalisms that we'll go through.
Then they implement the system in silico on a real world robot platform, navigating a warehouse environment using camera sensor input only.
And then they also have this third angle, not just the theoretical and the robotic implementation of that, but the biological.
And they relate their work to various findings and hypotheses in biology about navigation in the rodent and primate brain.
Okay.
Yeah.
Do you want to read that?
I mean, these are wonderful claims.
Before we jump into the claims, I was very fascinated by like the list of authors of the paper.
So I'll just zoom into that a bit if that's visible on the slide.
So, so you see that three, three of those authors are located in Belgium and the last author really fascinated me because they come from a center of psychedelic and consciousness research, which happens to be one of my favorite facilities in the entire world, focusing on these kinds of topics.
So, um, I would also like to ask you that how do these, uh, kinds of, um, like multidisciplinary research, um, like show through in this particular paper.
So obviously we have teams of engineers and researchers from Belgium, but we also have an author from a very different field.
And how do you think that contributed in this paper?
That'll be something great to ask them when they visit.
But I think at the general level, we see, uh, several factors, including like, of course, a shared interest, common framework in active inference.
Also, I'm sure some, uh, we'll have to find out in this specific case, but it's a great question and it's an important question.
Okay.
So, um, I'll read the abstract first half and then, uh, or the first three.
Localization and mapping has long been a standing, uh, localization and mapping has been a longstanding area of research, both in neuroscience to understand how mammals navigate their environment, as well as in robotics to enable autonomous mobile robots.
In this paper, we treat navigation as inferring actions that minimize expected variational free energy under a hierarchical generative model.
We find that familiar concepts like perception, path integration, localization mapping naturally emerge from this active inference formulation.
Yeah.
Moreover, we show that this model is consistent with models of hippocampal functions and can be implemented in silico on a real world robot.
Our experiments illustrate that a robot equipped with our hierarchical model is able to generate topologically consistent maps and correct navigation behavior is inferred when a goal location is provided to the system.
So, um, yeah, I mean, that's a lot to get into.
Yeah.
I mean, so the paper makes a very simple claim.
Like if we broadly look at the paper, it makes a very simple claim that active inference works and it's able to consistently reproduce maps, which are, um, representative of the physical world map.
Um, so, um, this also goes into, um, this literally goes into the map is not the terrain, um, kind of discussion that we have been having in active inference live streams.
Uh, and, uh, in this case, they are able to consistently reproduce a particular kind of map.
That is a warehouse kind of a setting and they compare it with many different approaches and there's many different tasks that you can see here.
So the highlighted tasks, uh, tell you that there's perception, which is understanding the entire environment, then combining all the parts that can be taken from point A to point B and then localization, which is understanding your own position as a robot in that particular environment.
Um, and then mapping, uh, as you are doing all of these things, simultaneously localizing your position and state as well as mapping, um, the entire region.
Um, while you're doing that.
Um, and all of these are naturally emerging from like formulating it as, um, like active inference, which is minimizing, uh, expected variation of free energy.
So, um, so yeah, just before we go into more detail, like, do you want to explain to robotics, uh, researchers who might visit this live stream about why they should, um, care about variational free energy.
And probably these new words that, um, that might be very important for them.

Thanks for that.
Very clear summary.
Nice.
Thanks for that.
Very clear summary.
And definitely we hope that this kind of a presentation, at least in the dot zero and also in the group discussions, it's like a two way street.
So people are going to have different amounts of familiarity with some of the robotics as well as with the active inference.
So to anyone who's anywhere in that space, I think there's a lot to be said for just taking a first principles approach.
That's sort of a simplicity and elegance route.
There's value to be found in transdisciplinary approaches like localization and mapping and cognitive affects and emotion.
Some of the cycle logical frameworks that we've been discussing in other live streams or other papers.
And so there's value in not just simplicity, but in finding connections like complexity and patterns across systems.
And I think also for something that is clearly so nascent in its development to be able to, as Sid is describing, have some functional closure of maps and cast this problem of like, where is one and how should one act?
And what is the bigger space map look like and all of those things, which as discussed in the real world, have all these other challenges like the communication of those maps and everything.
However, just at the individual wayfinding route, drawing on first principles from biology and being a part of a conversation that's clearly already functional, but also has a lot of potential is probably a good thing to at least listen to.
Okay, so how do they do that?
Here's the roadmap.
Here's the roadmap.
In the beginning, they introduced the problem and some of the background, just like we've done in these last minutes.
They then discuss some biological perspectives on navigation.
They then formulate in sections three and four, the hierarchical active inference model for navigation.
It's going to be a two layer model, and we're going to go into it a lot and there'll be colors that are consistently associated with the levels.
They then discuss the experiments, which is the implementation, the mrobotment embodiment of the robot, and then they have some discussion.
Okay.
Yeah.
Before we enter into each of these specific topics, like I would share what I had shared with Daniel a week ago when we started approaching this paper.
So, I mean, this paper is exceptionally well written, even if you're not from any of these fields.
So, just looking at like the language that's used, it's very easy to follow for the most part.
And they make references to like topics which people will be familiar with.
So, they explain active inference, free energy, and all these different concepts of SLAM and very technical terms in an extremely simple language, which is why I think it's a great paper to start with if you are new to either of these fields, robotics or active inference.
Very true, because I know I was looking up a lot of robot citations, watching videos and learning a lot because it's just totally not my area.
And I can imagine somebody with a different background would have a different experience.
So, it's, I agree, an awesome written paper and it exists for anyone who wants to go into more detail and check out the citation networks if you're in the future.
They listed several keywords, active inference, robot navigation, deep learning, SLAM, simultaneous localization and mapping, and then RAT SLAM, which is a biologically inspired version of SLAM.
So, let's just go to your active inference meme.
If you would like to give a real time meme reading, please feel free to.
Yeah, so the meme explains itself.
And this is essentially the teaching robots, like as if you're teaching a child.
And I think that is essentially what all kinds of learning techniques come down to.
And there was another meme of like a toddler reading neural networks for babies, which is not in this presentation.
But that meme essentially meant that a neural network is learning how neural networks work.
And so, this meme is inspired by that, that in order to solve a particular purpose, you need to infer actively, which means you need to firstly be active.
And that's the first condition.
And the second condition is that you need to be constantly inferring like your own assumptions about the environment, about the observations that have transpired in the last few time steps, and then continue to do both these steps in a loop.
And in that combination of those two loops, you are able to solve that purpose.
So, the meme is inspired from Rick and Morty, in which the only sole purpose of that robot is to pass butter.
And in this case, that sole purpose of just implementing active inference in a robot is all that's needed to solve that particular task.
And that is intended for the claim of the paper.
So, that is why active inference as a whole, I think, is like all encompassing when it comes to like doing all the steps that we covered in the last seconds.
Rick Archer, I'll only comment on what you said, because it's so true that as a holistic and composable model, it'd be possible to bring in different sensor modalities, different communication, connectivities, different actuator possibilities, and active inference could grow in terms of how it's being used.
Rick Archer, So, this is like relative to some other possible algorithms, which would have to be composed in a bit of an ad hoc or in-principled way.
This is a way to explore just that you infer actively could be for the robot in condition A or the robot in condition B, depending on the generative model and the Markov blanket and the external states in the world itself in the context.
Rick Archer, So, let's just go straight into the meme analysis of this second video meme you have prepared.
Rick Archer, Yeah, meme analysis is something new that might be unique for this live stream, at least in this animated format.
And as you can see in this particular meme, and in the previous meme that a robot has to forget all their existing SLAM techniques that robots are popularly used.
Rick Archer, So, we go into many different techniques that are cited in the paper.
Rick Archer, So, one of those techniques is obviously RAT SLAM, which we will go into next.
Rick Archer, But probabilistic robotics is like this popular book, this classical book, which was used by robots of the last decade or two.
Rick Archer, And it describes many different approaches of how SLAM can be implemented.
Rick Archer, And all techniques that we see in conventional robots today, whether it's like a robot that's cleaning your house or a robot that's serving you food in one of those experimental restaurants, all of them use probabilistic robotics techniques.
Rick Archer, And this meme in particular goes into firstly the mission of this entire participatory lab, which is ACT, INFER and SERVE.
Rick Archer, And once you do that, once you do all these three things as a robot, you're able to successfully navigate your way around these very confusing terrains, which might be complex and dynamic.
Rick Archer, And on the top you have a diagram which describes how deep learning methods typically work and how this paper implements one of those techniques with an active inference flavor on top of it.
Rick Archer, So, Dan, do you want to describe like how active inference and deep learning like how this like combination of these two fields has come through in this paper?
Dan Kaur, Sure.
Dan Kaur, First, I'll interpret the meme and then describe the deep learning, but then we'll get into more details as we actually walk through the paper.
So, I see the ACT, INFER, SERVE of ACT, INFLAB, which is open to anybody who wants to participate.
And then it's a little bit like the experiment where people are passing basketballs to each other and then something unexpected crosses the screen and many people will not report seeing that other thing crossing the screen.
But there's a lot of analogies to other cognitive contexts.
So, it's like we're focused in the lab, but then also we have to be aware of the unknowns and the unexpected and the anomalies within the anomaly space.
And then that's how we get to four, which is like the tetrahedra, which is bigger than just us, anyone.
So, how to be doing that Nestmate thing that we can juggle and three numbers in our head at once or seven numbers in our head at once or can only grab two things at once or even fewer.
So, how do we actually use these limitations that we have and be part of still a bigger navigation?
So, it's a nice meme.
Basically, this paper is going to present a method that uses some model structures from active inference, but also uses some more mainstream deep learning and machine learning techniques.
And those methods we'll talk about more like the specifics of how they're combined, but it contains both things that are like machine learning, neural network type approaches, as well as that being structured in an active inference way.
And that active inference structure, when it's just with simple matrices, can be looked at like in the model stream one or in active inference, a step-by-step guide.
That's the very simple matrix multiplication, very austere kernel of the active inference structuring.
And then here, because some of the data includes like video data and it's being implemented on modern hardware, it does have like a deep learning, machine learning aspects and modules to it.
Okay, so here's SLAM. Finally, finally, the keywords.
So, researching it, I found this paper, Are We Ready for Service Robots? and presenting a dataset for SLAM.
And on the bottom right, it's showing some different scenes as well as how they change.
And the paper concludes that with respect to this challenge of simultaneous localization and mapping, that various factors can often confuse a robot.
And so, one can imagine this is just like an algorithm that has a blind spot or some sort of area of poor performance for any number of reasons.
And that's exactly how these authors begin the paper with being able to robustly explore and navigate an environment has been a longstanding challenge in robotics.
So, the paper just begins with what we've been talking about, which is that this is like a perennial and a cross system problem, but also in hashtag 2022, it's far from solved in real world settings.
What else would you add?
Yeah, I mean, I especially like the title of the paper, which describes why we are doing all of this.
The title is, Are We Ready for Service Robots? And in the previous meme, we saw that the third pillar of the trifecta after ACT and INFOR is serve.
So, all the robots that we are building and most of the applications that we focus on are meant to serve.
They have service as an objective function. And that is what makes this task challenging, because if you are replacing human actions by a robot, you have to forget all the assumptions we make when dealing with human teams,
because human teams are dynamic and they learn on the fly. And obviously, they might not be as effective as a robot who might be better evolved to or better suited through its architecture to consider depth and different kinds of attributes in a changing environment.
environment. But that group organization poses a lot of challenges to traditional SLAM techniques, such as changing even one thing in that environment can greatly modify what map the robot had made.
And you can imagine this as there's a map and you had localized your position with reference to particular objects in the map, and then you move those objects. So the robots world just shifted all around it.
Literally. And that simple change might be very obvious for humans to detect. But for a robot, which is using those reference points to localize itself in the world and construct the map out of it, that is a big challenge in traditional SLAM approaches.
So, so yeah, many people who have tried to train a robot before it cleans their house by like driving the robot around in different rooms, is very familiar with this particular problem that when you move a chair in between the robot just completely forgets its entire sense of its surroundings.
So, so yeah, that's why I really like this reference.
Yeah. Yes. And that's going to come into play with the internally maintained hierarchical generative model that the robot has on board.
And that may offer it some resilience against these kinds of changes.
So that's why we're going this route at all.
And one adjacent work that's discussed in the paper is RAT SLAM.
So I will play the video, Sid, if you want to maybe describe or contextualize RAT SLAM.
Yeah. So RAT SLAM was this bio-inspired technique, which really solved SLAM in a very simple manner, which is that you, it, it could perform as effectively as other SLAM techniques, which relied on like expensive equipment and replaced it with like a simple camera, which has imperfect information.
So the video goes into it in a lot more detail and we'll cover it in the next slide as well.
But essentially it's a hippocampal model, which means that it, it models like a rat's brain and is able to like map the world and localize the robot that way.
So I think the video is very self-explanatory and the next video will explain it even more about how the map is constructed.
So yeah, let's look at that one.
Okay, go for it.
So what is happening in this second video?
Yeah. So the second video is one instance of RAT SLAM, which is open RAT SLAM.
So this was a code base that was released both for C++ as well as the ROS operating, the robot operating system.
And here you see this one particular robot called the IRAT robot mapping out an Australian environment, which is an urban environment that you see on the top right.
And you see the robot making specific circles around certain loops and making both exploration decisions along the boundaries as well.
So this is very similar to how a rat or a biological organism would explore a particular territory.
So all of this is being done with a single camera.
And that is the main like achievement of this particular piece of work.
So through this paper, you see that the inputs on the top right are mapped into the images that you see on the bottom right.
And those simple images are what's being used to map out the terrains.
So to the human eye, that particular input is extremely blurry and not high fidelity enough to map out a terrain effectively.
But as this paper explores, it can very effectively do that even when we degrade the image quality by a lot.
So that is that is why RAT SLAM became very popular as a cited reference in this paper,
because it's one of those bio inspired techniques which comes very close to active inference techniques that this paper goes into.
So, yeah, that's what this video covers and it explores different kinds of terrains, as you can see.
Awesome.
So the paper in the introduction introduces the relevance of this necessity of the deep navigational functions that humans and other organisms have,
but also that robots we would want to design having.
That's the main theme here.
If we learn from biology and bring action into robotic SLAM, we may be able to have a way to approach these questions.
And then they say, OK, well, how are we going to bring action into SLAM?
Because this is sort of the inactivist insight that having the perfect map in one's head is like the knowing.
But then the knowing how to act is not always trivial, even with the most high resolution map.
Like one could know exactly every molecule of the car and still not know how it would fail in an environmental situation.
And that's what inactivists and inactivism gets at, which is like, what if somebody doesn't have the digital twin model of where things are in their body,
but actually the representation, if there even is one, is more about how the body should move or how one should act.
So that's called the pragmatic turn or the inactivist term.
And in the terms of cognitive science, that's the 4E cognition.
So even though that is about the richness of usually human cognition embedded in culture, extended, et cetera, et cetera.
It's interesting to, again, see that come into play with this discussion of robotics.
Like what if there are cultural practices around movement in a space?
How could that or be integrated into a robotics model?
So there's a lot that goes with this taking serious of action selection as a real primary imperative, not just the hypothetical mapping.
So they say, well, let's use active inference as a process theory of the brain that casts action as perception as two sides of the same coin.
Not sure if it was action and perception, but still maybe it stands both ways.
And a process theory is just like a way that it gets done.
So how do organisms get it done or taking one step removed in the instrumental direction?
How will we model organisms getting it done?
And then people can debate about what organisms actually do.
But this is like us actionably mapping that territory.
In section two, they introduce some neural correlates of navigation, which we're going to discuss in the next slide.
And in section three, they bring the question of navigation in terms of active inference.
And so that's when they go from this hierarchical Bayesian generative model of localization.
And on one hand, connect it to the active inference framework and on the other to this prior work on machine learning in robotics.
And that was also related to their previous paper.
So the authors, of course, have previous work and there's related work too.
Okay.
So the H slash E.
Do you have anything to add there, Sid?
I mean, yeah.
In the introduction, they raised two very important points before they start to go into the actual techniques they have implemented.
So they say that humans easily explore and map their surroundings without much extra thought or considerations.
Like intuitively, we build a logically consistent map without needing accurate distance measurements.
And we find it natural to think about navigation in terms of sequences of moves towards locations.
And when we are considering moving to that new location, humans typically do not consider lower level tasks such as opening doors or lifting feet.
In this paper, they go into like lower level tasks as well, because those kinds of assumptions cannot be made for robots.
And they also mentioned an interesting point, which is that the working of the human mapping and localization hasn't been thoroughly understood.
But the best models we have so far are present for rodent navigation, which is where RAT SLAM and other techniques come from.
So this like predicates the work that goes on into this paper and how they model this as a multi-agent active inference task.
Great.
So the H slash E system is the hippocampal slash entorhinal system.
And homologous brain regions are here shown for the mouse, the rodent, the macaque, which is a type of primate and the human.
And these brains are sort of aligned.
And shown so that one can see how these regions are evolutionarily related to one another.
And then on the bottom are some examples of histology or tissue stainings showing like kind of a cross section and a little bit more detail at the cellular level, because as one might imagine, this has been studied.
And there's many, many copious numbers of like review papers.
And so it's like a whole thing, how people have studied this like many others.
But here is a citation that they provided in the paper, I believe, which was a Buzaki paper about memory navigation and the theta rhythm in the hippocampal entorhinal system.
So suffice to say that the function of this coupling of brain regions has been modeled in some very fascinating and rich ways and trying to understand how the same brain regions in different functional ways can be integrating different aspects of selfness and memory navigation, wayfinding, some of the complexities of how these different functions are related to each other.
Anything to add on that?
Anything to add on that?
And then we'll look at how that has been addressed in the active inference framework.
Yeah.
The only thing I would add is one particular image that I'll paste in this particular slide, which is like, look at the similarity between the tasks done by the hippocampus and the entorhinal system and the similar set of sensors on this particular robot.
So we use extremely similar architectures to center ourselves in the world, which is we use sensors in the form of sensory organs and obviously ears and eyes and all these are sensors.
But all of that is computed in that particular region of the brain, which is considered the robot localization module in this particular robot.
So, yeah, that's what that analogy I find interesting.
Awesome.
And that's with the action states and the sense states, like just like the sensors and the actuators, we could have two of the same kind or 50 of the same kind or 50 different kinds.
And that's like the kind of multi sensor fusion that's also interesting to think about.
And they write in the paper, we will ground the following discussion of the hippocampal entorhinal system in terms of its role in generalized search and navigation.
And the citation here is to this Kaplan and Fristin paper.
We're not going to go over this model right now, but people could pause, look at the graphical model, go to the citation and we'll hear about it more from the authors.
So, there's how did they build on prior work?
I'll add here, unless if you want to ask something, it's totally chill, would be they use a Bayesian graphical framework.
And we're going to see a lot of Bayesian graphical frameworks.
The nodes, the circles represent statistical variables of different kinds.
And then the edges reflect the sparsity of influence of connections amongst those variables.
So, like two variables that influence each other have arrows pointing between each other.
And this is a Bayesian graph way that is sometimes used to represent models graphically.
And that's kind of playing on graphical in two senses.
Like it's visual, it's graphical, like a picture, but also it's a graph like a network.
So, it's something that is a representation of models at the intersection of those two senses of the model.
And we use them a lot in active inference.
And in this paper, they made active inference models for navigation and search,
and they overlaid it on some of the plausible neuroanatomy of the brain
and some of the functions that those regions of the brain have been modeled or seen as performing.
Great.
Okay. Yeah.
The paper also on the biological section explores the grid cells.
And we saw the grid cells also in rat slam.
The grid cells are in the entorhinal cortex.
So, it's in the HE system.
And they represent a largely triangular or hexagonal tiling of space organized according to egocentric reference frames.
Now, it's hexagonal in the flat plane, but what shape is it in higher dimensions?
And they write that the regularity of these repeating grids provides a basis for path integration via estimating distances and location in terms of the direction and frequency with which this metric grid, metric tiling is traversed.
And this was pretty interesting to hear how they framed it.
In physical domains, it has been observed that the spacing of grid representations varies as a function of the space being tiled,
e.g. smaller and more fine-grained if an agent is situated within an enclosure or larger and more coarse-grained if it is situated in an open space.
The granularity of tilings appears to be influenced by brainstem locomotor nuclei, potentially reflecting an inductive bias for greater speed being more likely in larger spaces, as well as by exteroceptive stimulus such as optic flow.
So it makes me think about driving at 70 miles per hour.
And it's like one still has this extended sense of mobility.
And, well, I could make a left turn over that space and time scale.
And that's as natural feeling to somebody who's familiar with driving in a certain context as like I'm running at this speed and I could make a certain turn at a certain speed.
And then the optic flow reminds me of a great experiment with honeybees where they had them forage, but they had to go in and out through this long section where there was an alternating stripe pattern.
And so when the stripes were thick, like let's just say a meter of dark and then a meter of light, then they would forage a certain distance and they would be able to do the waggle dance and communicate it to their nest mates.
But then when that was replaced with a very fast alternating stripes, it increased what's known as optic flow, which is just the simple rate of change, like the frame differencing across the retina.
And the bees were foraging a shorter distance because it was like their estimates of optic flow were higher.
And I think that speaks to also a point that Steven has raised in the chat, which is the information geometry versus information geography.
And that could be connected to a lot of different other areas.
So that's just something to think about with how is the actual space represented?
How is the perceptual space represented?
And the grid cells are something that people have modeled as being at the intersection there from cognitive perspective and from a tissue perspective.
So, yeah, Steven has raised a great point about the geography and I think in humans and organisms like ants and bees, it's more about survival.
And that is why they like attach a different kind of grid sizing for different kinds of terrains.
And yeah, your description of driving in an open wide road is extremely accurate and so is the bees one.
And I think it comes down to minimizing error or being more specific in constrained environments.
So, so if their actions are as wide and as like broad ranging as an open environment that might like be harmful for their objective function, which is not only like reaching from point A to point B in that small environment, but also like survival, like just banging into an obstacle if they are not being very specific.
About their grid size.
So, so I think, yeah, it comes down to optical optic flow as well as I think these survival functions, which are like hidden states in like the models of all these agents.
Awesome.
Awesome.
Awesome.
Um, they move from the biological towards the formal by writing speculatively.
If hippocampal pattern completion is inherently predictive or generative in a Bayesian framework, then this could help to scaffold the development of more sophisticated predictive abilities for the rest of the brain.
So I think this is a very deep area that'll be fun to explore in the conversations, but it's almost like you can bootstrap more complexity off of something that is already providing a more complex and oscillating signal.
So I think the richness of self and the place based based and learnability there is quite interesting to explore.
And they also, uh, note that there's ample evidence that spatial awareness is at the core of the mammal brain with explicit representation for pose heading and location.
So what I wanted to explore here in the discussions was location is the core of the mammal brain or cognitive functions in general, or in insects to or something.
No, it's all faction.
No, it's emotion.
No, it's this.
So where do some of these core functions fit?
And then they close the section by just writing, uh, taking it from the introduction with the robotics to the biological in section two.
And then they say in the remainder of this paper, we will further build on these insights using a process theory of the brain deeply rooted in predictive processing, active inference.
So you'll note that other than our additional context, like we haven't gotten into active in the paper, but that's when they cross the Rubicon.
And from here on out, we're going to be talking about the active inference formalization.
Anything else to add to it?
Yeah.
Yeah.
I mean, I really liked how you framed that particular importance that different kinds of organisms and like robots have to be assigned.
When, when we are dealing with like their objective functions, which is, is location, like the most important state for them or are other senses more important.
And if you're thinking about like self driving cars and, uh, like evidently like Tesla is very particular on not using LIDAR and like laser depth sensing technologies.
It it's trying to just use RGB depth cameras and trying to navigate, um, the world.
And I think the same is true for, um, comma, which is, um, another open source self driving toolkit.
Um, so these kinds of, uh, toolkits that exist for navigation in the physical world, they, uh, just rely on location and, um, like vision as their only source of input and not other senses.
So, so yeah, it's interesting how you can modify the importance of these different attributes to achieve different tasks.
Right.
So into section three navigation as hierarchical active inference.
Okay.
So this is where active inference gets applied in the theory level.
And then it gets applied in another way when it becomes simulated and then in another way, when it becomes enacted, et cetera.
So we cast the slam problem in terms of a hierarchical Bayesian generative model, the agent reasons on two different nested levels.
So there's going to be the use of a higher and lower to describe these two different ones, but one could use different spatial metaphors like inner or outer or however else on a higher level.
But this is going to be consistent with the coloring and which one is placed above or below on a higher level for long-term navigation and on a lower level for short-term perception.
On the higher level, the agent is capable of reasoning in terms of sequences of location.
It wants to visit.
I want to go to the post office and then to the university and then back home without having to worry about the intricacies of how to control its actuators to get there.
Like I'm not overthinking the footsteps and how to cross the street.
On the lower level, the agent can reason and plan in terms of observation sequences without needing to think too far ahead.
Short-term action selection plans based upon ongoing input.
We will distinguish between the higher level and the lower level actuation by calling them moves, M, and actions, A, for the two higher and lower levels.
And the sensor readings like the visual input, but other sensors could be added to at the lower level are called observations and that's modeled with an O.
And that reminded me of the relationship between strategy and tactics in chess.
Whereas in strategy, there are more heuristics like control the center or the knight on the rim is grim because it has reduced mobility.
That doesn't actually suggest how to do it or what kind of a direct or oblique strategy would actually be realized in which way.
It's just sort of like general ideas.
And then there's the tactical and the rollout and all of that in the specifics of the situation, which cannot be really thought too far in advance.
Because even just two or three in advance, the branching is so complex that it's not really useful all the time.
Although some brute force approaches have used that to great success and it may work in certain cases, but it's not a general strategy just to roll out tactics further and further and then hope that strategy just falls out of rollouts of tactics.
So I'm sure you'll have some thought on that, but how do you think that frames this as a multi-scale statistical problem?
And then it's going to be approached from this Bayesian active inference way.
Yeah, I think it perfectly models it.
So you added strategy and tactics.
I would only add objective objectives like as the third element to that.
So objective strategy and tactics are like these different levels of tasks that people want to achieve.
And this is not only true for the tasks that that you refer to like chess or other applications, but also like when we go about in our own life, like our higher level task can not just be going to the post office, but achieving some objective as a result of that, which is I am going to the post office because I might have received an admission letter from from a university.
And that has a higher level task on top of it, which is this has broader implications to my career or life in general.
So one person's or one robot strategy can be another robot's tactics.
It's the way you define moves and actions is totally arbitrary and dependent on like how reliable your sensors are.
So I think the levels are the place where we draw the line between lower, higher or inner and outer levels are dependent on the sensors, which is the ground truth that we can reliably measure in that particular moment.
So the only thing I'll add there is that also, just like you said, where one robot strategy is another's tactics.
This nesting of Bayesian generative models can be three layers.
It can be four layers, et cetera.
So there's arbitrary design of these graphs.
And we've seen like in metacognitive papers, like act in five stream number 25 on metacognition as mental action.
It actually is like action and perception all the way up, all the way down.
So just because I'm a layer isn't modeled, we have an interface for the unknown through the blankets that we do specify.
Okay.
So let's look at it specifically.

On the left is figure one.
Figure one, it is the prototypical generative model of an active inference agent.
As we discussed a little before, the nodes in the graphical model represent random variables where the gray color is indicating the observed variables.
So the observations are observed in gray and then the actions are also observed.
So one could complicate this assumption, but we're assuming that like if the robot is hitting the gas, that it knows that it's actually doing that motion.
So an observation at the current time step O sub T is generated by the hidden state S.
So it has the white node.
So it is a not directly observed, but it's like a parameter in a model, the generative model of the robot, which in turn is generated by the previous hidden state and action at time step T minus one.
So it's like here's S in the past and it's marching forward.
And then it's influenced by its prior states, as well as by how actions influence states, if at all.
And future states and observations depend on future actions, which are determined or not completely determined, but that's but have a statistical relationship with the policy pie.
And policy pie is sequences of actions.
If one has a policy depth of one, then the action at the next time step in the policy are the same inference.
But when we have a horizon of planning that's deeper than one, it means that policies are actually sequences of action.
And that's part of the complexity of cybernetics and so on.
And on the right, I have a little bit cut this generative model into a grid.
So the now time step is the action that we took in the past, the hidden state inference at that time unobserved and the real time observation.
And then the left to right is the past time step, the now time step, the next time step, and then just deep future time steps, whatever the horizon of planning is.
And this is a discrete time model.
There's also continuous time active active inference models, and they can be used together, but it's not in this paper.
And at the top is policy selection.
And there's a lot of cognitive apparatus that might connect to this pie, but that's also not modeled here.
Action selection is these A's, and those are just your actions through time.
I moved E2, E4, and then NF3.
And then the hidden states are whatever the hidden states are that are being tracked as being influenced or related to policy selections via action.
And then hidden states emit observations, and that's what makes it a partially observed Markov process.
And then because it's a policy variable that's being modeled here, it's a partially observed Markov decision process, because it's not just the Markov process inference.
It's also having action as a parameter that's planning as inference.
Anything to add on one?
Yeah, I think adding the grid really helps.
Simplify the different steps that the agent has to take and how it's composable with different policies that might connect from different objectives.
So, yeah, the observed and unobserved are, I think, the more important key pieces here, which again can be, have like, which can have different probabilities.
Because as you go through deeper layers, you can consider the previous layers observation, previous layers unobserved state to be your current layers observed state.
So, it depends on how much probability you assign to the strength of that particular observation.
And yeah.
I just want to add one last thing, which is the observations in the future are unobserved.
So, just to note that there's a difference between the past and the future.
Yeah.
And one could also imagine that maybe there's a forgetting or something like that, but that's a very key difference is that the same type of variable, like actions are unobserved in the future.
We can't say, well, we'll make these three moves.
It's like, but what if another chess piece blocks that specific move?
Well, that would be dumb of them to do, but would it?
So, that's part of the complexity of strategy.
So, figure two is where they go from this single layer model.
This is kind of the kernel of the model, and they're going to introduce a slightly more complicated graphical model.
This is going to specifically cast navigation as a hierarchical generative model for active inference.
And so, the lower level is this, again, more tactical, more local visual perception on the bottom, filled in observations.
That's the real-time camera data coming in is one way to think about it.
But another way to think about it is actually by looking at the arrow direction, it's being generated using some underlying states.
And then the actions at that lower level are also being observed in the past.
And at the lower level, highlighted in blue, the model is entertaining beliefs about hidden states, S, that agents and the agents pose, P.
So, here's the S and the P.
Like each time step, there's a hidden state and the pose.
The hidden states are giving rise to the observations, O.
And then the hidden state and pose are influenced by the previous state.
That's the arrow coming horizontally.
Pose and action, or the higher level model in the case of the initial states.
And so, here is like at each time step.
So, here we're like in this blue block with a T.
Like at the faster model time step.
And then at the slower level, there's an injection from this like slower click that shoots something in.
And then that influences the rest of this blue block.
And then it's carried forward.
And there's another injection, like a slower timescale at that more strategic level.
And at the higher level, highlighted in red, the agent reasons about locations.
The next location is determined by executing the move on M.
So, here's the more slower updating movements, like where one is in that map.
And then this is the more fine-grained action selection.
What do you see in this figure?
Yeah.
So, yeah, it's like it's a continuation of the previous figure.
And like the speed differences are what's interesting here.
Like the higher level being just a two-step process, whereas the lower figure has more involved actions involved.
So, yeah, you see that observations exist in both these layers.
But there's more depth of unobserved states in that particular lower layer.
I hope that now by filling in some formalisms related to this, that we can put a little detail because there's a lot that could be said about this.
And I hope that we've been at least consistent in our descriptions, but we'll look forward to hearing from the authors on it.
So, they write, in active inference, the agent will infer beliefs over these hidden states based upon experience, looking back into the past observations.
Those are the observations from the past that the computer has access to, as well as infer future actions through a process of minimizing variational free energy.
This is where they're going to introduce this free energy minimization as kind of like a model metric that helps do parameter selection, parameter optimization on this type of graph.
So, we have some graphical structure, believe it or not, and it could look different, that does strategy and tactics.
It's like the skeleton.
But then the real challenge is to have the video data come in and to have the movement data actually modeled and to make that happen on limited hardware and so on.
So, what they do is first describe that in terms of equations and then they're going to talk a little bit later about like how the equations get adapted into using neural networks and actual cameras and sensors.
But this is just going to be still at the equation level going from this graphical intuition about how to do strategy and tactics and how to have them modify each other into an analytical way of framing it.
So, P is the joint model of OSA Pi.
That's the observations, the video camera data, the hidden states at this layer, and the actions, and the policy.
Different aspects of the past, present, and future are modeled as sparsely connected.
So, one could believe it or not that those are sparsely connected, so-called, in reality.
But in this model, there's actually quite sparse connectivity amongst variables, even though if it's new to you, it might look like a circuit board or something.
But relationship to the all versus all that it could be connected, this is a quite sparse connectivity.
Like this bottom left one doesn't influence this top right one, for example.
So, factorization is a way that that sparsity of the variables can be converted into a factorized equation.
So, we have this joint distribution, which is like the ultimate panopticon distribution.
But because there's sparsity of connectivity, different parts of the model can be like partitioned out differently.
So, it's like this big joint model that gets separated into separate parts.
And each of those one can interpret as being like the distribution of that.
So, like there's the distribution of policies, over two policies or over continuous policies.
Then there's the distribution of action states that are taken depending on the policy.
So, like given that I intended to move A and then B, did I actually take A?
Then there's the state underlying distribution in green, hidden state.
So, that's not directly observed.
The blue is the distribution of observations conditioned on hidden states.
That's like a Bayesian hidden Markov model.
And then there's this relatively more complex and combinatoric term that is asking,
well, how do states depend on past states and actions?
And then how do actions actually depend on policy decisions?
And how do the observations in the future depend on the hidden states in the future?
So, it's taking this joint model and breaking it down into a few different pieces that, as we'll see, can be simplified.
And that makes this problem tractable in a way that just the all by all non-factorized, non-factorizable model is much more difficult to fit.
Yeah, absolutely.
And yeah, this goes into like the practical implementation of how such a thing can be done.
And the interesting factor in this formula for me is like the combinatoric term, which takes in the previous states and like multiplies it with the current state.
And like this is one of the ways active inference can be modeled.
And I think in previous live streams, like there might be different implementations of the same framework,
where OSA and PI are used in many different like formulae and arrangements.
Great point. Yes.
Though there are some differences in notation across papers, there is hopefully more coherence than not.
So knowing this framework helps one understand active inference domain, different domain models.
Okay.
So how is free energy going to be used to fit this model, both on the sort of perception as inference side?
So that's the part of the model on the bottom.
That's more like a, what is my pose given the visual input and what action should I take in the short term?
And this deeper, more navigational layer in the red, how are those going to be reconciled and parameterized, which includes action selection and policy selection?
How's that going to be parameterized using a single criterion?
So they use the variational free energy and it's calculated up to the current step T.
So variational free energy as contrasted, which we'll get to with expected free energy.
Variational free energy is like the parts that are observable are easier to calculate over.
One can imagine. So that's the variational free energy.
The expected free energy is going to have continuity with the variational free energy, but it's going to introduce this complexity of calculating expected free energies about unobserved observations and actions.
But they're similar, but it goes like from first variational free energy is looking back and that's the more perceptual component.
And then there's a deeper expected component once a time horizon is considered.
So we can go into this more with the authors, but briefly in the first line.
F this variational free energy is being defined as the expectation.
That's the fancy E of the difference between the Q distribution, which is the variational distribution that's under the control of the experimenter of the robot.
And that's like a simplified distribution family.
So just like fitting a linear model can be done, even if the data are super nonlinear and you're totally misled, fitting a linear model can be quite fast or fitting just a parabolic.
model can be quite fast.
So if you constrain what model family you're willing to use for Q, though there are still some quite expressive families that are also tractable, then you can try to minimize the expectation of the difference between the distribution that you're controlling and this distribution that you'd like to know.
That's going to help you go a long way towards doing policy selection.
This expectation can be rewritten using a KL divergence.
And that can also be rephrased as a difference between a KL divergence and another expectation.
So we can go more into this with the authors and I think that will be great to hear their explanation.
But for now, I just want to leave it at that level of detail.
Yeah, I agree.
And I mean, the broader point that I see from this particular framing is like representing it in terms of divergence and evidence.
And this is how not only they use it for their experimental setting, but this is how the actual free energy model will be implemented in a real life situation as well, in which the first term which is in their control may not be like in their control when the robot is in a dynamic environment.
Like that.
Like that.
So in this particular paper, in a warehouse environment, this kind of a framing makes perfect sense.
But when the setting might be different, the framing might also need to reflect that.
Nice.
And also there's that complexity minus accuracy interpretation.
Yeah.
Okay.
So here's where they move from the variational free energy F to the expected free energy G.
So they write crucially in active inference, the agent will not only optimize its generative model by minimizing F for past observations.
In addition, the agent will also select actions that it believes will minimize its future surprise.
However, future observations are not yet available.
The free energy F cannot be computed and the expected free energy G is used instead to compare the effect of various policies or actions in relation to the goal of reaching the preferred state.
So wouldn't it be simple if we could just infer how the map looked in the past and then make decisions based upon how the map looked in the past?
But that opens up to all these basically failures of function in changing environments.
G in formalism three is a sum across over a given time horizon T.
So the expected free energy G of pi and T policy and time for a given certain policy pi and time step T in the future is defined as, and this is going to be another set of formalisms, but we can just pull back and remind ourselves of that sentence from the introduction.
Active inference is a process theory of the brain that casts action as perception as two sides of the same coin.
So variational free energy, which is more perceptual like because it's looking in past observed states, and then G, which is going to introduce the uncertainty of action in an uncertain future.
How are F and G similar or different?
How are they being cast as two sides of the same coin?
How through the present are those two processes being reconciled because time step five from now is going to be like now then.
So how will we have continuity in dealing with certain moments like now, but then there's things that we're uncertain about in the past and the present and the future.
And they're all very quite different kinds and they have different relationships to past actions.
And that's like the blockchain angle.
You can't change the past.
You can change your interpretation of the past, but then there's a different kind of variability or openness in inferences about the future.
So these are great questions to learn about and think about.
How are F and G similar and different?
What is variational free energy?
What is expected free energy?
What is free energy of the expected future?
Which Baron Milledge et al. have introduced.
And what other kinds of representations of this nexus are relevant to think about?
Because these cited papers and shown equations do not exhaust the richness of that setting.
But it's awesome how they pulled back to just this.
It's a function G of what you do.
Pi and what horizon you're considering it over.
Tau.
And then implicitly how you think about all of that and how you think about that.
So they both pulled out to a level that I think will provide a lot more discussion, but also we have to get specific in order for that robot to be in the warehouse.
Yeah.
And the only fascinating observation for me, like obviously there's a lot in this slide because this is the entire model.
This is the crux of the entire calculation where you have variational free energy and the expected free energy.
And you see the similarity between both these formulae where divergence and log evidence is mentioned.
And then complexity and accuracy are terms of that formula.
And eventually it comes down to risk and ambiguity in the expected free energy formula.
When all the probabilities are given a certain policy and on a particular time horizon.
So which is represented by Tau.
So these terms like divergence, complexity, risk are like in one bucket.
And log evidence, accuracy and ambiguity are like in the same similar category in those two formulae.
Awesome.
I think we will, as we expect the unexpected, we'll start to actually accelerate through because the goal of the dot zero is really to set a lot of that context, because that is what brings one to the trailhead, so to speak, for a lot of the details that they're going to present.
And of course, the accuracy of their experiments and the implications and everything like that.
So we're just going to sort of continue on knowing that that getting there is getting quite a far way with this paper.
And then we're going to go slightly faster through many other aspects of the paper just to like give it a first pass.
So here in formalism five, they are casting P of pi, the distribution of policies as a soft max sigma of the free energy on policy and this temperature parameter gamma.
This is casting planning as an inference problem, which allows one to go from like the relative free energies of different policies to a decision on those policies.
And when there's high temperature, it's like the pie chart is made, but one is still just picking from the different policies as if they had relatively more equal pies.
Whereas when the temperature is low, like absolute zero, then one is selecting the best policy, like more than it should be expected in a way.
And so that gamma reflects the confidence that the agent has in current beliefs over policies.
So when there's a lot of confidence, then the most, the best expected policy selected always when there's low confidence, then it's not taken into account as much.
And that's, of course, a fun to think about in the context of like expecting the unexpected.
I think I can. I think I can.
And then it says on the bottom right, no one had the heart to tell him he was going the wrong way.
So one can think they can and be acting consistent with their model and going the wrong way relative to what?
So there's a lot again there that connects like the math to some broader questions that we all have.
What do you think?
Yeah, totally agree. And the meme really brings the point home. So yeah, let's go to the next one.
And in 37 live stream number 37, people can read about this dual interpretation of preferences and expectations and about how they co realize each other.
So section 3.2, they move to the hierarchical generative model for navigation.
And here it's the same higher and lower model with blue at the lower timescale, red at the higher level.
And it's going to be basically as we spent more time on previously, but just applied to this multiscale navigation problem where it was being approached a little bit more abstractly before.
So in Formalism 6, they're going to have their big joint model be all the things that one would want to know in this whole nested model.
That's why previously when we saw the p distribution, there was only four variables because it was considered at like just a more simple kernel layer.
And this is writing it out for the whole nested model where there's actions and moves.
So moves across these two layers being jointly considered.
And then it's going to be like this multiplication between the lower level distribution and the higher level distribution because it can be factorized across these two levels because they're sparsely connected because of how it was designed.
So that simplification takes like sort of an all by all model.
And just at this level that corresponds graphically to the sparse connectivity allows those two to kind of twist a little bit independently from each other, yet also containing a common basis in this joint distribution.
Anything to add?
No, I think this will be clarified further in the next slide, which goes into global policy selection.
All right.
So in the higher level red, the global policy is omitted.
Every move is treated independent of each other.
This hierarchical arrangement allows the system to reason about its environment further ahead, both temporally and spatially.
And so then they take this joint distribution and it gets broken down into these three terms.
From Formalism 7, we can see the generative model decomposes into terms for both the lower level dynamics blue, i.e. how actions influence the next state and pose.
So we broke the blue out from the red, and then there's this other term which we can talk about from the joint distribution.
What do you think?
Yeah.
Yeah, I think this is where it comes to expressing in terms of G, which was the expected free energy.
And we see those terms repeat here.
And I think this is, I think, the most important formula of this paper in which the global policy selection happens.
And at the higher level.
Yeah.
Okay.
So as we saw before with a simpler version, first, there was a decomposition on P.
There's a factorization on a P distribution.
We saw this with like with a simpler P here that then got turned into an F and a G.
Here, we have a more full-featured P.
It is also going to be turned into an F, which is that variational free energy, and then a G.
So this is F of the hierarchical model.
They write, now that we fully specified our generative model, that was P, the factorized joint distribution.
We again turn the variational F and then later the expected G free energy that will be minimized in active inference.
So it's a variational distribution Q that they're fitting and they take the same approach as they took earlier with the single layer model.
And they reach this hierarchical free energy that can be rewritten by the bottom row as the decomposition of the free energy of the lower model and of the higher model.
So I think it'll be great to hear the authors, like how did they reach this and what do they think it means and so on.
But I think the awesome question to think about here is how do we think about free energy minimization in multi-agent and multi-scale systems?
How do free energy decompositions work and what if nine do really well, then one doesn't?
How does that group outcome get traded off against, well, everybody's doing a little bit worse, but isn't that better than one person doing a lot worse?
Well, it depends by how much you mean by a lot and a little and the situation and so on.
So how does all of that going to be amenable to these kinds of seemingly cut and dry decompositions?
Yeah, that is an excellent question.
And another question that I would add to this is how many terms can you decompose this into as you think about more and more models?
So here we have a lower level and a higher level, but can there be multiple levels for different kinds of scenarios?
Awesome. Okay. So they are now going to pick up on that bottom line.
There's a low and a high decomposition of the hierarchical variational free energy.
And they write, this falls apart into a term for the lower level and the higher level of the hierarchy, which we can further unpack.
For the higher level we get, and then they provide expansion of that F high and F low.
And these have the same complexity and accuracy interpretation as we saw with the previous F,
except that this complexity minus accuracy can be understood as being about only the higher level.
And this complexity minus accuracy on lower level can be interpreted as being about only the lower level.
So it's like been a separation of consideration between these levels.
But again, they're coming from a common joint distribution.
So that is just like a example of taking the analogous logic and path that was followed on the single level model,
then using this composable framework, making the nest degenerative model,
and then being able to apply the same kinds of techniques to reach the same kinds of conclusions.
But now in this different context.
Anything to add?
Yeah, totally agree.
Yeah.
Splitting it into like these very specific terms and differentiating the forest from the trees,
where high is the forest and the lower level are the trees, is very, very helpful.
And it also shows how they are related and not related.
Awesome.
So now they're going to make that F to G move.
When considering future time steps tau, the variational free energy becomes an expected free energy,
which again unfolds to a term for each level in the hierarchy.
So they're going to do that F high and F low type decomposition,
but it's going to be about G, the expected free energy.
And so here's the low on the right and the high on the left.
And so here there's that same risk plus ambiguity,
but now it's being applied to the decomposition between the high and the low.
And so similarly to equation four, this unpacks in a risk term to reach a prior goal location and an ambiguity term.
Intuitively, this means the agent selects a route to its goal location with the lowest ambiguity.
Hence, if the agent operates in a completely static environment without uncertainty,
this basically becomes equivalent to shortest path planning.
So that's was really interesting to hear about again, in the context of what you described,
like well mapped, well connected, real time updating, highly controlled settings.
The future is more like F than it is like G, because it's like, you can just trust in the future that you'll get a snapshot update
and you'll be able to make the perfect move because you'll be able to do shortest path planning and traditional optimization techniques,
because you'll have no ambiguity about the future basically in the short term.
And then that gets more complex when there actually is different kinds and different patterns of ambiguity in the future.
So it's just like such a cool way to hear about it now.
Yeah. Couldn't have said it better.
Similar thoughts on this particular framing.
Okay. So that was section three.
In section four there.
Now we still haven't seen active applied yet.
We haven't seen any action perception loops.
It's been like very analytical to this point.
So now in section four, they're going to actually bring that generative model into active inference.
So they write, now we've established our generative model in the variational free energy optimization objectives.
We present how to instantiate such a model in silico for navigation on a real robot with camera input.
So it's kind of interesting because in silico often means like we only simulated it, but here it means we implemented it on a silicon processor.
Yeah. In a real embedded situation.
And so the observations are the raw pixels from the camera sensor and the actions consist of the commands specifying the linear and angular velocity.
So that is just taking that generative model structure that we described kind of abstractly.
Like the, we just talked about the observed observations, but is that a one pixel camera?
Is it a 4k video?
Is it lidar?
Like this is where they are going to connect it to the specifics of what they actually do in the robot?
Yeah.

The only thing I'll add is again, this picture because it's such a helpful picture in framing the pixels and the sensors that are being captured in their case as well.
case as well. So they are taking just this camera inputs, which is R, G, and B values for this
particular paper, as well as like the IMU units and the odometry units, which is velocity.
Awesome. So in section 4.1, they highlight the visual perceptive aspects of their model. We're
not going to describe it here. We'll hear about it soon. But 4.1 focuses on that visual perceptive
aspect. 4.2, which we're also not going to focus on here, takes it a little bit out from the visual
perception. You know, how is the tree recognized given the retina? And this is like the path
integration around those trees. So this is a path integration approach. And then they also bring up
some points about how this has some similarities on the biological side. And also they introduce
this topological map component of the higher-level generative model, the red model. Do you have
anything to add, especially maybe about that topological basis of the higher model?
Yeah. So I mean, this is where it's attaching it to like the physical world. This is where
the lower levels and higher levels get connected through these particular formulations. So yeah,
this is a question I will have for the authors as well. Like how is this CAN-CN network represented?
And why did they choose this particular framing of connecting the two levels?
Yeah, they write, the posterior distribution, that's the one that we control, is represented
by a continuous attractor network, a CAN, a 3D cube that wraps around the edges with these
different dimensions. So that might enforce some type of closure on the network, which we also saw
happening with the RAT SLAM. But that'll be a good thing to ask. Okay. So then in Section 4.3,
they highlight the localization and mapping. These are being simultaneously inferred, so it's a SLAM.
And this is the localization and mapping features, which are another level kind of above or different
than just path integration. And they relate that to the higher-level model. So they provide some other
formalisms. And maybe this gets at what we were discussing.
Due to odometry integration drift. So inaccuracy about how many footsteps you took. Like that's the
kind of the reason why people apparently walk in a circle when they're lost in a feature list landscape,
because they have like a little bit of a different step length. And so they have drift in their heading.
Matching experiences will not have exactly the same associated pose. These displacement errors are
distributed throughout the graph by use of graph relaxation, shifting the stored pose according to
equation 16. This enforces the map to be topologically consistent, even after loop closures,
which is often challenging in metric SLAM systems. So that definitely gets at Stevens' information
geography or information geometry versus information topology. Because if we enforce a rigid geometry,
then tiny differences might drive us wild. But if we enforce topological closure, then even if a road
like became 30% longer, we'd still be able to navigate from city one to city two, and it wouldn't be so
bothersome.
Yeah. Yeah. And including drift is like one of the fundamental things all robotics experiments have to
do because everything that we formulate via math never seems to work out well in actual physical sensors
and actuators. There's always that drift term that needs to be added. And I like how they have handled
like the drift here. Awesome. In section 4.4, they discuss and highlight the navigation features. And
here we'll talk more. I just want to raise these questions because they make up like three of the
perspectives that are really getting integrated and recombined here. And you spoke to it right there.
How do mathematical entities navigate like Bayesian graph models and generative models? How do biological
entities navigate and how do robotic entities navigate? And what are their similarities and differences and
different opportunities and challenges? And how will we generalize and make the right kinds of
connections across different systems within these domains and across and among these domains? So that's
an awesome complexity question. I hope a lot of people can enter into these questions and like provide
their thought and be involved in this. Yeah. I mean, this could be a whole section on navigating navigation,
which is like an interesting topic for complexity. Awesome. Okay. Section 5. And this will be,
I think, just fascinating to hear their hands-on experience about these experiments, which we're not
going to go into too much detail in, but in section 5, they describe their setup and implementation. So this is a
tele-operation of a mobile robot in a lab with a warehouse style. And they describe some details
about like what kind of robot they used, what kind of camera was used and how many data points existed.
And then they talk a little bit about their implementation of how that generative model
became basically implemented using machine learning as a LSTM network.
Yeah. Yeah. This is where this is, this is the most fun part of the paper for many robotics,
like researchers, because this is like the standard robotic toolkit that's used in almost all robotics
labs around the world. Turtle bot has become like this raspberry pie of robots in which every lab has one,
and anyone can replicate this kind of an experiment easily. And it's interesting that they have access
to like all these sensors that they talk about, such as LIDAR and millimeter wave radar, but they only use
like the minimal set of sensors they need, which is the RGB data. And that is what they use to collect
data points. And they are sampling it at like an interval, which is very close to human perception,
like 100 milliseconds, it gets close to like biological level perception, like the frame rate that we have for our sensory organs.
So that is very interesting. And the implementation is even more interesting where they,
which we have to definitely ask the authors about how they use this setup.
So thank you. Great. In figure three, they show on the right side, a picture of the bot turtle bot. So there it is.
And then on the left side, we see some still images of the lab warehouse seen at different points. So I hear
point one on the map is corresponding to what was seen as like approaching this wall and kind of doing a U-turn.
And so this is the path that was taken as it was kind of circulating these warehouse shelves, basically.
Yeah. And also, I really appreciate how you like you described the commonality of these techniques,
because those I just didn't know that this was such a common hardware and it'd be awesome to see like what it will
look like when people start to deploy it in different settings. Yeah. And it's important because they use ROS.
First of all, TurtleBot uses the robot operating system. And like, if this is the first time people are looking at a TurtleBot,
and by just looking at the image, you can tell that it's a Roomba with like a shelf on top of it with many different sensors.
So honestly, that's all there is. So the movement is done by like the vacuum cleaner on the bottom,
the cleaning robot module on the bottom of the robot, and then the rest of the rack. The rack is full
of sensors where you see the cameras attached. So earlier, there used to be connect cameras attached,
and you can attach any sorts of additional units on top of it. And then there's a processing unit
there which like takes in all those inputs and does all the calculations on board. So yeah,
reproducibility in robotics research is extremely rare. And using a technique like this definitely
helps for other labs to reproduce these kinds of results. Yeah, thanks for that. And I'd be really
curious to learn more also about like the edge computing implications. Like is that a mini PC? What
exactly is needed here? What if the model were 100 times simpler? What if it were
100 times more complex? So in figure five, section five, three, they discussed the results, and they
asked three research questions, and those are addressed in the following section. So they ask,
does that lower level model learn accurate representations for inference and prediction
by minimizing free energy? So does the lower level work? Two, can these representations be used in the
hierarchical model for generating topological maps of the environment? Because although we kind of didn't
discuss it in detail, that is that topological closure that's impressed upon at the higher level,
but not at the lower level. So can the lower level work? And then can it be used as a useful interface
with this totally different in type topologically closed higher level model? And then the holistic
question is, does the system infer sensible moves and actions by minimizing expected free energy to
engage in navigation? Like, okay, given that the two components are interfacing, does the whole thing
do free energy minimization in a way that ends up doing so-called sensible moves? That is maybe what
a person would do if they said, just patrol that warehouse, just walk around without any too specific
of a goal, but just make sure that you walk everywhere pretty much. That's pretty sensible.
They didn't spend any time over here. They didn't just go up and down one shelf. So that's sensible,
even though there's not quite a heuristic for that. But I think that's really a fascinating question.
What is sensible behavior?
Yeah. And I think they go into how they quantify sensible behavior by comparing it with other approaches
in the results. So it will be interesting to ask the authors about that.
Yeah. Okay. Table one just goes into some details about their neural network parameterization.
We'll hear about it from the authors. So how did neural networks come into play? What was the process
of fitting that? Okay. Figure four. All right. Figure four is the sequences of the ground truth
observations. First row. So that's the video data coming in on the top. That's like, just looks like
regular video data. Reconstructed observations. Second row. That's the generative model of visual
input. And that's kind of like thinking about this in terms of like a core screening, but this brings the
visual input into the robot's terms corresponding to latent space samples. Third row. So this is like
potentially an internal representation, like a layer of a neural network. And so it's just showing that
these perhaps very similar or different scenes can be differentiated via their position in like a higher
dimensional latent space, or it's lower dimensional in the video, but it's higher dimensional than just
like the X and the Y. The robot is turning towards the left in the sequence, as can be seen from both the
sequence of observation, as well as the shift towards higher theta values in the pose cube.
And that's the pose cube activation on the bottom row. So this is what it looks like at that lower model
to go from video data to hidden state estimation, the kind of core screening generative model of the video
to this latent state internal representation to the pose estimation that's going to come into play
at the higher level of the model. They're kind of overlaying time steps as columns during this
execution of a turn and showing how different layers of that lower model are updating.
Yeah. And I think this is a time series like you described. Left to right indicates like 10 seconds,
for example, 10 seconds of a turn of a robot. And that was an interesting comment on the higher level
dimension for a robot is lower level fidelity for us with those pixels. So, so yeah, the way we
represent things and the way it's represented in a robot can have very different terminologies.
Yeah. And higher, lower, inner, outer, more or less, it's always in relationship. And so those can
sometimes get swept under the rug. It's a high dimensional representation that we did of this,
you know, what's, what do you, what do you have to ask in 42.0? How high?
Pixels. It's just a few pixels.
In figure five, they show the generated experience map left and a comparison map extracted from
localization with R tab map. So I show the citation here, but I would love to hear your interpretation
of what do they mean by the experience map is topological while the R tab map is metric. What
are being shown differently here, here?
Yeah. So, so yeah, they are comparing the figure that they obtained on the left with the data
obtained from a similar technique. So the way these robotics experiments work is they use different
localization techniques and they are using R tab map, which is another technique on the right. And yeah,
the second point is very interesting. And I think that is Stephen's question as well, which is how is the
information geography represented? So the experience map, which is on the left, it briefly describes how
how, like the environment is topologically, yeah, closed. And the R tab map is accurate to like physical
world metric units, which is measurements. So, so topology just means like how everything is oriented.
It doesn't need to be physically precise as a real world. It's like wisdom versus
knowledge. So topology is more, more of an idea that, that if you follow this kind of a map, you will
find your way and you won't get lost. Whereas metric is like precise mapping of the physical environment and
mapping it to scale, like one is to 20 or one is to 100 or whatever that scale may be.
I really liked that knowledge and wisdom. And then here's why there's always the minimum of two and why we
respect both because the topological maps may be totally non-comparable in their geometry or two
different entities mapping the same space. And so if we are both trying to get the geometry of the
geography, that's where it's possible to have the most objective agreements on the knowledge side,
allegorically here. And then the topological side can be so much simpler and so much more personalized
and local and can actually help in those wayfinding and the changing situations. And maybe there's
analogy or there's resonance or there's small isomorphisms with different wisdoms, but one has gone down that
path and has basically given up making the image on the right that other people will just see and
recognize as well. Yeah, that totally lines up with what I see. So that's quite a nice point.
Yeah. Okay. Figure six is some more outputs of the model. So they, right. Imaginary policies,
uh, imaginary policies. Oh, so there's several images of different things happening. There's the
current state, which is the video input at that time step. And then there's imagined short-term goals.
I want it to look like this. I want the frame differencing at that time step to be super small.
I want to be really unsurprised about looking like this at that short time step in this turn. You can kind of
see that, um, piece on the left that's getting brought more into view as I turn my head left.
I don't want to be surprised. I want it to feel normal. And then in the long-term goal, there's a
lot more like blurriness because it's not super important whether the handle is here or here because
it's just, uh, an uncertain future. And so these are imagined policies that can be considered at past,
present and future time steps. And that's kind of what the partial observability of the hidden Markov
model structure or motif brings into this picture. This is why it's good to have a generative model
rather than just a recognition or an input, a signal processing model. That's like where the
whole generative Bayesian concept and predictive processing from the biological side come into play.
And also in the future, it trails off. These are the same time series and further and further in the
future, it gets blurry and blurrier until it's like, I just want to be in a horizontal plane
in the future, basically. Standing. Yeah. Yeah. Yeah. Figure D is like, um, very interesting in this
particular picture where they have three different policies and you see very different results, um,
as a result of those policies. So this is, uh, like robotics 101 behavior where you program the robot to
always go left, always go right, or always go straight. And you, uh, start with these particular
policies and then, um, understand that these simple changes in behavior have like such vast differences
in the results. So yeah, the sentence you just highlighted is. Yeah. So, so here, the three
policies are basically, um, uh, the, the two different turns are going straight. And so they
say when calculating G low and evaluating the distribution on policies, this results in a
probability close to one to take the policy, go left. Like look at how on the bottom row,
that's the go left policy. It stays sharp in the future, but then this, the policies that diverge
increasingly from the goals at different timescales with respect to those goals, it becomes really
unclear. So it's like, I want a hundred dollars. So I'm saving $1 per day. Then at day 71, I expect
$71. Wow. It's exactly $71. That's like this bottom time one. And this is like, I'm losing money
every day. I'm getting less and less clear on how it's going to end up at a hundred at this future
timestep. So maybe that's not a good policy, not because my expected value is dropping, but because
it's just, it's unclear how I'm going to get to a hundred. And that's something that can be neutrally
said without even taking a judgment on the amount at any given timestep.
Yeah. Yeah. I think that analogy really drives the point home that you need to choose your policies
according to the goals. And I think all those goals were part of their formulation of the expected
free energy. So I think it's important to ask this to the authors, like how were these goals as well as
policies chosen? And can this be generalized for different kinds of environments?
Awesome. So figure seven, they write different goals for the long-term path of figure five.
So just here's the figure five again, with the topological closure of the higher model,
the lower level dynamics model will take the corresponding states as preferred state goals
sequentially. So this is where we see the connections between the models becoming enacted.
So let's just say that one is coming around this edge and there's two options. They can continue
straight or they can go right, or they can go in reverse, but we're considering forward motion only.
So there's two alternate policy. It's not the infinite space decision-making that humans are sometimes
confronted with, but here it's a robotics motion decision about continuing straight, ostensibly to
explore this final right-most shelf sequence or taking the right turn now. So go straight or turn
right. Now, what would sensible behavior be? If one had recently or repeatedly visited the closer shelf,
then to be more exploratory, it would make sense to like go straight so that this last shelf could be
explored. So that's the kind of decision that we would want that robot to be able to incorporate when
it's able to be making that decision. And so that could be thought of as having a long-term goal to
be expecting oneself to be on the far right shelf here, the bottom one. And then in the moment,
which one of these actions turn right or go straight is going to be preferred with respect to how one
acts now. And so then that's what it means to say the lower level dynamics model will take the
corresponding states from the higher long-term path as the preferred state goals. So then one could be
like, well, I'd prefer to see myself just right here. Already one has chosen a branch, but that is
helping you reduce your uncertainty about being found here later. So that, although I really look forward to
also hearing everyone else is like unpacking of like, what is the robot doing or thinking in that pivot
moment? Um, that's like kind of how I read the way that the long-term planning goals become imposed upon
the lower level action selections. Yeah. Okay. Um, what did you see or want to talk about with the
contrast with other SLAM approaches? Let me see. So yeah, this paragraph, um, like describes different
SLAM approaches and, um, you see the same, um, like group of authors mentioned from probabilistic robotics
where Sebastian Trun and the coauthors are mentioned. And those were engineered approaches, which also used
different kinds of Bayesian, um, like, um, like statistics. And then there were more bio-inspired
approaches such as the RAT SLAM group, which is, uh, the 2013, um, paper. And then, um, yeah, they rely on
PoseCAN and this experience map, which they compare it with. And recently, like deep learning has obviously
been used on visual SLAM, like you see in this, uh, like the bottom, um, like bottom of this paragraph
and yeah. Um, the underlined, um, section is important. Do you want to cover that? The active
inference allow for a holistic treatment? I think that's where they bring it home, which is they
say, well, yes, people have used this recognition variational autoencoder model. And yes, there's been
this topological approach to RAT SLAM navigation closer and et cetera, but then those are often
again, composed in, in an ad hoc way. Uh, and so active inference is providing a possible way to,
uh, approach it in a more principled and more integrative first principles way.
Okay. Um, conclusion let's, uh, hear it from the authors. People can draw
their own conclusions, but I'll just highlight the last sentence that we think this research
direction might offer new insights, both on how navigation works in the mammal brain,
as well as how to scale active inference to real world applications. So it's like,
those were the three vectors we brought in with a biological mathematical and the robotics.
And then from that nexus, it's kind of like, it feeds back out because now from the brain,
they might be learning about the math and the robotics. And then the others, uh,
in a similar fashion. Yeah. Yeah. And as the authors conclude the paper, they also bring up some open
questions such as, can these techniques we use for lifelong learning, which is a relatively new field
of machine learning in which states change all the time and you do not need to retrain your model, but
you, you do not, you need, just need to, um, like retrain specific parts of your model to continuously
learn throughout the lifetime of that application. So, um, so they, uh, suggest something like a sleep
cycle, but that means that whenever the robot is charging, that is when it can update its model of the
entire environment and share that and, um, do that, um, active inference approach to achieve lifelong learning.
So I'll be very interested in knowing this from the authors, like what are the weaknesses in this
approach and how can this be solved to scale for real world applications? Awesome. And how about just
describe what this last video is showing? Yeah. So this video is just for people who are coming from
the active inference lab, but want to see like a robot actually move. We have been talking about robots
moving. So if we play the video, it's just an introduction to turtle bot and how people use it in
an experimental setting. So, so yeah, the first few seconds of the video will describe all there is.
Awesome. Um, well, we leave a blank slide for the discussion sections. This was, um, an awesome and
memorable discussion, and it's just the opening of the 42 when we'll continue on in a participatory group
setting in the coming two weeks and hopefully have, uh, any of the authors join or anyone else who would
like to join in, uh, I'll let you give a penultimate thought, but just really appreciate the care that
you brought to these slides into the stream. Yeah. And thanks to Stephen and everyone else who asked
questions. Yeah. Okay. So if you have, do you have anything else you want to add? Otherwise we can just,
uh, thank the listeners and head out. Yeah. I mean, this was my first active inference,
appearance, uh, in, uh, in the sequence of, uh, hopefully a lot of appearances in the future. And
this clarified a lot of concepts for me as well, and connected it to one of the fields that I was very
intimately connected with, uh, almost a decade back. So, so yeah, happy to see connections being
reforged and yeah. Looking forward to meet with the authors. Okay. Thanks a lot, Sid. Thanks everybody.
And, uh, see you next week. Bye. Thank you.
Bye.
