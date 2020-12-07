from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList

import pytest

def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)



def test_insert(prep_tt):
    # head - Node(7) -> Node(5) -> None
    assert prep_tt.head.value == 7
    assert prep_tt.head.next.next == None
    assert prep_tt.head.next.value == 5



def test_includes(prep_tt):
    assert prep_tt.includes(7)==True
    assert prep_tt.includes(-5)==False
    assert prep_tt.includes('')==False

   
def test_str(prep_tt):
    assert str(prep_tt) == f'{{7}}->{{5}}->NULL'

def test_insert_before(prep_tt):
    prep_tt.insert_before(5,9)
    assert prep_tt.head.value == 7
    assert prep_tt.head.next.value == 9
    assert prep_tt.head.next.next.value == 5

def test_insert_after(prep_tt):
    prep_tt.insert_after(5,9)
    assert prep_tt.head.value == 7
    assert prep_tt.head.next.value == 5
    assert prep_tt.head.next.next.value == 9

def test_kth_from_end_if_k_greter_than_the_length(prep_tt):
    actual = prep_tt.kth_from_end(12)
    expected = 'Your variable is larger than the list length'
    assert actual==expected

def test_kth_from_end_if_k_is_equal_to_length(prep_tt):
    actual =  prep_tt.kth_from_end(1)
    expected = 7
    assert actual== expected

def test_kth_from_end_if_k_is_negative(prep_tt):
    actual = prep_tt.kth_from_end(-3)
    expected = 'You should input postive value'
    assert actual==expected

def test_kth_from_end_when_linked_list_length_is_one():
    tt = LinkedList()
    tt.insert(5)
    assert tt.kth_from_end(0)==5

def test_kth_from_end(prep_tt):
    actual = prep_tt.kth_from_end(1)
    expected = 7
    assert actual==expected





@pytest.fixture
def prep_tt():
    tt = LinkedList()
    tt.insert(5)
    tt.insert(7)
    
    return tt

