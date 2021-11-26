# Richard Castro
# November 2021
# Snake game built with PyGame library
# I had to learn pygame to build the Conway's game of life
# and now I am just creating a few games with what I learned
# before I literally forget it all.

import pygame, sys, os, random
from pygame.math import Vector2

from elements import *
# Game class
class RULES:
    def __init__(self):
        self.fruit=FRUIT()
        self.snake=SNAKE()
    def update(self):
        self.snake.move_snake()
        self.snackTime()

        self.check_fail()
        # self.snake.check_fail()

    def draw_elements(self):
            self.grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.score()
    def snackTime(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randonize()
            self.snake.grow()
    def score(self):
        score_text= str(len(self.snake.body)-3)
        score_display=game_font.render(score_text, True, (200,40,40))
        score_x=int(cell_size*cell_number-100)
        score_y=int(cell_size*cell_number-100)
        score_rect=score_display.get_rect(center=(score_x, score_y))
        gameScreen.blit(score_display, score_rect)

    def check_fail(self):
        # 1. check if snake head has hit the border edge
        if not 0<=self.snake.body[0].x < cell_number or not 0<=self.snake.body[0].y< cell_number:
            pygame.quit()
        # 2. check if snake head has hit the snake body



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


# Initialize the game
pygame.init()
clock=pygame.time.Clock()
game_font=pygame.font.Font('fonts/cotton.ttf', 24)
screenUpdate=pygame.USEREVENT
pygame.time.set_timer(screenUpdate, 150)
main_game=RULES()
START_BG=pygame.image.load('Images/snake_bg.jpg')

def main():

    # Pregame Screen Loop
    start_game=False
    while (start_game==False):
        GAME_FONT=pygame.font.SysFont("Britannic Bold", 40)
        START_BUTTON=GAME_FONT.render("Start Game", True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    start_game=True
        gameScreen.blit(START_BG,(0,0))
        gameScreen.blit(START_BUTTON,(120,650))
        pygame.display.flip()
        # -------------------

    # game loop exits
    while True:
        gameScreen.fill((147,205,58))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(fps)

        # User input and game controls
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

if __name__ == "__main__":
    main()
