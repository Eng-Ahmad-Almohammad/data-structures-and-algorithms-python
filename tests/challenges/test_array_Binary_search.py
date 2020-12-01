import data_structures_and_algorithms.challenges.array_binary_search.array_binary_search as func


def test_sortting():
    actual = func.sorting([1,2,5,7],)
    expected = [1,2,5,7]
    assert actual==expected


def test_value():
    actual = func.BinarySearch([-6,3,9,12,75],3)
    expected = 1
    assert actual==expected 

def test_valid_value():
    actual = func.BinarySearch([-6,3,9,12,75],345)
    expected = -1
    assert actual==expected