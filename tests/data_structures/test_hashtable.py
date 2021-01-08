from data_structures_and_algorithms.data_structures.hashtable.hashtable import Node, LinkedList, Hashtable
import pytest  


def test_adding_to_hashtable(hashh):
    assert hashh.map[hashh.hash('name')].head.value == 'Ahmad'
    assert hashh.map[hashh.hash('color')].head.value == 'Blue'
    assert hashh.map[hashh.hash('age')].head.value == 24
    assert hashh.map[hashh.hash('sport')].head.value == 'Football'
    assert hashh.map[hashh.hash('None')] == None
 

def test_handel_collision(hashh):
    assert hashh.map[hashh.hash('coldu')].head.value == 344
    assert hashh.map[hashh.hash('cloud')].head.next.value == 34
    assert hashh.map[hashh.hash('could')].head.next.next.value == 67

def test_get(hashh):
    assert hashh.get('name')== 'Ahmad'
    assert hashh.get('color')== 'Blue'
    assert hashh.get('age')== 24
    assert hashh.get('sport')== 'Football'
    assert hashh.get('could')== 67
    assert hashh.get('cloud')== 34
    assert hashh.get('coldu')== 344

def test_contains(hashh):
    assert hashh.contains('name') == True
    assert hashh.contains('color') == True
    assert hashh.contains('age') == True
    assert hashh.contains('sport') == True
    assert hashh.contains('could') == True
    assert hashh.contains('cloud') == True
    assert hashh.contains('coldu') == True
    assert hashh.contains('False') == False


@pytest.fixture
def hashh():
    ht = Hashtable(1024)
    ht.add('name', 'Ahmad')
    ht.add('color', 'Blue')
    ht.add('age', 24)
    ht.add('sport', 'Football')
    ht.add('could', 67)
    ht.add('cloud', 34)
    ht.add('coldu', 344)
    return ht