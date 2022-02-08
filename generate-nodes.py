import networkx as nx
import pandas as pd
from matplotlib.pylab import plt
#%matplotlib inline
 
G = nx.Graph()
 
# Read csv for nodes and edges using pandas:
nodes = pd.read_csv("query-researchers.csv")
#edges = pd.read_csv("edges.csv")
 
# Dataframe to list:
nodes_list = nodes.values.tolist()
#edges_list = edges.values.tolist()
 
# Import id, name, and group into node of Networkx:
for i in nodes_list:
    G.add_node(i[0].replace("http://data.cervantesvirtual.com/person/", ""), name=i[1])
 
# Import source, target, and value into edges of Networkx:
#for i in edges_list:
#    G.add_edge(i[0],i[1], value=i[2])

for i in nodes_list:
    G.add_edge(i[2].replace("http://data.cervantesvirtual.com/person/", ""),i[0].replace("http://data.cervantesvirtual.com/person/", ""), value=i[3])
 
# Visualize the network:
nx.draw_networkx(G)

from networkx.readwrite import json_graph

# Write json for nodes-links format:
import json
j = json_graph.node_link_data(G)
 
js = json.dumps(j, ensure_ascii=False, indent=2)
with open("node-link-value.json", "w") as file:
     file.write(js)
