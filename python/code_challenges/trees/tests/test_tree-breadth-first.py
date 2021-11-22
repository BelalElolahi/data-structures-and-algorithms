import pytest
from trees.tree import BinarySearchTree
from trees.breadth_first import breadth_first


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



def test_tree_breadth_first(creat_tree):
    excepted =  [6, 5, 7, 2, 10, 4]
    actual = breadth_first(creat_tree)
    assert excepted == actual

def test_tree_breadth_first1(creat_tree):
    excepted =  [4, 10, 2, 7, 5, 6]
    actual = breadth_first(creat_tree)
    assert excepted != actual
