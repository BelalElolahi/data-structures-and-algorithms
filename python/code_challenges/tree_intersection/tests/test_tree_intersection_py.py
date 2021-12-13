from tree_intersection_py import __version__
import pytest

from tree_intersection_py.tree import BinaryTree , Node
from tree_intersection_py.tree_insertion import tree_intersection

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def creat_firsttree() :
    tree = BinaryTree()
    tree.root = Node(80)
    tree.root.right = Node(70)
    tree.root.left = Node(200)
    tree.root.left.left = Node(66)
    tree.root.left.right = Node(64)

    return tree

@pytest.fixture
def Creat_secondtree() :
    tree2 = BinaryTree()
    tree2.root = Node(20)
    tree2.root.right = Node(10)
    tree2.root.left = Node(200)
    tree2.root.left.left = Node(48)
    tree2.root.left.right = Node(66)
    return tree2




def test_1(creat_firsttree,Creat_secondtree) :
    actual = tree_intersection(creat_firsttree,Creat_secondtree)
    excepted = [200,66]
    assert actual == excepted


def test_2() :
    binarytree = BinaryTree()
    binarytree.root = Node(20)
    binarytree.root.right = Node(10)
    binarytree.root.left = Node(30)
    binarytree.root.left.left = Node(48)
    binarytree.root.left.right = Node(66)

    binarytree2 = BinaryTree()
    binarytree2.root = Node(15)
    binarytree2.root.right = Node(11)
    binarytree2.root.left = Node(12)
    binarytree2.root.left.left = Node(22)
    binarytree2.root.left.right = Node(25)

    actual = tree_intersection(binarytree,binarytree2)
    excepted = 'no intersection'
    assert actual == excepted
