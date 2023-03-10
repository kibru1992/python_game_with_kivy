from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':  # these code(on_keyboard_down and on_keyboard_up)
        self.current_speed_x = self.SPEED_X  # are used to control the horizontal movement
    elif keycode[1] == 'right':  # (left or right) on the keyboard
        self.current_speed_x = -self.SPEED_X
    return True


def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    return True


def on_touch_down(self, touch):
    if not self.state_game_over and self.state_game_has_started:
        if touch.x < self.width / 2:  # these code(on_touch_down and on_touch_up)
            # print("<-")                                     # are used to control the horizontal movement
            self.current_speed_x = self.SPEED_X  # (left or right) on the screen
        else:
            # print("->")
            self.current_speed_x = -self.SPEED_X
    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    # print("UP")
    self.current_speed_x = 0
