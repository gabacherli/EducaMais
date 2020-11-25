import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, settings):
        platform = pygame.image.load(settings.platform_image)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform, settings.platform_ratio)
        self.rect = pygame.Rect(settings.char_starting_pos_x, settings.char_starting_pos_y)

    def scale_image(self, image, escala_da_imagem):
        platform = pygame.image.load(image)
        return pygame.transform.scale(platform, escala_da_imagem)


