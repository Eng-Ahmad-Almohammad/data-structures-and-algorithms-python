from data_structures_and_algorithms.challenges.get_edge.get_edge import *
from data_structures_and_algorithms.data_structures.graph.graph import Graph
import pytest

def test_get_edges(graph_test):
    assert get_edge(graph_test, ['r','c']) == [False,'$0']
    assert get_edge(graph_test, [1,7]) == [False,'$0']
    assert get_edge(graph_test, ['d','a']) == [True,'$9']





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