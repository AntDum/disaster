from project_od.gui import Panel, Button, Label,GUIComponent
from option import *
import pygame as pg
from src.ressources import import_button,import_background

class Menu:

    btn1_img = import_button("main_menu_button1",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn1_img_hover = import_button("main_menu_button1_hover",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn1_img_click = import_button("main_menu_button1_click",(BUTTON_WIDTH,BUTTON_HEIGHT))

    btn2_img = import_button("main_menu_button2",(int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)))
    btn2_img_hover = import_button("main_menu_button2_hover",(int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)))
    btn2_img_click = import_button("main_menu_button2_click",(int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)))

<<<<<<< HEAD
    btn_resume_img = import_button("resume_button",(BUTTON_HEIGHT,BUTTON_HEIGHT))
=======
    btn_resume_img = import_button("resume_button",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)))
    btn_resume_img_clicked = import_button("resume_button_clicked",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)))

    btn_exit_img = import_button("exit_button",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)))
    btn_exit_img_clicked = import_button("exit_button_clicked",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)))
>>>>>>> a863b6a0ebaa1bf74105e26529f8a6ad1b7ef8b9

    big_planche = import_button("big_planche",(int(BUTTON_WIDTH*2.4),int(BUTTON_HEIGHT*2)))


    pause_bckg = import_button("big_planche",(PANEL_WIDTH,PANEL_HEIGHT))
    bckg = import_background("main_menu")


    def __init__(self, gameManager) -> None:
        self.manager = gameManager
        self.page = -1
        self.panel = None

    def home(self, screen):
        if self.page != 0:
            self.page = 0
            screen.background = self.bckg
            pn = Panel((0,0), (WIDTH, HEIGHT))

            big_planche = GUIComponent((30,-10),(int(BUTTON_WIDTH*2.4),int(BUTTON_HEIGHT*2)), image = self.big_planche).center_x(pn).move((-50,0))
            title = Label((30,50), "Welcome to Panic city", ULTRA_THICC_FONT, text_color=(255,255,255)).center_x(pn).move((-50,0))
            # PLAY BUTTON SETTING
            play_btn = Button((15,150), (BUTTON_WIDTH,BUTTON_HEIGHT), LARGE_FONT, "Play", image=self.btn1_img).center_x(pn).move((-100,0)).center_text()
            play_btn.label.move((35,-3))
            play_btn.on_hover_enter = lambda : play_btn.set_image(self.btn1_img_hover)
            play_btn.on_hover_exit = lambda : play_btn.set_image(self.btn1_img)
            play_btn.on_press_left = lambda : play_btn.set_image(self.btn1_img_click)



            how_to_btn = Button((20,250), (int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)), LARGE_FONT, "How to play",image = self.btn2_img).center_x(pn).move((-50,0)).center_text()
            how_to_btn.on_hover_enter = lambda : how_to_btn.set_image(self.btn2_img_hover)
            how_to_btn.on_hover_exit = lambda : how_to_btn.set_image(self.btn2_img)
            how_to_btn.on_press_left = lambda : how_to_btn.set_image(self.btn2_img_click)

            quit_btn = Button((25,375), (BUTTON_WIDTH,BUTTON_HEIGHT), LARGE_FONT, "Quit", image=self.btn1_img).center_x(pn).move((-100,0)).center_text()
            quit_btn.on_hover_enter = lambda : quit_btn.set_image(self.btn1_img_hover)
            quit_btn.on_hover_exit = lambda : quit_btn.set_image(self.btn1_img)
            quit_btn.on_press_left = lambda : quit_btn.set_image(self.btn1_img_click)
            quit_btn.label.move((35,-3))

            play_btn.on_click = lambda : self.manager.play()
            quit_btn.on_click = lambda : self.manager.quit()

            pn.add(play_btn, how_to_btn, quit_btn, big_planche, title)
            self.panel = pn

        self.panel.update()
        self.panel.draw(screen)

    def pause(self, screen):
        if self.page != 1:
            self.page = 1
            pn = Panel((0,0), (WIDTH, HEIGHT))
            panel_bckg = GUIComponent((30,30),(PANEL_WIDTH,PANEL_HEIGHT), image = self.pause_bckg).center_x(pn).center_y(pn)
            title = Label((30,50), "Pause", LARGE_FONT, text_color=(255,255,255)).center_x(pn).move((-50,0))

            resume_btn = Button((15,150), (BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)), LARGE_FONT, "", image=self.btn_resume_img).center_x(pn).center_y(pn).move((150,0))
            resume_btn.on_press_left = lambda : resume_btn.set_image(self.btn_resume_img_clicked)
            resume_btn.on_hover_exit = lambda : resume_btn.set_image(self.btn_resume_img)
            resume_btn.on_click = lambda : self.manager.resume()


            exit_btn = Button((15,150), (BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)), LARGE_FONT, "", image=self.btn_exit_img).center_x(pn).center_y(pn).move((-150,0))
            exit_btn.on_press_left = lambda : exit_btn.set_image(self.btn_exit_img_clicked)
            exit_btn.on_hover_exit = lambda : exit_btn.set_image(self.btn_exit_img)
            exit_btn.on_click = lambda : self.manager.quit()


            pn.add(panel_bckg,resume_btn,exit_btn,title)
            self.panel = pn
        self.panel.update()
        self.panel.draw(screen)
