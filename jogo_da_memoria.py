# Jogo da memória
import random 
import pygame
import time
pygame.init()

# criando a tela do jogo
hight = 800
width = 1280
tela = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Jogo da Memória')
game = True
jogo = True 
Jogadas = True
tema = False

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Load nas imagens 

# load nos planos de fundo 
fundo_starwars = pygame.image.load('Tela de fundo do jogo.png').convert_alpha()
fundo_harrypotter = pygame.image.load('Tela de fundo do jogo.png').convert_alpha()
fundo_pokemon = pygame.image.load('Tela de fundo do jogo.png').convert_alpha()

# load das cartas de trás 
carta_capa_s = pygame.image.load('Verso da carta.png').convert_alpha()
carta_capa_p = pygame.image.load('Verso da carta.png').convert_alpha()
carta_capa_h = pygame.image.load('Verso da carta.png').convert_alpha()

# load nas cartas 

# Harry Potter
carta_h_1 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_2 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_3 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_4 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_5 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_6 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_7 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_8 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_9 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_10 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_11 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_12 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_13 = pygame.image.load('C-3PO.png').convert_alpha()
carta_h_14 = pygame.image.load('C-3PO.png').convert_alpha()

# Star Wars
carta_s_1 = pygame.image.load('Admiral Ackbar.png').convert_alpha()
carta_s_2 = pygame.image.load('BB-8.png').convert_alpha()
carta_s_3 = pygame.image.load('Boba Fett.png').convert_alpha()
carta_s_4 = pygame.image.load('C-3PO.png').convert_alpha()
carta_s_5 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_s_6 = pygame.image.load('Darth Maul.png').convert_alpha()
carta_s_7 = pygame.image.load('Darth Vader.png').convert_alpha()
carta_s_8 = pygame.image.load('Emperor Palpatine.png').convert_alpha()
carta_s_9 = pygame.image.load('Finn.png').convert_alpha()
carta_s_10 = pygame.image.load('Han Solo.png').convert_alpha()
carta_s_11 = pygame.image.load('Jabba The Hutt.png').convert_alpha()
carta_s_12 = pygame.image.load('Luke Skywalker.png').convert_alpha()
carta_s_13 = pygame.image.load('Princess Leia.png').convert_alpha()
carta_s_14 = pygame.image.load('Rey.png').convert_alpha()

# Pokemon
carta_p_1 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_2 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_3 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_4 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_5 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_6 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_7 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_8 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_9 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_10 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_11 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_12 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_13 = pygame.image.load('Chewbacca.png').convert_alpha()
carta_p_14 = pygame.image.load('Chewbacca.png').convert_alpha()

# load nos botões da página inicial 
botao_starwars = pygame.image.load('botao_starwars.png').convert_alpha()
botao_harrypotter = pygame.image.load('botao_potter.png').convert_alpha()
botao_pokemon = pygame.image.load('botao_pokemon.png').convert_alpha()

# load no título
titulo = pygame.image.load('imagens/titulo.png').convert_alpha()

# Load tela inicial 
imagem_tela_incial = pygame.image.load('Tela de fundo do jogo.png').convert_alpha()


# FORMATANDO AS IMAGENS 

# Definido tamanho das cartas
CARTA_WIDTH = 320 # 120 original
CARTA_HEIGHT = 170 # 150 original

# Formatando planos de fundo 
fundo_starwars =  pygame.transform.scale(fundo_starwars, (1280, 800))
fundo_harrypotter = pygame.transform.scale(fundo_harrypotter, (1280, 800))
fundo_pokemon = pygame.transform.scale(fundo_pokemon, (1280, 800))

# Formatando as cartas de trás 
carta_capa_s = pygame.transform.scale(carta_capa_s, (CARTA_WIDTH, CARTA_HEIGHT))
carta_capa_p = pygame.transform.scale(carta_capa_p, (CARTA_WIDTH, CARTA_HEIGHT))
carta_capa_h = pygame.transform.scale(carta_capa_h, (CARTA_WIDTH, CARTA_HEIGHT))

