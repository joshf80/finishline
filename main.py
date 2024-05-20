import pygame
import random
import time

from car import Car
from dust import Dust
from wasd import Wasd
from dune import Dune
from rock import Rock
from rock2 import Rock2
from collision import Collision

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 65)
pygame.display.set_caption("Finishline")

# set up variables for the display
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

hit_time = time.time()

going_forward = False
colliding = False
set_back = False
going_left = False
going_right = False
begin = False

message = "Finishline"
message2 = "Press 'W' to begin"
display_message = my_font.render(message, True, (255, 255, 255))
my_font = pygame.font.SysFont('Comic Sans', 25)
display_message2 = my_font.render(message2, True, (255, 255, 255))
health = 100

# Instantiate the images
car = Car(700, 600)
d = Dust(700, 600)
wasd = Wasd(800, 400)
game_map = Dune(0, 0)

rand_shift = random.randint(-200, 200)
rand_shift2 = random.randint(-200, 200)

rock = Rock(random.randint(0, 1440), -250)
rock2 = Rock(random.randint(0, 1440), -250 - random.randint(-75, 75))
rock3 = Rock2(random.randint(0, 1440), -250)
rock4 = Rock2(random.randint(0, 1440), -250 - random.randint(0, 300))

collision = Collision(car.x, car.y)

rock2.change_size(1.25)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
while run:
    clock.tick(90)
    # print(health)
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
        rand_shift4 = random.randint(-25, 240)
        health -= 7
        hit_time = time.time()
        colliding = True
        set_back = True
        going_forward = True
    elif not car.rect.colliderect(rock.rect) and not car.rect.colliderect(rock2.rect) and not car.rect.colliderect(rock3.rect) and not car.rect.colliderect(rock4.rect) and colliding is True:
        colliding = False

    # --- Main event loop
    # ----- NO BLIT ZONE START ----- #
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    #  ----- NO BLIT ZONE END  ----- #
    screen.fill((0, 0, 0))
    screen.blit(game_map.image, (game_map.x, game_map.y))
    screen.blit(rock.image, (rock.x, rock.y))
    screen.blit(rock2.image, (rock2.x, rock2.y))
    screen.blit(rock3.image, (rock3.x, rock3.y))
    screen.blit(rock4.image, (rock4.x, rock4.y))

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

    if begin is True:
        if going_forward:
            screen.blit(d.image, (car.x + 120 + random.randint(0, 20), car.y + 265 + random.randint(0, 20)))
            screen.blit(d.image, (car.x + random.randint(0, 20), car.y + 265 + random.randint(0, 20)))
            screen.blit(d.image, (car.x, car.y + 265 + random.randint(0, 20)))
            rock.move(rock.x, rock.y + 10)
            rock2.move(rock2.x, rock2.y + 10)
            rock3.move(rock3.x, rock3.y + 10)
            rock4.move(rock4.x, rock4.y + 10)
            if rock.y > 1500:
                rock = Rock(random.randint(0, 1440), -850)
                rock.change_size(random.randint(int(0.8), int(1.45)))
            if rock2.y > 1500:
                rock2 = Rock(random.randint(0, 1440), -650 - random.randint(-50, 50))
                rock2.change_size(random.randint(int(0.8), int(1.45)))
            if rock3.y > 1500:
                rock3 = Rock2(random.randint(0, 1440), -250)
                rock2.change_size(random.randint(int(0.8), int(1.45)))
            if rock4.y > 1500:
                rock4 = Rock2(random.randint(0, 1440), -450 - random.randint(-20, 300))
                rock4.change_size(random.randint(int(0.8), int(1.45)))
        if going_left and going_forward and car.x > 0:
            car.move(car.x - 6, car.y)
        if going_right and going_forward and car.x < 1445:
            car.move(car.x + 6, car.y)
    else:
        screen.blit(display_message, (635, 160))
        screen.blit(display_message2, (1200, 425))
        screen.blit(wasd.image, (1000, 350))

    pygame.display.update()
    # END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
