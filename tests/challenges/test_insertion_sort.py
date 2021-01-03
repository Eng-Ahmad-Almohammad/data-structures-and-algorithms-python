from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import *

def test_insertion_sort():
    actual = insertion_sort([8,4,23,42,16,15])
    expect = [4, 8, 15, 16, 23, 42]
    assert actual == expect

def test_insertion_sort1():
    actual = insertion_sort([20,18,12,8,5,-2])
    expect = [-2, 5, 8, 12, 18, 20]
    assert actual == expect

def test_insertion_sort2():
    actual = insertion_sort([5,12,7,5,5,7])
    expect = [5, 5, 5, 7, 7, 12]
    assert actual == expect

def test_insertion_sort3():
    actual = insertion_sort([2,3,5,7,13,11])
    expect = [2, 3, 5, 7, 11, 13]
    assert actual == expect

