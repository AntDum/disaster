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

    def preview(self, x, y):

        return [(x+i, y) for i in range(4)]


class TsunamiCard(Card):

    #image = img.load(os.path.join("res","cards","tsunami.png"))
    
    def __init__(self, pos=(0, 0), quantity=1) -> None:
        super().__init__(pos, quantity)
