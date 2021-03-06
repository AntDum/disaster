from src.ressources import import_disaster, import_tile
from src.building import NoBuilding
from option import CITY_PADDING_X, CITY_PADDING_Y, TILE_SIZE, WATER_COLOR
from project_od.utils import clamp


class City:
    water = import_tile("eau")
    preview_image = import_disaster("preview")

    def __init__(self, manager, coasts) -> None:
        self.grid = []
        self.coast = coasts #Left, Up, Right, Down
        self.preview_disaster = set()
        self.preview_destroy = set()
        self.w = 0
        self.h = 0
        self.padding = [0,0]
        self.fire_station = []
        self.forum = []
        self.manager = manager


    def draw(self, screen):
        # Dessine toute les cases
        for y, line in enumerate(self.grid):
            for x, case in enumerate(line):
                case.draw(screen, *self.grid_to_screen((x,y)))

        # Dessine les cotes
        if self.coast[0]:
            for y in range(self.h):
                screen.draw_rect((self.grid_to_screen((-1, y)), (TILE_SIZE, TILE_SIZE)), WATER_COLOR)
        if self.coast[1]:
            for x in range(self.w):
                screen.draw_rect((self.grid_to_screen((x, -1)), (TILE_SIZE, TILE_SIZE)), WATER_COLOR)
        if self.coast[2]:
            for y in range(self.h):
                screen.draw_rect((self.grid_to_screen((self.w, y)), (TILE_SIZE, TILE_SIZE)), WATER_COLOR)
        if self.coast[3]:
            for x in range(self.w):
                screen.draw_rect((self.grid_to_screen((x, self.h)), (TILE_SIZE, TILE_SIZE)), WATER_COLOR)
        
        # Dessine les previews
        for x,y in self.preview_disaster:
            x, y = self.grid_to_screen((x,y))
            screen.blit(self.preview_image, ((x, y)))
        # Dessine les previews destroy
        for x,y in self.preview_destroy:
            x, y = self.grid_to_screen((x,y))
            screen.blit(self.preview_image, ((x, y)))

    def update(self, dt):
        for line in self.grid:
            for case in line:
                case.update(dt)

    def __getitem__(self, i):
        if 0 <= i[1] < len(self.grid) and 0 <= i[0] < len(self.grid[i[1]]):
            return self.grid[i[1]][i[0]]
        else:
            return NoBuilding(self.manager)


    def __setitem__(self, i, e):
        self.grid[i[1]][i[0]] = e

    def reset_preview(self):
        self.preview_disaster.clear()
        self.preview_destroy.clear()

    def add_preview(self, pos):
        self.preview_disaster.add(pos)

    def add_destroy(self, pos):
        self.preview_destroy.add(pos)

    def cursor_to_grid(self, x, y):
        x -= CITY_PADDING_X
        y -= CITY_PADDING_Y
        x //= TILE_SIZE
        y //= TILE_SIZE
        x = clamp(x, -1, self.w)
        y = clamp(y, -1, self.h)
        # print(x,y)
        return x,y

    def grid_to_screen(self, pos):
        return self.padding[0] + CITY_PADDING_X + pos[0]*(TILE_SIZE + 1), self.padding[1] + CITY_PADDING_Y + pos[1]*(TILE_SIZE + 1)

    def has_fire_man(self):
        return any([case.alive() for case in self.fire_station])

    def has_forum(self):
        return any([case.alive() for case in self.forum])
