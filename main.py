import pygame
from Node_system import NodeSystem
from Grid_system import GridSystem







dimensions = (800, 500)
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
grid_size = (10,10)


Nodes = NodeSystem(10, screen, grid_size)
Grid = GridSystem(screen, grid_size)


running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))
    Nodes.update(event)
    Grid.draw_grid()
    Nodes.draw_edges()
    Nodes.draw_nodes()


    pygame.display.flip()



    clock.tick(60)
    pygame.display.update()
