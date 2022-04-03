from option import *
from src.map import City
from src.building import *
from project_od.gui import Panel,Label
from src.cardDisaster import *
from src.level import Level
from src.ressources import import_background


class GameManager:
    game_background = import_background("background_game")


    def __init__(self, screen) -> None:
        self.in_game = False
        self.game_finish = False
        self.selecting = False
        self.paused = False
        self.shutdown = False
        self.how_to = False

        self.city = None
        self.side_bar = None
        self.screen = screen

        self.init_value()

        self.l = None
        self.current_level = 1

    def init_value(self):
        self.disaster_selected = None
        self.disaster_launch = False

        self.disaster = None
        self.score = 0

        self.disaster_count = 0


    def set_disaster(self, disaster):
        if not self.disaster_launch:
            if self.disaster_selected:
                self.disaster_selected.selected = False
            self.disaster_selected = disaster
            disaster.selected = True

    def set_level(self, level):
        self.current_level = level

    def load_level(self, level=-1):
        if level != -1:
            self.current_level = level
        self.city = City(self)
        self.l = Level(self.current_level)
        setup = self.l.report()

        self.init_value()

        self.city.grid = []
        for line in setup['grid']:
            row = []
            for tile in line:
                if tile == '0':
                    row.append(NoBuilding(self))
                elif tile == '1':
                    row.append(House(self))
                elif tile == '2':
                    row.append(FireStation(self))
                elif '3' in tile:
                    row.append(Dyke(self))
                elif tile == '4':
                    row.append(Bunker(self))
                elif tile == '5':
                    row.append(Forum(self))
                elif tile == '6':
                    row.append(Church(self))
            self.city.grid.append(row)

        self.city.w = setup["size"]
        self.city.h = setup["size"]

        pn = Panel((0,0), (SIDE_WIDTH, HEIGHT))

        self.cards = []
        positions = [(0,CARD_PADDING_Y),(CARD_PADDING_X+CARD_WIDTH,CARD_PADDING_Y),(0,CARD_PADDING_Y + CARD_HEIGHT + CARD_PADDING_Y),(CARD_PADDING_X+CARD_WIDTH,CARD_PADDING_Y + CARD_HEIGHT + CARD_PADDING_Y),(0,2*(CARD_PADDING_Y + CARD_HEIGHT) + CARD_PADDING_Y),(CARD_PADDING_X+CARD_WIDTH,2*(CARD_PADDING_Y + CARD_HEIGHT) + CARD_PADDING_Y)]
        iterator = 0
        for card,qte in setup["cards"]:
            if card == 'tornado':
                self.cards.append(TornadoCard(self,positions[iterator],int(qte)))
                iterator += 1
            elif card == 'tsunami':
                self.cards.append(TsunamiCard(self,positions[iterator],int(qte)))
                iterator += 1
            elif card == 'earthquake':
                self.cards.append(EarthquakeCard(self,positions[iterator],int(qte)))
                iterator += 1
            elif card == 'fire':
                self.cards.append(FireCard(self,positions[iterator],int(qte)))
                iterator += 1
            elif card == 'flood':
                self.cards.append(FloodCard(self,positions[iterator],int(qte)))
                iterator += 1
            elif card == 'meteor':
                self.cards.append(MeteorCard(self,positions[iterator],int(qte)))
                iterator += 1
            elif card == 'volcano':
                self.cards.append(VolcanoCard(self,positions[iterator],int(qte)))
                iterator += 1

            self.disaster_count += int(qte)

        self.score_label = Label((SIDE_POS_X/2-30,10),"Score : 0",NORMAL_FONT)

        pn.add(*self.cards)

        pn.move((SIDE_POS_X, SIDE_POS_Y))

        self.side_bar = pn

    def update(self, screen, dt):
        self.score_label.set_text("Score : "+str(self.score))
        self.side_bar.update()
        self.city.update(0)

        if not self.disaster_launch and self.disaster_count == 0:
            self.finish_level()

        self.city.reset_preview()
        if not self.disaster_launch:
            if self.disaster_selected != None:
                mx, my = pg.mouse.get_pos()
                if mx < SIDE_POS_X:

                    pos = self.disaster_selected.preview(*self.city.cursor_to_grid(mx, my)) # With the mouse
                    for p in pos:
                        self.city.add_preview(p)


                    if len(pos) > 0:
                        if pg.mouse.get_pressed()[0]:
                            self.disaster = self.disaster_selected.get()
                            self.disaster_launch = True
                            self.disaster.launch()
                            self.disaster_count -= 1
                            self.disaster_selected.set_quantity(self.disaster_selected.quantity - 1)
                            if not self.disaster_selected.can_be_selected():
                                self.disaster_selected.selected = False
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

    def finish_level(self):
        self.game_finish = True

    def current_win(self):
        return not self.city.has_forum, self.score

    def play(self, level=-1):
        self.screen.background = self.game_background
        self.in_game = True
        self.game_finish = False
        self.selecting = False
        self.load_level(level)
    
    def reset(self):
        self.play(self.current_level)
    
    def next_level(self):
        self.play(self.current_level + 1)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def quit(self):
        self.shutdown = True

    def home(self):
        self.paused = False
        self.selecting = False
        self.in_game = False
        self.game_finish = False
        self.how_to = False

    def select_level(self):
        self.selecting = True

    def how_to_play(self):
        self.how_to = True
