import pygame
import random
import time
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BG = pygame.Color("pink")
RED = pygame.Color("red")
ORANGE = pygame.Color("orange")
GREEN = pygame.Color("green")
YELLOW = pygame.Color("yellow")
class Sprite(pygame.sprite.Sprite): 
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
    def change_color(self):
            self.image.fill(random.choice([GREEN, ORANGE, RED, YELLOW]))
class Sprite2(pygame.sprite.Sprite): 
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
    def change_color(self):
            self.image.fill(random.choice([GREEN, ORANGE, RED, YELLOW]))
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(GREEN, 20, 30)
sp1.rect.x = (250)
sp1.rect.y = (170)
all_sprites_list.add(sp1)
sp2 = Sprite2(ORANGE, 20, 30)
sp2.rect.x = (200)
sp2.rect.y = (100)
all_sprites_list.add(sp2)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Sprites_Project")
bg_color = BG
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
            sp2.change_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()