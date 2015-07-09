# Webcast: Creating a Playable Tic-Tac-Toe game with Python

## Webcast Recording

Here is the link to the [video][recording]

##What We Will Learn
We will go over how to use Python to make a playable Tic-Tac-Toe game in this Webcast.
This will give us practice in these areas:
- Dividing a large problem into more easily solved pieces
- Using helper functions effectively
- Using `**kwargs` and named parameters to functions
- Getting input from a user from the Python terminal


###Using named parameters and unpacking parameters using `*` or `**`
Parameters can be passed into a Python function as either named or unnamed parameters.
As an example let's say we have a function like that defined below:


```python
def some_function(one_parameter, another_parameter, a_third_parameter):
    print "The parameter 'one_parameter' is equal to:", one_parameter
    print "The parameter 'another_parameter' is equal to:", another_parameter
    print "The parameter 'a_third_parameter' is equal to:", a_third_parameter
```
You are probably most used to passing in parameters to a function with unnamed parameters, like so:
```python
#We normally call functions with unnamed parameters
some_function(1,2,3)
#>>>The parameter 'one_parameter' is equal to: 1
#>>>The parameter 'another_parameter' is equal to: 2
#>>>The parameter 'a_third_parameter' is equal to: 3
```
With unnamed parameters, each parameter is given the value corresponding to the same order with which the parameters are listed in the functions call.

We can also do the same thing with named parameters, and the order won't matter:
```python
some_function(another_parameter = "another parameter", one_parameter = "1_parameter", a_third_parameter = "param 3")
#>>>The parameter 'one_parameter' is equal to: 1_parameter
#>>>The parameter 'another_parameter' is equal to: another parameter
#>>>The parameter 'a_third_parameter' is equal to: param 3
```
Here, each parameter is assigned based on its given *name*.

Essentially, the first method (unnamed parameters) is like passing in a tuple (or list) of parameters, and the second (named parameters) is like passing in a dictionary of parameters.
We can actually use actual tuples (or lists) and dictionaries to do the same thing!

Now, for unnamed parameters, we include a single `*` infront of the tuple (or list) to 'unpack' it, like so:
```python
some_list = [1,2,3]
some_function(*some_list)
#>>>The parameter 'one_parameter' is equal to: 1
#>>>The parameter 'another_parameter' is equal to: 2
#>>>The parameter 'a_third_parameter' is equal to: 3
```
We can do the same for named parameters with a dictionary, using two asterisks ( `**`) instead of one:
```python
some_dictionary = {"another_parameter" : "another parameter", "one_parameter" : "1_parameter", "a_third_parameter" : "param 3"}
some_function(**some_dictionary)
#>>>The parameter 'one_parameter' is equal to: 1_parameter
#>>>The parameter 'another_parameter' is equal to: another parameter
#>>>The parameter 'a_third_parameter' is equal to: param 3
```

The same can be done in reverse, by supplying the asterisk (`*`) to an argument of a function definition, so that it expects a list or tuple and then does the reverse.
A useful link explaining how to use the reverse, generally refered to as `*args` and `**kwargs`, can be found here: http://stackoverflow.com/questions/3394835/args-and-kwargs
Basically, `*args` can be used to pass multiple parameters into a function, while `**kwargs` can pass an undetermined number of named parameters into a function. 

####Some more examples or packing and unpacking parameters:
Python functions can accept both named and unnamed parameters.  Let's show a function for demonstration:
```python
def some_function(param1, param2):
    print param1, param2
```
Now, we can pass in 2 unnamed parameters and see what we get:
```python
some_function(1,2)
#>>>1, 2
```
This is the normal way you've been passing in parameters to a function.  Parameters can also be specified by name, instead of position:
```python
some_function(param2 = 1, param1 = 2)
#>>>2, 1
```
Notice that we specified param2, which is the second parameter in the definition, first.
#####`*args`
Now, moving to passing in function multiple parameters with *args:
```python
some_list = [1,2]
some_function(*some_list)
#>>>1,2
```
Here, you see that despite the fact that the function took 2 parameters, it successfully ran with a single unpacked list as input.  
#####`**kwargs`
The same could be done with named parameters:
```python
some_dict = {"param1" : "parameter 1", "param2": "parameter 2"}
some_function(**some_dict)
#>>>parameter 1 parameter 2
```

This can also be done in reverse; defining a function to take multiple parameters, whether named (`**kwargs`) or unnamed (`*args`)
```python
def some_other_function(*args, **kwargs):
    for arg in args:  #args is like a list
        print arg
    for kwarg in kwargs:  #kwargs is like a dictionary
        print kwarg, kwargs[kwarg]

x = 1
y = 2
z = ['a', 'b']
a_dict = {'hello': 'World!'}
a_tuple = (1,2,3,4,5)

some_other_function(x, y, z, some_dictionary = a_dict, some_tuple = a_tuple)     
#>>>args:
#>>>1
#>>>2
#>>>['a', 'b']
#>>>kwargs:
#>>>some_dictionary  :  {'hello': 'World!'}
#>>>some_tuple  :  (1, 2, 3, 4, 5)
```

##Summary

- 

[recording]: https://plus.google.com/u/0/events/cciortcifbg5qttjrmg533f78c4?authkey=CMj07bft-ovZPg

