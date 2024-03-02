import numpy as np
def nonzero(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] !=0:
                return i, j

A = [[0,0,0],
     [0,5,0],
     [0,0,0]]

r,c = nonzero(A)
print(r)
print(c)