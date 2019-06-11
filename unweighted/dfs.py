graph = {0: set([1, 2]),
         1: set([0, 3, 4]),
         2: set([0, 5]),
         3: set([1]),
         4: set([1, 5]),
         5: set([2, 4])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print dfs(graph, 0) # {4, 3, 5, 0, 2, 1}

