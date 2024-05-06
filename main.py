import pygame

from car import Car
from dust import Dust

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 16)
pygame.display.set_caption("Finishline")

# set up variables for the display
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

going_forward = False
going_left = False
going_right = False

message = "Finishline"
display_message = my_font.render(message, True, (255, 255, 255))

# Instantiate the images
car = Car(700, 600)
d = Dust(700, 600)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
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

    # --- Main event loop
    # ----- NO BLIT ZONE START ----- #
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    #  ----- NO BLIT ZONE END  ----- #
    screen.fill((0, 0, 0))
    if going_forward is True:
        screen.blit(d.image, (car.x + 120, car.y + 269))

    screen.blit(display_message, (180, 160))
    screen.blit(car.image, (car.x, car.y))

    pygame.display.update()
    # END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
