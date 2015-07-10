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
- A way to keep track of the whose turn it is
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

If we have a dictionary or a list, we can unpack them to do the same thing.

#####Dict:
```python
some_dict = {"item_two": 2, "item_one": 1, "item_three" : 3}
some_string = "{item_one}, {item_two}, {item_three}".format(**some_dict)
print some_string
#>>>1, 2, 3
```
#####List:
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

Let's test it to make sure it works:
With current_positions containing all empty spaces:
```
      |   |  
    ---------
      |   |  
    ---------
      |   |  
```
With current_positions containing all empty spaces except 'center', which equals 'X':
```
      |   |  
    ---------
      | X |  
    ---------
      |   |  
```
Looks like it works!

###Allowing the User to chose a move
We still need a way to actually *play* anything, though.  Lets' try to make a function which will allow a user to make a move.

This function will need to do several things:
- It should allow a user to pick where they want to go next
- It should *only* let a user make a legal move
- It should switch whose turn it is after a move has been made
- It should update the board with the user's move

Ok, now we should think; for the above, what are the right inputs and outputs?
#####Inputs:
- We'll need the current board; specifically, the dictionary we are storing positions in
- We'll also need to know whose turn it is

#####Outputs:
- We'll need to update the dictionary storing positions
- We'll need to print the current board to be displayed
- We'll need to update whose turn it is

For user input, we'll need to actually *get* user input; Python has a built in function for this called [raw_input()](https://docs.python.org/2/library/functions.html#raw_input)

We will need to make a loop which takes the user input, and only moves on once that user input represents a legal move.


Ok, on to the code:

```python
def user_move(current_positions, current_player):
    "Let a human user make a move"
    #First, find which moves are possible to make
    possible_moves = []
    #We also need to prompt the user for what choices they can make
    user_prompt = "Please pick your move from the options below!"
    for position in current_positions:
        #It's only a possible move if the space both exists and is empty
        if current_positions[position] == " ":  
            possible_moves.append(position)
            user_prompt += "\n" + position
    user_prompt += '\n'
    #since Python is case sensitive, we'll make sure to convert everything 
    #the user gives to lower-case to avoid confusion with string.lower()
    user_choice = raw_input(user_prompt).lower()
    while user_choice not in possible_moves:
        user_choice = raw_input(user_prompt).lower()
    #Once we exit the loop, the user has chosen a legal next move
    
    #Time to update the dictionary based on the move just made
    current_positions[user_choice] = current_player
    
    #Now we update whose turn it is
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        
    #We return the current positions and whose turn it is
    return current_positions, current_player
```

###Checking to see if anyone has won
Now we can move on to test if the game is over; either someone has won, the game has ended in a draw, or the game continues.
We'll make a function to do this.  As always, we'll think of needed inputs and outpus:
#####Inputs
- The current board; what are the current positions?

That's all we'll need as input for this function; we can pass in current_positions as its only parameter.

#####Outputs
- What is the status of the game?
    - Has someone won?  Who was it, if so?
    - Has the game ended in a draw?
    - Should the game continue?

We could return multiple outputs here, but it is probably easier to return a single thing which contains the information from the above choices.

We'll return a string saying what the outcome of the game is if it is over, and False if the game continues.

Seeing if the game is either a draw or should continue should be easy if we know someone hasn't won yet; we just need to see if all of the positions haven't been filled.  

Seeing if someone has won will be trickier.  We'll need to check that each of the possible winning combinations to see if they have been fulfilled!

Luckily, Tic-Tac-Toe only has 8 possible winning combinations.  You can fill any of the 3 rows horizontally with the same letter, any of the 3 columns vertically with the same letter, or one of the 2 diagonals with the same letter.  Since there are so few combinations, we can simply list them all out.

We'll then search through each winning combination to see if it contains all of one letter; if we see either an empty space (" ") or a letter not matching a previous letter ("X" where the first was "O" or vice-versa), then we know that combination hasn't been reached.  If *none* of the combinations have been reached, we know nobody has won yet.

Let's get into the code:
```python
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
    #Going through all of the winning combinations
    for winning_combo in winners:
        #Someone will only have possibly won if every entry is the same as the first
        possible_winner = current_positions[winning_combo[0]]
        
        #Nobody has won if any entry is " ", including the first
        if possible_winner != " ":
            possibly_won = True
            for value in winning_combo:
                if current_positions[value] != possible_winner:
                    possibly_won = False
                    break
            if possibly_won:
                return possible_winner + " Wins!"
    
    #If we get this far, that means that nobody has won
    #Test for a draw; are any spaces still " "?
    is_draw = True
    for position in current_positions:
        if current_positions[position] == " ":
            is_draw = False
            #Looks like we should continue the game!
            return False
            
    #Note; if we get this far, there is definately a draw
    if is_draw:
        return "Draw!"
```



###Playing the Game

Now we have all the pieces of the game, but the game isn't continuous yet.  We need to make is so that once the game starts, it plays until it is finished.  We'll do that with our main function, play_game().  

```python
def play_game():
    #Start by defining our variables so that we don't need to rely on globals
    current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}
    current_player = "X"
    #Play while our is_game_over() function tells us the game isn't over
    result = False
    while not result:
        #Display the current board after every turn
        display_board(current_positions)
        #always update our positions and turns
        current_positions, current_player = user_move(current_positions, current_player)
        #always check to see if the game is over
        result = is_game_over(current_positions)
        if result:
            print "GAME OVER"
            print "Result: ", result


play_game()
```
Now we have a working Tic-Tac-Toe game!


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

[recording]: https://plus.google.com/u/0/events/cciortcifbg5qttjrmg533f78c4?authkey=CMj07bft-ovZPg

