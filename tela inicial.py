import pygame
from pygame.locals import *

pygame.init()

# criando a tela do jogo
hight = 800
width = 1280
tela = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Jogo da Memória')

game = True

imagem_tela_incial = pygame.image.load('memória.png').convert()
imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))

while game == True:

    tela.fill((0, 0, 0))
    tela.blit(imagem_tela_incial, (0, 0))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseXcor = event.pos[0]
            mouseYcor = event.pos[1]

            if 340 < mouseXcor < 940 and 350 < mouseYcor < 450:

            elif 340 < mouseXcor < 940 and 350 < mouseYcor < 450:

            elif 340 < mouseXcor < 940 and 350 < mouseYcor < 450:

    # criando botões

    pygame.draw.polygon(tela, (0, 0, 0), [(340, 350), (340, 450), (940, 450), (940, 350)])
    pygame.draw.polygon(tela, (0, 0, 0), [(340, 200), (340, 300), (940, 300), (940, 200)])
    pygame.draw.polygon(tela, (0, 0, 0), [(340, 500), (340, 600), (940, 600), (940, 500)])

        
    pygame.display.update()