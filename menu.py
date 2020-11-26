import pygame
import sys
import json

from Model.Settings import Settings

with open('gamesettings.json') as settings_file:
    settings_json = json.load(settings_file)

settings = Settings(settings_json)

pygame.init()
pygame.font.init()
# Background e resolução da tela #
window = pygame.display.set_mode((settings.width, settings.height))
background_image = pygame.image.load(settings.background_image).convert_alpha()
background = pygame.transform.scale(background_image, (settings.width, settings.height))

# Fontes #
main_font = pygame.font.SysFont('Verdana', 25, )
main_font_bold = pygame.font.SysFont('Verdana', 22, True)
black = (0,0,0)
background_yellow = (251, 237, 162)

# Botoes do Menu principal #
start_button = pygame.Rect(settings.width/2.2, 160, 200, 50)
exit_button = pygame.Rect(settings.width/2.2, 230, 200, 50)

click = False

def menu_screen():
    global click

    while True:
        pygame.display.set_caption("Menu principal")
        window.blit(background, background.get_rect(center=window.get_rect().center))

        draw_menu_buttons()

        mx, my = pygame.mouse.get_pos()

        if start_button.collidepoint((mx, my)):
            if click:
                import EducaMais
        if exit_button.collidepoint((mx, my)):
            if click:
                pygame.quit()

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def draw_menu_buttons():
    pygame.draw.rect(window, background_yellow, start_button)
    pygame.draw.rect(window, background_yellow, exit_button)

    start_text = main_font_bold.render('START GAME', False, black)
    window.blit(start_text, (settings.width/2.13, 175))

    quit_text = main_font_bold.render('SAIR', False, black)
    window.blit(quit_text, (settings.width/2, 243))


menu_screen()