import random
class Site:
    def __init__(self):
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        
        # If site is greater than a certain number, it's good
        value_of_site = random.randint(0,10)