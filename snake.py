# Richard Castro
# November 2021
# Snake game built with PyGame library
# I had to learn pygame to build the Conway's game of life
# and now I am just creating a few games with what I learned
# before I literally forget it all.

import pygame, sys, os
w=800
h=800
s=(w,h)
fps=30
clock=pygame.time.Clock()
pygame.init()
gameScreen=pygame.display.set_mode(s)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    gameScreen.fill((120,120,120))
    pygame.display.update()
    clock.tick(fps)
