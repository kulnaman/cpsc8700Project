import pygame as pg
from pytmx.util_pygame import load_pygame

from Const import *

class Map(object):
    """
    This class contains every map object. We are loading all the characters and sprites in it.
    """

    def __init__(self,world_num):
        self.mapSize=(0,0)
        self.sky = 0
        self.map = 0
        self.textures = {}

    def loadWorld(self):
        
        #Loading map data using pytmx
        
        tmx_data = load_pygame("assets/level_5.tmx")
        
        # setting mapsize
        
        self.mapSize = (tmx_data.width,tmx_data.height)
        
        # setting sky property

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#5c94fc')))
        
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        
        for layer in tmx_data.visible_layers:
            
            for y in range(tmx_data.height):
                
                for x in range(tmx_data.width):
                    
                    # Getting pygame surface

                    image = tmx_data.get_tile_image(x, y, layer_num)
                    

