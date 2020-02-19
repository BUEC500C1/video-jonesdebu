#from __future__ import annotations
from time import sleep
import queue
import subprocess
import threading
#import twitter api function here enter arguments from here
#import queue function and twitter function into a main program
#input = functions as a list and arguments for functions as a list

# create queue with constructor
q = queue.Queue()

#define some dummy worker functions for testing
def worker1( a ):
    print("worker1")
    sleep(1)

def worker2( a ):
    print("worker2")
    sleep(1)

def worker3( a ):
    print("worker3")

func_list = [worker1, worker2, worker3]
arg_list = ['a', 'a', 'a']

def queue_check(q):
    if q.empty() is True:
        print("queue is empty")
    else:
        print()
        print("queue is not empty")
        print("current queue size is" + ' ' + str(q.qsize()))
        print()

# get function and arguments from the queue to be run
#def dest_thread( a ):
    #func, args = q.get()
    #func(*args)
def queue_handler(function_list, argument_list):
    # start a new thread to put functions


    #sleep( 1 )
    q.put( (function_list[0], argument_list[0]) )
    #sleep( 1 )
    q.put( (function_list[1], argument_list[1]) )
    #sleep( 1 )
    q.put( (function_list[2], argument_list[2]) )

    queue_check(q)

    index = 1;
    threads = []
    while q.empty() is False:
        items = q.get()
        func = items[0]
        args = items[1:]
        thread = threading.Thread(target=func, args=args, name=str(index))
        index+=1
        #thread.start()
        threads.append(thread)
        #sleep (1)
        #print(threading.active_count())

    array_length = len(threads)
    for thread in range(array_length):
        print("starting" + ' ' + str(threads[thread].name))
        threads[thread].start()
        print("active thread count:" + ' ' + str(threading.active_count()))
        print()

    sleep (3)

    for thread in range(array_length):
        print(str(threads[thread].name) +' is alive: ' + str(threads[thread].is_alive()))
        print()
    #check to see if all of the threads called are dead
    #becasue we sleep for 3 seconds before checking this they should all be false

    queue_check(q)

    #return statement does not work to execute in thread
    #worker2() # prints nothing
    #a = worker2() # printing a prints what worker2() returns
    #print(a)

    #TODO: 1. Figure out how to get the functions to run aftter getting them from Queue.get()
    # start thread then subprocess library to run thread

    #there are three threads running at the end because workers 1 and 2 are sleeping when worker#3 starts
queue_handler(func_list, arg_list)
