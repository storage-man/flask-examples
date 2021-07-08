import threading
import time as t
def print_cube(num):
    """
    function to print cube of given num
    """
    i=0
    while i < 100:
        t.sleep(1)
        print("Cube: {}".format(num * num * num))
        i=i+1
def print_square(num):
    """
    function to print square of given num
    """
    j=0
    while j < 100:
        t.sleep(1)
        print("Square: {}".format(num * num))
        j=j+1
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")