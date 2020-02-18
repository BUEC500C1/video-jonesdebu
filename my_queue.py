#from __future__ import annotations
from time import sleep
import queue
import subprocess
import threading

#need to import the twitter api function and pass the arguments as arguments to this queue starter function

# create queue with constructor
q = queue.Queue()

#define some dummy worker functions for testing
def worker1( a ):
    print("worker1")

def worker2( a ):
    print("worker2")

def worker3( a ):
    print("worker3")

# get function and arguments from the queue to be run
#def dest_thread( a ):
    #func, args = q.get()
    #func(*args)

# start a new thread to put functions

print("start")
#sleep( 1 )
q.put( (worker1, 'a') )
#sleep( 1 )
q.put( (worker2, 'a') )
#sleep( 1 )
q.put( (worker3, 'a') )

index = 1;
threads = []
while q.empty() is False:
    items = q.get()
    func = items[0]
    args = items[1:]
    thread = threading.Thread(target=func, args=args)
    thread.start()
    threads.append(thread)

print("stop")

if q.empty() is True:
    print("queue is empty")
else:
    print("queue is not empty")
    print(q.qsize())

#return statement does not work to execute in thread
#worker2() # prints nothing
#a = worker2() # printing a prints what worker2() returns
#print(a)

#TODO: 1. Figure out how to get the functions to run aftter getting them from Queue.get()
# start thread then subprocess library to run thread
