current_positions = {"top left": " ", "top center": " ", "top right": " ",
             "center left": " ", "center": " ", "center right": " ",
             "bottom left": " ", "bottom center": " ", "bottom right": " "}

current_player = "X"
"""
some_dictionary = {"a_value" : "x", "some_value" : "y"}
some_string = "Hello {a_value}, {some_value}".format(**some_dictionary)
print some_string
"""
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
