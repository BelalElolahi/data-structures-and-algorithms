from stack_and_queue.stack import Stack


def test_is_empty () :
    stack = Stack()

    expected = True
    actual = stack.is_empty()
    assert expected == actual


def  test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("ABC")

    expected = "ABC"
    actual = stack.top.value
    assert expected == actual

def  test_pop() :
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("ABC")

    expected = "ABC"
    actual = stack.pop()
    assert expected == actual
def test_empty_a_stack_after_multiple_pops() :
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("ABC")

    stack.pop()
    stack.pop()
    stack.pop()

    expected = True
    actual = stack.is_empty()
    assert expected == actual



def test_peek () :
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("ABC")

    expected = "ABC"
    actual = stack.peek()
    assert expected == actual


def test_calling_or_peek_on_empty_stack() :
    stack = Stack()

    expected = "this is a  Empty Stack"
    actual = stack.peek()
    assert expected == actual






