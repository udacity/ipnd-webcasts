Recursive Functions in Python in 10 Minutes
======
####[Link to the video](https://www.youtube.com/watch?v=0Ii3mM-vgGE)
## Introduction

This Webcast will explain the main concepts of recursion and give some quick examples of how it can be used to solve problems.

## What is a Recursion

Recursion is a tricky thing to explain.

A procedure where the last step is the procedure itself. 

A more formal definition (from Wikipedia) is:
A process which contains
* A base case which defines the last step of a process.
* A set of rules that reduce other cases toward the base case

The Fibonacci sequence is an example of recursion. The base case is that the first two integers are 0 and 1. You can find the value of a given position in the sequence by adding up the numbers that precede it until you reach the first two of 0 and 1.

In terms of computer programming, a recursive function is created by calling the function you are defining inside the definition itself. Imagine you are trying to define the factorial function in Python. Which is N*(N-1)*(N-2)...*(1)
Imagine if you define it without using recursion.
```
def factorial(n):
    out = 1
    while n > 0:
        out = out * n
        n -= 1
    return out

print factorial(1) --> 1
print factorial(2) --> 2
print factorial(4) --> 4*3*2*1 = 24
```
This works, but let's try something a little neater

First the base case will be if we hit one. And then we will define the recursive step which includes our function.


```
def fact(n):
	if n == 0:
		return 1
	else:
		return n*(fact(n-1))
```
This function will keep calling itself until n becomes reduced to 1. 

For the average program, you might not find yourself using recursion, but if you are trying to build something that has a repetitive process built into it, then recursion is very useful. It's also commonly used in interviews. 