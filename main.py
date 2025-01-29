import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (updatable)

    lets_go = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    delta_time = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
    


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    asteroid_field = AsteroidField()
    while lets_go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(delta_time)   
             
        screen.fill("black")

        for item in drawable:
            item.draw(screen)  
             
        pygame.display.flip()
       
        # framerate lock to 60 
        delta_time = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()  