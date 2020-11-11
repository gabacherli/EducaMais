import pygame


class Boy(pygame.sprite.Sprite):
    def __init__(self):
        init_character = pygame.image.load("Misc/Images/Characters/looking_right.png")
        pygame.sprite.Sprite.__init__(self)
        self.vl_x = 1
        self.vl_y = 3
        boy = init_character
        print(self.vl_x, self.vl_y)
        self.image = pygame.transform.scale(boy, (85, 155))
        self.rect = pygame.Rect((10, 240), (85, 155))
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0.009

    def move_esquerda(self):
        self.image = self.scale_image("Misc/Images/Characters/looking_left.png")
        self.velocidade_x = -1

    def move_direita(self):
        self.image = self.scale_image("Misc/Images/Characters/looking_right.png")
        self.velocidade_x = 1
        self.vl_x = 1
        self.vl_y = 1

    def pular(self):
        self.velocidade_y = -5

    def update(self, *args):
        self.rect.centerx += self.velocidade_x
        # gravidade do Y
        self.velocidade_y += self.gravidade
        self.rect.centery += self.velocidade_y
        self.vl_x += self.vl_x
        self.vl_y += self.vl_y

    def para_horizontal(self):
        self.velocidade_x = 0

    def para_vertical(self):
        self.velocidade_y = 0

    def scale_image(self, image):
        boy = pygame.image.load(image)
        return pygame.transform.scale(boy, (85, 155))