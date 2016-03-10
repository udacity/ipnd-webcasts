#Problem Solving Session

You can find a link to the video [here](https://plus.google.com/u/0/events/cnla2rtg8bpkho19so48kskclu4)

#The Problem
For today's problem, Luke and Rahul will be creating an interactive [hangman game][https://en.wikipedia.org/wiki/Hangman_(game)].  

Luke starts out by outlining what the program will need to do:

###Steps
- Provide a word to be guessed
- Prompt the user to guess letters
- Judging guesses as either correct or incorrect, and keeping a tally
- Evaluating if the game is over, and who won



###Solving the problem

Luke starts out by creating a function for an initial user to provide a word to be guessed:

```python
def start_hangman():
    word_to_guess = ""
    while not word_to_guess:
        word_to_guess = raw_input("What word should be guessed?")
        if not word_to_guess:
            print "You have to enter something to be guessed!"
    #give enough space so that you can't see the word given when guessing begins
    print "\n"*25  
    return word_to_guess
```

This function is meant to make sure that a first player provides non-blank input to be guessed; once they do, the game continues.

After trying that first bit out, Luke finds that 25 new lines is not actually enough to hide the given words, so it is changed to 75 lines:

```python
def start_hangman():
    word_to_guess = ""
    while not word_to_guess:
        word_to_guess = raw_input("What word should be guessed?")
        if not word_to_guess:
            print "You have to enter something to be guessed!"
    #give enough space so that you can't see the word given when guessing begins
    print "\n"*75 
    return word_to_guess
```

From there, Luke and Rahul decide to go over what must happen in the main function of a game.  The game should go through a look where the following happens:

- Blanks and filled in letters are displayed (possibly with how many guesses are left)
- The user is prompted to guess (and we could check to make sure it is a one character guess)
- Fill in the blank if the guess is correct; fill in hangman (or increment hangman count) if guess is incorrect
- Check to see if the game is over and who has one
- Repeat all these steps until the game ends

These steps, with a few false starts and missteps, eventually leads to the following code:


```python
#Provide a word be guessed
#Prompting the user to guess letters
#Judging guesses as either correct or incorrect, and keeping tally

def start_hangman():
    """start the game; prompts user to provide word to be guessed,
    returns word to be guessed"""
    word_to_guess = ""
    while not word_to_guess:
        word_to_guess = raw_input("What word should be guessed?")
        if not word_to_guess:
            print "You have to enter something to be guessed!"
    print "\n"*75
    return word_to_guess

def is_letter_in_word(user_guess, word):
    "checks to see a guessed letter is in the word; returns True or False"
    if len(user_guess) == 1 and user_guess in word:
        return True
    else:
        return False

def is_game_over(total_guesses, word, hangman_count, max_hangman_count = 6):
    """checks to see if the game is over; returns True if either side wins, 
    false otherwise.  Prints 'You win' if the guesser wins"""
    if hangman_count >= max_hangman_count:
        print "Sorry, you're out of guesses!  Game over!"
        return True #Word chooser wins
    user_wins = False
    for letter in word:
        if letter not in total_guesses:
            return False
    print "You win!  The word is " + word + "!"
    return True #User wins

def display_blanks(total_guesses, word):
    """Takes in all previous guesses and the target word, returns 
    a string with blanks for unguessed letters in the word and filled in letters for 
    already guessed letters.  There is a space between every character."""
    to_display = ""
    for letter in word:
        if letter in total_guesses:
            to_display += letter + " "
        else:
            to_display += "_ " 
    return to_display

def user_guesses_leter():
    "Prompts user for a possible letter in the word; returns their input."
    user_guess = raw_input("What letter do you guess?")
    while len(user_guess) != 1:
        print "Your guesses must be only one letter!"
        user_guess = raw_input("What letter do you guess?")
    return user_guess

# What happens in play_hangman:
# Start the game and get the word to be guessed
# then, in a loop...
# Display blanks
# Prompt user to guess
# If user guess is one character:
# Either fill in character (right guess) or fill in hangman (wrong guess)
# Check to see if the game is over
# Repeat these steps if not
def play_hangman():
    "Main function of the game."
    word = start_hangman()
    gameover = False
    total_guesses = []
    hangman_count = 0
    max_hangman_count = 6
    while not gameover:
        print display_blanks(total_guesses, word)
        user_guess = user_guesses_leter()
        total_guesses += user_guess
        if is_letter_in_word(user_guess, word):
            print "Nice!"
        else:
            print "Sorry, that's not in the word..."
            hangman_count += 1
            print "You have " + str(max_hangman_count - hangman_count) + " guesses left."
        gameover = is_game_over(total_guesses, word, hangman_count)


play_hangman()
```

Now we have a fully functioning hangman game!  There are a variety of ways this could be improved; we could make sure the word is a correctly spelled word in an english language dictionary, the letters alread guessed could be displayed (and not allowed to be guessed again), the hangman could be drawn in with ASCII art or with a GUI, if the GUI route is taken, the entire game could be put into the GUI instead of the terminal, etc...

However, there was not nearly enough time to do the above in the 45 minutes spent making this program!
