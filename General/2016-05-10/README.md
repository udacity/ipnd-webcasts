#Making a Playable text-based Connect Four Game

Today Luke and Kelly go through how to create a playable connect four game with Python! 

The link to the video can be found [here](https://www.youtube.com/watch?v=pAv7kyQ-Q80).

# Overview

The first step of solving any problem is to step back and think through it.  First, we decide what the inputs and outputs will be, and what big picture steps we will take.

For inputs, we will be getting a user to decide which location to 'drop' the piece for every turn.

For outputs, we want to display an updated ASCII (i.e. text) board that displays the results of every move made up to the current moment, and which can detect if the game is over.

This brings us to which steps we will take to solve the problem.  We need to:
 - Make and display a board
 - Be able to chose a location and make that choice
 - Alter the board based on what we choose
 - Switch between players
 - See if the game is over
  - see who won (or if it is a tie)

## Making the Game

####Make the Board
To start off, we'll create a function to make a board.

```python
def create_board(x, y):
    board = []
    for j in range(y):
        new_row = []
        for i in range(x):
            new_row.append([])
        board.append(new_row)
    return board
```

Here, we make the decision to form the board out of a list of lists, with each element *also* being a list (which would technically make this a list of lists of lists).

We can test this using the built-in pretty print module of python to see what our board looks like:

```python
board = create_board(7, 6)
pprint.pprint(board)
```

This creates this output:

```txt
[[[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []]]
 ```

 One thing to note here; the top left would be `board[0][0]` while, with `board[y][x]`, y goes down and x goes right as they rise.

####Altering the Board
 Next up, we should make a function to alter the board by choosing a row.  Here, we aren't looking for user input, but rather just a way to programmatically alter our data structure:

 ```python
 def choose_row(current_turn, board, x):
    if board[-1][x]: #Make sure the move is legal
        return False
    current_y = 0
    while board[current_y][x]:
        current_y += 1 #drop down until we find an occupied location
    new_board = copy.deepcopy(board) #create a copy of the board so we don't mutate it
    new_board[current_y][x].append(current_turn)
    return new_board
```

Now we can test this:

```python
board = choose_row('O', board, 0)
board = choose_row('O', board, 0)
board = choose_row('O', board, 0)

pprint.pprint(board)
```

This produces the result:

```txt
[[['O'], [], [], [], [], [], []],
 [['O'], [], [], [], [], [], []],
 [['O'], [], [], [], [], [], []],
 [[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []],
 [[], [], [], [], [], [], []]]
 ```

 So it looks like it is working!

####Displaying the Board
 Now, we'd really rather that it was easier to see what is going on than using pprint.  Instead, we will create a function to display the board in a more user-friendly way:


```python
def display_board(board):
    display = ""
    for row in board:
        newrow = "|"
        for column in row:
            if column:
                newrow += str(column[0]) + "|"
            else:
                newrow += " |"
        newrow += "\n" + "--"*len(row) + "-\n"
        display = newrow + display
    display = "--"*len(board[0])+'-\n' + display
    return display
```

The above function actually flips the y axis; `board[0][0]` now points to the bottom left, and `board[y][x]` now goes up as y increases (while x still goes right).

To test this, we can display the same board as before:

```python
print display_board(board)
```

```txt
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
|O| | | | | | |
---------------
|O| | | | | | |
---------------
|O| | | | | | |
---------------
```

####Getting User Input
For our next step, we should start to think about user input.  

```python
def is_legal_move(move, board):
    try:
        if not board[-1][move]:
            return True
        return False
    except:
        return False

def get_player_input(board, player):
    possible_cols = []
    for cols in range(len(board[0])):
        if is_legal_move(cols, board):
            possible_cols.append(cols)
    prompt = "Player {0}, please select which column to enter.\nChoose from these possibilities: {1}\n".format(player, possible_cols)
    move = None
    while move not in possible_cols:
        try:
            move = int(raw_input(prompt))
        except:
            move = None
    return move
```


Here, in get_player_input(), we first find any possible moves that can be made by checking each column in the top row for anything that's currently there.  If it is empty, we know that there is a possible move there.  With knowledge of what's possible, we prompt the user to give us a number.  If they give us a non-possible number (or, if they crash that section of the program by giving us something that isn't a number at all), we re-run the prompt until they give us a possible number.

####Writing the Main Function
```python
def play_game():
    board = create_board(7,6)
    players = ["O", "X"]
    current_player = players[0]
    while not is_game_over(board):
        print display_board(board)
        move = get_player_input(board, current_player)
        board = choose_row(current_player, board, move)
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]
    winner = is_game_over(board)
    if winner == "Tie":
        print "It's a tie!"
    else:
        print winner, "won!"
    print display_board(board)
```

Now we can write our main function.  It creates a board, sets the players, and then runs the game while the game isn't over.  While it runs the game, it displays the board, gets user input, updates the board, and switches players after each move.  The only thing left is writing the function which sees if the game is over!

####Seeing if the Game is Over (and Who Won)
```python
def is_game_over(board):
    is_board_full = True
    for y in range(len(board)):
        for x in range(len(board[0])):
            current = board[y][x]
            if not current:
                is_board_full = False
                continue
            #check up
            if y+3 < len(board) and current:
                if board[y][x] == board[y+1][x] == board[y+2][x] == board[y+3][x]:
                    return current[0]

            #check right
            if x+3 < len(board[0]) and current:
                if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3]:
                    return current[0]

            #check upright
            if y+3 < len(board) and x+3 < len(board[0]) and current:
                if board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3]:
                    return current[0]

            #check downright
            if y-3 >= 0 and x+3 < len(board[0]) and current:
                if board[y][x] == board[y-1][x+1] == board[y-2][x+2] == board[y-3][x+3]:
                    return current[0]
    if is_board_full:
        return "Tie"
    return False
```

There are two ways that the game could be over; someone could have won, or the board could be completely fun (and the game ends in a tie).  We check to see if someone has won by going through every single square on the board and checking up, right, upright, and down-right to see if there are four non-empty identical squares in a row.  If there are, we know the game is over and who won.  If there aren't, we keep moving to the next square.  If all squares were occupied but nobody won, the game ends in a tie.  Otherwise, we return False to continue playing the game.

####Final Program
Together, that brings us this final Python program:

```python
#Things to do:

# Make and display a board
# Be able to chose a location and make that choice
# Alter the board based on what we choose
# Switch between players
# See if the game is over
#   see who won (or if it is a tie)

import pprint
import copy

def create_board(x, y):
    board = []
    for j in range(y):
        new_row = []
        for i in range(x):
            new_row.append([])
        board.append(new_row)
    return board

#test
# board = create_board(7, 6)
# pprint.pprint(board)

def choose_row(current_turn, board, x):
    if board[-1][x]:
        return False
    current_y = 0
    while board[current_y][x]:
        current_y += 1
    new_board = copy.deepcopy(board)
    new_board[current_y][x].append(current_turn)
    return new_board

# test
# board = choose_row('O', board, 0)
# board = choose_row('O', board, 0)
# board = choose_row('O', board, 0)

# pprint.pprint(board)

def display_board(board):
    display = ""
    for row in board:
        newrow = "|"
        for column in row:
            if column:
                newrow += str(column[0]) + "|"
            else:
                newrow += " |"
        newrow += "\n" + "--"*len(row) + "-\n"
        display = newrow + display
    display = "--"*len(board[0])+'-\n' + display
    return display

def is_legal_move(move, board):
    try:
        if not board[-1][move]:
            return True
        return False
    except:
        return False

# print display_board(board)
def get_player_input(board, player):
    possible_cols = []
    for cols in range(len(board[0])):
        if is_legal_move(cols, board):
            possible_cols.append(cols)
    prompt = "Player {0}, please select which column to enter.\nChoose from these possibilities: {1}\n".format(player, possible_cols)
    move = None
    while move not in possible_cols:
        try:
            move = int(raw_input(prompt))
        except:
            move = None
    return move

def is_game_over(board):
    is_board_full = True
    for y in range(len(board)):
        for x in range(len(board[0])):
            current = board[y][x]
            if not current:
                is_board_full = False
                continue
            #check up
            if y+3 < len(board) and current:
                if board[y][x] == board[y+1][x] == board[y+2][x] == board[y+3][x]:
                    return current[0]

            #check right
            if x+3 < len(board[0]) and current:
                if board[y][x] == board[y][x+1] == board[y][x+2] == board[y][x+3]:
                    return current[0]

            #check upright
            if y+3 < len(board) and x+3 < len(board[0]) and current:
                if board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3]:
                    return current[0]

            #check downright
            if y-3 >= 0 and x+3 < len(board[0]) and current:
                if board[y][x] == board[y-1][x+1] == board[y-2][x+2] == board[y-3][x+3]:
                    return current[0]
    if is_board_full:
        return "Tie"
    return False


def play_game():
    board = create_board(7,6)
    players = ["O", "X"]
    current_player = players[0]
    while not is_game_over(board):
        print display_board(board)
        move = get_player_input(board, current_player)
        board = choose_row(current_player, board, move)
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]
    winner = is_game_over(board)
    if winner == "Tie":
        print "It's a tie!"
    else:
        print winner, "won!"
    print display_board(board)

play_game()
```
