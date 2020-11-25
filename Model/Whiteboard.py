import pygame

red = (255,0,0)

class Whiteboard(pygame.sprite.Sprite):
    def __init__(self, settings):
        whiteboard = pygame.image.load(settings.whiteboard)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(whiteboard, settings.whiteboard_ratio)
        self.rect = pygame.Rect(settings.whiteboard_starting_left_top, settings.whiteboard_starting_width_height)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.word_rectangle = pygame.Rect(settings.whiteboard_word_starting_left_top, settings.whiteboard_word_starting_width_height)
        self.word_rectangle.center = self.rect.center
        self.word_rectangle.centery = self.rect.centery * 1.56


    def write_word_to_word_rectangle(self, word):
        self.word_surface = self.font.render(word, True, red)

        return self.word_surface


