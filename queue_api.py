#from __future__ import annotations
from time import sleep
import queue
import subprocess
import threading
#import twitter api function here enter arguments from here
#import queue function and twitter function into a main program
#input = queue to be handled function name and arguments

#define some dummy worker functions for testing
def worker1( a, b ):
    print(str(a) + str(b))
    sleep(3)

def worker2( a, b ):
    print(str(a) + str(b))
    sleep(1)

def worker3( a, b ):
    print(str(a) + str(b))

#check the items in the queue (empty or not and if not how many items)
def queue_check(q):
    if q.empty() is True:
        print("queue is empty")
    else:
        print()
        print("queue is not empty")
        print("current queue size is" + ' ' + str(q.qsize()))
        print()

#num_args is the number of arguments per function
def muti_thread_queue(q, func_name, args):

    q.put( func_name, args )

# Get the function and arguments from the queue and add them to a list
    threads = []
    while q.empty() is False:
        func = q.get()
        args = args
        thread = threading.Thread(target=func, args=args, name=str(func_name))
        threads.append(thread)

    array_length = len(threads)
    for thread in range(array_length):
        # Start the threads and display the active numebr of threads each time a new threwad starts
        print("starting" + ' ' + str(threads[thread].name))
        threads[thread].start()
        print()
        print("active thread count:" + ' ' + str(threading.active_count()))
        print()

    for thread in range(array_length):
        if threads[thread].is_alive() is False:
            print(str(threads[thread].name) + ' is dead')





#return statement does not work to execute in thread
#worker2() # prints nothing
#a = worker2() # printing a prints what worker2() returns
#print(a)



q = queue.Queue()
muti_thread_queue(q, worker1, ('worker1 ', 'is working'))
muti_thread_queue(q, worker2, ('worker2 ', 'is working'))
muti_thread_queue(q, worker3, ('worker3 ', 'is working'))


#becasue we sleep for 3 seconds before checking this they should all be false
