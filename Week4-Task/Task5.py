def dijkstra(graph, start):
    # Initialize distances and visited nodes
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
        # Find the unvisited node with minimum distance
        min_distance = float('infinity')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
        if min_node is None:
            break
            
        # Mark the node as visited
        visited.add(min_node)
        
        # Update distances to neighbors
        for neighbor, weight in graph[min_node].items():
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight
    
    return distances

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}
start_node = 'A'
result = dijkstra(graph, start_node)
for node, distance in result.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")