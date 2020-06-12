import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Smiley Pong")
keepGoing = True
#pic = pygame.image.load("crazy-smile.jpg")
BLACK = (0,0,0)
WHITE = (255, 255, 255)
timer = pygame.time.Clock()
sprite_list = pygame.sprite.Group()
points = 0
lives = 3
font = pygame.font.SysFont("Times", 24)

def drawString(dstring):
  text = font.render(dstring, True, WHITE)
  text_rect = text.get_rect()
  text_rect.centerx = screen.get_rect().centerx
  text_rect.y = 10
  screen.blit(text, text_rect)
  pygame.display.update()

draw_string = "Lives: " + str(lives) + " Points: " + str(points)
drawString(draw_string)