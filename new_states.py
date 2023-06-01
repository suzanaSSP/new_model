from math import sqrt
import world_model as wm

class State:
    timer = 0
    def __init__(self,color):
        self.color = color

class RestingState(State):
    def __init__(self):
        super().__init__((30,144,255)) #Blue   
        
class ExploreState(State):
    site = 0

    def __init__(self):
        pass
     
    # Adding one to the site count if site is good
    def finding_site(self):
        
        # Function to create a list with the location of a given site or agent
        def finding_distance(point1, point2):
            location = sqrt((wm.x[point2] - wm.x[point1])**2 + (wm.y[point2] - wm.y[point1])**2)
            return location
        
        # If the site is greater than this number, it is good
        value_of_good_site = 30
        # Distance between agent and site
        distance1 = abs(finding_distance(1,0))
        distance2 = abs(finding_distance(2,0))
        distance3 = abs(finding_distance(3,0))
        
        for i in range(wm.num_steps):
            if distance1 < value_of_good_site or distance2 < value_of_good_site or distance3 < value_of_good_site:
                self.site += 1

    
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
        


    


        
        