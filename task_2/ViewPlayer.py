from enum import Enum


class AppearancePlayer(Enum):
    FACE = {
        'face_shape': ['овальное', 'круглое', 'квадратное', 'треугольное', 'вытянутое', 'сердцевидное'],
        'facial_expression': ['серьёзное', 'улыбчивое', 'хмурое', 'надменное', 'усталое'],
        'face_size': ['маленькое', 'среднее', 'крупное']
    }

    BODY = {
        'build': ['худощавое', 'спортивное', 'полное', 'мускулистое', 'гибкое', 'коренастое'],
        'posture': ['прямая', 'сутулая', 'гордая', 'расхлябанная']
    }

    NOSE = {
        'nose_shape': ['прямой', 'курносый', 'орлиный', 'широкий', 'вздёрнутый', 'с горбинкой'],
        'nose_size': ['маленький', 'средний', 'большой']
    }

    EARS = {
        'ear_shape': ['округлые', 'заострённые', 'удлинённые', 'прижатые', 'оттопыренные'],
        'ear_size': ['маленькие', 'средние', 'большие']
    }

    MUSCLES = {
        'muscle_development': ['слабые', 'умеренные', 'рельефные', 'мощные', 'жилистые', 'накачанные'],
        'definition': ['выраженный', 'скрытый', 'сухой']
    }

    EYES = {
        'eye_color': ['голубые', 'карие', 'зелёные', 'серые', 'чёрные', 'янтарные'],
        'eye_shape': ['миндалевидные', 'круглые', 'узкие', 'раскосые'],
        'gaze': ['спокойный', 'острый', 'холодный', 'тёплый', 'безумный']
    }

    HAIR = {
        'hair_length': ['короткие', 'средние', 'длинные', 'лысый'],
        'hair_type': ['прямые', 'кудрявые', 'волнистые', 'жёсткие'],
        'hair_color': ['чёрные', 'русые', 'рыжие', 'седые', 'белые', 'пепельные']
    }

    SKIN = {
        'skin_tone': ['бледная', 'смуглая', 'загорелая', 'красноватая', 'фиолетовая', 'зелёная'],
        'skin_texture': ['гладкая', 'шершавая', 'чешуйчатая', 'морщинистая'],
        'features': ['веснушки', 'шрамы', 'татуировки', 'чистая']
    }

    HEIGHT = {
        'height': ['карликовый', 'низкий', 'средний', 'высокий', 'очень высокий', 'гигантский']
    }

    TEETH = {
        'teeth_shape': ['ровные', 'кривые', 'острые', 'отсутствуют'],
        'teeth_color': ['белоснежные', 'жёлтые', 'тёмные']
    }

    VOICE = {
        'voice_timbre': ['низкий', 'высокий', 'хриплый', 'мягкий', 'громкий', 'шёпот'],
        'speech_manner': ['спокойная', 'быстрая', 'шепелявая', 'торжественная']
    }

    HANDS = {
        'hand_type': ['мозолистые', 'изящные', 'сильные', 'дрожащие', 'когтистые'],
        'finger_length': ['длинные пальцы', 'короткие пальцы', 'нормальные пальцы']
    }

    FEET = {
        'foot_size': ['большие', 'маленькие', 'широкие', 'узкие', 'копытные'],
        'gait': ['быстрая', 'тяжёлая', 'плавная', 'косолапая']
    }

    def __init__(self, dataJs):
        self._data = dataJs

    def getValue(self, key):
        return self._data[key]


