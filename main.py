import pygame
import random
import time

from car import Car
from dust import Dust
from rock import Rock
from ui import UI

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Georgia', 40)
pygame.display.set_caption("Finishline")

# set up variables for the display
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

hit_time = time.time()
bot_hit_time = time.time()

going_forward = False
bot_forward = True
colliding = False
bot_colliding = False
set_back = False
bot_set_back = False
going_left = False
going_right = False
begin = False

score = 0
score_count = "Score: " + str(score)
message = "Finishline"
message2 = "Press 'W' to begin"

display_score = my_font.render(score_count, True, (255, 255, 255))
my_font = pygame.font.SysFont('Comic Sans', 65)
display_message = my_font.render(message, True, (255, 255, 255))
display_message2 = my_font.render(message2, True, (255, 255, 255))
my_font = pygame.font.SysFont('Georgia', 40)
end_game = False

# Instantiate the images
car = Car(700, 600, "red")
bot_car = Car(700, 610, "blue")
d = Dust(700, 600)
wasd = UI(800, 400, "wasd")
game_map = UI(0, 0, "dune")
game_over = UI(0, 0, "end")
health_bar = UI(0, 800, "health")
health_pos = 225

rand_shift = random.randint(-200, 200)
rand_shift2 = random.randint(-200, 200)

rock = Rock(random.randint(0, 1440), -250 - random.randint(0, 300), 1)
rock2 = Rock(random.randint(0, 1440), -250 - random.randint(-75, 75), 1)
rock3 = Rock(random.randint(0, 1440), -250 - random.randint(0, 300), 2)
rock4 = Rock(random.randint(0, 1440), -250 - random.randint(0, 300), 2)

collision = UI(car.x, car.y, "collision")

rock2.change_size(1.25)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
while run:
    clock.tick(90)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        begin = True
        going_forward = True
    else:
        going_forward = False

    if keys[pygame.K_a]:
        going_left = True
    else:
        going_left = False

    if keys[pygame.K_d]:
        going_right = True
    else:
        going_right = False

    if (car.rect.colliderect(rock.rect) or car.rect.colliderect(rock2.rect) or car.rect.colliderect(rock3.rect) or car.rect.colliderect(rock4.rect)) and colliding is False:
        rand_shift3 = random.randint(-50, 50)
        rand_shift4 = random.randint(-25, 165)
        health_pos -= 15

        hit_time = time.time()
        colliding = True
        set_back = True
        going_forward = False
    elif not car.rect.colliderect(rock.rect) and not car.rect.colliderect(rock2.rect) and not car.rect.colliderect(rock3.rect) and not car.rect.colliderect(rock4.rect) and colliding is True:
        colliding = False

    if (bot_car.rect.colliderect(rock.rect) or bot_car.rect.colliderect(rock2.rect) or bot_car.rect.colliderect(
            rock3.rect) or bot_car.rect.colliderect(rock4.rect)) and bot_colliding is False:
        bot_hit_time = time.time()
        bot_colliding = True
        bot_set_back = True
        bot_forward = False
    elif not bot_car.rect.colliderect(rock.rect) and not bot_car.rect.colliderect(rock2.rect) and not bot_car.rect.colliderect(rock3.rect) and not bot_car.rect.colliderect(rock4.rect) and bot_colliding is True:
        bot_colliding = False

    # --- Main event loop
    # ----- NO BLIT ZONE START ----- #
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    #  ----- NO BLIT ZONE END  ----- #
    score_count = "Score: " + str(score)
    display_score = my_font.render(score_count, True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(game_map.image, (game_map.x, game_map.y))
    screen.blit(rock.image, (rock.x, rock.y))
    screen.blit(rock2.image, (rock2.x, rock2.y))
    screen.blit(rock3.image, (rock3.x, rock3.y))
    screen.blit(rock4.image, (rock4.x, rock4.y))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(45, 85, health_pos, 35))
    screen.blit(health_bar.image, (0, 0))
    screen.blit(display_score, (15, 15))

    screen.blit(bot_car.image, (bot_car.x, bot_car.y))
    screen.blit(car.image, (car.x, car.y))
    if colliding:
        screen.blit(collision.image, (car.x + rand_shift3, car.y + rand_shift4))

    updated_time = time.time()
    if colliding is False:
        if (hit_time - updated_time) < -0.25:
            set_back = False
    if set_back is True:
        rock.move(rock.x, rock.y - 14)
        rock2.move(rock2.x, rock2.y - 14)
        rock3.move(rock3.x, rock3.y - 14)
        rock4.move(rock4.x, rock4.y - 14)
        bot_car.y -= 8

    if bot_colliding is False:
        if (bot_hit_time - updated_time) < -0.2:
            bot_set_back = False
            bot_forward = True
    if bot_set_back is True:
        bot_car.y += 15

    if begin is True:
        
        if going_forward:
            if bot_car.y < car.y and bot_forward:
                bot_car.y += .1
            if bot_car.y > car.y and bot_forward:
                score += 1
                bot_car.y -= .6

            screen.blit(d.image, (car.x + 120 + random.randint(0, 20), car.y + 265 + random.randint(0, 20)))
            screen.blit(d.image, (car.x + random.randint(0, 20), car.y + 265 + random.randint(0, 20)))
            screen.blit(d.image, (car.x, car.y + 265 + random.randint(0, 20)))
            rock.move(rock.x, rock.y + 10)
            rock2.move(rock2.x, rock2.y + 10)
            rock3.move(rock3.x, rock3.y + 10)
            rock4.move(rock4.x, rock4.y + 10)
            if rock.y > 1600:
                rock.move(random.randint(0, 1440), -250 - random.randint(-50, 700))
            if rock2.y > 1600:
                rock2.move(random.randint(0, 1440), -250 - random.randint(-50, 700))
            if rock3.y > 1600:
                rock3.move(random.randint(0, 1440), -250 - random.randint(-50, 700))
            if rock4.y > 1600:
                rock4.move(random.randint(0, 1440), -250 - random.randint(-50, 700))
        else:
            bot_car.y -= 10

        if bot_car.y < -400:
            bot_car.y += 20
        if bot_car.y > 1200:
            bot_car.y -= 20

        if going_left and going_forward and car.x > 0:
            car.move(car.x - 8, car.y)
        if going_right and going_forward and car.x < 1445:
            car.move(car.x + 8, car.y)
    else:
        screen.blit(display_message, (635, 160))
        screen.blit(display_message2, (1200, 425))
        screen.blit(wasd.image, (1000, 350))

    if health_pos < 0:
        end_game = True

    if end_game is True:
        screen.blit(game_over.image, (0, 0))

    pygame.display.update()
    # END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
