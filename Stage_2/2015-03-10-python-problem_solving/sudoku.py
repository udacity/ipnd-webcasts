###############################
# Steps for solving larger problems:
#
# 1) Understand Problem
#      - What are the input(s)?
#      - What do we need to do to the input(s)?
#          The classic Sudoku game involves a grid of 81 squares.
#          The grid is divided into nine blocks, each containing nine squares.
#          The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares.
#          Each number can only appear once in a row, column or box.
#      - What are the output(s)?
#
# 2) Plan a solution
#      - You can do this on paper!
#      - Or with "pretend" code (otherwise known as pseudocode)
#
# 3) Fill out your solution!
#      - Test along the way!
#########
# Steps For THIS Problem
# 1a What are input(s)? "A list of lists representing a
#    sudoku grid"
# 1b What do we need to do with the input(s)?
# 1c What are output(s) "A boolean (True or False) to
#    indicate whether the input grid is valid"
#
# 2) I did the planning by using "wishful thinking" while
#    writing code. I wrote code assuming that I had
#    already written functions which didn't actually exist yet
#
# 3) I filled out the solution by gradually writing
#    the code for the functions that didn't yet exist.
########

# this grid doesn't pass the column check
INVALID_GRID = [[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]]

# this grid is good!
VALID_GRID = [[4,3,5,2,6,9,7,8,1],
              [6,8,2,5,7,1,4,9,3],
              [1,9,7,8,3,4,5,6,2],
              [8,2,6,1,9,5,3,4,7],
              [3,7,4,6,8,2,9,1,5],
              [9,5,1,7,4,3,6,2,8],
              [5,1,9,3,2,6,8,7,4],
              [2,4,8,9,5,7,1,3,6],
              [7,6,3,4,1,8,2,5,9]]

# We can write this code even BEFORE we have written
# the check_rows, check_columns, and check_squares
# functions! It won't work until we do, but this helps
# us think about the problem.
def check_sudoku(sudoku_grid):
  print "Checking sudoku grid:"
  display_grid(sudoku_grid)
  if check_rows(sudoku_grid) == True:
    print "rows look good!"
    if check_columns(sudoku_grid) == True:
      print "columns look good!"
      if check_squares(sudoku_grid) == True:
        "squares look good! This is a valid Sudoku Grid!"
        return True
  # The only way we would get here is if we failed one
  # of the 3 checks
  return False

# I wrote this even before I had the is_valid_row function
def check_rows(grid):
  for row in grid:
    if is_valid_row(row) == False:
      return False
  return True

def is_valid_row(row):
  required_numbers = [1,2,3,4,5,6,7,8,9]
  # required_numbers = range(1,10) <--would also work
  for number in required_numbers:
    if number not in row:
      return False
  return True

# this function turns all the columns from the
# original grid into rows for a new grid
# then it uses the check_rows function that I
# already wrote to verify
def check_columns(grid):
  columns = []
  for index in range(9):
    new_column = []
    for row in grid:
      new_column.append(row[index])
    columns.append(new_column)
  return check_rows(columns)

# this was the hardest check to make!
def check_squares(grid_9by9):
  rows_of_squares = make_squares(grid_9by9)
  for row_of_squares in rows_of_squares:
    for sq in row_of_squares:
      if check_square(sq) == False:
        return False
  return True

# NOTE: After I started writing this function I
# started to regret my decision for how I was
# doing this. Four nested 'for loops' is a lot!
def make_squares(sudoku_grid):
  grid_of_squares = []
  # I start with an empty list...
  for i in range(3):
    # and create 3 rows of 3x3 squares...
    new_row_of_squares=[]
    for j in range(3):
      # in each row there are 3 3x3 squares...
      new_square = []
      for row_num in range(3):
        # each square has 3 rows...
        new_row = []
        for cell_num in range(3):
          # and each row has 3 cells...
          sudoku_cell_value = sudoku_grid[i*3 + row_num][j*3 + cell_num]
          new_row.append(sudoku_cell_value)
          # The above 2 lines are tricky. Can you figure out what i*3 and j*3 are doing?
        new_square.append(new_row)
      new_row_of_squares.append(new_square)
    grid_of_squares.append(new_row_of_squares)
  return grid_of_squares

def check_square(square):
  single_row = []
  for row in square:
    # remember, [1,2,3] + [4,5,6] is [1,2,3,4,5,6] NOT [1,2,3,[4,5,6]]
    single_row = single_row + row
  if is_valid_row(single_row):
    return True
  else:
    return False

#############################################
#
# DISPLAY FUNCTIONS
#   I wrote these after the coding session.
#   You're welcome to use them to display
#   sudoku grids in a nicer way.
def display_grid(sudoku_grid):
  rows_of_squares = make_squares(sudoku_grid)
  print ' ----------------------- '
  to_print = ''
  display_row_of_squares(rows_of_squares[0])
  print '|-------|-------|-------|'
  display_row_of_squares(rows_of_squares[1])
  print '|-------|-------|-------|'
  display_row_of_squares(rows_of_squares[0])
  print ' ----------------------- '

def display_row_of_squares(row_of_squares):
  for i in range(3):
    line = '|'
    for sq in row_of_squares:
      line = line + ' '
      row = sq[i]
      for cell in row:
        line = line + str(cell) + ' '
      line = line + '|'
    print line

# This is where we actually call the check_sudoku function!
print check_sudoku(VALID_GRID)

# these are 2 examples of 3x3 squares
# SQ1 = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# SQ2 = [[1,3,5],
#        [7,9,2],
#        [4,6,8]]
# EXAMPLE_GRID_OF_SQUARES = [[SQ1, SQ2, SQ1],
#                            [SQ2, SQ1, SQ2],
#                            [SQ1, SQ2, SQ1]]

