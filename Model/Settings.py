class Settings():
    def __init__(self, settings_json):
        self.sound_on = settings_json['sound_on']
        self.background_image = settings_json['background_image']
        self.width = settings_json['res_width']
        self.height = settings_json['res_height']
        self.char_left = settings_json['character_to_the_left']
        self.char_right = settings_json['character_to_the_right']
        self.char_ratio = tuple(map(int, settings_json['character_ratio'].split(',')))
        self.char_starting_pos_x = tuple(map(int, settings_json['character_starting_pos_x'].split(',')))
        self.char_starting_pos_y = tuple(map(int, settings_json['character_starting_pos_y'].split(',')))