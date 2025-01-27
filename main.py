import pygame
import pygame
from constants import *

def main():
    pygame.init() 
    game_time = pygame.time.Clock()
    delta_time = 0
    
     
    lets_go = True
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while lets_go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        delta_time = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()