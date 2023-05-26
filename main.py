import world_model
from new_agent import Agent
import matplotlib.pyplot as plt

for step in range(world_model.num_steps):
    world_model.update_simulation(step)
    print(Agent.state)
    
    Agent.transitions(Agent)
    
plt.show()
    