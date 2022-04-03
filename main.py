import pygame as pg
from src.gamemanager import GameManager
from src.menu import Menu
from project_od.screen import SmartScreen
from option import *
from pygame.locals import*

pygame.mixer.init()
musique = pygame.mixer.Sound("res/X2Download.com - Art of Silence - Dramatic _ Cinematic [Free to use] (320 kbps).mp3")
musique.play(-1,0,0)

pg.init()

screen = SmartScreen(WIDTH, HEIGHT, caption="Welcome to Panic city")

clock = pg.time.Clock()

gameManager = GameManager(screen)
menu = Menu(gameManager)

# Skip menu

while not gameManager.shutdown:
    dt = clock.tick(30) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
           gameManager.quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if gameManager.in_game:
                    if gameManager.paused:
                        gameManager.resume()
                    else:
                        gameManager.pause()

    screen.draw_background()

    if gameManager.in_game:
        if gameManager.paused:
            menu.pause(screen)
        elif gameManager.game_finish:
            menu.end_game(screen)
        else:
            gameManager.update(screen, dt)
    else:
        if gameManager.selecting:
            menu.menu_selector(screen)
        elif gameManager.how_to:
            menu.menu_how_to_play(screen)
        else:
            menu.home(screen)

    screen.display_update()


pg.quit()
