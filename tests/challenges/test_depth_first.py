from data_structures_and_algorithms.challenges.depth_first.depth_first import depth_first
from data_structures_and_algorithms.data_structures.graph.graph import Graph
import pytest


def test_happy_path(graph_test):
    assert depth_first(graph_test,'a') == ['a','b','d','c']

def test_unattached(graph_test):
    
    assert depth_first(graph_test,'a') == ['a','b','d','c']
    assert depth_first(graph_test,'x') == 'Invalid Input'










@pytest.fixture
def graph_test():
    graph = Graph()
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_edge('a','b',4)
    graph.add_edge('a','d',9)
    graph.add_edge('a','c',3)
    graph.add_edge('b','a',4)
    graph.add_edge('c','a',3)
    graph.add_edge('c','d',6)
    graph.add_edge('d','a',9)
    graph.add_edge('d','b',5)
    graph.add_edge('d','c',6)
    return graph