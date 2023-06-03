import matplotlib.pyplot as plt
from new_agent import Agent
from sites import Site
from world_model import World
from typing import List
import numpy as np

AGENT_VELOCITY = 0.5    # velocity
eta          = 0.6      # random fluctuation in angle (in radians)
L            = 20       # size of world
R            = 0.5      # interaction radius
dt           = 0.1      # time step
Nt           = 200      # number of time steps
N            = 20       # number of agents
MAX_QUALITY  = 250
N_SITES      = 5       # number of sites
S_RADIUS     = 0.2      # site radius

agent : List[Agent] = []
site  : List[Site] = []
hub   : Site
    
def main():
    # Plot figure
    fig = plt.figure(figsize=(L,L), dpi=96)
    ax = plt.gca()
    ax.set(xlim=(-1 , L + 1), ylim=(-1 , L + 1))
    ax.set_aspect('equal')
    
    world = World()
    
    hub = Site(S_RADIUS + np.random.rand()*(L - S_RADIUS), S_RADIUS + np.random.rand()*(L - S_RADIUS)) # Size of circle for hub, point where agents will leave
    # Adding hub to the animation
    hub_dot = plt.Circle((hub.x, hub.y), S_RADIUS, color ='red',  alpha=0.5)
    # Adding hub to the World object
    world.hub = hub
    
    sites = [Site(S_RADIUS + np.random.rand()* (L-S_RADIUS), S_RADIUS + np.random.rand()* (L-S_RADIUS)) for _ in range(N_SITES)]
    
    world.sites = sites
    
    agents = [Agent(hub.x, hub.y) for _ in range(N)]

    agents = [Agent(hub.x, hub.y) for _ in range(N)] 
    world.agents = agents    
   
    while True:
          
        for agent in agents:
            agent.state()
            
        # Clear the plot
        plt.cla()
        
        ax.add_artist(hub_dot)
        
        for site in sites:
            circle = plt.Circle((site.x, site.y), S_RADIUS, color='black',alpha=0.5)
            ax.add_artist(circle)
            
        for agent in world.agents:
            plt.scatter(agent.x, agent.y, color = agent.color)
            
        ax.set(xlim=(0,L), ylim=(0,L))
        ax.set_aspect('equal')
        plt.pause(0.01)
        
if __name__ == '__main__':
    main()
    