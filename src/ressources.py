import pygame.image as img
from pygame.transform import scale
import os

def import_button(file,prout):
    return scale(img.load(os.path.join("res","button",f"{file}.png")),prout)

def import_background(file):
    return img.load(os.path.join("res","bckg",f"{file}.png"))