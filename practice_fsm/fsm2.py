class FSM:
    def __init__(self):
        activestate = None

    def set_state(self, state):
        self.activestate = state

class Traffic_Lights:
    """ Start at red light, after 10 seconds go to green light, after 5 seconds go to yellow light, then after 2 second go back to red light"""

    def __init__(self):
        self.timer = 0
        self.brain = FSM()
        self.brain.set_state(self.red_light)

    # Clock telling time. After 17 seconds (10+5+2) it restarts, so after 10 seconds the light will always change and I won't have to do any calculations after that
    def clock(self):
        def timer_loop():
            while self.timer < 17:
                self.timer += 1
        while True:
            if self.timer == 17:
                self.timer = 0
                timer_loop(self.timer)

    def red_light(self):
        if self.timer == 10:
            self.brain.set_state(self.green_light)

    def green_light(self):
        if self.timer == 15:
            self.brain.set_state(self.yellow_light)

    def yellow_light(self):
        if self.timer == 17:
            self.brain.set_state(self.red_light)
