# Write an algorithm such that if an element in an MxN matrix 0, its
# entire row and column is set to 0
import copy
matrix = [[1, 0, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


def set_zero(matrix):
    new_matrix = copy.deepcopy(matrix)
    for ind_row, val_row in enumerate(matrix):
        for ind_col, val_col in enumerate(val_row):
            print(ind_col)
            if val_col == 0:
                for ind_change, val_change in enumerate(matrix[ind_row]):
                    new_matrix[ind_row][ind_change] = 0
                for ind_change, val_change in enumerate(matrix):
                    new_matrix[ind_change][ind_col] = 0
    return new_matrix


print(set_zero(matrix))
