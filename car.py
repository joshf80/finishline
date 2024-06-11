import pygame

class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("car.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .6, self.image_size[1] * .6)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])