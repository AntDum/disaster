from project_od.gui import Panel, Button, Label
from option import *
import pygame as pg
import pygame.image as img
import os
from src.ressources import import_button

class Menu:
    btn1_img = import_button("main_menu_button1",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn1_img_hover = import_button("main_menu_button1_hover",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn1_img_click = import_button("main_menu_button1_click",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn2_img = import_button("main_menu_button2",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn2_img_hover = import_button("main_menu_button2_hover",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn2_img_click = import_button("main_menu_button2_click",(BUTTON_WIDTH,BUTTON_HEIGHT))

    def __init__(self, gameManager) -> None:
        self.manager = gameManager
        self.page = -1
        self.panel = None

    def home(self, screen):
        if self.page != 0:
            self.page = 0
            pn = Panel((0,0), (WIDTH, HEIGHT))

            title = Label((30,50), "Welcome to Panic city", NORMAL_FONT, text_color=(255,255,255)).center_x(pn)

            # PLAY BUTTON SETTING


            play_btn = Button((30,150), (BUTTON_WIDTH,BUTTON_HEIGHT), NORMAL_FONT, "Play", image=self.btn1_img).center_x(pn).center_text()
            play_btn.on_hover_enter = lambda : play_btn.set_image(self.btn1_img_hover)
            play_btn.on_hover_exit = lambda : play_btn.set_image(self.btn1_img)
            play_btn.on_press_left = lambda : play_btn.set_image(self.btn1_img_click)



            how_to_btn = Button((30,250), (BUTTON_WIDTH,BUTTON_HEIGHT), NORMAL_FONT, "How to play",image=self.btn2_img).center_x(pn).center_text()
            how_to_btn.on_hover_enter = lambda : how_to_btn.set_image(self.btn2_img_hover)
            how_to_btn.on_hover_exit = lambda : how_to_btn.set_image(self.btn2_img)
            how_to_btn.on_press_left = lambda : how_to_btn.set_image(self.btn2_img_click)
            
            quit_btn = Button((30,350), (150,50), NORMAL_FONT, "Quit", image=self.btn1_img).center_x(pn).center_text()
            quit_btn.on_hover_enter = lambda : quit_btn.set_image(self.btn1_img_hover)
            quit_btn.on_hover_exit = lambda : quit_btn.set_image(self.btn1_img)
            quit_btn.on_press_left = lambda : quit_btn.set_image(self.btn2_img_click)


            play_btn.on_click = lambda : self.manager.play()
            quit_btn.on_click = lambda : self.manager.quit()

            pn.add(play_btn, how_to_btn, quit_btn, title)
            self.panel = pn
        
        self.panel.update()
        self.panel.draw(screen)

    def pause(self, screen):
        pass