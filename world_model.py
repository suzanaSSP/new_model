import matplotlib.pyplot as plt
import numpy as np
import random
from new_agent import Agent
from sites import Site

agent = Agent()
site = Site()

num_agents = 20
num_sites = 20

agents = [agent(agent.x, agent.y) for _ in range(num_agents)]
sites = [site(site.x, site.y) for _ in range(num_sites)]
    

# Plot figure
fig, ax = plt.subplots()
# Number of frames. This number will be used in the for loop of main.py and the for loop in Explore State
num_steps = 100
def update_simulation(step):
    # Update positions based on velocities or any other rules
    for i in range(agent.num_agents):
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
    
#Seperate the agents and sites to add color

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

