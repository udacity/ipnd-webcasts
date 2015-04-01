"""
Possible solution, after fixing problems in earlier code
"""

# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)


def is_square(matrix):
    for row in matrix:
        if len(row) != len(matrix):
            print "This is not a square matrix!"
            return False
    return True


def is_identity_matrix(matrix):
    if not is_square(matrix):
        return False
    row_number = 0
    for row in matrix:
        column_number = 0
        for column in row:
            if row_number == column_number:
                if column != 1:
                    return False
            else:
                if column != 0:
                    return False
            column_number += 1
        row_number += 1
    return True


def test():
    def is_square_actual(a_list):
        assert isinstance(a_list, list)
        for row in a_list:
            assert isinstance(row, list)
            if len(row) != len(a_list):
                return False
        return True


    def is_identity_matrix_actual(matrix):
        if not is_square_actual(matrix):
            return False
        for row in range(len(matrix)):
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

