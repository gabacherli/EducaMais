import pygame

class Eraser(pygame.sprite.Sprite):
    def __init__(self, settings):
        eraser = pygame.image.load(settings.eraser)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(eraser, settings.eraser_ratio)
        self.rect = pygame.Rect(settings.eraser_starting_left_top, settings.aurelinho_starting_width_height)
        self.image = self.scale_image(settings.eraser, settings.eraser_ratio)
        self.velocidade_x = -2
        self.velocidade_y = 0
        self.gravidade = 0.03
        self.x = 0

    def update(self, settings):
        self.rect.centerx += self.velocidade_x

        if self.rect.x < 0 - settings.eraser_ratio[0]:
            self.rect.x  = settings.width

    def scale_image(self, image, escala_do_personagem):
        boy = pygame.image.load(image)
        return pygame.transform.scale(boy, escala_do_personagem)