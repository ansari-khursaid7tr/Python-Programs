import matplotlib.pyplot as plt
import math, random
total=1000
inside=0
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0, 0), 1, 1, edgecolor='k', fill=False)
circ = plt.Circle((0.5, 0.5), 0.5, edgecolor='k', fill=False)
ax.add_patch(rect)
ax.add_patch(circ)
plt.axis('scaled')
for t in range(total):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if((x-0.5)**2+(y-0.5)**2)<(0.25):
            inside=inside+1
            ax.scatter(x, y, marker='^',s=5,color='r')
        elif((x-0.5)**2+(y-0.5)**2)>(0.25):
            ax.scatter(x, y, marker='o',s=5,color='b')
pi=4*(inside/total)
err=abs(100.0-pi/3.1415926)

print("Inside Points = %d"%inside)
print("Total Points = %d"%total)
print("Value of Pi = %f"%pi)
print("Standard Error = %f"%err)
plt.show()