import pygame as pg

from option import TILE_SIZE

class Case:
    def __init__(self) -> None:
        self.protected = []
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))

    def draw(self, screen, x, y):
        screen.blit(self.image, (x,y))

    def update(self, dt=0):
        pass

    def destroy(): # Détruit le batiment.
        pass

    def is_protected(self, disaster):
        return isinstance(disaster, self.protected)

    
class NoBuilding(Case):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill((255,0,0))
    
    def is_protected(self, disaster):
        return False

class House(Case):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill((0,255,0))

