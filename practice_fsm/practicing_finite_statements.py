class FSM:
    # Simple version of finite statements
    def __init__(self):
        activestate = None

    # Set which state you are going to 
    def set_state(self, state):
        self.activestate = state

    def update(self):
        if self.activestate:
            self.activestate()

class StackFSM:
    """Implementation of Stack-based FSM. Now, there is a connection bewteen going home and runing away, just like in the finding leaf state.
    After you are done running away, how will you know which state to go back to, going home or finding leaf? 
    By stacking the states, you can keep track of what state you were previously and go back to that one, it would be the one under you, or before you in a list
    A state can pop off, which means the previous state becomes the new one, and can be pushed, meaning the new state is simply put on top of the previous state. 
    A stack-based FSM pops and pushes off. It pops off the one you're in, put still mantains it on the list to go back to it.  
    """
    def __init__(self):
        self.stack = []

    # Get the previous state you were in, it could be either going home or finding leaf
    def get_current_state(self):
        return self.stack[-1] if len(self.stack) > 0 else None
    
    # Go back to the previous state
    def update(self):
        current_state_function = self.get_current_state()
        if current_state_function:
            current_state_function()

    # Remove state from list
    def pop_state(self):
        return self.stack.pop()
    
    # Add state to list, but mantain previous state, you're going back to it
    def push_state(self, state):
        if self.get_current_state() != state:
            self.stack.append(state)


class Ant:

    def __init__(self, posX, posY):
        self.position = Vector3D(posX, posY)
        self.velocity = Vector3D(-1,-1)
        self.leaf = Leaf(40,40)
        self.home = Home(90,20)
        self.mouse = Mouse(500,600)
        self.brain = StackFSM()
        self.brain.set_state(self.find_leaf)
    
    def distance(x, y):
        return abs(x-y)

    def find_leaf(self):
        velocity = Vector3D(self.leaf.x - self.posX, self.leaf.y - self.posY)
        if self.distance(self.leaf, self) <=10:
            self.brain.pop_state()
            self.brain.push_state(self.go_home)
        if self.distance(self.mouse, self) <= 120:
            self.brain.push_state(self.run_away)

    def go_home(self):
        velocity = Vector3D(self.home.x - self.posX, self.home.y, self.posY)
        if self.distance(self.home, self) <= 10:
            self.brain.pop_state()
            self.brain.push_state(self.find_leaf)

        if self.distance(self.mouse, self) <=120:
            self.brain.push_state(self.run_away)

    def run_away(self):
        velocity = Vector3D(self.mouse.x - self.posX, self.mouse.y - self.posY)
        if self.distance(self.mouse, self) > 120:
            self.brain.pop_state()
            self.brain.update()

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Leaf:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Home:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y