import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        if self.timer < 0:
            self.timer = 0

        keys = pygame.key.get_pressed()

        # go left
        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        
        # go right
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # go forward
        if keys[pygame.K_w]:
            self.move(dt)
        
        # go backwards
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        directional_unit_vector = pygame.math.Vector2(0, 1).rotate(self.rotation)
        self.position += directional_unit_vector * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer == 0:
            new_shot = Shot(self.position.x, self.position.y)
            new_shot.velocity = pygame.math.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOT_COOLDOWN    
        