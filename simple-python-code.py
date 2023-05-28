import numpy as np
import time

def sum_squares(arr):
    result = 0.0
    for i in range(arr.shape[0]):
        result += arr[i]**2
    return result

arr = np.random.rand(10000000)

start = time.time()
result = sum_squares(arr)
end = time.time()
print(result)
print("time taken =>>> ",end - start)