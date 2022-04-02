import pygame.image as img
import pygame as pg
import os


class Disaster:
    def __init__(self) -> None:
        pass

class Tornado(Disaster):

    image = img.load(os.path.join("res","disaster","tornade_1.png"))


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

    def preview(self):
        l = []
        if self.axe == 0:
            for i in range(self.city.w-1, -1, -1):
                pos = (i, self.pos[1])
                case = self.city[pos]
                if case.is_protected(self):
                    break
                l.append(pos)
        elif self.axe == 1:
            for i in range(self.city.h):
                pos = (self.pos[0], i)
                case = self.city[pos]
                if case.is_protected(self):
                    break
                l.append(pos)
        elif self.axe == 2:
            for i in range(self.city.w):
                pos = (i, self.pos[1])
                case = self.city[pos]
                if case.is_protected(self):
                    break
                l.append(pos)
        elif self.axe == 3:
            for i in range(self.city.h-1, -1, -1):
                pos = (self.pos[0], i)
                case = self.city[pos]
                if case.is_protected(self):
                    break
                l.append(pos)
        return l

                

    def draw(self, screen, x ,y):
        screen.blit_grid(self.image, (x,y))

    def update(self, dt):
        pass