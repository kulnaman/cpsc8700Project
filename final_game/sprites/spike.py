
import pygame as pg
from settings import *
import Vector
vec = Vector.Vec2d





class Spikes(pg.sprite.Sprite):
    def __init__(self,x_pos,y_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Assets/spike.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

