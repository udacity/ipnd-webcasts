# Webcast: General Problem Solving With Python


## Webcast Recording

Here is the link to the [video][recording]

## The Problem

We are tasked with creating a program to validate a Sudoku grid. The grid is represented as a two-dimensional list, basically a lists of lists. This is how we represent a list of lists inside Python:

```
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

Here is a framework to help us think through any problem:

###Understand the Problem
  - What are the input(s)?
  - What do we need to do to the input(s)?
    - The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares. The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.
  - What are the output(s)?

###Plan a solution
  - You can do this on paper!
  - Or with "pretend" code (otherwise known as pseudocode)
#
###Fill out your solution!
  - Test along the way!

Andy walked through how to write code and functions that don't even exist yet. He demonstrates a common coding practice called writing "pseudocode". Pseudocode is basically a high level outline of what we want the computer to do. We either write the steps out in plain English and we then proceed to convert our outline into actual code or write out code at a high level that Andy demonstrated.

In this case, Andy is writing computer code in a high level fashion and seeks to define functions that do not exist yet, drilling down and breaking the problem apart into small pieces by using a series of smaller functions.

##Breaking It Down

Andy first started off with simply defining the big function `check_sudoku`. He then asked himself "What is the first thing I should check?" Andy wanted to check whether all of the rows in the entire grid has the numbers 1 through 9. Therefore he broke the problem down and proceeded to create a function named `check_rows`.

This is a crucial step that should be iterated again. Andy addressed one requirement in the problem and proceeded to isolate that one requirement and focused on how to create a program to check that requirement.

So far, Andy's code will look like:

```
def check_sudoku(sudoku_grid):
  print "Checking sudoku grid:"
  display_grid(sudoku_grid)
  if check_rows(sudoku_grid) == True:
    print "rows look good!"
```

Andy then dives deep and proceeds to write the function `check_rows`

Here, he needs to step through the grid and checks whether each row is valid using a function called `is_valid_row`

Again, Andy further drills down and chunks up the code into small manageable pieces that can be programmed:

```
def check_rows(grid):
  for row in grid:
    if is_valid_row(row) == False:
      return False
  return True
```

If any row is false, Andy knows that the entire grid is false and returns False. 

If all rows are true, then `check_rows` will return True

Andy proceeds to dive in again and wries the `is_valid_row` function:

```
def is_valid_row(row):
  required_numbers = [1,2,3,4,5,6,7,8,9]
  # required_numbers = range(1,10) <--would also work
  for number in required_numbers:
    if number not in row:
      return False
  return True
```

Now, Andy is at the point where he can simply check for the existence of every number from 1 through 9 by looping through a list of acceptable numbers and checking whether each number exists in the row.

##Zooming Out 

Now Andy can zoom out and entirely check the first part of his requirement works: does every row have numbers 1 through 9 in the grid?

##Stepping Into The Other Requirements

What's left is checking whether the columns have numbers 1 through 9 and whether all the 3x3 squares in the gride have numbers 1 - 9 as well.

Andy follows the same procedural steps for columns, but now starts to first convert the columns into a set of rows. For example, for a 3x3 grid:

```
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

The first column will get converted into a row that equals:

`row = [1, 4, 7]`

Andy will create a function called `check_columns` that converts a column into a row and proceed to use the `check_rows` function he defined earlier.

```
def check_columns(grid):
  columns = []
  for index in range(9):
    new_column = []
    for row in grid:
      new_column.append(row[index])
    columns.append(new_column)
  return check_rows(columns)
```

Finally he tackles the squares requirement and again, proceeds to break the problem down by first defining a function to make squares from the grid and proceeds to create another function to check the squares. If any square is invalid, the whole function returns False.

The full code can be seen [here][code]

You should comment out the code and step through each requirement to understand what each section of the code is doing.

##Summary

Programming can be thought of as a series of functions that run after the other. Functions call other functions which call other functions that ultimately:

- Assigns variables
- Processes calculations
- Step through loops
- Access and set data inside data structures
- Check and execute certain code based on certain conditions

This procedural thinking is key to mastering programming: we break the problem down into small little procedures that execute one after the other.

Outlining our code or writing pseudocode will enable us to organize our code in a high-level way so we can keep track of the bigger picture of our program.

[recording]: https://plus.google.com/events/cvd7n15lqrmf267jfb4b978bo7c?authkey=CNiLyr-Q-t_I2AE
[code]: sudoku.py
