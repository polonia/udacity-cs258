from queue_test import *

def test():
    ###Your code here. tabs and space errors
    q = Queue(1)
  assert (q.empty()), "test2 NOT OK: queue is empty, but empty() is false"
	assert (not q.full()), "test2 NOT OK: queue full without elements"
    assert (q.dequeue() == none), "test2 NOT OK: dequeue an empty queue return true"
    ## val_2 = random.randint(1, 40000)
    assert (q.enqueue(10)), "test2 NOT OK: val_1 not enqueued"
    assert (not q.empty()), "test2 NOT OK: queue is not empty, but empty() is true"
	assert (q.full()), "test2 NOT OK: queue full with elements but full() == false"
    assert (not q.enqueue(20)), "test2 NOT OK: val_2 enqueued"
    assert (not q.empty()), "test3 NOT OK: queue is not empty, but empty() is true"
	assert (q.full()), "test3 NOT OK: queue full with elements but full() == false"
    value = q.dequeue()
	assert (value == 10), "test2 NOT OK: dequeue should return 10, NOT FIFO queue"
	assert (q.empty()), "test2 NOT OK: queue is empty, but empty() is false"
	assert (not q.full()), "test2 NOT OK: queue full without elements"
