from collections import namedtuple
import heapq

# Define the namedtuple for the graph
Edge = namedtuple('Edge', ['source', 'destination', 'weight'])

# Create an empty list to store edges
edges = []

# Function to add an edge to the graph
def add_edge(edges, source, destination, weight):
    edges.append(Edge(source, destination, weight))

# Example edges with weights (assuming undirected graph)
edges_to_add = [
    ('San Fernando', 'Bauang', 14.5), 
    ('San Fernando', 'San Juan', 13.1), 
    ('San Fernando', 'Naguilian', 22.1),
    ('Bauang', 'Caba', 22.7), 
    ('Bauang', 'Naguilian', 16.1),
    ('Bacnotan', 'Balaoan', 12.6),
    ('Bacnotan', 'San Juan', 11.1),
    ('Balaoan', 'Luna', 10.4),
    ('Caba', 'Aringay', 17.6),
    ('Caba', 'Naguilian', 17),
    ('Aringay', 'Agoo', 12.2),
    ('Aringay', 'Naguilian', 31.7)
]

# Adding edges to the graph
for source, destination, weight in edges_to_add:
    add_edge(edges, source, destination, weight)
    add_edge(edges, destination, source, weight)  # Add the reverse edge for an undirected graph

# Function to find the shortest path using Dijkstra's algorithm
def shortest_path(edges, start, end):
    graph = {}
    for edge in edges:
        if edge.source not in graph:
            graph[edge.source] = []
        graph[edge.source].append((edge.destination, edge.weight))

    pq = [(0, start)]
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {city: None for city in graph}

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph.get(current_city, ()):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current_city = end
    while current_city:
        path.append(current_city)
        current_city = previous[current_city]
    path.reverse()

    return path, distances[end]

# Ask the user for starting and destination cities
if __name__ == "__main__":
    # Prompt the user to input the starting city
    start_city = input("Enter the starting city: ")
    
    # Prompt the user to input the destination city
    end_city = input("Enter the destination city: ")

    shortest_path, distance = shortest_path(edges, start_city, end_city)
    print(f"The shortest path from {start_city} to {end_city} is: {shortest_path}")
    print(f"The distance is: {distance} km")