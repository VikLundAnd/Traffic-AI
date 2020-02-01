import pygame

class Edge(object):
    def __init__(self, start_node, stop_node, direction):
        self.start_node = start_node
        self.stop_node = stop_node
        self.direction = direction
        self.offset = None
        self.determine_offset()

        self.width = 5
        self.color = (255,0,255)

    def draw(self, screen, grid_size):
        width, height = screen.get_size()
        self.startpos = (self.start_node.grid_x * int(width / grid_size[0]), self.start_node.grid_y * int(height / grid_size[1]))
        self.endpos = (self.stop_node.grid_x * int(width / grid_size[0]), self.stop_node.grid_y * int(height / grid_size[1]))


        self.startpos = tuple(map(sum, zip(self.startpos, self.offset)))
        self.endpos = tuple(map(sum, zip(self.endpos, self.offset)))


        pygame.draw.line(screen, self.color,self.startpos, self.endpos, self.width)

    def determine_offset(self):
        offset = 5
        x = 0
        y = 0
        if self.direction == 'up':
            x = offset
        if self.direction == 'down':
            x = -offset
        if self.direction == 'left':
            y = -offset
        if self.direction == 'right':
            y = offset

        self.offset = (x,y)
        print(self.offset)
