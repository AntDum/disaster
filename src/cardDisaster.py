from src.disaster import Fire, Flood, Meteor, Tornado, Earthquake, Tsunami, Volcano
from project_od.gui import GUIComponent, Label, THEME_WHITE
from option import *
from src.ressources import import_card
import pygame as pg

class Card(GUIComponent):
    def __init__(self,manager,pos = (0,0), quantity = 1, **kwargs) -> None:
        super().__init__(pos,(CARD_WIDTH, CARD_HEIGHT), **kwargs)
        self.quantity = quantity
        self.manager = manager
        theme = THEME_WHITE
        theme.border_radius = 8
        self.selected = False
        self.dot = GUIComponent((pos[0]+(CARD_WIDTH*0.5)//10, pos[1]+((CARD_HEIGHT*17.5)//20)), (CARD_WIDTH//10, CARD_HEIGHT//10), theme=theme)
        self.label_quantity = Label((pos[0]+((CARD_WIDTH*7)//10),pos[1]+((CARD_HEIGHT*8)//10)), str(quantity), NORMAL_FONT, text_color=(200,0,0))

    def draw(self, screen):
        super().draw(screen)
        self.label_quantity.draw(screen)
        self.dot.draw(screen)

    def update(self):
        super().update()
        self.label_quantity.update()
        self.dot.update()

    def preview(self, x, y):
        return []

    def set_quantity(self, x):
        self.quantity = x
        self.label_quantity.set_text(self.quantity)

    def can_be_selected(self):
        return self.quantity > 0

    def get(self):
        return None

    def on_click(self):
        if self.can_be_selected():
            self.manager.set_disaster(self)
    
    def on_pre_update(self):
        if self.selected:
            self.dot.color = COLOR_SELECTED
        else:
            if self.can_be_selected():
                self.dot.color = COLOR_AVAILABLE
            else:
                self.dot.color = COLOR_NO_AVAILABLE

    def on_press(self):
        if self.can_be_selected() and not self.selected:
            self.dot.color = COLOR_PRESS

    def on_hover(self):
        if self.can_be_selected() and not self.selected:
            self.dot.color = COLOR_HOVER

    def on_focus(self):
        pass

    def move(self, pos):
        super().move(pos)
        self.label_quantity.move(pos)
        self.dot.move(pos)

class TornadoCard(Card):

    image = import_card("tornado")

    def __init__(self, manager,pos = (0,0), quantity = 1) -> None:
        super().__init__(manager, pos, quantity, image=self.image)
        self.axe = 0
        self.pos = (0,0)

    def preview(self, x, y):
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
        return []

    def get(self):
        return Tornado(self.axe, self.pos, self.manager.city)

class TsunamiCard(Card):

    image = import_card("tsunami")

    def __init__(self,manager, pos=(0, 0), quantity=1) -> None:
        super().__init__(manager,pos, quantity, image = self.image)
        self.axe = 0

    def preview(self, x, y):
        city = self.manager.city
        if y != -1 and y != city.h:
            if x == -1: # left
                self.axe = 2
            elif x == city.w: # right
                self.axe = 0
        elif x != -1 and x != city.w:
            if y == -1: # up
                self.axe = 3
            elif y == city.h: # down
                self.axe = 1
        tsu = self.get().preview()
        return [j for i in tsu for j in i]
    
    def get(self):
        return Tsunami(self.manager.city, self.axe)

class FloodCard(Card):

    image = import_card("flood")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, **kwargs, image=self.image)
        self.axe = 0

    def preview(self, x, y):
        city = self.manager.city
        if y != -1 and y != city.h:
            if x == -1: # left
                self.axe = 2
            elif x == city.w: # right
                self.axe = 0
        elif x != -1 and x != city.w:
            if y == -1: # up
                self.axe = 3
            elif y == city.h: # down
                self.axe = 1
        return self.get().preview()
    
    def get(self):
        return Flood(self.manager.city, self.axe)

class FireCard(Card):

    image = import_card("fire")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, **kwargs, image=self.image)

    def preview(self, x, y):
        self.pos = (x,y)
        return self.get().preview()

    def get(self):
        return Fire(self.manager.city, self.pos)

class EarthquakeCard(Card):

    image = import_card("earthquake")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, **kwargs, image=self.image)

    def preview(self, x, y):
        return self.get().preview()

    def get(self):
        return Earthquake(self.manager.city)

class MeteorCard(Card):

    image = import_card("meteor")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, image=self.image, **kwargs)

    def preview(self, x, y):
        self.pos = (x,y)
        return self.get().preview()

    def get(self):
        return Meteor(self.manager.city, self.pos)

class VolcanoCard(Card):

    image = import_card("volcano")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, image=self.image, **kwargs)

    def preview(self, x, y):
        self.pos = (x,y)
        return [j for i in self.get().preview() for j in i]
        

    def get(self):
        return Volcano(self.manager.city, self.pos)
