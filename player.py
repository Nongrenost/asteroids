import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    attack_timer = 0 
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time
        
    
    def update(self, delta_time):
        self.key_handler(delta_time)
        self.attack_timer_tick(delta_time)
            
    def key_handler(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time
        
    def shoot(self):
        if self.can_shoot():
            _velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            Shot(self.position.x, self.position.y, _velocity)
                            
            self.reset_attack_cooldown()
                
    def can_shoot(self):
        return self.attack_timer < 0
    
    
    def reset_attack_cooldown(self):
        self.attack_timer = PLAYER_SHOOT_COOLDOWN
        
    def attack_timer_tick(self, delta_time):
        self.attack_timer -= delta_time
    
    