# -*- coding: utf-8 -*-
import pygame

#Colores
BLANCO =  (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()

dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("The Luciano Game")
imagen_protagonista = pygame.image.load("personaje/image.png").convert()
imagen2_protagonista = pygame.image.load("personaje/image2.png").convert()
imagen_protagonista.set_colorkey(NEGRO)
imagen2_protagonista.set_colorkey(NEGRO)
pulsar_sonido = pygame.mixer.Sound("sonidos/qubodup-cfork-ccby3-jump.ogg")
fondo = pygame.image.load("fondo/fondo.png").convert()

#Cargo la fuente para el texto y defino el texto
miFunteSistema = pygame.font.SysFont("Bold",30)
miTexto = miFunteSistema.render("Gano la barra Violeta",0,(0,0,0))
miTexto2 = miFunteSistema.render("Gano la barra Cyan",0,(0,0,0))

#Posición de partida del protagonista
rect_x = 325
rect_y = 50

# Velocidad y dirección del protagonista
rect_cambio_x = 5
rect_cambio_y = 5

# Velocidad en píxeles por fotograma
x_speed_inferior = 0
x_speed_superior = 0
 
# Posición del bloque
x_coord = 500
y_coord = 450
a_coord = 500
b_coord = 50

hecho = False
arrancar = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            arrancar=True
            if evento.key == pygame.K_LEFT:
                x_speed_inferior = -6
            if evento.key == pygame.K_RIGHT:
                x_speed_inferior = 6
            if evento.key == pygame.K_a:
                x_speed_superior = -6
            if evento.key == pygame.K_d:
                x_speed_superior = 6
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                x_speed_inferior = 0
            if evento.key == pygame.K_RIGHT:
                x_speed_inferior = 0
            if evento.key == pygame.K_a:
                x_speed_superior = 0
            if evento.key == pygame.K_d:
                x_speed_superior = 0

    pantalla.blit(fondo, (0, 0))
    #Dibujamos el rectangulo y protagonista
    pygame.draw.rect(pantalla,(0,108,106),[x_coord, y_coord, 160,20])
    pygame.draw.rect(pantalla,(92,53,102),[a_coord, b_coord, 160,20])
    pantalla.blit(imagen2_protagonista, [rect_x,rect_y])
    
    # Mueve el punto de partida de la bola al presionar una tecla
    if arrancar:
        rect_x += rect_cambio_x
        rect_y += rect_cambio_y
        x_coord += x_speed_inferior
        a_coord += x_speed_superior
       #y_coord += y_speed
    
    # Cambia imagen cuando el personaje viene cayendo
    if rect_cambio_y < 0 :
        pantalla.blit(fondo, (0, 0))
        #pantalla.fill(NEGRO)
        pantalla.blit(imagen_protagonista, [rect_x,rect_y])
    pygame.draw.rect(pantalla,(0,108,106),[x_coord, y_coord, 160,20])
    pygame.draw.rect(pantalla,(92,53,102),[a_coord, b_coord, 160,20])

    # Rebota contra los bordes y el bloque (GLITCH ARREGLADO)
    if rect_y == 420:
        if rect_x > x_coord and rect_x <(x_coord + 160):
            rect_cambio_y = rect_cambio_y * -1
            pulsar_sonido.play()

    if rect_y == 50:
        if rect_x > a_coord and rect_x <(a_coord + 160):
            rect_cambio_y = rect_cambio_y * -1
            pulsar_sonido.play()
            
    if rect_x > 650 or rect_x < 0:          
        rect_cambio_x = rect_cambio_x * -1   
        
    if rect_y < 0:          
        rect_cambio_y = rect_cambio_y * -1

    # No se pasa de largo el bloque en los bordes
    if x_coord > 526:
    	x_coord = 525

    if a_coord > 526:
    	a_coord = 525

    if x_coord < 11:
    	x_coord = 10

    if a_coord < 11:
    	a_coord = 10

    
    # Se detine cuando cae 
    if rect_y > 460:
        rect_cambio_y = rect_cambio_x = 0

    if rect_y < 0:
        rect_cambio_y = rect_cambio_x = 0


    #Se mueven las barras cuando alguien pierde y avisa quien gano
    if rect_y < 0:
    	x_speed_inferior = -2
    	x_speed_superior = 2
        pygame.draw.rect(pantalla,(0,108,106),[255, 250, 200,20])
        pantalla.blit(miTexto2,(255,250))

    if rect_y > 460:
    	x_speed_superior = -2
    	x_speed_inferior = 2
        pygame.draw.rect(pantalla,(92,53,102),[255, 250, 200,20])
        pantalla.blit(miTexto,(255,250))

    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()
