Air Date: 10/27/2015 [video][recording]

Functional Programming Concepts in Python
===

# Introduction

This Webcast session will be about functional programming in Python -- what it is and why you should use it! This is meant as an introduction to functions used in functional programming, but it is still a fairly advanced topic. I recommend using what you learn here only after you're comfortable writing programs in Python. 


By the end of this webcast, you will understand

- What Functional Programming is, and where you can find it
- Why it makes coding time shorter and reduces errors in code
- What the three main functions of functional programming are and how they work
- How lambda functions can be an alternative way to define a function

# What is Functional Programming
In practice, functional programming involves using a function the same way you would use a variable. That is, functional programming is when you can pass functions to other functions and you assign functions to variables.

## What's So Cool About It?
Companies like Facebook (their NewsFeed), Twitter (they use Scala), WhatsApp (they use Erlang), and many algorithmic trading companies use functional programming languages and concepts to develop their core services.

Every programming language today either contains functional programming concepts, or is having functional programming concepts added to it. If you take a look at code in a programming language like C or Assembly Language (Google it if you dare!), you'll see that programming has changed a lot. It's much easier to read and write the same programs we would write in C or Assembly in languages like Python and Ruby instead.

Faster processors and more memory in computers have enabled us to transition to modern languages, which are slower and have greater memory requirements. Modern langauges are able to abstract away the complex aspects of older languages, making them easier to read and write. (For an example of this, just see how difficult it is to reverse a string in C versus reversing a string in Python.) The popular languages of tomorrow will similarly replace the languages of today by abstracting away verbose, error-prone constructs. 

And functional programming is one way this is happening. Functional programming is being used to replace the need for loops, where code can often be difficult to follow and where errors in logic happen all the time. Understanding how these abstractions work and using them today will better prepare you for possible changes in programming in the future, and give you an edge in writing cleaner, less error-prone code. 

Today we're going to be talking about three specific functions that are the three central concepts of functional programming: the "map", "filter" and "reduce" functions. We'll also talk about the concept of lambda functions, which are also used (or can be created) in any language that employs functional programming.

## The Functions

Functional programming, unsurprisingly, involves passing a function and an iterable structure to another function. An iterable structure is just a list or dictionary. The function that is being passed in has to accept members of the list as input. The function accepting this input then applies the input function to each member of the input list. Let's demonstrate how this works using the most common functional programming procedure, ```map()```. 


### The `map()` function

```map()``` is the most common procedure in functional programming. All it does is take a function and applies it to each member of the input list (in some programming languages, ```map()``` is called ```apply()```). Let's look at an example. Suppose we are trying to multiply each element of a list by 5 and record the results. This is one way we could do this:

```python
l = [0,1,2,3,4,4,5,8]

new_list = []
for num in l:
	product = 5*num
	new_list.append(product)

>>> new_list
[0, 5, 10, 15, 20, 20, 25, 40]
```
Here we had to

- create a new list, which uses more memory
- call append on the new list, which slows the program
- use a for-loop, where we have to follow what goes on in each step to make sure we are correctly performing the steps

This is fine, but every time we come across a for-loop in our code, we have to figure out what is being done inside it. That is to say, a for-loop is almost like a function in itself; it just does the same computation over an iterable structure each time. For-loops make quickly reading code difficult because we have to slow down and understand what it is the for loop is doing for each cycle -- this is an opportunity to make our code more abstract. Let's see how we can do that.

```
l = [0,1,2,3,4,4,5,8]

def multiply_by_5(number):
	return number*5

l = map(multiply_by_5, l)
>>> l
[0, 5, 10, 15, 20, 20, 25, 40]
```
This is better because

- you're focusing more on results and less on steps
- the code is shorter (3 lines vs. 4 lines)
- we are separating the functionality more explicitly here from the iteration;
this makes it easier to see what happens to each member of the list `l` by considering just one case
- if we need to debug the code, we've already separated the problem area to inspect!
- we are reinforcing DRY principles because if we want to re-use this functionality, we would just repeat the call of this function! (Much easier than copying the functionality of a for-loop, no?)
- you're breaking apart your problems by functionality, which is an efficient method of planning out your program


What do you think this bit of code does? What is the result?

```python
l = [1,2,3,4,5]

def square(num):
	return num**2

>>> map(square, l)
???
```

### The `filter()` function

This is filter

* takes a function and a list
* the function has to return some boolean on each member of the list
* returns a list containing only elements of the input list that satisfy the boolean condition

```python
def is_even(num):
	if num % 2 == 0:
		return True

l = [0,1,2,3,4,4,5,8]
new_list = []
for num in l:
	if is_even(num):
		new_list.append(num)
>>> new_list
[0,2,4,4,8]

l = filter(is_even, l)
>>> l
[0,2,4,4,8]
```

### The `reduce()` function
This is reduce (JavaScript, Python) aka fold (Haskell, Lisp) aka inject (Ruby)

* takes a function and a list
* Reduce works as follows: take the first two elements; apply them to the operator, to get a single result; apply this result and the next element to the operator, to get a new result; and repeat, until there are no elements left, and you get a single final result.
* So returns one element

```python
l = [0,1,2,3,4,4,5,8]

def greater(a,b):
	if a > b:
		return a
	else:
		return b

# the normal way
greatest = 0
for num in l:
	greatest = greater(num, greatest)	

>>> greatest
8

# using reduce
greatest = reduce(greater, l)
>>> greatest
8

```

### An Application: Google MapReduce technology
Google has made a lot of money off of a service that employs the concepts of `map()` and `reduce()`, known fittingly as MapReduce. The service is used to process computationally heavy programs by using multiple computers around the world to do a small part of the computation, and then combine the results of each computation until we arrive at one answer. 

Anthony, can you see how the `map()` and `reduce()` function are being used here?

## The Main Benefits of Functional Programming

* As Neal Ford of IBM puts it: "functional programming enables us to replace other core building blocks with higher-order abstractions, and to focus more on results than on steps"

- Shifts the programming paradigm to focusing on processing just one element in a collection of data, instead of the whole collection

- Debugging is simplified because functions are generally small and clearly specified. 

- A more practical benefit of functional programming is that it forces you to break apart your problem into small pieces.

- The concept of DRY and Abstraction are reinforced using functional programming

## Lambda functions

* "mini" functions that can be assigned to variables, and then variables can be used in functions
* some people call them "anonymous" functions
* using "sorted" in the context of lambda functions

```python
# traditional add_one function
def add_one(x):
	sum = x + 1
	return sum

>>> print add_one(4)
5

# the same function using a lambda expression
add_one_lambda = lambda x: x+1
>>> print add_one_lambda(4)
5

```

The `x` as used in the lambda function is used exactly the same way as `x` in the normal function. The `:` separates the input variable declaration from what's done with the variable. In this case, what's done with the variable `x` in the lambda expression is 1 being added to it and returned. 

[recording]: