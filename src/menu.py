from cProfile import label
from email.header import Header
from project_od.gui import Panel, Button, Label
from option import *
import pygame as pg

class Menu:
    def __init__(self, gameManager) -> None:
        self.manager = gameManager
        self.page = -1
        self.panel = None

    def home(self, screen):
        if self.page != 0:
            self.page = 0
            pn = Panel((0,0), (WIDTH, HEIGHT))

            title = Label((30,50), "Welcome to Panic city", NORMAL_FONT, text_color=(255,255,255)).center_x(pn)

            play_btn = Button((30,150), (150,50), NORMAL_FONT, "Play").center_x(pn).center_text()
            how_to_btn = Button((30,250), (150,50), NORMAL_FONT, "How to play").center_x(pn).center_text()
            quit_btn = Button((30,350), (150,50), NORMAL_FONT, "Quit").center_x(pn).center_text()

            play_btn.on_click = lambda : self.manager.play()
            quit_btn.on_click = lambda : self.manager.quit()

            pn.add(play_btn, how_to_btn, quit_btn, title)
            self.panel = pn
        
        self.panel.update()
        self.panel.draw(screen)

    def pause(self, screen):
        pass