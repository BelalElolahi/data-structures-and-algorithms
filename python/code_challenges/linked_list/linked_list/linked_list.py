
class Node :
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList :

    def __init__(self) -> None:
         self.head = None

     #  check if the Linked list is empty
    def is_empty(self) :
        if self.head == None :
            return True
        else:
            return False


    def length(self) :
        count = 0

        if self.is_empty():
            return 0
        current = self.head
        while current.next !=None:
            count +=1
            current= current.next
        return count

    #add element at first of LINKED LIST
    def insert(self,value) :
         node =Node(value)

         if self.is_empty() :
             self.head = node
             return

         node.next = self.head
         self.head = node



    # add element at the end of LINKED LIST
    def append(self,value) :
        node = Node(value)

        #check if the Linked list is empty
        # make the head = node
        if self.is_empty() :
            self.insert(value)
            return

        # add the value at the end
        current = self.head
        while current.next != None :
            current = current.next
            print(current)
        current.next = node

    def insert_at(self,value,index) :
        node =Node(value)
        if self.is_empty() :
            return


        count = 0
        current  = self.head
        if index == 0 :
            self.insert(value)
        while current.next != None :
            if count == index - 1:
                node.next = current.next
                current.next = node
                return
            count +=1
            current = current.next
        self.append(value)

    def include (self,value) :
         current = self.head
         while current.next != None :
            if current.value == value :
                return True
            current = current.next
         return False

    def insert_after(self,value,newValue) :
        node = Node(newValue)
        if self.include(value) :
            current = self.head
            while current.next != None :
                if current.value == value :
                    node.next = current.next
                    current.next = node
                    return
                current = current.next












    def __str__(self):
        outout= ""

        if self.is_empty():
            return f" Head -> Null "
        current = self.head
        while current.next != None :
            outout += f" ""{"" "+str(current.value)+" ""}""  -> "
            current = current.next
        outout += "NULL"
        return outout

if __name__=="__main__" :
    ll=LinkedList()
    ll.insert(1)
    ll.insert(1)
    ll.insert(30)
    ll.insert(20)
    ll.insert(10)
    print(ll)
    print(ll.length())

    print(ll.include(3))
    print(ll.include(20))
    print(ll.include(1))
    print(ll.include(7))

    print("======================================== ")
    ll.insert_after(30,4)
    ll.insert_after(10,4)
    print(ll)


