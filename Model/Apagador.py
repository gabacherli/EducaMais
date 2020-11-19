import pygame

class Apagador(pygame.sprite.Sprite):
    def __init__(self, settings):
        apagador = pygame.image.load(settings.obj_apagador)
        pygame.sprite.Sprite.__init__(self)

        self.vl_x = 0
        self.vl_y = 0
        self.image = pygame.transform.scale(apagador, settings.char_ratio)
        self.rect = pygame.Rect(settings.obj_apagador_starting_pos_x, settings.char_starting_pos_y)
        self.image = self.scale_image(settings.obj_apagador, settings.obj_apagador_ratio)
        self.velocidade_x = -2
        self.velocidade_y = 0
        self.gravidade = 0.03
        self.x = 0

   

    def update(self):
        self.rect.centerx += self.velocidade_x

        if self.rect.x < 0:
            self.rect.x  = 1250

        
        #print(self.rect.x) 

    def scale_image(self, image, escala_do_personagem):
        boy = pygame.image.load(image)
        return pygame.transform.scale(boy, escala_do_personagem)