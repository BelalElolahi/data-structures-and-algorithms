from graph import __version__

import pytest

from graph.graph_implement import Graph
def test_version():
    assert __version__ == '0.1.0'




@pytest.fixture
def create_graph():
    graph = Graph()
    graph.add_node('z')
    graph.add_node('x')
    graph.add_node('b')
    graph.add_node('k')
    graph.add_node('l')
    graph.add_edge('z','x')
    graph.add_edge('z','k')
    graph.add_edge('k','b')
    graph.add_edge('b','l',)
    return graph


def test_add_to_graph(create_graph):
   actual = create_graph.get_nodes()
   excepted = ['z', 'x', 'b', 'k', 'l']
   assert actual == excepted


def test_add_ege(create_graph):
    actual = create_graph.get_neighbors('z')
    excepted= ['x', 'k']
    assert actual == excepted

def test_get_Nodes (create_graph):
   actual = create_graph.get_nodes()
   excepted = ['z', 'x', 'b', 'k', 'l']
   assert actual == excepted

def test_get_neighbors(create_graph):
    actual = create_graph.get_neighbors('k')
    excepted= ['b']
    assert actual == excepted

def test_graph_size(create_graph):
    actual = create_graph.size()
    excepted= 5
    assert actual == excepted

def test_add__one_node () :
    graph1 = Graph()
    graph1.add_node('DD')
    actual = graph1.get_nodes()
    excepted = ['DD']
    assert actual == excepted


def test_empty_graph () :
    graph2 = Graph()
    actual = graph2.get_nodes()
    excepted = "Null"
    assert actual == excepted
