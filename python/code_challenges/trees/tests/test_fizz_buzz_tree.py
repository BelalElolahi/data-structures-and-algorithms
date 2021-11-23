import pytest
from trees.tree_fizz_buzz import fizz_buzz_tree
from trees.node import Node
from trees.tree import BinaryTree


@pytest.fixture
def creat_tree() :
   tree =BinaryTree()
   tree.root =Node(3)
   tree.root.left=Node(5)
   tree.root.right=Node(5)
   tree.root.left.left=Node(15)
   tree.root.right.right=Node(3)
   tree.root.right.left=Node(15)
   return tree
@pytest.fixture
def creat_tree1() :
   tree =BinaryTree()
   tree.root =Node(2)
   tree.root.left=Node(5)
   tree.root.right=Node(4)
   tree.root.left.left=Node(15)
   tree.root.right.right=Node(7)
   tree.root.right.left=Node(15)
   return tree



def test_fizz_buzz_tree(creat_tree):
    result = fizz_buzz_tree(creat_tree)

    excepted = ['Fizz', 'Buzz', 'Buzz', 'FizzBuzz', 'Fizz', 'FizzBuzz']

    actual = result.pre_order(result.root)
    assert excepted == actual

def test_fizz_buzz_tree_1(creat_tree):
    result = fizz_buzz_tree(creat_tree)

    excepted = ['Fizz', 'Fizz', 'Buzz', 'FizzBuzz', 'Fizz', 'FizzBuzz']

    actual = result.pre_order(result.root)
    assert excepted != actual



def test_fizz_buzz_tree_2(creat_tree1):
    result = fizz_buzz_tree(creat_tree1)

    excepted = ['2', 'Buzz', '4', '7', 'FizzBuzz', 'FizzBuzz']

    actual = result.pre_order(result.root)
    assert excepted == actual





