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


# Use Dijkstra's algorithm to find the shortest route from a start node to all other nodes in the network.
def dijkstra(network, start):
    unvisited = {node: float('infinity') for node in network}
    visited = {}
    current = start
    current_distance = 0
    unvisited[current] = current_distance

    predecessors = {node: None for node in network}

    while True:
        for neighbor, weight in network[current].items():
            if neighbor not in unvisited: continue
            new_distance = current_distance + weight
            if unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance
                predecessors[neighbor] = current

        visited[current] = current_distance
        del unvisited[current]

        if not unvisited: break

        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

    return visited, predecessors


# Use the output from the Dijkstra algorithm to trace back and determine the shortest path from source to destination.
def get_path(source, destination, network):
    distances, predecessors = dijkstra(network, source)
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
    path, distance = get_path(source, destination, routers)
    print(f"Shortest path from {source} to {destination}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")

    source, destination = 'D', 'H'
    path, distance = get_path(source, destination, routers)
    print(f"Shortest path from {source} to {destination}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")

    source, destination = 'B', 'E'
    path, distance = get_path(source, destination, routers)
    print(f"Shortest path from {source} to {destination}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")