import world_model
from new_agent import Agent
import matplotlib.pyplot as plt

agent = Agent()

for step in range(world_model.num_steps):
    world_model.update_simulation(step)
    print(agent.state)
    
    agent.transitions()
    
plt.show()
    