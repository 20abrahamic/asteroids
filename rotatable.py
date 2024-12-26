from movable import Movable
from math import cos, sin, radians


class Rotatable(Movable):
   def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
       super(). __init__(x, y, dx, dy, world_width, world_height)
       self.mRotation = rotation
       return
  
   def getRotation(self):
       return self.mRotation
  
   def rotate(self, delta_rotation):
       self.mRotation = (self.mRotation + delta_rotation) % 360
       return
  
   def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
       angle_rad = radians(rotation)
       return delta_velocity * cos(angle_rad), delta_velocity * sin(angle_rad)
  
   def accelerate(self, delta_velocity):
       delta_x, delta_y = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
       self.mDX += delta_x
       self.mDY += delta_y
       return
      
   def rotatePoint(self, x, y):
       angle_rad = radians(self.mRotation)
    
       return (x * cos(angle_rad) - y * sin(angle_rad), x * sin(angle_rad) + y * cos(angle_rad))


  
   def translatePoint(self, x, y):
       return x + self.mX, y + self.mY
  
   def rotateAndTranslatePoint(self, x, y):
       x_rot, y_rot = self.rotatePoint(x, y)
       return self.translatePoint(x_rot, y_rot)
  
   def rotateAndTranslatePointList(self, point_list):
       return [self.rotateAndTranslatePoint(x, y) for x, y in point_list]