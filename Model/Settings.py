import pygame

class Settings():
    def __init__(self, settings_json):
        # Propriedades do menu #
        self.sound_on = settings_json['sound_on']
        self.soundtrack = settings_json['soundtrack']
        self.background_image = settings_json['background_image']
        self.width = settings_json['res_width']
        self.height = settings_json['res_height']
        # Personagem - Aurelinho #
        self.char_left = settings_json['character_to_the_left']
        self.char_right = settings_json['character_to_the_right']
        self.char_walking_left1 = settings_json['character_walking_to_the_left1']
        self.char_walking_left2 = settings_json['character_walking_to_the_left2']
        self.char_walking_right1 = settings_json['character_walking_to_the_right1']
        self.char_walking_right2 = settings_json['character_walking_to_the_right2']
        self.char_ratio = tuple(map(int, settings_json['character_ratio'].split(',')))
        self.char_starting_pos_x = tuple(map(int, settings_json['character_starting_pos_x'].split(',')))
        self.char_starting_pos_y = tuple(map(int, settings_json['character_starting_pos_y'].split(',')))
        # Apagador #
        self.eraser = settings_json['eraser']
        self.eraser_ratio = tuple(map(int, settings_json['eraser_ratio'].split(',')))
        self.eraser_starting_pos_x = tuple(map(int, settings_json['eraser_starting_pos_x'].split(',')))
        # Vida #
        self.life = settings_json['life']
        self.life_ratio = tuple(map(int, settings_json['life_ratio'].split(',')))
        self.life_starting_pos_x = tuple(map(int, settings_json['life_starting_pos_x'].split(',')))
        self.starting_number_of_lives = settings_json['starting_number_of_lives']
        # Gamover #
        self.gameover_image = settings_json['gameover_image']
        self.gameover_sound = settings_json['gameover_sound']
        # Sons #
        self.hit_sound = settings_json['hit_sound']



    # Sound effects #
    def som_colisao(self):
        pygame.mixer.music.load(self.som_colisao)
        pygame.mixer.music.play(0)

    def som_gameover():
        pygame.mixer.music.load(self.som_gameover)
        pygame.mixer.music.play(0)