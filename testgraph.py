import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.cycles import find_cycle
from networkx.generators.classic import null_graph
from numpy import empty

def find_qty(G,node_name, sum, need):
    node = G.nodes(name=node_name)
    print(node)
    sum = sum + node["qty"]
    if(sum >= need):
        return node
    else:
        neighbours = [n for n in G.neighbours(node)]
        for n in neighbours:
            return node + find_qty(G,n["name"],sum,need)


G = nx.DiGraph()
G.add_node("A", name="A")
G.add_node("B", name="B")
G.add_node("C", name="C")
G.add_node("D", name="D")

G.add_edge("A","B")
G.add_edge("B","C")
G.add_edge("C","A")
G.add_edge("C","D")
G.add_edge("D","B")
G.add_edge("D","A")

G.nodes["A"]["qty"]=2
G.nodes["B"]["qty"]=5
G.nodes["C"]["qty"]=4
G.nodes["D"]["qty"]=3

G.neighbors("A")
# Find the path which will give me full qty
need = 8
sum=0
find_qty(G,G.nodes["A"]["name"],sum,need)

ud=nx.to_undirected(G)
nx.draw_networkx(ud)
plt.show()


     