import tkinter

import pygame
from pygame.locals import*
import sys
import random
from tkinter import filedialog
from tkinter import*

vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
AAC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Heroes Adventure")

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
while True:

    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
              pass
