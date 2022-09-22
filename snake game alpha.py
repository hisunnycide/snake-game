from cgitb import text
from contextlib import redirect_stderr
from string import whitespace
import pygame
import random
import os

x = pygame.init()
#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
#creating window
screen_W = 900
screen_H = 600
gameWindow = pygame.display.set_mode((screen_W,screen_H))
pygame.display.set_caption('My Game')
# print(os.listdir())



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def s_screen(text, color, x, y):
    s_screen = font.render(text, True, color)
    gameWindow.blit(s_screen, [x, y])  #pygame func updates screen

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        s_screen('welcome to snake', black, 260, 250)
        s_screen('Press Space to Play', black, 245, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                      gameloop()   
        pygame.display.update()
        clock.tick(60)
#creating a game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    init_velocity = 3
    food_x = random.randint(20 , screen_W/2) 
    food_y = random.randint(20 , screen_H/2) 
    score = 0
    fps = 60 
    snk_list = []
    snk_length = 1
    flag = 0
    if not os.path.exists('hiscore.txt'):
        with open('hiscore.txt', 'w') as f:
            f.write('0')
    with open ('hiscore.txt', 'r') as f:
             hiscore = f.read()
    while not exit_game:
        if snake_x <= 0:
            snake_x = 900
        elif snake_x >= 900:
            snake_x = 0
            
        if snake_y <= 0:
            snake_y = 600 
        elif snake_y >= 600:
            snake_y = 0
        if game_over:
            with open ('hiscore.txt', 'w') as f:
               f.write(str(hiscore))
            gameWindow.fill(white)
            s_screen('game over! press enter to continue', red, 100, 250)
            
            for event in pygame.event.get(): #tells input
                if event.type == pygame.QUIT:   
                    exit_game = True
                if event.type ==   pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()  
        else:
            for event in pygame.event.get(): #tells input
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN: #tells the program that a ket is pressed
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                if event.type == pygame.KEYDOWN: #tells the program that a ket is pressed
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity  
                        velocity_y = 0
                if event.type == pygame.KEYDOWN: #tells the program that a ket is pressed
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                if event.type == pygame.KEYDOWN: #tells the program that a ket is pressed
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity 
                        velocity_x = 0 
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if flag == 0:
                if abs(snake_x - food_x) < 80 and abs(snake_y - food_y) < 50:
                    food_x = random.randint(20, screen_W/1.5)
                    food_y = random.randint(20, screen_H/1.5)
                    flag += 1
                    # print(flag)
                    # print("hello")

            elif flag == 1:
                if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                    food_x = random.randint(20, screen_W/1.5)
                    food_y = random.randint(20, screen_H/1.5)
                    score += 1
                    if init_velocity != 6:
                        init_velocity += 1
                    snk_length += 3
                    flag -= 1
                    # print(flag, "hello")

            gameWindow.fill(black) 
            s_screen('score: '+ str(score) + '  highscore: '+ str(hiscore), red,5 ,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append (head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True
            # if snake_x<0 or snake_x>screen_W or snake_y<0 or snake_y>screen_H:
            #     game_over = True
                
            
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, white, snk_list, snake_size) 
        pygame.display.update()   
        clock.tick(fps)
    
        
    pygame.quit()
    quit()

welcome()