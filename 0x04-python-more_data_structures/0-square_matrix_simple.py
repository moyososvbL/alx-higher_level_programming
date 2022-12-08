#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
 """Compute the square value of all integers of a matrix."""
	new_matrix = []
for i in matrix:
	new_matrix.append(i**2)
return new_matrix
