# Jogo da memória
import random 
import pygame
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

# Criar um dicionário para cada grupo de personagens 

# Definindo o diconário de pokemon 
pokemon = {}
pokemon["carta_1"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_2"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_3"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_4"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_5"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_6"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_7"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_8"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_9"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_10"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_11"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_12"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_13"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_14"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_15"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_16"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_17"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_18"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_19"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_20"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_21"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_22"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_23"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_24"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_25"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_26"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_27"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_28"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_29"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_30"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_31"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_32"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_33"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_34"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_35"] = ["b", "foto_frente", "foto_trás", [0, 0]]
pokemon["carta_36"] = ["b", "foto_frente", "foto_trás", [0, 0]]


#Definindo o dicionário de Star Wars]
star_wars = {}
star_wars["carta_1"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_2"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_3"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_4"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_5"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_6"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_7"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_8"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_9"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_10"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_11"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_12"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_13"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_14"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_15"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_16"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_17"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_18"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_19"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_20"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_21"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_22"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_23"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_24"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_25"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_26"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_27"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_28"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_29"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_30"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_31"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_32"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_33"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_34"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_35"] = ["b", "foto_frente", "foto_trás", [0, 0]]
star_wars["carta_36"] = ["b", "foto_frente", "foto_trás", [0, 0]]


# Definindo o dicionário de Harry Potter
harry_potter = {}
harry_potter["carta_1"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_2"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_3"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_4"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_5"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_6"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_7"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_8"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_9"]  = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_10"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_11"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_12"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_13"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_14"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_15"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_16"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_17"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_18"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_19"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_20"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_21"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_22"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_23"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_24"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_25"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_26"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_27"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_28"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_29"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_30"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_31"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_32"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_33"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_34"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_35"] = ["b", "foto_frente", "foto_trás", [0, 0]]
harry_potter["carta_36"] = ["b", "foto_frente", "foto_trás", [0, 0]]




# Estrutura do jogo 

# Definir o dicionário que será utilizada a partir da resposta do jogador
 #Colocar o dicionário que foi escolido pelo usuario 

# Sorteia uma posição para cada foto
lista_posicoes = [[0, 0],[1, 1],[2, 2],[3, 3],[4, 4],[5, 5],[6, 6],[7, 7],[8, 8],[9, 9],[10, 10],
[11, 11],[12, 12],[13, 13],[14, 14],[15, 15],[16, 16],[17, 17],[18, 18],[19, 19],[20, 20],[21, 21],
[22, 22],[23, 23],[24, 24],[25, 25],[26, 26],[27, 27],[28, 28],[29, 29],[30, 30],[31, 31],[32, 32],
[33, 33],[34, 34],[35, 35],[36, 36]]

# Embaralha a lista de posições 
random.shuffle(lista_posicoes)

# Adicionar as posições para cada valor do dicionário
i = 0
for carta in dic_jogo:
    lista_carta = dic_jogo[carta]
    lista_carta[3] = lista_posicoes[i]
    i += 1

#print(dic_jogo)


# Nesse ponto o dicionário já está pronto para começar a ser utilizado no jogo 




# DEFININDO AS CONDIÇÕES INICIAIS DO JOGO, Usar a termologia "b" caso a carta esteja virada para baixo e "c" caso a carta esteja virada para cima
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Imprimir todas as cartas virada para cima 
for carta in dic_jogo:
    lista_carta = dic_jogo[carta]
    # Pegando parametros da carta
    png_carta = lista_carta[1]
    posicao_x = lista_carta[3][0]
    posicao_y = lista_carta[3][1]
    # Salvando a carta na tela 
    tela.blit(png_carta, (posicao_x, posicao_y))

# Atualiza a imagem das cartas virada para cima
pygame.display.update()

# Esperar 5 segundo 
pygame.time.wait(5000)

