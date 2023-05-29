import time
import numpy as np

"""
In this example, we create two 100x100 matrices a and b with more complex calculations involving multiplication and addition.
We then compute c as the matrix product of a and b squared, using nested loops and using NumPy's dot function and thepower function.
"""

# Without NumPy
start = time.time()
a = [[i * j for j in range(100)] for i in range(100)]
b = [[i + j for j in range(100)] for i in range(100)]
c = [[0 for j in range(100)] for i in range(100)]

for i in range(100):
    for j in range(100):
        for k in range(100):
            c[i][j] += a[i][k] * b[k][j] ** 2
end = time.time()
print("Without NumPy: ", end - start)

# With NumPy
start = time.time()
a = np.array([[i * j for j in range(100)] for i in range(100)])
b = np.array([[i + j for j in range(100)] for i in range(100)])
c = np.dot(a, np.power(b, 2))
end = time.time()
print("With NumPy: ", end - start)