import pygame as pg
from src.disaster import Tornado
from option import TILE_SIZE
from src.ressources import import_tile
class Case:
    def __init__(self) -> None:
        self.protected = []
        self.blocked = []
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))

    def draw(self, screen, x, y):
        screen.blit(self.image, (x,y))

    def update(self, dt=0):
        pass

    def destroy(self): # Détruit le batiment.
        pass

    def is_protected(self, disaster):
        return isinstance(disaster, tuple(self.protected))
    
    def block(self, disaster):
        return isinstance(disaster, tuple(self.blocked))

    
class NoBuilding(Case):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill((255,0,0))
    
    def is_protected(self, disaster):
        return False

class House(Case):
    def __init__(self) -> None:
        super().__init__()
        self.image = import_tile("house")

class Bunker(Case):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill((10,10,10))
        self.protected = [Tornado]
