'''This is the module contains TileManager class
'''
from operator import itemgetter 

from tile import Brick
from entities.enum import TileState
from entities.enum import TileType

class TileManager(object):
    '''TileManager class provides methods for create tile map.
    '''
    def __init__(self, image_surf, display_surf, weight, height):
        '''Constructor initialize the tile map 
        '''

        self._image_surf = image_surf
        self._display_surf = display_surf
        self._weight = weight
        self._height = height

        self._tile_map_array = [[0,0,0,0,0,0,0,0,1,1], [1,1,0,0,0,1,1,0,1,1]]
        self._tile_map = []

        for row_index, row in enumerate(self._tile_map_array):
            tile_map_row = []
            for col_index, col in enumerate(row):
                if col == TileType.BRICK:
                    tile = Brick(TileState.INIT, self._image_surf, self._display_surf, self._weight, self._height, current_position_x=col_index*32, current_position_y=(row_index+1)*32)
                    tile_map_row.append(tile)
                else:
                    tile_map_row.append(None)

            self._tile_map.append(tile_map_row)

    def render(self):
        '''Render the tile image
        '''
        for row in self._tile_map:
            for col in row:
                if col is not None:
                    col.render()

    def get_all_tiles(self):
        '''Get all tiles, exception none
        '''
        flattened = [val for sublist in self._tile_map for val in \
                     sublist if val is not None ]

        return flattened

    def get_all_rects(self):
        '''Get rects for all tiles
        '''
        flattened = [val.get_rect() for sublist in self._tile_map for val in \
                     sublist if val is not None ]

        return flattened

    def check_tiles_by_hit_missile(self, collide_rect_indexs):
        if len(collide_rect_indexs) > 0:
            tiles = self.get_all_tiles()
            for collide_rect_index in collide_rect_indexs:
                tile = tiles[collide_rect_index]
                if tile.is_dead():
                    # Remove tile
                    self.remove_tile_by_id(tiles[collide_rect_index].get_id())
                else:
                    tile.change_state()
            return True
        else:
            return False

    def remove_tile_by_id(self, tile_id):
        for row in self._tile_map:
            for col in row:
                if col is not None:
                    if col.get_id() == tile_id:
                        row.remove(col)
