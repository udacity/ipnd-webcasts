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
```

1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
-----|-----|-----|-----|----|----|----|---|---|---|---
1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1

That gives a binary number of 10000010101

```python
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

##Priority Levels



##Operators
Python has all of the standard mathematical operators:

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
From the [Python Docs](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex):

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


##Computational Efficiency

###O(n)






##Good References:
https://docs.python.org/2/reference/expressions.html#
https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex

##Summary


[recording]: https://plus.google.com/
[code1]: https://plus.google.com
[code2]: https://plus.google.com


