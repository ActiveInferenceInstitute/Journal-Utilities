---
title: "Active InferAnt Stream 001.1 ~ FieldSHIFT-2: Fully Synthetic Dissertations for All-by-All Domains"
category: "ActiveInferAntStream"
series: "ActiveInferAntStream_001"
episode: "1"
speakers:
  - "FieldSHIFT-2: Fully Synthetic Dissertations for All-by-All Domains"
duration: "1:48:38"
url: "https://www.youtube.com/watch?v=6E4CpJvzddg"
views: 789
exported_at: "2026-02-18T22:37:37.699737+00:00"
format: markdown
---

# Active InferAnt Stream 001.1 ~ FieldSHIFT-2: Fully Synthetic Dissertations for All-by-All Domains

All right. Hello and welcome. It is August 5th, 2024. This is Active InfraAnt Stream,
001.1, new stream series just dropped. And this is where we're headed today. We're going to be
doing linguistic analysis on fully synthetic all-by-all dissertations. We're going to go
into a lot more detail on what that means, but just quickly at the top level, each of these points
in a principal component semantic space is a written dissertation shifting from one field to
another, following on on the lab of Mike Levin et al., who worked on the field shift one. This is
field shift two. It does quite a few different things. And for example, this data point is the
actual term frequency usage distribution on synthetic negotiation to synthetic quantum
computation. I'll talk more about what the synthetic part means. This is like a PhD dissertation that's
going from negotiation to quantum computation. And here we have similarity clustering across
in all-by-all of different domains. So we're going to be going to a lot of different places and ways.
Let's just start with this text file off the bat. Super excited for this. It's been really rapidly
developing. I'm using cursor 0.39 came out just a few days ago, even better than the prior ones.
So let's start this off, right? I'm going to push 3000 files to a major Git release. This is going to
take a few minutes. Once it pushes, push that now. All right. Once that pushes, then I'm going to
come over to Zenodo and make a new release on GitHub. So first just wanted, while that's loading,
you can see it on the top of the page. Zenodo makes it super easy to connect GitHub repos
via Zenodo who offers DOIs, digital object identifiers. So active inference is right here.
Once the GitHub push is completed, then we'll make a release of the repo.
And then that will get a new DOI and archive it on Zenodo. So that's really awesome. So just a few
different tools using Zenodo for publishing for DOI, GitHub for a code. And let's reload it, see if we're in.
One minute ago, active inference stream 001. So now let's make a new release.
This is going to be number 01.1. Needs a tag. 1.01. During the stream.
Publish it. 1.1 is published. Reload on Zenodo.
And it'll probably take a few minutes, but that's pretty cool because then it'll also have
the DOI coming from Zenodo and the archiving. So maybe we'll check back there later.
Okay. Let us go to...
These are... It's in the background. It's translating the dissertations into Sanskrit and Arabic in the
background. So hence these new files being added, but we're going to get all there.
Okay. Start with the GitHub push. Done. Reload and confirm. Update. Make the GitHub update.
We did that. And we're using cursor 0.39. Came out a few days ago.
Okay. For backup. There's a page
in the active block for its coda.
So it summarizes a little bit about field shift. So I'm doing this. That's right now. August 5th,
16 UTC. The code's in active inference. Just uploaded now.
What field shift 2 is doing right now is generating thousands of these all-by-all domain A to domain B.
And I borrow this term and develop in the same tradition from Mike Levin et al.'s work.
So here's the paper here. Machine learning for hypothesis generation in biology and medicine,
exploring the latent space of neuroscience and developmental bioelectricity.
O'Brien et al. Levin.
So they briefly...
Let's see if the figures look bigger.
They briefly describe how AI is playing an important and pervasive role in the scientific process.
They talk about analogies and isomorphisms between, for example, the neural synapse and the cellular junction,
bioelectrically and chemically considered.
They talk about some even broader, quote, functional invariance between neuroscience and developmental biology.
So that sounds kind of cool, promising. Of course, metaphor.
Here's the BART-based domain translator.
This relates to taking material from one content and then putting it into an encoder. It gets decoded.
And here they provide the outline of a GPT-4-based domain translator.
So neuroscience concepts and developmental biology concepts are juxtaposed.
I'll show what their data looked like in a second.
And they used that.
They also had annotators.
They had several person annotators and they tested how well were the ideas that it came up with.
They just showed that a few of the kinds of cases that they tested
and then did some preliminary go type analyses looking at,
like, were these hypotheses better than a uniform random distribution?
So that was really inspiring.
And I had shared previously with Mike Levin,
the sort of MikeLevin.py from elsewhere in the research methods folder.
So I thought that was pretty cool.
Let's look at field shift one and then we're going to go through field shift two.
So what field shift one is, first, I brought the whole paper's plain text in
because then I can use this and say, what would field shift one think about this?
And then here's what their data sets look like.
So they had one expression.
So many memories come to mind.
So many pattern memories come to the body.
So they have a kind of expression from the neuroscience domain
and then an expression that's analogous, deemed to be analogous from the developmental biology frame.
So I started playing with that and playing with that and playing with that.
So here's where we got to.
I'll start with what are called domains.
So this is in field shift two now.
Domains, I have here.
ATM transactions, biology, blockchain, Buckminster Fuller, chemistry, cognitive security,
cooking, entomology, fabric, free energy principle, active inference,
healthcare, hospitality, hymenoptera.
That's the ants, the bees and the wasps, the sawflies.
Logistics, mitochondrial biology, negotiation, neuroscience, prediction matter expertise,
quantum computation, spatial web, traditional wisdom, William Blake.
And we can make another synthetic domain.
So if anybody is in the chat and they want to request a domain,
I will see if we can make it on the fly.
I'll show what it looks like.
But while somebody is posting a fun domain to add, it can be as narrow.
It could be entering the third digit of the pin in the ATM transaction.
Or it could be like that corner, but not this corner.
Because a domain, it could be an ism.
It could be a kind of a person.
It could be an entity.
So it significantly generalizes on what I had above with the entities.
But here's what the structure of these files are.
So the first line with a hashtag is saying what the domain is, just its name.
Then there are several dozens to several hundred examples and questions.
Also, depending on the situation and how it was generated and all this other things here,
like a fact.
So chemistry may have definitions, examples.
All right.
Vladimir wrote intelligent soft matter.
Excellent.
I will add this.
So new file.
Synthetic intelligent soft matter dot MD.
Okay.
Hashtag intelligent soft matter.
Control.
Okay.
So.
Control A.
Control K.
Inline editing.
Using Claude 3.5 Sonnet.
We're in the domain folder.
New file that was just created.
In the syntactic style.
Of.
At.
Cooking.
Sorry.
Synthetic.
These are.
I just want to pick a few of the synthetics.
At markdown.
At markdown.
Transaction.
At.
Heminoptera.
Synthetic chemistry.
Let's just see if one is enough.
Please write many relevant.
Professional.
Concise.
Statements.
And questions.
Related to.
Intelligence.
Soft matter.
Soft matter.
So that's why I described these knowledge bases as synthetic.
Because they're being entirely synthesized in the file.
I'm not bringing in any transcripts or any factual databases.
I'm just saying.
Generate likely expressions.
Giving.
The topic.
So it'll take a while.
I've.
I've.
Way.
Way.
Rate limited.
The.
Cursor.
So here we go.

