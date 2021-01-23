from data_structures_and_algorithms.data_structures.graph.graph import *
import pytest



def test_adding(graph_test):
    actual = graph_test.add_node('e')
    expect = 'e'
    assert actual==expect


def test_get_neighbors(graph_test):
    actual = graph_test.get_neighbors('a')
    expect = [[4,'b'],[9,'d'],[3,'c']]
    assert expect == actual


def test_size(graph_test):
    actual = graph_test.size()
    expect = 4
    assert actual == expect


    
def test_graph_with_one_node():
    graph = Graph()
    assert graph.add_node('a') == 'a'
    assert graph.get_neighbors('a') == []
    assert graph.size() == 1
    assert graph.get_neighbors('v') == 'Node does not exist'


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