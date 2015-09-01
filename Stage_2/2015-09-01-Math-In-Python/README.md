# Webcast: Math in Python


## Webcast Recording

Here is the link to the [video][recording]
Here are links to [Luke's Code][code1] and [Michael's Code][code2]


##Nature of Computing (It's base 2)
Today we are going into using Python for Math and Computation!  Before we get into more advanced details, it is very useful to go back to basics and find out how computation of any kind is done.  

In any computer, every form of data is fundamntally stored in Binary:  1 or 0, True or False, On or Off, electricity flows through a transistor or it doesn't.  This means that numbers are going to be stored in base 2, and any mathematical operations are going to need to be run in base 2!


###Base 2 examples
We should probably start on how to convert from base 10 to base 2.

In decimal, you can divide a number into it's 1's place, 10's place, 100's place, 1000's place, etc., like so:

The number 1045 would be composed of 5 1's, 4 10's, 0 100's, and 1 1000's.

Similarly, binary numbers are divided into powers of 2:  2^0, 2^1, 2^2, etc.  The powers of 2 would be as such:

2^x | Decimal Value
----|----
2^0 | 1
2^1 | 2
2^2 | 4
2^3 | 8
2^4 | 16
2^5 | 32
2^6 | 64
2^7 | 128
2^8 | 256
2^9 | 512
2^10 | 1024

So, if we convert the decimal number 1045 to binary, we would convert it like so:

```python
# #(using integer division)
# 1045 / 1024 = 1
# 1045 % 1024 = 21
# 21 / 512 = 0
# 21 / 256 = 0
# 21 / 128 = 0
# 21 / 64 = 0
# 21 / 32 = 0
# 21 / 16 = 1
# 21 % 16 = 5
# 5 / 8 = 0
# 5 / 4 = 1
# 5 % 4 = 1
# 1 / 2 = 0
# 1 / 1 = 1
```

1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
-----|-----|-----|-----|----|----|----|---|---|---|---
1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1

That gives a binary number of 10000010101

```python
#We havent' gone over Python operators, but this 
def convert_to_binary(decimal_number):
    "Converts a decimal number to a binary number; binary number is returned as a list.
    needed_binary = []
    current_power = 0
    #Find how many bits we need
    while 2**current_power <= decimal_number:
        needed_binary.append(0)
        current_power += 1

    #Follow the same algorithm we did above
    for e in range(len(needed_binary)):
        current_power -= 1
        needed_binary[e] = decimal_number / (2**current_power)
        if needed_binary[e]:
            decimal_number = decimal_number % (2**current_power)
    return needed_binary

#Test it out
for i in range(16):
    print i, convert_to_binary(i)
```

Counting in Binary:

Binary | Decimal
-------|-------
0000   | 0
0001   | 1
0010   | 2
0011   | 3
0100   | 4
0101   | 5
0110   | 6
0111   | 7
1000   | 8
1001   | 9
1010   | 10
1011   | 11
1100   | 12
1101   | 13
1110   | 14
1111   | 15

Each of the binary numbers above are expressed in 4 bits; that is, the numbers are defined by four 1's and 0's.  A computer actually works not in bits, but in bytes!  Instead of a a single 1 or 0, a byte will be defined by ***8***  1's or 0's, like so:

```
00000000
00000001
00000010
...
10101010
...
11111111
```

While a single bit can be only one of two possible values, n bits can hold one of 2^n possible values!  This means a byte can hold 2^8, or one of 256 possible values.  While this may be sufficient to hold an ANSI character, it is a fairly small range of numbers to be held by an integer.  This is why C, the language which Python is typically built in, typically has an integer defined as 4 bytes; 4 bytes can hold 2^32 (4294967296) possible values!


#####What happens if you give an integer a value beyone what it can hold?
Well, what happens if you add 1 to 11111111 in binary?  You should be getting 100000000, however, you don't have the memory set aside to get this result!  Instead, you will end up cutting off the first digit, giving you 00000000 !

C actually has several numerical types for this reason.

###Int vs. Float
We have so far dealt with only integers, which have a straightforward mathematical conversion.  What happens if we want to include a decimal point, creating non-integer numbers?  This is done with something called a 'float'; in C, this also takes 4 bytes of memory.  

In C, there are also types which are identical, except that they take up more memory; these would be 'long' for ints and 'double' for floats!

