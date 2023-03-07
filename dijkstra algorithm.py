import networkx as nx
import matplotlib.pyplot as plt
options = {
    'node_color': 'red',
    "edge_color":"red",
    'node_size': 450,
    'width': 2.5,
}
G = nx.Graph()
subax1 = plt.subplot(121)
G.add_edges_from([(0,1,{"weight":4}),(0,7,{"weight":8}),(1,2,{"weight":8}),(1,7,{"weight":11}),(2,8,{"weight":2}),(2,3,{"weight":7}),(2,5,{"weight":5}),(8,2,{"weight":2}),(8,6,{"weight":6}),(8,7,{"weight":7}),(6,7,{"weight":1}),(6,5,{"weight":2}),(3,4,{"weight":9}),(3,5,{"weight":14}),(4,5,{"weight":10})])
nx.draw(G, with_labels=True, font_weight='bold',**options)
aaa = nx.dijkstra_path(G,0,4)
print(aaa)

plt.show()