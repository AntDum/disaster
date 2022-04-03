import pygame as pg
from src.disaster import Earthquake, Fire, Flood, Tornado, Tsunami, Volcano
from option import TILE_SIZE
from src.ressources import import_tile
class Case:
    value = 5
    destroy_image = import_tile("ruins")
    background_image = import_tile("cobble")
    def __init__(self, manager, image) -> None:
        self.protected = []
        self.blocked = []
        self.dammagable = []
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
            # print(self.manager.score)

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

    def is_dammagable(self, disaster):
        if not self.is_destroyed:
            return isinstance(disaster, tuple(self.dammagable))
        else:
            return False

    def alive(self):
        return not self.is_destroyed


class NoBuilding(Case):

    value = 0
    def __init__(self, manager) -> None:
        super().__init__(manager, None)

        self.is_destroyed = True


class House(Case):

    value = 20

    def __init__(self, manager) -> None:
        super().__init__(manager, import_tile("house"))
        self.blocked = []
        self.protected = [Earthquake]

class Bunker(Case):

    value = 10

    def __init__(self, manager) -> None:
        super().__init__(manager, import_tile("Bunker"))
        self.protected = [Tornado, Fire, Tsunami, Flood, Volcano]

class Church(Case):
    def __init__(self, manager) -> None:
        super().__init__(manager,  import_tile("church"))
        self.blocked = [Tornado]
        self.protected = [Earthquake]

class FireStation(Case):
    def __init__(self, manager) -> None:
        super().__init__(manager,  import_tile("firefighters"))
        self.blocked = []
        self.protected = [Fire, Earthquake]
        manager.city.fire_station.append(self)

class Dyke(Case):
    def __init__(self, manager) -> None:
        super().__init__(manager,  import_tile("Dig"))
        self.blocked = [Tsunami, Flood]
        self.protected = [Tsunami, Flood,Tornado]

class Forum(Case):
    def __init__(self, manager) -> None:
        super().__init__(manager,  import_tile("Mairie"))
        self.blocked = []
        self.protected = [Tsunami,Flood,Tornado, Earthquake]
        manager.city.forum.append(self)
