from project_od.gui import Panel, Button, Label,GUIComponent
from option import *
import pygame as pg
from src.ressources import import_button,import_background, import_tutorial

class Menu:

    btn1_img = import_button("main_menu_button1",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn1_img_hover = import_button("main_menu_button1_hover",(BUTTON_WIDTH,BUTTON_HEIGHT))
    btn1_img_click = import_button("main_menu_button1_click",(BUTTON_WIDTH,BUTTON_HEIGHT))

    btn2_img = import_button("main_menu_button2",(int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)))
    btn2_img_hover = import_button("main_menu_button2_hover",(int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)))
    btn2_img_click = import_button("main_menu_button2_click",(int(BUTTON_WIDTH*1.4),int(BUTTON_HEIGHT*1.4)))

    btn_resume_img = import_button("resume_button",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)))
    btn_resume_img_clicked = import_button("resume_button_clicked",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)))

    btn_exit_img = import_button("exit_button",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1)))
    btn_exit_img_clicked = import_button("exit_button_clicked",(BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1)))

    big_planche = import_button("big_planche",(int(BUTTON_WIDTH*2.4),int(BUTTON_HEIGHT*2)))
    small_planche = import_button("big_planche", (BUTTON_WIDTH, BUTTON_HEIGHT))

    btn_level = import_button("level_button", (BUTTON_LENGTH, BUTTON_LENGTH))
    btn_level_hover = import_button("level_button_hover", (BUTTON_LENGTH, BUTTON_LENGTH))
    btn_level_press = import_button("level_button_press", (BUTTON_LENGTH, BUTTON_LENGTH))

    big_panel = import_button("big_planche",(int(BUTTON_WIDTH*4.5),int(BUTTON_HEIGHT*8)))

    pause_bckg = import_button("big_planche",(PANEL_WIDTH,PANEL_HEIGHT))
    bckg = import_background("main_menu")


    tutorial = [import_tutorial("tornado"),import_tutorial("tsunami"),import_tutorial("volcano"),import_tutorial("fire"),import_tutorial("meteor"),import_tutorial("flood")]

    iterator = 0


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

            play_btn.on_click = lambda : self.manager.select_level()
            how_to_btn.on_click = lambda : self.manager.how_to_play()
            quit_btn.on_click = lambda : self.manager.quit()

            pn.add(play_btn, how_to_btn, quit_btn, big_planche, title)
            self.panel = pn

        self.panel.update()
        self.panel.draw(screen)

    def pause(self, screen):
        if self.page != 1:
            self.page = 1
            screen.background = self.bckg
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
            exit_btn.on_click = lambda : self.manager.home()


            pn.add(panel_bckg,resume_btn,exit_btn,title)
            self.panel = pn

        self.panel.update()
        self.panel.draw(screen)

    def menu_selector(self, screen):
        if self.page != 2:
            self.page = 2
            screen.background = self.bckg
            pn = Panel((0,0), (WIDTH, HEIGHT))

            X = [BUTTON_SPACING, BUTTON_SPACING*3, BUTTON_SPACING*5, BUTTON_SPACING*7, BUTTON_SPACING*9, BUTTON_SPACING*11, BUTTON_SPACING*13, BUTTON_SPACING*15]
            Y = [BUTTON_SPACING, BUTTON_SPACING*3, BUTTON_SPACING*5, BUTTON_SPACING*7]

            btn_list = []

            for i in range(NUMBER_LEVEL):
                x = X[i%len(X)]
                y = Y[i//len(X)] + BUTTON_SPACING // 2

                btn = Button((x,y), (BUTTON_LENGTH, BUTTON_LENGTH), LARGE_FONT, str(i+1), image=self.btn_level).center_text()
                btn.on_hover_enter = (lambda j: (lambda : btn_list[j].set_image(self.btn_level_hover)))(i)
                btn.on_hover_exit = (lambda j : (lambda : btn_list[j].set_image(self.btn_level)))(i)
                btn.on_press_left = (lambda j: (lambda : btn_list[j].set_image(self.btn_level_press)))(i)

                btn.on_click = (lambda j : (lambda : self.manager.play(j)))(i+1)
                btn_list.append(btn)

            img_planch = Button((0, -10), (BUTTON_WIDTH, BUTTON_HEIGHT), NORMAL_FONT_BOLD, "Level selection", text_color=(255,255,255)).center_x(pn).center_text()
            img_planch.set_image(self.small_planche)

            pn.add(*btn_list)
            pn.add(img_planch)

            self.panel = pn

        self.panel.update()
        self.panel.draw(screen)

    def lmd(self,obj):
        self.iterator += 1
        if(self.iterator < len(self.tutorial)):
            obj.set_image(self.tutorial[self.iterator])
        else:
            self.manager.home()

    def menu_how_to_play(self,screen):
        if self.page != 3:
            self.page = 3
            self.background = self.bckg

            pn = Panel((0,0), (WIDTH, HEIGHT))

            big_panel = GUIComponent((30,-10),(int(BUTTON_WIDTH*4.5),int(BUTTON_HEIGHT*8)), image = self.big_panel).center_x(pn).move((-20,-80))

            # print((int(BUTTON_WIDTH*4.5),int(BUTTON_HEIGHT*8)))

            exit_btn = Button((15,150), (BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1)), LARGE_FONT, "", image=self.btn_exit_img).center_x(pn).center_y(pn).move((430,180))
            exit_btn.on_press_left = lambda : exit_btn.set_image(self.btn_exit_img_clicked)
            exit_btn.on_hover_exit = lambda : exit_btn.set_image(self.btn_exit_img)
            exit_btn.on_click = lambda : self.manager.home()

            self.iterator = 0

            tuto = Button((0,0), (TUTO_WIDTH,TUTO_HEIGHT),NORMAL_FONT,"", image = self.tutorial[self.iterator]).center_x(pn).center_y(pn)

            tuto.on_click = lambda : self.lmd(tuto)

            pn.add(big_panel,exit_btn,tuto)
            self.panel = pn

        self.panel.update()
        self.panel.draw(screen)
    
    def end_game(self, screen):
        if self.page != 4:
            self.page = 4
            self.background = self.bckg

            pn = Panel((0,0), (WIDTH, HEIGHT))
            panel_bckg = GUIComponent((30,30),(PANEL_WIDTH,PANEL_HEIGHT), image = self.pause_bckg).center_x(pn).center_y(pn)

            win, score = self.manager.current_win()
            title = Label((30,50), "Win" if win else "Lose" + " Score : " + str(score), LARGE_FONT, text_color=(255,255,255)).center_x(pn).move((-50,0))

            if win:
                resume_btn = Button((15,150), (BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)), LARGE_FONT, "", image=self.btn_resume_img).center_x(pn).center_y(pn).move((150,0))
                resume_btn.on_click = lambda : self.manager.next_level()
            else:
                resume_btn = Button((15,150), (BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)), LARGE_FONT, "", image=self.btn_resume_img).center_x(pn).center_y(pn).move((150,0))
                resume_btn.on_click = lambda : self.manager.reset()

            resume_btn.on_press_left = lambda : resume_btn.set_image(self.btn_resume_img_clicked)
            resume_btn.on_hover_exit = lambda : resume_btn.set_image(self.btn_resume_img)

            exit_btn = Button((15,150), (BUTTON_HEIGHT*2,int(BUTTON_HEIGHT*1.5)), LARGE_FONT, "", image=self.btn_exit_img).center_x(pn).center_y(pn).move((-150,0))
            exit_btn.on_press_left = lambda : exit_btn.set_image(self.btn_exit_img_clicked)
            exit_btn.on_hover_exit = lambda : exit_btn.set_image(self.btn_exit_img)
            exit_btn.on_click = lambda : self.manager.home()


            pn.add(panel_bckg,resume_btn,exit_btn,title)
            self.panel = pn

        self.panel.update()
        self.panel.draw(screen)