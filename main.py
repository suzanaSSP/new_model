import matplotlib.pyplot as plt
import numpy as np
import random
from new_agent import Agent
from sites import Site

def main():
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

    while True:
        
        for site in sites:
            circle = plt.Circle((site.x, site.y), radius=0.2, color='black')
            ax.add_patch(circle)
            ax.set_aspect('equal')
            
        # Update positions based on velocities or any other rules
        for agent in agents:
            ax.scatter(agent.x, agent.y)

        # Clear the plot
        ax.clear()
        plt.xlim(0,50)
        plt.ylim(0,50)
        # Update the scatter plot with new positions
        ax.scatter(agent.x, agent.y)
        # Set a delay between frames if desired
        plt.pause(0.1)

if __name__ == '__main__':
    main()
    