Definitions.
Example.
Definition.
Example.
Fact.
Intelligent soft matter often incorporates nanomaterials to enhance functionality and responsiveness.
Okay.
So looks good.
Control.
A.
Control.
K.
Please.
So now it knows exactly the format too.
Please add many relevant examples and questions.
Demands.
But the semantics of what are broadly there are already defined.
So let's just let it do one more pass.
Then this is perfect because it'll.
It'll expand our domains from 22.
To 23.
Okay.
I'll add one more.
For.
Michael Lennon.
Then with the 24.
We'll push the 24 through the whole.
Outline.
Here's.
Here's the visualization.
Here's what's going to happen.
First.
We're going to generate the input domains.
That's where we're going to have 24 of them in this case.
Then we're going to generate pro shifted domains.
These are just going to be like concatenated text files that will get sent off to the LLM.
It doesn't have to be its own script or anything like that.
But what the shift domains dot PY does is it's going to send this concatenated list of all by all domain shifts.
So basically prompt.
Then domain A.
Then domain B.
Shift domains is going to send that to open API.
Open AI.
API.
Get back a shifted domain.
The shifted domain is going to get prompted again to the LLM.
And it will say make a dissertation outline with this structure.
So then there's a dissertation outline for each all by all.
Then from the outline generate it.
Then this is another LLM step.
Then from the draft improve it.
LOL.
Draft.
Then translate it into a variety of languages.
And just on the language side.
This is what that will look like.
Translated dissertations.
Here's the folders.
Spanish.
Sanskrit.
Russian.
Punjabi.
Portuguese.
Navajo.
It's really interesting what it says for different languages.
What it will and won't do.
And then at any of these steps.
We're basically just talking about a folder of markdown files.
So we can use a variety of language meta-analytic methods.
And use those kinds of landscapes for our own.
Okay.
Back to soft matter.
Okay.
I just wrote please add many relevant examples and questions.
So these can be.
You could add in more factual information or specific information.
So now we're up to.
And we go.
Field shift two.
Just refresh the folder.
Inputs and outputs.
Domain.
Okay.
Okay.
Let's add the.
The one that.
Michael Lennon said.
Just.
Do this.
And then we'll push.
Both of those.
On through the all by all.
Non-science ways of knowing.
Okay.


In the.
In the.
In the syntactic style of.
At.
Intelligent soft matter.
The one we just generated.
Same request.
Same request.
Here's intelligent soft matter.
In the file structure.
Yeah.
And this is like.
Gets fascinating.
With.
Well.
What does the LLM.
Slash pipeline.
Think are likely.
Salient.
Acceptable.
Safe.
Responses.
To.
Asking about.
This or that.
Thank you for the.
Gift.
Upcycle club.
Who wrote.
Stigma G.
Ant emoji.
All right.
Yeah.
72.
Statements.
Interesting.
Citizen science initiatives.
We'll just do one more expansion.
Add many more.
Relevant.
Examples.
And questions.
All right.
Then we're going to.
With those 24 domains.
Then we're going to push through the all by all.
But previously we had 22 domains.
And so.
That generated.
444.
484.
Pro shifted domains.
So let's look at these files.
This is just a concatenated file.
So here's the prompt.
It's going to say.
Whoa.
Whoa.
The prompt is.
You're an expert.
Follow these steps.
For the domain transposition.
There's 12 steps.
And here's the output.
Okay.
Here's domain.
Go.
Here's the synthetic statements.
Atm transactions.
All of them.
Then.
At a roughly equal length.
Here now.
Where domain B is chemistry.
So then this is going to be.
Atm.
Isomorphies.
Transposed onto.
Chemistry.
So it's like.
The way that people.
Might think about things.
And the reverse.
So.
Gripper and gripped.
Push and pull.
Swapping.
Perspective swapping.
There and back.
Back and out.
All right.
Now we have 24.
Okay.
So kind of.
Come along.
In the cursor.
And in the file structure.
So first thing.
In the terminal.
Just clear.
LS.
In the.
Directory.
With these scripts.
So.
We go to the visualization.
First.
We had the input domains.
Generate.
Pro shift.
Domains.
Okay.
Total domains processed.
24.
To the output directory.
Okay.
Now we're at.
576.
Pro shifted domains.
Okay.
Now.
We're ready to do.
The domain shift.
Shift.
Underscore domains.
Okay.
It skips.
Files.
That edit.
Had already.
Output.
So.
While it's.
Doing that first domain shift.
Awesome.
While it's doing that.
First domain shift.
And it'll report the timing.
Which one it did.
Dean asked.
In the chat.
Can you explain.
Field shift.
In a scale friendly.
As compared to a scale free.
Perspective.
Let's revisit that.
But it's a great question.
It makes me think of.
Tilt shift.
Photography.
Depth of field.
So here's what happened.
The ones that we already had.
The 484.
Of the 576.
Those were skipped.
So then.
We got to.
The first new.
Field shift.
And we'll look at the script.
Also.
But it's nothing more than the.
Text file.
Plus.
Open AI.
Synthetic neuroscience.
So neuroscience.
Neuroscience concepts.
Transposed onto.
Intelligent soft matter.
Next new one was.
So that took.
22 seconds.
They're taking up.
19 to 23 seconds.
Now.
In the inputs.
Outputs.
Reload it.
So pro shifted domains.
Is 576.
That's our.
Cap.
But.
In the shifted domain.
SD file.
We're at 487.
Because we finished three.
So.
That is going to keep.
Plugging.
Meanwhile.
It was just translating.
The background.
To have more.
Now.
Just.
We can already.
Start to push.
We'll run it again.
Later.
To catch up.
But.
We can already.
Take the next step.
With the.
488.
Shifted domains.
Okay.
So.
Pull back to the visualization.
What does the shifted domain.
Look like.
And then.
How.
How are we going to use that.
To write the dissertation.
Outline.
So.
Here.
Let's look at.
Logistics.
Applied to Hymenoptera.
So.
Every single.
All by all.
Was.
Just the concatenation of.
You're a prompt.
Expert.
You're about to do.
This domain shift.
Here's domain A.
Here's domain B.
Make the shift.
So here's what the.
Shift domain.
Yields.
So.
Deep analysis.
Of domain A.
And this could be structured.
With systems thinking.
Len Troncali.
George Mobus.
Etc.
Etc.
Etc.
It would be awesome.
And there's many more structured.
That's been one of the most surprising.
Learnings.
Overall.
Of the last like.
Five days.
Is.
Yeah.
There's some.
Structured ways.
To do cognitive modeling.
Claims analysis.
Rhetorical analysis.
All these kinds of concepts.
However.
Especially with cursor.
In the game.
There's so much.
That can already be.
Brought forth.
With this.
Rough.
Or fuzzy.
Probabilistic.
Blob.
And hope.
Strategy.
So.
Domain A.
Deep analysis.
Domain B.
Separate analyses.
Identification of isomorphies.
Isomorphies.
Sorry.
Identify.
Isomorphism.
So.
Similarities in structure.
Between A and B.
Transposition of fundamental elements.
Novel hypotheses and theory.
Ant colony supply chain management.
Develop a new.
Lexicon.
Who's on first?
Outline a research agenda.
Envision.
Revolutionizing education.
Identify technological innovations.
Anticipate resistance limitations.
Propose interdisciplinary collaborations.
Construct a compelling narrative.
So those were the 12.
Sections from the prompt.
So that's why these shifted responses.
Are just responding to the structure.
That was.
Suggested by the prompt.
So now we're going to go from.
Those shifted domains.
Which are just kind of like.
Fact sheet type reports.
Now.
We're going to go from the shifted domain.
To the dissertation.
Outline generator.
Dissertation.
Tab.
Outline generator.
Similar.
Where the dissertation.
Output file.
Already exists.
It skips it.
Now it's going to be.
Writing an outline.
So now let's go to.
What.
Let's look at the dissertation.
Outline script.
All right.
So first.
Generate pro shift domains.
Just really fast.
Logging.
Cursor.
Incredible.
For helping logging.
And bugging.
And debugging.
Here's the concatenation.
Prompt.
Domain A.
Domain B.
Please prepare yourself.
To make a shift domain.
Here's domain A.
Here's domain B.
For all domains.
That outputs.
That concatenation.
Okay.
Now we go to the.
Out.
The outline generator.
Dean asks.
Are those.
A.
B.
Isomorphisms.
Assume stable.
It's a great question.
Put it this way.
If you didn't change.
A text file.
And you ran.
The same computer.
It would give.
Probabilistically.
Within that envelope.
The same quote.
Results.
Which may or may not.
Reflect.
How things actually were.
Of course.
You can make synthetic domain.
You can make custom domains.
You can do Harry Potter.
You could make different.
Domains.
That also don't have anything.
To do with anything.
So maybe you could say.
This is.
This is the platonic solid domain.
This is just very few expressions.
Very accurate.
All right.
Outline generator.
Again.
Logging.
Getting the.
OpenAI API key.
This is kept.
In like two ways.
In the.
Env.
Environment file.
And dot.
LLM keys.
Dot key.
Both of them are in the.
Get ignore.
So you can put.
Private.
And I won't open them on the stream.
But then it enables the scripts.
To use the API.
So you can just change that one file.
Like figure.
Out.
What your API key is.
Put it into.
One of these kinds of files.
And then basically.
There's a way to do it.
So.
Generate the dissertation outline.
This one.
I.
Used another method.
Relatively.
So instead of.
Whereas in the.
In this.
Concatenator.
I set the prompt.
As a variable.
And then.
Just concatenated.
Three variables.
So there could be different prompts.
Put in there.
Like.
It could go a lot of different.
Other ways.
Just to.
At the.
At the outset.
Because the prompt.
Here is going to.
Sort of direct.
How everything.
It's.
It's more upstream.
Whereas.
In the dissertation.
Outline generator.
Now.
Here's the.
Structure.
Of the dissertation.
By adding.
Many sections.
Even if it only gives.
Like one to three sentences.
In each of the sections.
It's still going to have.
A good length.
So it just says.
Provide.
You're.
Creating a comprehensive.
Groundbreaking.
PhD dissertation plan.
For a newly shifted domain.
This domain.
Represents a fusion.
Etc.
It does.
These can be on new lines.
It doesn't really matter.
Your task.
Is to create.
A detailed.
Expansive.
Intellectually rigorous.
Dissertation plan.
That articulates.
Etc.
Long line.
Using the provided.
Shifted domain description.
So that's that kind of like.
Fact sheet report.
Like here's how logistics.
Could apply to Hymenoptera.
Develop a massive.
Dissertation plan.
Then here's the.
Structure expected.
That's it.
Then.
It concatenates it with.
The.
So that fixed prompt.
Plus the.
Shifted domain.
That yields.
Shifted domain dissertation outline.
So.
Now this is starting to get.
Bumped up.
From 484.
To 493.
So let's look at.
One of these new.
Shifted domains.
Outlines.
So let's look at.
See if any have.
Been written for the matter yet.
Let's see which ones.
Have just been written.
Most recently.
Okay.
Okay.




























