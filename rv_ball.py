import pygame as pg # para no tener que escribir "pygame" en vez de "pg" en todo el código.

pg.init() # inicia todo el proceso de PYGAME, después montar bucle principal
pantalla = pg.display.set_mode((600, 400)) # Crea la pantalla
pg.display.set_caption("Hola") # Título de la pantalla


game_over = False

while not game_over:

    # Gestión de eventos
     for evento in pg.event.get():
         pass

    # Gestión del estado

    # Refrescar pantalla

     pantalla.fill ((0, 255, 0)) # Pinta el color de la pantalla (RGB (Red, Green, Blue))

     pg.display.flip() # Manda la pantalla a la memoria de la tarjeta gráfica (pinta la pantalla)
     




