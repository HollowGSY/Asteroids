# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    #Initialize pygame
    pygame.init()

    #Restrict FPS
    clock = pygame.time.Clock()
    dt = 0

    #Create rendering groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    #Set up screen (width, height)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Set the window title
    pygame.display.set_caption("Asteroids")
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game loop
    while True:
        #handle the quit event so you can close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(asteroid):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")

        #allow the player to rotate
        
        # Draw the player
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()