Synthetic hospitality.
To synthetic intelligent.
Soft matter.
So.
This could be.
A hospitality lab.
Saying let's go into soft matter.
Could be the.
Soft matter lab.
Saying let's go into hospitality.
But look at this one.
And the other flipped.
Okay.
So.
Personalization.
Service quality.
And sustainability.
From hospitality.
The research.
Aims to redefine.
The capabilities.
Of soft materials.
Creating responsive.
User centric.
Designs that adapt.
Environmental stimuli.
So background.
On the shifted domain.
Novelty.
Overarching questions.
So again.
This is the direction.
Of going.
How can the principles.
Of guest experience.
Be applied.
To the design.
And functionality.
Of intelligent soft materials.
Whereas.
The text file.
That says.
Intelligent soft matter.
To hospitality.
Will say.
What can we learn.
From intelligent soft matter.
That will help us.
In the hospitality.
Questions.
And situations.
Then it has.
All the structures.
Okay.
New theoretical constructs.
Emerging from the shift.
So this one.
These are actually.
Sometimes super funny.
And there could be sections.
Like add more puns.
And memes.
And everything.
But responsive experience theory.
User interactions.
With materials.
Can enhance functionality.
And satisfaction.
Like the material.
It's not like.
Its properties.
Are just a priori.
And fixed.
They're interactive.
So there's a.
A relationship.
With responsivity.
Materials.
Quality.
Assurance model.
A framework.
For assessing.
Intelligent materials.
Based on user.
Experience metrics.
Again.
Let.

