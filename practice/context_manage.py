with open("data.txt", "a") as f:
    f.write("Its 23 October today")

with open("data.txt", "r") as f:
    print(f.read())


# File Handling

try:
    with open("data.txt", "r") as f:
        d = f.read()
        print(d)
except FileNotFoundError as e:
    print("Error Handled", e)

# Custom Context Management

class MyContext:
    def __enter__(self):
        print("Entering Context...")
        return "resources"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit Context...")
        if exc_type:
            print("Error", exc_value)
        return True

with MyContext() as m:
    print("Inside Block...")
    
    raise ValueError("Something went wrong.")


# Real Life Example for measuring time of code

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    print("Start time: ",start)
    yield
    end = time.time()
    print("End time: ",end)
    
    print(f"Execution time: {end - start:.4f} seconds")

with timer():
    sum([i**2 for i in range(100000)])


with open("data.txt", "r") as src, open("output.txt", "w") as dest:
    for line in src:
        dest.write(line.upper())
        
        
