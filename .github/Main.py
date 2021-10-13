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
