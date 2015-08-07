from random import randint
import pygame

from entities import enum
from system import utils
from pygame import Rect

class Base(object):
    _id = None
    _image_x = 0
    _image_y = 0
    _image_size = 32
    _offset = 1
    
    _image_surf = None
    _display_surf = None
    _name = None
    _direction = None
    
    _is_left_move_allowed = False
    _is_right_move_allowed = False
    _is_up_move_allowed = False
    _is_down_move_allowed = False
    
    _move_increment = 1 
    
    _current_position_x = 0;
    _current_position_y = 0;
    
    _screen_weight = 0
    _screen_height = 0
    
    _rect = None
    
    _move_direction_counter = 0
    _random_direction = enum.Sprite.DOWN

    _image_X_Y = {}
            
    def get_id(self):
        return self._id
    
    def __init__(self, direction, image_surf, display_surf, screen_width, screen_height, image_X_Y, move_increment=1, current_position_x = 0, current_position_y = 0):
        
        self._id = utils.Utils.get_uuid()
    
        self._image_X_Y = image_X_Y
        self.set_direction(direction)
        self._image_surf = image_surf
        self._display_surf = display_surf
        
        self._screen_weight = screen_width
        self._screen_height = screen_height
        
        self._move_increment = move_increment
        self._current_position_x = current_position_x
        self._current_position_y = current_position_y

        self._random_direction = randint(1, 4)
    
    def get_rect(self):
        return pygame.Rect((self._current_position_x, self._current_position_y), (self._image_size-self._offset, self._image_size-self._offset))
    
    def is_collide(self, rect):
        return self.get_rect().colliderect(rect)

    def get_rect_of_next_move(self):
        x = self.get_current_position_x()
        y = self.get_current_position_y()
        
        moving = False
                
        if self._is_right_move_allowed:
            if (self._direction == enum.Sprite.RIGHT):
                if self._current_position_x < (self._screen_weight - self.get_image_size()):
                    x = self._current_position_x + self._move_increment
            moving = True

        if self._is_left_move_allowed:    
            if (self._direction == enum.Sprite.LEFT):
                if self._current_position_x > 0:
                    x = self._current_position_x - self._move_increment
            moving = True
        
        if self._is_up_move_allowed:    
            if (self._direction == enum.Sprite.UP):
                if self._current_position_y > 0:
                    y = self._current_position_y - self._move_increment

            moving = True

        if self._is_down_move_allowed: 
            if (self._direction == enum.Sprite.DOWN):
                if self._current_position_y < (self._screen_height - self.get_image_size()):
                    y = self._current_position_y + self._move_increment
            moving = True

        if moving:
            return Rect(x, y, self._image_size, self._image_size)
        else:
            return None

    def get_collision_side(self, rect):
        if self.get_direction() == enum.Sprite.UP or self.get_direction() == enum.Sprite.DOWN:
            if self.get_rect().centery < rect.centery:
                return enum.Sprite.DOWN
            elif self.get_rect().centery > rect.centery:
                return enum.Sprite.UP

        if self.get_direction() == enum.Sprite.LEFT or self.get_direction() == enum.Sprite.RIGHT:
            if self.get_rect().centerx > rect.centerx:
                return enum.Sprite.LEFT
            if self.get_rect().centerx < rect.centerx:
                return enum.Sprite.RIGHT

    def set_current_position(self, x, y):
        self.set_current_position_x(x)
        self.set_current_position_y(y)
    
    def set_current_position_x(self, x):
        self._current_position_x = x
    
    def get_current_position_x(self):
        return self._current_position_x
    
    def set_current_position_y(self, y):
        self._current_position_y = y
        
    def get_current_position_y(self):
        return self._current_position_y    
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
        
    def get_image_x(self):
        return self._image_x
    def set_image_x(self, imageX):
        self._image_x = imageX
    
    def set_image_y(self, imageY):
        self._image_y = imageY
    def get_image_y(self):
        return self._image_y
    
    def get_image_size(self):
        return self._image_size;
    
    def set_direction(self, direction):
        self._direction = direction
    
    def get_direction(self):
        return self._direction

    def set_up(self):
        self.set_direction(enum.Sprite.UP)
        self.set_is_move_allowed(True, enum.Sprite.UP)
    def set_down(self):
        self.set_direction(enum.Sprite.DOWN)
        self.set_is_move_allowed(True, enum.Sprite.DOWN)
    def set_left(self):
        self.set_direction(enum.Sprite.LEFT)
        self.set_is_move_allowed(True, enum.Sprite.LEFT)
    def set_right(self):
        self.set_direction(enum.Sprite.RIGHT)
        self.set_is_move_allowed(True, enum.Sprite.RIGHT)

    def set_move_direction(self, direction):
        if direction == enum.Sprite.UP:
            self.set_up()
        if direction == enum.Sprite.DOWN:
            self.set_down()
        if direction == enum.Sprite.LEFT:
            self.set_left()
        if direction == enum.Sprite.RIGHT:
            self.set_right()

    def set_is_move_allowed(self, allowed, direction):
        #self._is_move_allowed = allowed
        if direction == enum.Sprite.DOWN:
            self._is_down_move_allowed = allowed
        if direction == enum.Sprite.LEFT:
            self._is_left_move_allowed = allowed
        if direction == enum.Sprite.RIGHT:
            self._is_right_move_allowed = allowed
        if direction == enum.Sprite.UP:
            self._is_up_move_allowed = allowed
    
    def get_random_direction(self):
        self._move_direction_counter += 1
        
        if self._move_direction_counter == 100:
            self._move_direction_counter = 0
            self._random_direction = randint(1, 4)   
        
        return self._random_direction

    def move(self):
        if self._is_right_move_allowed:
            if (self._direction == enum.Sprite.RIGHT):
                if self._current_position_x < (self._screen_weight - self.get_image_size()):
                    self._current_position_x += self._move_increment
        
        if self._is_left_move_allowed:    
            if (self._direction == enum.Sprite.LEFT):
                if self._current_position_x > 0:
                    self._current_position_x -= self._move_increment
        
        if self._is_up_move_allowed:    
            if (self._direction == enum.Sprite.UP):
                if self._current_position_y > 0:
                    self._current_position_y -= self._move_increment
        
        if self._is_down_move_allowed: 
            if (self._direction == enum.Sprite.DOWN):
                if self._current_position_y < (self._screen_height - self.get_image_size()):
                    self._current_position_y += self._move_increment
        
    def render(self):
        self._display_surf.blit(self._image_surf,(self._current_position_x, self._current_position_y), (self._image_x, self._image_y, self._image_size, self._image_size))