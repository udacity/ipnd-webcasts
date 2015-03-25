"""
Buggy code, not fixed, but with some debugging code commented out:

Fix it!


Test as you go!!!

Use print statements to check the state of your program.
Assert statements can check assumtions, if you wish to use them.

Test like it is a scientific hypothesis:
    Observe what happens.
    Try to think of why it happens.
    Change things, and see if it fits your hypothesis of what is going wrong.


    After you are confident in what the problem is, then go and fix it.

Use Python traceback to see where syntax (e.g. typo errors) or type errors (e.g. 1.append(), since 1 isn't a list) occur..

"""

# Problem:  
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

#Identity matrix examples:
#   [1, 0]
#   [0, 1]

#   [1, 0, 0]
#   [0, 1, 0]
#   [0, 0, 1]

#Matrices which are *NOT* idenity matrices:

#   [1, 0]

#   [1]
#   [0]

#   [1, 1]
#   [1, 1]

#   [2, 0]
#   [0, 2]

#   [1, 0, 1]
#   [0, 1, 0]
#   [1, 0, 1]

#   [1, 0, 0, 0]
#   [0, 1, 0, 0]
#   [0, 0, 1, 0]

def is_square(matrix):
    for row in matrix:
        for column in row:
            if len(row) != len(column):
                print ((["This is not a square matrix!")))
                return False
    return True

#A square matrix (nxn)
a_matrix = [[1, 0], 
           [0, 1]]

#A matrix which is not nxn
another_matrix = [[1, 1], 
                 [0, 1], 
                 [1,2]]

#print is_square(a_matrix)  #Should return True
#print is_square(another_matrix)  #Should return False


def is_identity_matrix(matrix):
    if not is_square(matrix):
        return False
    row_number = 0
    column_number = 0
    for row in matrix:
        #print "row_number: ", row_number  #Used to check the state of row_number as we go through the program
        #print "column_number: ", column_number  #Used to check the state of column_number as we go through the program
        for column in row:
            if row_number == column_number:
                if column != 1:
                    #print matrix, False  #Printing out what will be returned given a specific input
                    return False
            else:
                if column != 0:
                    #print matrix, False  Printing out what will be returned given a specific input
                    return False
            column_number += 1
        row_number += 1
    #print matrix, True  Printing out what will be returned given a specific input
    return True


def test():
    def is_square_actual(a_list):
        '''correct is_square solution, to be used with is_identity_matrix_actual and tested against'''
        #assert statements can be used to check the assumptions of a procedure or to 
        #outline ranges a value could possibly have.

        #An assert statement throws an error (and crashes the program), letting you know something is wrong and 
        #where it went wrong as soon as it happens.
        assert isinstance(a_list, list)
        for row in a_list:
            assert isinstance(row, list)
            if len(row) != len(a_list):
                return False
        return True


    def is_identity_matrix_actual(matrix):
        '''correct is_identity_matrix solution, to be tested against'''
        if not is_square_actual(matrix):
            return False
        for row in range(len(matrix)):  #range(5) would produce the list [0, 1, 2, 3, 4]
            for column in range(len(matrix[row])):
                if row == column:
                    if matrix[row][column] != 1:
                        return False
                else:
                    if matrix[row][column] != 0:
                        return False
        return True

    matrix_list = []
    matrix_list.append([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]])
    matrix_list.append([[1,0,0],
                       [0,1,0],
                       [0,0,0]])
    matrix_list.append([[2,0,0],
                       [0,2,0],
                       [0,0,2]])
    matrix_list.append([[1,0,0,0],
                       [0,1,1,0],
                       [0,0,0,1]])
    matrix_list.append([[1,0,0,0,0,0,0,0,0]])
    matrix_list.append([[1,0,0,0],  
                       [0,1,0,2],  
                       [0,0,1,0],  
                       [0,0,0,1]])
    for matrix in matrix_list:
        if is_identity_matrix(matrix) != is_identity_matrix_actual(matrix):
            print "Failed Test"
            return False
    print "Passed Tests!"
    return True

test()
