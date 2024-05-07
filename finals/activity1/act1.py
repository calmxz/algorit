from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])

nodes = ["A", "B", "C", "D", "E", "F"]
edges = [
    ("A", "B"),
    ("A", "D"),
    ("A", "C"),
    ("A", "E"),
    ("A", "F"),
    ("B", "D"),
    ("C", "E")
]

G = Graph(nodes, edges)

def adjacency_dict(graph):
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    return adj

def adjacency_matrix(graph):
    adj = [[0 for _ in range (len(graph.nodes))] for _ in range (len(graph.nodes))]
    
    node_to_index = {node: i for i, node in enumerate(graph.nodes)}
    
    for edge in graph.edges:
        node1, node2 = edge
        i = node_to_index[node1]
        j = node_to_index[node2]
        adj[i][j] += 1
        adj[j][i] += 1
    return adj

print(adjacency_dict(G))
print(adjacency_matrix(G))        