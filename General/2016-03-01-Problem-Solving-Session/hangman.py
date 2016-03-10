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
        return True #Word choser wins
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
