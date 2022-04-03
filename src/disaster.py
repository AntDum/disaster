import pygame.image as img
import pygame as pg
import os
from random import random
from option import DISASTER_DURATION, DISASTER_SPEED, TILE_SIZE


class Disaster:
    def __init__(self, city) -> None:
        self.timer = 0
        self.city = city
        self.finish = False

    def update(self, dt):
        self.timer += dt
    
    def launch(self):
        pass

    def draw(self, screen):
        pass

    def preview(self):
        return []

class Tornado(Disaster):

    image = img.load(os.path.join("res","disaster","tornade_1.png"))


    def __init__(self, axe, pos, city) -> None:
        super().__init__(city)
        self.axe = axe # left, up, right, down
        self.pos = pos # (x,y)
        
    
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

    def draw(self, screen):
        screen.blit(self.image, self.city.grid_to_screen(self.pos))

    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_SPEED:
            self.timer = 0
            if not self.move():
                self.finish = True

class Fire(Disaster):
    image = img.load(os.path.join("res","disaster","tornade_1.png"))

    def __init__(self, city, pos) -> None:
        super().__init__(city)
        self.pos = pos

    def preview(self):
        l = []
        for i in range(2):
            for j in range(2):
                x, y = self.pos[0] + i, self.pos[1] + j
                if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
                    l.append((x, y))
        return l
    
    def launch(self):
        self.next = self.preview()
    
    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_DURATION:
            self.finish = True

    def draw(self, screen):
        for pos in self.next:
            screen.blit(self.image, self.city.grid_to_screen(pos))

class Flood(Disaster):
    def __init__(self, city) -> None:
        super().__init__(city)

class Tsunami(Disaster):
    def __init__(self, city) -> None:
        super().__init__(city)

class Earthquake(Disaster):
    def __init__(self, city) -> None:
        super().__init__(city)
    
    def preview(self):
        return [(x,y) for x in range(self.city.w) for y in range(self.city.h)]

    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_DURATION:
            self.city.padding = [0,0]
            self.finish = True
            for pos in self.preview():
                case = self.city[pos]
                if(not case.is_protected(self)):
                    case.destroy()
        else:
            self.city.padding = [(random()*TILE_SIZE)//10, (random()*TILE_SIZE)//10]

            
