#Problem Solving Session

You can find a link to the video [here](https://plus.google.com/u/0/events/cn22jtq5i00kd8nf5u8gfehp4ic)

#Problem 1- Rock Paper Scissors
For the first problem of the day, Jonah tells Luke to create a game which will play rock-paper-scissors with a human player.  The game will randomly select which it will do based on a random number generator.

Luke starts out by outlining what the computer will need to do:

###Steps
- The computer will decide what it will do
- Prompt the user for one of the three options
- The computer will see who wins / if there is a tie
- The computer will print out the result
- Ask if the player wants to play again / keep score

###Solving the problem

Luke then starts with a function which will prompt the user to chose what they plan to use.  One wrinkle he throws into the program is to allow for a variety of user input.  This is done through a dictionary; each acceptable input is listed as a key, and the value it will be converted to is the value of that key/value pair mapping: 

```python
valid_answers = {"rock" :"rock",
                        "r":"rock",
                        "1":"rock",
                        "paper" :"paper",
                        "p": "paper",
                        "2": "paper",
                        "scissors": "scissors",
                        "s":"scissors",
                        "3":"scissors"}
```

A lowercase version of user input is then compared to all of the keys in this dictionary; if it is found, it will convert the user input to the value given by the specific key.  This means '1', 'r', and 'rock' will all be accepted and converted to 'rock'.

A while loop allows prompts to be given continuously until the user gives an answer the program can map to a specific choice.  The full function then looks like this:

```python
def get_user_choice():
    """Prompts user to select from Rock, Paper, or Scissors
    Returns a string representing the user's choice"""
    user_choice = ""
    while not user_choice:  
        prompt = "\nPlease select Rock, Paper, or Scissors\n"
        valid_answers = {"rock" :"rock",
                        "r":"rock",
                        "1":"rock",
                        "paper" :"paper",
                        "p": "paper",
                        "2": "paper",
                        "scissors": "scissors",
                        "s":"scissors",
                        "3":"scissors"}

        user_input = raw_input(prompt).lower()
        if user_input in valid_answers:
            user_choice = valid_answers[user_input]
            print "\nYou've chosen " + user_choice + "!\n"
        else:
            print "That wasn't an option!  Please pick again."
    return user_choice
```

After the user chooses what they want to throw, we'll need to pick what the computer will do.  It would be unfair for the computer to look at what the user chose to make its own choice, and we don't have the time to try something fancy like using machine learning to recognize patterns in what a user might pick based on his or her previous choices.  So we will instead simply pick rock, paper, or scissors randomly!  We can do this with the randint function from the random module.  

The random module is in the Python Standard Library, so we know it will be installed.  The randint() function takes two arguments, which specify the lowest possible integer and the highest possible integer.  So, for our purposes, we will use

```python
randint(0,2)
```

which will return either 0, 1, or 2.  We can then compare this number with rock (0), paper (1), or scissors (2).  Based on the random number generated, we can use an if statement to show the game as a tie, the computer winning, or the user winning.  

We can put all of this inside of a function 'play_game()', which will act much like a 'main' function in many programming languages.  

This would then look like this:

```python
import random
def play_game():
    "This will play one game"
    possible_choices = ("rock", "paper", "scissors")
    computer_choice = random.randint(0, 2)
    player_choice = get_user_choice()
    print "The computer chose " + possible_choices[computer_choice]
    if player_choice == possible_choices[computer_choice]:
        return "Tie"
    elif player_choice == possible_choices[computer_choice - 1]:
        return "Computer wins"
    else:
        return "Player wins"
```

The leaves the full solution looking like this:

###Solution
```python
#Steps

#The computer will decide what it will do
#Prompt the user for one of the three options

#The computer will see who wins / if there is a tie
#The computer will print out the result
#Ask if the player wants to play again / keep score

def get_user_choice():
    user_choice = ""
    while not user_choice:
        prompt = "\nPlease select Rock, Paper, or Scissors\n"
        valid_answers = {"rock" :"rock",
                        "r":"rock",
                        "1":"rock",
                        "paper" :"paper",
                        "p": "paper",
                        "2": "paper",
                        "scissors": "scissors",
                        "s":"scissors",
                        "3":"scissors"}

        user_input = raw_input(prompt).lower()
        if user_input in valid_answers:
            user_choice = valid_answers[user_input]
            print "\nYou've chosen " + user_choice + "!\n"
        else:
            print "That wasn't an option!  Please pick again."
    return user_choice

import random
def play_game():
    "This will play one game"
    possible_choices = ("rock", "paper", "scissors")
    computer_choice = random.randint(0, 2)
    player_choice = get_user_choice()
    print "The computer chose " + possible_choices[computer_choice]
    if player_choice == possible_choices[computer_choice]:
        return "Tie"
    elif player_choice == possible_choices[computer_choice - 1]:
        return "Computer wins"
    else:
        return "Player wins"

print play_game()
```

#Fibonacci Sequence
For the second problem of the day, Luke gives Jonah a problem related to the Fibonacci sequence.  The Fibonacci sequence is an infinite series in which every term is the sum of the previous two terms, like:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

The goal of this problem is to give a number of terms you want of the Fibonacci sequence as a parameter to a function, and have that function return a list containing that many numbers in the Fibonacci sequence, starting with [0, 1].

This is a classic problem to solve with recursion, and that is exactly what Jonah uses to solve it:

```python
def fib(length):
    returnlist = []
    if length == 1:
        returnlist.append(0)
        return returnlist
    elif length == 2:
        returnlist = [0,1]
        return returnlist
    else:
        currentlist = fib(length-1)
        nextnumber = currentlist[-1]+currentlist[-2]
        currentlist.append(nextnumber)
        return currentlist
```

Recursive solutions have both a base case and a recursion case.  A base case will be the case where the function ends; recursive cases call the function once more, similar to how a loop goes over the same piece of code again.

In Jonah's base case, if the requested length is 1 or 2, the function will return that list directly.  Otherwise, it will use a recursive case to get to the point where the requested case is in the base cases (in this case, length == 2), and then add an extra number from the sequence to the list based on the last two numbers, and then return that list.



