import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        new1 = Asteroid(self.position.x, self.position.y, newRadius)
        new2 = Asteroid(self.position.x, self.position.y, newRadius)
        new1.velocity = vector1 * 1.2
        new2.velocity = vector2 * 1.2
        