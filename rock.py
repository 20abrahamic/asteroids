from polygon import Polygon
import random
from math import cos, sin, radians, pi


class Rock(Polygon):
   def __init__(self, x, y, world_width, world_height, radius=20, num_points=8):
       super().__init__(x, y, 0, 0, random.uniform(0, 359.9), world_width, world_height)
       self.mSpinRate = random.uniform(-90, 90)
       self.setPolygon(self.createRandomPolygon(radius, num_points))
       self.accelerate(random.uniform(10, 20))


   def getSpinRate(self):
       return self.mSpinRate
  
   def setSpinRate(self, spin_rate):
       if spin_rate < 0:
           self.mSpinRate = spin_rate  # Set directly, even if negative
       self.mSpinRate = spin_rate  # Correct attribute to set


  
   def createRandomPolygon(self, radius, num_points):
       angle_increment = 2 * pi / num_points  # Ensure equal angular spacing
       points = []


       for i in range(num_points):
           angle = i * angle_increment
           r = random.uniform(0.7, 1.3) * radius  # Randomized distance
           x = r * cos(angle)
           y = r * sin(angle)
           points.append((x, y))


       return points
  
   def evolve(self, dt):
       self.move(dt)
       self.rotate(self.mSpinRate * dt)