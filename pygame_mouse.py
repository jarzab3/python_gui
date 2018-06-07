import pygame
from pygame import *
import sys, random, math, fractions
from time import sleep

pygame.init()

infoObject = pygame.display.Info()

Screen_Width, Screen_Height = infoObject.current_w, infoObject.current_h

print("Screen width: %s screen height: %s" %(Screen_Width, Screen_Height ))

screen = pygame.display.set_mode((Screen_Width, Screen_Height))

white = (255, 255, 255)

blue = (0, 0, 255)

clock = pygame.time.Clock()

running = True

red = (255,0,0)

screen.fill(white)

while running:

    clock.tick(60)

    pygame.draw.rect(screen, red, (20, 20, (Screen_Width - 45), (Screen_Height - 120)), 3)

    pygame.display.update()

    event = pygame.event.wait()

    if event.type == QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEBUTTONUP:

        Mouse_x, Mouse_y = pygame.mouse.get_pos()

        pygame.draw.circle(screen, red, (Mouse_x, Mouse_y), 5, 4)

        pygame.display.update()

        print(Mouse_x, Mouse_y)
