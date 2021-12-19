#######################################################################
# Richard Castro                                                    ###
# November 2021                                                     ###
# Snake game built with PyGame library                              ###
# I had to learn pygame to build the Conway's game of life          ###
# and now I am just creating a few games with what I learned        ###
# before I literally forget it all.                                 ###
#######################################################################


###########################
##  FUTURE UPGRADES:     ##
##  1. POISON FRUIT      ##
##  2. OBSTICLES         ##
##  3. PAUSE SCREEN      ##
##  4. SNAKE LIVES       ##
##  5. TOP SCORE CHART   ##
##  6. SOUND EFFECTS     ##
##  7. GAME MODES        ##
###########################

# obsticle size
# snake head => obsticle location and <=osticle location +obsticle size

# IMPORT LIBRARIES
import pygame, sys, os
from elements import *
pygame.init()
clock=pygame.time.Clock()
game_font=pygame.font.Font('fonts/cotton.ttf', 24)
GAME_FONT=pygame.font.SysFont("Britannic Bold", 40)
munch_sound=pygame.mixer.Sound("assets/munch.wav")
game_speed=150
# This will be for the game modes
Easy=200
Medium=150
Hard=110
score_multiplier=10
# This needs to grab a csv file and display the top score
top_score="3200"

# GAME CLASS
class RULES:
    def __init__(self):
        self.fruit=FRUIT()
        self.snake=SNAKE()
        self.obsticle=OBSTICLES()
        self.obsticle2=OBSTICLES()


    def update(self):
        self.snake.move_snake()
        self.snackTime()
        self.check_fail()

    def draw_elements(self):
            self.grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.obsticle.draw_obs(Crate)
            self.obsticle2.draw_obs(Crate)
            self.score()

    def snackTime(self):
        if self.fruit.pos == self.snake.body[0]:
            # RANDONLY PICK FRUIT OR POISON
            pygame.mixer.Sound.play(munch_sound)
            self.fruit.randomize()
            # self.obsticle.randomize()
            self.snake.grow()

    def score(self):
        score_text= str(len(self.snake.body)-3)
        score_display=game_font.render(score_text, True, (200,40,40))
        score_x=int(cell_size*cell_number-100)
        score_y=int(cell_size*cell_number-100)
        score_rect=score_display.get_rect(center=(score_x, score_y))
        gameScreen.blit(score_display, score_rect)

    def check_fail(self):
        if not 0<=self.snake.body[0].x < cell_number or not 0<=self.snake.body[0].y< cell_number:
            self.snake.game_over()
        if self.snake.body[0] == self.obsticle.pos:
            pygame.quit()

        if self.snake.body[0] == self.obsticle2.pos:
            pygame.quit()

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


def home_screen():
    # PERGAME SCREEN LOOP
        pygame.mixer.music.load("assets/snake_intro.wav")
        pygame.mixer.music.play(-1)
        START_BG=pygame.image.load('assets/snake_bg.jpg')
        START_BUT=BUTTON((0,255,0), 320,380,175,50, "Start Game")
        QUIT_BUT=BUTTON((0,255,0), 320,460,175,50,"Quit Game")
        TOP_SCORE=BUTTON((255,0,0), 10, 10, 175, 50, "3200 pts")
        # START_BUTTON=GAME_FONT.render("Start Game", True, (255, 255, 255))
        # QUIT_BUTTON=GAME_FONT.render("Quit Game", True, (255,255,255))
        start_game=False
        while (start_game==False):
            gameScreen.blit(START_BG,(0,0))
            START_BUT.draw(gameScreen)
            QUIT_BUT.draw(gameScreen)
            TOP_SCORE.draw(gameScreen)
            # gameScreen.blit(START_BUTTON,(120,650))
            # gameScreen.blit(QUIT_BUTTON,(120,700))
            pygame.display.flip()
            for event in pygame.event.get():
                pos=pygame.mouse.get_pos()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if START_BUT.isOver(pos):
                        start_game=True
                    if QUIT_BUT.isOver(pos):
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()



def game_run():

        main_game=RULES()
        pygame.mixer.music.stop()
        screenUpdate=pygame.USEREVENT
        pygame.time.set_timer(screenUpdate, game_speed)
    # GAME LOOP
        while True:
            # User input and game controls
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==screenUpdate:
                    main_game.update()
                if event.type==pygame.KEYDOWN or event.type==pygame.KEYUP:
                    if event.key==pygame.K_UP:
                        if main_game.snake.direction.y !=1:
                            main_game.snake.direction=Vector2(0,-1)
                    if event.key==pygame.K_DOWN:
                        if main_game.snake.direction.y !=-1:
                            main_game.snake.direction=Vector2(0,1)
                    if event.key==pygame.K_RIGHT:
                        if main_game.snake.direction.x !=-1:
                            main_game.snake.direction=Vector2(1,0)
                    if event.key==pygame.K_LEFT:
                        if main_game.snake.direction.x !=1:
                            main_game.snake.direction=Vector2(-1,0)
            gameScreen.fill((150,200,60))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(fps)





# Initialize the game

# Main Game Loop,
def main():
    home_screen()
    game_run()

if __name__ == "__main__":
    main()
