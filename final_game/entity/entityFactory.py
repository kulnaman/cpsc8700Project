from entity.wall import *
from entity.platform import *
from entity.platform_base import *
class EntityFactory:
    def __init__(self,posX,posY,width,height):
        self.x = posX
        self.y = posY
        self.w = width
        self.h = height

    def getSolidObject(self,typeSolid:str):
        if typeSolid == "Platform":
            return Platform(self.x,self.y,self.w,self.h)
        elif typeSolid == "Wall":
            return Wall(self.x,self.y,self.w,self.h)
        elif typeSolid == "Base":
            return Platform_base(self.x,self.y,self.w,self.h)

