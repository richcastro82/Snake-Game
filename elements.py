import pygame, sys, os, random
from pygame.math import Vector2
cell_size=40
cell_number=20
fps=30

gameScreen=pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
apple=pygame.image.load('assets/apple.png').convert_alpha()
poison=pygame.image.load('assets/poison.png').convert_alpha()
Crate=pygame.image.load("assets/Crate.png")
# Button Class
class BUTTON:
    def __init__(self, color, x, y, width, height, text=""):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
    def draw(self, gameScreen, outline=None):
        if outline:
            pygame.draw.rect(gameScreen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(gameScreen,(160,210,60), (self.x, self.y, self.width, self.height), 0)

        if self.text !="":
            font=pygame.font.SysFont('comicsans', 20)
            text=font.render(self.text, 1, (100,50,20))
            gameScreen.blit(text, (self.x+(self.width/2-text.get_width()/2), self.y+(self.height/2-text.get_height()/2) ))
    def isOver(self, pos):
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y+self.height:
                return True
        return False

# Fruit class
class FRUIT:
    # Initialize the class
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size,cell_size,cell_size)
        gameScreen.blit(apple,fruit_rect)

    def draw_poison(self):
        poison_rect=pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
        gameScreen.blit(poison, poison_rect)

    def randonize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x, self.y)

# Fruit class
class OBSTICLES:
    # Initialize the class
    def __init__(self):
        self.x=random.randint(0,cell_number-2)
        self.y=random.randint(0,cell_number-2)
        self.pos=Vector2(self.x, self.y)

    def draw_obs(self, obs_img):
        obsticle_rect=pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size,80,80)
        gameScreen.blit(obs_img,obsticle_rect)

    def randonize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x, self.y)

# Snake class
class SNAKE:
    # Initialize the class
    def __init__(self):
        self.body=[Vector2(4,4),Vector2(3,4),Vector2(2,4)]
        self.direction=Vector2(1,0)
        self.new_block=False
        self.head_up=pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down=pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_left=pygame.image.load('assets/head_left.png').convert_alpha()
        self.head_right=pygame.image.load('assets/head_right.png').convert_alpha()
        self.tail_up=pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down=pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_left=pygame.image.load('assets/tail_left.png').convert_alpha()
        self.tail_right=pygame.image.load('assets/tail_right.png').convert_alpha()
        self.body_vert=pygame.image.load('assets/body_vertical.png').convert_alpha()
        self.body_hori=pygame.image.load('assets/body_horizontal.png').convert_alpha()
        self.body_tr=pygame.image.load('assets/body_tr.png').convert_alpha()
        self.body_tl=pygame.image.load('assets/body_tl.png').convert_alpha()
        self.body_br=pygame.image.load('assets/body_br.png').convert_alpha()
        self.body_bl=pygame.image.load('assets/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_snake_head()
        self.update_snake_tail()

        for index, block in enumerate(self.body):
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos, y_pos, cell_size,cell_size)

            if index==0:
                gameScreen.blit(self.head, block_rect)
            elif index== len(self.body)-1:
                gameScreen.blit(self.tail, block_rect)
            else:
                previous_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if previous_block.x==next_block.x:
                    gameScreen.blit(self.body_vert, block_rect)
                elif previous_block.y==next_block.y:
                    gameScreen.blit(self.body_hori, block_rect)
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        gameScreen.blit(self.body_tl, block_rect)
                    elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                        gameScreen.blit(self.body_bl, block_rect)
                    elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        gameScreen.blit(self.body_tr, block_rect)
                    elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                        gameScreen.blit(self.body_br, block_rect)

    def update_snake_head(self):
        head_position=self.body[1]-self.body[0]
        if head_position==Vector2(1,0):self.head=self.head_left
        elif head_position==Vector2(-1,0):self.head=self.head_right
        elif head_position==Vector2(0,1):self.head=self.head_up
        elif head_position==Vector2(0,-1):self.head=self.head_down

    def update_snake_tail(self):
        tail_position=self.body[-2]-self.body[-1]
        if tail_position==Vector2(1,0):self.tail=self.tail_left
        elif tail_position==Vector2(-1,0):self.tail=self.tail_right
        elif tail_position==Vector2(0,1):self.tail=self.tail_up
        elif tail_position==Vector2(0,-1):self.tail=self.tail_down
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

    def game_over(self):
        pygame.quit()
