class Settings():
    def __init__(self, settings_json):
        self.sound_on = settings_json['sound_on']
        self.soundtrack = settings_json['soundtrack']
        self.background_image = settings_json['background_image']
        self.background_image_gameover = settings_json['background_image_gameover']
        self.width = settings_json['res_width']
        self.height = settings_json['res_height']
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