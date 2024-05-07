import networkx as nx
from pyvis.network import Network
import random

# Generate a random graph with up to 10 vertices
num_vertices = random.randint(2, 10)
G = nx.Graph()
G.add_nodes_from(range(num_vertices))

# Add random edges to the graph
for i in range(num_vertices):
    for j in range(i+1, num_vertices):
        if random.random() < 0.5:
            G.add_edge(i, j)

# Create a PyVis network object
net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")

# Add nodes and edges to the network
for node in G.nodes():
    net.add_node(node, label=str(node))

for edge in G.edges():
    net.add_edge(edge[0], edge[1])

# Customize the network
net.repulsion(node_distance=420, central_gravity=0.33, spring_length=200, spring_strength=0.10, damping=0.95)

# Save the network as an HTML file
net.show_buttons(filter_=['physics'])
net.save_graph("random_graph.html")