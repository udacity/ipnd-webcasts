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




