from data_structures_and_algorithms.data_structures.linked_list.linked_list import *
from data_structures_and_algorithms.challenges.ll_zip.ll_zip import *
import pytest


def test_happy_path(prep_tt1,prep_tt2):
    actual = str(zipLists(prep_tt1,prep_tt2))
    expected = f'{{7}}->{{9}}->{{5}}->{{4}}->NULL'
    assert actual==expected


def test_one_of_lists_longer_than_other():
    ll1 = LinkedList()
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(9)
    ll2.append(4)

    actual = str(zipLists(ll1,ll2))
    expected = f'{{5}}->{{9}}->{{4}}->NULL'
    assert actual==expected


def test_one_of_lists_is_empty():
    ll1 = LinkedList()
    
    ll2 = LinkedList()
    ll2.append(9)
    ll2.append(4)

    actual = str(zipLists(ll1,ll2))
    expected = f'{{9}}->{{4}}->NULL'
    assert actual==expected




@pytest.fixture
def prep_tt1():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    return ll

@pytest.fixture
def prep_tt2():
    ll = LinkedList()
    ll.insert(4)
    ll.insert(9)
    return ll


