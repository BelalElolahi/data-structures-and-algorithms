import pytest
from graph.graph_implement import Graph





@pytest.fixture
def create_graph():

    graph = Graph()
    graph.add_node('pandora')
    graph.add_node('arendelle')
    graph.add_node('metroville')
    graph.add_node('narina')
    graph.add_node('naboo')
    graph.add_node('manstropolis')
    graph.add_edge('pandora','arendelle')
    graph.add_edge('pandora','metroville')
    graph.add_edge('arendelle','pandora')
    graph.add_edge('arendelle','metroville')
    graph.add_edge('arendelle','manstropolis')
    graph.add_edge('metroville','pandora')
    graph.add_edge('metroville','arendelle')
    graph.add_edge('metroville','manstropolis')
    graph.add_edge('metroville','naboo')
    graph.add_edge('metroville','narina')
    graph.add_edge('narina','metroville')
    graph.add_edge('narina','naboo')
    graph.add_edge('naboo','narina')
    graph.add_edge('naboo','metroville')
    graph.add_edge('naboo','manstropolis')
    graph.add_edge('manstropolis','naboo')
    graph.add_edge('manstropolis','arendelle')
    graph.add_edge('manstropolis','metroville')


    return graph


def test_BSF (create_graph) :
   actual = create_graph.BFS('pandora')
   excepted =['pandora', 'arendelle', 'metroville', 'manstropolis', 'naboo', 'narina']
   assert actual == excepted


def test_BFS_1():
    graph1 = Graph()
    graph1.add_node('z')
    graph1.add_node('x')
    graph1.add_node('b')
    graph1.add_node('k')
    graph1.add_node('l')
    graph1.add_edge('z','x')
    graph1.add_edge('z','k')
    graph1.add_edge('k','b')
    graph1.add_edge('b','l',)

    actual = graph1.BFS('z')
    excepted = ['z', 'x', 'k', 'b', 'l']
    assert actual == excepted

