## Intro
This webcast is intended to address some issues you guys have been having with the "Code Your Own Quiz" Project
By the end of this webcast, you will have an idea of how to approach not only the programming problem posed by Stage 2,
but all programming problems of varying difficulty.

## Where do most students fail?
Here are the top five reasons submissions don't pass for this project:

- not enough comments for inputs and outputs
- not using functions for repeated tasks
- 18 lines of code or longer
- prompt users to try again
- print the quiz after you've replaced the blank

The commonality one notices here is confusion about functions. So today we're going to be talking about functions.

## How to think about the task you are being asked
The point of this project is to get you thinking about how to abstract away big parts of what you're being asked so you know where to begin. Let's look at a problem. Say that our problem looks like this:

1) Show a user three different people drinking coke.

Sufficiently ambiguous, right? Let's break down the problem!

What does "show" mean? Well, because there are sometimes no one we can ask, we have to make a reasonable assumption about what is meant, and try to move forward like that. Let's assume that "Show" means "print."

What does "three different people" mean? Let's assume these are strings too. Then what we're tasked with is just printing
out the words "So-and-so drinks coke."

# Commenting
After you've broken down the problem logically, the first thing you want to do is write what you want to do in comments in your coding workspace:

```python
# have the three people we want to print ready to be printed

# take in first person, print first person drinking coke

# take in second person, print second person drinking coke

# take in third person, print third person drinking coke
```
Here we've got the basic set up of our function! Notice that we've done two things:

- we've noted what our function needs to, well, function and
- what you figure has to change over the course of the function

```python
# have the three people we want to print ready to be printed
person1 = "Susie"
person2 = "Rahul"
person3 = "Anthony"

# take in first person, print first person drinking coke
def susie_drinks_coke(person1):
	print "Susie drinks coke"

# take in second person, print second person drinking coke
def rahul_drinks_coke(person2):
	print "Rahul drinks coke"

# take in third person, print third person drinking coke
def anthony_drinks_coke(person3):
	print "Anthony drinks coke"

susie_drinks_coke(person1)
rahul_drinks_coke(person2)
anthony_drinks_coke(person3)
```

## Taking the Problem Apart (Abstraction)

Does anyone see the problem in programming this way? One thing we should have done after breaking down what was being
asked of us is trying to group together our checklist of things to do **in as few tasks as possible**.

What do I mean by this? Well, consider that one of our tasks is "showing" and the other is "showing three different people."
So one thing I want to do is print out three different people, but using a minimal amount of code. To do this, I stop thinking about printing *three* people drinking coke and start thinking about printing *a* person drinking coke; that is,
how do I print just a single person? I do this with the belief that once I find a way to do this task for a person, it's
just a matter of doing this thing for `x` number of times.

```python
# have the three people we want to print ready to be printed
person1 = "Susie"
person2 = "Rahul"
person3 = "Anthony"

def drinks_coke(person):
	""" Takes as input a person (string) and prints that person drinking coke"""
	print person + " drinks coke"

drinks_coke(person1)
drinks_coke(person2)
drinks_coke(person3)
```

So here we did several things:

- we abstracted parts of the problem to make it easier to understand how we can code it
- by doing this we avoided repeating ourself in the future
- we prevented the development of really long code from the very beginning
- we prevented repeating ourselves by reducing the complexity of the logic of our code
- we refined our comments and put them in triple quotes

Alternatively, if you're having trouble breaking down a problem in this fashion, you could also just
start coding the parts that you understand, and then take a look at what you wrote, identifying the parts
that essentially are doing the same things -- like having three functions that print out three different
people drinking coke.

## Lessons to take from this example
- think about a level in the abstract sense, not three levels. Remember that the 'sample' you're given is an example of a 'level'
- identify what needs a function after you've broken down the task you're faced with
- make sure to group tasks that seem like they're doing the same thing, like repeatedly asking your user for something or printing something multiple times

## Other tips
- I don't suggest the use of the "mad libs" code exactly for this project (that is, going every couple of indices) -- the goal is to adapt the *concept*
- lines of code from this exercise add up -- try to use replace, which removes all instances of the words to be replaced
inputs and outputs

