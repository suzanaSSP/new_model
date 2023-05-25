from new_states import RestingState, DancingState, ExploreState, AcessingState, THub
import random
import numpy as np
import matplotlib.pyplot as plt

     
class Agent:
    def __init__(self):
        self.state = RestingState()
        
    def transitions(self):
        if isinstance(self.state, RestingState):
            if self.state.timer > 120:
                self.state = ExploreState()
                
            # If some bees are dancing, go straight to accessing state to access sites
            if DancingState.dances > 0:
                self.state = AcessingState()
            
        if isinstance(self.state, ExploreState):
            if self.state.site ==1:
                self.state = AcessingState()
                
            # If you were exploring but didn't find anything, just rest
            if self.state.timer > 120 and self.state.sites ==0:
                self.state = THub()
            if isinstance(self.state, THub):
                self.state = RestingState()
            
        if isinstance(self.state, AcessingState):
            self.state = DancingState()
            
        if isinstance(self.state, DancingState) and self.state.dances >= 3:
            self.state = RestingState()
  
 


    
        
                     
# Questions: What is considered a good site? That will help me write -> if ____ : self.dances +=1
            # What is THub? Why do I have to go through it?
            
# Use Matplotlib to show bees and have them print which state they are in

