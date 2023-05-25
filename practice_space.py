import matplotlib.pyplot as plt
import numpy as np
import random
	
num_agents = 100
x = [random.randint(0,500)for _ in range(num_agents)]
y = [random.randint(0,500)for _ in range(num_agents)]
velocities = np.random.rand(num_agents, 2)

fig, ax = plt.subplots()

def update_simulation(step):
    # Update positions based on velocities or any other rules
    for i in range(num_agents):
        x[i] += random.randint(-2,2)
        y[i] += random.randint(-2,2)

    # Clear the plot
    ax.clear()
    plt.xlim(0,500)
    plt.ylim(0,500)
    # Update the scatter plot with new positions
    ax.scatter(x, y)

    # Customize the plot if needed (e.g., setting axes limits, titles, etc.)

    # Set a delay between frames if desired
    plt.pause(0.001)

num_steps = 1000
for step in range(num_steps):
    update_simulation(step)
    
plt.show()

