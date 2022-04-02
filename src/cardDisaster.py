from src.disaster import Tornado
from project_od.gui import GUIComponent
from option import CARD_WIDTH, CARD_HEIGHT
from src.ressources import import_card


class Card(GUIComponent):
    def __init__(self,manager,pos = (0,0), quantity = 1, **kwargs) -> None:
        super().__init__(pos,(CARD_WIDTH, CARD_HEIGHT), **kwargs)
        self.quantity = quantity
        self.manager = manager

    def draw(self, screen):
        super().draw(screen)

    def update(self):
        super().update()
    
    def preview(self, x, y):
        pass

    def get(self):
        return None

    def on_click(self):
        if self.quantity > 0:
            self.manager.set_disaster(self)

class TornadoCard(Card):

    image = import_card("tornado")

    def __init__(self, manager,pos = (0,0), quantity = 1) -> None:
        super().__init__(manager, pos, quantity, image=self.image)
        self.axe = 0
        self.pos = (0,0)
        self.launchable = False

    def preview(self, x, y):
        self.launchable = True
        city = self.manager.city
        if y != -1 and y != city.h:
            if x == -1: # right
                self.axe = 2
                self.pos = (0,y)
                return self.get().preview()
            elif x == city.w: # left
                self.axe = 0
                self.pos = (city.w-1,y)
                return self.get().preview()
        elif x != -1 and x != city.w:
            if y == -1: # down
                self.axe = 3
                self.pos = (x,0)
                return self.get().preview()
            elif y == city.h: # up
                self.axe = 1
                self.pos = (x,city.h-1)
                return self.get().preview()
        self.launchable = False
        return []
    
    def get(self):
        return Tornado(self.axe, self.pos, self.manager.city)



class TsunamiCard(Card):

    image = import_card("tsunami")
    
    def __init__(self,manager, pos=(0, 0), quantity=1) -> None:
        super().__init__(manager,pos, quantity, image = self.image)
