from new_states import RestingState, DancingState, ExploreState, AcessingState, THub, State
import numpy as np
import matplotlib.pyplot as plt

     
class Agent:
    state = ExploreState()
    
    def __init__(self):
        pass
        
    def transitions(self):
        if isinstance(self.state, RestingState):
            # If some bees are dancing, go straight to accessing state to access sites
            if DancingState.dances > 0:
                self.state = AcessingState()
            
        if isinstance(self.state, ExploreState):
            if self.state.site > 1:
                self.state = AcessingState()
                
            # If you were exploring but didn't find anything, just rest
            if State.timer > 120 and self.state.site ==0:
                self.state = THub()
            if isinstance(self.state, THub):
                self.state = RestingState()
            
        if isinstance(self.state, AcessingState):
            print("I'm in the accessing state!")
            
        if isinstance(self.state, DancingState) and self.state.dances >= 3:
            self.state = RestingState()
  
 


    
        
                     
# Questions: What is considered a good site? That will help me write -> if ____ : self.dances +=1
            # What is THub? Why do I have to go through it?
            
# Use Matplotlib to show bees and have them print which state they are in

