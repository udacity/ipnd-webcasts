List Comprehensions and Generators
===

# Introduction

This Webcast session will be about list comprehensions -- a faster, cleaner-looking way to generate iterable structures like lists and dictionaries -- as well as iterators, known in python as generators.

List comprehensions are used in Stage 4 and Stage 5 to generate complex lists. You will find them all over the place in your career developing in python; it's a useful syntax to get accustomed to and try out on your own.

At the end of the Webcast session, we will understand:

* How list comprehensions can be used to quickly generate iterable structures
* How to use generators and the yield statement to create a "disposable", iterable data structure

TECHNICAL NOTE: In the webcast it was said that tuples and generators are iterable data structures -- this is not true of an individual tuple and not true in the technical sense of a generator. What was meant is a list of tuples is an iterable structure, and that the elements of a generator can be traversed at most once as an iterator. If these terms don't make sense to you yet, keep reading!


# What is a List Comprehension?

A list comprehension is best understood by demonstration. Imagine that you are trying to fill a list with the numbers 0 through 9. Using a for-loop, the most efficient way to do this would be:

```python
# for-loop demonstration
numbers = []
for i in range(10):
  numbers.append(i)
```
This same list can be built using a list comprehension:

```python 
# list comprehension demonstration

numbers = [i for i in range(10)]
```

Wow! We just turned a three-line chunk of code into one! You can test out the two different techniques in your python console and see that you get the same value for `numbers` in each case. Let's break down what's going on here:

* furthest to the left is the name of the variable we store the result of the list comprehension into: `numbers`

* the square brackets ( [ ] ) are the usual syntax we use to indicate an empty list. By having the for-loop inside the square brackets, we are basically telling python "whatever the result of this for-loop is, it should go into a list"

* the `i` furthest to the left within the square brackets is the variable that we are telling python to store in the list we are building. We can manipulate the value of whatever `i` is to how we would like to add it to the list -- we can store `i-1`, `i**2`, even store `i` into a list like this `[i]` to create a list of lists!

* We don't need to use `i` per se -- `i` is just the variable name we give for the element that we are looking at in the for-loop, which is exactly the same syntax as it always is. We coul have also use `num` or `integer` or any name you want!

What we CAN'T do is try to execute a statement that does an I/O operation on the `i` furthest to the left -- for example, we can't have something like:

```python
# this will result in syntax error
numbers = [print(i) for i in range(10)]
```
We also CAN'T do variable assignment within a list comprehension:

```python
# this will result in syntax error
numbers = [i+=4 for i in range(10)]
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
We can also add conditionals to our list comprehensions. To add a conditional to our for-loop, we tack it on to the end. See this example that creates a list of even numbers using the modulus operator (%). If you have never seen the modulus operator before, just think of it as the "remainder operator," like the remainder resulting from the division of one number by another.

```python

# store only even numbers
# numbers are even when there are divisible by 2, that is, when they have no remainder
even_numbers = [i for i in range(10) if i%2==0]
```

If we want to make a double for-loop, or triple and so on, you can do that too! For every nested loop you need, just put them one after the other (but you must be careful: list comprehensions can become difficult to read when you have too much code in them):

```python
multiple_nums = [j for i in range(3) for j in range(10)]
```
and if you would like a conditional, just tack it onto the end of the for-loop that is associated with it. 

```python
# use of multiple conditionals
testing = [j for i in range(3) if i < 2 for j in range(10) if j > 5]
>>> testing
[6, 7, 8, 9, 6, 7, 8, 9]
```

Moreover, you can make a list comprehension within a list comprehension: 

```python
multiple_num_lists = [[j*i for i in range(3)]for j in range(10)]
>>> multiple_num_lists
[[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6], [0, 4, 8], [0, 5, 10], [0, 6, 12], [0, 7, 14], [0, 8, 16], [0, 9, 18]]
```
Try out other examples in your favorite python console and see what you get!

Here is a more complicated example that uses the power of list comprehensions to generate a list of primes from 0 to 50:

```python
# a list of non-prime numbers:
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]

