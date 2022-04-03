from option import *
from src.map import City
from src.building import *
from project_od.gui import Panel,Label
from src.cardDisaster import *
from src.level import Level


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

        self.l = None

    def set_disaster(self, disaster):
        if not self.disaster_launch:
            self.disaster_selected = disaster

    def set_level(self, level):
        self.city = City()
        self.l = Level(level)
        setup = self.l.report()
        print(setup.keys())

        self.city.grid = []
        for line in setup['grid']:
            row = []
            for tile in line:
                if(tile == '0'):
                     row.append(NoBuilding(self))
                elif(tile == '1'): row.append(House(self))
            self.city.grid.append(row)

        self.city.w = setup["size"]
        self.city.h = setup["size"]

        pn = Panel((0,0), (SIDE_WIDTH, HEIGHT))
        #TODO : Automatiser les imports de cartes.

        self.cards = []
        positions = [(0,CARD_PADDING),(CARD_PADDING+CARD_WIDTH,CARD_PADDING),(0,CARD_PADDING + CARD_HEIGHT + CARD_PADDING),(CARD_PADDING+CARD_WIDTH,CARD_PADDING + CARD_HEIGHT + CARD_PADDING),(0,2*(CARD_PADDING + CARD_HEIGHT) + CARD_PADDING),(CARD_PADDING+CARD_WIDTH,2*(CARD_PADDING + CARD_HEIGHT) + CARD_PADDING)]
        iterator = 0
        for card,qte in setup["cards"]:
            if(card == 'tornado'):
                self.cards.append(TornadoCard(self,positions[iterator],int(qte)))
                iterator += 1
            if(card == 'tsunami'):
                self.cards.append(TsunamiCard(self,positions[iterator],int(qte)))
                iterator += 1
            if(card == 'earthquake'):
                self.cards.append(EarthquakeCard(self,positions[iterator],int(qte)))
                iterator += 1
            if(card == 'fire'):
                self.cards.append(FireCard(self,positions[iterator],int(qte)))
                iterator += 1
            if(card == 'flood'):
                self.cards.append(FloodCard(self,positions[iterator],int(qte)))
                iterator += 1
            if(card == 'meteor'):
                self.cards.append(MeteorCard(self,positions[iterator],int(qte)))
                iterator += 1

        self.score_label = Label((SIDE_POS/2-30,10),"Score : 0",NORMAL_FONT)

        pn.add(*self.cards)

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

                    if len(pos) > 0:
                        if pg.mouse.get_pressed()[0]:
                            self.disaster = self.disaster_selected.get()
                            self.disaster_launch = True
                            self.disaster.launch()
                            self.disaster_selected.set_quantity(self.disaster_selected.quantity - 1)
                            if not self.disaster_selected.can_be_selected():
                                self.disaster_selected = None
        else:
            self.disaster.update(dt)
            if self.disaster.finish:
                self.disaster_launch = False

        self.score_label.draw(screen)
        self.city.draw(screen)
        self.side_bar.draw(screen)

        if self.disaster_launch:
            self.disaster.draw(screen)



    def play(self):
        self.screen.make_background((35,35,35))
        self.in_game = True

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def quit(self):
        self.shutdown = True
