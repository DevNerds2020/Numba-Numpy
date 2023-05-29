import time
import numpy as np
"""
In this example, we compare the time taken to perform scalar multiplication using a Python list comprehension and using NumPy's ndarray.
Using NumPy is significantly faster than using a Python list comprehension since NumPy uses optimized C code under the hood.
"""

# Without NumPy
start = time.time()
a = [i * 2 for i in range(1000000)]
end = time.time()
print("Without NumPy: ", end - start)

# With NumPy
start = time.time()
a = np.arange(1000000) * 2
end = time.time()
print("With NumPy: ", end - start)