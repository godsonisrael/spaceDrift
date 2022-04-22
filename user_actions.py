from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.acceleration_x = -self.move_x
    elif keycode[1] == 'right':
        self.acceleration_x = self.move_x
    return True


def on_keyboard_up(self, keyboard, keycode):
    self.acceleration_x = 0
    return True


def on_touch_down(self, touch):
    if not self.is_game_over and self.is_game_started:
        if touch.x < self.width / 2:
            self.acceleration_x = -self.move_x
        if touch.x > self.width / 2:
            self.acceleration_x = self.move_x
    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    self.acceleration_x = 0