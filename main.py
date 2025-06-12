# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Initialize pygame
    pygame.init()

    #Set up screen (width, height)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Set the window title
    pygame.display.set_caption("Asteroids")
    
    #Game loop
    while True:
        #handle the quit event so you can close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()