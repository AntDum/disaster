from option import *
from src.map import City
from src.building import *
from project_od.gui import Panel,Label
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

        self.score = 0

    def set_disaster(self, disaster):
        if not self.disaster_launch:
            self.disaster_selected = disaster
    
    def set_level(self, level):
        if level == 1:
            self.city = City()
            w = 4
            h = 4
            self.city.grid = [[House(self) for _ in range(w)] for _ in range(h)]
            self.city.w = w
            self.city.h = h
            self.city.grid[0][0] = NoBuilding(self)
            self.city.grid[1][0] = NoBuilding(self)
            self.city.grid[3][0] = NoBuilding(self)
            self.city.grid[0][2] = NoBuilding(self)
            self.city.grid[3][2] = NoBuilding(self)

            pn = Panel((0,0), (SIDE_WIDTH, HEIGHT))
            #TODO : Automatiser les imports de cartes.
            jor1 = TornadoCard(self,(CARD_PADDING+CARD_WIDTH,CARD_PADDING),2)

            self.score_label = Label((SIDE_POS/2-30,10),"Score : 0",NORMAL_FONT)

            pn.add(jor1)

            pn.move((SIDE_POS, 0))

            self.side_bar = pn

            self.score = 0
    
    def update(self, screen, dt):
        self.score_label.set_text("Score : "+str(self.score))
        self.side_bar.update()
        self.city.update(0)
        
        self.city.reset_preview()
        if not self.disaster_launch:
            if self.disaster_selected != None:
                mx, my = pg.mouse.get_pos()
                if mx < SIDE_POS:

                    pos = self.disaster_selected.preview(*self.city.cursor_to_grid(mx, my)) # With the mouse
                    for p in pos:
                        self.city.add_preview(p)

                if pg.mouse.get_pressed()[0]:
                    self.disaster = self.disaster_selected.get()
                    self.disaster_launch = True
                    self.disaster.launch()
                    self.disaster_selected.set_quantity(self.disaster_selected.quantity - 1)
                    self.disaster_selected = None
        else:
            self.disaster.update(dt)
            if self.disaster.finish:
                self.disaster_launch = False

        self.score_label.draw(screen)
        self.city.draw(screen)
        self.side_bar.draw(screen)

        if self.disaster_launch:
            x, y = self.city.grid_to_screen(self.disaster.pos)
            self.disaster.draw(screen, x, y)
    
        

    def play(self):
        self.screen.make_background((35,35,35))
        self.in_game = True
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
    
    def quit(self):
        self.shutdown = True

    