# Jogo da memória

import pygame
pygame.init()

# criando a tela do jogo
hight = 800
width = 1280
tela = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Jogo da Memória')

game = True

imagem_carta = pygame.image.load('imagens/star wars/han solo.png').convert_alpha()
imagem_tela_incial = pygame.image.load('memória.png').convert()
imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))
imagem_carta = pygame.transform.scale(imagem_carta, (50, 100))

#carta1 = Carta(imagem_carta, 100, 100)
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
                print('botaão 1')

        
    ##tela.blit(carta1.image, carta1.rect)
    #tela.blit(text1, (420, 20))
    #tela.blit(text2, (500, 90))

    # criando botões

    pygame.draw.polygon(tela, (0, 0, 0), [(340, 350), (340, 450), (940, 450), (940, 350)])
    pygame.draw.polygon(tela, (0, 0, 0), [(340, 200), (340, 300), (940, 300), (940, 200)])
    pygame.draw.polygon(tela, (0, 0, 0), [(340, 500), (340, 600), (940, 600), (940, 500)])

    # criando textos dos botões

        
    pygame.display.update()
# criando tela inicial



# Criar um dicionário para cada grupo de personagens 

# Definindo o diconário de pokemon 
dic_pokemon = {}
dic_pokemon["carta_1"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_2"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_3"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_4"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_5"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_6"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_7"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_8"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_9"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_10"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_11"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_12"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_13"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_14"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_15"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_16"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_17"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
dic_pokemon["carta_18"] = ["foto_frente", "foto_trás", [0, 0], [0,0]] 

#Definindo o dicionário de Star Wars]
star_wars = {}
star_wars["carta_1"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_2"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_3"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_4"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_5"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_6"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_7"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_8"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_9"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_10"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_11"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_12"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_13"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_14"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_15"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_16"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_17"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
star_wars["carta_18"] = ["foto_frente", "foto_trás", [0, 0], [0,0]] 

# Definindo o dicionário de Harry Potter
harry_potter = {}
harry_potter["carta_1"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_2"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_3"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_4"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_5"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_6"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_7"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_8"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_9"]  = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_10"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_11"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_12"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_13"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_14"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_15"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_16"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_17"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]
harry_potter["carta_18"] = ["foto_frente", "foto_trás", [0, 0], [0,0]]

# Escolhendo valores aleatório para cada carta

# Criar uma lista com posições para as 36 cartas

# Atribuir cada uma das posições para cada uma da carta do dicionário escolhido 

# Mostrar cada carta no painel por 5 segundos virada para cima 

# Virar Todas as cartas para baixo 

# Jogador escolhe primeira carta

# Jogador escolhe a segunda 

# Verifica se são iguais 

# Muda o tabuleiro 

# Conta em quantas rodadas foram feitas o jogo 

# Mostra no final um ranking e a sua posição 