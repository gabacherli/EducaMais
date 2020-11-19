import pygame
import sys
import json

from Model.Boy import Boy
from Model.Settings import Settings
from Model.Apagador import Apagador

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

# Criar instância do objeto Apagador #
apagador = Apagador(settings)
obj_apagador = pygame.sprite.Group(apagador)

tempo = pygame.time.Clock()

while True:
    window.blit(background, background.get_rect(center=window.get_rect().center))
    characters.draw(window)
    obj_apagador.draw(window)
    characters.update()
    obj_apagador.update()

    # Caso tiver colisão entre o Boy e o Apagador
    if apagador.rect.colliderect(boy):
        apagador.rect.x = 1250

    # Manter personagem dentro dos limites da janela #
    # Impedir que o personagem ultrapasse o limite horizontal pela esquerda #
    if boy.rect.centerx < 1:
        boy.velocidade_x = 0
        boy.rect.centerx = 1

    # Impedir que o personagem ultrapasse o limite vertical por baixo e manter personagem em contato com o solo #
    if boy.rect.centery > settings.height/1.38:
        boy.velocidade_y = 0
        boy.rect.centery = settings.height/1.38

    # Impedir que o personagem ultrapasse o limite horizontal pela direita #
    if boy.rect.centerx > settings.width - settings.char_ratio[0]:
        boy.velocidade_x = 0
        boy.rect.centerx = settings.width - settings.char_ratio[0]

    # Impedir que o personagem ultrapasse o limite vertical por cima #
    if boy.rect.centery < -(settings.char_ratio[1]):
        boy.velocidade_y = 0
        boy.rect.centery = -(settings.char_ratio[1])

    # Atualiza a tela #
    pygame.display.update()

    # Lê eventos #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boy.mover_para_esquerda(settings)
            if event.key == pygame.K_RIGHT:
                boy.mover_para_direita(settings)
            if event.key == pygame.K_SPACE:
                boy.pular()
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                boy.parar_movimento_horizontal()
            if event.key in [pygame.K_SPACE]:
                boy.parar_movimento_vertical()