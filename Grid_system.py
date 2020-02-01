import pygame

class GridSystem(object):
    def __init__(self,screen, grid_size):
        self.screen = screen
        self.grid_size = grid_size

    def draw_grid(self):
        width, height = self.screen.get_size()
        for i in range(1, self.grid_size[0]):
            pygame.draw.line(self.screen, (50,50,50), ((width / self.grid_size[0]) * i, 0), ((width / self.grid_size[0]) * i, height), 1)

        for i in range(1, self.grid_size[0]):
            pygame.draw.line(self.screen, (50,50,50), (0, (height / self.grid_size[1]) * i), (width, (height / self.grid_size[1]) * i), 1)
