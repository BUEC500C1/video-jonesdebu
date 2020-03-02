#test keys file against JSON
#if keys are not present we use test using dummy funcitons
#test text based tweets output using JSON
#test image output by filename
#test that a video with the correct name is created
import pytest
from queue_api import muti_thread_queue
def test_placeholder():
    pass

def test_multi_thread_queue():
    def worker1( a, b ):
        print(str(a) + str(b))
        sleep(1)

    def worker2( a, b ):
        print(str(a) + str(b))
        sleep(1)

    def worker3( a, b ):
        print(str(a) + str(b))
        sleep(1)

    q = queue.Queue()
    muti_thread_queue(q, worker1, ('worker1 ', 'is working'))
    muti_thread_queue(q, worker2, ('worker2 ', 'is working'))
    muti_thread_queue(q, worker3, ('worker3 ', 'is working'))
    assert threading.active_count() == 3
