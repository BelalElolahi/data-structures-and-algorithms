from trees.tree import BinarySearchTree


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None



class Queue :
    def __init__(self) -> None:
         self.front = None
         self.rear = None

    def  enqueue(self,value):
        new_node = Node(value)
        if self.is_empty() :
            self.front = new_node
            self.rear =new_node
        else :
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise NameError(" You try to dequeue from empty queue ")
        elif self.rear==self.front:
            temp = self.front
            self.rear =  None
            self.front = None
            return temp.value
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value


    def peek(self) :
        if self.is_empty():
            return "this is a  Empty queue"
        else :
           return self.front.value

    def is_empty(self):
       return self.front == None


def breadth_first(tree):

    que_breadth = Queue()
    breadth = []

    curr = tree.root
    que_breadth.enqueue(curr)

    while que_breadth.front :
        curr =que_breadth.dequeue()
        breadth.append(curr.value)

        if curr.left  :
            que_breadth.enqueue(curr.left)
        if curr.right :
            que_breadth.enqueue(curr.right)
    return breadth








