import pygame

class Boy(pygame.sprite.Sprite):
    def __init__(self, settings):
        boy = pygame.image.load(settings.char_right)
        pygame.sprite.Sprite.__init__(self)

        self.vl_x = 0
        self.vl_y = 0
        self.image = pygame.transform.scale(boy, settings.char_ratio)
        self.rect = pygame.Rect(settings.char_starting_pos_x, settings.char_starting_pos_y)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0.009

    def mover_para_esquerda(self, settings):
        self.image = self.scale_image(settings.char_left, settings.char_ratio)
        self.velocidade_x = -1

    def mover_para_direita(self, settings):
        self.image = self.scale_image(settings.char_right, settings.char_ratio)
        self.velocidade_x = 1
        self.vl_x = 1
        self.vl_y = 1

    def pular(self):
        self.velocidade_y = -5

    def update(self):
        self.rect.centerx += self.velocidade_x
        # gravidade do Y
        self.velocidade_y += self.gravidade
        self.rect.centery += self.velocidade_y
        self.vl_x += self.vl_x
        self.vl_y += self.vl_y

    def parar_movimento_horizontal(self):
        self.velocidade_x = 0

    def parar_movimento_vertical(self):
        self.velocidade_y = 0

    def scale_image(self, image, escala_do_personagem):
        boy = pygame.image.load(image)
        return pygame.transform.scale(boy, escala_do_personagem)
