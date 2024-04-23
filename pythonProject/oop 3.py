import pygame
from pygame.sprite import Sprite


class GameSprite(Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.image.load(player_image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        elif keys[pygame.K_RIGHT] and self.rect.x < 700:
            self.rect.x += self.speed

        elif keys[pygame.K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed


hero = Hero('ship.jpg', 350, 400, 60, 40, 10)

window = pygame.display.set_mode((700, 500))

background = pygame.image.load("145.jpg")
background = pygame.transform.scale(background, (700, 500))

clock = pygame.time.Clock()

game = True
while game:
    window.blit(background, (0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game = False
    hero.update()
    hero.show()
    pygame.display.update()
    clock.tick(60)
