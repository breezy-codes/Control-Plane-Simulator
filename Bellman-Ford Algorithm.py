# Define a network of routers with their neighbours and associated costs (distances).
routers = {
    'A': {'B': 1, 'C': 2, 'E': 3},
    'B': {'A': 1, 'C': 1, 'D': 2, 'F': 2},
    'C': {'A': 2, 'B': 1, 'D': 1, 'G': 3},
    'D': {'B': 2, 'C': 1, 'H': 2},
    'E': {'A': 3, 'F': 1},
    'F': {'B': 2, 'E': 1, 'G': 1},
    'G': {'C': 3, 'F': 1, 'H': 2},
    'H': {'D': 2, 'G': 2},
}

# Use Bellman-Ford Algorithm to find the shortest route from a start node to all other nodes in the network.
def bellman_ford(network, start):
    distance = {node: float('inf') for node in network}
    predecessor = {node: None for node in network}
    distance[start] = 0

    for _ in range(len(network) - 1):
        for node in network:
            for neighbor, weight in network[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
                    predecessor[neighbor] = node

    for node in network:
        for neighbor, weight in network[node].items():
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance, predecessor

# Use the output from the Bellman-Ford algorithm to trace back and determine the shortest path from source to destination.
def get_path_bellman_ford(source, destination, network):
    distances, predecessors = bellman_ford(network, source)
    path = [] # Store the shortest path nodes.
    node = destination
    while node != source:
        if node is None:
            print("Path doesn't exist.")
            return
        path.append(node)
        node = predecessors[node]
    path.append(source)
    path.reverse()
    return path, distances[destination]

# Test the algorithm and find the paths between specific routers
if __name__ == "__main__":
    source, destination = 'A', 'H'
    path, distance = get_path_bellman_ford(source, destination, routers)
    print(f"Shortest path from {source} to {destination}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")

    source, destination = 'D', 'H'
    path, distance = get_path_bellman_ford(source, destination, routers)
    print(f"Shortest path from {source} to {destination}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")

    source, destination = 'B', 'E'
    path, distance = get_path_bellman_ford(source, destination, routers)
    print(f"Shortest path from {source} to {destination}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")