Let.
In the all by all.
Semantic.
Landscape.
Let.
Let that be the starting point.
But if there's a.
If it's a variant.
Or if it's like.
Another way to go.
Then that's just the starting point.
So that just gets the conversation going.
Methods.
Ethical.
Personalized soft matter.
Quality metrics for materials.
Smart integration.
Sustainable design principle.
Interdisciplinary implications.
Practical applications.
Future research.
Conclusion.
Let's look at.
Another recent one.
Okay.
Okay.
Entomology.
Two.
Non-science.
Ways of knowing.
Dissertation plan.
How can the principles of entomology.
Inform personal development.
Community resilience.
What new theoretical constructs.
Emerge from the intersection.
Of entomology.
And non-science.
Ways of knowing.
In what ways.
Can this shift to domain.
Influence.
Educational practices.
Societal structures.
Metamorphosis.
As transformation.
Social structures.
And community.
Communication models.
Ecological wisdom.
Etc.
Thank you Michael.
And Dean.
Great comments.
Alright.
So.
Back to the visualization.
So.
That was generating.
The dissertation outline.
Next.
Dissertation generator.py.
Same.
Same.
Logic.
Skipping the files.
That already existed.
Let's look at.
What the dissertation.
Looks like.
So.
Shifted dissertations.
484.
That was the starting number.
So.
These were the ones.
That were there earlier.
How about.
Cooking.
Two.
Free energy.
Principle.
Active inference.
By analyzing.
How flavor profiles.
Cooking techniques.
And culinary fusion.
Can be understood.
Through predictive coding.
And variational free energy.
This research.
Seeks to redefine.
Culinary arts.
And enhance the dining experience.
How can culinary practices.
Be modeled.
As adaptive systems.
That minimize free energy.
What role do.
Predictive coding.
And variational free energy.
Play in the development.
Of flavor profiles.
And cooking techniques.
In what ways.
Can this interdisciplinary approach.
Influence culinary education.
Etc.
New theoretical constructs.
Culinary systems.
As adaptive systems.
The role of sensory feedback.
Okay.
Here.
36 seconds.
It also includes.
The self.
I didn't exclude.
The.
The A shift to A.
So.
That's actually.
Another informative loop.
About.
About.
What's there.
All right.
But now.
We have some new ones.
Refresh.
Okay.
Neuroscience.
Two.
Non-science.
Ways of knowing.
The significance.
Of this research.
Lies in its innovative approach.
To.
Knowledge integration.
Challenging traditional boundaries.
Between science.
And non-science.
By leveraging insights.
From neuroscience.
Etc.
Etc.
Etc.
How can principles.
From neuroscience.
Be applied.
To understand.
And enhance.
Cultural practices.
How?
What are the implications.
Of cultural neuroplasticity.
For community resilience.
And adaptation.
How do cultural narratives.
Function as symbolic messengers.
That influence emotional states.
And behavior.
What interdisciplinary methodologies.
Can be developed.
To facilitate this integration.
Of knowledge.
History.
Ramonica Hall.
Non-science.
Ways of knowing.
New theoretical constructs.
Cultural neuroplasticity theory.
Maybe it's drawn from somewhere.
Maybe it's just a synthesis.
Symbolic transmission hypothesis.
Whatever is in the schema.
For the dissertation.
It will write something.
With that output.
There's a few situations.
Where.
Where.
Especially in translation.
And things.
We'll say.
Oh.
I don't really do that.
Okay.
Let's.
Let's just carry.
Carry on.
In the pipeline.
Then.
That.
That's the dissertation draft.
So this.
Should.
Maybe be dissertation draft generator.
But.
Obviously.
It's all a draft.
So.
The dissertation improver.
Okay.
So.
It's.
It.
You can.
Open a new terminal window.
If you want to have.
Another.
Open.
Edge.
With the API.
But.
Let's.
Just.
Terminate.
Terminate.
The one.
That's.
Shifting.
The domains.
So.
That's how many.
We'll.
We'll just carry forth.
Okay.
All right.
Dissertation improver.
Skips.
The ones.
That are already written.
It's gonna.
Now.
It's hitting.
New ones.
That are also.
Getting pumped in.
From here.
This could be coordinated.
Like a lot.
Better.
All right.
Dissertation improver.
Okay.
This could be iterative.
There could be different rounds.
Of commentary.
So.
That was.
Again.
One of the most shocking.
Slash.
Interesting things.
Was.
On.
On.
On.
Two different.
Domains.
So.
At the.
Structure.
At the level.
Of.
Sections.
Of a.
Document.
Like.
Structuring.
Modular.
Publishing.
And all these kinds of.
Efforts.
And.
At the level.
Of.
Structuring.
Like.
Agents.
And reviewers.
And critiquer.
And actor.
Network.
Models.
So.
Here's.
Where.
Both of those.
I was.
Surprised.
On.
For.
The.
Document.
Composition.
There's.
Very.
Good.
Adherence.
To this.
To the.
Prompts.
Like.
I'm.
Using.
Here.
Like.
Every.
Single.
PhD.
Outline.
Uses.
The.
Exact.
One.
That's.
Requested.
So.
You could.
Add.
More.
Sections.
And.
Add.
The.
Token.
Length.
And.
Everything.
Add.
Different.
Sections.
You could.
Request.
A.
Different.
Kind.
Of.
Document.
Structured.
With.
Certain.
Subsections.
That.
Like.
Do.
Or.
Don't.
Make.
Sense.
With.
Relationship.
To.
Your.
Your.
Input.
Folder.
Um.
So.
Yes.
It's.
Very.
Strong.
And.
Interesting.
To.
Pursue.
The.
Strongly.
Composable.
Document.
Composition.
However.
Using.
Clear.
Prompts.
Is.
Giving.
Documents.
With.
Good.
Structure.
Then.
On.
This.
Level.
Of.
Like.
Multi-agent.
Science.
Science.
Agents.
Writing.
Massive.
Writing.
All.
These.
Kinds.
Of.
Things.
There's.
A lot.
Of.
Like.
Flow.
Like.
What.
If.
This.
Went.
To.
Here.
And.
That.
Went.
To.
Here.
And.
I.
Think.
Again.
That's.
Very.
Interesting.
And.
Jakob.
Smekal.
And.
I.
Wrote.
The.
Generative.
Research.
Teams.
The.
GRTs.
That.
Discusses.
A lot.
And.
It.
Was.
Exciting.
Okay.
How.
To.
Active.
Inference.
Agents.
And.
Other.
Kinds.
Of.
Of.
Intelligences.
Worked.
Together.
Ecosystem.
Shared.
Intelligence.
AOS.
The.
Active.
Entity.
Ontology.
For.
Science.
Back.
In.
The.
D.
Sci.
2022.
Days.
All.
Those.
Kinds.
Of.
Directions.
Like.
Let's.
Have.
Some.
Kind of.
Interoperable.
Strong.
Message.
Passing.
And.
Again.
I.
Think.
That.
Is.
Going.
To.
Be.
A.
Strong.
And.
A.
Vital.
Element.
But.
Here.
With.
The.
Total.
Cost.
Of.
Millions.
Of.
Tokens.
Still.
Under.
The.
Tens.
Of.
Cents.
At.
Least.
Using.
Cursor.
It's.
Been.
Easier.
To.
Just.
Do.
All.
By.
All.
All.
By.
All.
By.
All.
And.
Just.
Filter.
Folders.
Of.
Markdown.
Files.
But.
Then.
Just.
Do.
Another.
Combinatoric.
Explosion.
And.
Filter.
Down.
And.
Also.
There's.
An.
Interesting.
Connection.
There.
With.
How.
That.
Kind.
Of.
Relates.
To.
Abductive.
Inference.
And.
The.
Two-stroke.
Engine.
With.
Generating.
And.
Then.
Winnowing.
So.
So.
That's.
Actually.
Super.
Interesting.
Too.
Because.
It.
Turns.
Out.
I'm.
Not.
Saying.
Well.
If.
We.
Connected.
This.
One.
To.
Blake.
And.
That.
Fabric.
Science.
It's.
Like.
Just.
Blast.
Filter.
If.
Needed.
But.
If.
It's.
Not.
Even.
Needed.
If.

