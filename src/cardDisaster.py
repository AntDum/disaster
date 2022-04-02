from project_od.gui import GUIComponent
from option import CARD_WIDTH, CARD_HEIGHT
import pygame.image as img
import os

class Card(GUIComponent):
    def __init__(self,city,pos = (0,0), quantity = 1) -> None:
        super().__init__(pos,(CARD_WIDTH, CARD_HEIGHT))
        self.quantity = quantity
        self.city = city

    def draw(self, screen):
        super().draw(screen)

    def update(self):
        super().update()
    
    def preview(self, x, y):
        pass

class TornadoCard(Card):

    #image = img.load(os.path.join("res","cards","tornado.png"))

    def __init__(self, city,pos = (0,0), quantity = 1) -> None:
        super().__init__(city, pos, quantity)
        self.axe = 0
        self.pos = (0,0)
        self.launchable = False

    def preview(self, x, y):
        self.launchable = True
        if y != -1 and y != self.city.h:
            if x == -1:
                self.axe = 2
                self.pos = (0,y)
                return [(i, y) for i in range(self.city.w)]
            elif x == self.city.w:
                self.axe = 0
                self.pos = (self.city.w-1,y)
                return [(i, y) for i in range(self.city.w-1, -1, -1)]
        elif x != -1 and x != self.city.w:
            if y == -1:
                self.axe = 0
                self.pos = (x,0)
                return [(x, i) for i in range(self.city.h)]
            elif y == self.city.h:
                self.axe = 3
                self.pos = (x,self.city.h-1)
                return [(x, i) for i in range(self.city.h-1, -1, -1)]
        self.launchable = False
        return []


class TsunamiCard(Card):

    #image = img.load(os.path.join("res","cards","tsunami.png"))
    
    def __init__(self,city, pos=(0, 0), quantity=1) -> None:
        super().__init__(city,pos, quantity)
