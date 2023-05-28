import numpy as np
from numba import njit, prange
import time

"""

In this example, we define a function called parallel_sum that uses Numba's @njit decorator with the parallel=True flag to instruct Numba to automatically parallelize the code.
We also use the prange function from Numba to create a parallel range object 
that can be iterated over in parallel by multiple threads. 
Finally, we use the same test array as before and call the parallel_sum function to compute its sum using multiple threads.
"""
# Define a function to compute the sum of an array using multiple threads
@njit(parallel=True)
def parallel_sum(arr):
    total = 0.0
    for i in prange(arr.shape[0]):
        total += arr[i]
    return total

# Create a test array
arr = np.random.rand(1000000)

# Call the function and time it
start = time.time()
result = parallel_sum(arr)
end = time.time()

print(result)
print("time taken =>>> ",end - start)