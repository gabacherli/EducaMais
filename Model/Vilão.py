import pygame
from idlelib import window
from Model.Settings import Settings

class Vilao(pygame.sprite.Sprite):
    def __init__(self, settings):
        global window
        vilao = pygame.image.load(settings.char_right)
        balao01 = pygame.image.load(settings.char_balao_speak01)
        balao02 = pygame.image.load(settings.char_balao_speak02)
        window = pygame.display.set_mode((settings.width, settings.height))
        pygame.sprite.Sprite.__init__(self)

        self.sprites_Right = []
        self.is_movementing_Right = True
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right1, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right2, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right3, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right4, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right5, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right6, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right7, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right8, settings.char_vilao_ratio))
        self.sprites_Right.append(self.scale_image(settings.char_walking_vilao_right9, settings.char_vilao_ratio))
        self.current_sprite = 0
        self.image = self.sprites_Right[self.current_sprite]
        self.image_balao01 = pygame.transform.scale(balao01, settings.char_balao_ratio)
        self.image_balao02 = pygame.transform.scale(balao02, settings.char_balao_ratio)
        self.rect = pygame.Rect(settings.char_starting_vilao_pos_x, settings.char_starting_vilao_pos_y)
        self.velocidade_x = -1
        self.velocidade_y = 0


    def mover_para_direita(self, settings):
        if self.is_movementing_Right == True:
            self.current_sprite += 0.03
            if self.current_sprite >= len(self.sprites_Right):
                self.current_sprite = 0
            self.image = self.sprites_Right[int(self.current_sprite)]   


    def update(self):
        self.rect.centerx += self.velocidade_x
        settingsx = Settings

        # Caminhar para a direita
        Vilao.mover_para_direita(self, settingsx)

        if self.rect.x < 700:
            window.blit(self.image_balao01, ((self.rect.x - 50), (self.rect.y - 50)))
           
        if self.rect.x < 200:
            window.blit(self.image_balao02, ((self.rect.x - 50), (self.rect.y - 50)))

        if self.rect.x < 0:
            self.rect.x  = 1250
   

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
