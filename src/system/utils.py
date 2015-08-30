import uuid

import pygame

from operator import itemgetter

class Utils(object):
    @classmethod
    def get_uuid(cls):
        return uuid.uuid4()

    @classmethod
    def get_collide_indexes(cls, rect, rects):
        ''' Return index of a collided rect in a list
        '''
        collision_rects_index = rect.collidelistall(rects)
        return collision_rects_index

    @classmethod
    def is_collide(cls, rect, rects):
        '''To test whether the provided rect has collision with any of the
        rect in rects
        '''
        collision_rects_index = rect.collidelistall(rects)
        collision_rects = []

        if len(collision_rects_index) > 0:
            value = itemgetter(*collision_rects_index)(rects)

            if isinstance(value, tuple):
                collision_rects = list(value)
            else:
                collision_rects.append(value)
            return collision_rects
        else:
            return []

    @classmethod
    def draw_text_on_screen(cls, display_surf, text, size, color, position):
        font = pygame.font.Font(None, size)
        text_to_display = font.render(text, 1, color)

        display_surf.blit(text_to_display, position)
        pygame.display.flip()
