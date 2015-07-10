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


##Making the Game
###What do you need to play the game on paper?
- A background to play on
- A way to keep track of who has already moved where
- A way to keep track of the who's turn it is
- Only allow legal moves
- End the game once someone wins or it ends in a draw

###Breaking the game into functions
We can get some of the simpler things out of the way immediately.

We can use a dictionary to keep track of where players have made moves.  A value of " " can represent an empty location; otherwise, the location will have either an 'X' or an 'O'.

```python
current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}
```
We'll use another variable to keep track of whose turn it is:

```python
current_player = "X"
```

Next, we should see if we can write a function to display the board.


Python string formatting is probably the easiest way to do this.

###Python String Formatting
One easy way to format strings in Python is to use the string.format() method; it takes any number of aruments, named or unnamed, and substitutes them into a given string.  For example:

```python
some_string = "{0} cannot find {1}, but {0} can find {2}".format("Matthew", "Mark", "Luke")
print some_string
#>>>Matthew cannot find Mark, but Matthew can find Luke
```
While integers are used for unnamed arguments, variable names can be used for named arguments:
```python
some_string = "{name_one} cannot find {name_two}, but {name_one} can find {name_three}".format(name_two = "Mark", name_three = "Luke", name_one = "Matthew")
print some_string
#>>>Matthew cannot find Mark, but Matthew can find Luke
```

If we have a dictionary or a list, we can unpack them to do the same thing:
Dict:
```python
some_dict = {"item_two": 2, "item_one": 1, "item_three" : 3}
some_string = "{item_one}, {item_two}, {item_three}".format(**some_dict)
print some_string
#>>>1, 2, 3
```
List:
```python
some_list = [2,1,3]
some_string = "{1}, {0}, {2}".format(*some_list)
print some_string
#>>>1, 2, 3
```

Now, we can display the board using Python formatting!
```python
def display_board(current_positions):
    board = """
    {top left} | {top center} | {top right}
    ---------
    {center left} | {center} | {center right}
    ---------
    {bottom left} | {bottom center} | {bottom right}
    """.format(**current_positions)
    print board
```





##Final Code:
```python
current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}

current_player = "X"

def display_board(current_positions):
    board = """
    {top left} | {top center} | {top right}
    ---------
    {center left} | {center} | {center right}
    ---------
    {bottom left} | {bottom center} | {bottom right}
    """.format(**current_positions)
    print board

def user_move(current_positions, current_player):
    possible_moves = []
    user_prompt = "Please pick your move from the options below!"
    for position in current_positions:
        if current_positions[position] == " ":
            possible_moves.append(position)
            user_prompt += "\n" + position
    user_prompt += '\n'
    user_choice = raw_input(user_prompt).lower()
    while user_choice not in possible_moves:
        user_choice = raw_input(user_prompt).lower()
    current_positions[user_choice] = current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return current_positions, current_player


def is_game_over(current_positions):
    #Assuming only one winner
    winners = [["top left", "top center", "top right"],
               ["center left", "center", "center right"],
               ["bottom left", "bottom center", "bottom right"],
               ["top left", "center left", "bottom left"],
               ["top center", "center", "bottom center"],
               ["top right", "center right", "bottom right"],
               ["top left", "center", "bottom right"],
               ["top right", "center", "bottom left"]]
    for winning_combo in winners:
        possible_winner = current_positions[winning_combo[0]]
        if possible_winner != " ":
            possibly_won = True
            for value in winning_combo:
                if current_positions[value] != possible_winner:
                    possibly_won = False
                    break
            if possibly_won:
                return possible_winner + " Wins!"
    is_draw = True
    for position in current_positions:
        if current_positions[position] == " ":
            is_draw = False
            return False
    if is_draw:
        return "Draw!"

def play_game():
    current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}
    current_player = "X"
    result = False
    while not result:
        display_board(current_positions)
        current_positions, current_player = user_move(current_positions, current_player)
        result = is_game_over(current_positions)
        if result:
            print "GAME OVER"
            print "Result: ", result


play_game()
```


##Summary

- 

[recording]: https://plus.google.com/u/0/events/cciortcifbg5qttjrmg533f78c4?authkey=CMj07bft-ovZPg

