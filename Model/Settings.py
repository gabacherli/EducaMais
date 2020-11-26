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
        self.aurelinho_ratio = tuple(map(int, settings_json['aurelinho_ratio'].split(',')))
        self.aurelinho_starting_pos_x = tuple(map(int, settings_json['aurelinho_starting_pos_x'].split(',')))
        self.aurelinho_starting_pos_y = tuple(map(int, settings_json['aurelinho_starting_pos_y'].split(',')))
        self.aurelinho_starting_left_top = tuple(map(int, settings_json['aurelinho_starting_left_top'].split(',')))
        self.aurelinho_starting_width_height = tuple(map(int, settings_json['aurelinho_starting_width_height'].split(',')))
        self.aurelinho_to_the_left = settings_json['aurelinho_to_the_left']
        self.aurelinho_to_the_right = settings_json['aurelinho_to_the_right']
        self.aurelinho_walking_to_the_left1 = settings_json['aurelinho_walking_to_the_left1']
        self.aurelinho_walking_to_the_left2 = settings_json['aurelinho_walking_to_the_left2']
        self.aurelinho_walking_to_the_right1 = settings_json['aurelinho_walking_to_the_right1']
        self.aurelinho_walking_to_the_right2 = settings_json['aurelinho_walking_to_the_right2']
        # Personagem - Vilão #
        self.villain_ratio = tuple(map(int, settings_json['villain_ratio'].split(',')))
        self.villain_starting_pos_x = tuple(map(int, settings_json['villain_starting_pos_x'].split(',')))
        self.villain_starting_pos_y = tuple(map(int, settings_json['villain_starting_pos_y'].split(',')))
        self.villain_walking_to_the_left1 = settings_json['villain_walking_to_the_left1']
        self.villain_walking_to_the_left2 = settings_json['villain_walking_to_the_left2']
        self.villain_walking_to_the_left3 = settings_json['villain_walking_to_the_left3']
        self.villain_walking_to_the_left4 = settings_json['villain_walking_to_the_left4']
        self.villain_walking_to_the_left5 = settings_json['villain_walking_to_the_left5']
        self.villain_walking_to_the_left6 = settings_json['villain_walking_to_the_left6']
        self.villain_walking_to_the_left7 = settings_json['villain_walking_to_the_left7']
        self.villain_walking_to_the_left8 = settings_json['villain_walking_to_the_left8']
        self.villain_walking_to_the_left9 = settings_json['villain_walking_to_the_left9']
        # Balão de fala #
        self.chat_balloon_ratio = tuple(map(int, settings_json['chat_balloon_ratio'].split(',')))
        self.chat_balloon01 = settings_json['chat_balloon01']
        self.chat_balloon02 = settings_json['chat_balloon02']
        # Plataforma #
        self.platform = settings_json['platform']
        self.platform_ratio = tuple(map(int, settings_json['platform_ratio'].split(',')))
        # Apagador #
        self.eraser = settings_json['eraser']
        self.eraser_ratio = tuple(map(int, settings_json['eraser_ratio'].split(',')))
        self.eraser_starting_left_top = tuple(map(int, settings_json['eraser_starting_left_top'].split(',')))
        # Vida #
        self.life = settings_json['life']
        self.life_ratio = tuple(map(int, settings_json['life_ratio'].split(',')))
        self.life_starting_left_top = tuple(map(int, settings_json['life_starting_left_top'].split(',')))
        self.starting_number_of_lives = settings_json['starting_number_of_lives']
        # Quadro branco #
        self.whiteboard = settings_json['whiteboard']
        self.whiteboard_ratio = tuple(map(int, settings_json['whiteboard_ratio'].split(',')))
        self.whiteboard_starting_left_top = tuple(map(int, settings_json['whiteboard_starting_left_top'].split(',')))
        self.whiteboard_starting_width_height = tuple(map(int, settings_json['whiteboard_starting_width_height'].split(',')))
        # Palavra do quadro branco #
        self.whiteboard_word_starting_left_top = tuple(map(int, settings_json['whiteboard_word_starting_left_top'].split(',')))
        self.whiteboard_word_starting_width_height = tuple(map(int, settings_json['whiteboard_word_starting_width_height'].split(',')))
        # Gameover #
        self.gameover_image = settings_json['gameover_image']
        # Sons #
        self.gameover_sound = settings_json['gameover_sound']
        self.hit_sound = settings_json['hit_sound']
