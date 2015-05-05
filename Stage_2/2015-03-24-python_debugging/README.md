Office Hours: Introduction to Python Debugging
==========================================

Here is a link to the [Office Hours Video][OH]

#What We Will Learn

  - Work flow that will minimize debugging time
  - How to find a mistake using Python Traceback
  - How to find logic errors by checking the state of the program

##Effective Work Flow

Test Often!  For every small piece of code you write, test it immediately before moving on.  Try to write the smallest testable code you can manage for each step; it's good practice both for minimizing debugging time and for reusing code later!

##Using Python Traceback

When a Python program crashes, Python will tell you where your error is.  

For instance, running [debugging_demo.py]() without debugging it at all will produce this:

File "debugging_demo.py", line 67

    print ((["This is not a square matrix!")))
                                           ^
SyntaxError: invalid syntax

That tells you that on line 67, there is an error (specifically, invalid syntax), and the problem line is:

print ((["This is not a square matrix!")))

It is also possible for a traceback to give you the line *after* the error in the case of a line with something unclosed, like a missing quotation mark, parenthesis or bracket.  

Traceback also can give you where in the program the problem line is called from:

Traceback (most recent call last):

  File "debugging_demo.py", line 172, in <module>
  
    test()
    
  File "debugging_demo.py", line 166, in test
  
    if is_identity_matrix(matrix) != is_identity_matrix_actual(matrix):
    
  File "debugging_demo.py", line 85, in is_identity_matrix
  
    if not is_square(matrix):
    
  File "debugging_demo.py", line 66, in is_square
  
    if len(row) != len(column):
    
TypeError: object of type 'int' has no len()


Line 66 is the problem line here, in the function is_square.  This is from the time is_square() was called from is_identity_matrix() in line 85.  That function was called from function test() in line 166, which itself was called from line 172.  

##Checking the state of the program

When debugging a program, it is very useful to check the state of variables at various points in the execution of the program.  Scattering print statements to find out what the values of selected variables are will show you what the variable is at specific points in the program.  This can be used to compare what you think the variable states should be with what they actually are, allowing you to find errors.

##Process of Debugging

Remember to use the scientific method to find bugs in your code:

1.  Observe what is happening in your program by checking the state of the program in various places.

2.  Form a hypothesis as to what your program is actually doing (as compared to what you want it to do)

3.  Make and run tests to confirm or reject your hypothesis; fix your program if you now know what is causing the problem, or observe more of your program states if you do not.

[OH]: https://plus.google.com/u/0/events/centl78lqajmhq2erne9isecr74

