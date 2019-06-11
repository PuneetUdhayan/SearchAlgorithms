graph = {0: set([1, 2]),
         1: set([0, 3, 4]),
         2: set([0, 5]),
         3: set([1]),
         4: set([1, 5]),
         5: set([2, 4])}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print bfs(graph, 0) # {4, 3, 5, 0, 2, 1}
