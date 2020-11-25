import pygame
import sys
import json

from Model.Boy import Boy
from Model.Settings import Settings
from Model.Eraser import Eraser
from Model.Soundboard import Soundboard
from Model.Life import Life

pygame.init()
pygame.display.set_caption("EducaMais")

with open('gamesettings.json') as file:
    settings_json = json.load(file)

# Instanciando as classes de configuração #
settings = Settings(settings_json)
soundboard = Soundboard(settings)

# Background e resolução da tela #
window = pygame.display.set_mode((settings.width, settings.height))
background_image = pygame.image.load(settings.background_image).convert_alpha()
background = pygame.transform.scale(background_image, (settings.width, settings.height))

# Criar instância do personagem #
boy = Boy(settings)
sprite_boy = pygame.sprite.Group(boy)

# Criar instância do eraser #
eraser = Eraser(settings)
sprite_eraser = pygame.sprite.Group(eraser)

# Criar sprites da vida do personagem #
vidas = []

for i in range(settings.starting_number_of_lives):
    vidas.append(Life(settings))
    vidas[i].rect.centerx = vidas[i].rect.centerx if i == 0 else vidas[i - 1].rect.centerx + 60

sprite_lives = pygame.sprite.Group(vidas)

tempo = pygame.time.Clock()

gameover = False

while True:
    if not gameover:
        window.blit(background, background.get_rect(center=window.get_rect().center))
        sprite_boy.draw(window)
        sprite_eraser.draw(window)
        sprite_boy.update()
        sprite_eraser.update()
        sprite_lives.draw(window)

        # Caso tiver colisão entre o Boy e o Apagador
        if eraser.rect.colliderect(boy):
            print("Colidiu")
            eraser.rect.x = 1250
            if vidas[len(vidas) - 1] and len(vidas) > 1:
                vidas[len(vidas) - 1].kill()
                vidas.pop()
                soundboard.play_hit_sound()
            else:
                gameover_image = pygame.image.load(settings.gameover_image).convert_alpha()
                gameover = True
                window.blit(gameover_image, gameover_image.get_rect(center=window.get_rect().center))
                soundboard.play_gameover_sound()

    # Manter personagem dentro dos limites da janela #
    # Impedir que o personagem ultrapasse o limite horizontal pela esquerda #
    if boy.rect.centerx < 1:
        boy.velocidade_x = 0
        boy.rect.centerx = 1

    # Impedir que o personagem ultrapasse o limite vertical por baixo e manter personagem em contato com o solo #
    if boy.rect.centery > settings.height / 1.38:
        boy.velocidade_y = 0
        boy.rect.centery = settings.height / 1.38

    # Impedir que o personagem ultrapasse o limite horizontal pela direita #
    if boy.rect.centerx > settings.width - settings.char_ratio[0]:
        boy.velocidade_x = 0
        boy.rect.centerx = settings.width - settings.char_ratio[0]

    # Impedir que o personagem ultrapasse o limite vertical por cima #
    if boy.rect.centery < -(settings.char_ratio[1]):
        boy.velocidade_y = 0
        boy.rect.centery = -(settings.char_ratio[1])

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