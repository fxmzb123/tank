import pygame

from entities import base

class Board(base.Base):
    def set_number(self, number):
        self._number = number

    def get_number(self):
        return self._number

class GreenTankBoard(Board):
    '''Board class for green tank
    '''
    def __init__(self, direction, image_surf, display_surf, screen_width, screen_height, current_position_x = 0, current_position_y = 0):

        self.set_image_x(363)
        self.set_image_y(33)

        self.set_number(3)

        super(GreenTankBoard, self).__init__(direction, image_surf, display_surf, screen_width, screen_height, None, current_position_x=current_position_x, current_position_y=current_position_y)

    def render(self):
        super(GreenTankBoard, self).render()

        font = pygame.font.Font(None, 16)
        text = font.render(str(self.get_number()), 1, (255, 255, 255))
        if self.get_number() > 9:
            self._display_surf.blit(text, (335, 130))
        else:
            self._display_surf.blit(text, (337, 130))

class BlueTankBoard(Board):
    '''Board class for blue tank
    '''
    def __init__(self, direction, image_surf, display_surf, screen_width, screen_height, current_position_x = 0, current_position_y = 0):

        self.set_image_x(396)
        self.set_image_y(33)

        super(BlueTankBoard, self).__init__(direction, image_surf, display_surf, screen_width, screen_height, None, current_position_x=current_position_x, current_position_y=current_position_y)

    def render(self):
        super(BlueTankBoard, self).render()
