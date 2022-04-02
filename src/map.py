from option import CITY_PADDING, TILE_SIZE
from project_od.utils import clamp


class City:
    def __init__(self) -> None:
        self.grid = []
        self.coast = [False, False, False, False] #Left, Up, Right, Down
        self.preview_disaster = set()
        self.w = 0
        self.h = 0


    def draw(self, screen, padding_x=0, padding_y =0):
        for y, line in enumerate(self.grid):
            for x, case in enumerate(line):
                case.draw(screen, padding_x + x*(TILE_SIZE + 1), padding_y+ y*(TILE_SIZE + 1))
        for x,y in self.preview_disaster:
            screen.draw_rect(((padding_x + x*(TILE_SIZE + 1) + TILE_SIZE//4, padding_y+ y*(TILE_SIZE + 1) + TILE_SIZE//4),
                                    (TILE_SIZE//2, TILE_SIZE//2)), (0,0,255))

    def update(self, dt):
        for line in self.grid:
            for case in line:
                case.update(dt)

    def __getitem__(self, i):
        return self.city[i[0]][i[1]]

    def reset_preview(self):
        self.preview_disaster.clear()

    def add_preview(self, pos):
        self.preview_disaster.add(pos)

    def cursor_to_grid(self, x, y):
        x -= CITY_PADDING
        y -= CITY_PADDING
        x //= TILE_SIZE
        y //= TILE_SIZE
        x = clamp(x, -1, self.w)
        y = clamp(y, -1, self.h)
        # print(x,y)
        return x,y