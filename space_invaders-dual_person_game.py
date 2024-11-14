import pygame
from pygame.locals import *
import os

from pygame.sprite import Group
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
MAX_BULLETS = 3

# TRANSFORM AND SCALE:
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Lesson_6', 'space.png')), (WIDTH, HEIGHT))
# health
red_health = 100
yellow_health = 100

class Spaceship(pygame.sprite.Sprite):
    # properties/counstructor
    def __init__(self,image,angle,x,y):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(image,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),angle)
        self.rect=self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y


    # functions
    def move_horizontol(self,v,player):
        self.rect.x += v
        if player == 1:
            if self.rect.left<=0 or self.rect.right>= BORDER.left:
                self.rect.move_ip(-v,0)
        if player == 2:
            if self.rect.left<=BORDER.right or self.rect.right>= WIDTH:
                self.rect.move_ip(-v,0)

    def move_vertical(self,v):
        self.rect.move_ip(0,v)
        if self.rect.top<=0 or self .rect.bottom>=HEIGHT:
            self.rect.move_ip(0,-v)

# objects/instances
red = Spaceship(RED_SPACESHIP_IMAGE,270,670,220)        
yellow = Spaceship(YELLOW_SPACESHIP_IMAGE,90,20,220)
sprites = pygame.sprite.Group()
sprites.add(red)
sprites.add(yellow)

# draw window
def draw_window():
        WIN.blit(SPACE, (0, 0))
        pygame.draw.rect(WIN, BLACK, BORDER)
        red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
        yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
        WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        WIN.blit(yellow_health_text, (10, 10))

def draw_bullets():
        for bullet in red_bullets:
            pygame.draw.rect(WIN, RED, bullet)
            bullet.x -= BULLET_VEL
            
        for bullet in yellow_bullets:
            pygame.draw.rect(WIN, YELLOW, bullet)
            bullet.x += BULLET_VEL
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#def handle_bullets():
     

        


