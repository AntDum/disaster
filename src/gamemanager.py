from option import CARD_HEIGHT, CARD_PADDING, CARD_WIDTH, CITY_PADDING, HEIGHT, SIDE_POS, SIDE_WIDTH
from src.map import City
from src.building import *
from project_od.gui import Panel
from src.cardDisaster import TornadoCard

class GameManager:
    def __init__(self) -> None:
        self.in_game = False
        self.paused = False
        self.shutdown = False

        self.city = None
        self.side_bar = None

        self.disaster_selected = None

    def set_disaster(self, disaster):
        self.disaster_selected = disaster
    
    def set_level(self, level):
        if level == 1:
            self.city = City()
            self.city.grid = [[House() for _ in range(4)] for _ in range(4)]
            self.city.grid[0][0] = NoBuilding()
            self.city.grid[1][0] = NoBuilding()
            self.city.grid[3][0] = NoBuilding()
            self.city.grid[0][2] = NoBuilding()
            self.city.grid[3][2] = NoBuilding()

            pn = Panel((0,0), (SIDE_WIDTH, HEIGHT))
            #TODO : Automatiser les imports de cartes.
            jor1 = TornadoCard((0,CARD_PADDING))
            jor2 = TornadoCard((0,CARD_PADDING + CARD_HEIGHT + CARD_PADDING))
            jor3 = TornadoCard((CARD_PADDING+CARD_WIDTH,CARD_PADDING))
            jor4 = TornadoCard((CARD_PADDING+CARD_WIDTH,CARD_PADDING + CARD_HEIGHT + CARD_PADDING))

            jor1.on_click = lambda : self.set_disaster(jor1)
            pn.add(jor1, jor2, jor3, jor4)

            pn.move((SIDE_POS, 0))

            self.side_bar = pn
    
    def update(self, screen):
        self.side_bar.update()
        self.city.update(0)
        
        self.city.draw(screen, padding_x=CITY_PADDING,  padding_y=CITY_PADDING)
        self.side_bar.draw(screen)

        self.city.reset_preview()
        if self.disaster_selected != None:
            mx, my = pg.mouse.get_pos()
            if mx < SIDE_POS:

                pos = self.disaster_selected.preview(*self.city.cursor_to_grid(mx, my)) # With the mouse
                for p in pos:
                    self.city.add_preview(p)
        

    def play(self):
        self.in_game = True
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
    
    def quit(self):
        self.shutdown = True

    