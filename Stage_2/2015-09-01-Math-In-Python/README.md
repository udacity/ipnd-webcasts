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

So, if we have the number 1045 in binary, we would convert it like so:

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


def convert_to_binary(decimal_number):
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


1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
-----|-----|-----|-----|----|----|----|---|---|---|---
1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1

That gives a binary number of 10000010101

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


###How C impliments variables

#####int vs. long


#####float vs. double


###How Python impliments variables



##Numeric Types — int, float, long, complex
There are four distinct numeric types: plain integers, long integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of plain integers. Plain integers (also just called integers) are implemented using long in C, which gives them at least 32 bits of precision (sys.maxint is always set to the maximum plain integer value for the current platform, the minimum value is -sys.maxint - 1). Long integers have unlimited precision. Floating point numbers are usually implemented using double in C; information about the precision and internal representation of floating point numbers for the machine on which your program is running is available in sys.float_info. Complex numbers have a real and imaginary part, which are each a floating point number. To extract these parts from a complex number z, use z.real and z.imag. (The standard library includes additional numeric types, fractions that hold rationals, and decimal that hold floating-point numbers with user-definable precision.)

Numbers are created by numeric literals or as the result of built-in functions and operators. Unadorned integer literals (including binary, hex, and octal numbers) yield plain integers unless the value they denote is too large to be represented as a plain integer, in which case they yield a long integer. Integer literals with an 'L' or 'l' suffix yield long integers ('L' is preferred because 1l looks too much like eleven!). Numeric literals containing a decimal point or an exponent sign yield floating point numbers. Appending 'j' or 'J' to a numeric literal yields a complex number with a zero real part. A complex numeric literal is the sum of a real and an imaginary part.

Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “narrower” type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex. Comparisons between numbers of mixed type use the same rule. [2] The constructors int(), long(), float(), and complex() can be used to produce numbers of a specific type.

All built-in numeric types support the following operations. See The power operator and later sections for the operators’ priorities.

All built-in numeric types support the following operations. See The power operator and later sections for the operators’ priorities.

##Priority Levels



##Operators
Python has all of the standard 
```python
print 1 / 2
print 1//2
#>>>0
#>>>0
print 2 / 2
print 2//2
#>>>1
#>>>1
print -1/ 2
print -1//2
#>>>-1
#>>>-1
print -3 / 2
print -3 // 2
#>>>-2
#>>>-2
print -3.0 // 2
print -3.0 / 2
#>>>-2.0
#>>>-1.5
```

Operation	Result	Notes
x + y	sum of x and y	 
x - y	difference of x and y	 
x * y	product of x and y	 
x / y	quotient of x and y	(1)
x // y	(floored) quotient of x and y	(4)(5)
x % y	remainder of x / y	(4)
-x	x negated	 
+x	x unchanged	 
abs(x)	absolute value or magnitude of x	(3)
int(x)	x converted to integer	(2)
long(x)	x converted to long integer	(2)
float(x)	x converted to floating point	(6)
complex(re,im)	a complex number with real part re, imaginary part im. im defaults to zero.	 
c.conjugate()	conjugate of the complex number c. (Identity on real numbers)	 
divmod(x, y)	the pair (x // y, x % y)	(3)(4)
pow(x, y)	x to the power y	(3)(7)
x ** y	x to the power y	(7)


##Computational Efficiency

###O(n)






##Good References:
https://docs.python.org/2/reference/expressions.html#
https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex

##Summary


[recording]: https://plus.google.com/
[code1]: 
[code2]: 
