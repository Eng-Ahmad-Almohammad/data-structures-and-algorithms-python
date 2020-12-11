from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *
import pytest

def test_push_to_stack():
    stack = Stack()
    stack.push(5)
    assert stack.top.data == 5
    stack.push(7)
    assert stack.top.data == 7
    
def test_pop_from_stack(prep_st):
    assert prep_st.pop()==7
    assert prep_st.top.data ==5
    assert prep_st.pop()==5
    assert prep_st.pop() == 'Stack is empty'

def test_peek_from_stack(prep_st):
    assert prep_st.peek()== 7
    assert prep_st.pop()== 7
    assert prep_st.peek()==5
    assert prep_st.pop()==5
    assert prep_st.peek()=='Stack is empty'



def test_enqueue_to_queue():
    queue = Queue()
    queue.enqueue(5)
    assert queue.front.data == 5
    queue.enqueue(7)
    assert queue.rear.data == 7
    
def test_dequeue_from_queue(prep_que):
    assert prep_que.dequeue()==5
    assert prep_que.front.data ==7
    assert prep_que.dequeue()==7
    assert prep_que.dequeue() == 'Queue is empty'

def test_peek_from_queue(prep_que):
    assert prep_que.peek()== 5
    assert prep_que.dequeue()== 5
    assert prep_que.peek()==7
    assert prep_que.dequeue()==7
    assert prep_que.peek()=='Queue is empty'





@pytest.fixture
def prep_st():
    stack = Stack()
    stack.push(5)
    stack.push(7)
    return stack

@pytest.fixture
def prep_que():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(7)
    return queue