import time 
import numpy as np

def simple_sum(arr):
    result = 0.0
    for i in range(arr.shape[0]):
        result += arr[i]
    return result 

arr = np.random.rand(10000000)

start = time.time()
result = simple_sum(arr)
end = time.time()

print(result)
print("time taken =>>> ",end - start)
