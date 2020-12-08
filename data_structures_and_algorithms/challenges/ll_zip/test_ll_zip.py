from data_structures_and_algorithms.challenges.ll_zip.ll_zip import *
from data_structures_and_algorithms.data_structures.linked_list.linked_list import *
import pytest
def test_values(prep_tt1,prep_tt2):
    actual = zipLists(prep_tt1,prep_tt2)
    expected = f'{{7}}->{{9}}->{{7}}->{{3}}->NULL'
    assert actual == expected








@pytest.fixture
def prep_tt1():
    tt = LinkedList()
    tt.append(5)
    tt.append(7)
    
    return tt


@pytest.fixture
def prep_tt2():
    tt = LinkedList()
    tt.append(9)
    tt.append(3)
    
    return tt