import pytest

from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms.data_structures.tree.tree import *

def test_happy_path(tree1,tree2):
    actual = tree_intersection(tree1,tree2)
    expect = {100, 160, 125, 175, 200, 350, 500}
    assert actual == expect

def test_empty_tree():
    bt = BinaryTree()
    bt1 = BinaryTree()
    actual = tree_intersection(bt,bt1)
    expect = 'tree is empty'
    assert actual == expect




@pytest.fixture

def tree1():
    bt = BinaryTree()
    bt.root = Node(150)
    bt.root.right = Node(250)
    bt.root.left = Node(100)
    bt.root.left.left = Node(75)
    bt.root.left.right = Node(160)
    bt.root.left.right.left = Node(125)
    bt.root.left.right.right = Node(175)
    bt.root.right.left = Node(200)
    bt.root.right.right = Node(350)
    bt.root.right.right.left = Node(300)
    bt.root.right.right.right = Node(500)
    return bt

@pytest.fixture
def tree2():
    bt1 = BinaryTree()
    bt1.root = Node(42)
    bt1.root.right = Node(600)
    bt1.root.left = Node(100)
    bt1.root.left.left = Node(15)
    bt1.root.left.right = Node(160)
    bt1.root.left.right.left = Node(125)
    bt1.root.left.right.right = Node(175)
    bt1.root.right.left = Node(200)
    bt1.root.right.right = Node(350)
    bt1.root.right.right.left = Node(4)
    bt1.root.right.right.right = Node(500)
    return bt1