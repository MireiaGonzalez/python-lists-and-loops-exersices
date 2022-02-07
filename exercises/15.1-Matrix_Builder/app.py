#Import random
from random import random

#Create the function below:
def matrix_builder(num):
    matrix = []
    for x in range(num):
        matrix.append([])
        for y in range(num):
            matrix[x].append(1)

    return matrix

print(matrix_builder(5))