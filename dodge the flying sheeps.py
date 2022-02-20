from curses.ascii import ESC
import pygame, random 
from pygame.locals import * 
from pygame import mixer

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((690,900))

#declare colours, images, sounds, fonts
x = 240
y = 680
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
Calibri60 = pygame.font.SysFont("Calibri", 60)
player_sprite = pygame.image.load("player_sprite.png").convert_alpha()
sheep_sprite = pygame.image.load("sheep_sprite.png").convert_alpha()
sheep_speed = -5
sheep_y = -50
sheep_x = random.randrange(0,x)

#transformations

player_sprite = pygame.transform.scale(player_sprite, (140,140))

#variables for keeping track of my game players etc.

quit = False

x = 240
y = 680
space = False
space_counter = 0
movex = 0
movey = 0

#main game loop
while  not quit:

    #process events
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            quit = True
        elif event.type == KEYDOWN:
            if event.key == ord("w"):
                y = y - 40
            if event.key == ord("s"):
                y = y + 40
            if event.key == ord("a"):
                x = x - 40
            if event.key == ord("d"):
                x = x + 40
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
            
    

    #perform calculations
   

    #draw graphics
    window.fill(yellow)
    
    window.blit(player_sprite, (x,y))
    sheep_y = sheep_y + sheep_speed
    if sheep_y > y:
        
        sheep_x = random.randrange(0,x)
        sheep_y = -25
        window.blit(sheep_sprite, (sheep_x, sheep_y))
    #update
    pygame.display.update()
    fps.tick(25)

#loop over, game over
pygame.quit()


