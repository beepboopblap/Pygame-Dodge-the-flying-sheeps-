from turtle import window_width
import pygame, random 
from pygame.locals import * 
from pygame import mixer
import math


SCREEN_HEIGHT = 900
SCREEN_WIDTH = 690

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#declare colours, images, sounds, fonts
x = 690
y = 900
player_x = 240
player_y = 680
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
Calibri60 = pygame.font.SysFont("Calibri", 60)
Calibri40 = pygame.font.SysFont("Calibri", 40)
player_sprite = pygame.image.load("player_sprite.png").convert_alpha()
sheep_sprite = pygame.image.load("sheep_sprite.png").convert_alpha()
sheep_speed = -5
sheep_x = 104
sheep_x1 = 40
sheep_x2 = 13
sheep_x3 = 79
sheep_y = -17
sheep_y1 = -10
sheep_y2 = -4
sheep_y3 = -7
start_text = Calibri60.render("Press a key to begin!",1, red )



#transformations

player_sprite = pygame.transform.scale(player_sprite, (140,140))
sheep_sprite = pygame.transform.scale(sheep_sprite, (140,140))
sheep_sprite1 = pygame.transform.scale(sheep_sprite, (140,140))
sheep_sprite2 = pygame.transform.scale(sheep_sprite, (140,140))
sheep_sprite3 = pygame.transform.scale(sheep_sprite, (140,140))
sheep_sprite4 = pygame.transform.scale(sheep_sprite, (140,140))

#variables for keeping track of my game players etc.
def isCollision(sheep_x, sheep_y, player_x, player_y):
    distance = math.sqrt((math.pow(player_x-sheep_x, 2)) + (math.pow(player_y - sheep_y, 2)))
    if distance < 120:
        return True
    else: 
        return False
def isCollision(sheep_x1, sheep_y1, player_x1, player_y1):
    distance = math.sqrt((math.pow(player_x1-sheep_x1, 2)) + (math.pow(player_y1 - sheep_y1, 2)))
    if distance < 120:
        return True
    else: 
        return False
def isCollision(sheep_x2, sheep_y2, player_x2, player_y2):
    distance = math.sqrt((math.pow(player_x2-sheep_x2, 2)) + (math.pow(player_y2 - sheep_y2, 2)))
    if distance < 120:
        return True
    else: 
        return False
def isCollision(sheep_x3, sheep_y3, player_x3, player_y3):
    distance = math.sqrt((math.pow(player_x3-sheep_x3, 2)) + (math.pow(player_y3 - sheep_y3, 2)))
    if distance < 120:
        return True
    else: 
        return False




quit = False
game_over =  True
player_x = 240
player_y = 680


#main game loop
while  not quit:
    
        
       
        #process events
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                quit = True
            elif event.type == KEYDOWN:
                if event.key == ord("w"):
                    player_y = player_y - 40
                if event.key == ord("s"):
                    player_y = player_y + 40
                if event.key == ord("a"):
                    player_x = player_x - 40
                if event.key == ord("d"):
                    player_x = player_x + 40
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()

    

    #perform calculations
        if player_x >= 599:
            player_x = 599
        if player_x <= -35:
            player_x = -35
        if player_y >= 760:
            player_y = 760
        if player_y <= 0:
            player_y = 0

        #draw graphics
        window.fill(yellow)

        window.blit(player_sprite, (player_x,player_y))
        pygame.draw.rect(window, black, (3,3 ,683, 890), 4)
        watch_out_label = Calibri40.render("Watch out for flying sheep!", 1, red)
        controls = Calibri40.render("Use WASD to move", 1, red)
        window.blit(controls, (150, 300))
        window.blit(watch_out_label, (70, 200))
    
        if sheep_y < y:

            window.blit(sheep_sprite, (sheep_x, sheep_y))
            sheep_y = sheep_y + 20
            if sheep_y > 830:
                sheep_x = random.randrange(0,x)
                sheep_y = 0

        #Collision for sheep
            collision = isCollision(sheep_x, sheep_y, player_x, player_y)

            if collision: 
                sheep_y = 0
                sheep_x = random.randrange(0,x)







        if sheep_y1 < y:

            window.blit(sheep_sprite1, (sheep_x1, sheep_y1))
            sheep_y1 = sheep_y1 + 30
            if sheep_y1 > 830:
                sheep_x1 = random.randrange(0,100)
                sheep_y1 = 0

            collision = isCollision(sheep_x1, sheep_y1, player_x, player_y)

            if collision: 
                sheep_y1 = 0
                sheep_x1 = random.randrange(0,x)

        if sheep_y2 < y:

            window.blit(sheep_sprite2, (sheep_x2, sheep_y2))
            sheep_y2 = sheep_y2 + random.randint(20,60)
            if sheep_y2 > 830:   
                sheep_x2 = random.randrange(0,SCREEN_WIDTH)
                sheep_y2 = 0

            collision = isCollision(sheep_x2, sheep_y2, player_x, player_y)

            if collision: 
                sheep_y2 = 0
                sheep_x2 = random.randrange(0,x)
        
    #update
        pygame.display.update()
        fps.tick(9)       
#loop over, game over
pygame.quit()


