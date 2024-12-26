import math
class Movable:
   def __init__(self,x,y,dx,dy,world_width,world_height):
       self.mX = x
       self.mY = y
       self.mDX = dx
       self.mDY = dy
       self.mWorldWidth = world_width
       self.mWorldHeight = world_height
       self.mActive = True
      
       return
      
   def getX(self):
       return self.mX
      
   def getY(self):
       return self.mY
      
   def getDX(self):
       return self.mDX
      
   def getDY(self):
       return self.mDY
      
   def getWorldWidth(self):
       return self.mWorldWidth
      
   def getWorldHeight(self):
       return self.mWorldHeight
  
   def getActive(self):
       return self.mActive
  
   def setActive(self, active):
       self.mActive = active
  
   def hits(self, other):
       d = math.sqrt((self.mX - other.getX()) **2 + (self.mY - other.getY()) **2)
       total_radius = self.getRadius() + other.getRadius()
      
       if d <= total_radius:
           return True
       else:
           return False
      
   def move(self, dt):
       self.mX = (self.mX + self.mDX * dt) % self.mWorldWidth
       self.mY = (self.mY + self.mDY * dt) % self.mWorldHeight
      
       return
  
   def getRadius(self):
       raise NotImplementedError("Child must implement getRadius method")
   def accelerate(self, delta_velocity):
       raise NotImplementedError("Child must implement accelerate method")
   def evolve(self, dt):
       raise NotImplementedError("Child must implement evolve method")
   def draw(self, surface):
       raise NotImplementedError("Child must implement draw method")