import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

x = []
y = []

for i in range(20):
    x.append(random.randint(0,50))
    y.append(random.randint(0,50))
    
    if i % 5 ==0:
        plt.xlim(0,50)
        plt.ylim(0,50)
        plt.scatter(x,y)
        plt.pause(0.001)
    
plt.show()
