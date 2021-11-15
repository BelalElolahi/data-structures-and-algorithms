from stack_queue_animal_shelter.queue import Queue


class Cat :
    def __init__(self,name) -> None:
        self.name=name
        self.type = 'cat'

class Dog :
    def __init__(self,name) -> None:
        self.name=name
        self.type = 'dog'



class animalShelter :
    def __init__(self) -> None:
       self.dogs = Queue()
       self.cats = Queue()


    def enqueue (self,animal):
        if animal.type == 'cat' :
            self.cats.enqueue(animal)

        if animal.type == "dog":
            self.dogs.enqueue(animal)

    def dequeue(self,pref) :
        if pref == 'cat' :
           return self.cats.dequeue()

        elif pref == "dog":
            return self.dogs.dequeue()
        else :
            return 'Null'

