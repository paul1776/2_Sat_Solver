# Algorithm for problem 3-e of HW1 for COSC247 Gems of Theoretical CS
import networkx

n, m = [int(i) for i in input().split()]
G = networkx.DiGraph()
for node_number in range(1, n+1):
    G.add_node(node_number)
    G.add_node(node_number*(-1))

for _i in range(m):
    x, y = [int(j) for j in input().split()]
    G.add_edge(x*(-1), y)
    G.add_edge(y*(-1), x)

strongly_connected = [c for c in networkx.strongly_connected_components(G)]
satisfiable = True

for connected_subgraph in strongly_connected:
    for node in connected_subgraph:
        if node*(-1) in connected_subgraph:
            satisfiable = False
            break

if satisfiable:
    print("SATISFIABLE")
else:
    print("UNSATISFIABLE")
