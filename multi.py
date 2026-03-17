import multiprocessing
import time

def heavy_computation():
    print("starting doing compuitation...")
    time.sleep(2)
    print("computation done!")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=heavy_computation)
    p2 = multiprocessing.Process(target=heavy_computation)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print("main program finished!")


#next question:--

import os

def who_am_i():
    print(f"my process id is {os.getpid()}")

if __name__ == "__main__":
    print(f"main process id is {os.getpid()}")

    p1 = multiprocessing.Process(target=who_am_i)
    p2 = multiprocessing.Process(target=who_am_i)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("main program finished!")