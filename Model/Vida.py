import pygame

class Vida(pygame.sprite.Sprite):
    def __init__(self, settings):
        vida = pygame.image.load(settings.obj_vida)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(vida, settings.obj_vida_ratio)
        self.rect = pygame.Rect(settings.obj_vida_starting_pos_x, settings.char_starting_pos_y)


