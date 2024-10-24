import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for updatables in updatable:
            updatables.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()