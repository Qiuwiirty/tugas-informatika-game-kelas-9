import pygame
# Tugas kls 9 buat program... (game tembak tembah mungkin)
from pygame.math import Vector2
pygame.init()

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
player_img = pygame.image.load("itsanarrow.png").convert_alpha() #bentuknya kayak arrow
while running:
    #ini kode hanya untuk tutup game nya saat udah selesai..,
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    screen.blit(player_img, (328, 328)) #328 dari 360 - 32
    pygame.display.flip()
    clock.tick(60)
pygame.quit()