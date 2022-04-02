import pygame.image as img
import pygame as pg
import os

from option import DISASTER_SPEED


class Disaster:
    def __init__(self) -> None:
        self.timer = 0

    def update(self, dt):
        self.timer += dt

class Tornado(Disaster):

    image = img.load(os.path.join("res","disaster","tornade_1.png"))


    def __init__(self, axe, pos, city) -> None:
        super().__init__()
        self.axe = axe # left, up, right, down
        self.pos = pos # (x,y)
        self.city = city
        self.finish = False
    
    def move(self):
        if self.moved >= len(self.next):
            return False
        self.pos = self.next[self.moved]
        self.moved += 1
        case = self.city[self.pos]
        if(not case.is_protected(self)):
            case.destroy()
        return True

    def preview(self):
        l = []
        if self.axe == 0: # left
            for i in range(self.city.w-1, -1, -1):
                pos = (i, self.pos[1])
                case = self.city[pos]
                if case.block(self):
                    break
                l.append(pos)
        elif self.axe == 1: # top
            for i in range(self.city.h-1, -1, -1):
                pos = (self.pos[0], i)
                case = self.city[pos]
                if case.block(self):
                    break
                l.append(pos)
        elif self.axe == 2: # right
            for i in range(self.city.w):
                pos = (i, self.pos[1])
                case = self.city[pos]
                if case.block(self):
                    break
                l.append(pos)
        elif self.axe == 3: # down
            for i in range(self.city.h):
                pos = (self.pos[0], i)
                case = self.city[pos]
                if case.block(self):
                    break
                l.append(pos)
        return l
    
    def launch(self):
        self.next = self.preview()
        self.moved = 0

    def draw(self, screen, x, y):
        screen.blit(self.image, (x,y))

    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_SPEED:
            self.timer = 0
            if not self.move():
                self.finish = True