Just.
Text.
Files.
And.
It's.
Only.
A few.
Hundreds.
To.
Hundreds.
Of.
Thousands.
Should.
Be.
Fine.
So.
Dissertation.
Improver.
You're a world-class academic writer tasked with improving an existing PhD dissertation.
Enhance it in these 10 ways.
Follow these guidelines.
Like.
Only add things.
Make it better.
Make tables.
Add hypotheses.
Enhance the language.
You could.
You know.
Whatever it happens to be.
Here's the dissertation to improve.
Insert dissertation in the concatenated file.
Please.
Do it now.
So.
Here's improving dissertation.
Chemistry to soft matter.
So.
Some of these.
It's like.
And again.
This is what the language analyses show.
Like.
In the semantic spaces.
In their own different ways.
Whether it's a syntactic or the semantic side.
Is like.
Okay.
Chemistry to chemistry.
Or chemistry to quantum.
Or chemistry to soft matter.
Those might.
Like.
Cluster.
Closer.
That's the exact kind of thing.
That we do.
So.
That we do.
Measure.
And analyze.
And this is just a representative image here.
Because you can imagine all kinds of linguistic.
Analyses there.
So let's go to the improved dissertations.
This slightly.
Increases their length.
I didn't.
Analyze the distribution.
But like.
They're all.
Kind of like.
Over 20.
Mostly.
So.
Shifted dissertations.
That was the input.
Improved once.
Let's do.
Let's just look at one that was already.
Things.
Oh.
Well.
Blockchain to logistics.
Everyone knows about that one.
It's like.
Okay.
How about ATM transaction.
To Bucky Fuller.
By transposing.
The efficiency.
Accessibility.
And security.
Of ATM transactions.
Into Fuller's framework.
Of sustainable design.
Systems thinking.
This research.
Aims to develop.
A novel model.
For resource management.
And service delivery.
The proposed.
Dymaxion kiosk.
It's like.
New post.
Fuller term.
Just dropped.
Will serve.
As a practical.
Application.
Of this model.
Addressing global challenges.
Through community engagement.
And innovative.
Technology.
Okay.
Dean says.
Michael says.
It's hilarious.
And yet.
Strangely educational.
Absolutely.
And.
And I think.
Another thread.
To pull on.
Is like.
This is simpler.
It's so different.
You know.
Catastrophically.
Different.
Than.
2014.
To 2019.
Doing my PhD.
With.
Limited.
Computer.
Fieldwork.
Less video chatting.
But.
It's.
It's easier.
To just.
Handle the folder.
Slash.
Different.
So.
It's.
It's just.
It's all.
You know.
Different is different.
And then.
Dean says.
Can you build an information mutation.
At some specific level.
Would that help the what ifs.
Over the derivative intersection.
Yeah.
Yeah.
That's like.
Someone just says like.
This is just like.
Pulling a crank.
Like.
Like.
You're just like.
Moving.
Strings of pasta forward.
And then.
They're just going to.
Be.
All headed for the trash pile.
But.
What you could do.
Is you could be like.
Okay.
Like.
Okay.
Cooking to logistics.
That's kind of interesting.
Maybe there's a grant program.
Or there's like a PhD student.
Applicant.
Volunteer.
Who thinks this is like.
Funny.
And then.
Synthetic cooking logistics.
But it's just a text file.
So now.
Later.
We're going to translate this.
But.
You could change this.
And just say.
We're.
Redacting this part.
You know.
Replacing that one with that part.
I'm not going to stick it.
But.
You can change this.
Or you could write another script.
That says.
Mutate.
And it just does.
Any kind of mutation.
To any subset of these.
Text files.
Okay.
So then.
Back to the visualization.
Now.
It's translated.
It's translated.
Dissertation.
Translation.
Again.
It's so cheap.
Per translation.
Below.
Below cents.
Per.
Operation.
So here's translation.
Here's the list of.
Languages.
We're going to look into the folder.
And just see what it outputs.
For some of these.
Translated dissertations.
By language folder.
Okay.
Here's.
Here's.
Neuroscience to William Blake.
In Bengali.
can't read it
chemistry onto itself in hindi
okay languages with uh data sets that are large
have strong complete translations
we can tell just by looking at the file sizes here so for hindi they're all 34 ish
here we have a range which is interesting so here's a smaller one here's very small
i cannot provide a translation of an entire phd dissertation into navajo
here's a longer one
translating a phd dissertation into navajo while maintaining high academic quality and technical
accuracy is a complex task that requires deep understanding of both languages and the subject
matter below is a translation of the provided dissertation into navajo following the guidelines
you specified
neuro neuroscience onto cognitive security
so here it's like i won't but then i did 14 here's a 4.3
okay it's going to be hard it's a complex task however i can provide a sample translation of a portion of the dissertation to demonstrate how this can be approached please note that due to the limitations of this plan i can't be able to do this for the
to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make this to make
Similarly, there's a 228 version.
Let's read it.
I can't do it.
And then an even smaller version.
I can't do it.
But the ones with a lot of training data, they have large consistent file sizes.
So here it is also logging, taking one minute less than a cent per translation.
Skip the ones that I had done.
72, 67, 58.
All right.
Language analysis, last thing.
Then we'll just do some other random improvements and look at Super Chats and everything.
Michael Lennon says, I feel like I'm witnessing a shifting, a pushing of the boundaries of
what does science slash knowledge work in the near future?
Thank you, Michael.
Thank you.
I'm super happy to be able to share this.
And for it to be open source and for there to be so many affordances for people to contribute
and fork and clone.
All right.
Language analysis.
Language analysis.
Let's just see what we have running right now.
Okay.
So now this one is finished.
So right now the orchestration, like you, you kind of have to comb over the folder a few
times, or you could do, let it all shift, then let it all write the outline, et cetera.
Or you could add multiple multi-thread computing, but these kinds of things are what cursor at
all are incredible on.
It's like selecting a piece of code and then just saying control K or control shift L saying,
make this run on N processors.
And then there are ways that it will do it.
Well, okay.
So from the terminal again, clear.
Okay.
Synthetic domains, or it could have been real data or any kind of data.
All these are just text file outputs.
You can mutate them arbitrarily at every single step.
No need for agent orchestration, just good old bioinformatics style text file.
Input domains, but not saying that, that there wouldn't be cases where you'd have higher efficiency,
et cetera, with more nuanced approaches and different things.
Input domains.
They were fully synthetic in this case.
We had start 22.
Then we bumped it to 24 with Vladimir Michael's suggestion.
Concatenate prep.
Optional step, if you want, you can just batch these two.
Shift domains makes the situation report on the shift.
Write the dissertation outline according to how you say it is.
Generate the draft from the outline.
Improve it once, expand it, add unique hypotheses, et cetera.
Now translate to N languages in their own folder.
And then last script for now, just the language analysis.
Oh, now it's called meta-analysis shifted dissertation.
All right.
So it's running in the terminal, processing text.
So this is a local computation.
This is not using the AI or open API, et cetera.
You define the input and output folder.
So here we're going to be looking at the analysis for the first dissertation draft.
But you just change the input folder and you can make it look at any folder.
These are just examples of linguistic analyses.
Again, I just control A and just like add more relevant, interesting visual outputs
to each folder.
Or make a new kind of folder.
Or make me something that will reflect my curiosity about X.
Okay.
So the script on the prior version slash on disk, quote disk, is here running.
But now we're also live editing.
We're confirming that the prior version works.
It's kind of like a little nano git, because then if I accept these green edits and just
rerun it right away, either it'll continue to run or it'll not.
Okay.
So here's, okay.
Now it's added networks, interactive, and dendrograms.
Will they work?
Let's find out.
Scanning over the parts that are already, that are just not being touched.
But there's times where it will just say, oh, deletes a huge block of code.
Or there's times where it just does things that move you in circles.
But you get to see a lot of code, and it's a well-structured code, at least to this non-professional
programmer's cursor-enhanced way.
Okay.
So it's a simpler semantic layer, whereas programming, when it got lost in the obscurity of where the
bracket is closing, it gets really down there.
Okay.
So I'm just going to close that prior version.
Clear.
Save the script.
So if this works, then we'll see new things popping up in this analysis dissertations.
So if that will pop up in these new folders.
But here's what these folders have now.
So this is principal component analysis.
K-means clustering.
Matrix decomposition methods.
T-SNE.
Not saying these are the most, like, performance or anything.
So many visual improvements.
But just to say those are clustering methods.
Oh, this one will, the axes may need to be adjusted depending on how many, like, terms are in there.
Okay.
Top terms.
Okay.
Top 30 terms across all documents.
Okay.
Okay.
Okay.
This is just the PCA kind of L that we saw before, but there's a shading, like a 95% density.
So this could be used like, okay, what's that one, that one, that one, and that one.
Or like, you know, and then there's the PCA interpretability methods, which look like.
So here's, here's.
Okay.
So here's PC1 and PC2.
These are linear decompositions and variance quote explanation.
So here, PCA component one.
So this explains the greatest linear fraction of the variance, just to kind of pull back one more step on the PCAs.
Every time you take a PC, you're explaining more variance.
That's what it's called.
It's not in the causal sense.
It's the correlational kind of explanation here.
But you're always going to explain more variance because you can always get some.
But then you look at the accumulation curve of the explained variance.
It's like, okay, maybe, you know, and then you could either calculate like, oh, this is the optimum, or we only have space for three, but it's good to know that it's only 18%.
Okay.
So here's one and two.
Each data point is a written outline.
So written file names can be improved.
So negotiation is highly weighted on this.
And quantum is negative.
So documents that use negotiation, negotiators, conflict, strategies, resolution, these are to the right on PC1, documents that mention quantum to the left.
PC2, which is the y-axis, is associated with the use of the word quantum.
And, for example, not the word culinary or mitochondrial.
Let's say, okay, yeah, quantum is up and to the right, et cetera.
So that's kind of what these plots are showing.
But then landscapes, and so, oh, what would be right here?
What would be like that one?
Okay.
Term loadings, let's see if it works.
Okay.
Specific terms.
Here's again, quantum is low on PC1, high on PC2.
Negotiation is slightly high on PC2.
Very far outlier.
You might get more resolution, like on this analysis, by just excluding these three terms.
But this is just one way to do the analysis.
Okay.
It's still chugging along.
But, yeah, you can extract what are the terms that are in each principal component.
So that's the kind of semantic space.
Okay.
Let's see.
While the visualization method is running.
So, like, here the translations are just chugging along.
Chemistry to cooking in Portuguese.
Chemistry to cooking, Bengali.
Now it's just looping through these languages.
Okay.
All right.
So, let's return to this kind of overall one.
But we'll watch the visual script run.
Okay.
End-to-end, all-by-all, field-shifting.
Domains can be synthetic or etc.
Dissertation outlining.
Expansion into the draft.
Draft improvement.
Draft translation.
Meta-analytic methods.
These are shown in the visualization.
But the visualization was just like, control A, control K.
Make ASCII art for this.
I think combining it with the grant methods that are in another corner of this repo.
Here.
Here.
That's one.
Adjacency.
Upcoming developments.
Okay.
Incorporation of the entity and organization cognitive model.
So, just, again, this was on the sort of how structured does a cognitive model need to be?
It was like, here's fields.py, Chris Fields.
Now, these are not even real quotes.
Necessarily.
But they were drawn from these six.
I draw the six interviews in.
Here's Friston, Bucky Fuller, Deborah Gordon, etc.
And, yes, there's other people thrown in.
So, it's nowhere near anything like a structured cognitive model, let alone like the kinds of real speaker-sorted transcripts that many people and organizations have.
This was just taking a few podcasts with these people.
And then, just distilling it.
And this, we can go into it like another time where we can add an entity if somebody wants.
There, again, there are these condensed quotes.
But depending on how you prompt it.
Okay.
Giving a vision or plotting here.
But let's see if it'll put anything else.
These are these like .py's.
Pseudocode-ish.
Quotey.
Now, they could be interoperable if you had a schema defined.
Maybe a PhD student could work on that.
But then, they can also be loose.
But bringing the entity and saying, okay, how could these two entities, like this organization and this person or these two people or these two organizations, these three, concatenate their entity models?
Like, we can even do this.
And then say, how could they refract through this shifted PhD dissertation to that grant?
Well, if you can compose it, it's at least plausible.
Okay.
Entity and organization cognitive models.
Integration of grant proposals per research method.
Secure funding for PhD projects.
Explain like I am dot, dot, dot.
So, we could concatenate a prompt that's like, explain this shifted about the dissertation that's applying ATM transactions to cognitive security.
Explain that like it's this kind of event to this person.
It never is going to at least be interesting and funny when it shows.
Okay.
Okay.
Thank you, Michael, for your great comments.
Always very insightful.
Okay.
So, then we could do, how would you explain this to dot, dot, dot.
And then that generalizes, oh, 17, 18, 19, 20.
But then, so what does the model think about how you should explain something?
And then it's like, well, let's call multiple models if they're getting so, so, so available.
Now, that's the whole deeper questions about like externalities, et cetera.
Grant methods.
Okay.
Just as a brief recap.
Well, I'll put the, in the live chat.
Here's the field shift coda.
Here's the grant method.
So, this is, this is from prior.
So, this kind of goes through what the grant concatenation methods do.
I'm not going to go through it on this stream.
But they're in the same research methods folder.
Okay.
Yeah.
And, and then any other things.
So, maybe one, we can try one suggestion that somebody has.
Like one analysis or a new domain or a new entity or like, let's just do one random thing.
Um, you can support the project and earmark donations at donate.activeinference.institute.
Future streams.
Oh, this will be, there's actually a few, a few other interesting topics while people are thinking about, um, what else to say.
Okay.
Uh, P3IF.
There are some pretty extensive P3IF methods in the repo.
It'll be a later actinf, uh, ant stream.
But check it out.
If you look at the repo.
Uh, it would be awesome to have, if, if someone sees like an adjacency or if they see something that they can add to like section nine.
Um, any of these kinds of, of like frameworks that could be awesome.
And then we go, oh, make a Kafka database that sends messages to the Coda API to write these grants and then post it through MatterBridge to Discord.
Then developing the active inference, uh, kernel of the inferant repo.
So Python, PyMDP, et cetera, Julia, Rx, and for other languages, there's several other languages.
Section nine.
Okay.
Okay.
Here was just one sort of thought on the multiply scale science.
So this is just using just a sort of standard academic ontology here.
PhD student is like one dissertation contains multiple papers, which was how it was, uh, concisely described to me.
Then a principal investigator has a lab with multiple dissertations, overlapping serially.
The organizational scale is to have multiple labs within one organization.
And then above the organizational scale, especially in an online context, it is a Spaceship Earth situation.
And that's part of this, um, grand science, Spaceship Earth journey.
Um, one tiny step for an epistemic forager, one giant leap for ant kind.
Flower poem.
Flower poem.
Okay.
This is going to be a short Tennyson poem.
So the, the kind of background on this was, um, Buckminster Fuller was on the editor team for this journal called T-Square, later known as Shelter.
And Frank Lloyd Wright wrote this article about how all may, may plant flowers.
And then I looked that up as a title and found that it came from this, uh, poem.
So, and then also it's going to be awesome to see how the, the, um, cursor can enrich this too.
Okay.
The Flower by Alfred Tennyson.
Once in a golden hour, I cast to earth a seed.
Up there came a flower.
The people said, a weed.
To and fro they went, through my garden bower.
And muttering discontent, cursed me and my flower.
Then it grew so tall, it wore a crown of light.
But thieves from over the wall stole the seed by night.
Sowed it far and wide, by every town and tower.
Till all the people cried, splendid is the flower.
Read my little fable, he that runs may read.
Most can raise the flowers now, for all have got the seed.
And some are pretty enough, and some are poor indeed.
And now again the people call it but a weed.
And then I, I did this one time, but I'll, I'll see where it goes this time.
Explain this in the, uh, just discuss this in the context of open source.
It, it said some really funny things.
But then the way that kind of connected to the doing and the learning and the foraging,
and then also the planting, planting experiments, collaborations, really proceeding on grants.
Um, like, not just planting the seed, but there's the foraging and, and, like, attending and being attended to.
And planting and, and or foraging.
For, for having and or being able to have the seed.
However, that doesn't mean every foraging trip, etc.
Okay.
So, open source, you know, from, from back in the day.
The seed is dismissed.
Next.
Resistance from proprietary software.
Success.
The, the theft of the seed at night might symbolize how proprietary companies sometimes adopt open source principles or code without fully embracing the open ethos.
People use it.
Anyone can use it.
The final stanza reflects the reality of the open source ecosystem.
Not all projects or forks are of equal quality.
What was once novel may become commonplace or even dismissed again.
Um, wow.
Okay.
Thank you, all the, the chatters.
Let's, let's look at, let's do one of the, let's do one more kind of permutation.
Let's do the explain like I am X.
So, we just saw the, uh,
outline generator.
Let's go to one that has a fixed prompt.
It will be simpler.
Take the copy.
Rename it.
Explainer.
Control shift L.
Go on to the right side.
It could be done in line too, but just sometimes it's more deliberative on the right side.

