Webcast: Exploring Loops In Python
==========================================

Here is a link to the [video][OH]

#What We Will Learn

  - Understand what While loops and For loops are
  - How to setup a loop structure appropriately
  - Practice with some loop problems

# Loops: Why Are They Important?

Loops are the essential construct that lets us execute a series of instructions as many times as we want. Try to imagine a mundane job that we have done in real life, like stuff envelopes for a party. Wouldn't it be great to program a robot that stuffs our envelopes for us? We essentially provide the instructions to stuff one envelope and then tell the robot to repeat those instructions 500 times in order to stuff 500 envelopes.

That is the general idea of loops: we program a set of instructions for a computer to repeat a certain number of times.

# Setting Up Loop Structures

## While Loops

From the course, we setup a While loop structure like this:

```
while equality_expression is True:
  # Give instructions here until equality_expression is False
```

To be more concrete, a typical While loop is set up like this:

```
count = 0
while count < n:
   # Code more instructions here
   count += 1
```

This code tells us we will run our set of instructions n number of times, where n can be any positive number. If n equals 100, then we loop through our set of instructions 100 times.

Note how we added `count += 1` at the end of our loop. It's HIGHLY recommended that whenever we code a while loop, we first set up the structure and make sure that our count variable increases in value. This will help us avoid getting into infinite loops with While loops.

## For Loops

From the course, we setup a For loop structure like this:

```
for element in list_or_tuple_otherIterable:
  # Do more instructions here
```

The construct: `for element in list_or_tuple_otherIterable` tells us to iterate through each element in our list,tuple, or other iterable until we reach the end of this iterable.

For example if we have a list that equals = `[1,4,4,2,3,9,0]`, n will equal 1, 4, 4, 2, 3, 9, 0 in that order for each iteration. Let's try this out and print out what n will equal:

```
l = [1,4,4,2,3,9,0]
for n in l:
  print n
```

Notice how that we do not need to worry about incrementing any variable named `count` because by using this construct, we have told the For loop construct to end the loop once it has reached the end of the list.

If we simply want to iterate through a list of increasing numbers from 0 to 10, we can use the range() function. The range() function can take a number and return a list of values increasing from 0 to that number, exclusive, meaning that the list does not include the number that we are passing into the range() function.

`print range(11)` will equal `[0,1,2,3,4,5,6,7,8,9,10]`

Therefore a typical setup for a For loop can be:

```
for n in range(100)
   # Do instructions here 100 times
```

# Problem 1 - While Loops:

For this problem, we'll learn a basic technique to create a list of random numbers.

We first need to know how to create a random integer. To create a random integer from 0 to 10, we first import the random module

`import random`

We then print a random integer using the `random.randint()` function. For example:

`print "Random number generated: " + str(random.randint(0,10))`

We now want to create a list filled with random numbers. The list should be 
of length 20

```
random_list = []
list_length = 20
```

What we need to do: Use a While loop to populate this list of random integers.

# Problem 1 - Solution

## Breaking Down the Problem
We first need to understand what are the inputs and what are the outputs (or results) that we want to obtain.

The inputs are:

* An empty list
* A variable that has the value 20, telling us that we want to create a list of length 20

The output is:

* A list of random integers between 0 and 10 with length 20 that could look like:

   > [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
 
## What To Do

Therefore we want to generate a list of random integers given an empty list. One way is to use the append() method for lists and add in a random integer, 20 times. 

That's how a person would do it manually on pen and paper anyway. Let's see if we can write an outline of what to do if we were to do this manually on pen and paper:

<ol>
 <li>Generate a random integer between 0 and 10</li>
 <li>Add this random integer to our list</li>
 <li>Do we have a list of length 20 yet?</li>
 <li>If not, we loop back up and go through steps 1 to 3 again while length of the list is less than 20</li>
</ol>

If we translate these steps into real code, we can use a While loop that checks whether the length of the list is less than 20.

##Answer Code

```
random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))
```

Here's alternative code that simplifies the logic a bit if the above code is complicated to understand.

```
random_list = []
list_length = 20
count = 0

while count < list_length:
  random_list.append(random.randint(0,10))
  count += 1
```

# Problem 2 - For Loops 

This problem is taken from [Project Euler][PE]

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

> Find the sum of all the multiples of 3 or 5 below 1000.

# Problem 2 - Solution

## Breaking Down the Problem

We first need to understand what are the inputs and what are the outputs (or results) that we want to obtain.

The inputs are:

* All numbers below 1000 - this is the situation that we are given from the problem description above. We can interepret a situation given to us as an input.

The output is:

* A number that represents the sum of what multples of 3 or 5 that are less than 1000.

 
## What To Do

Let's break down what we want to do given our inputs and outputs and see if we can write an outline of what to do if we were to do this manually on pen and paper:

<ol>
 <li>Create a list of numbers from 0 to 999</li>
 <li>Go through each number in the list and see if the number is a multiple of 3 or 5</li>
 <li>If the number is a multiple of 3 or 5, we add this number to a running total that we have somewhere in our notes.</li>
 <li>If not, we step through the loop again and check the next number to see if it's a multiple of 3 or 5</li>
 <li>After the loop finishes, the running total would represent the sum of all multiples of 3 or 5 that are less than 1000
</ol>


##Answer Code

###Step 1: Create a list of numbers from 0 to 999

We can use the range() function and use: `range(1000)` to get this list

###Step 2: Go through each number in the list and see if the number is a multiple of 3 or 5

This involves us creating a For loop to steps through all of our numbers and checks whether the number is a multiple of 3 or 5

```
for n in range(1000):
   # Check if n is multiple of 3 or 5, add this number to current total
```

In order to check whether n is a multiple of any other number, we use the modulus operator `%` to get the remainder of a division between any two numbers. If a number is a multiple of another number, that means that the remainder equals to zero: `if n % 3 == 0 or n % 5 == 0` giving us this code:


```
for n in range(1000):
   if n % 3 == 0 or n % 5 == 0:  
```

###Step 3: If the number is a multiple of 3 or 5, we add this number to a running total that we have somewhere in our notes

We need to create another variable that keeps track of the running total. Let's define that variable as `total` and initialize this variable with the value of zero outside the For loop: `total = 0`. We simply increment this total by our current number if the number is a multiple of 3 or 5.

```
total = 0
for n in range(1000):
   if n % 3 == 0 or n % 5 == 0:  
     total += n
```

###Steps 4 to 5

Our For loop construct will take care of checking the next number in our list of a thousand numbers. At the end of the loop, `total` should equal **233168**

##Answer Code

```
total = 0
for n in range(1000):
   if n % 3 == 0 or n % 5 == 0:  
     total += n
     
print total
```

#Summary

Loops are basic building blocks of programming and are a powerful method to complete a series of instructions any number of times. This helps saves programmers a lot of time because programmers only need to program the instructions once.

The two loops in Python are While loops and For loops and both are constructed differently. For While loops, keep in mind that whenever we create a While loop, we should make sure that we guarantee a stopping point for our While loop or else the While loop will run our instructions forever - we call this an infinite loop. Most of the time, we want our loops to end in a finite amount of time.


[OH]: https://plus.google.com/events/cel50l7ao0k3qcfv2nicvailpgg?authkey=CIXpl6Te7KGITw
[PE]: https://projecteuler.net
