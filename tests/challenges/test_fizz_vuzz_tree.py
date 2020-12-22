from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import *
from data_structures_and_algorithms.data_structures.tree.tree import *
def test_fizz_buzz():
    bt = BinaryTree()
    bt.root = Node(15)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = FizzBuzzTree(bt)
    expect = ['FizzBuzz', 7, 2, 'Fizz', 'Buzz', 11, 'Buzz', 'Fizz', 4]
    assert actual == expect


def test_fizz_buzz_with_string():
    bt = BinaryTree()
    bt.root = Node(15)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node('hello')
    actual = FizzBuzzTree(bt)
    expect = ['FizzBuzz', 7, 2, 'Fizz', 'Buzz', 11, 'Buzz', 'Fizz', 'hello']
    assert actual == expect