from data_structures_and_algorithms.challenges.quick_sort.quick_sort import *

def test_happy_path():
    actual = quick_sort([8,4,23,42,16,15],0,5)
    expect = [4,8,15,16,23,42]
    assert actual == expect

def test_reverse_sorted():
    actual = quick_sort([20,18,12,8,5,-2],0,5)
    expect = [-2, 5, 8, 12, 18, 20]
    assert actual == expect

def test_few_uniques():
    actual = quick_sort([5,12,7,5,5,7],0,5)
    expect = [5, 5, 5, 7, 7, 12]
    assert actual == expect

def test_nearly_sorted():
    actual = quick_sort([2,3,5,7,13,11],0,5)
    expect = [2, 3, 5, 7, 11, 13]
    assert actual == expect