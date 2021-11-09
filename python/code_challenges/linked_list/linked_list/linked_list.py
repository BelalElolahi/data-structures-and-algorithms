


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

    # check IF the Value in the LINKED LIST
    def include (self,value) :
         current = self.head
         while current.next != None :
            if current.value == value :
                return True
            current = current.next
         return False




# Addin Method



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


     # Add Before Specifice Value
    def insert_before(self,value,newValue) :
        newnode = Node(newValue)
        current = self.head
        if not self.include(value) :
            raise NameError("value not found")
        while current.next != None :
            if current.next.value == value :
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next


     # Add after Specifice Value
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
        else :
            raise NameError("value not found")


    # return value at index

    #return value form the start
    def KthFromStart (self,indx) :
        if indx < 0 or indx >= self.length() :
            raise NameError("index out of range")

        if self.is_empty() :
            return

        count = 0
        current  = self.head
        while current.next != None :
            if count == indx :
                return current.value
            count +=1
            current = current.next


    #return value form the gevin index
    def kthFromEnd(self,k) :
        len = self.length() -1
        return self.KthFromStart(len - k)




     #link two linked lists
    def zipLists(self, list1, list2):
        current1 = list1.head
        current2 = list2.head

        while current1 != None and current2 != None:

            save_curr1_next = current1.next
            save_curr2_next = current2.next


            current1.next = current2
            current2.next= save_curr1_next


            current1 = save_curr1_next
            current2 = save_curr2_next






    #print Method
    def __str__(self) :
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
    ll2=LinkedList()

    ll.insert(1)
    ll.insert(1)
    ll.insert(1)
    ll.insert(1)
    ll.insert(1)

    ll2.insert(2)
    ll2.insert(2)
    ll2.insert(2)

    print("========================")
    print(ll)

    print("========================")
    print(ll2)
    print("========================")
    ll.zipLists(ll,ll2)
    print(ll)










