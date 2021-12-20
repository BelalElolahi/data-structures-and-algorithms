from graph.graph_implement import Graph

import pytest



@pytest.fixture
def create_graph () :
    graph = Graph()
    graph.add_node('s')
    graph.add_node('w')
    graph.add_node('h')
    graph.add_node('d')
    graph.add_node('x')
    graph.add_edge('s','w')
    graph.add_edge('s','h')
    graph.add_edge('w','d')
    graph.add_edge('w','x')
    return graph


def test_dfs(create_graph):
    actual = create_graph.DFS('s')
    excepted  = ['s', 'w', 'd', 'x', 'h']
    assert actual == excepted
