import pygame


class Car:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color == "red":
            self.image = pygame.image.load("car.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .6, self.image_size[1] * .6)
        if color == "blue":
            self.image = pygame.image.load("blue_car.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)

        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
