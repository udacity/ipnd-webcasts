#Problem Solving Session

The link to the video can be found [here](https://plus.google.com/u/0/events/c9vns1l2dqmqj43gc0npabsn53k?authkey=CMLg6p_swOOEowE).


Today we'll be solving two problems live.  In the first, Jonah presents Luke with the problem found [here](http://codingbat.com/prob/p118406).  In the second, Luke gives Jonah the problem found [here](https://projecteuler.net/problem=11).  

###First problem
First, the problem stump:

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops

This is pretty similar to a problem Luke solved with Anthony a few months ago; his first approach is very similar to that one:

```python
def make_bricks(small, big, goal):
    current_len = 0
    big_used = 0
    small_used = 0
    while current_len < goal:
        counter += 1
        if big_used < big and current_len + 5 <= goal:
            big_used += 1
            current_len += 5
        elif small_used < small and current_len + 1 <= goal:
            small_used += 1
            current_len += 1
        else:
            break
    if current_len == goal:
        return True
    return False
```

However, the website wasn't accepting the answer because it was timing out!  To figure out what was happening, Luke started to test it on his own machine.  To do this, he added a counter and a break to make sure that the loop would definately finish:

```python
def make_bricks(small, big, goal):
    current_len = 0
    big_used = 0
    small_used = 0
    counter = 0
    while current_len < goal:
        counter += 1
        if big_used < big and current_len + 5 <= goal:
            big_used += 1
            current_len += 5
        elif small_used < small and current_len + 1 <= goal:
            small_used += 1
            current_len += 1
        elif counter >1000:
            print "infinite loop"
            break
        else:
            break
    if current_len == goal:
        return True
    return False
```

This seemed to work perfectly on his machine, but the website still wouldn't take the answer.  After noticing that the website said a loop wasn't necessary, Luke tried to solve the problem without using any loops.  To do this, he utilized Python's integer floor rounding. 

#####Integer division
In Python, as well as many other languages, if you divide two ints, you will always get an int as an answer, even though the numerator may not be divisible by the denominator.  It does this by *always* truncating (rounding down).  So, in Python, 5/2 == 2, although any float makes the answer a float (5.0/2 == 2.5). Integer division that always rounds down is also called **floor division**.

#####Back to first problem

Luke then solved the problem without loops:

```python
def make_bricks(small, big, goal):
    if big * 5 + small < goal:
        return False

    max_with_big = big * 5
    if max_with_big >= goal:
        big_used = goal // 5  #// ensures floor division
    else:
        big_used = big
    left = goal - big_used * 5
    if small >= left:
        return True
    return False
```

This, the website accepted!

###Second Problem

Luke then gave Jonah a problem from project Eular:

n the 20×20 grid below, four numbers along a diagonal line have been marked.


| 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08  
| 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00  
| 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65  
| 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91  
| 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80  
| 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50  
| 32 98 81 28 64 23 67 10 **26** 38 40 67 59 54 70 66 18 38 64 70  
| 67 26 20 68 02 62 12 20 95 **63** 94 39 63 08 40 91 66 49 94 21  
| 24 55 58 05 66 73 99 26 97 17 **78** 78 96 83 14 88 34 89 63 72  
| 21 36 23 09 75 00 76 44 20 45 35 **14** 00 61 33 97 34 31 33 95  
| 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92  
| 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57  
| 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58  
| 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40  
| 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66  
| 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69  
| 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36  
| 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16  
| 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54  
| 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48  


The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?




######Luke's Original Solution:
```python
# coding=utf-8
# In the 20×20 grid below, four numbers along a diagonal line 
# have been marked in red.

grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in 
# the same direction (up, down, left, right, or diagonally)
# in the 20×20 grid?

grid_rows = 0 #start at 0, since we have a newline befor first row
for char in grid:
    if char == '\n':
        grid_rows += 1
grid_rows -= 1 #take one off, since we end with a newline

grid = grid.split()
column_len = len(grid) / grid_rows
new_grid = []
current_col = 0
col = []
for num in grid:
    if len(col) < column_len:
        col.append(int(num))
    else:
        new_grid.append(col)
        col = [int(num)]
new_grid.append(col)

# for row in new_grid:
#     print row

max_sum = 0

#check accross
for row in range(len(new_grid)):
    for col in range(len(new_grid[0])):
        diag_up_right = 1
        diag_down_right = 1
        diag_down_left = 1
        diag_up_left = 1
        left = 1
        right = 1
        up = 1
        down = 1
        for i in range(4):
            try:
                diag_up_right *= new_grid[row-i][col+i]
            except:
                diag_up_right = 0
            try:
                diag_down_right *= new_grid[row+i][col+i]
            except:
                diag_down_right = 0
            try:
                diag_down_left *= new_grid[row+i][col-i]
            except:
                diag_down_left = 0
            try:
                diag_up_left *= new_grid[row-i][col-i]
            except:
                diag_up_left = 0
            try:
                up *= new_grid[row+i][col]
            except:
                up = 0
            try:
                down *= new_grid[row-i][col]
            except:
                down = 0
            try:
                left *= new_grid[row][col-i]
            except:
                left = 0
            try:
                right *= new_grid[row][col+i]
            except:
                right = 0

        for summ in [diag_up_right, diag_down_right,
                      diag_down_left, diag_up_left,
                      left, right, up, down]:
            if summ > max_sum:
                max_sum = summ
                #print new_grid[row][col], (row, col), max_sum

print max_sum
#70600674
```


