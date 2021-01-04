from data_structures_and_algorithms.challenges.merge_sort.merge_sort import *

def test_merge():
    actual = merge([5],[2],[5,2])
    expect = [2,5]
    assert actual == expect


def test_merge_sort():
    actual = merge_sort([92,85,49,21,15,5,-10])
    expect = [-10, 5, 15, 21, 49, 85, 92]
    assert actual == expect

def test_merge_sort1():
    actual = merge_sort([92,85,85,85,15,5,-10])
    expect = [-10, 5, 15, 85, 85, 85, 92]
    assert actual == expect