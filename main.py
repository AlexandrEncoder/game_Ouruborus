import pygame
from  pygame.locals import*
from pygame import mixer
from sys import exit
from random import randint

pygame.init()
#driando tela
HEIGHT = 1200
WIDTH =  780

tela = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('OURUBORUS')
relogio = pygame.time.Clock()



devour_ouruborus = []

#tiro

#municao
tam_x = 4
tam_y = 7

#Comprimento incicial do ouruborus
initial_lenght = 5


def evolution_ouruborus(devour_ouruborus):
    for XeY in devour_ouruborus:
        #Lista XeY = [X,Y] Se eu pegar XeY[0] = vai valer  X caso eu pegue XeY[1] = vai valer o Y
        pygame.draw.rect(tela, (255,255,0), (XeY[0], XeY[1], 10, 10))


#Movimento
x_ouruborus = HEIGHT/2
y_ouruborus = WIDTH/2

x_control = 20
y_control = 20



#pontos iniciais
point = 0
# texto para os Pontos
font_point = pygame.font.SysFont('impact', 40, True, False)

# Movimento presa
x_presa = randint(40, 1100)
y_presa = randint(60, 700)

#Criar loop inifinito para manter o jogo rodando
while True:
# tempo de movimentacao
    relogio.tick(10)

 #TEXTO 
    mensagem = f'SOUL: {point}'   

# mensagem  
    texto_formatado = font_point.render(mensagem, True, (255,255,255))

# Esse comando faz com que a posição anterio na tela vire preto 
    tela.fill((0,0,0))

# PEgando eventos por for
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # Agora fazemos que com ao final da tela ele volte para o incio 
        if event.type == KEYDOWN:
            if event.key == K_a:
                x_control = -10
                y_control = 0
            if event.key == K_d:
                x_control =  10
                y_control = 0
            if event.key == K_w:
                y_control = -10
                x_control = 0
            if event.key == K_s:
                y_control =  10
                x_control = 0
            

            if event.key == K_p:
                if point > 0:
                    point = point - 1



    x_ouruborus = x_ouruborus + x_control
    y_ouruborus = y_ouruborus + y_control
    #Criando imagem com formar 
    ouruborus = pygame.draw.rect(tela, (255,255,0), (x_ouruborus,y_ouruborus,10,10))
    presa = pygame.draw.rect(tela, (0,255,0), (x_presa,y_presa,10,10))

#parametro para colisao onde ela vai sugir apos a colisao
    if ouruborus.colliderect(presa):
        x_presa = randint(40, 1100)
        y_presa = randint(60, 700)
        #cobra poder crescer mais 1
        point = point + 1
        initial_lenght = initial_lenght + 1


    tela.blit(texto_formatado, (900, 40))
# lista que sera usada para guardar posições para desenhar a cobra        
    cranium_ouruborus = []
    cranium_ouruborus.append(x_ouruborus)
    cranium_ouruborus.append(y_ouruborus)

    devour_ouruborus.append(cranium_ouruborus)
    
    if len(devour_ouruborus) >initial_lenght:
        del devour_ouruborus[0]
    
    evolution_ouruborus(devour_ouruborus)

    pygame.display.update()
