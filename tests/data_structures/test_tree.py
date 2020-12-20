from data_structures_and_algorithms.data_structures.tree.tree import *
import pytest

def test_check_root(prep):
    assert prep.root.data == 5


def test_add_to_left(prep):
    prep.add(1)
    assert prep.root.left.data == 1
    


def test_add_to_right (prep):
    prep.add(10)
    assert prep.root.right.data == 10

def test_preOrder(prep):
    prep.add(1)
    prep.add(10)
    
    assert prep.preOrder() == [5,1,10]

def test_inOrder(prep):
    prep.add(1)
    prep.add(10)
    
    assert prep.inOrder() == [1,5,10]

def test_postOrder(prep):
    prep.add(1)
    prep.add(10)
    
    assert prep.postOrder() == [1,10,5]



def test_maximum_value():
    bt = BinaryTree()
    bt.root = Node(4)
    bt.root.right = Node(9)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(6)
    bt.root.left.left = Node(3)
    bt.root.left.right = Node(8)
    assert bt.find_maximum_value() == 9




@pytest.fixture
def prep():
    bts = BinarySearchTree()
    bts.add(5)
  
    return bts