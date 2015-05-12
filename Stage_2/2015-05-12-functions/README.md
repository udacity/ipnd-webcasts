##What a Function / Procedure is in Python
Functions (which are identical to a procedures in Python) are bits of code which can be called repetatively.  Functions need to be defined before they can be used.

####Function Definiton
A Function is defined with a def statement:
```python
def some_function():
    #Some code the function runs goes here
```
Here, the funtion some_function() is defined.  All function definitions need to start with the word def, followed by the name of the function (some_funciton here), followed by parenthesis () which hold the parameters of the function (this function has no parameters), followed by a colol (:)

####Running the Function
What is inside the function definition is not run until the function is called.  A function is called like this:

```python
some_function()
```
A function is defined once, but can be called any number of times.

##Local Scope
When you define a function, any variables which are created inside of the function are destroyed when the function ends.  This is known as 'local scope'; this is contrasted with 'global scope', which is what a variable defined outside of any function would be.  Let's show an example of this:

```python
a = 6

def some_function():
    a = 5
    print "Function: " + str(a)

some_function()
print "Global: " + str(a)
```

We then get this for output:
Function: 5
Global: 0

The variable named 'a' inside of some_function is *completely unrelated to* the variable named 'a' in the global scope.

Let's take a deeper look at how scope works:

```python
a = 0

def some_function():
    print "Function: " + str(a)

some_function()
```
This produces:

Function: 0

Here, since 'a' is a *global* variable, we can access it inside of a function so long as we don't create a local variable of the same name before we access it.  We can't do the same thing in reverse, though:

```python
#a = 0  Commented this out

def some_function():
    a = 5
    print "Function: " + str(a)

some_function()
print "Global: " + str(a)

```
This produces:

Function: 5
Traceback (most recent call last):
  File "Test.py", line 8, in <module>
    print "Global: " + str(a)
NameError: name 'a' is not defined

Here, because the local variable a is destroyed as soon as the function finishes, Python doesn't know what 'a' is supposed to be when we access it in the global scope.

##Paramaters
A parameter is a value that can be passed into a function.  Any number of parameters can be passed into the function:
```python
def some_function(parameter_1, parameter_2):
    print parameter_1
    print parameter_2

some_function("Hello World!", 2)
#Prints:
#>>>Hello World
#>>>2
```
Here we passed in the string "Hello World!" to parameter_1 and passed in the int 2 to parameter_2.  

This can also be done with variables:
```python
def some_function(parameter_1, parameter_2):
    print parameter_1
    print parameter_2

a = 5
b = 2
some_function(a, b)
#Prints:
#>>>5
#>>>2
```

Something to note here; what happens to parameter_1 *does not* affect what a is unless a is *mutable*.


####Mutability (Mutable vs. Immutable values)
A Mutable value is one which can be altered, like lists, sets, and dictionaries.  (You'll be introduced to dictionaries later.)  

In order to understand mutability, you need a good understanding of variables.  In Python, a variable *points* to a value that it holds.  When you change an immutable variable, you change the pointer to point to a new value; however, with a mutable varaible, you can change the value that is being pointed to without changing the pointer.  You can see this here:

```python
>>> a = 5  
>>> id(a)
140311678477608
>>> a = 6
>>> id(a)
140311678477584
>>> a  = [1]
>>> id(a)
4337778272
>>> a.append(1)
>>> id(a)
4337778272
```

Immutable variables include int's, str's, floats, and tuples

As we already noted, with a immutable variable as a parameter to the function, what happens in the function *does not affect* what happens to the variable passed into the function.  That's not the case with an mutable variable; what happens to the variable inside of the function happens to the global variable passed in.

```python
def some_function(some_list):
    some_list.append(1)
    print "Local: " + str(some_list)

a = [1,2,3]
some_function(a)
print "Global: " + str(a)
#Prints:
#>>>Local: [1, 2, 3, 1]
#>>>Global: [1, 2, 3, 1]
```

##Return
So, if we want an immutable value back from a function, how will we get it?  We can *return* the value!  A return statement ends a function immediately, and returns the value given, like so:

```python
def some_function(some_value):
    some_value += 1
    return some_value

a = 5
x = some_function(a)

print a
print x
```
You can see that x now has the value returned from the function some_function().  This can be done withany type of varibale, mutable or immutable.

You can even return more than one value!

```python
def some_other_function(param1, param2, param3):
    x = param1+param2
    y = param2 * param3
    z = param1 / param2 ** param3
    return x, y, z

u, v, w = some_other_function(16, 2, 3)
print u, v, w
#>>>18 6 2
```
Techincally, you are returning a tuple here; you could assign it to a single variable:
```python
def some_other_function(param1, param2, param3):
    x = param1+param2
    y = param2 * param3
    z = param1 / param2 ** param3
    return x, y, z

u = some_other_function(16, 2, 3)
print u
#>>>(18, 6, 2)
```
You also don't need to assign the returned values to anything; you can either run the function and do nothing with the function or print what the function returns directly:

#####Using Return to end a function
```python
def some_function():
    print 1
    print 2
    return
    return 3

some_function()
#>>>1
#>>>2
```
#####Printing the returned value directly
```python
def some_function():
    return "Hello World!"

print some_function()
#>>>"Hello World!"
```

####Return vs. print
Notice here how print differs from return; print literally *prints* something to the console (meaning that it shows you the value in the place you run the program from), while return will literally return a value from a function to be used *outside* of that function.  If you don't print the value that your return at some point, you never see it, but the program keeps track of it.  On the other hand, printing something has no effect on the program state; it doesn't alter how the program runs beyond showing you some value.  

####None
With Python, if nothing is *explicitly* returned, a function will implicitly return None.  None is similar to null in other programming languages.  If you are interested, you can read more about None [here](http://www.pythoncentral.io/python-null-equivalent-none/)

This means these two pieces of code are functionally identical:
```python
def some_function(x, y):
    x.append(y)
```

```python
def some_function(x, y):
    x.append(y)
    return None
```



##Function vs. Procedure vs. Method
In mathematics, a function is somethig which maps some (unique) input to some output; for example, f(x) = mx + b.  In some programming languages, a function is something similar; it takes input (parameters), it gives output (from what it returns), and it effects nothing beyond taking input and giving output.  In contrast, a procedure would be something which runs code (and alters the program state of things outside of the procedure) but which doesn't return anything.  Python lacks such a distincting; functions and procedures refer to the same thing.  You can see this must be the case given what you know about functions / procedures: mutable variables can be altered in functions that explicitly return something (this is known as the function having *side effects*), and every function / procedure will implicitly return None even if we don't explicitly do it ourselves.  



