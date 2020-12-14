from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest


def test_enqueu(prep_qu):
    assert prep_qu.front.name == 'Alex'
    assert prep_qu.front.next.name == 'sherry'
    assert prep_qu.front.next.next.name == 'soso'
    assert prep_qu.front.next.next.next.name == 'JJ'

def test_dequeue(prep_qu):
    assert prep_qu.dequeue('dog')== 'Alex'
    assert prep_qu.dequeue('dog')== 'JJ'





@pytest.fixture
def prep_qu():
    shelter = AnimalShelter()
    shelter.enqueue(Dog('Alex'))
    shelter.enqueue(Cat('sherry'))
    shelter.enqueue(Cat('soso'))
    shelter.enqueue(Dog('JJ'))
    return shelter
