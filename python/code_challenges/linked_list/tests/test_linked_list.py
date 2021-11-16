from linked_list import __version__
from linked_list.linked_list import LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_append() :
    ll=LinkedList()


    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    actual =ll.head.value
    excepted =  1
    assert actual == excepted



def test_append_1() :
    ll=LinkedList()


    ll.append("ABCD")

    actual =ll.head.value
    excepted = 'ABCD'
    assert actual == excepted


def test_include():
    ll=LinkedList()
    ll.append('ACD')
    ll.append(4)
    ll.append(5)
    ll.append("ABCD")

    actual =ll.include("ACD")
    excepted = True
    assert actual == excepted

def test_Not_include():
    ll=LinkedList()
    ll.append(3)
    ll.append(4)


    actual =ll.include('11')
    excepted = False
    assert actual == excepted


def test_collection_of_all_the_values_that_exist_in_the_linked_list():
    ll=LinkedList()

    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)

    actual =ll.__str__()
    excepted =  ' { 6 }  ->  { 5 }  ->  { 4 }  ->  { 3 }  ->  { 2 }  ->  { 1 }  -> NULL'
    assert actual == excepted

def test_instantiate_an_empty_linked_list():
    ll=LinkedList()

    actual =ll.is_empty()
    excepted = True
    assert actual == excepted





