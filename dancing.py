import matplotlib.pyplot as plt
import numpy as np
import random

num_agents = 100

x =[random.randint(0,500) for _ in range(num_agents)]
y = [random.randint(0,500) for _ in range(num_agents)]

fig, ax = plt.subplots()

def update_simulation(step):
    for i in range(num_agents):
        x[i] += random.randint(-2,2)
        y[i] += random.randint(-2,2)

    ax.clear()
    plt.xlim(0,500)
    plt.ylim(0,500)

    ax.scatter(x,y)

    plt.pause(0.001)

num_steps = 500
for step in range(num_steps):
    update_simulation(step)

plt.show()