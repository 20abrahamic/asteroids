from polygon import Polygon
from bullet import Bullet
import math


class Ship(Polygon):
    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        self.setPolygon([(-10, -10), (20, 0), (-10, 10)])  # Define the ship's shape

    def fire(self):
        # Get the tip of the ship (first point in the polygon)
        ship_point = self.mOriginalPolygon[0]
        
        # Transform the point based on the ship's rotation and position
        transformed_point = self.rotateAndTranslatePointList([ship_point])[0]
        
        # Offset the bullet slightly forward from the ship's tip
        offset_distance = 10  # Adjust as needed
        bullet_x = transformed_point[0] + math.cos(math.radians(self.mRotation)) * offset_distance
        bullet_y = transformed_point[1] + math.sin(math.radians(self.mRotation)) * offset_distance

        # Create and return the bullet
        bullet = Bullet(bullet_x, bullet_y, self.mDX, self.mDY, self.mRotation, self.mWorldWidth, self.mWorldHeight)
        return bullet

    def evolve(self, dt):
        self.move(dt)
