import pygame
# Tugas kls 9 buat program... (game tembak tembah mungkin)
from pygame.math import Vector2
from enum import Enum
pygame.init()
class EnemyType(Enum):
    SQUARE = 0
    CIRCLE = 1
class Enemy:
    def __init__(self, x: float, y: float, health: int, type: EnemyType):
        self.pos = Vector2(x, y)
        self.health = health
        self.type = type
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
enemies = [Enemy(10, 10, 1, EnemyType.CIRCLE)]
running = True
player_img = pygame.image.load("itsanarrow.png").convert_alpha() #bentuknya kayak arrow
player_pos = Vector2(0, 0) #sebenarnya tidak kasih gerak posisi player tapi semuanya
while running:
    #ini kode hanya untuk tutup game nya saat udah selesai..,
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    #region Input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y += 10
    if keys[pygame.K_s]:
        player_pos.y -= 10
    if keys[pygame.K_a]:
        player_pos.x += 10
    if keys[pygame.K_d]:
        player_pos.x -= 10
    #endregion

    #region Rendering nya
    #musuh nya
    for enemy in enemies:
        match enemy.type:
            case EnemyType.CIRCLE:
                pygame.draw.circle(screen, "white", enemy.pos + player_pos, 30.0)
            case EnemyType.SQUARE:
                pygame.draw.rect(screen, "white", (enemy.pos.x - 15 + player_pos.x, enemy.pos.y - 15 + player_pos.y, 30.0, 30.0))

    new_player_img = pygame.transform.rotate(player_img, 0)
    new_rect = new_player_img.get_rect(center=(328, 328)) #328 dari 360 - 32. why get_rect()? karena wobble-wobble dikit entah napa
    screen.blit(new_player_img, new_rect)
    #endregion
    pygame.display.flip()
    clock.tick(60)
pygame.quit()