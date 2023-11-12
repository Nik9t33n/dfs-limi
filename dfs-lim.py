def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")

    neighbors = list(graph[vertex])
    while neighbors:
        next_vertex = neighbors.pop()
        if next_vertex not in visited:
            dfs_recursive(graph, next_vertex, visited)
    return visited
if __name__ == "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    dfs_recursive(graph, 'A')
