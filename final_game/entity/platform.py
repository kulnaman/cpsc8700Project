import pygame as pg
from src.settings import *
from src.Vector import *
vec = Vec2d

class Platform(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
