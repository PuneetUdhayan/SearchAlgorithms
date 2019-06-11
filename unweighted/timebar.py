import numpy as np
from matplotlib import pyplot as plt

x_axis=['BFS','DFS']
y_axis=[]

totalbfs=0.0
totaldfs=0.0
number=0.0

fobj=open("timec.txt","r")
for line in fobj:
	temp=line.split(" ")
	totalbfs=totalbfs+float(temp[0])
	totaldfs=totaldfs+float(temp[1])
	number=number+1;
fobj.close()

y_axis.append(totalbfs/number)
y_axis.append(totaldfs/number)

ind=np.arange(len(x_axis))

plt.bar(ind,y_axis)
plt.xticks(ind+0.4,x_axis)
plt.ylabel('Time')
plt.title('Time comparison on DFS and BFS')

plt.show()

