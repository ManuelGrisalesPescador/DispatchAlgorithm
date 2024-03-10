import pygame
from pygame.locals import *
import sys, copy, Button

import anim, FifoAlgorithm, SJFAlgorithm

WIDTH = 1000
HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()
font = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm")

ButtonFIFO = pygame.image.load('Imgs/ButtonFIFO.png').convert_alpha()
ButtonSJF = pygame.image.load('Imgs/ButtonSJF.png').convert_alpha()
ButtonRoundRobin = pygame.image.load('Imgs/ButtonRoundRobin.png').convert_alpha()
Imgs = [ButtonFIFO, ButtonSJF, ButtonRoundRobin]

class Proceso:
    def __init__(self, nombre, tiempo_total, tiempo_llegada):
        self.nombre = nombre
        self.tiempo_total = tiempo_total
        self.tiempo_restante = tiempo_total
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_inicio_ejecucion = None
        self.tiempo_finalizacion = None
        self.color = self.get_color(nombre)

    def get_color(self, nombre):
        colores = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
        return colores[int(nombre[1:]) % len(colores)]

Buttons = []

for x in range(3):
    XPosition = ((x * 141)) + 80
    DataButton = Button.Button(XPosition + (XPosition), 250, Imgs[x], screen, pygame)
    Buttons.append(DataButton)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255,255,255))
        pos = pygame.mouse.get_pos()
        

        for Button in Buttons:
            Button.Draw(pos)

        proceso1 = Proceso("P1", 6, 0)
        proceso2 = Proceso("P2", 4, 2)
        proceso3 = Proceso("P3", 2, 4)

        Q = 2

        procesos = [proceso1, proceso2, proceso3]

        if Buttons[0].Action:
            Buttons[0].Action = False
            print("B1")
            FifoAlgorithm.main(procesos)
        elif Buttons[1].Action:
            Buttons[1].Action = False
            print("B2")
            SJFAlgorithm.main(procesos)
        elif Buttons[2].Action:
            Buttons[2].Action = False
            print("B3")
            anim.main(procesos, Q)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
