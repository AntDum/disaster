from project_od.gui import GUIComponent
from option import CARD_WIDTH, CARD_HEIGHT
import pygame.image as img
import os

class Card(GUIComponent):
    def __init__(self,pos = (0,0), quantity = 1) -> None:
        super().__init__(pos,(CARD_WIDTH, CARD_HEIGHT))
        self.quantity = quantity

    def draw(self, screen):
        super().draw(screen)

    def update(self):
        super().update()
    
    def preview(self):
        pass

class TornadoCard(Card):

    #image = img.load(os.path.join("res","cards","tornado.png"))

    def __init__(self,pos = (0,0), quantity = 1) -> None:
        super().__init__(pos, quantity)

    def preview(self):
        pass


class TsunamiCard(Card):

    #image = img.load(os.path.join("res","cards","tsunami.png"))
    
    def __init__(self, pos=(0, 0), quantity=1) -> None:
        super().__init__(pos, quantity)
