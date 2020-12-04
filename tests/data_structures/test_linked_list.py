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



@pytest.fixture
def prep_tt():
    tt = LinkedList()
    tt.insert(5)
    tt.insert(7)
    return tt