# Formatando as cartas de frente

# Harry Potter
carta_h_1 = pygame.transform.scale(carta_h_1, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_2 = pygame.transform.scale(carta_h_2, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_3 = pygame.transform.scale(carta_h_3, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_4 = pygame.transform.scale(carta_h_4, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_5 = pygame.transform.scale(carta_h_5, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_6 = pygame.transform.scale(carta_h_6, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_7 = pygame.transform.scale(carta_h_7, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_8 = pygame.transform.scale(carta_h_8, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_9 = pygame.transform.scale(carta_h_9, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_10 = pygame.transform.scale(carta_h_10, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_11 = pygame.transform.scale(carta_h_11, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_12 = pygame.transform.scale(carta_h_12, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_13 = pygame.transform.scale(carta_h_13, (CARTA_WIDTH, CARTA_HEIGHT))
carta_h_14 = pygame.transform.scale(carta_h_14, (CARTA_WIDTH, CARTA_HEIGHT))

# Star Wars
carta_s_1 = pygame.transform.scale(carta_s_1, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_2 = pygame.transform.scale(carta_s_2, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_3 = pygame.transform.scale(carta_s_3, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_4 = pygame.transform.scale(carta_s_4, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_5 = pygame.transform.scale(carta_s_5, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_6 = pygame.transform.scale(carta_s_6, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_7 = pygame.transform.scale(carta_s_7, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_8 = pygame.transform.scale(carta_s_8, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_9 = pygame.transform.scale(carta_s_9, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_10 = pygame.transform.scale(carta_s_10, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_11 = pygame.transform.scale(carta_s_11, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_12 = pygame.transform.scale(carta_s_12, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_13 = pygame.transform.scale(carta_s_13, (CARTA_WIDTH, CARTA_HEIGHT))
carta_s_14 = pygame.transform.scale(carta_s_14, (CARTA_WIDTH, CARTA_HEIGHT))

# Pokemon
carta_p_1 = pygame.transform.scale(carta_p_1, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_2 = pygame.transform.scale(carta_p_2, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_3 = pygame.transform.scale(carta_p_3, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_4 = pygame.transform.scale(carta_p_4, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_5 = pygame.transform.scale(carta_p_5, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_6 = pygame.transform.scale(carta_p_6, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_7 = pygame.transform.scale(carta_p_7, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_8 = pygame.transform.scale(carta_p_8, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_9 = pygame.transform.scale(carta_p_9, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_10 = pygame.transform.scale(carta_p_10, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_11 = pygame.transform.scale(carta_p_11, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_12 = pygame.transform.scale(carta_p_12, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_13 = pygame.transform.scale(carta_p_13, (CARTA_WIDTH, CARTA_HEIGHT))
carta_p_14 = pygame.transform.scale(carta_p_14, (CARTA_WIDTH, CARTA_HEIGHT))

# Formatando os botões da página inicial 
botao_pokemon = pygame.transform.scale(botao_pokemon, (1080, 400))
botao_harrypotter = pygame.transform.scale(botao_harrypotter, (1080, 400))
botao_starwars = pygame.transform.scale(botao_starwars, (1080, 400))

# Formatando o título
titulo = pygame.transform.scale(titulo, (960, 540))

# Formatando a imagem inicial 
imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Estrutura do jogo 

while jogo:
    # Página inicial esperado o jogador escolher um tema 
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
                tema_escolido = "star_wars"
                tema = True
            elif 330 < mouseXcor < 950 and 400 < mouseYcor < 500:
                tema_escolido = "harry_potter"
                tema = True
            elif 330 < mouseXcor < 950 and 550 < mouseYcor < 650:
                tema_escolido = "pokemon"
                tema = True

        # criando botões
        tela.blit(botao_starwars, (100, 100))
        tela.blit(botao_harrypotter, (100, 250))
        tela.blit(botao_pokemon, (100, 400))    
        pygame.display.update()
        
    # Entrar no if somente quando o jogador tiver escolido um tema    
    if tema:

        # Definindo o diconário de pokemon 
        pokemon = {}
        pokemon["carta_1"]  = ["b", carta_p_1, carta_capa_p, [0, 0]]
        pokemon["carta_2"]  = ["b", carta_p_1, carta_capa_p, [0, 0]]
        pokemon["carta_3"]  = ["b", carta_p_2, carta_capa_p, [0, 0]]
        pokemon["carta_4"]  = ["b", carta_p_2, carta_capa_p, [0, 0]]
        pokemon["carta_5"]  = ["b", carta_p_3, carta_capa_p, [0, 0]]
        pokemon["carta_6"]  = ["b", carta_p_3, carta_capa_p, [0, 0]]
        pokemon["carta_7"]  = ["b", carta_p_4, carta_capa_p, [0, 0]]
        pokemon["carta_8"]  = ["b", carta_p_4, carta_capa_p, [0, 0]]
        pokemon["carta_9"]  = ["b", carta_p_5, carta_capa_p, [0, 0]]
        pokemon["carta_10"] = ["b", carta_p_5, carta_capa_p, [0, 0]]
        pokemon["carta_11"] = ["b", carta_p_6, carta_capa_p, [0, 0]]
        pokemon["carta_12"] = ["b", carta_p_6, carta_capa_p, [0, 0]]
        pokemon["carta_13"] = ["b", carta_p_7, carta_capa_p, [0, 0]]
        pokemon["carta_14"] = ["b", carta_p_7, carta_capa_p, [0, 0]]
        pokemon["carta_15"] = ["b", carta_p_8, carta_capa_p, [0, 0]]
        pokemon["carta_16"] = ["b", carta_p_8, carta_capa_p, [0, 0]]
        pokemon["carta_17"] = ["b", carta_p_9, carta_capa_p, [0, 0]]
        pokemon["carta_18"] = ["b", carta_p_9, carta_capa_p, [0, 0]]
        pokemon["carta_19"] = ["b", carta_p_10, carta_capa_p, [0, 0]]
        pokemon["carta_20"] = ["b", carta_p_10, carta_capa_p, [0, 0]]
        pokemon["carta_21"] = ["b", carta_p_11, carta_capa_p, [0, 0]]
        pokemon["carta_22"] = ["b", carta_p_11, carta_capa_p, [0, 0]]
        pokemon["carta_23"] = ["b", carta_p_12, carta_capa_p, [0, 0]]
        pokemon["carta_24"] = ["b", carta_p_12, carta_capa_p, [0, 0]]
        pokemon["carta_25"] = ["b", carta_p_13, carta_capa_p, [0, 0]]
        pokemon["carta_26"] = ["b", carta_p_13, carta_capa_p, [0, 0]]
        pokemon["carta_27"] = ["b", carta_p_14, carta_capa_p, [0, 0]]
        pokemon["carta_28"] = ["b", carta_p_14,carta_capa_p, [0, 0]]



        #Definindo o dicionário de Star Wars]
        star_wars = {}
        star_wars["carta_1"]  = ["b", carta_s_3, carta_capa_s, [0, 0]]
        star_wars["carta_2"]  = ["b", carta_s_3, carta_capa_s, [0, 0]]
        star_wars["carta_3"]  = ["b", carta_s_3, carta_capa_s, [0, 0]]
        star_wars["carta_4"]  = ["b", carta_s_3, carta_capa_s, [0, 0]]
        star_wars["carta_5"]  = ["b", carta_s_3, carta_capa_s, [0, 0]]
        star_wars["carta_6"]  = ["b", carta_s_3, carta_capa_s, [0, 0]]
        star_wars["carta_7"]  = ["b", carta_s_4, carta_capa_s, [0, 0]]
        star_wars["carta_8"]  = ["b", carta_s_4, carta_capa_s, [0, 0]]
        star_wars["carta_9"]  = ["b", carta_s_5, carta_capa_s, [0, 0]]
        star_wars["carta_10"] = ["b", carta_s_5, carta_capa_s, [0, 0]]
        star_wars["carta_11"] = ["b", carta_s_6, carta_capa_s, [0, 0]]
        star_wars["carta_12"] = ["b", carta_s_6, carta_capa_s, [0, 0]]
        star_wars["carta_13"] = ["b", carta_s_7, carta_capa_s, [0, 0]]
        star_wars["carta_14"] = ["b", carta_s_7, carta_capa_s, [0, 0]]
        star_wars["carta_15"] = ["b", carta_s_8, carta_capa_s, [0, 0]]
        star_wars["carta_16"] = ["b", carta_s_8, carta_capa_s, [0, 0]]
        star_wars["carta_17"] = ["b", carta_s_9, carta_capa_s, [0, 0]]
        star_wars["carta_18"] = ["b", carta_s_9, carta_capa_s, [0, 0]]
        star_wars["carta_19"] = ["b", carta_s_10, carta_capa_s, [0, 0]]
        star_wars["carta_20"] = ["b", carta_s_10, carta_capa_s, [0, 0]]
        star_wars["carta_21"] = ["b", carta_s_11, carta_capa_s, [0, 0]]
        star_wars["carta_22"] = ["b", carta_s_11, carta_capa_s, [0, 0]]
        star_wars["carta_23"] = ["b", carta_s_12, carta_capa_s, [0, 0]]
        star_wars["carta_24"] = ["b", carta_s_12, carta_capa_s, [0, 0]]
        star_wars["carta_25"] = ["b", carta_s_13, carta_capa_s, [0, 0]]
        star_wars["carta_26"] = ["b", carta_s_13, carta_capa_s, [0, 0]]
        star_wars["carta_27"] = ["b", carta_s_14, carta_capa_s, [0, 0]]
        star_wars["carta_28"] = ["b", carta_s_14, carta_capa_s, [0, 0]]


        # Definindo o dicionário de Harry Potter
        harry_potter = {}
        harry_potter["carta_1"]  = ["b", carta_h_1, carta_capa_h, [0, 0]]
        harry_potter["carta_2"]  = ["b", carta_h_1, carta_capa_h, [0, 0]]
        harry_potter["carta_3"]  = ["b", carta_h_2, carta_capa_h, [0, 0]]
        harry_potter["carta_4"]  = ["b", carta_h_2, carta_capa_h, [0, 0]]
        harry_potter["carta_5"]  = ["b", carta_h_3, carta_capa_h, [0, 0]]
        harry_potter["carta_6"]  = ["b", carta_h_3, carta_capa_h, [0, 0]]
        harry_potter["carta_7"]  = ["b", carta_h_4, carta_capa_h, [0, 0]]
        harry_potter["carta_8"]  = ["b", carta_h_4, carta_capa_h, [0, 0]]
        harry_potter["carta_9"]  = ["b", carta_h_5, carta_capa_h, [0, 0]]
        harry_potter["carta_10"] = ["b", carta_h_5, carta_capa_h, [0, 0]]
        harry_potter["carta_11"] = ["b", carta_h_6, carta_capa_h, [0, 0]]
        harry_potter["carta_12"] = ["b", carta_h_6, carta_capa_h, [0, 0]]
        harry_potter["carta_13"] = ["b", carta_h_7, carta_capa_h, [0, 0]]
        harry_potter["carta_14"] = ["b", carta_h_7, carta_capa_h, [0, 0]]
        harry_potter["carta_15"] = ["b", carta_h_8, carta_capa_h, [0, 0]]
        harry_potter["carta_16"] = ["b", carta_h_8, carta_capa_h, [0, 0]]
        harry_potter["carta_17"] = ["b", carta_h_9, carta_capa_h, [0, 0]]
        harry_potter["carta_18"] = ["b", carta_h_9, carta_capa_h, [0, 0]]
        harry_potter["carta_19"] = ["b", carta_h_10, carta_capa_h, [0, 0]]
        harry_potter["carta_20"] = ["b", carta_h_10, carta_capa_h, [0, 0]]
        harry_potter["carta_21"] = ["b", carta_h_11, carta_capa_h, [0, 0]]
        harry_potter["carta_22"] = ["b", carta_h_11, carta_capa_h, [0, 0]]
        harry_potter["carta_23"] = ["b", carta_h_12, carta_capa_h, [0, 0]]
        harry_potter["carta_24"] = ["b", carta_h_12, carta_capa_h, [0, 0]]
        harry_potter["carta_25"] = ["b", carta_h_13, carta_capa_h, [0, 0]]
        harry_potter["carta_26"] = ["b", carta_h_13, carta_capa_h, [0, 0]]
        harry_potter["carta_27"] = ["b", carta_h_14, carta_capa_h, [0, 0]]
        harry_potter["carta_28"] = ["b", carta_h_14, carta_capa_h, [0, 0]]


        # Definir qual dicionário vai ser utilizado 
        if tema_escolido == "star_wars":
            dic_jogo = star_wars
            fundo = fundo_starwars
            #carta_capa = carta_capa_s
            
        if tema_escolido == "harry_potter":
            dic_jogo = harry_potter
            fundo = fundo_harrypotter
            #carta_capa = carta_capa_h

        if tema_escolido == "pokemon":
            dic_jogo = pokemon
            fundo = fundo_pokemon
            #carta_capa = carta_capa_p

        fundo = pygame.transform.scale(fundo, (1280, 800))
        fundo.blit(fundo, (0, 0))

        #print(dic_jogo)
        # Pega as posições das cartas e embaralha 
        lista_posicoes = [[40, 20], [200, 20], [360, 20], [520, 20], [680, 20], [840, 20], [1000, 20],
    [40, 190], [200, 190], [360, 190], [520, 190], [680, 190], [840, 190], [1000, 190],
    [40, 360], [200, 360], [360, 360], [520, 360], [680, 360], [840, 360], [1000, 360],
    [40, 530], [200, 530], [360, 530], [520, 530], [680, 530], [840, 530], [1000, 530]]
        
        random.shuffle(lista_posicoes)
        
        # Adicionar as posições para cada valor do dicionário
        i = 0
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lista_carta[3] = lista_posicoes[i]
            i += 1


# DEFININDO AS CONDIÇÕES INICIAIS DO JOGO, Usar a termologia "b" caso a carta esteja virada para baixo e "c" caso a carta esteja virada para cima
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        #tela.fill((0, 0, 0))

        # Esperar 5 segundo 
        #pygame.time.wait(5000)
        tela.blit(fundo, (0, 0))
        pygame.display.update()

        # Trocando todas as carta para ficarem viradas para cima 
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lista_carta[0] = "c"

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
        fundo = pygame.transform.scale(fundo, (1280, 800))
        fundo.blit(fundo, (0, 0))
        pygame.display.update()

        # Esperar 5 segundo 
        time.sleep(1.5)

        # Trocando todas as carta para ficarem viradas para baixo
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lista_carta[0] = "b"

        # Imprimir as cartas da forma atualizada delas  
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lado = lista_carta[0]
            if lado == "b":
                png_carta = lista_carta[2]
            if lado == "c":
                png_carta = lista_carta[1]
            posicao_x = lista_carta[3][0]
            posicao_y = lista_carta[3][1]
            # Salvando a carta na tela 
            tela.blit(png_carta, (posicao_x, posicao_y))

        # Atualiza a imagem das cartas virada para cima
        fundo = pygame.transform.scale(fundo, (1280, 800))
        fundo.blit(fundo, (0, 0))
        pygame.display.update()


        # Começar o loop do jogo 
        jogando= True
        while jogando:
     
        # ESCOLHA DA PRIMEIRA CARTA 
        #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # tela.fill((0, 0, 0))
            # Escolher uma carta e muda o status para virado para cima 
            # Criar um código que detecta a carta e slava em uma variavel
            clik = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseXcor, mouseYcor = event.pos
                    
                    for i, posicao in enumerate(lista_posicoes):
                        carta_x, carta_y = posicao
                        carta_largura = 320
                        carta_altura = 170
                        deslocamentox = -80
                        deslocamentoy = 0
                        
                        if carta_x - deslocamentox < mouseXcor < carta_x + carta_largura + deslocamentox and carta_y - deslocamentoy < mouseYcor < carta_y + carta_altura + deslocamentoy:
                            coordenada_da_carta_escolhida = lista_posicoes[i]
                            print("Carta 1 escolhida:", coordenada_da_carta_escolhida)
                            clik = True 

            if clik:
                # Salva em uma variavel a carta escolida de acordo com a sua cordenada
                for carta in dic_jogo:
                    lista_carta_1 = dic_jogo[carta]
                    cordenada = lista_carta_1[3]
                    if coordenada_da_carta_escolhida == cordenada:
                        carta_clik = carta

                print("Carta escolida", carta_clik)
                carta_escolida_1 = carta_clik
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



            # ESCOLHA DA SEGUNDA CARTA 
            #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                carta2 = True
                clik2 = False
                while carta2:

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseXcor, mouseYcor = event.pos
                            
                            for i, posicao in enumerate(lista_posicoes):
                                carta_x, carta_y = posicao
                                carta_largura = 320
                                carta_altura = 170
                                deslocamentox = -80
                                deslocamentoy = 0
                                
                                if carta_x - deslocamentox < mouseXcor < carta_x + carta_largura + deslocamentox and carta_y - deslocamentoy < mouseYcor < carta_y + carta_altura + deslocamentoy:
                                    coordenada_da_carta_escolhida = lista_posicoes[i]
                                    print("Carta  2 escolhida:", coordenada_da_carta_escolhida)
                                    clik2 = True 

                    if clik2:
                        # Salva em uma variavel a carta escolida de acordo com a sua cordenada
                        for carta in dic_jogo:
                            lista_carta = dic_jogo[carta]
                            cordenada = lista_carta[3]
                            if coordenada_da_carta_escolhida == cordenada:
                                carta_clik_2= carta

                        print("Carta escolida", carta_clik_2)
                        carta_escolida_2 = carta_clik_2
                        lista_carta_2 =  dic_jogo[carta_escolida_2] 
                        lista_carta_2[0] = "c" # Ver se de fato está atualiuzando o dicionário

                        # Imprimir as cartas da forma atualizada delas  
                        for carta in dic_jogo:
                            lista_carta = dic_jogo[carta]
                            lado      = lista_carta [0]
                            if lado == "b":
                                png_carta = lista_carta [2]
                            if lado == "c":
                                png_carta = lista_carta [1]
                            posicao_x = lista_carta [3][0]
                            posicao_y = lista_carta [3][1]
                            # Salvando a carta na tela 
                            tela.blit(png_carta, (posicao_x, posicao_y))

                        # Atualiza a imagem das cartas virada para cima
                        pygame.display.update()
                        carta2 = False  

                # Verifico se as cartas são iguais 
                png_imagem_escolhida_1 = lista_carta_1[1]   
                png_imagem_escolhida_2 = lista_carta_2[1]
                        
                if png_imagem_escolhida_1 != png_imagem_escolhida_2:
                    # Espero 3 segundos 
                    time.sleep(1)
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
                    #print(dic_jogo)



                # Verifico que todas estão viradas para cima 
                v = "t"
                for carta in dic_jogo:
                    list_carta = dic_jogo[carta]
                    posicao_carta = list_carta[0]
                    if posicao_carta == "b":
                        v = "f" 
                if v == "t":
                    print("Todas as cartas estão para cima ")
                    jogo == False
                else:
                    print("Ainda tem carta para baixo")
                if  event.type == pygame.QUIT:
                    jogo = False
                    # Acabou o jogo 

                carta2 = False