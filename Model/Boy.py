import pygame

class Boy(pygame.sprite.Sprite):
    def __init__(self, settings):
        boy = pygame.image.load(settings.char_right)
        pygame.sprite.Sprite.__init__(self)
        self.sprites_Right = []
        self.sprites_Left = []
        self.is_movementing_Right = False
        self.is_movementing_Left = False
        self.sprites_Right.append(self.scale_image(settings.char_right, settings.char_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_right1, settings.char_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_right2, settings.char_ratio))
        self.sprites_Left.append(self.scale_image(settings.char_left, settings.char_ratio))
        self.sprites_Left.append(self.scale_image(settings.char_walking_left1, settings.char_ratio))
        self.sprites_Left.append(self.scale_image(settings.char_walking_left2, settings.char_ratio))
        self.current_sprite = 0
        self.image = self.sprites_Right[self.current_sprite]
        self.rect = pygame.Rect(settings.char_starting_pos_x, settings.char_starting_pos_y)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0.03

    def mover_para_esquerda(self, settings):
        self.is_movementing_Left = True
        self.velocidade_x = -1

    def mover_para_direita(self, settings):
        self.is_movementing_Right = True        
        self.velocidade_x = 1

    def pular(self):
        self.velocidade_y = -3

    def update(self):
        self.rect.centerx += self.velocidade_x

        # gravidade do Y
        self.velocidade_y += self.gravidade
        self.rect.centery += self.velocidade_y

        # Caminhar para a direita
        if self.is_movementing_Right == True:
            self.current_sprite += 0.03
            if self.current_sprite >= len(self.sprites_Right):
                self.current_sprite = 0
            self.image = self.sprites_Right[int(self.current_sprite)]    

        # Caminhar para a esquerda
        if self.is_movementing_Left == True:
            self.current_sprite += 0.03
            if self.current_sprite >= len(self.sprites_Left):
                self.current_sprite = 0
            self.image = self.sprites_Left[int(self.current_sprite)] 

    def parar_movimento_horizontal(self):
        self.velocidade_x = 0
        if self.is_movementing_Right == True:
            self.is_movementing_Right = False
            self.image = self.sprites_Right[int(0)] 
        elif self.is_movementing_Left == True:
            self.is_movementing_Left = False
            self.image = self.sprites_Left[int(0)] 

    def parar_movimento_vertical(self):
        self.velocidade_y = 0

    def scale_image(self, image, escala_do_personagem):
        boy = pygame.image.load(image)
        return pygame.transform.scale(boy, escala_do_personagem)
