import pygame.image as img
import pygame as pg
import os


class Disaster:
    def __init__(self) -> None:
        pass

class Tornado(Disaster):

    image = img.load(os.path.join("res","disaster","tornado.png"))


    def __init__(self, axe, pos, city) -> None:
        super().__init__()
        self.axe = axe # left, up, right, down
        self.pos = pos # (x,y)
        self.city = city
    
    def move(self):
        case = self.city[self.pos]
        if(not case.is_protected(self)):
            case.destroy()
        if(self.axe == 0):
            self.pos[0] -= 1
        elif(self.axe == 1):
            self.pos[1] -= 1
        elif(self.axe == 2):
            self.pos[0] += 1
        elif(self.axe == 3):
            self.pos[1] += 1
                

    def draw(self, screen, x ,y):
        screen.blit_grid(self.image, (x,y))

    def update(self, dt):
        pass