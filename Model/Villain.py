import pygame


class Villain(pygame.sprite.Sprite):
    def __init__(self, settings):
        global window
        villain = pygame.image.load(settings.villain_walking_to_the_left1)
        pygame.sprite.Sprite.__init__(self)
        window = pygame.display.set_mode((settings.width, settings.height))

        self.sprites_to_the_left = []
        self.is_moving_to_the_left = True
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left1, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left2, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left3, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left4, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left5, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left6, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left7, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left8, settings.villain_ratio))
        self.sprites_to_the_left.append(self.scale_image(settings.villain_walking_to_the_left9, settings.villain_ratio))
        self.current_sprite = 0
        self.image = self.sprites_to_the_left[self.current_sprite]

        self.rect = pygame.Rect(settings.villain_starting_pos_x, settings.villain_starting_pos_y)
        self.velocidade_x = -1
        self.velocidade_y = 0

        chat_balloon01 = pygame.image.load(settings.chat_balloon01)
        chat_balloon02 = pygame.image.load(settings.chat_balloon02)
        self.balloon_image01 = pygame.transform.scale(chat_balloon01, settings.chat_balloon_ratio)
        self.balloon_image02 = pygame.transform.scale(chat_balloon02, settings.chat_balloon_ratio)


    def mover_para_esquerda(self):
        if self.is_moving_to_the_left == True:
            self.current_sprite += 0.03
            if self.current_sprite >= len(self.sprites_to_the_left):
                self.current_sprite = 0
            self.image = self.sprites_to_the_left[int(self.current_sprite)]


    def update(self, settings):
        self.rect.centerx += self.velocidade_x

        # Caminhar para a esquerda
        self.mover_para_esquerda()

        if self.rect.x < settings.width/1.5:
            window.blit(self.balloon_image01, ((self.rect.x - 50), (self.rect.y - 50)))
           
        if self.rect.x < settings.width/6:
            window.blit(self.balloon_image02, ((self.rect.x - 50), (self.rect.y - 50)))

        if self.rect.x < 0 - settings.villain_ratio[0]:
            self.rect.x = settings.width

    def scale_image(self, image, escala_do_personagem):
        villain = pygame.image.load(image)
        return pygame.transform.scale(villain, escala_do_personagem)
