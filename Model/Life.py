import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, settings):
        life = pygame.image.load(settings.life)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(life, settings.life_ratio)
        self.rect = pygame.Rect(settings.life_starting_pos_x, settings.char_starting_pos_y)


