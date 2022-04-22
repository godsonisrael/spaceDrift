from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.lang import Builder
from kivy.core.window import Window
from kivy import platform
from kivy.app import App
from kivy.properties import Clock, ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout

Builder.load_file("menu.kv")


def is_desktop():
    if platform in ('linux', 'win', 'macosx'):
        return True
    return False


class MainWidget(RelativeLayout):
    from transform import transform_perspective
    from user_actions import keyboard_closed, on_keyboard_up, on_keyboard_down, on_touch_down, on_touch_up
    from lines import update_lines, get_line_x_from_index, get_line_y_from_index, draw_lines
    from tiles import draw_tiles, update_tiles, pre_filled_tiles, generate_tiles_coordinates, get_tile_coordinates
    from ship import draw_ship, update_ship, is_ship_inside_tile, is_ship_collide
    from audio import init_audio, game_over_delay

    menu_widget: ObjectProperty()

    perspective_point_x = 0
    perspective_point_y = 0

    V_NB_LINES = 10
    V_LINES_SPACING = .25
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = .2
    horizontal_lines = []

    hl_start_index = -int(V_NB_LINES / 2) + 1
    hl_end_index = hl_start_index + V_NB_LINES - 1

    current_offset_y = 0
    acceleration_y = .6
    current_loop_y = 0

    current_offset_x = 0
    acceleration_x = 0
    move_x = 2

    tiles = []
    NB_TILES = 16
    tiles_coordinates = []

    SHIP_WIDTH = .1
    SHIP_HEIGHT = .035
    SHIP_BASE_Y = 0.04
    ship = 0
    ship_coordinates = [(0, 0), (0, 0), (0, 0)]

    is_game_over = False
    is_game_started = False

    menu_title = StringProperty("G    A    L    A    X    Y")
    menu_button_title = StringProperty("S T A R T")
    score_txt = StringProperty()

    sound_begin = None
    sound_gameover_impact = None
    sound_gameover_voice = None
    sound_music1 = None
    sound_restart = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_audio()
        self.draw_lines()
        self.draw_tiles()
        self.draw_ship()
        self.restart_game()

        if is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1 / 60)

    def restart_game(self):

        self.current_offset_y = 0
        self.current_loop_y = 0

        self.current_offset_x = 0
        self.acceleration_x = 0

        self.tiles_coordinates = []

        self.pre_filled_tiles()
        self.generate_tiles_coordinates()

        self.is_game_over = False

    def update(self, dt):
        time_factor = dt * 60

        self.update_lines()
        self.update_tiles()
        self.update_ship()

        if not self.is_game_over and self.is_game_started:
            speed_x = self.acceleration_x * self.width / 100
            speed_y = self.acceleration_y * self.height / 100

            self.current_offset_x += speed_x * time_factor
            self.current_offset_y += speed_y * time_factor

            while self.current_offset_y >= self.H_LINES_SPACING * self.height:
                self.current_offset_y -= self.H_LINES_SPACING * self.height
                self.current_loop_y += 1
                self.score_txt = "SCORE: " + str(self.current_loop_y)
                self.generate_tiles_coordinates()

        if not self.is_ship_collide() and not self.is_game_over:
            self.menu_title = "G  A  M  E    O  V  E  R"
            self.menu_button_title = "R E S T A R T"
            self.is_game_over = True
            self.menu_widget.opacity = 1
            self.sound_music1.stop()
            self.sound_gameover_impact.play()
            Clock.schedule_once(self.game_over_delay, 1)

    def on_menu_button_pressed(self):
        if self.is_game_over:
            self.sound_restart.play()
        else:
            self.sound_begin.play()
        self.sound_music1.play()

        self.restart_game()
        self.is_game_started = True
        self.menu_widget.opacity = 0


class SpaceDriftApp(App):
    pass


SpaceDriftApp().run()
