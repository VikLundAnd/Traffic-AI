import pygame
import random
from Node import Node


class NodeSystem(object):
    def __init__(self, amount_of_nodes, screen, grid_size):
        self.grab = False
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False


        self.nodes = []
        self.screen = screen
        self.grid_size = grid_size
        self.nodeSize = 12
        self.create_nodes(amount_of_nodes)
        for node in self.nodes:
            self.check_and_establish_connection(node)


    def update(self, event):
        width, height = self.screen.get_size()

        if event.type == pygame.MOUSEBUTTONDOWN and self.grab == False: # evaluate left button
            x, y = event.pos
            grid_x = int(((x + (width / self.grid_size[0])/2) / (width / self.grid_size[0])))
            grid_y = int(((y + (height / self.grid_size[1])/2) / (height / self.grid_size[1])))
            for node in self.nodes:
                if node.grid_x == grid_x and node.grid_y == grid_y:
                    self.nodes.remove(node)
                    self.grab = True

        if self.grab:
            self.grab_node(event)

    def create_nodes(self, amount):
        for i in range(amount):
            Node_ = Node(random.randint(0,self.grid_size[0]),random.randint(0,self.grid_size[1]), self.nodeSize, self.grid_size)
            self.nodes.append(Node_)

    def draw_nodes(self):
        for node in self.nodes:
            node.draw(self.screen, self.grid_size)

    def draw_edges(self):
        for node in self.nodes:
            if node.edge_up != None:
                node.edge_up.draw(self.screen, self.grid_size)
            if node.edge_down != None:
                node.edge_down.draw(self.screen, self.grid_size)
            if node.edge_left != None:
                node.edge_left.draw(self.screen, self.grid_size)
            if node.edge_right != None:
                node.edge_right.draw(self.screen, self.grid_size)


    def arrow(self,direction,color):
        arrow = pygame.Surface((300,300))
        pygame.draw.polygon(arrow, color, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        arrow = pygame.transform.scale(arrow,(20,20))

        if direction == "UP":
            return pygame.transform.rotate(arrow, 90)

        if direction == "DOWN":
            return pygame.transform.rotate(arrow, -90)

        if direction == "LEFT":
            return pygame.transform.flip(arrow,True,False)


        if direction == "RIGHT":
            return arrow

    def draw_arrows(self,x,y):
        Color_Arrow_Active = (0,255,0)
        Color_Arrow_InActive = (255,0,0)
        if self.UP == False:
            self.screen.blit(self.arrow("UP",Color_Arrow_InActive), (x-(self.nodeSize/2)-4,y-40))
        else:
            self.screen.blit(self.arrow("UP",Color_Arrow_Active), (x-(self.nodeSize/2)-4,y-40))

        if self.DOWN == False:
            self.screen.blit(self.arrow("DOWN",Color_Arrow_InActive), (x-(self.nodeSize/2)-3,y+20))
        else:
            self.screen.blit(self.arrow("DOWN",Color_Arrow_Active), (x-(self.nodeSize/2)-3,y+20))

        if self.LEFT == False:
            self.screen.blit(self.arrow("LEFT",Color_Arrow_InActive), (x-40,y-(self.nodeSize/2)-5))
        else:
            self.screen.blit(self.arrow("LEFT",Color_Arrow_Active), (x-40,y-(self.nodeSize/2)-5))

        if self.RIGHT == False:
            self.screen.blit(self.arrow("RIGHT",Color_Arrow_InActive), (x+20,y-(self.nodeSize/2)-5))
        else:
            self.screen.blit(self.arrow("RIGHT",Color_Arrow_Active), (x+20,y-(self.nodeSize/2)-5))


    def grab_node(self, event):
        width, height = self.screen.get_size()
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            self.grab = False
            newNode = Node( int(((x + (width / self.grid_size[0])/2) / (width / self.grid_size[0]))),
                            int(((y + (height / self.grid_size[1])/2) / (height / self.grid_size[1]))),
                            self.nodeSize,
                            self.grid_size)
            self.check_and_establish_connection(newNode)
            self.nodes.append((newNode))

            self.UP = False
            self.DOWN = False
            self.LEFT = False
            self.RIGHT = False

        else:
            pygame.draw.circle(self.screen, (200,200,255), (x,y), self.nodeSize)
            self.draw_arrows(x,y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.UP = not self.UP;
                print("UP")
            if event.key == pygame.K_DOWN:
                self.DOWN = not self.DOWN;
                print("DOWN")
            if event.key == pygame.K_LEFT:
                self.LEFT = not self.LEFT;
                print("LEFT")
            if event.key == pygame.K_RIGHT:
                self.RIGHT = not self.RIGHT;
                print("RIGHT")



    def check_and_establish_connection(self, node_in):
        UP = None
        DOWN = None
        LEFT = None
        RIGHT = None

        comp_LEFT = 0
        comp_UP = 0
        comp_RIGHT = 10
        comp_DOWN = 10

        # Find UP
        if self.UP:
            for node in self.nodes:
                if node.grid_x == node_in.grid_x:
                    for i in range(node_in.grid_y - 1, 0 - 1 , -1):
                        if node.grid_y == i:
                            if i > comp_UP:
                                comp_UP = i
                                UP = node



        # Find DOWN
        if self.DOWN:
            for node in self.nodes:
                if node.grid_x == node_in.grid_x:
                    for i in range(node_in.grid_y + 1, self.grid_size[1] + 1, 1):
                        if node.grid_y == i:
                            if i < comp_DOWN:
                                comp_DOWN = i
                                DOWN = node



        # Find LEFT
        if self.LEFT:
            for node in self.nodes:
                if node.grid_y == node_in.grid_y:
                    for i in range(node_in.grid_x - 1, 0 - 1, -1):
                        if node.grid_x == i:
                            if i > comp_LEFT:
                                comp_LEFT = i
                                LEFT = node



        # Find RIGHT
        if self.RIGHT:
            for node in self.nodes:
                if node.grid_y == node_in.grid_y:
                    for i in range(node_in.grid_x + 1, self.grid_size[0] + 1, 1):
                        if node.grid_x == i:
                            if i < comp_RIGHT:
                                comp_RIGHT = i
                                RIGHT = node


        node_in.make_connections((UP,DOWN,LEFT,RIGHT))







        '''
        try:
            print("UP: " + str(UP.grid_x) + ", " + str(UP.grid_y))
        except:
            pass
        try:
            print("DOWN: " + str(DOWN.grid_x) + ", " + str(DOWN.grid_y))
        except:
            pass
        try:
            print("LEFT: " + str(LEFT.grid_x) + ", " + str(LEFT.grid_y))
        except:
            pass
        try:
            print("RIGHT: " + str(RIGHT.grid_x) + ", " + str(RIGHT.grid_y))
        except:
            pass




        x_potentials = []
        y_potentials = []

        for node in self.nodes:
            if node.grid_x == node_in.grid_x and node.grid_y != node_in.grid_y:
                y_potentials.append(node)
            if node.grid_y == node_in.grid_y and node.grid_x != node_in.grid_x:
                x_potentials.append(node)

        x_potentials.sort(key=lambda Node: Node.grid_x)
        y_potentials.sort(key=lambda Node: Node.grid_y)
        print(x_potentials[0].grid_x)
        '''
