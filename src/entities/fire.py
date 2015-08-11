from entities import base
from enum import FireState

class Fire(base.Base):
    '''Fire class
    '''
    def __init__(self, direction, image_surf, display_surf, screen_width, screen_height, current_position_x = 0, current_position_y = 0):

        fire_image_x_y = {}
        fire_image_x_y[FireState.FIRST] = {"x": 33, "y": 33}
        fire_image_x_y[FireState.SECOND] = {"x": 66, "y": 33}
        fire_image_x_y[FireState.THIRD] = {"x": 99, "y": 33}

        self._fire_counter = 3
        self._fire_state = 1
        self._fire_index = 0

        self._image_size = 31
        super(Fire, self).__init__(direction, image_surf, display_surf, screen_width, screen_height, fire_image_x_y, current_position_x=current_position_x, current_position_y=current_position_y)

    def set_direction(self, direction):
        super(Fire, self).set_direction(direction)
        
        self._image_x = self._image_X_Y[direction]["x"]
        self._image_y = self._image_X_Y[direction]["y"]

    def render(self):
        
        if self._fire_index < self._fire_counter and self._fire_state <= 3:
            if self._fire_state == FireState.FIRST:
                self.set_direction(FireState.FIRST)

            if self._fire_state == FireState.SECOND:
                self.set_direction(FireState.SECOND)

            if self._fire_state == FireState.THIRD:
                self.set_direction(FireState.THIRD)

            super(Fire, self).render()
            self._fire_index = self._fire_index + 1
        else:
            self._fire_index = 0
            self._fire_state = self._fire_state + 1
