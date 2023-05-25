import matplotlib.pyplot as plt
import random

n_site = 15
x = [random.randint(0,20) for _ in range(n_site)]
y = [random.randint(0,20) for _ in range(n_site)]

fig = plt.figure(figsize=(6,6), dpi=96)
ax = plt.gca()

while True:
    plt.cla()
    x = [random.randint(0,20) for _ in range(n_site)]
    y = [random.randint(0,20) for _ in range(n_site)]
    plt.scatter(x,y)
    plt.pause(0.5)
    
environment = plt.scatter(x,y)

plt.show()

"""
import pygame
import random

pygame.init()

height = 600
width = 800

cell_size = 20
n_rows = height // cell_size
n_collums = width // cell_size


grid = [[random.randint(0,1) for _ in range(n_collums)] for _ in range(n_rows)]

def render_environment():
    for row in range(n_rows):
        for col in range(n_collums):
            site = grid[row][col]
            color = (255,255,255)
            
            if site == 0:
                color = (255,0,0) #red
                
            pygame.draw.rect(screen, color, (cell_size//2, cell_size//2, cell_size, cell_size))
           
    pygame.display.update
    
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = [[random.randint(0,1) for _ in range(n_collums)] for _ in range(n_rows)]
    render_environment()
    
pygame.quit()          
"""

