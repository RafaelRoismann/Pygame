import pygame

class Carta(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect.x = x
        self.rect.y = y

#carta1 = Carta(imagem_carta, 100, 100) - define a carta
#tela.blit(carta1.image, carta1.rect) - blita a carta na tela