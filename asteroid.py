from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, delta_time):
        self.position += self.velocity * delta_time
        
    def split(self):
        self.kill()     
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_random_angle = random.uniform(20, 50)
        
        split_first_velocity = self.velocity.rotate(new_random_angle)
        split_second_velocity = -split_first_velocity
        split_size = self.radius - ASTEROID_MIN_RADIUS
        split_speed_increase = 1.2
        
        Asteroid(self.position.x, self.position.y, split_size).velocity = split_first_velocity * split_speed_increase 
        Asteroid(self.position.x, self.position.y, split_size).velocity = split_second_velocity * split_speed_increase