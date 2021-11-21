from trees import __version__, tree

import pytest
from trees.node import Node
from trees.tree import BinarySearchTree, BinaryTree


def test_version():
    assert __version__ == '0.1.0'

"""
    A
  B   C
D    F  E

pre =['A','B','D','C','F','E']
in-order = ['B','D','A','C','F','E']
post = ['D','B','F','E','C','A']


"""

def test_instantiate_an_empty_tree ():
     tree = BinaryTree()

     excepted = True
     actual = tree.is_empty()

     assert excepted == actual

def test_instantiate_a_tree_with_a_single_root_node():
    tree = BinarySearchTree()
    tree.add(10)

    actual = tree.root.value
    excepted = 10
    assert actual == excepted

def  test_add_a_left_child_and_right_child_to_a_single_root_node():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(5)
    tree1.add(15)

    actual =  [tree1.root.value,tree1.root.left.value,tree1.root.right.value]
    excepted = [10,5,15]
    assert actual == excepted
    pass


def test_return_a_collection_from_a_preorder_traversal(creat_tree):
    excepted = ['A','B','D','C','F','E']
    actual = creat_tree.pre_order(creat_tree.root)
    assert excepted == actual

def test_return_a_collection_from_an_inorder_traversal(creat_tree):
    excepted = ['B','D','A','C','F','E']
    actual = creat_tree.in_order(creat_tree.root)
    assert excepted == actual


def test_return_a_collection_from_an_postorder_traversal(creat_tree):
    excepted =  ['D','B','F','E','C','A']
    actual = creat_tree.post_order(creat_tree.root)
    assert excepted == actual


def test_contains():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(5)
    tree1.add(15)

    actual = tree1.contains(10)
    excepted = True
    assert actual == excepted
    pass









@pytest.fixture
def creat_tree() :
   tree =BinaryTree()
   tree.root =Node("A")
   tree.root.left=Node("B")
   tree.root.right=Node("C")
   tree.root.left.left=Node("D")
   tree.root.right.right=Node("E")
   tree.root.right.left=Node("F")
   return tree


