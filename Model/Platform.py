import pygame

from random import randint

black = (0,0,0)

class Platform(pygame.sprite.Sprite):
    def __init__(self, settings, letter):
        width = settings.platform_ratio[0]
        height = settings.platform_ratio[1]
        random_left_top = (randint(10, settings.width - width), randint(int(settings.height/5) + height, int(settings.height/1.25)))
        random_width_height = (randint(0, settings.width - width), randint(int(settings.height/1.25), settings.height - height))
        platform = pygame.image.load(settings.platform)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform, settings.platform_ratio)
        self.rect = pygame.Rect(random_left_top, random_width_height)
        self.font = pygame.font.Font('freesansbold.ttf', 50)

        self.letter_rectangle = pygame.Rect(random_left_top, random_width_height)
        self.letter_rectangle.center = self.rect.center
        self.letter_rectangle.x = self.rect.x + width / 2.36
        self.letter_rectangle.centery = self.rect.centery - height/1.5

    def generate_platform_that_wont_collide(self, settings, platforms, letter):
        new_platform = Platform(settings, letter)

        while new_platform.rect.collidelist(platforms):
            new_platform = new_platform.generate_platform_that_wont_collide(settings, platforms, letter)

        return new_platform

    def write_letter_to_letter_rectangle(self, letter):
        self.text_surface = self.font.render(letter, True, black)

        return self.text_surface


