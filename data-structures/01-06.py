# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degress.
# Do it in place.

from os import urandom
from copy import deepcopy

def generate_matrix(N = 3, output = 'num'):
    if output == 'byte':
        matrix = [[urandom(4) for i in range(N)] for i in range(N)]
    else:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return matrix

def rotate_matrix(matrix):
    n = len(matrix)
    ind = 0
    ind_array = 0
    new_matrix = deepcopy(matrix)
    for ind_row, val_row in enumerate(matrix):
        for ind_col, val_col in enumerate(val_row):
            new_matrix[ind_col][n - 1 - ind_row] = val_col
    return new_matrix

def  (matrix):
    n = len(matrix)
    for layer in range(0, int((n / 2) + 1)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            top = matrix[first][i]
            offset = i - first
            # bottom left -> top left
            matrix[first][i] = matrix[last - offset][first]
            # bottom right -> bottom left
            matrix[last - offset][first] = matrix[last][last - offset]
            # top right -> bottom right
            matrix[last][last - offset] = matrix[i][last]
            # top left -> top right
            matrix[i][last] = top
    return matrix
    

matrix = generate_matrix()
print(matrix)
rotated_matrix = rotate_matrix(matrix)
print(rotated_matrix)

matrix = generate_matrix(5, 'byte')
rotated_matrix= rotate_matrix(matrix)
print(rotated_matrix)

matrix = generate_matrix()
print(matrix)
rotated_matrix = rotate_matrix_in_place(matrix)
print(rotated_matrix)