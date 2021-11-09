from linked_list import __version__
from linked_list.linked_list import LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_Zip_lists_tow() :
    ll=LinkedList()
    ll2=LinkedList()

    ll.insert(1)
    ll.insert(3)
    ll.insert(1)
    ll.insert(3)
    ll.insert(1)
    ll.insert(3)
    ll.insert(1)
    ll.insert(3)

    ll2.insert(20)
    ll2.insert(30)
    ll2.insert(40)
    ll2.insert(50)
    ll2.insert(60)
    ll2.insert(70)
    ll2.insert(80)
    ll2.insert(90)

    ll.zipLists(ll,ll2)


    actual =ll.__str__()
    excepted = ' { 3 }  ->  { 90 }  ->  { 1 }  ->  { 80 }  ->  { 3 }  ->  { 70 }  ->  { 1 }  ->  { 60 }  ->  { 3 }  ->  { 50 }  ->  { 1 }  ->  { 40 }  ->  { 3 }  ->  { 30 }  ->  { 1 }  -> NULL'
    assert actual == excepted




def test_Zip_lists_() :
    ll=LinkedList()
    ll2=LinkedList()
    ll.insert(1)
    ll.insert(3)
    ll.insert(1)
    ll.insert(3)
    ll.insert(1)
    ll.insert(3)
    ll.insert(1)
    ll.insert(3)

    ll2.insert(20)
    ll2.insert(30)
    ll2.insert(40)
    ll.zipLists(ll,ll2)


    actual =ll.__str__()
    excepted = ' { 3 }  ->  { 40 }  ->  { 1 }  ->  { 30 }  ->  { 3 }  ->  { 20 }  ->  { 1 }  ->  { 3 }  ->  { 1 }  ->  { 3 }  -> NULL'
    assert actual == excepted





