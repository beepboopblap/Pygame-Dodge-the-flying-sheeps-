import pygame, random
from pygame.locals import *
from pygame import mixer
import math


SCREEN_HEIGHT = 900
SCREEN_WIDTH = 690


pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# declare colours, images, sounds, fonts
x = 690
y = 900
player_x = 240
player_y = 680
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
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
start_text = Calibri60.render("Press a key to begin!", 1, red)
lives = 3
collision_sfx = mixer.Sound("spacebar_soundfx.mp3")
hurt_sfx = mixer.Sound("hurt_sfx (mp3cut.net).mp3")
game_over_text = Calibri60.render("Game Over", 1, red)


start = True
running = True
in_game = False
quit = False
gameover = False
player_x = 240
player_y = 680


# transformations

player_sprite = pygame.transform.scale(player_sprite, (140, 140))
sheep_sprite = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite1 = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite2 = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite3 = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite4 = pygame.transform.scale(sheep_sprite, (140, 140))

all_sprites = [
    player_sprite,
    sheep_sprite,
    sheep_sprite1,
    sheep_sprite2,
    sheep_sprite3,
    sheep_sprite4,
]


# variables for keeping track of my game players etc.

# collision code
def isCollision(sheep_x, sheep_y, player_x, player_y):
    distance = math.sqrt(
        (math.pow(player_x - sheep_x, 2)) + (math.pow(player_y - sheep_y, 2))
    )
    if distance < 114:
        return True
    else:
        return False


def isCollision(sheep_x1, sheep_y1, player_x1, player_y1):
    distance = math.sqrt(
        (math.pow(player_x1 - sheep_x1, 2)) + (math.pow(player_y1 - sheep_y1, 2))
    )
    if distance < 114:
        return True
    else:
        return False


def isCollision(sheep_x2, sheep_y2, player_x2, player_y2):
    distance = math.sqrt(
        (math.pow(player_x2 - sheep_x2, 2)) + (math.pow(player_y2 - sheep_y2, 2))
    )
    if distance < 114:
        return True
    else:
        return False


def isCollision(sheep_x3, sheep_y3, player_x3, player_y3):
    distance = math.sqrt(
        (math.pow(player_x3 - sheep_x3, 2)) + (math.pow(player_y3 - sheep_y3, 2))
    )
    if distance < 114:
        return True
    else:
        return False


point = 0
start = True
game_over = False
score = 0

# main game loop
while running:

    if start == True:
        window.fill(yellow)

        if point == 0:
            start_text = Calibri60.render("Start", 1, red)
            exit_text = Calibri40.render("Exit", 1, black)
            main_menu = Calibri60.render("Main Menu", 1, blue)
            credits_text = Calibri40.render("Made by", 1, black)
            credits_name = Calibri60.render("beepboopblap", 1, red)
            window.blit(credits_text, (140, 730))
            window.blit(credits_name, (140, 780))

            window.blit(start_text, (290, 400))
            window.blit(exit_text, (290, 490))
            window.blit(main_menu, (170, 100))

        elif point == 1:
            start_text = Calibri40.render("Start", 1, black)
            exit_text = Calibri60.render("Exit", 1, red)
            window.blit(start_text, (290, 400))
            window.blit(exit_text, (290, 490))
            window.blit(main_menu, (170, 100))

            credits_text = Calibri40.render("Made by", 1, black)
            credits_name = Calibri60.render("beepboopblap", 1, red)
            window.blit(credits_text, (140, 730))
            window.blit(credits_name, (140, 780))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    point += 1
                    collision_sfx.play()
                elif event.key == K_UP:
                    point -= 1
                    collision_sfx.play()
                elif event.key == K_RETURN:
                    if point == 0:
                        start = False
                        game = True
                    elif point == 1:
                        pygame.quit()

        point = point % 2
        pygame.display.update()

    elif game_over == True:
        window.fill(yellow)
        window.blit(game_over_text, (190, 400))

        for event in pygame.event.get():
            if event.type == QUIT:

                pygame.quit()

            elif event.type == KEYUP:
                if event.key == ord("r"):
                    game_over == False
                    game == True

        pygame.display.update()

    elif game == True:

        # process events
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
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

        # perform calculations

        # code for borders
        if player_x >= 599:
            player_x = 599
        if player_x <= -35:
            player_x = -35
        if player_y >= 760:
            player_y = 760
        if player_y <= 0:
            player_y = 0

        # draw graphics
        window.fill(yellow)

        window.blit(player_sprite, (player_x, player_y))
        pygame.draw.rect(window, black, (3, 3, 683, 890), 4)
        watch_out_label = Calibri40.render("Watch out for flying sheep!", 1, blue)
        controls = Calibri40.render("Use WASD to move", 1, blue)
        window.blit(controls, (150, 300))
        window.blit(watch_out_label, (70, 200))
        lives_counter = Calibri40.render("Lives left:" + str(lives), 1, red)
        window.blit(lives_counter, (10, 60))
        score_text = Calibri40.render("Score:" + str(score), 1, red)
        window.blit(score_text, (10, 140))

        if lives <= 0:
            game = False
            game_over = True

        # sheep falling from the sky code

        if sheep_y < y:

            window.blit(sheep_sprite, (sheep_x, sheep_y))
            sheep_y = sheep_y + 20
            if sheep_y > 830:
                sheep_x = random.randrange(0, x)
                sheep_y = 0
                score = score + 1
                if score == 50:
                    lives = lives + 1
                elif score == 100:
                    lives = lives + 1
                elif score == 150:
                    lives = lives + 1
                elif score == 200:
                    lives = lives + 1
                elif score == 250:
                    lives = lives + 1
                elif score == 300:
                    lives = lives + 1

            # Collision for sheep
            collision = isCollision(sheep_x, sheep_y, player_x, player_y)

            if collision:
                sheep_y = 0
                sheep_x = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y1 < y:

            window.blit(sheep_sprite1, (sheep_x1, sheep_y1))
            sheep_y1 = sheep_y1 + 30
            if sheep_y1 > 830:
                sheep_x1 = random.randrange(0, 100)
                sheep_y1 = 0
                score = score + 1
                if score == 50:
                    lives = lives + 1
                elif score == 100:
                    lives = lives + 1
                elif score == 150:
                    lives = lives + 1
                elif score == 200:
                    lives = lives + 1
                elif score == 250:
                    lives = lives + 1
                elif score == 300:
                    lives = lives + 1

            collision = isCollision(sheep_x1, sheep_y1, player_x, player_y)

            if collision:
                sheep_y1 = 0
                sheep_x1 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y2 < y:

            window.blit(sheep_sprite2, (sheep_x2, sheep_y2))
            sheep_y2 = sheep_y2 + random.randint(20, 60)
            if sheep_y2 > 830:
                sheep_x2 = random.randrange(0, SCREEN_WIDTH)
                sheep_y2 = 0
                score = score + 1
                if score == 50:
                    lives = lives + 1
                elif score == 100:
                    lives = lives + 1
                elif score == 150:
                    lives = lives + 1
                elif score == 200:
                    lives = lives + 1
                elif score == 250:
                    lives = lives + 1
                elif score == 300:
                    lives = lives + 1

            collision = isCollision(sheep_x2, sheep_y2, player_x, player_y)

            if collision:
                sheep_y2 = 0
                sheep_x2 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

    pygame.display.update()
    fps.tick(11)

    # update

# loop over, game over
pygame.quit()
