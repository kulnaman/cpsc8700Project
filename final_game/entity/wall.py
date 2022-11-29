import pygame as pg
from src.settings import *
from src.Vector  import *
vec = Vec2d
class Wall(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,height))
        #self.image = pg.image.load('Assets/brick.jpg').convert()
        self.image.fill(BACKGROUND_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
