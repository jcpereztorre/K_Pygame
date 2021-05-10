import pygame as pg
import sys
from random import randint

def rebotaX(x):
    if x <= 0 or x >= ANCHO:
        return -1
    
    return 1

def rebotaY(y):
    if y <= 0 or y >= ALTO:
        return -1
    return 1

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

bolas = []
for _ in range(10):
    bola = {'x': randint(0, ANCHO),
            'y': randint(0, ALTO),
            'vx':randint(5, 10),
            'vy':randint(5, 10),
            'color': (randint(0, 255), randint(0, 255), randint(0, 255))
    }
    bolas.append(bola)

game_over = False
while not game_over:
    reloj.tick(60)
    # Gestión de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

# Modificación de estado
    for bola in bolas:
        bola['x'] += bola['vx']
        bola['y'] += bola['vy']
        
        bola['vx'] *= rebotaX(bola['x'])
        bola['vy'] *= rebotaY(bola['y'])


    # Gestión de la pantalla
    pantalla.fill(NEGRO) # Borra la pantalla antes de pintar
    for bola in bolas:
        pg.draw.circle(pantalla, bola['color'], (bola['x'], bola['y']), 10) # circle(surface, color, center, radius) -> Rect
   
    pg.display.flip()

pg.quit()
sys.exit()
