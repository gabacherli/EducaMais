import pygame
import sys
import json

from Model.Boy import Boy
from Model.Settings import Settings
from Model.Apagador import Apagador
from Model.Vida import Vida


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
gameover_img = pygame.image.load(settings.background_image_gameover).convert_alpha()

# Criar instância do personagem #
boy = Boy(settings)
characters = pygame.sprite.Group(boy)

# Criar instância do objeto Apagador #
apagador = Apagador(settings)
obj_apagador = pygame.sprite.Group(apagador)

# Som para colisão 
def som_colisao():
    pygame.mixer.music.load(settings.som_colisao)
    pygame.mixer.music.play(0)

# Som Game over 
def som_gameover():
    pygame.mixer.music.load(settings.som_gameover)
    pygame.mixer.music.play(0)

# vidas 
vida01 = Vida(settings)
obj_vida01 = pygame.sprite.Group(vida01)

vida02 = Vida(settings)
obj_vida02 = pygame.sprite.Group(vida02)
vida02.rect.centerx = 60

vida03 = Vida(settings)
obj_vida03 = pygame.sprite.Group(vida03)
vida03.rect.centerx = 110

tempo = pygame.time.Clock()

gameover = False
while True:
    if not gameover: 
        window.blit(background, background.get_rect(center=window.get_rect().center))
        obj_vida01.draw(window)
        obj_vida02.draw(window)
        obj_vida03.draw(window)
        characters.draw(window)
        obj_apagador.draw(window)
        characters.update()
        obj_apagador.update()

        # Caso tiver colisão entre o Boy e o Apagador
        if apagador.rect.colliderect(boy):
            print("Colidiu")  
            apagador.rect.x = 1250
            if vida01:
                vida01.kill()
                print("Perdeu 1 vida")
                vida01 = False
                som_colisao()
            elif vida02:
                vida02.kill()
                print("Perdeu 2 vidas")
                vida02 = False
                som_colisao()
            elif vida03:
                vida03.kill()
                print("Perdeu 3 vidas")
                vida03 = False

            
            if vida03 == False:
                gameover =  True
                window.blit(gameover_img, gameover_img.get_rect(center=window.get_rect().center))
                som_gameover()

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