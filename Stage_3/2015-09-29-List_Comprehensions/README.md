List Comprehensions and Generators
===

# Introduction

This Webcast session will be about list comprehensions -- a faster, cleaner-looking way to generate iterable structures like lists and dictionaries, and iterators -- known in python as generators.

List comprehensions are used in Stage 4 and Stage 5 to generate complex lists. You will find them all over the place in your career developing in python, so it is definitely a useful syntax to get accustomed to and try out on your own.

At the end of the Webcast session, we will understand:

* How list comprehensions can be used to quickly generate iterable structures
* How to use generators and the yield statement to create a "disposable", iterable data structure
* Why speed and memory efficiency are desirable to have in code, balanced with code readability

TECHNICAL NOTE: In the webcast it was said that tuples and generators are iterable data structures -- this is not true of an individual tuple and not true in the technical sense of an iterable structure. What was meant is a list of tuples is an iterable structure, and that the elements of a generator can be traversed at most once. 


# What is a List Comprehension?

A list comprehension is best understood by demonstration. Imagine that you are trying to fill a list with the numbers 0 through 9. Using a for-loop, the most efficient way to do this would be:

```python
# for-loop demonstration
numbers = []
for i in range(10):
  numbers.append(i)
```
This syntax is the most efficient way that we currently know of to add things to a list in python. This same list can be built using a list comprehension:

```python 
# list comprehension demonstration

numbers = [i for i in range(10)]
```

Wow! We just turned a three-line chunk of code into one! You can test out the two different techniques in your python console and see that you get the same value for `numbers` in each case. Let's break down what's going on here:

* furthest to the left is the name of the variable we store the result of the list comprehension into: `numbers`

* the square brackets ([ ]) are the usual syntax we use to indicate an empty list. By have the for-loop inside it, we are basically telling python "whatever the result of this for-loop is, it should go into a list"

* the `i` furthest to the left within the square square brackets is the variable that we are telling python to store in the list we are building. We can manipulate the value of whatever `i` is to how we would like to add it to the list -- we can store `i-1`, `i**2`, even store `i` into a list like this `[i]`!

* We don't need to use `i` per se -- `i` is just the variable name we give for the element that we are looking at in the for-loop, which is exactly the same syntax as it always is. 

What we CAN'T do is try to execute a statement that does an I/O operation on the `i` furthest to the left -- for example, we can't have something like:

```python
# this will result in syntax error
numbers = [print(i) for i in range(10)]
```

But we CAN call a function that manipulates `i` and then sends it back to be stored in the list. For example, this is perfectly valid code:

```python
# this function prints the number, x, and returns it with 1 added to it
def print_and_add_one(x):
    print x
    return x+1

# this code will not result in a syntax error
numbers = [print_and_add_one(i) for i in range(10)]
```
We can also add conditionals to our list comprehensions. To add a conditional to our for-loop, we tack it on to the end. See this example that creates a list of even numbers using the modulus operator (%). If you have never seen the modulus operator before, just think of it as the "remainder operator", like the remainder resulting from when you divide some number by another.

```python

# store only even numbers
# numbers are even when there are divisible by 2, that is, when they have no remainder
even_numbers = [i for i in range(10) if i%2==0]
```

If we want to make a double for-loop, or triple and so on, you can do that too! For every nested loop you need, just put them one after the other (but you must be careful: list comprehensions can become difficult to read when you have too much code in them):

```python
multiple_nums = [j for i in range(3) for j in range(10)]
```
and if you would like a conditional, just take it onto the end of the for-loop that is associated with it. Moreover, you can make a list comprehension within a list comprehension: 

```python
multiple_num_lists = [[j*i for i in range(3)]for j in range(10)] 
```
Try these out in your favorite python console and see what you get!

Here is a more complicated example that uses the power of list comprehensions to generate a list of primes from 0 to 50:

```python
# a list of non-prime numbers:
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]

# list of primes
primes = [x for x in range(2, 50) if x not in noprimes]
```

## Dictionary Comprehensions

The syntax for creating a dictionary using a comprehension is identical to that of a list comprehension, but the syntax that tells python we are using a dictionary -- namely, cruly brackets ({ }). Say that we want to create a dictionary where the key in each dictionary is a number from 0 through 9 (as we have been doing), and each key has a value that is a string representation of the integer. So one element of the dictionary would be `1: '1'`:

```python
num_dict_comp = {i:'%s' % i for i in range(10)}
```

If you haven't seen the colon syntax yet, `i:'%s' % i` means the key (on the left of the colon) is `i` and the value (on the right of the colon) is `'%s' % i`, which is a string representation of the integer `i`. We can also traverse the dictionary we just created in the same way we would in a normal for-loop:

```python
num_dict_unload = {k:v for k,v in num_dict_comp}
```
where `k,v` stands for each 'key' and 'value' pair in the dictionary, num_dict_comp. (Here we are just recreating the dictionary we are unloading, `num_dict_comp`) All the same rules regarding conditionals and multiple for loops apply the same here as it did for lists.

# Generators and the `yield` statement

So far in your python education you have come across a variety of different data structures including lists and dictionaries. Each of these data structures are known as iterable structures, meaning we can go through each element one-by-one.

Another type of data structure that list comprehensions allow us to introduce are generators. Generators are a type of iterable data structure that can only be traversed once (in other programming languages, generators are often called iterators). Here's an example:

```python
num_generator = (i for i in range(10))
```
Notice that the syntax is precisely the same as that of list comprehensions, save for the parentheses instead of square brackets. The parenthetic syntax wrapping a list comprehension is how a generator is created. However, if you attempt to print the generator `num_generator`, you will not see the contents of the generator, but some odd expression like this:

```<generator object <genexpr> at 0x10afb8e60>```

You don't need to worry about this too much; just know that your generator is stored in a different part of your computer than your list would be stored. In versions of Python prior to v.3, this characteristic would help items in generators be accessed faster than in lists; following Python3, both lists and generators are equally fast to access.

The thing to remember about generators and iterators in general is that you can only go through each element in the structure once. For example, say we traverse the generator from the previous example, `num_generator`, by emptying the contents of the generator into a list:

```python
# first time
result = [i for i in num_generator]
>>> result
[0,1,2,3,4,5,6,7,8,9]

#second time
result = [i for i in num_generator]
>>> result
[]
```

Printing out results, we see can see the contents of generator unloaded in the list comprehension, and stored in results. However, if after doing so we attempt to unload `num_generator` again, we see that result is an empty list.