# list of primes
primes = [x for x in range(2, 50) if x not in noprimes]
```

## Dictionary Comprehensions and Tuples

NOTE: If you haven't seen dictionaries yet, you can skip this section. If you're interested in learning, check out the "Using Dictionaries in Python" webcast in Stage 2.

The syntax for creating a dictionary using a comprehension is identical to that of a list comprehension, except for the syntax that tells python we are using a dictionary -- namely, curly brackets ( { } ). Say that we want to create a dictionary where the key in each dictionary is a number from 0 through 9 (as we have been doing), and each key has a value that is a string representation of the integer. So one element of the dictionary would be `1: '1'`:

```python
num_dict_comp = {i:'%s' % i for i in range(10)}
```

If you haven't seen the colon syntax yet, `i:'%s' % i` means the key (on the left of the colon) is `i` and the value (on the right of the colon) is `'%s' % i`, which is a string representation of the integer `i`. We can also traverse `num_dict_comp` in the same way we would in a normal for-loop. If we want to create a list of tuples with `num_dict_comp`, we could do it like this:

```python
num_dict_unload = [(k,v) for k,v in num_dict_comp]
```
where `k,v` stands for each 'key' and 'value' pair in the dictionary, num_dict_comp. All the same rules regarding conditionals and multiple for-loops apply the same here as it did for lists.

# Generators and the `yield` statement

So far in your python education you have come across a variety of different data structures including lists and dictionaries. Each of these data structures are known as iterable structures, meaning we can go through each element one-by-one.

Another type of data structure that list comprehensions allow us to introduce are generators. Generators are a type of iterable data structure that can only be traversed once (in other programming languages, generators are often called iterators). Here's an example:

```python
num_generator = (i for i in range(10))
```
Notice that the syntax is precisely the same as that of list comprehensions, save for the parentheses instead of square brackets. (The use of parentheses may seem confusing considering tuples have the same syntax; just remember that tuples ALWAYS have a comma in the parentheses that separate the variables.) The parenthetic syntax wrapping a list comprehension is how a generator is created. However, if you attempt to print the generator `num_generator`, you will not see the contents of the generator, but some odd expression like this:

```<generator object <genexpr> at 0x10afb8e60>```

You don't need to worry about this too much; just know that your generator is stored in a different part of your computer than your list would be stored. In versions of Python prior to v.3, this characteristic would help items in generators be accessed faster than in lists; following Python3, both lists and generators are equally fast to access, though generators still take less memory.

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

Printing out `result`, we see can see the contents of the generator unloaded as a list comprehension, and stored in `result`. However, if we attempt to unload `num_generator` after doing so once already, we see that result is an empty list.

## Creating Generators Using `yield`

Generators do not necessarily have to be created by comprehensions. Another way to create a generator is to utilize the `yield` keyword. You can think of `yield` as a type of `return` statement in a function, but allowing you to return many elements -- one at a time -- in a loop, ending when the loop ends. For example:

```python
def return_gen():
  for i in range(10):
    yield i

# assign the result of the function to a variable
numbers = return_gen()
num_list = [num for num in numbers]
>>> num_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Unlike a `return` statement, `yield` does not break the for-loop and exit out of the function. Instead, `i` is returned until the condition in the for-loop is satisfied. This means when there are no more elements left in `range(10)`. However, if you choose to use a `yield` in your function, you cannot also have a `return` statement somewhere in your code. If you are creating a generator, then using a `yield` statement is the fastest way to go.

# Summary

A comprehension is an elegant way to create lists, lists of tuples, dictionaries, and generators. However, they do have some minor faults:

* variable assignment and I/O functions cannot be made within a comprehension
* depending on your familiarity, list comprehensions can be difficult to read, especially when you have several for-loops in one comprehension 
* list comprehensions are faster than regular looping mechanisms, which is an important consideration when you need to scale your program. But not the fastest. See the python module `itertools` for a faster, albeit more abstracted solution to iteration

You may have been wondering what we mean by "fast" or "speed" in a computer program. When we say "fast," we mean the actual speed in real time that it takes to finish a computation, usually measured by the cycles of effort the CPU in the computer undergoes to complete a task (the fewer the better/faster). Generally when we code we try to write programs that are first readable, then fast (consuming the minimal amount of CPU power), then space-efficient (consuming as little RAM, or working memory) as possible. As you continue your programming career, the resources available to you will become a concern whether you are making a server-side web application or a mobile application for your phone. List comprehensions are one of the many tools that will help you build cool projects efficiently and elegantly. Happy coding!


