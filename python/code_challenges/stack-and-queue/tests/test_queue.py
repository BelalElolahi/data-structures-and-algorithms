from stack_and_queue.queue import Queue


def test_is_empty () :
    queue = Queue()
    expected = True
    actual = queue.is_empty()
    assert expected == actual


def  test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("ABC")
    expected = "ABC"
    actual = queue.rear.value
    assert expected == actual



def  test_dequeue() :
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("ABC")

    expected = 1
    actual = queue.dequeue()
    assert expected == actual

def test_empty_a_stack_after_multiple_dequeues() :
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("ABC")

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    expected = True
    actual = queue.is_empty()
    assert expected == actual




def test_peek () :
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("ABC")
    expected = 1
    actual = queue.peek()
    assert expected == actual

def test_calling_or_peek_on_empty_queues() :
    queue = Queue()

    actual = queue.peek()
    expected = "this is a  Empty queue"
    assert expected == actual






