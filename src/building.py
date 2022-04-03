import pygame as pg
from src.disaster import Tornado, Tsunami
from option import TILE_SIZE
from src.ressources import import_tile
class Case:
    value = 5
    destroy_image = import_tile("destruct")
    background_image = import_tile("pave")
    def __init__(self, manager, image) -> None:
        self.protected = []
        self.blocked = []
        self.manager = manager
        self.image = image
        self.is_destroyed = False

    def draw(self, screen, x, y):
        screen.blit(self.background_image, (x,y))
        if self.image:
            screen.blit(self.image, (x,y))

    def update(self, dt=0):
        pass

    def destroy(self): # Détruit le batiment.
        if not self.is_destroyed:
            self.image = self.destroy_image
            self.manager.score += self.value
            self.is_destroyed = True
            print(self.manager.score)

    def is_protected(self, disaster):
        if not self.is_destroyed:
            return isinstance(disaster, tuple(self.protected))
        else:
            return False
    
    def block(self, disaster):
        if not self.is_destroyed:
            return isinstance(disaster, tuple(self.blocked))
        else:
            return False

    
class NoBuilding(Case):

    value = 0
    def __init__(self, manager) -> None:
        super().__init__(manager, None)

        self.is_destroyed = True
    

class House(Case):

    value = 20
    
    def __init__(self, manager) -> None:
        super().__init__(manager, import_tile("bulding"))

class Bunker(Case):

    value = 10

    def __init__(self, manager) -> None:
        super().__init__(manager, pg.Surface((TILE_SIZE, TILE_SIZE)))
        self.protected = [Tornado]
