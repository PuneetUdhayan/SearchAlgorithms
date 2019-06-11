import time

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

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

start_dfs=time.time()
print dfs(graph, 0) 
end_dfs=time.time()

start_bfs = time.time()
print bfs(graph, 0) 
end_bfs=time.time()


dfs_time=end_dfs-start_dfs
bfs_time=end_bfs-start_bfs

entry=str(bfs_time)+" "+str(dfs_time)+"\n"

fobj=open("timec.txt","a")
fobj.write(entry)
print entry
fobj.close()
