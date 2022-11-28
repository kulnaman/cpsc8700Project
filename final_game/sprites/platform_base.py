import pygame as pg
from settings import *
import Vector
vec = Vector.Vec2d

class Platform_base(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos,width,height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Assets/brick.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
