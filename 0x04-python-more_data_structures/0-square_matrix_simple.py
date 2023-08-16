#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        rows = []
        for col in range(len(matrix[row])):
            rows.append(matrix[row][col] ** 2)
        new_matrix.append(rows)
    return new_matrix
