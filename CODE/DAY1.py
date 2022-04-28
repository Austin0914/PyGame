from turtle import width
import pygame

run_jud=True
FPS=60
WIDTH=600
HEIGHT=600

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption("Pygame!!!!!!!!")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
    
    def update(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x+=10
        if key_pressed[pygame.K_LEFT]:
            self.rect.x-=10
        self.rect.y +=10
        if(self.rect.y>=HEIGHT):
            self.rect.y=0
        if(self.rect.right>WIDTH):
            self.rect.right=WIDTH
        if(self.rect.left<0):
            self.rect.left=0

all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)

while run_jud:
    clock.tick(FPS)
    for event in pygame.event.get(): #return all the event in screen
        if event.type==pygame.QUIT:
            run_jud =False
    
    all_sprites.update()

    screen.fill((100,100,100))
    all_sprites.draw(screen)
    pygame.display.update()
