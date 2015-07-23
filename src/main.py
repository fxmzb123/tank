import os
import sys

import pygame
from pygame.locals import *

from entities.tank import *
from entities.missile import *
from entities.enum import *
from system.keyqueue import *
from tile.tile import *
from tile.tile_manager import TileManager

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 320, 384
        self.background_color = (0,0,0)
        self._image_surf = None
        self._image_name = "tankbrigade.bmp"
                
    def on_init(self):
        
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tank Brigade')
        self._display_surf.fill(self.background_color);

        self._image_surf = pygame.image.load( os.path.join(os.path.dirname(__file__), "images", self._image_name) ).convert()
        
        green_tank_image_X_Y={}
        green_tank_image_X_Y[enum.Sprite.UP] = {"x":528, "y":33}
        green_tank_image_X_Y[enum.Sprite.DOWN] = {"x":528, "y":66}
        green_tank_image_X_Y[enum.Sprite.RIGHT] = {"x":528, "y":99}
        green_tank_image_X_Y[enum.Sprite.LEFT] = {"x":561, "y":132}
        
        blue_tank_image_X_Y={}
        blue_tank_image_X_Y[enum.Sprite.UP] = {"x":528, "y":330}
        blue_tank_image_X_Y[enum.Sprite.DOWN] = {"x":528, "y":363}
        blue_tank_image_X_Y[enum.Sprite.RIGHT] = {"x":726, "y":132}
        blue_tank_image_X_Y[enum.Sprite.LEFT] = {"x":693, "y":132}
        
        self._tank = Tank(Sprite.LEFT, self._image_surf, self._display_surf, self.weight, self.height, green_tank_image_X_Y, current_position_x=0, current_position_y=352)        
        
        self._blue_tanks = []
        for i in range(3):
            self._blue_tanks.append(Tank(Sprite.DOWN, self._image_surf, self._display_surf, self.weight, self.height, blue_tank_image_X_Y, current_position_x=(i*144), current_position_y=0))

        self._running = True
        
        self._tile_manager = TileManager(self._image_surf, self._display_surf, self.weight, self.height)
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
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
                self.fire_missile()
                KeyQueue.pursh_key(Key.FIRE)
            
            #if (pygame.key.get_pressed()[K_UP] and pygame.key.get_pressed()[K_SPACE]):
            #    self.fire_missile()
            #    self._tank.set_up()
        
        elif event.type == pygame.KEYUP:
            
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
                
        missile = Missile(self._tank.get_direction(), self._image_surf, self._display_surf, self.weight, self.height, None, 5, current_position_x=missile_position['x'], current_position_y=missile_position['y'])
        missile.set_is_move_allowed(True, self._tank.get_direction())
        self._tank.add_missile(missile)
                
    def on_update(self):
        self._tank.move()
        
        print self._tile_manager.is_collide(self._tank.get_rect())
        
        for blue_tank in self._blue_tanks:
            blue_tank.move()
                
        for missile in self._tank.get_missiles():
            if missile:
                if missile.is_touched_border():
                    self._tank.get_missiles().remove(missile)
                else: 
                    missile.move()

    def on_render(self):
        self._display_surf.fill(self.background_color);
        
        #self._display_surf.blit(self._image_surf,(0,0), (561,132,32,32))
        self._tank.render()
        
        for missile in self._tank.get_missiles():
            if missile:
                missile.render()
        
        for blue_tank in self._blue_tanks:
            blue_tank.render()
        
        self._tile_manager.render()
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
            
            self.on_update()
            self.on_render()
            
            pygame.time.Clock().tick(30)

        self.on_cleanup()
        sys.exit(0)

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
