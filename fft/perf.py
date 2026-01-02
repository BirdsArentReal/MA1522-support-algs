import time
def timeit(func, iterations = 1):
    start = time.time()
    for i in range(iterations):
        continue
    end = time.time()
    diff = end - start
    
    start = time.time()
    for i in range(iterations):
        res = func()
    end = time.time()
    diff = (end - start - diff)/iterations
    print(f"Elapsed time: {end - start}")
    return res, end-start