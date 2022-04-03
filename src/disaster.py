from shlex import join
import pygame.image as img
import pygame as pg
import os
from random import random
from option import ANIMATION_SPEED, DISASTER_DURATION, DISASTER_SPEED, TILE_SIZE
from src.ressources import import_disaster


class Disaster:
    def __init__(self, city) -> None:
        self.timer = 0
        self.anim_time = 0
        self.city = city
        self.finish = False
        self.anim_frame_count = 0

    def update(self, dt):
        self.timer += dt
        self.anim_time += dt
        if self.anim_time >= ANIMATION_SPEED:
            self.anim_time = 0
            self.anim_frame_count += 1
    
    def launch(self):
        pass

    def draw(self, screen):
        pass

    def preview(self):
        return []

class Tornado(Disaster):

    images = [import_disaster("tornado1"),
                import_disaster("tornado2")]


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
                l.append(pos)
                if case.block(self):
                    break
        elif self.axe == 1: # top
            for i in range(self.city.h-1, -1, -1):
                pos = (self.pos[0], i)
                case = self.city[pos]
                l.append(pos)
                if case.block(self):
                    break
        elif self.axe == 2: # right
            for i in range(self.city.w):
                pos = (i, self.pos[1])
                case = self.city[pos]
                l.append(pos)
                if case.block(self):
                    break
        elif self.axe == 3: # down
            for i in range(self.city.h):
                pos = (self.pos[0], i)
                case = self.city[pos]
                l.append(pos)
                if case.block(self):
                    break
        return l
    
    def launch(self):
        self.next = self.preview()
        self.moved = 0

    def draw(self, screen):
        screen.blit(self.images[self.anim_frame_count%2], self.city.grid_to_screen(self.pos))

    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_SPEED:
            self.timer = 0
            if not self.move():
                self.finish = True

class Fire(Disaster):

    images = [import_disaster("fire1"),
                import_disaster("fire2")]

    def __init__(self, city, pos) -> None:
        super().__init__(city)
        self.pos = pos

    def preview(self):
        l = []
        if self.city.has_fire_man():
            x, y = self.pos[0], self.pos[1]
            if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
                l.append((x, y))
        else:
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
            for pos in self.next:
                case = self.city[pos]
                if(not case.is_protected(self)):
                    case.destroy()
            self.finish = True

    def draw(self, screen):
        for pos in self.next:
            screen.blit(self.images[self.anim_frame_count%2], self.city.grid_to_screen(pos))

class Flood(Disaster):

    images = [import_disaster("flood1"),
                import_disaster("flood2")]

    def __init__(self, city, axe) -> None:
        super().__init__(city)
        self.axe = axe

    def preview(self):
        l = []
        if self.axe == 0 and self.city.coast[(self.axe+2)%4]: # left
            i = self.city.w-1
            for j in range(self.city.h):
                pos = (i, j)
                l.append(pos)

        elif self.axe == 1 and self.city.coast[(self.axe+2)%4]: # top
            i = self.city.h-1
            for j in range(self.city.w):
                pos = (j, i)
                l.append(pos)

        elif self.axe == 2 and self.city.coast[(self.axe+2)%4]: # right
            i = 0
            for j in range(self.city.h):
                pos = (i, j)
                l.append(pos)

        elif self.axe == 3 and self.city.coast[(self.axe+2)%4]: # down
            i = 0
            for j in range(self.city.w):
                pos = (j, i)
                l.append(pos)

        return l

    def launch(self):
        self.next = self.preview()
    
    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_DURATION:
            for pos in self.next:
                case = self.city[pos]
                if(not case.is_protected(self)):
                    case.destroy()
            self.finish = True
    
    def draw(self, screen):
        for pos in self.next:
            screen.blit(self.images[self.anim_frame_count%2], self.city.grid_to_screen(pos))
        

