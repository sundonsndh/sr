import numpy as np

X = np.array([[1, 10], [2, 9], [3, 8], 
              [4, 7], [5, 6], [6, 5]])
X
array([[ 1, 10],
       [ 2,  9],
       [ 3,  8],
       [ 4,  7],
       [ 5,  6],
       [ 6,  5]])
from mlxtend.preprocessing import minmax_scaling

minmax_scaling(X, columns=[0, 1])
array([[ 0. ,  1. ],
       [ 0.2,  0.8],
       [ 0.4,  0.6],
       [ 0.6,  0.4],
       [ 0.8,  0.2],
       [ 1. ,  0. ]])
