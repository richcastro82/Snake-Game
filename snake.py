# Richard Castro
# November 2021
# Snake game built with PyGame library
# I had to learn pygame to build the Conway's game of life
# and now I am just creating a few games with what I learned
# before I literally forget it all.

import pygame, sys, os, random
from pygame.math import Vector2
cell_size=40
cell_number=20
fps=30
clock=pygame.time.Clock()

class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(gameScreen,(0,0,0), fruit_rect)


class SNAKE:
    def __init__(self):
        self.body=[Vector2(4,4),Vector2(5,4),Vector2(6,4)]
        self.direction=Vector2(1,0)
    def draw_snake(self):
        for block in self.body:
            snake_rect=pygame.Rect(block.x*cell_size, block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(gameScreen, (8,8,8), snake_rect)



pygame.init()
gameScreen=pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

fruit=FRUIT()
snake=SNAKE()
# main game loop
screenUpdate=pygame.USEREVENT
pygame.time.set_timer(screenUpdate, 150)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


    gameScreen.fill((120,120,120))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(fps)
