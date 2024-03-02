import numpy as np
def indices_of_smallest_elements(x,n):
     sorted_indices = np.argsort(x)
     return sorted_indices[:n]

x = np.array([3,2,5,4,1,7])
n = 3
indices = indices_of_smallest_elements(x,n)
print(n, indices)