###How Python impliments variables
Python is generally written in C, and its numerical types are based of off C's.  The respective memory specifications are differnt, however; a Python int is a C long, while a Python float is a C double!  Python also has a 'long' data type; similar to in C, it is an integer type.  However, in Python, because of the way 'long' is written, it actually can take an unlimited number of possible values!  Of course, your machine has actual limits to how much memory it can hold and access, so it isn't truly unlimited, but it does provide a very useful type for solving math problems with very large numbers, similar to the kind you might find at [Project Euler](https://projecteuler.net).

There is also a complex variable types in Python! Simply adding a lowercase or capital 'j' (or 'J') will give you a complex literal.

```
a_number = 12 +2j
print a_number
#>>>(12+2j)
```
It follows the rules any complex number would:

```
a_number = 12 + 2J
another_number = 5
a_thrid_number = 1j

x = a_number + another_number
print x
#>>>(17+2j)

y = a_number + a_thrid_number
print y
#>>>(12+3j)
z = a_thrid_number*a_thrid_number
print z
#>>>(-1+0j)
```

One big thing in Python; whenever you mix types, the result will be of the "wider" type.  From the Python Docs:
"Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “narrower” type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex. Comparisons between numbers of mixed type use the same rule. "

What this means is that if you add (or subtract, or multiply, divide, take the power of, etc.) an int and a float, your result will be a float.  The int will actually be converted to a float before the calculation is done!


##Operators
Python has all of the standard mathematical binary operators:
(Here, a binary operator is one that takes two arguments).

The '+' sign does exactly what you expect it to do; it adds two numbers together.  
The '-' sign does exaclty what you expect it to do as well; it subtracts one number from another to find the difference.
The '*' sign again does what you probably expect it to do; it multiplies to numbers together, resulting in a product.

However, '/' does *not* do what you expect it to do.  

If one or both of the numbers is a float (floating point number), it divides the two of them together in a normal fasion.

However, if both of the numbers are ints (integers), then the '/' sign does something called *integer division*.  Integer division always results in an integer, even if the divisor (i.e. the denominator) is not evenly divisible by the numerator.  Instead, the quotient in integer division is *rounded down*.  Integer division in Python is actually identical to floor division, which also has its own Python symbol ('//').

For instance:

```python
print 1 / 2
print 1//2
#>>>0
#>>>0
print 2 / 2
print 2//2
#>>>1
print 12 / 5
print 12 // 5
#>>>2
#>>>2
#>>>1

#Negative integer results are still rounded down (away from 0); they are not truncated.
print -1/ 2
print -1//2
#>>>-1
#>>>-1
print -3 / 2
print -3 // 2
#>>>-2
#>>>-2

#There is a difference between floor division and division when at least one number is a float, though:
print -3.0 // 2
print -3.0 / 2
#>>>-2.0
#>>>-1.5
```
#####Modulo
There is also another operator, %,  called the **modulo**. It is actually conceptually linked to integer division!  Think back to grade school, when you learned to do long division by hand.  If you were dividing 21 by 9, you would get 2 remainder 3, since 9*2 = 18, and 18+3 = 21.  Here, 21/9 using iteger division would give you 2, while 21 % 9 would give you 3, the remainder!  

#####Power
There are several built in ways to find x^n in Python as well.  The simplest would be to simply use two asteriscs:

```
x = 5
n = 2
print x**n
#>>>>25
```
This is completely identical to using the `pow()` keyword:

```
x = 5
n = 2
print pow(x, n)
#>>>>25
```

####Unary Operators
You can also have operators which take only one number as an argument; these would be called 'unary' operators.
You can take the absolute value of a number with the `abs()` keyword:

```
print abs(-5)
#>>>5
print abs(5)
#>>>5
```

As we've already been doing, you can add a `+` or a `-` sign before a number; the `-` sign will give you the negative of that number:

```
print -5
#>>>-5
print +5
#>>>5
```


####An overview on simple operators from the [Python Docs](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex):

Operation |	Result 
----------|--------
x + y |	sum of x and y
x - y | difference of x and y
x * y | product of x and y 
x / y | quotient of x and y
x // y | (floored) quotient of x and y
x % y | remainder of x / y
-x | x negated 
+x | x unchanged
abs(x) | absolute value or magnitude of x
int(x) | x converted to integer
long(x) | x converted to long integer
float(x) | x converted to floating point
complex(re,im) | a complex number with real part re, imaginary part im. im defaults to zero.	 
c.conjugate() | conjugate of the complex number c. (Identity on real numbers)	 
divmod(x, y) | the pair (x // y, x % y)
pow(x, y) | x to the power y
x ** y | x to the power y

##Priority Levels
Much like in math, there is an order of operations to Python!  In Python, this is called an operator's ***Priority Level***.  You can find a good resource on a ranking of Python's priority levels [here](http://www.tutorialspoint.com/python/operators_precedence_example.htm).

Python follows standard Math order of operations:

- Power (**) is the highest priority level.
- A negative sign (-) (or a positive sign (+) or compliment sign (~)) is the next highest
- Those things dealing with multiplication or addition are next (*, /, //, %)
- Addition (+) and subtraction (-) are next
- Python then reads from left to right, and things which are the same priority level are read on the left first.  However, the *right* side of assignment is computed before the *left* side of assignment, as you would expect, since you are assigning the left side the value of the right:

```
x = 5+4*0
print x
#>>>5
```

##Assignment Operators (=, %=, /=, //=, -=, +=, *=, **=)
As you are probably aware, asignment in Python is done with a single equal sign (=), while a test for equivalency is done with two (==).  You may not be aware that there are shortcuts for a variable preforming an operation on itself, though!

Any operator can let a variable preform an operation on itself if it comes before the equals sign.  For instance:

```python
some_variable = 1
#You are probably familiar with adding one two a variable as you use it as a counter in a loop:
some_variable = some_variable + 1

#You can do the *exact* same thing with less typing!
some_variable += 1  #(completely equivalent)
```
As a note; no matter what the operator being used, it will be the *last* operator applied; first, the computer will evaluate the complete expression to the right of the operator, then it will apply the operator to the variable it is assigning, and then it will assign the variable the result it gets.  For example

```python
print some_variable
#>>>
some_variable *= 2+5
print some_variable
#>>>21  #So... 2+5 = 7, some_variable was 3, 3*7 = 21
```

###Back to Decimal to Binary Conversion
Now that we know how operators work, lets go back and review the code I wrote to convert decimal numbers to binary numbers!
```python
#We havent' gone over Python operators, but this 
def convert_to_binary(decimal_number):
    "Converts a decimal number to a binary number; binary number is returned as a list.
    needed_binary = []
    current_power = 0
    #Find how many bits we need
    while 2**current_power <= decimal_number:
        needed_binary.append(0)
        current_power += 1

    #Follow the same algorithm we did above
    for e in range(len(needed_binary)):
        current_power -= 1
        needed_binary[e] = decimal_number / (2**current_power)
        if needed_binary[e]:
            decimal_number = decimal_number % (2**current_power)
    return needed_binary

#Test it out
for i in range(16):
    print i, convert_to_binary(i)
```


##Computational Efficiency
A very large idea in computer science is that of computational efficiency.  This is generally about two things; how long does it take to run a program, and how much memory does it take to run a program.  

While memory efficiency is still going to be considered, the RAM in modern computers far, far outstrips what most programs require.  For this reason, the time it takes to run a program is generally the chief concern when one optimizes a program to run efficiently.


###How to measure efficiency
Measuring how long it takes a program (or part of a program) to run is very simple in Python:

```
import time
start_time = time.time()
#Run the program you want to measure
total_time = time.time() - start_time
print total_time  #This will be in seconds
```

You'll notice that when you build a program in Sublime text, it actually prints this out for you!
Programs are generally not run on pre-determined inputs, though.  This is why the running time of a program is typically refered to in terms of the size of its input!

For instance, a frequent thing we do in programming is to go through a list:
```python
import random

#List comprehension to make a random list with 200 entries
some_list = [random.random() for x in range(200)]  

for x in some_list:
    print x
```
In this list, we will do that print statement once for every time we go through the list.  The number of 'basic' computations a program does in its complete running time is a good proxy for total running time; we can count each print statement and each move from one element of the list to the next as 1 computation for the sake of our own comparisons.

Let's compare this with two other things we could do while going through the list:

```python
y = 0
z = 0
for x in some_list:
    y += 1
    z += 2
    print x
```
Here, we'll do 4 things for every element of the list.

```python
for x in some_list:
    for y in some_list:
        print x
```

Here, if there are n elements in the list, we are suddenly doing n<sup>2</sup> computations!


###O(n)
We often categorize a particular program based on the infinite limit of how many computations it will preform when given a specific data set.  

This is frequently applied to accessing data from some data structure.  You are currently probably familiar with one of Python's most used data structures; the list.  Let's say we are searching a list for a particular value.  A list that has 10000 entries will take a for loop 10000 repetitions to go through, and the worst case senario is the value either is in the last entry or isn't in the list at all, so it is very possible that we have to take 10000 actions to find the value we want.  However, if you want to access the 100th entry, it doesn't matter how long the list is, it always takes the same amount of time to retrieve the 100th entry.  (This is true of any particular entry, even finding the last entry is only one computation.)

We would then say that retrieval is O(1), while search is O(n).  This is called big O notation.  


If you want to know more about O(n), efficiency, and data structures, take our [Intro to Algorithms course](https://www.udacity.com/course/viewer#!/c-cs215)!





##Good References:
https://docs.python.org/2/reference/expressions.html#
https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex

##Summary


[recording]: https://plus.google.com/
[code1]: https://plus.google.com
[code2]: https://plus.google.com


