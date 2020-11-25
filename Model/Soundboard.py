import pygame

class Soundboard():
    def __init__(self, settings):
        self.gameover_sound = settings.gameover_sound
        self.hit_sound = settings.hit_sound

    # Sound effects #
    def play_hit_sound(self):
        pygame.mixer.music.load(self.hit_sound)
        pygame.mixer.music.play(0)

    def play_gameover_sound(self):
        pygame.mixer.music.load(self.gameover_sound)
        pygame.mixer.music.play(0)