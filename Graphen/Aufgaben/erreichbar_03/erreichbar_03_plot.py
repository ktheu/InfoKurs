# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

G = {
    'a': set('d'),
    'b': set('ce'),
    'c': set('b'),
    'd': set('a'),
    'e': set('bf'),
    'f': set('e')
}

def createGraphFromDictOfSets(G):
     nodlist = list(G.keys())
     G0 = nx.Graph()
     G0.add_nodes_from(nodlist)
     for v in G:
         for w in G[v]:
             G0.add_edge(v,w)
     nx.draw_circular(G0,with_labels=True,node_color='y', node_size=600, node_shape='o', )
     plt.show()     
     
createGraphFromDictOfSets(G)