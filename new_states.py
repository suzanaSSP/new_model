import math
from new_agent import Agent

class State:
    agent = Agent()
    def __init__(self,color):
        self.color = color

class RestingState(State):
    def __init__(self):
        super().__init__((30,144,255)) #Blue   
        
class ExploreState(State):

    def __init__(self):
        pass
     
    # Adding one to the site count if site is good
    def finding_site(self):
        
        # Function to create a list with the location of a given site or agent
         def finding_site(self):
            for agent in agent.agents:
                for site in self.sites:
                    if math.dist(site[0:-1], agent[:]) <= self.fov:
                        self.near_sites.append(site)

    
class THub(ExploreState):
    def __init__(self):
        super().__init__(80, 80, 80) # Gray
        
class AcessingState(State):
    def __init__(self):
        super().__init__((112,41,99)) # Red
        
class DancingState(State):
    dances = 0
    def __init__(self):
        super().__init__((255,0,255)) # Pink
        

# Implement a search radius 
        


    


        
        