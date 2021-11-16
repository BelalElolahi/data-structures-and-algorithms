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


    def length(self) :
        current = self.top
        count = 0
        if self.is_empty() :
            return 0
        while current :
            count += 1
            current = current.next
        return count


def validate_brackets (str) :
    stack = Stack()
    opening_list = ["[","{","("]
    closing_list = ["]","}",")"]

    for ch in str:
        if ch in opening_list:
            stack.push(ch)
        elif ch in closing_list:
            pos = closing_list.index(ch)
            if stack.length() > 0 and opening_list[pos] == stack.peek() :
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False



if __name__=="__main__":
    validate_brackets('{[()]}')

    validate_brackets('{[(')
    validate_brackets('{[()]}')
    validate_brackets('{[(')


