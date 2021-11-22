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


class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size,cell_size,cell_size)
        gameScreen.blit(apple,fruit_rect)
        # pygame.draw.rect(gameScreen,(0,0,0), fruit_rect)

    def randonize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body=[Vector2(4,4),Vector2(5,4),Vector2(6,4)]
        self.direction=Vector2(1,0)
        self.new_block=False
        self.head_up=pygame.image.load('image/head_up.png').convert_alpha()
        self.head_down=pygame.image.load('image/head_down.png').convert_alpha()
        self.head_left=pygame.image.load('image/head_left.png').convert_alpha()
        self.head_right=pygame.image.load('image/head_right.png').convert_alpha()
        self.tail_up=pygame.image.load('image/tail_up.png').convert_alpha()
        self.tail_down=pygame.image.load('image/tail_down.png').convert_alpha()
        self.tail_left=pygame.image.load('image/tail_left.png').convert_alpha()
        self.tail_right=pygame.image.load('image/tail_right.png').convert_alpha()
        self.body_vert=pygame.image.load('image/body_vertical.png').convert_alpha()
        self.body_hort=pygame.image.load('image/body_horizontal.png').convert_alpha()
        


    def draw_snake(self):
        for index, block in enumerate(self.body):





        # for block in self.body:
        #     snake_rect=pygame.Rect(block.x*cell_size, block.y*cell_size,cell_size,cell_size)
        #     pygame.draw.rect(gameScreen, (8,8,8), snake_rect)

    def move_snake(self):
        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body=body_copy[:]

    def grow(self):
        self.new_block=True

    # def check_fail(self):
    #     if not 0 <= self.body[0] <= 20:
    #         self.game_over()

    def game_over(self):
        pygame.quit()

class RULES:
    def __init__(self):
        self.fruit=FRUIT()
        self.snake=SNAKE()

    def update(self):
        self.snake.move_snake()
        self.snackTime()
        # self.snake.check_fail()

    def draw_elements(self):
            self.grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()

    def snackTime(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randonize()
            self.snake.grow()

    def grass(self):
        grass_color=(160,210,60)
        for row in range(cell_number):
            if row % 2==0:
                for col in range(cell_number):
                    if col % 2==0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(gameScreen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2!=0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(gameScreen,grass_color,grass_rect)


clock=pygame.time.Clock()
pygame.init()
gameScreen=pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
apple=pygame.image.load('images/apple.png').convert_alpha()
main_game=RULES()
screenUpdate=pygame.USEREVENT
pygame.time.set_timer(screenUpdate, 150)

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==screenUpdate:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN:
                main_game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_RIGHT:
                main_game.snake.direction=Vector2(1,0)
            if event.key==pygame.K_LEFT:
                main_game.snake.direction=Vector2(-1,0)


    gameScreen.fill((147,205,58))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(fps)
