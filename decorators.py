def polite_decorator(func):
    def wrapper(*args, **kwargs):
        print("Please wait, executing...")
        func(*args, **kwargs)
        print("Thank you, execution complete!")
    return wrapper

@polite_decorator

def say_hello(name):
    print(f"Hello, {name}")

say_hello("Alice")


#next question:--

import time

def time_detector(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("starting execution...")
        end_time = time.time()
        print(f"execution completed in {end_time - start_time} seconds")
    return wrapper

@time_detector

def time():
    for i in range(1000000):
        pass


#next quesition:--

