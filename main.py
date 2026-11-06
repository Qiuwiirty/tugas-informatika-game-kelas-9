import pygame
# Tugas kls 9 buat program... (game tembak tembah mungkin)
from pygame.math import Vector2
pygame.init()

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
while running:
    #ini kode hanya untuk tutup game nya saat udah selesai..,
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
pygame.quit()