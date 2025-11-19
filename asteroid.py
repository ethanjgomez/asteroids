from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        vecA = self.velocity.rotate(angle)
        vecB = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y

        newA = Asteroid(x, y, radius)
        newB = Asteroid(x, y, radius)

        newA.velocity = vecA * 1.2
        newB.velocity = vecB * 1.2
