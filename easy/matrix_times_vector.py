"""
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
"""

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    row = a[0]
    if len(row) != len(b):
        return -1
    output = []
    for row in a:
        output.append(sum([row_el * vec_el for row_el, vec_el in zip(row, b)]))
    return output

