class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None



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


class Pseudo_queue() :
    def __init__(self) -> None:
        self.stack = Stack()
        self.stack2=Stack()


    def enqueue(self,value):
          self.stack.push(value)
          return self.stack.top.value


    def dequeue(self) :
        current= self.stack.top
        counter =0
        while current :
            self.stack2.push(current.value)
            current=current.next
            counter +=1

        for x in range(counter):
            self.stack.pop()
        first_rmove = self.stack2.pop()

        current2 = self.stack2.top
        while current2 :
            self.stack.push(current2.value)
            current2=current2.next
            counter +=1
            self.stack2.pop()

        return first_rmove


    def __str__(self) :
        output = ""
        if self.stack.is_empty():
             return "this is a  Empty Pseudo_queue"
        current = self.stack.top
        while current != None :
             output += f" {current.value}  "
             current = current.next

        return output












