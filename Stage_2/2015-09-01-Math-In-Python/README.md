# Webcast: Math in Python


## Webcast Recording

Here is the link to the [video][recording]
Here are links to [Luke's Code][code1] and [Michael's Code][code2]

##Nature of Computing (It's base 2)

###Base 2 examples
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111




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
