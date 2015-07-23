from entities.base import Base
from entities.enum import TileState

'''This module contains Tile class
'''
class Tile(Base):
    '''Base tile class, it provides some common methods for its sub classes
    '''
    def set_direction(self, direction):
        super(Tile, self).set_direction(direction)
        
        self._image_x = self._image_X_Y[direction]["x"]
        self._image_y = self._image_X_Y[direction]["y"]
        
class Brick(Tile):
    '''Tile class for brick tile
    '''
    def __init__(self, direction, image_surf, display_surf, screen_width, screen_height, current_position_x = 0, current_position_y = 0):
        brick_tile_image_x_y = {}
        brick_tile_image_x_y[TileState.INIT] = {"x": 132, "y": 99}
        brick_tile_image_x_y[TileState.LIGHT_BREAK] = {"x": 231, "y": 330}
        brick_tile_image_x_y[TileState.MIDDLE_BREAK] = {"x": 264, "y": 330}
        brick_tile_image_x_y[TileState.FINAL_BREAK] = {"x": 297, "y": 330}

        super(Brick, self).__init__(direction, image_surf, display_surf, screen_width, screen_height, brick_tile_image_x_y, current_position_x=current_position_x, current_position_y=current_position_y)
              
class Grass(Tile):
    '''Tile class for grass tile
    '''
    pass
