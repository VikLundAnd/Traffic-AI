import pygame
from Edge_system import Edge

class Node(object):
    def __init__(self, grid_x, grid_y, nodeSize, gridSize):
        self.nodeSize = nodeSize
        self.grid_size = gridSize
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.Spawner = False
        self.list_of_neighbours = None
        self.edge_up = None
        self.edge_down = None
        self.edge_left  = None
        self.edge_right = None

        self.check_and_set_if_spawner()




    def draw(self, screen, grid_size):
        if self.Spawner:
            color = (255,50,50)
        else:
            color = (255,255,255)


        width, height = screen.get_size()
        pygame.draw.circle(screen, color, (self.grid_x * int(width / grid_size[0]), self.grid_y * int(height / grid_size[1])), self.nodeSize)

    def check_and_set_if_spawner(self):
        if self.grid_x == 0 or self.grid_x == self.grid_size[0] or self.grid_y == 0 or self.grid_y == self.grid_size[0]:
            self.Spawner = True
        else:
            self.Spawner = False

    def make_connections(self, list_of_neighbours):
        self.list_of_neighbours = list_of_neighbours
        self.create_edges()


    def create_edges(self):
        for i, neighbour in enumerate(self.list_of_neighbours):
            if neighbour:
                if i == 0:
                    self.edge_up = Edge(self,neighbour, 'up')
                if i == 1:
                    self.edge_down = Edge(self,neighbour, 'down')
                if i == 2:
                    self.edge_left = Edge(self,neighbour, 'left')
                if i == 3:
                    self.edge_right = Edge(self,neighbour, 'right')
