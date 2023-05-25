import world_model

class State:
    def __init__(self,color):
        self.color = color
        self.timer = 0
  
class RestingState(State):
    def __init__(self):
        super().__init__((30,144,255)) #Blue   
        
class ExploreState(State):
    def __init__(self):
        super().__init__((253,218,13)) # Yellow
        
    def finding_site(self):
        distance = world_model.x[0] - world_model.x[0:]
        for i in range(world_model.num_steps):
            if abs(distance) < 1:
                print("Site near")

class THub(ExploreState):
    def __init__(self):
        super().__init__(80, 80, 80) # Gray
        
class AcessingState(State):
    def __init__(self):
        super().__init__((112,41,99)) # Red
        
class DancingState(State):
    def __init__(self):
        super().__init__((255,0,255)) # Pink
        self.dances = 0
        
        
ExploreState.finding_site(ExploreState)

    


        
        