#encoding=utf-8
import functools #簡化帶入參數減少、活用
import graphviz as gv

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple): #判斷是否為Tuple
            graph.node(n[0],**n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1]) #*多個參數 **多個tuple
        else:
            graph.edge(*e)
    return graph



import itertools

nodes1 = list('ABCD')
edges1 = [e for e in itertools.combinations(nodes1, 2)]
g3 = add_nodes(g3, nodes1)
g3 = add_edges(g3, edges1)
g3.render('graph\\demo67_g3')

nodeA = ('A', {'label': 'Toyota'})
nodeB = ('B', {'label': 'Lexus'})
nodeC = ('C', {'label': 'Ford'})
nodeD = ('D', {'label': 'Nissan'})
nodes2 = [nodeA, nodeB, nodeC, nodeD]
g4 = add_nodes(g4, nodes2)
edgeAB = (('A', 'B'), {'label': 'same holding company'})
edgeAC = (('A', 'C'), {'label': 'popular company'})
edgeBD = (('B', 'D'), {'label': 'formula racing'})
edges2 = [edgeAB, edgeAC, edgeBD]
g4 = add_edges(g4, edges2)
g4.render('graph\\demo67_g4')

