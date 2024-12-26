import pygame
from rotatable import Rotatable


class Circle(Rotatable):
   def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
       # Call the parent (Rotatable) class constructor
       super().__init__(x, y, dx, dy, rotation, world_width, world_height)
      
       self.mRadius = radius
       self.mColor = (255,255,255)  # Default color is white


   def getRadius(self):
       return self.mRadius
  
   def getColor(self):
       return self.mColor
  
   def setRadius(self, radius):
       """Sets the circle's radius, ensuring it's at least 1."""
       if radius >= 1:
           self.mRadius = radius
       
   def setColor(self, color):
       self.mColor = color
  
   def draw(self, surface):
       """Draws the circle on the given surface."""
       # Draw the circle using pygame.draw.circle
       pygame.draw.circle(surface, self.mColor, (self.mX, self.mY), self.mRadius)
