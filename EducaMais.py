import pygame
import sys

from Model.Boy import Boy

pygame.init()

width = 1824
height = 762

window = pygame.display.set_mode((width, height))
tempo = pygame.time.Clock()

background_image = pygame.image.load('Misc/Images/Background/yellow.jpg').convert_alpha()
background = pygame.transform.scale(background_image, (width, height))
pygame.display.set_caption("EducaMais")

boy = Boy()
herois = pygame.sprite.Group(boy)

while True:

    # window.blit(background, (0, 0))
    window.blit(background, background.get_rect(center=window.get_rect().center))

    herois.draw(window)
    # window.blit(boy,(200, 490))

    # Calcular regras
    herois.update()

    if boy.rect.centery > 550:
        boy.velocidade_y = 0
        boy.rect.centery = 550
        tempo = pygame.time.Clock()

    # Atualizar a tela
    pygame.display.update()
    # tempo.tick(80)

    # processa eventos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                boy.move_direita()
            if event.key == pygame.K_LEFT:
                boy.move_esquerda()
            if event.key == pygame.K_SPACE:
                boy.pular()
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                boy.para_horizontal()
            if event.key in [pygame.K_SPACE]:
                boy.para_vertical()
