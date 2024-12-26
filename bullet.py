from circle import Circle

class Bullet(Circle):
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height, source=None):
        super().__init__(x, y, dx, dy, rotation, 3, world_width, world_height)
        self.mAge = 0  # Bullet's age in seconds
        self.mSource = source  # Source of the bullet (e.g., the ship)
        self.accelerate(100.0)  # Accelerate the bullet
        self.move(0.1)  # Move the bullet by 0.1 seconds of movement

    def getAge(self):
        """Returns the bullet's current age."""
        return self.mAge

    def setSource(self, source):
        """Sets the source of the bullet."""
        self.mSource = source

    def getSource(self):
        """Returns the source of the bullet."""
        return self.mSource

    def evolve(self, dt):
        """Moves the bullet and increases its age. Inactivates if it's older than 6 seconds."""
        # Move the bullet
        self.move(dt)

        # Increase the age by dt (time passed)
        self.mAge += dt

        # If the bullet is older than 6 seconds, mark it as inactive
        if self.mAge > 6:
            self.setActive(False)
