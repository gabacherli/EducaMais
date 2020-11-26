import pygame
import sys
import json
import random

from Model.Boy import Boy
from Model.Platform import Platform
from Model.Settings import Settings
from Model.Villain import Villain
from Model.Eraser import Eraser
from Model.Soundboard import Soundboard
from Model.Life import Life
from Model.Whiteboard import Whiteboard

def generate_plataforms():
    current_word = random_words[len(random_words) -1]
    platforms = []

    for i in current_word:
        platform = Platform(settings, i)
        platforms.append(platform)
        if len(platforms) > 1 and platform.rect.collidelist(platforms):
            platforms.pop()
            new_platform = platform.generate_platform_that_wont_collide(settings, platforms, i)
            platforms.append(new_platform)

    return platforms

pygame.init()
pygame.display.set_caption("EducaMais")

with open('gamesettings.json') as settings_file:
    settings_json = json.load(settings_file)

with open('Misc/Text/words2.txt') as text_file:
    words = [line.rstrip() for line in text_file]
    random_words = random.sample(words, len(words))

# Instanciando as classes de configuração #
settings = Settings(settings_json)
soundboard = Soundboard(settings)

# Background e resolução da tela #
window = pygame.display.set_mode((settings.width, settings.height))
background_image = pygame.image.load(settings.background_image).convert_alpha()
background = pygame.transform.scale(background_image, (settings.width, settings.height))

# Criar instância do quadro branco #
whiteboard = Whiteboard(settings)
sprite_whiteboard = pygame.sprite.Group(whiteboard)

# Criar instância do personagem #
boy = Boy(settings)
sprite_boy = pygame.sprite.Group(boy)

# Criar instância do personagem vilão #
villain = Villain(settings)
sprite_villain = pygame.sprite.Group(villain)

# Criar instância do apagador #
eraser = Eraser(settings)
sprite_eraser = pygame.sprite.Group(eraser)

# Criar sprite das vidas do personagem #
vidas = []

for i in range(settings.starting_number_of_lives):
    vidas.append(Life(settings))
    vidas[i].rect.centerx = vidas[i].rect.centerx if i == 0 else vidas[i - 1].rect.centerx + 60

sprite_lives = pygame.sprite.Group(vidas)

# Plataformas #
platforms = generate_plataforms()

sprite_platforms = pygame.sprite.Group(platforms)

tempo = pygame.time.Clock()

gameover = False

while True:
    if not gameover:
        # Desenhar elementos fixos da tela #
        current_word = random_words[len(random_words) -1]

        window.blit(background, background.get_rect(center=window.get_rect().center))
        # Palavra no quadro-branco #
        sprite_whiteboard.draw(window)
        word = whiteboard.write_word_to_word_rectangle(current_word)
        sprite_platforms.draw(window)

        # Letras nas plataformas #
        for i in platforms:
            last_letter = current_word[-1]
            letter = i.write_letter_to_letter_rectangle(last_letter)
            window.blit(letter, i.letter_rectangle)

            current_word = current_word[:-1]

        window.blit(word, whiteboard.word_rectangle)
        sprite_villain.draw(window)
        sprite_boy.draw(window)
        sprite_eraser.draw(window)
        sprite_lives.draw(window)
        sprite_villain.update(settings)
        sprite_eraser.update(settings)
        sprite_boy.update()
        sprite_lives.draw(window)

        # Caso tenha colisão entre o personagem e o apagador #
        if eraser.rect.colliderect(boy):
            eraser.rect.x = settings.width
            if vidas[len(vidas) - 1] and len(vidas) > 1:
                vidas[len(vidas) - 1].kill()
                vidas.pop()
                soundboard.play_hit_sound(settings.sound_on)
            else:
                gameover_image = pygame.image.load(settings.gameover_image).convert_alpha()
                gameover = True
                window.blit(gameover_image, gameover_image.get_rect(center=window.get_rect().center))
                soundboard.play_gameover_sound(settings.sound_on)

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
    if boy.rect.centerx > settings.width - settings.aurelinho_ratio[0]:
        boy.velocidade_x = 0
        boy.rect.centerx = settings.width - settings.aurelinho_ratio[0]

    # Impedir que o personagem ultrapasse o limite vertical por cima #
    if boy.rect.centery < -(settings.aurelinho_ratio[1]):
        boy.velocidade_y = 0
        boy.rect.centery = -(settings.aurelinho_ratio[1])

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