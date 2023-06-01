import numpy as np
import matplotlib.pyplot as plt
import math
import random
     
class Agent:
    
    def __init__(self):
        self.fov = 50
        self.reading = []
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        
        self.state = ExploreState()
         
    def update(self,reading):
        self.near_sites = reading
        self.state.update()
       
    """ 
    def transitions(self):
        if isinstance(self.state, RestingState):
            # If some bees are dancing, go straight to accessing state to access sites
            if DancingState.dances > 0:
                self.state = AcessingState()
            
        if isinstance(self.state, ExploreState):
            self.state.finding_site()
            if self.state.site >= 1:
                self.state = AcessingState()
                
        if isinstance(self.state, AcessingState):
            print("I'm in the accessing state!")
            
        if isinstance(self.state, DancingState) and self.state.dances >= 3:
            self.state = RestingState()
            
        """
       

from new_states import ExploreState
        
   
                
 


    
        
                     
# Questions: What is considered a good site? That will help me write -> if ____ : self.dances +=1
            # What is THub? Why do I have to go through it?
            
# Use Matplotlib to show bees and have them print which state they are in

