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

CARTA_WIDTH = 120
CARTA_HEIGHT = 150

game = True

botao_starwars = pygame.image.load('botao_starwars.png').convert_alpha()
botao_harrypotter = pygame.image.load('botao_potter.png').convert_alpha()
botao_pokemon = pygame.image.load('botao_pokemon.png').convert_alpha()
imagem_tela_incial = pygame.image.load('imagens/bg inicio.jpg').convert()
carta_capa = pygame.image.load('capa_harrypotter.png').convert()
carta_1 = pygame.image.load('Captura de tela 2023-05-19 160445.png').convert()
carta_2 = pygame.image.load('Captura de tela 2023-05-19 160456.png').convert()
carta_3 = pygame.image.load('Captura de tela 2023-05-19 160518.png').convert()
fundo_harrypotter = pygame.image.load("imagens/fundo_harrypotter.jpg").convert()
fundo_starwars = pygame.image.load("imagens/fundo_starwars.png").convert()
fundo_pokemon = pygame.image.load("imagens/fundo_pokemon.png").convert()
titulo = pygame.image.load('imagens/titulo.png').convert_alpha()

imagem_tela_incial = pygame.transform.scale(imagem_tela_incial, (1280, 800))
titulo = pygame.transform.scale(titulo, (960, 540))
botao_pokemon = pygame.transform.scale(botao_pokemon, (1080, 400))
botao_harrypotter = pygame.transform.scale(botao_harrypotter, (1080, 400))
botao_starwars = pygame.transform.scale(botao_starwars, (1080, 400))
carta_1 = pygame.transform.scale(carta_1, (CARTA_WIDTH, CARTA_HEIGHT)) 
carta_2 = pygame.transform.scale(carta_2, (CARTA_WIDTH, CARTA_HEIGHT))
carta_3 = pygame.transform.scale(carta_3, (CARTA_WIDTH, CARTA_HEIGHT))
carta_capa = pygame.transform.scale(carta_3, (CARTA_WIDTH, CARTA_HEIGHT))


jogo = True 
Jogadas = True
tema = False


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
        '''pokemon = {}
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
        star_wars["carta_36"] = ["b", "foto_frente", "foto_trás", [0, 0]]'''

        # Definindo o dicionário de Harry Potter
        harry_potter = {}
        harry_potter["carta_1"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_2"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_3"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_4"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_5"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_6"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_7"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_8"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_9"]  = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_10"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_11"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_12"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_13"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_14"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_15"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_16"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_17"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_18"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_19"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_20"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_21"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_22"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_23"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_24"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_25"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_26"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_27"] = ["b", carta_2, carta_capa, [0, 0]]
        harry_potter["carta_28"] = ["b", carta_2, carta_capa, [0, 0]]



        # Definir qual dicionário vai ser utilizado 
        if tema_escolido == "star_wars":
            dic_jogo = star_wars
            fundo = fundo_starwars
            
        if tema_escolido == "harry_potter":
            dic_jogo = harry_potter
            fundo = fundo_harrypotter

        if tema_escolido == "pokemon":
            dic_jogo = pokemon
            fundo = fundo_pokemon

        fundo = pygame.transform.scale(fundo, (1280, 800))
        fundo.blit(fundo, (0, 0))

        print(dic_jogo)
        # Pega as posições das cartas e embaralha 
        lista_posicoes = [[40, 20], [200, 20], [360, 20], [520, 20], [680, 20], [840, 20], [1000, 20],
    [40, 190], [200, 190], [360, 190], [520, 190], [680, 190], [840, 190], [1000, 190],
    [40, 360], [200, 360], [360, 360], [520, 360], [680, 360], [840, 360], [1000, 360],
    [40, 530], [200, 530], [360, 530], [520, 530], [680, 530], [840, 530], [1000, 530]]



        #lista_posicoes = [[50, 50],[250, 50],[450, 50]]
        #random.shuffle(lista_posicoes)

        # Adicionar as posições para cada valor do dicionário
        i = 0
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lista_carta[3] = lista_posicoes[i]
            i += 1
        
        #print(dic_jogo)

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
        pygame.display.update()

        # Esperar 5 segundo 
        time.sleep(5)

        # Trocando todas as carta para ficarem viradas para cima 
        for carta in dic_jogo:
            lista_carta = dic_jogo[carta]
            lista_carta[0] = "b"

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


        # Começar o loop do jogo 
        jogando= True

        while jogando:

        # ESCOLHA DA PRIMEIRA CARTA 
        #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # tela.fill((0, 0, 0))
            # Escolher uma carta e muda o status para virado para cima 
            carta_escolida_1 = "carta_2"
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
            carta_escolida_2 = "carta_4"
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
            if  event.type == pygame.QUIT:
                jogo = False
                # Acabou o jogo '''


# Ultima atualização