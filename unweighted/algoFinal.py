import time
import random

n=10
g=[]
G={}

for i in range(n):
	temp=[]
	for j in range(0,n):
		temp.append(0)
	g.append(temp)

for i in range(0,n):
	for j in range(i+1,n):
		g[i][j]=random.randint(0,1)

for i in range(0,n):
	for j in range(i+1,n):
		g[j][i]=g[i][j]

for i in range(n):
	l=set()
	for j in range(n):	
		if g[i][j]==1:
			l.add(j)
	G[i]=l

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
print dfs(G, 0) 
end_dfs=time.time()

start_bfs = time.time()
print bfs(G, 0) 
end_bfs=time.time()


dfs_time=end_dfs-start_dfs
bfs_time=end_bfs-start_bfs

entry=str(bfs_time)+" "+str(dfs_time)+"\n"

fobj=open("timec.txt","a")
fobj.write(entry)
print entry
fobj.close()

