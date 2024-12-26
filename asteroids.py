from movable import Movable
from polygon import Polygon
from rock import Rock
from rotatable import Rotatable
from ship import Ship
from star import Star
from bullet import Bullet
import pygame
import random


class Asteroids:
    def __init__(self, world_width, world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = Ship(world_width // 2, world_height // 2, world_width, world_height)
        self.mRocks = [Rock(random.randint(0, world_width), random.randint(0, world_height), world_width, world_height)
                       for i in range(10)]
        self.mStars = [Star(random.randint(0, world_width), random.randint(0, world_height), world_width, world_height)
                       for i in range(20)]
        self.mBullets = []
        self.mObjects = [self.mShip] + self.mRocks + self.mStars + self.mBullets

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getShip(self):
        return self.mShip

    def getRocks(self):
        return self.mRocks

    def getBullets(self):
        return self.mBullets

    def getStars(self):
        return self.mStars

    def getObjects(self):
        return self.mObjects

    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
        return

    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
        return

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
        return

    def fire(self):
        if self.mShip.getActive() and len(self.mBullets) < 3:
            new_bullet = self.mShip.fire()
            new_bullet.setSource(self.mShip)  # Tag the bullet with its source
            self.mBullets.append(new_bullet)
            self.mObjects.append(new_bullet)
        return

    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)
        return

    def collideShipAndBullets(self):
        if self.mShip.getActive():
            for bullet in self.mBullets:
                # Exclude bullets fired by the ship and bullets in their grace period
                if bullet.getActive() and bullet.hits(self.mShip) and bullet.getSource() != self.mShip and bullet.getAge() > 0.1:
                    self.mShip.setActive(False)
                    bullet.setActive(False)
        return

    def collideShipAndRocks(self):
        if self.mShip.getActive():
            for rock in self.mRocks:
                if rock.getActive() and rock.hits(self.mShip):
                    self.mShip.setActive(False)
                    rock.setActive(False)
        return

    def collideRocksAndBullets(self):
        for bullet in self.mBullets:
            if bullet.getActive():
                for rock in self.mRocks:
                    if rock.getActive() and rock.hits(bullet):
                        rock.setActive(False)
                        bullet.setActive(False)
                        break
        return

    def removeInactiveObjects(self):
        # Create temporary list for active objects
        active_objects = []

        # Filter for only active objects
        for obj in self.mObjects:
            if obj.getActive():
                active_objects.append(obj)

        # Update main objects list
        self.mObjects = active_objects

        # Clean up specific type lists
        self.mBullets = [bullet for bullet in self.mBullets if bullet.getActive()]
        self.mRocks = [rock for rock in self.mRocks if rock.getActive()]

        return

    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.collideRocksAndBullets()
        self.removeInactiveObjects()
        return

    def draw(self, surface):
        for obj in self.mObjects:
            if obj.getActive():
                obj.draw(surface)
