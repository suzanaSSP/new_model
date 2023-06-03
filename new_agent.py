import numpy as np
from world_model import World
import math
from sites import Foreign_Site
from typing import List


world = World()
AGENT_VELOCITY = 0.4
REPULSION_FACTOR = 0.01
behavior_time_step = 0.1
oscilation_time_increment = 0.045
MAX_RESTING_CYCLES = 30000
REPULSION_DETECT_RADIUS = 0.5
SITE_SENSING_DISTANCE = 0.7
MAX_EXPLORING_CYCLES = 400000
L            = 20 
  
class Agent:
    
    def __init__(self, x, y) -> None:
        self.fov = 50
        self.reading = []
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.oscilating_angle = 0
        
        self.clock = 0
        self.color = 'green'
        
        self.state = self.resting_state
            
    def resting_state(self):
        self.clock += 1 
            
        if self.clock > 3:
            self.state = self.explore_state
            self.clock = 0
        
    def explore_state(self):
        self.clock += 1

        """
        neighbors: List[Agent] = list(filter(lambda other_agent: other_agent != self and math.dist(other_agent.location, self.location) < REPULSION_DETECT_RADIUS**2, world.agents))
        for other_agent in neighbors:
            if other_agent.velocity_x != None:
                try:
                    self.velocity_x -= 1/(other_agent.x - self.x)*REPULSION_FACTOR
                    self.velocity_y -= 1/(other_agent.y - self.y)*REPULSION_FACTOR
                except ZeroDivisionError as e:
                    self.velocity_x -= 1/(((other_agent.x - self.x)*REPULSION_FACTOR)+1)
                    self.velocity_y -= 1/(((other_agent.y - self.y)*REPULSION_FACTOR)+1)
        """
         
        if self.velocity_x ==0 and self.velocity_y ==0:
            linear_angle = np.random.rand()*2*np.pi
        else:
            linear_angle = np.arctan2(self.velocity_y, self.velocity_x)
            
        non_linear_angle = linear_angle + np.sin(self.oscilating_angle) * 0.045
        self.oscilating_angle += oscilation_time_increment
        
        self.velocity_x = AGENT_VELOCITY*np.cos(non_linear_angle)
        self.velocity_y = AGENT_VELOCITY*np.sin(non_linear_angle)
        
        self.x += self.velocity_x *behavior_time_step
        self.y += self.velocity_y *behavior_time_step
        self.x %= L
        self.y %= L
        
        self.clock += 1
        
        foreign_sites : List[Foreign_Site] = sorted(world.sites, key = lambda foreign_site : (foreign_site.x - self.x)**2 + \
                                             (foreign_site.y - self.y)**2)
        closest_site = foreign_sites[0]
        
        if (closest_site.x - self.x)**2 + (closest_site.y - self.y)**2 < SITE_SENSING_DISTANCE**2:
            self.clock = 0
            self.color = 'black'
            self.x = closest_site.x
            self.y = closest_site.y
            self.state = self.accessing_state
  
            
            return
          
    def accessing_state(self):
        self.clock += 1
        
        
   


