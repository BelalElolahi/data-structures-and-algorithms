from stack_queue_pseudo import __version__
from stack_queue_pseudo.pesudo_queue import Pseudo_queue


def test_version():
    assert __version__ == '0.1.0'

def test_enqueue():
    qu = Pseudo_queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)


    acutal = qu.enqueue(88)
    excepted = 88

    assert acutal == excepted

def  test_dequeue() :
    qu = Pseudo_queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)



    acutal = qu.dequeue()
    excepted = 1
    assert acutal == excepted


def  test_dequeue1() :
    qu = Pseudo_queue()
    #one the first in
    qu.enqueue(1)
    qu.enqueue(2)

    # one first out
    acutal = qu.dequeue()
    excepted = 1
    assert acutal == excepted

