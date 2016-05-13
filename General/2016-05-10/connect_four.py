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
