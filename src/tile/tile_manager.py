from tile import Brick
from entities.enum import TileState
from entities.enum import TileType

class TileManager(object):
    def __init__(self, image_surf, display_surf, weight, height):
        self._image_surf = image_surf
        self._display_surf = display_surf
        self._weight = weight
        self._height = height

        self._tile_map_array = [[1,1,0,1,1,1,1,0,1,1], [1,1,0,1,1,1,1,0,1,1]]
        self._tile_map = []

        for row_index, row in enumerate(self._tile_map_array):
            tile_map_row = []
            for col_index, col in enumerate(row):
                if col == TileType.BRICK:
                    tile_map_row.append(Brick(TileState.INIT, self._image_surf, self._display_surf, self._weight, self._height, current_position_x=col_index*32, current_position_y=(row_index+1)*32))
                else:
                    tile_map_row.append(None)

            self._tile_map.append(tile_map_row)

    def render(self):
        for row in self._tile_map:
            for col in row:
                if col is not None:
                    col.render()
