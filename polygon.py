from rotatable import Rotatable
import math
import pygame


class Polygon(Rotatable):
   def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
       super().__init__(x, y, dx, dy, rotation, world_width, world_height)
       self.mOriginalPolygon = []
       self.mColor = (255, 255, 255)  # Default white color


   def getPolygon(self):
       return self.mOriginalPolygon


   def getColor(self):
       return self.mColor
  
   def getRadius(self):
       if not self.mOriginalPolygon:
           return 0
      
       total_distance = 0
      
       for (x,y) in self.mOriginalPolygon:
           distance = math.sqrt(x**2 + y**2)
           total_distance += distance
          
       return total_distance / len(self.mOriginalPolygon)


   def setPolygon(self, point_list):
       self.mOriginalPolygon = point_list


   def setColor(self, color):
       self.mColor = color


   def draw(self, surface):
       transformed_polygon = self.rotateAndTranslatePointList(self.mOriginalPolygon)
       pygame.draw.polygon(surface, self.mColor, transformed_polygon)