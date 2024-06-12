import pygame


class Rock:

    def __init__(self, x, y, variation):
        self.x = x
        self.y = y
        if variation == 1:
            self.image = pygame.image.load("rock.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        else:
            self.image = pygame.image.load("rock2.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .8, self.image_size[1] * .8)

        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def change_size(self, sf):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * sf, self.image_size[1] * sf)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
