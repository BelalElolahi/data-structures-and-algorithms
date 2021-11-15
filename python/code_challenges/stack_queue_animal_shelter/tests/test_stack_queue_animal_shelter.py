from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.animalShelter import Cat, Dog, animalShelter


def test_version():
    assert __version__ == '0.1.0'



def test_enqueue_animal_cat():
    que=animalShelter()
    cat = Cat("mshmsh")
    cat2 = Cat("lolo")
    dog = Dog("jack")
    dog2 = Dog("poby")


    que.enqueue(cat)
    que.enqueue(dog)
    que.enqueue(dog2)
    que.enqueue(cat2)
    excepted = que.cats.front.value.type
    actual = 'cat'
    assert excepted  == actual

def test_enqueue_animal_dog():
    que=animalShelter()
    cat = Cat("mshmsh")
    cat2 = Cat("lolo")
    dog = Dog("jack")
    dog2 = Dog("poby")


    que.enqueue(cat)
    que.enqueue(dog)
    que.enqueue(dog2)
    que.enqueue(cat2)
    excepted = que.dogs.front.value.type
    actual = 'dog'
    assert excepted  == actual

def test_dequeue_animal_cat():
    que=animalShelter()
    cat = Cat("mshmsh")
    cat2 = Cat("lolo")
    dog = Dog("jack")
    dog2 = Dog("poby")


    que.enqueue(cat)
    que.enqueue(dog)
    que.enqueue(dog2)
    que.enqueue(cat2)

    excepted = que.dequeue("cat").name
    actual = 'mshmsh'

    assert excepted  == actual

def test_dequeue_animal_dog():
    que=animalShelter()
    cat = Cat("mshmsh")
    cat2 = Cat("lolo")
    dog = Dog("jack")
    dog2 = Dog("poby")


    que.enqueue(cat)
    que.enqueue(dog)
    que.enqueue(dog2)
    que.enqueue(cat2)

    excepted = que.dequeue("dog").name
    actual = 'jack'

    assert excepted  == actual

def test_dequeue_not_dog_cat() :
    que=animalShelter()
    cat = Cat("mshmsh")
    cat2 = Cat("lolo")
    dog = Dog("jack")
    dog2 = Dog("poby")


    que.enqueue(cat)
    que.enqueue(dog)
    que.enqueue(dog2)
    que.enqueue(cat2)

    excepted = que.dequeue("tiger")
    actual = 'Null'
    assert excepted  == actual