Adapt this script to be an explain like I am blank.
Analogous to the list of.
Target languages.
Make it.
E.g.
Target audiences.
Michael wrote.
Michael wrote.
Angus Deaton, Nobel for econometrics, warned recently about hidden power dynamics behind
quantified models.
Helping with the inter-humaning around the tech, e.g.
Uncovering hidden power or fussing forward through competing interests is key.
Thank you, Michael.
Oh yeah.
If anyone has, uh, something for in the, uh, 10 to 30 minutes total, let's see how far this
explainer goes.
And then, uh, anything else or like comments or, or questions that people want there.
Okay.


Okay.
Okay.
Okay.
Okay.
Okay.
Okay.
Okay.
Okay.

Okay.
Okay.
Okay.
Okay.
Okay.
Okay.
Okay.
So, it changed target languages to target audiences.
Keep the API key.
Here's translate dissertation.
Here's explain dissertation.
So, replace target languages with target audience.
Renamed translate to explain.
Updated the prompt.
Updated file naming, adjusted log message and print statements.
It's like, what?
You did what?
Uh, accepted.
Okay.
Let's tune the, uh, well, first let's just see if there are any other visuals that that
script halted.
Shannon diversity indices.
Shannon diversity indices.
So, this is the font, of course, can be fixed, but this is kind of interesting.
This, this, this may just be a, a, a random draw, but still within the documents, some have
a higher and a lower Shannon diversity of, of term usage.
So, maybe those are more interesting or have more combinations.
Heat map.
Term frequency heat map.
Okay.
Yeah.
Y axis, you know, scale could probably be improved, but there are some things there.
Correlation matrices.
Interactive, nothing output.
It just halted.
It just, maybe it's too big of a jump.
Networks, halted.
PCA.
3D.
In and out.
Think outside the box.
What box?
Quantum negotiations.
This showed the vector that we kind of looked at with the loadings.
Variance accumulation.
No vector, just the data.
Like, again, this is just PCA.
This was taken from the grant processing pipeline.
So, it was, you could look at the heat maps of different entities.
Top terms.
Just across all documents.
Word clouds.
Didn't output.
Okay.
Let's, if there's any target audience.
Let's see if we can do just a couple.
So, we get a few across each.
Let's have curious five-year-old.
Oh, autocomplete.
Curious.
It's just like that.
With the syntax and the autocomplete.
But, I'll edit this down to a few.
But, also, anyone should write in the chat and we can include a few creative target audiences.
Skeptic.
Skeptic.
Well-studied and highly motivated.
Skeptic.
Well-studied and highly motivated.
Skeptic.
College students undecided on their major.
Michael Lennon writes, some additional dashboard indicators.
Epistemic forging adjacency.
Oh, yeah.
Additional audience types.
Okay.
Yeah.
I'll wait.
I'll wait a few minutes.
I'm going to throw.
I'll, while people write that for a minute.
Okay.
So, now the functions explain dissertation.
So, now here's the prompt template.
Fixed.
Prompt.
Your world-class educator tasks with explaining PhD dissertation to a target audience.
Maintain accuracy while adapting the explanation.
To the audience's type of understanding and broader person-ness.
Adjust language.
These are, this is where it gets triply.
Interesting with how people really think about the topics.

