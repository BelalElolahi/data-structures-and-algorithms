from hashtable.linked_list import LinkedList


class HashTable () :
    def __init__(self,size=1024) -> None:
        self.size =size
        self.map=[None]*size

    def hash(self, key) :
        sum_of_asccii = 0
        for ch in key :
          asccii_of_ch = ord(ch)
          sum_of_asccii +=asccii_of_ch

        temp_value  = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key



    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = value
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
            else:
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=chain
                chain.add(existing_pair)
                chain.add(new_pair)

    def get(self,key):
        index = self.hash(key)
        if not self.map[index] :
            return "Null"
        return self.map[index]

    def contains(self,key):
        index = self.hash(key)
        if self.map[index]:
            print(True)
            return True

        else :
            print(False)
            return False