class ViewPlayer(Enum):
    HUMAN = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),
        (AppearancePlayer.EARS, 'ear_shape'),
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'eye_color'),
        (AppearancePlayer.HAIR, 'hair_color'),
        (AppearancePlayer.SKIN, 'skin_tone')
    ]

    ELF = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),
        (AppearancePlayer.EARS, 'ear_shape'),  # заострённые
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'eye_color'),
        (AppearancePlayer.HAIR, 'hair_length'),
        (AppearancePlayer.HEIGHT, 'height')
    ]

    DWARF = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_size'),  # крупный
        (AppearancePlayer.EARS, 'ear_shape'),
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'eye_color'),
        (AppearancePlayer.HAIR, 'hair_type'),  # густая борода
        (AppearancePlayer.HEIGHT, 'height')  # низкий
    ]

    ORC = [
        (AppearancePlayer.FACE, 'facial_expression'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),
        (AppearancePlayer.EARS, 'ear_shape'),
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'gaze'),
        (AppearancePlayer.TEETH, 'teeth_shape'),  # острые клыки
        (AppearancePlayer.SKIN, 'skin_tone')  # зелёная
    ]

    HALFLING = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_size'),
        (AppearancePlayer.EARS, 'ear_size'),
        (AppearancePlayer.EYES, 'eye_color'),
        (AppearancePlayer.HAIR, 'hair_color'),
        (AppearancePlayer.HEIGHT, 'height'),
        (AppearancePlayer.FEET, 'foot_size')  # большие ступни
    ]

    GNOME = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_size'),
        (AppearancePlayer.EARS, 'ear_shape'),
        (AppearancePlayer.EYES, 'eye_shape'),
        (AppearancePlayer.HAIR, 'hair_color'),
        (AppearancePlayer.HEIGHT, 'height'),
        (AppearancePlayer.HANDS, 'finger_length')
    ]

    TIEFLING = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),
        (AppearancePlayer.EARS, 'ear_shape'),
        (AppearancePlayer.EYES, 'eye_color'),
        (AppearancePlayer.HAIR, 'hair_color'),
        (AppearancePlayer.SKIN, 'skin_tone'),  # красноватая/фиолетовая
        (AppearancePlayer.VOICE, 'voice_timbre')
    ]

    DRAGONBORN = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'eye_shape'),
        (AppearancePlayer.SKIN, 'skin_texture'),  # чешуя
        (AppearancePlayer.TEETH, 'teeth_shape'),
        (AppearancePlayer.VOICE, 'voice_timbre')
    ]

    GOBLIN = [
        (AppearancePlayer.FACE, 'facial_expression'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),  # крючковатый
        (AppearancePlayer.EARS, 'ear_shape'),
        (AppearancePlayer.EYES, 'eye_shape'),
        (AppearancePlayer.TEETH, 'teeth_shape'),
        (AppearancePlayer.SKIN, 'skin_tone'),
        (AppearancePlayer.HEIGHT, 'height')
    ]

    CATFOLK = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_size'),
        (AppearancePlayer.EARS, 'ear_shape'),  # кошачьи уши
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'eye_shape'),  # вертикальный зрачок
        (AppearancePlayer.HAIR, 'hair_type'),
        (AppearancePlayer.HANDS, 'hand_type')  # когти
    ]

    LIZARDFOLK = [
        (AppearancePlayer.FACE, 'face_shape'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.NOSE, 'nose_shape'),
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'eye_shape'),
        (AppearancePlayer.SKIN, 'skin_texture'),  # чешуя
        (AppearancePlayer.TEETH, 'teeth_shape'),
        (AppearancePlayer.HANDS, 'hand_type')
    ]

    FAIRY = [
        (AppearancePlayer.FACE, 'face_size'),
        (AppearancePlayer.BODY, 'build'),
        (AppearancePlayer.EYES, 'eye_color'),
        (AppearancePlayer.HAIR, 'hair_color'),
        (AppearancePlayer.SKIN, 'skin_tone'),
        (AppearancePlayer.HEIGHT, 'height'),  # крошечный
        (AppearancePlayer.VOICE, 'voice_timbre'),
        (AppearancePlayer.EARS, 'ear_shape')
    ]

    UNDEAD = [
        (AppearancePlayer.FACE, 'facial_expression'),
        (AppearancePlayer.BODY, 'posture'),
        (AppearancePlayer.MUSCLES, 'muscle_development'),
        (AppearancePlayer.EYES, 'gaze'),
        (AppearancePlayer.SKIN, 'skin_tone'),  # бледная/серая
        (AppearancePlayer.TEETH, 'teeth_shape'),
        (AppearancePlayer.VOICE, 'voice_timbre'),
        (AppearancePlayer.HANDS, 'hand_type')
    ]

    # ====================================== #

    def __init__(self, l):
        self._items = l
        self._N = len(l)

    def buildView(self) -> dict:
        resdata = {'face': self._items[0][0].getValue(self._items[0][1]),
                   'body': self._items[1][0].getValue(self._items[1][1]),
                   'muscles': self._items[2][0].getValue(self._items[2][1]),
                   'eyes': self._items[3][0].getValue(self._items[3][1]),
                   'skin': self._items[4][0].getValue(self._items[4][1]),
                   'teeth': self._items[5][0].getValue(self._items[5][1]),
                   'voice': self._items[6][0].getValue(self._items[6][1]),
                   'hands': self._items[7][0].getValue(self._items[7][1])
                   }
        return resdata
