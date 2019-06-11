import numpy as np
from matplotlib import pyplot as plt

x_axis=['AStar','BestFirst']
y_axis=[]

totalastar=0.0
totalgbfs=0.0
number=0.0

fobj1=open("astar_time.txt","r")

for line in fobj1:
	totalastar=totalastar+float(line)
	number=number+1;
fobj1.close()

fobj2=open("bfs_time.txt","r")

for line in fobj2:
	totalgbfs=totalgbfs+float(line)
fobj2.close()


y_axis.append(totalastar/number)
y_axis.append(totalgbfs/number)

ind=np.arange(len(x_axis))

plt.bar(ind,y_axis)
plt.xticks(ind+0.4,x_axis)
plt.ylabel('Time')
plt.title('Time comparison on AStar and Greedy best first search')

plt.show()
