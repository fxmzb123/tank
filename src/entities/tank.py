from random import randint

from entities import base
from entities.missile import Missile
from entities import enum

class Tank(base.Base):
    

    def fire_missile_randomly(self):
        random_integer = randint(0, 50)

        if random_integer == 50:
            self.fire_missile()

    def fire_missile(self):
        missile_position = self.get_missile_position()

        missile = Missile(self.get_direction(), self._image_surf, self._display_surf, self._screen_weight, self._screen_height, None, 5, current_position_x=missile_position['x'], current_position_y=missile_position['y'], offset=14)
        missile.set_is_move_allowed(True, self.get_direction())
        self.add_missile(missile)
    
    def add_missile(self, missile):
        self._missiles.append(missile)
    
    def get_missiles(self):
        return self._missiles   
    
    def remove_missiles(self, indexes):
        for index in indexes:
            del self._missiles[index]

    def get_missile_position(self):
        missile_position = {}
        
        if self.get_direction() == enum.Sprite.UP:
            missile_position['x'] = self.get_current_position_x()
            missile_position['y'] =  self.get_current_position_y() - self.get_image_size()   
        
        if self.get_direction() == enum.Sprite.DOWN:
            missile_position['x'] = self.get_current_position_x()
            missile_position['y'] =  self.get_current_position_y() + self.get_image_size()
        
        if self.get_direction() == enum.Sprite.LEFT:
            missile_position['x'] = self.get_current_position_x() - self.get_image_size()
            missile_position['y'] =  self.get_current_position_y()   
        
        if self.get_direction() == enum.Sprite.RIGHT:
            missile_position['x'] = self.get_current_position_x() + self.get_image_size()
            missile_position['y'] =  self.get_current_position_y()
    
        return missile_position
        
    def set_direction(self, direction):
        super(Tank, self).set_direction(direction)
        
        if self._direction == enum.Sprite.UP:
            self._image_x = self._image_X_Y[enum.Sprite.UP]["x"]
            self._image_y = self._image_X_Y[enum.Sprite.UP]["y"]
        
        if self._direction == enum.Sprite.DOWN:
            self._image_x = self._image_X_Y[enum.Sprite.DOWN]["x"]
            self._image_y = self._image_X_Y[enum.Sprite.DOWN]["y"]
        
        if self._direction == enum.Sprite.RIGHT:
            self._image_x = self._image_X_Y[enum.Sprite.RIGHT]["x"]
            self._image_y = self._image_X_Y[enum.Sprite.RIGHT]["y"]
            
        if self._direction == enum.Sprite.LEFT:
            self._image_x = self._image_X_Y[enum.Sprite.LEFT]["x"]
            self._image_y = self._image_X_Y[enum.Sprite.LEFT]["y"]
        