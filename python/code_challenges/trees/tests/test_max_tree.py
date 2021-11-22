import pytest
from trees.tree import BinarySearchTree

@pytest.fixture
def creat_tree() :
   tree =BinarySearchTree()
   tree.add(6)
   tree.add(5)
   tree.add(7)
   tree.add(2)
   tree.add(10)
   tree.add(4)
   return tree

def test_max_value_1(creat_tree):
    excepted =  10
    actual = creat_tree.tree_max()
    assert excepted == actual


def test_max_value(creat_tree):
    creat_tree.add(11)
    excepted =  11
    actual = creat_tree.tree_max()
    assert excepted == actual




