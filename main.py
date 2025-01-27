import pygame
from constants import *
from player import Player

def main():
    pygame.init() 
    lets_go = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    delta_time = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
     
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    while lets_go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        delta_time = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()