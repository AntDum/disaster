from option import CARD_HEIGHT, CARD_PADDING, CARD_WIDTH, CITY_PADDING, HEIGHT, SIDE_POS, SIDE_WIDTH
from src.map import City
from src.building import *
from project_od.gui import Panel
from src.cardDisaster import TornadoCard

class GameManager:
    def __init__(self, screen) -> None:
        self.in_game = False
        self.paused = False
        self.shutdown = False

        self.city = None
        self.side_bar = None
        self.screen = screen

        self.disaster_selected = None
        self.disaster_launch = False

        self.disaster = None

    def set_disaster(self, disaster):
        if not self.disaster_launch:
            self.disaster_selected = disaster
    
    def set_level(self, level):
        if level == 1:
            self.city = City()
            w = 4
            h = 4
            self.city.grid = [[House() for _ in range(w)] for _ in range(h)]
            self.city.w = w
            self.city.h = h
            self.city.grid[0][0] = NoBuilding()
            self.city.grid[1][0] = NoBuilding()
            self.city.grid[3][0] = NoBuilding()
            self.city.grid[0][2] = NoBuilding()
            self.city.grid[3][2] = NoBuilding()

            pn = Panel((0,0), (SIDE_WIDTH, HEIGHT))
            #TODO : Automatiser les imports de cartes.
            jor1 = TornadoCard(self.city,(0,CARD_PADDING))
            jor2 = TornadoCard(self.city,(0,CARD_PADDING + CARD_HEIGHT + CARD_PADDING))
            jor3 = TornadoCard(self.city,(CARD_PADDING+CARD_WIDTH,CARD_PADDING))
            jor4 = TornadoCard(self.city,(CARD_PADDING+CARD_WIDTH,CARD_PADDING + CARD_HEIGHT + CARD_PADDING))

            jor1.on_click = lambda : self.set_disaster(jor1)
            pn.add(jor1, jor2, jor3, jor4)

            pn.move((SIDE_POS, 0))

            self.side_bar = pn
    
    def update(self, screen):
        self.side_bar.update()
        self.city.update(0)
        
        self.city.reset_preview()
        if not self.disaster_launch():
            if self.disaster_selected != None:
                mx, my = pg.mouse.get_pos()
                if mx < SIDE_POS:

                    pos = self.disaster_selected.preview(*self.city.cursor_to_grid(mx, my)) # With the mouse
                    for p in pos:
                        self.city.add_preview(p)

            self.disaster = self.disaster_selected.get()
        else:
            pass

        
        self.city.draw(screen, padding_x=CITY_PADDING,  padding_y=CITY_PADDING)
        self.side_bar.draw(screen)

    
        

    def play(self):
        self.screen.make_background((35,35,35))
        self.in_game = True
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
    
    def quit(self):
        self.shutdown = True

    