class Tsunami(Disaster):

    images = [import_disaster("tsunami1"),
                import_disaster("tsunami2")]

    def __init__(self, city, axe) -> None:
        super().__init__(city)
        self.axe = axe

    def preview(self):
        l = []
        no_j = set()
        if self.axe == 0 and self.city.coast[(self.axe+2)%4]: # left
            for i in range(self.city.w-1, -1, -1):
                mini_l = []
                for j in range(self.city.h):
                    pos = (i, j)
                    case = self.city[pos]
                    if j not in no_j:
                        mini_l.append(pos)
                    if case.block(self):
                        no_j.add(j)
                l.append(mini_l)
        elif self.axe == 1 and self.city.coast[(self.axe+2)%4]: # top
            for i in range(self.city.h-1, -1, -1):
                mini_l = []
                for j in range(self.city.w):
                    pos = (j, i)
                    case = self.city[pos]
                    if not j in no_j:
                        mini_l.append(pos)
                    if case.block(self):
                        no_j.add(j)
                l.append(mini_l)
        elif self.axe == 2 and self.city.coast[(self.axe+2)%4]: # right
            for i in range(self.city.w):
                mini_l = []
                for j in range(self.city.h):
                    pos = (i, j)
                    case = self.city[pos]
                    if not j in no_j:
                        mini_l.append(pos)
                    if case.block(self):
                        no_j.add(j)
                l.append(mini_l)
        elif self.axe == 3 and self.city.coast[(self.axe+2)%4]: # down
            for i in range(self.city.h):
                mini_l = []
                for j in range(self.city.w):
                    pos = (j, i)
                    case = self.city[pos]
                    if not j in no_j:
                        mini_l.append(pos)
                    if case.block(self):
                        no_j.add(j)
                l.append(mini_l)
        return l

    def launch(self):
        self.next = self.preview()
        self.moved = 0

    def move(self):
        if self.moved >= len(self.next):
            return False
        for pos in self.next[self.moved]:
            case = self.city[pos]
            if(not case.is_protected(self)):
                case.destroy()
        self.moved += 1
        return True
    
    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_SPEED:
            self.timer = 0
            if not self.move():
                self.finish = True
    
    def draw(self, screen):
        if self.moved < len(self.next):
            for pos in self.next[self.moved]:
                screen.blit(self.images[self.anim_frame_count%2], self.city.grid_to_screen(pos))
        

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

            

class Meteor(Disaster):

    images = [import_disaster("meteor1"),
                import_disaster("meteor2")]

    def __init__(self, city, pos) -> None:
        super().__init__(city)
        self.pos = pos

    def preview(self):
        l = []
        x, y = self.pos[0], self.pos[1]
        if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
            l.append((x, y))
        return l
    
    def launch(self):
        self.next = self.preview()
    
    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_DURATION:
            for pos in self.next:
                case = self.city[pos]
                if(not case.is_protected(self)):
                    case.destroy()
            self.finish = True

    def draw(self, screen):
        for pos in self.next:
            screen.blit(self.images[self.anim_frame_count%2], self.city.grid_to_screen(pos))
            
class Volcano(Disaster):

    images = [import_disaster("volcano1"),
                import_disaster("volcano2")]

    def __init__(self, city, pos) -> None:
        super().__init__(city)
        self.pos = pos # (x,y)
        
    
    def move(self):
        if self.moved >= len(self.next):
            return False
        for pos in self.next[self.moved]:
            case = self.city[pos]
            if(not case.is_protected(self)):
                case.destroy()
        self.moved += 1
        return True

    def preview(self):
        f = []
        s = []
        x, y = self.pos[0], self.pos[1]
        if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
            f.append((x, y))
        x -= 1
        if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
            s.append((x, y))
        x += 2
        if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
            s.append((x, y))
        x -= 1
        y -= 1
        if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
            s.append((x, y))
        y += 2
        if x < self.city.w and y < self.city.h and x >= 0 and y >= 0:
            s.append((x, y))
        return [f,s]
    
    def launch(self):
        self.next = self.preview()
        self.moved = 0

    def draw(self, screen):
        if self.moved < len(self.next):
            for pos in self.next[self.moved]:
                screen.blit(self.images[self.anim_frame_count%2], self.city.grid_to_screen(pos))

    def update(self, dt):
        super().update(dt)
        if self.timer >= DISASTER_SPEED:
            self.timer = 0
            if not self.move():
                self.finish = True