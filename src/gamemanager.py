from option import *
from project_od.gui.component import Button
from src.map import City
from src.building import *
from project_od.gui import Panel,Label
from src.cardDisaster import *
from src.level import Level
from src.ressources import import_background, import_button


class GameManager:
    game_background = import_background("background_game")
    menu_background = import_background("main_menu")
    end_game_background = import_background("end_game")
    small_planche = import_button("big_planche", (BUTTON_WIDTH, BUTTON_HEIGHT))

    btn_reset_img = import_button("restart_button",(BUTTON_HEIGHT, BUTTON_HEIGHT))
    btn_reset_img_clicked = import_button("restart_button_clicked",(BUTTON_HEIGHT, BUTTON_HEIGHT))
    # btn_reset_img_hover = import_button("restart_button_hover",(BUTTON_HEIGHT*2, BUTTON_HEIGHT))

    btn_pause_img = import_button("pause_button",(BUTTON_HEIGHT, BUTTON_HEIGHT))
    btn_pause_img_clicked = import_button("pause_button_clicked",(BUTTON_HEIGHT, BUTTON_HEIGHT))
    # btn_pause_img_hover = import_button("pause_button_hover",(BUTTON_HEIGHT*2, BUTTON_HEIGHT))

    def __init__(self, screen) -> None:
        self.in_game = False
        self.game_finish = False
        self.selecting = False
        self.paused = False
        self.end_game = False
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
        self.l = Level(self.current_level)
        setup = self.l.report()
        coco = ['1' in setup["coasts"],'2' in setup["coasts"],'3' in setup["coasts"],'4' in setup["coasts"]]
        self.city = City(self,coco)

        self.init_value()

        self.city.grid = []
        for line in setup['grid']:
            row = []
            for tile in line:
                if tile == '1':
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
                else :
                    row.append(NoBuilding(self))
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

        pn.add(*self.cards)

        pn.move((SIDE_POS_X, SIDE_POS_Y))

        self.score_label = Button((SIDE_POS_X/2-30,-20),(BUTTON_WIDTH, BUTTON_HEIGHT), NORMAL_FONT_BOLD, "Score : 0", text_color=(255,255,255)).center_text()
        self.score_label.set_image(self.small_planche)

        pn_btn = Panel((0,0), (WIDTH, HEIGHT))

        self.pause_btn = Button((0,0), (BUTTON_HEIGHT, BUTTON_HEIGHT), NORMAL_FONT, "", image=self.btn_pause_img)
        self.pause_btn.on_press_left = lambda : self.pause_btn.set_image(self.btn_pause_img_clicked)
        self.pause_btn.on_hover_exit = lambda : self.pause_btn.set_image(self.btn_pause_img)
        self.pause_btn.on_click = lambda : self.pause()

        self.reset_btn = Button((BUTTON_HEIGHT,0), (BUTTON_HEIGHT, BUTTON_HEIGHT), NORMAL_FONT, "", image=self.btn_reset_img)
        self.reset_btn.on_press_left = lambda : self.reset_btn.set_image(self.btn_reset_img_clicked)
        self.reset_btn.on_hover_exit = lambda : self.reset_btn.set_image(self.btn_reset_img)
        self.reset_btn.on_click = lambda : self.reset()

        pn_btn.add(self.pause_btn, self.reset_btn)
        self.tool = pn_btn

        self.side_bar = pn

    def update(self, screen, dt):
        self.score_label.set_text("Score : "+str(self.score))
        self.side_bar.update()
        self.tool.update()
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
        self.tool.draw(screen)
        self.city.draw(screen)
        self.side_bar.draw(screen)

        if self.disaster_launch:
            self.disaster.draw(screen)

    def finish_level(self):
        self.screen.background = self.menu_background
        self.game_finish = True

    def current_win(self):
        return not self.city.has_forum(), self.score

    def play(self, level=-1):
        self.screen.background = self.game_background
        self.in_game = True
        self.game_finish = False
        self.selecting = False
        self.load_level(level)

    def reset(self):
        self.play(self.current_level)

    def next_level(self):
        if self.current_level + 1 > NUMBER_LEVEL:
            self.screen.background = self.end_game_background
            self.end_game = True
        else:
            self.play(self.current_level + 1)

    def pause(self):
        self.screen.background = self.menu_background
        self.paused = True

    def resume(self):
        self.screen.background = self.game_background
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
