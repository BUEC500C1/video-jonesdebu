from __future__ import annotations
import _thread
from time import sleep
import queue
import subprocess



# create queue with constructor
q = queue.Queue(0)

#define some dummy worker functions for testing
def worker1( b ):
    return "worker1"

def worker2( b ):
    return "worker2"

def worker3( b ):
    return "worker3"

# get function and arguments from the queue to be run
def dest_thread( a ):
    func, args = q.get()
    func(*args)
# start a new thread to put functions
#dest_thread("a")
print("start")
#sleep( 1 )
q.put( (worker1, "b") )
#sleep( 1 )
q.put( (worker2, "b") )
#sleep( 1 )
q.put( (worker3, "b") )

func, args = q.get()
func(*args)

print("stop")

if q.empty() is True:
    print("queue is empty")
else:
    print("queue is not empty")
    print(q.qsize())

#TODO: 1. Figure out how to get the functions to run aftter getting them from Queue.get()
