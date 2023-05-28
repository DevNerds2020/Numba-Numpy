import threading
import time
"""
In this sample code, we define a function called worker that takes a slice of a list as its input and computes the sum of its elements. We then split a test list into chunks and create a list of threads, each of which is responsible for computing the sum of a chunk.
We use the threading.
Thread class to create each thread and pass the worker function as its target.
We also pass the start and end indices of the chunk, the list to be processed, and a shared list to store the result of each thread.
We start each thread using the start method and wait for all threads to complete using the join method. Finally, we compute the final result by summing the values in the shared result list.
"""
# Define a function to be executed in parallel
def worker(start, end, arr, result):
    s = 0.0
    for i in range(start, end):
        s += arr[i]
    result.append(s)

# Create a test array
arr = list(range(1000000))

# Split the array into chunks and create a list of threads
chunk_size = 10
threads = []
result = []
for i in range(0, len(arr), chunk_size):
    start = i
    end = min(i+chunk_size, len(arr))
    thread = threading.Thread(target=worker, args=(start, end, arr, result))
    threads.append(thread)

# Start the threads and wait for them to complete
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Compute the final result
start = time.time()
final_result = sum(result)
end = time.time()

print(final_result)
print("time taken =>>> ",end - start)