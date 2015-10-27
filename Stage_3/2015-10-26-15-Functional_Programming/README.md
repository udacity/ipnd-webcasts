Air Date: 09/29/2015 [video][recording]

Functional Programming Concepts in Python
===

# Introduction

This Webcast session will be about Functional Programming in Python -- what it is and why you should use it!
start creating script for 10/27 webcast: functional programming
What is functional programming

* "Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input."

* I like to think of functional programming in practice as using a function the same way you would use a variable. That is, you pass functions to other functions and you assign functions to variables.

Why should I use functional programming (Anthony)
*If you take a look at code in a programming language like C or Assembly Language (recommended if you're interested in how programming languages used to be like), you'll see that programming has changed a lot. It's much easier today to read and write the same programs we would write in C or Assembly in languages like Python and Ruby instead.

* The reason this has happened over time is because computers have gotten much faster and can store much more data than they could in the early days of computing, paving the way for the languages we use today, which are slower and have greater memory requirements than older languages

* The same thing is happening right now, today, in abstracting away the hard-to-read-and-write aspects of computer programming in Python, Java, and other languages; functional programming concepts and functions are being added to every programming language that exist today. 

* There is a huge trend in the mainstream for the functions we are going to talk about today to take care verbose chunks of code like for loops in the future. Being prepared for these abstractions and using them today will better prepare you for the future of programming and give you an edge over others by writing code more quickly.

* As Neal Ford of IBM puts it: "functional programming enables us to replace other core building blocks with higher-order abstractions, and to focus more on results than on steps"

* Today we're going to be talking about three specific functions that are the three central concepts of functional programming: "map", "filter" and "reduce." We'll also talk about the concept of lambda functions, which are also used in any language that employs FP.

map
*Suppose you have a function and want to apply the function to each element in a list
* takes a function and a list
* the function has to accept input of the type contained in the list
* returns a list of the changed elements of the list -- the input list and output list are the same size.
*why use this? (Anthony question)

filter
* takes a function and a list
* the function has to return some boolean on each member of the list
* returns a list containing only elements of the input list that satisfy the boolean condition
* why use this? (Anthony question)

reduce
* takes a function and a list
* Reduce works as follows: take the first two elements; apply them to the operator, to get a single result; apply this result and the next element to the operator, to get a new result; and repeat, until there are no elements left, and you get a single final result.
* So returns one element
* why use this? (Anthony question)

lamba functions?
* "mini" functions that can be assigned to variables, and then variables can be used in functions
* some people call them "anonymous" functions
* using "sorted" in the context of lambda functions


[recording]: