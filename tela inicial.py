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
imagem_tela_incial = pygame.image.load('memória.png').convert()

imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))
botao_pokemon = pygame.transform.scale(botao_pokemon, (700, 100))
botao_harrypotter = pygame.transform.scale(botao_harrypotter, (700, 100))
botao_starwars = pygame.transform.scale(botao_starwars, (700, 100))

while game == True:

    tela.fill((0, 0, 0))
    tela.blit(imagem_tela_incial, (0, 0))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseXcor = event.pos[0]
            mouseYcor = event.pos[1]

            if 340 < mouseXcor < 940 and 200 < mouseYcor < 300:
                print('botão 1')

            elif 340 < mouseXcor < 940 and 350 < mouseYcor < 450:
                print('botão 2')

            elif 340 < mouseXcor < 940 and 500 < mouseYcor < 600:
                print('botão 3')

    # criando botões

    pygame.draw.polygon(tela, (0, 0, 0), [(340, 350), (340, 450), (940, 450), (940, 350)])
    pygame.draw.polygon(tela, (0, 0, 0), [(340, 200), (340, 300), (940, 300), (940, 200)])
    pygame.draw.polygon(tela, (0, 0, 0), [(340, 500), (340, 600), (940, 600), (940, 500)])

    tela.blit(botao_starwars, (340, 600))
    tela.blit(botao_harrypotter, (340, 450))
    tela.blit(botao_pokemon, (340, 300))
        
    pygame.display.update()