
import numpy as np
import numba
import time

"""
In this sample code, we define a function called sum_squares that takes a NumPy array as its input and computes the sum of squares of its elements using a for loop.
We use the @jit decorator to instruct Numba to compile this function using its JIT compiler, which can significantly speed up the execution of the function. 
We also set the nopython=True flag to ensure that Numba generates code that does not rely on the Python interpreter.
"""
# Define a function to compute the sum of squares of an array
@numba.jit(nopython=True)
def sum_squares(arr):
    result = 0.0
    for i in range(arr.shape[0]):
        result += arr[i]**2
    return result

# Create a test array
arr = np.random.rand(10000000)

# Call the function and time it
start = time.time()
result = sum_squares(arr)
end = time.time()
print(result)
print("time taken =>>> ",end - start)