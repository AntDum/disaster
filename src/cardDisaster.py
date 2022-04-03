from src.disaster import Fire, Tornado, Earthquake
from project_od.gui import GUIComponent, Label
from option import CARD_WIDTH, CARD_HEIGHT, NORMAL_FONT
from src.ressources import import_card


class Card(GUIComponent):
    def __init__(self,manager,pos = (0,0), quantity = 1, **kwargs) -> None:
        super().__init__(pos,(CARD_WIDTH, CARD_HEIGHT), **kwargs)
        self.quantity = quantity
        self.manager = manager
        self.label_quantity = Label((pos[0]+((CARD_WIDTH*7)//10),pos[1]+((CARD_HEIGHT*8)//10)), str(quantity), NORMAL_FONT, text_color=(200,0,0))

    def draw(self, screen):
        super().draw(screen)
        self.label_quantity.draw(screen)

    def update(self):
        super().update()
        self.label_quantity.update()

    def preview(self, x, y):
        pass

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

    def move(self, pos):
        super().move(pos)
        self.label_quantity.move(pos)

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

    def preview(self, x, y):
        pass


class FloodCard(Card):

<<<<<<< HEAD
    image = import_card("flood")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, **kwargs, image=self.image)


class FireCard(Card):

    image = import_card("fire")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, **kwargs, image=self.image)
=======
    image = import_card("Journal inondation ")
    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, image=self.image, **kwargs)


class FireCard(Card):
    image = import_card("Journal incendie")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, image=self.image, **kwargs)
        self.pos = (0,0)
>>>>>>> 0686b536ec152441de9e575d8cc054c64eaddd35

    def preview(self, x, y):
        self.pos = (x,y)
        return self.get().preview()

    def get(self):
        return Fire(self.manager.city, self.pos)

class EarthquakeCard(Card):

<<<<<<< HEAD
    image = import_card("earthquake")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, **kwargs, image=self.image)

    def preview(self):
        return Earthquake().preview()
=======
    image = import_card("Journal séisme ")

    def __init__(self, manager, pos=(0, 0), quantity=1, **kwargs) -> None:
        super().__init__(manager, pos, quantity, image=self.image,**kwargs)
    
    def preview(self, x, y):
        return self.get().preview()
>>>>>>> 0686b536ec152441de9e575d8cc054c64eaddd35

    def get(self):
        return Earthquake(self.manager.city)