Adjust.
This is just, we won't go into deep.
The model training and this and how it's processed.
Adjust.
Adjust.
This is just, we won't go into deep editing this, but this is just what it comes up with as the
likeliest thing that you can do.
To generalize across explanations as a concept.
So, now the, the model training and this is just, we won't go into deep editing this, but this is just what it comes up with as the likeliest thing that you would say to generalize across explanations as a concept.
Okay.
Okay.
Thank you, Michael.
Let's do.
curious five-year-old
okay we can go rich or we can just go more simple and general
of a just well this one phd student then college students we have we have five-year-old
how about high school senior undecided on
whether or where to go to college
phd so we have five 17 phd student
advanced
um professional advanced technical professional
okay
python 3 dissertation explainer okay bug that was the the one shot so then here's here's
it'll it maybe we need to fix the input outputs
let's go from original oh it's not original dissertation so that's that's like a it's
just like there it didn't take the file structure into strong account um but in many many cases
it does it just that's where it so while it's kind of thinking that just because it's saying
from original because i use the word original but then it didn't know which one of these
so let's go to make it the shifted dissertations improved once

clear
explaining dissertation to a curious five-year-old boom
cursor's gotten better and better in every version truly and uh these are some of the minor things
that you know whether it's whether how it's cursor side or the llm side just the way that it's uh doing web search for best practices and and able to parse some of these just arcane syntax
it's incredible all right they are coming out into
explain dissertations we'll let a few accumulate okay
explain dissertations
explain dissertations we'll let a few accumulate okay
the goal this script doesn't really work or this overview now needs to adopt slightly but the goal of this was to make
like let's see also it's this is one other thing is sometimes it helps to manually resync the index
that's the vector embedding that cursor is using um under the hood
so it won't be able to unindex code it will not be able to find
so i i even if you do add new files see it it it here now it's synced it so now
control k let's just do i think control shift l
update this to reflect the folder structure input outputs functions etc of everything now
update this to reflect the folder
now
hundreds of changed files
you
you
you
you
you
you
you
you






you
we









































































partially accurate there aren't the explanations so it's like wildly
admixed combinations of close technical very subtle
uh errors on through just like totally believable but also and then just like
okay here's how you run the script it's like no it's not
reject it
okay explanations
all right five-year-old
okay first it's starting with all right so let's let's do
um okay the
neuroscience to we're applying neuroscience methods to biology for a five-year-old so this is maybe like
some of mike levin's love from that original field shift paper like neuroscience concepts onto
developmental biology
okay what's the big idea understanding how nature and brains work together
what's the big idea
imagine if nature like a big park with lots of plants and animals works a bit like a brain
this project called the dissertation etc why is it important questions we want to answer
what we found out before found out about brains we found out about biology those are the from the two domains same strategy
new ideas nature can change learning from experience
neuro concepts applied to ecosystem but i remember the paper like what can ecosystems learn and it's it's always coming up and then so it's like stabilize the metaphor
the metaphor raise the water level on the metaphors overall and the kind of take the water table to to to be like this for every all by all how we're going to learn more what we'll discover why it matters what's next let's keep exploring even little emojis okay now let's go to high school
it's still in the it's uh
still okay
let's let's go to phd
neuroscience to cooking
neuroscience
literature
written more in a high school textbook
style
background significance and novelty overarching research questions literature review overview of neural networks
world networks


i don't know how you pronounce some of these uh tables in conversation
58 perceptron
okay historical development the culinary arts
current state of the art
here's the gaps and opportunities
pretty long this is uh this is looking more like
well this was over this was for a phd student
so this is more like here's the kind of brief on each of the sections of the dissertation
neuroscience
neuroscience
to cooking
let's see if this one has similar
okay this is like sharing uh your overall
outline
for like quals
or something
high school senior
okay
so this is a
um
um
same one we looked at with cooking
but now for the high school senior

what if cooking was not just an art but a science
because it's neuroscience

background
significance
simpler questions
but still broadly like the uh
structure of the dissertation
here's what the chapters are about
and
but with just one sentence instead of like
several paragraphs there
however it's structured like a dissertation
and then
yeah okay let's do a few
mills 8102 wrote
i love these wild mashups i bet there's plenty of gold in this approach
oh
so
now we're just pushing like
kind of trickling the next few
through
but let's let's go to the shifted
once
so these are these are you know the ones that have been improved once in a certain way
so
let's do
Blake applied to logistics
!
so this one was super fun
again i just wrote
make expressions about William Blake
and add about his mythology
so
by examining the parallels within Blake's emphasis on creativity spirituality and social critique where the challenges faced in modern logistics the research needs to establish a new paradigm term the Blakeian model of logistics that prioritizes visionary approaches to supply chain management

William Blake's life
how can Blake's concept of imagination and contraries inform innovative practices in logistics
and then if someone's like well what about this other important concept it's like first off
maybe it would have selected from it second off
add that to the original synthetic domain
and then that topic will come up in approaches
in what


in what ways can a spiritual approach to work enhance ethical considerations in supply chain management
what frameworks can be developed to balance efficiency and sustainability in logistics
Blake's accurate birth and death because it was included in the factual claims
the Blakeian model of logistics
the Blakeian model of logistics
duality framework
balancing competing priorities in supply chain management

statistics
usually a kind of mixed method
like
through structured prompt or
! any of these way more advanced methods
access to the literature etc
any of these way more advanced methods access to the literature etc you could have it be proposing
specific hypotheses it could even be writing the code for for the pre-registration and everything
sustainability okay the blank ones are fun um
uh let's quickly look at the prediction matter expertise domain just just because it's it's the
it's the outlier domain so this is part of the long-running uh dean tickleism with the subject
matter expertise like the domains and then prediction matter expertise as this kind of
like orthogonal dimension so for this one i did copy in a few of our specific uh papers
like about alice and bob wayfinding so there was a few then i just said just expand on this concept of
a prediction matter expertise come up with mottos come up with memes switching gears like a pme pro
when in doubt synthesize it out predicting the future one cross-disciplinary inset at a time
so questions examples but it it so it just invents all these examples so that one is sort of like
that's what's that's the the paradox with the um pme as an sme but let's see what one of those might
look like okay so this is healthcare principles applied to pme
so pme is what needs to be transformed by establishing a robust framework for user experience
quality metrics and tech driven solutions predictive analytics patient-centric
how can we map healthcare situations to prediction matters
healthcare what how about something with uh
with the spatial web
cognitive security to the spatial web cooking to the spatial web
examining how principles from the culinary domain can enhance user experience design in digital environments
how can what works for restaurants as as places and times and experiences work for
spatial web how about prediction matter expertise to spatial web
and then again it's like oh i would have said something different first off we can have many
branches of people's models but also then just we edit the source document
this seems to highlight just a predictive statistics
and adaptability angle
but then the language analysis can be like on these and then you can do it on the explanations and and
one of the one of the interesting and i think helpful ways to think about a few of these operations that
are happening is like the principal component analysis on the term frequency
uses so let me pull that one up and then
the other one up and then we'll see if we can do it on the term frequency
so here term frequencies are being used across within and across documents
so in this situation if you had uh x dissertations in the folder and then you're going to translate into
a bunch of different languages like l so if you cluster on syntax like term usage
then the languages are going to cluster together because they're using terms that are like exclusive
to one language or another character sets even if you clustered on semantics then the dissertation
would cluster together across languages which convey in in the case of an accurate translation like
similar-ish semantics so that's basically the difference between syntax and semantics
and that's something that's really opened up with these methods is what what i've been showing with the
term frequency type analyses syntax based methods they're still very cool and there's actually a lot
of information in them however what cursor especially but the language models overall are enabling is just like
that's like arbitrary semantic discussion so
thank you michael you know explain the at
field shift overall to a clam
okay advanced technical here we go
neuroscience to blockchain for advanced technical professional
foundational work proposed integrative mild model neuro chain adaptive consensus learning smart contracts
mixed method case studies surveys interviews simulations analytical approaches
so here's

