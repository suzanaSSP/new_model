import matplotlib.pyplot as plt
import numpy as np
import random

# Site coordinates and their values. The second value in the numpy array shows how much they value
num_sites = 1
site_x    = np.random.rand(num_sites, 2) * 50
site_y    = np.random.rand(num_sites, 2) * 50
    
#colors
yellow = [255,255,0]
black  = [0,0,0]
white  = [255,255,255]

# Agent's coordinates 
num_agents = 1
x = [25]
y = [10]

# Adding only the first item from the numpy array of the site's arrays to the x, y value list
for list in site_x:
    for i in list:
        x.append(i)
        
for list in site_y:
    for i in list:
        y.append(i)

# Plot figure
fig, ax = plt.subplots()

def update_simulation(step):
    # Update positions based on velocities or any other rules
    for i in range(num_agents):
        x[i] += random.randint(-2,2)
        y[i] += random.randint(-2,2)

    # Clear the plot
    ax.clear()
    plt.xlim(0,50)
    plt.ylim(0,50)
    # Update the scatter plot with new positions
    ax.scatter(x, y)

    # Set a delay between frames if desired
    plt.pause(0.1)

# Amount of frames
num_steps = 500
for step in range(num_steps):
    update_simulation(step)
    
plt.show()

"""
import pygame
import random

pygame.init()

height = 600
width = 800

cell_size = 20
n_rows = height // cell_size
n_collums = width // cell_size


grid = [[random.randint(0,1) for _ in range(n_collums)] for _ in range(n_rows)]

def render_environment():
    for row in range(n_rows):
        for col in range(n_collums):
            site = grid[row][col]
            color = (255,255,255)
            
            if site == 0:
                color = (255,0,0) #red
                
            pygame.draw.rect(screen, color, (cell_size//2, cell_size//2, cell_size, cell_size))
           
    pygame.display.update
    
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = [[random.randint(0,1) for _ in range(n_collums)] for _ in range(n_rows)]
    render_environment()
    
pygame.quit()          
"""

