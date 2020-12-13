from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import *
import pytest

def test_dequeue(perp_qu):
    assert perp_qu.dequeue() == 5
    assert perp_qu.dequeue()==7
 

def test_empty_stack(perp_qu):
    assert perp_qu.dequeue() == 5
    assert perp_qu.dequeue()==7
    assert perp_qu.dequeue() == 'Stack is empty'







@pytest.fixture
def perp_qu():
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(7)
    return queue
