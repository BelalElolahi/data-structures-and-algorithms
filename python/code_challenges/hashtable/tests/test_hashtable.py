from hashtable.hash_map import HashTable
import pytest
from hashtable import __version__


def test_version():
    assert __version__ == '0.1.0'



@pytest.fixture
def create_hashTabel() :
    hashtable= HashTable()
    hashtable.add("Alli",30)
    hashtable.add("Sami",30)
    hashtable.add("Yaseen",55)
    hashtable.add("Alli",55)

    return hashtable


def test_add(create_hashTabel) :
    actual = create_hashTabel.contains("Alli")
    excepted = True
    assert actual == excepted

def test_get(create_hashTabel) :
    actual = create_hashTabel.get("Yaseen")
    excepted = 55
    assert actual == excepted

def test_Key_dose_not_exisit(create_hashTabel):
    actual = create_hashTabel.get("mohamed")
    excepted = "Null"
    assert actual == excepted

def test_collision(create_hashTabel) :
    actual = create_hashTabel.get("Alli").__str__()
    excepted = [30, ['Alli', 55]]
    assert actual == excepted

def test_collision_retrieve(create_hashTabel):
  actual = create_hashTabel.get('Alli').__str__()[0]
  excepted =30

  actual2 = create_hashTabel.get('Alli').__str__()[1][1]
  excepted2 = 55

  assert (actual == excepted and actual2 == excepted2)


def test_hash(create_hashTabel):
    actual = create_hashTabel.hash("Yaseen")
    excepted = 383
    assert actual == excepted














