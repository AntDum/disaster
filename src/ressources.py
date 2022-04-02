import pygame.image as img
from pygame.transform import scale
from option import *
import os

def import_button(file,prout):
    return scale(img.load(os.path.join("res","button",f"{file}.png")),prout)

def import_background(file):
    return img.load(os.path.join("res","bckg",f"{file}.png"))

def import_tile(file):
    return scale(img.load(os.path.join("res","tiles",f"{file}.png")),(TILE_SIZE,TILE_SIZE))

def import_disaster(file):
    return scale(img.load(os.path.join("res","disaster",f"{file}.png")),(TILE_SIZE,TILE_SIZE))

def import_card(file):
    return scale(img.load(os.path.join("res","card",f"{file}.png")),(CARD_WIDTH,CARD_HEIGHT))