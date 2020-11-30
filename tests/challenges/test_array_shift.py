import data_structures_and_algorithms.challenges.array_shift.array_shift as func

def test_even_number_of_content():
    actual = func.insertShiftArray([1,2,3,4],5)
    expected  = [1,2,5,3,4]
    assert actual == expected

def test_odd_number_of_content():
    actual = func.insertShiftArray([1,2,3,4,5],6)
    expected  = [1,2,3,6,4,5]
    assert actual == expected


