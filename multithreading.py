import threading
import time

def download_movie():
    print("Downlaoding movie...")
    time.sleep(3)
    print("Movie downloaded!")

t1 = threading.Thread(target=download_movie)
t2 = threading.Thread(target=download_movie)

t1.start()
t2.start()

print("main program finished!")


#next question:--

import threading
import time

def download_movie():
    print("downloading movie...")
    time.sleep(3)
    print("movie downloaded!")

t1 = threading.Thread(target=download_movie)
t2 = threading.Thread(target=download_movie)

t1.start()
t2.start()

t1.join()
t2.join()

print("main program finished")


#next question:--

import time

def print_numbers(name):
    for i in range(1, 6):
        print(f"{name}: {i}")
        time.sleep(0.1)

t1 = threading.Thread(target=print_numbers, args=("Thread 1",))
t2 = threading.Thread(target=print_numbers, args=("thread 2",))

print("starting thread...")
t1.start()
t2.start()

t1.join()
t2.join()
print("main program finished")


#next question:--

import threading
import time

counter = 0

def add_million():
    for _ in range(1000000):
        global counter
        counter += 1

t1 = threading.Thread(target=add_million)
t2 = threading.Thread(target=add_million)

print("starting threads...")

t1.start()
t2.start()

t1.join()
t2.join()
print("main program finished")
print(f"counter value: {counter}")


#next question:--

