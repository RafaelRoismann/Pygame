# Jogo da memória

import pygame
pygame.init()

# criando a tela do jogo
hight = 800
width = 1280
tela = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Jogo da Memória')

game = True

font = pygame.font.SysFont(None, 70)
font2 = pygame.font.SysFont(None, 45)
text1 = font.render('JOGO DA MEMÓRIA', True, (87, 197, 235))
text2 = font2.render('ESCOLHA UM TEMA', True, (0, 0, 0))

imagem_tela_incial = pygame.image.load('memória.png').convert()
imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))

vertices = [(250, 0), (250, 200), (0, 400), (0, 200)]
while game == True:

    tela.fill((0, 0, 0))
    tela.blit(imagem_tela_incial, (0, 0))
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            game = False

    tela.blit(text1, (420, 20))
    tela.blit(text2, (500, 90))

    # criando botões

    retangulo = pygame.Rect(0, 0, largura, altura)
    pygame.draw.rect(tela, (0, 0, 0), retangulo)


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