# Imprimir todas as cartas viradas para baixo 
for carta in dic_jogo:
    lista_carta = dic_jogo[carta]
    # Pegando parametros da carta
    png_carta = lista_carta[2]
    posicao_x = lista_carta[3][0]
    posicao_y = lista_carta[3][1]
    # Salvando a carta na tela 
    tela.blit(png_carta, (posicao_x, posicao_y))

# Atualiza a imagem das cartas virada para cima
pygame.display.update()



# Começar o loop do jogo 
jogo = True

while jogo:

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
                dic_jogo = star_wars

            elif 330 < mouseXcor < 950 and 400 < mouseYcor < 500:
                dic_jogo = harry_potter

            elif 330 < mouseXcor < 950 and 550 < mouseYcor < 650:
                dic_jogo = pokemon

    # criando botões

    tela.blit(botao_starwars, (100, 100))
    tela.blit(botao_harrypotter, (100, 250))
    tela.blit(botao_pokemon, (100, 400))
        
    pygame.display.update()

# ESCOLHA DA PRIMEIRA CARTA 
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    # Escolher uma carta e muda o status para virado para cima 
    carta_escolida_1 = "carta_18"
    lista_carta_1 =  dic_jogo[carta_escolida_1] 
    lista_carta_1[0] = "c" # Ver se de fato está atualiuzando o dicionário

    # Imprimir as cartas da forma atualizada delas  
    for carta in dic_jogo:
        lista_carta = dic_jogo[carta]
        lado      = lista_carta[0]
        if lado == "b":
            png_carta = lista_carta[2]
        if lado == "c":
            png_carta = lista_carta[1]
        posicao_x = lista_carta[3][0]
        posicao_y = lista_carta[3][1]
        # Salvando a carta na tela 
        tela.blit(png_carta, (posicao_x, posicao_y))

    # Atualiza a imagem das cartas virada para cima
    pygame.display.update()



# ESCOLHA DA SEGUNDA CARTA 
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    # Escolher a segunda carta e muda o status para virado para cima 
    carta_escolida_2 = "carta_18"
    lista_carta_2 =  dic_jogo[carta_escolida_2] 
    lista_carta_2[0] = "c"

    # Imprimir as cartas da forma atualizada delas  
    for carta in dic_jogo:
        lista_carta = dic_jogo[carta]
        lado      = lista_carta[0]
        if lado == "b":
            png_carta = lista_carta[2]
        if lado == "c":
            png_carta = lista_carta[1]
        posicao_x = lista_carta[3][0]
        posicao_y = lista_carta[3][1]
        # Salvando a carta na tela 
        tela.blit(png_carta, (posicao_x, posicao_y))

    # Atualiza a imagem das cartas virada para cima
    pygame.display.update()
    

    # Verifico se as cartas são iguais 
    png_imagem_escolhida_1 = lista_carta_1[1]   
    png_imagem_escolhida_2 = lista_carta_2[1]
    
    if png_imagem_escolhida_1 != png_imagem_escolhida_2:
        pygame.time.wait(3000)
        # Espero 3 segundos 
        # Desviro as cartas 
        lista_carta_1[0] = "b" # Ver se de fato está atualiuzando o dicionário
        lista_carta_2[0] = "b" # Ver se de fato está atualiuzando o dicionário
        # Imprimir as cartas da forma atualizada delas  
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lado      = lista_carta[0]
            if lado == "b":
                png_carta = lista_carta[2]
            if lado == "c":
                png_carta = lista_carta[1]
            posicao_x = lista_carta[3][0]
            posicao_y = lista_carta[3][1]
            # Salvando a carta na tela 
            tela.blit(png_carta, (posicao_x, posicao_y))

        # Atualiza a imagem das cartas virada para cima
        pygame.display.update()



    # Verifico que todas estão viradas para cima 
    v = "t"
    for carta in dic_jogo:
        list_carta = dic_jogo[carta]
        posicao_carta = list_carta[0]
        if posicao_carta == "b":
            v = "f" 
    if v == "t":
        jogo == False 
        # Acabou o jogo 