import pygame as pg
from src.disaster import Tornado
from option import TILE_SIZE
from src.ressources import import_tile
class Case:
    value = 5
    def __init__(self, manager) -> None:
        self.protected = []
        self.blocked = []
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.manager = manager
        self.is_destroyed = False

    def draw(self, screen, x, y):
        screen.blit(self.image, (x,y))

    def update(self, dt=0):
        pass

    def destroy(self): # Détruit le batiment.
        if not self.is_destroyed:
            self.image.fill((255,255,0))
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
        super().__init__(manager)
        self.image.fill((255,0,0))
        self.is_destroyed = True
    

class House(Case):

    value = 20
    
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.image = import_tile("house")

class Bunker(Case):

    value = 10

    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.image.fill((10,10,10))
        self.protected = [Tornado]
