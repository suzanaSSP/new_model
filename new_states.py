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
        self.sites = 0

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
        
    


        
        