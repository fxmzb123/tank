from entities import base
from entities import missile
from entities import enum

class Tank(base.Base):
    _missiles = []
    
    def add_missile(self, missile):
        self._missiles.append(missile)
    
    def get_missiles(self):
        return self._missiles    
    
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
        