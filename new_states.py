import math
from new_agent import Agent
from world_model import World
import numpy as np

world = World()
max_resting_time = 10

def resting_state(agent: Agent):
    agent.clock += 1 
    
    if np.random.rand() < agent.clock / max_resting_time:
        agent.clock = 0
        agent.state = explore_state
      
def explore_state(agent: Agent):
    
    value_of_near_site = 20
    
    sites = sorted(world.sites, key = lambda site : math.dist(site.location, agent.location))
    closest_site = sites[0]
    
    if closest_site < value_of_near_site:
        agent = acessing_state
    
def acessing_state(agent: Agent):
    if isinstance(agent.state, acessing_state):
        print("I'm in the accesing state!")


    


        
        