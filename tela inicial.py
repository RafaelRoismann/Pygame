import pygame
from pygame.locals import *

pygame.init()

# criando a tela do jogo
hight = 800
width = 1280
tela = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Jogo da Memória')

game = True

botao_starwars = pygame.image.load('imagens/botao/botao_starwars.png').convert_alpha()
botao_harrypotter = pygame.image.load('imagens/botao/botao_potter.png').convert_alpha()
botao_pokemon = pygame.image.load('imagens/botao/botao_pokemon.png').convert_alpha()
imagem_tela_incial = pygame.image.load('imagens/bg inicio.jpg').convert()
titulo = pygame.image.load('imagens/titulo.png').convert_alpha()

imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))
titulo = pygame.transform.scale(titulo, (960, 540))
botao_pokemon = pygame.transform.scale(botao_pokemon, (1080, 400))
botao_harrypotter = pygame.transform.scale(botao_harrypotter, (1080, 400))
botao_starwars = pygame.transform.scale(botao_starwars, (1080, 400))

while game == True:

    tela.fill((0, 0, 0))
    tela.blit(imagem_tela_incial, (0, 0))
    tela.blit(titulo, (150, -150))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseXcor = event.pos[0]
            mouseYcor = event.pos[1]

            if 330 < mouseXcor < 950 and 250 < mouseYcor < 350:
                dic_jogo = 0

            elif 330 < mouseXcor < 950 and 400 < mouseYcor < 500:
                dic_jogo = 0

            elif 330 < mouseXcor < 950 and 550 < mouseYcor < 650:
                dic_jogo = 0

    # criando botões

    tela.blit(botao_starwars, (100, 100))
    tela.blit(botao_harrypotter, (100, 250))
    tela.blit(botao_pokemon, (100, 400))
        
    pygame.display.update()