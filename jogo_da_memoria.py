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
dic_jogo = harry_potter #Colocar o dicionário que foi escolido pelo usuario 



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

# Inicio da estrutura do jogo

# Imprimir no display cada imagem 
# Usar a termologia "b" caso a carta esteja virada para baixo e "c" caso a carta esteja virada para cima 


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





jogo = True

# Começar o loop do jogo 
while jogo:

#           ESCOLHA DA PRIMEIRA CARTA 
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Escolher uma carta e muda o status para virado para cima 
    carta_escolida_1 = "carta_18"
    lista_carta_1 =  dic_jogo[carta_escolida_1] 
    lista_carta_1[0] = "c"

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

#           ESCOLHA DA SEGUNDA CARTA 
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Escolho a segunda carta
    # Escolher a segunda carta e muda o status para virado para cima 
    carta_escolida_2 = "carta_18"
    lista_carta_2 =  dic_jogo[carta_escolida_2] 
    lista_carta_1[0] = "c"

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
        # Se forem mudo o estádo para viradas para cima 
        # Se não forem viro as duas para baixo 

    # Verifico que todas estão viradas para cima 

