from graph.graph_implement import Graph
from graph.graph_implement import business_trip

import pytest

@pytest.fixture
def create_graph() :
    graph = Graph()

    graph.add_node('pandora')
    graph.add_node('arendelle')
    graph.add_node('metroville')
    graph.add_node('narina')
    graph.add_node('naboo')
    graph.add_node('manstropolis')

    graph.add_edge('pandora','arendelle',150)
    graph.add_edge('pandora','metroville',82)
    graph.add_edge('arendelle','pandora',150)
    graph.add_edge('arendelle','metroville',99)
    graph.add_edge('arendelle','manstropolis',42)
    graph.add_edge('metroville','pandora',82)
    graph.add_edge('metroville','arendelle',99)
    graph.add_edge('metroville','manstropolis',105)
    graph.add_edge('metroville','naboo',26)
    graph.add_edge('metroville','narina',37)
    graph.add_edge('narina','metroville',37)
    graph.add_edge('narina','naboo',250)
    graph.add_edge('naboo','narina',250)
    graph.add_edge('naboo','metroville',26)
    graph.add_edge('naboo','manstropolis',73)
    graph.add_edge('manstropolis','naboo',73)
    graph.add_edge('manstropolis','arendelle',42)
    graph.add_edge('manstropolis','metroville',105)

    return graph


def test_business_trip(create_graph):
    actual =  business_trip(create_graph,['pandora','metroville'])
    excepted = [True, 82]
    assert actual == excepted



def test_business_trip_2(create_graph):
    actual =  business_trip(create_graph,['arendelle','manstropolis', 'naboo'] )
    excepted = [True, 115]
    assert actual == excepted
