import pygame


class UI:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        if image == "keys":
            self.image = pygame.image.load("wasd.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        elif image == "health":
            self.image = pygame.image.load("health.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 0.25, self.image_size[1] * 0.25)
        elif image == "end":
            self.image = pygame.image.load("game_over.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 3, self.image_size[1] * 2.5)
        elif image == "collision":
            self.image = pygame.image.load("collision.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 0.25, self.image_size[1] * 0.25)
        else:
            self.image = pygame.image.load("dune.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 2.25, self.image_size[1] * 2.85)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])