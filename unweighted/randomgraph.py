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
	print g[i]

for i in range(n):
	l=set()
	for j in range(n):	
		if g[i][j]==1:
			l.add(j)
	G[i]=l

print G