that's the explanation script is running oh here's the clam
you're nestled in your cozy ocean bed and suddenly the water around you starts to change
you're not going to worry about the amount of space to change that's a bit like what field shift does but for
researchers studying the world above the waves
field shift is a special tool that helps scientists understand how the environment is changing
interesting
field shift collects a lot of data about the environment like temperature rainfall and plant growth it's like
what
so that's kind of the funny again the the huge
the huge range of what comes out in different contexts.
Let's look at a few more random dissertations.
Yeah, these are the ones that were made more recently,
but we halted that one.
Let's just look at one or two more.
Okay, William Blake.
Oh, we looked at a Blake one already,
but we haven't looked at a...
Let's look at one.
FEP.
See, this whole FEP applied to X.
This is like...
I hope broadening the scope,
it's like it's not just A to B for FEP to that.
The immediately available adjacency space
is domains to the second power.
For starter,
even before imposing other more high-dimensional aspects
for interdisciplinary from to to.
But then there's other structures of synthesis,
other kinds of patterns that can be emulated.
But this is just the from to to.
So we have...
Whatever expressions and claims we put in about FEP and ACT-INF
that fit in with the LLM schema slash length and attributes,
this is the starting point or a starting point
for some of those discussions.
So here's...
So here's...
FEP mitobiology.
Transposing the free energy principle to mitochondrial function.
How can predictive coding and active inference
be applied to mitochondrial function?
Different methods.
Like that would relate to the actual working it out.
FEP to an ATM transaction.
It transcends the immediate context of self-service banking.
It holds broader implications for adaptive systems
and technology and user experience design.
First principles for the ATM.
First principles for the ATM.
First principles for the ATM.
First principles for the ATM.
FEP to quantum.
Something that is happening.
So in the context and or in the files or...
It may...
FEP.
First in.
How can the concept of VFE be applied to optimize quantum algorithms?
In what ways do generative models in FEP correspond to quantum states
and quantum computation?
What are the implications of active inference for the measurement processes in quantum systems?
Okay.
FEP to cooking.
How does predictive coding and active inference apply to flavor development in culinary practices?
In what ways can generative models inform the evolution of cuisines and culinary fusion?
What educational frameworks can be developed to integrate FEP concepts into culinary training?
How is this ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail ail
If anyone has a last comment though, please feel free to ask a comment or question.
Position 10, slow request.
So even when I'm way over 500.
Oh, also here's what else is amazing.
I'm going to reload the page.
I don't think anything will.
I've spent $12 on this whole phase of the project.
First API call I made was on August 1st to GPT-4.
I was like, okay, that's the best model, right?
Wrote two of like the two of the first step.
First two shifted domains.
Stopped it.
Wait five minutes.
Reload.
I was like, oh no.
Well, that was $3.
Oh, $1.50.
It's like, okay.
And then I looked up.
I asked perplexity.
I was like, what are the costs and everything?
And what's the best one for large stock?
It's like, oh, GPT-4O.
Okay.
So that's $2 today.
And then yesterday when I went through all the, I mean, when it was going through all the, like, 484 or whatever it was, that was $3.
Then activity, number of tokens.
Now it's hidden too fast, but that's even just with a couple of Python terminals.
Here's GPT-4 mini.
That was 11 million, 11.7 million tokens for $3.
So tokens not exactly a word, but like, this is on the order depending on everything, et cetera, et cetera.
I don't know.
But it's, it's, it's not, it's not 10x and it's not a tenth.
So it's an incredible amount of text processing.
Today, 6.8 million tokens for $2.41, $2.42.
And then cursor.
So cursor, I'm paying $20 a month.
This is just to describe the method, methodological and the kind of financial, not the time side, but just like cursors $20 a month for the 500 fast requests.
But then the slow ones are not that bad.
So I don't, I don't know how it is, not with that at all, but, but it's, it's clearly worth that and, and beyond.
Then the API calls for open AI.
Oh, some colleagues shared the open router.
I think it's a great idea to like improve the LLM handling, make that more flexible, be able to do that locally, et cetera.
But just to use what was working now for several dollars to, to create these all by all's, do the shift, make the outline.
Write the draft, improve the draft, translate to arbitrary.
Control K, add the, this add the.
Explainer.
Into the visualization.
All right.
Any last comments?
Then I'll end it and push it after this.
It's like, it just says, no.
It's like, it just says, no.
Maybe if I don't call it.
Maybe if I don't call it.
Explanation still.
Okay.
Okay.
Curious five-year-old.
Let's see.
Little Blake.
Neuroscience, blockchain, chemistry.
Okay.
Neuroscience to Blake.
This special study looks at a famous artist and poet named William Blake and how his ideas
are like the way our brains talk to each other.
How can we think about Blake's ideas like a brain?
What can we learn from mixing brain science and stories?
Here?
Again?
No.
Well, I guess it isn't to be right now.
Check for any last read me.
But, and the folder structure may slightly change.
These are all just early working folders.
I think, Fonds underneath research, underneath methods, underneath one, this might be a good
source for longer reference to like grants and to structure that better.
But already in the research methods folder, this is where all the grants methods are.
But that's kind of grant methods 1.0.
So we can make it kind of grant methods 2.0, field shift, plus, plus, plus, field shift 3.
And that would maybe with more flexibility, like select a prompt, select the entity combination,
maybe select the order.
And then we could just, we could get rolling on, on many fronts.
Whereas actually like, you know, in its own meta way, this was manual with heavy augmentation
for a lot of all by all considered as text files, but, but, but structurally manually derived.
So it could be distilled and improved.
Okay.
I'll just wait one more minute to read anything people write while I end the stream, push the
github.
So, it's, it's going to be a active project at the Institute for the active Infraant project.
So people can contribute asynchronously with questions, issues, documentation on the Coda pages
in the github.
If someone wants to work on this or integrate it with some other way, please just contact me.
We can figure out the right Institute related or, or just other arrangements and add a bunch
of pieces to all of this.
And just part of the beauty of the, the code and the open source system is like it, it hopefully
can ratchet the function.
Like this doesn't do it all, but now this is a starting point and the outputs, even if you
don't run any code at all in the github, you can still see the outputs.
So I'll push it.
We'll look at the github final and push.
So, prepare methods research field shift to everything's in here inputs outputs, shift
to dissertations.
And then, you can see the graph, you know, just whatever you want to search for.
Like it'll search on both sides.
Blake to neuroscience.
Here it is.
Translated dissertations.
Sanskrit.
Here it is.
I don't know.
Cool.
All right.
Thank you.
Upcycle.
Thank you.
Mills 181 80.
Thank you.
Mills 8102.
Thank you, Andrew.
Yeah.
All right.
Well, we're live.
The calls go on.
So I hope people who are interested share it and the repo and the video and let's do
infra ant streams to develop so many of these fractal functionalities of this repo that has
long been in the institute's domain.
Andrew wrote, wondering if a separate 10-ish minute setup tutorial on how to reproduce the
cursor Python GitHub integration would be helpful for others to contribute.
Yeah.
Yeah.
Great suggestion.
Like make the issue on the GitHub and then I'll make it an issue and then we'll get to
it.
Cool.
All right.
Thank you.
Bye.
Bye.
Bye.
