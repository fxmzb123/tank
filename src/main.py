import os
import sys

from sets import Set

import pygame
from pygame.locals import *

from entities.tank import *
from entities.missile import *
from entities.enum import *
from entities.fire import *
from system.keyqueue import *
from tile.tile_manager import TileManager
from system import utils
from entities.board import GreenTankBoard
from entities.board import BlueTankBoard

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.weight, self.height = 320, 384
        self.size = (self.weight + 36, self.height)
        self.background_color = (0,0,0)
        self._image_surf = None
        self._image_name = "tankbrigade.bmp"
        self._collision_direction = []

    def on_init(self):

        pygame.init()

        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tank Brigade')
        self._display_surf.fill(self.background_color)
        self._image_surf = pygame.image.load( os.path.join(os.path.dirname(__file__), "images", self._image_name) ).convert()
        
        # This is for green tank
        self._total_number_of_tanks = 3
        # This is for blue tanks
        self._batch_number = 3
        self._total_blue_tanks = 20
        
        self._delay_index = 0
        self._delay_index_blue_tank = 0

        self._tank = self.get_new_green_tank()

        self._blue_tanks = []
        self._green_tank_batch_set = Set()

        for i in range(self._batch_number):
            self._blue_tanks.append(self.get_new_blue_tank(i))
            self._green_tank_batch_set.add(i)

        self._total_blue_tanks = self._total_blue_tanks - self._batch_number

        self._running = True

        self._tile_manager = TileManager(self._image_surf, self._display_surf, self.weight, self.height)

        self._fire_list = []

        self._green_tank_board = GreenTankBoard(None, self._image_surf, self._display_surf, self.size[0], self.size[1], current_position_x = 324, current_position_y = 100)
        self._blue_tank_board = BlueTankBoard(None, self._image_surf, self._display_surf, self.size[0], self.size[1], current_position_x = 324, current_position_y = 150)

        self._show_welcome = True
        
        utils.Utils.draw_text_on_screen(self._display_surf, "Tank Brigade", 36, (255,255,255), (100,100))
        utils.Utils.draw_text_on_screen(self._display_surf, "Press space to start", 26, (255,255,255), (100,160))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if self._tank:

                if event.key == pygame.K_UP:
                    self._tank.set_up()
                    KeyQueue.pursh_key(Key.UP)

                if event.key == pygame.K_DOWN:
                    self._tank.set_down()
                    KeyQueue.pursh_key(Key.DOWN)

                if event.key == pygame.K_LEFT:
                    self._tank.set_left()
                    KeyQueue.pursh_key(Key.LEFT)

                if event.key == pygame.K_RIGHT:
                    self._tank.set_right()
                    KeyQueue.pursh_key(Key.RIGHT)

                if event.key == pygame.K_SPACE:
                    if self._show_welcome:
                        self._show_welcome = False

                    self.fire_missile()
                    KeyQueue.pursh_key(Key.FIRE)

            #if (pygame.key.get_pressed()[K_UP] and pygame.key.get_pressed()[K_SPACE]):
            #    self.fire_missile()
            #    self._tank.set_up()
        
        elif event.type == pygame.KEYUP:
            if self._tank:
                if event.key == pygame.K_UP:
                    self._tank.set_is_move_allowed(False, enum.Sprite.UP)
                    KeyQueue.remove_key(Key.UP)

                if event.key == pygame.K_DOWN:
                    self._tank.set_is_move_allowed(False, enum.Sprite.DOWN)
                    KeyQueue.remove_key(Key.DOWN)

                if event.key == pygame.K_LEFT:
                    self._tank.set_is_move_allowed(False, enum.Sprite.LEFT)
                    KeyQueue.remove_key(Key.LEFT)

                if event.key == pygame.K_RIGHT:
                    self._tank.set_is_move_allowed(False, enum.Sprite.RIGHT)
                    KeyQueue.remove_key(Key.RIGHT)

    def fire_missile(self):
        missile_position = self._tank.get_missile_position()
                
        missile = Missile(self._tank.get_direction(), self._image_surf, self._display_surf, self.weight, self.height, None, 5, current_position_x=missile_position['x'], current_position_y=missile_position['y'], offset=14)
        missile.set_is_move_allowed(True, self._tank.get_direction())
        self._tank.add_missile(missile)

    def get_new_blue_tank(self, index):
        blue_tank_image_X_Y={}
        blue_tank_image_X_Y[enum.Sprite.UP] = {"x":528, "y":330}
        blue_tank_image_X_Y[enum.Sprite.DOWN] = {"x":528, "y":363}
        blue_tank_image_X_Y[enum.Sprite.RIGHT] = {"x":726, "y":132}
        blue_tank_image_X_Y[enum.Sprite.LEFT] = {"x":693, "y":132}
        
        blue_tank = Tank(Sprite.DOWN, self._image_surf, self._display_surf, self.weight, self.height, blue_tank_image_X_Y, current_position_x=(index*144), current_position_y=0)
        blue_tank.set_batch_index(index)
        
        return blue_tank
            
    def get_new_green_tank(self):
        green_tank_image_X_Y={}
        green_tank_image_X_Y[enum.Sprite.UP] = {"x":528, "y":33}
        green_tank_image_X_Y[enum.Sprite.DOWN] = {"x":528, "y":66}
        green_tank_image_X_Y[enum.Sprite.RIGHT] = {"x":528, "y":99}
        green_tank_image_X_Y[enum.Sprite.LEFT] = {"x":561, "y":132}

        green_tank = Tank(Sprite.UP, self._image_surf, self._display_surf, self.weight, self.height, green_tank_image_X_Y, current_position_x=100, current_position_y=352)        

        return green_tank

    def on_update(self):

        if self._tank is None:
            if self._delay_index == 50:
                self._delay_index = 0
                self._tank = self.get_new_green_tank()
            else:
                self._delay_index = self._delay_index +1

        tile_rects = self._tile_manager.get_all_rects()
        tiles = self._tile_manager.get_all_tiles()

        blue_tank_rects = []

        for blue_tank in self._blue_tanks:
            blue_tank_rects.append(blue_tank.get_rect())
            blue_tank.fire_missile_randomly()

            for missile in blue_tank.get_missiles():
                if missile.is_touched_border():
                    blue_tank.get_missiles().remove(missile)
                else:
                    allow_missile_move = False
                    # Check collision with tiles
                    collide_rect_indexs = utils.Utils.get_collide_indexes(missile.get_rect(), tile_rects)
                    
                    result = self._tile_manager.check_tiles_by_hit_missile(collide_rect_indexs)

                    if result:
                        blue_tank.get_missiles().remove(missile)

                    if self._tank:
                        # Check missile collision
                        tank_missiles = self._tank.get_missiles()
                        tank_missile_rects = [tank_missile.get_rect() for tank_missile in tank_missiles]
                        collide_rect_indexs = utils.Utils.get_collide_indexes(missile.get_rect(), tank_missile_rects)
                        
                        if len(collide_rect_indexs) > 0:
                            self._tank.remove_missiles(collide_rect_indexs)
                            blue_tank.get_missiles().remove(missile)
                            missile = None

                        if missile:
                            # Do missile collision detection
                            collide_rect_indexs = utils.Utils.get_collide_indexes(missile.get_rect(), [self._tank.get_rect()])
    
                            if len(collide_rect_indexs) > 0:
                                blue_tank.get_missiles().remove(missile)
    
                                index = collide_rect_indexs[0]
                                fire = Fire(FireState.FIRST, self._image_surf, self._display_surf, self.weight, self.height, current_position_x=self._tank.get_current_position_x(), current_position_y=self._tank.get_current_position_y())
                                self._fire_list.append(fire)                       
    
                                self._total_number_of_tanks = self._total_number_of_tanks - 1
                                self._green_tank_board.set_number(self._total_number_of_tanks)
                                self._tank = None
    
                                if self._total_number_of_tanks == 0:
                                    self._running = False
    
                            else:
                                allow_missile_move = True                    
                    else:
                        allow_missile_move = True

                    if allow_missile_move:
                        if missile:
                            missile.move()

        for index, blue_tank in enumerate(self._blue_tanks):

            other_blue_tank_rects = blue_tank_rects[:index] + blue_tank_rects[(index + 1):]

            other_blue_tank_rects.extend(tile_rects)
            if self._tank:
                other_blue_tank_rects.append(self._tank.get_rect())

            blue_tank.set_move_direction(blue_tank.get_random_direction())

            allow_move = blue_tank.is_allow_move(other_blue_tank_rects)

            if allow_move:
                blue_tank.move()

        if self._tank:
            other_object_rects = []

            other_object_rects.extend(blue_tank_rects)
            other_object_rects.extend(tile_rects)
            allow_move = self._tank.is_allow_move(other_object_rects)

            if allow_move:
                self._tank.move()

            for missile in self._tank.get_missiles():
                if missile:
                    if missile.is_touched_border():
                        self._tank.get_missiles().remove(missile)
                    else:
                        # Do missile detection with tiles
                        collide_rect_indexs = utils.Utils.get_collide_indexes(missile.get_rect(), tile_rects)

                        result = self._tile_manager.check_tiles_by_hit_missile(collide_rect_indexs)

                        if result:
                            # Remove missile
                            self._tank.get_missiles().remove(missile)

                        # Do missile collision detection
                        collide_rect_indexs = utils.Utils.get_collide_indexes(missile.get_rect(), blue_tank_rects)

                        if len(collide_rect_indexs) > 0:
                            index = collide_rect_indexs[0]
                            fire = Fire(FireState.FIRST, self._image_surf, self._display_surf, self.weight, self.height, current_position_x=self._blue_tanks[index].get_current_position_x(), current_position_y=self._blue_tanks[index].get_current_position_y())

                            self._fire_list.append(fire)               
                            del self._blue_tanks[index]
                            self._tank.get_missiles().remove(missile)                        
                        else:
                            missile.move()

        # We check if number of blue tanks is less than the batch number
        if len(self._blue_tanks) < self._batch_number:
            if self._total_blue_tanks > 0:
                if self._delay_index_blue_tank == 50:
                    self._delay_index_blue_tank = 0

                    missing_index = self.get_missing_index()

                    for index in missing_index:
                        self._blue_tanks.append(self.get_new_blue_tank(index))
                        self._total_blue_tanks = self._total_blue_tanks -1

                        if self._total_blue_tanks == 0:
                            break
                else:
                    self._delay_index_blue_tank = self._delay_index_blue_tank +1

        self._blue_tank_board.set_number(self._total_blue_tanks)
        
    def get_missing_index(self):
        blue_tank_index_set = Set()

        for tank in self._blue_tanks:
            blue_tank_index_set.add(tank.get_batch_index())

        return list(self._green_tank_batch_set - blue_tank_index_set)

    def on_render(self):
        self._display_surf.fill(self.background_color);

        for blue_tank in self._blue_tanks:
            for missile in blue_tank.get_missiles():
                if missile:
                    missile.render()

        #self._display_surf.blit(self._image_surf,(0,0), (561,132,32,32))
        if self._tank:
            self._tank.render()

            for missile in self._tank.get_missiles():
                if missile:
                    missile.render()

        for blue_tank in self._blue_tanks:
            blue_tank.render()

        self._tile_manager.render()
        
        for fire in self._fire_list:
            fire.render()

        pygame.draw.line(self._display_surf, pygame.Color(125, 125, 125), (322, 0), (322, 384), 3)

        self._green_tank_board.render()
        self._blue_tank_board.render()

        pygame.display.flip()
    
    def on_cleanup(self):
        pygame.display.quit()
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)

            if not self._show_welcome:
                self.on_update()
                self.on_render()

            pygame.time.Clock().tick(30)

        self.on_cleanup()
        sys.exit(0)

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
