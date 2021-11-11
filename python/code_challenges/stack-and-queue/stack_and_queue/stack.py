from stack_and_queue.node import Node



class Stack :
    def __init__(self) -> None:
        self.top = None


    def push(self,value) :
        new_node = Node(value)

        if self.is_empty() :
             self.top = new_node
        else :
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise NameError(" You try to dequeue from empty queue ")
        else :
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value



    def is_empty(self):
        return self.top == None



    def peek (self) :
        if self.is_empty():
            return "this is a  Empty Stack"
        else :
          return self.top.value









