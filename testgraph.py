import networkx as nx

def find_qty(G,node_name, sum, need, path, all_paths):
    node = [n for n,d in G.nodes(data=True) if(d["name"]==node_name)]
    sum = sum + G.nodes(data=True)[node[0]]["qty"]
    path = path + node
    if(sum >= need):
        all_paths.append([path,sum])
        return
    else:
        neighbours = [n for n in G.neighbors(node[0])]
        for n in neighbours:
            find_qty(G,n,sum,need,path,all_paths)
    return all_paths

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

# Find the path which will give me full qty
need = 30
sum=0
all_paths = []
find_qty(G,G.nodes["A"]["name"],sum,need, [],all_paths)
print(all_paths)

     