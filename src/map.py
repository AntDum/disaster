from option import TILE_SIZE


class City:
    def __init__(self) -> None:
        self.grid = []
        self.coast = [False, False, False, False] #Left, Up, Right, Down

    def draw(self, screen, padding_x=0, padding_y =0):
        for y, line in enumerate(self.grid):
            for x, case in enumerate(line):
                case.draw(screen, padding_x + x*(TILE_SIZE + 1), padding_y+ y*(TILE_SIZE + 1))

    def update(self, dt):
        for line in self.grid:
            for case in line:
                case.update(dt)

    def __getitem__(self, i):
        return self.city[i[0]][i[1]]