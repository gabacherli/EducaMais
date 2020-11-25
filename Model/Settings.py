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
        self.obj_apagador = settings_json['objeto_apagador']
        self.obj_apagador_starting_pos_x = tuple(map(int, settings_json['objeto_apagador_starting_pos_x'].split(',')))
        self.obj_apagador_ratio = tuple(map(int, settings_json['objeto_apagador_ratio'].split(',')))
        self.obj_vida = settings_json['objeto_vida']
        self.obj_vida_starting_pos_x = tuple(map(int, settings_json['objeto_vida_starting_pos_x'].split(',')))
        self.obj_vida_ratio = tuple(map(int, settings_json['objeto_vida_ratio'].split(',')))
        self.som_gameover = settings_json['som_gameover']
        self.som_colisao = settings_json['som_colisao']
        self.char_walking_vilao_right1 = settings_json['character_vilao_walking_to_the_right1']
        self.char_walking_vilao_right2 = settings_json['character_vilao_walking_to_the_right2']
        self.char_walking_vilao_right3 = settings_json['character_vilao_walking_to_the_right3']
        self.char_walking_vilao_right4 = settings_json['character_vilao_walking_to_the_right4']
        self.char_walking_vilao_right5 = settings_json['character_vilao_walking_to_the_right5']
        self.char_walking_vilao_right6 = settings_json['character_vilao_walking_to_the_right6']
        self.char_walking_vilao_right7 = settings_json['character_vilao_walking_to_the_right7']
        self.char_walking_vilao_right8 = settings_json['character_vilao_walking_to_the_right8']
        self.char_walking_vilao_right9 = settings_json['character_vilao_walking_to_the_right9']
        self.char_balao_speak01 = settings_json['character_balao_speak01']
        self.char_balao_speak02 = settings_json['character_balao_speak02']
        self.char_starting_vilao_pos_x = tuple(map(int, settings_json['character_starting_vilao_pos_x'].split(',')))
        self.char_starting_vilao_pos_y = tuple(map(int, settings_json['character_starting_vilao_pos_y'].split(',')))
        self.char_vilao_ratio = tuple(map(int, settings_json['char_vilao_ratio'].split(',')))
        self.char_balao_ratio = tuple(map(int, settings_json['char_balao_ratio'].split(',')))
        self.char_starting_left_top = tuple(map(int, settings_json['character_starting_left_top'].split(',')))
        self.char_starting_width_height = tuple(map(int, settings_json['character_starting_width_height'].split(',')))
        # Apagador #
        self.eraser = settings_json['eraser']
        self.eraser_ratio = tuple(map(int, settings_json['eraser_ratio'].split(',')))
        self.eraser_starting_left_top = tuple(map(int, settings_json['eraser_starting_left_top'].split(',')))
        # Vida #
        self.life = settings_json['life']
        self.life_ratio = tuple(map(int, settings_json['life_ratio'].split(',')))
        self.life_starting_left_top = tuple(map(int, settings_json['life_starting_left_top'].split(',')))
        self.starting_number_of_lives = settings_json['starting_number_of_lives']
        # Plataforma #
        self.platform = settings_json['platform']
        self.platform_ratio = tuple(map(int, settings_json['platform_ratio'].split(',')))
        # Quadro branco #
        self.whiteboard = settings_json['whiteboard']
        self.whiteboard_ratio = tuple(map(int, settings_json['whiteboard_ratio'].split(',')))
        self.whiteboard_starting_left_top = tuple(map(int, settings_json['whiteboard_starting_left_top'].split(',')))
        self.whiteboard_starting_width_height = tuple(map(int, settings_json['whiteboard_starting_width_height'].split(',')))
        self.whiteboard_word_starting_left_top = tuple(map(int, settings_json['whiteboard_word_starting_left_top'].split(',')))
        self.whiteboard_word_starting_width_height = tuple(map(int, settings_json['whiteboard_word_starting_width_height'].split(',')))
        # Gameover #
        self.gameover_image = settings_json['gameover_image']
        # Sons #
        self.gameover_sound = settings_json['gameover_sound']
        self.hit_sound = settings_json['hit_sound']
