import pygame

class Boy(pygame.sprite.Sprite):
    def __init__(self, settings):
        boy = pygame.image.load(settings.char_right)
        pygame.sprite.Sprite.__init__(self)
        self.sprites_to_the_right = []
        self.sprites_to_the_left = []
        self.is_moving_to_the_right = False
        self.is_moving_to_the_left = False
        self.sprites_to_the_right.append(self.scale_image(settings.char_right, settings.char_ratio))
        self.sprites_to_the_right.append(self.scale_image(settings.char_walking_right1, settings.char_ratio))
        self.sprites_to_the_right.append(self.scale_image(settings.char_walking_right2, settings.char_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.char_left, settings.char_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.char_walking_left1, settings.char_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.char_walking_left2, settings.char_ratio))
        self.current_sprite = 0
        self.image = self.sprites_to_the_right[self.current_sprite]
        self.rect = pygame.Rect(settings.char_starting_left_top, settings.char_starting_width_height)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0.03

    def mover_para_esquerda(self, settings):
        self.is_moving_to_the_left = True
        self.velocidade_x = -3

    def mover_para_direita(self, settings):
        self.is_moving_to_the_right = True        
        self.velocidade_x = 3

    def pular(self):
        self.velocidade_y = -3

    def update(self):
        self.rect.centerx += self.velocidade_x

        # gravidade do Y
        self.velocidade_y += self.gravidade
        self.rect.centery += self.velocidade_y

        # Caminhar para a direita
        if self.is_moving_to_the_right == True:
            self.current_sprite += 0.03
            if self.current_sprite >= len(self.sprites_to_the_right):
                self.current_sprite = 0
            self.image = self.sprites_to_the_right[int(self.current_sprite)]

        # Caminhar para a esquerda
        if self.is_moving_to_the_left == True:
            self.current_sprite += 0.03
            if self.current_sprite >= len(self.sprites_to_the_left):
                self.current_sprite = 0
            self.image = self.sprites_to_the_left[int(self.current_sprite)]

    def parar_movimento_horizontal(self):
        self.velocidade_x = 0
        if self.is_moving_to_the_right == True:
            self.is_moving_to_the_right = False
            self.image = self.sprites_to_the_right[int(0)]
        elif self.is_moving_to_the_left == True:
            self.is_moving_to_the_left = False
            self.image = self.sprites_to_the_left[int(0)]

    def parar_movimento_vertical(self):
        self.velocidade_y = 0

    def scale_image(self, image, escala_do_personagem):
        boy = pygame.image.load(image)
        return pygame.transform.scale(boy, escala_do_personagem)
