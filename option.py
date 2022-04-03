from pygame import font
font.init()

WIDTH = 1080
HEIGHT = 576

FPS = 30

TILE_SIZE = 80

CARD_WIDTH = WIDTH // 7
CARD_HEIGHT = CARD_WIDTH
CARD_PADDING_X = CARD_WIDTH // 5
CARD_PADDING_Y = CARD_WIDTH // 20

SIDE_WIDTH = CARD_WIDTH * 2 + CARD_PADDING_X * 3
SIDE_POS_X = WIDTH-SIDE_WIDTH
SIDE_POS_Y = CARD_PADDING_Y * 5

CITY_PADDING_X = SIDE_POS_X // 5
CITY_PADDING_Y = SIDE_POS_X // 5

# Menu
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 100

# Level selector
BUTTON_SPACING = 60
BUTTON_LENGTH = 100

DISASTER_SPEED = 0.5 # second
DISASTER_DURATION = 1 # second

ANIMATION_SPEED = 0.2

PANEL_WIDTH = 800
PANEL_HEIGHT = 400

NUMBER_LEVEL = 28

# COLOR CARD DOT
COLOR_SELECTED = (220,220,30)
COLOR_HOVER = (0,150,0)
COLOR_PRESS = (0,100,0)
COLOR_AVAILABLE = (0,255,0)
COLOR_NO_AVAILABLE = (255,0,0)

WATER_COLOR = (20,150,200)

TUTO_WIDTH = 600
TUTO_HEIGHT = int(TUTO_WIDTH*2/3)


SMALL_FONT = font.SysFont("Agency FB", 16)
NORMAL_FONT = font.SysFont("Agency FB", 26)
NORMAL_FONT_BOLD = font.SysFont("Agency FB", 30, True)
LARGE_FONT = font.SysFont("Agency FB", 46)
ULTRA_THICC_FONT = font.SysFont("Agency FB", 66, True)
