import pygame as pg
import sys

ROJO = (255, 0 ,0)
AZUL = (0, 0 ,255)
VERDE = (0, 255 ,0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600


pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO))

game_over = False
x = ANCHO // 2
y = ALTO // 2
vx = -13
vy = -13
reloj = pg.time.Clock()

while not game_over:
    reloj.tick(60)
    # Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # modificacion del estado
    x += vx
    y += vy

    if y <= 0 or y>= ALTO:
        vy = -vy

    if x <= 0 or x >= ANCHO:
        vx = -vx
    
    # gestion de pantalla
    pantalla.fill(NEGRO)
    pg.draw.circle(pantalla, ROJO, (x, y), 10)

    pg.display.flip() # pasa a la tarjeta grafica

pg.quit()
sys.exit()
