import pygame
import sys
import json

from Model.Boy import Boy
from Model.Settings import Settings

pygame.init()
pygame.display.set_caption("EducaMais")

with open('gamesettings.json') as file:
    settings_json = json.load(file)

# Instanciando a classe Settings com as propriedades do arquivo gamesettings.json #
settings = Settings(settings_json)

# Background e resolução da tela #
window = pygame.display.set_mode((settings.width, settings.height))
background_image = pygame.image.load(settings.background_image).convert_alpha()
background = pygame.transform.scale(background_image, (settings.width, settings.height))

# Criar instância do personagem #
boy = Boy(settings)
characters = pygame.sprite.Group(boy)

tempo = pygame.time.Clock()

while True:
    window.blit(background, background.get_rect(center=window.get_rect().center))
    characters.draw(window)
    characters.update()

    if boy.rect.centery > 550:
        boy.velocidade_y = 0
        boy.rect.centery = 550
        tempo = pygame.time.Clock()

    # Atualiza a tela #
    pygame.display.update()

    # Lê eventos #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                boy.move_direita(settings)
            if event.key == pygame.K_LEFT:
                boy.move_esquerda(settings)
            if event.key == pygame.K_SPACE and boy.velocidade_y <= 1:
                boy.pular()
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                boy.para_horizontal()
            if event.key in [pygame.K_SPACE]:
                boy.para_vertical()