
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

from initial_graph import g


def maxmatch(g, donar, receiver):

    k = list(nx.maximal_matching(g))        # Halls Theorem
    # print(k)

    g2 = nx.Graph()

    g2.add_nodes_from(donar, bipartite=0)
    g2.add_nodes_from(receiver, bipartite=1)
    g2.add_edges_from(k)

    nx.draw_networkx(g2, pos = nx.drawing.layout.bipartite_layout(g2, donar), width = 2)

    # plt.savefig("final.png")
    plt.show()

    return k

