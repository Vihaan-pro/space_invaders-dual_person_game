import pygame
from pygame.locals import *
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACE INVADERS")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

#load sounds
BULLET_HIT_SOUND =pygame.mixer.Sound("lesson_6/Grenade+1.mp3")
BULLET_FIRE_SOUND =pygame.mixer.Sound("lesson_6/Gun+Silencer.mp3")

#load fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

#load images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Lesson_6', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Lesson_6', 'spaceship_red.png'))

FPS = 60
VEL = 5
BULLET_VEL = 12
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

# TRANSFORM AND SCALE:
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Lesson_6', 'space.png')), (WIDTH, HEIGHT))
# health
red_health = 100
yellow_health = 100
