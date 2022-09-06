import pygame
import time
from sys import exit

pygame.init()
size = (800,400)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
FPS = 60
pygame.display.set_caption('Runner')
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# test_surface = pygame.Surface((100,200))
# test_surface.fill('azure')

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
#render('text',anti-alliasing (True/False), color)
text_surface = test_font.render('My game',False,'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600
snail_speed = 2

#--- define game variables ---#
previous = time.time() * 1000
lag = 0.0
done = False
clock=pygame.time.Clock()

#--- game ---#
while True:

    #--- update time step ---#
    current = time.time() * 1000
    elapsed = current - previous
    lag += elapsed
    previous = current

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #screen.blit(surface,position)
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,280))
    screen.blit(text_surface,(300,50))
    snail_x_pos -=snail_speed
    if snail_x_pos <-100: snail_x_pos= 800
    screen.blit(snail_surface,(snail_x_pos,250))
    pygame.display.update()
    clock.tick(FPS)