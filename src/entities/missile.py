import pygame

from entities import base
from entities import enum

class Missile(base.Base):
    def is_touched_border(self):
        if self._direction == enum.Sprite.UP:
            if self.get_current_position_y() <= 0:
                return True
        
        if self._direction == enum.Sprite.DOWN:
            if self.get_current_position_y() + self.get_image_size() >= self._screen_height:
                return True
        
        if self._direction == enum.Sprite.RIGHT:
            if self.get_current_position_x() + self.get_image_size() >= self._screen_weight:
                return True
            
        if self._direction == enum.Sprite.LEFT:
            if self.get_current_position_x() <= 0:
                return True
        
        return False
          
    def set_direction(self, direction):
        super(Missile, self).set_direction(direction)
        
        if self._direction == enum.Sprite.UP:
            self._image_x = 132
            self._image_y = 33
        
        if self._direction == enum.Sprite.DOWN:
            self._image_x = 231
            self._image_y = 33
        
        if self._direction == enum.Sprite.RIGHT:
            self._image_x = 198
            self._image_y = 33
            
        if self._direction == enum.Sprite.LEFT:
            self._image_x = 165
            self._image_y = 33
    
    def get_rect(self):
        return pygame.Rect((self._current_position_x+self._offset, self._current_position_y+self._offset), (self._image_size-self._offset*2, self._image_size-self._offset*2))