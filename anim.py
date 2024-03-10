import pygame
import sys
from collections import deque
import Button

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Dimensiones de la pantalla
WIDTH = 1000
HEIGHT = 600

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Round Robin Scheduler")

# Fuente
font = pygame.font.SysFont(None, 30)

BackButton = pygame.image.load('Imgs/BackButton.png').convert_alpha()

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

def round_robin(procesos, Q):
    cola = deque()
    pendientes = deque()

    tiempo_actual = 0
    indice_proceso_actual = 0
    tiempo_espera_total = 0
    tiempo_sistema_total = 0
    cola.append(procesos[indice_proceso_actual])
    indice_proceso_actual += 1

    gantt = []

    while True:
        if not cola:
            if indice_proceso_actual >= len(procesos):
                break
            else:
                tiempo_actual = procesos[indice_proceso_actual].tiempo_llegada
                continue

        proceso_actual = cola.popleft()
        if proceso_actual.tiempo_inicio_ejecucion is None:
            proceso_actual.tiempo_inicio_ejecucion = tiempo_actual
        gantt.append((proceso_actual.nombre, tiempo_actual, tiempo_actual + min(Q, proceso_actual.tiempo_restante), proceso_actual.color))
        tiempo_actual += min(Q, proceso_actual.tiempo_restante)
        proceso_actual.tiempo_restante -= Q

        # Verificar si hay procesos que han llegado durante la ejecución de este proceso
        while indice_proceso_actual < len(procesos) and procesos[indice_proceso_actual].tiempo_llegada <= tiempo_actual:
            cola.append(procesos[indice_proceso_actual])
            indice_proceso_actual += 1

        if pendientes:
            pendiente = pendientes.popleft()
            cola.append(pendiente)

        if proceso_actual.tiempo_restante > 0:
            pendientes.append(proceso_actual)
        else:
            proceso_actual.tiempo_finalizacion = tiempo_actual
            tiempo_espera_total += proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_total - proceso_actual.tiempo_llegada
            tiempo_sistema_total += proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada

    tiempo_espera_promedio = tiempo_espera_total / len(procesos)
    tiempo_sistema_promedio = tiempo_sistema_total / len(procesos)

    return gantt, tiempo_espera_promedio, tiempo_sistema_promedio

def draw_gantt(gantt):
    bar_height = 30
    y_spacing = 10
    max_time = max([fin for _, _, fin, _ in gantt])
    x_unit = (WIDTH - 300) / max_time
    FirstHeight = HEIGHT - (len(gantt) * (bar_height + y_spacing)) - 100

    # Dibujar ejes
    pygame.draw.line(screen, BLACK, (200, 100), (200, HEIGHT - 100), 2)
    pygame.draw.line(screen, BLACK, (200, HEIGHT - 100), (WIDTH - 100, HEIGHT - 100), 2)

    # Dibujar cuadrícula
    for x in range(0, max_time + 1):
        pygame.draw.line(screen, BLACK, (200 + x * x_unit, 100), (200 + x * x_unit, HEIGHT - 100), 1)

    # Ordenar procesos por orden de llegada
    gantt.sort(key=lambda x: x[1])

    for proceso, inicio, fin, color in gantt:
        Process = int(proceso[1])

        if Process != 1:
            y = (((bar_height + y_spacing) + ((bar_height + y_spacing) * (Process - 2))) + (FirstHeight))
        else:
            y = FirstHeight

        pygame.draw.rect(screen, color, (200 + inicio * x_unit, y, (fin - inicio) * x_unit, bar_height))
        text = font.render(proceso, True, BLACK)
        screen.blit(text, (150, y + bar_height // 2 - text.get_height() // 2))
        #y += bar_height + y_spacing

def draw_info(tiempo_espera_promedio, tiempo_sistema_promedio):
    text_te = font.render(f"Te: {tiempo_espera_promedio:.2f}", True, BLACK)
    text_ts = font.render(f"Ts: {tiempo_sistema_promedio:.2f}", True, BLACK)
    screen.blit(text_te, (10, HEIGHT - 60))
    screen.blit(text_ts, (10, HEIGHT - 30))

def draw_legend():
    legend_y = 120
    for i in range(len(procesos)):
        proceso = procesos[i]
        pygame.draw.rect(screen, proceso.color, (WIDTH - 80, legend_y, 20, 20))
        text = font.render(proceso.nombre, True, BLACK)
        screen.blit(text, (WIDTH - 50, legend_y))
        legend_y += 30



def main(Process, Q):
    global procesos
    # Procesos de ejemplo
    proceso1 = Proceso("P1", 6, 0)
    proceso2 = Proceso("P2", 4, 2)
    proceso3 = Proceso("P3", 2, 4)

    procesos = Process

    # Quantum
    #Q = 2

    # Ordenar procesos por tiempo de llegada
    procesos.sort(key=lambda x: x.tiempo_llegada)

    # Ejecutar algoritmo Round Robin
    gantt, tiempo_espera_promedio, tiempo_sistema_promedio = round_robin(procesos, Q)

    BackB = Button.Button(50, 25, BackButton, screen, pygame)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_gantt(gantt)
        draw_info(tiempo_espera_promedio, tiempo_sistema_promedio)
        draw_legend()
        pos = pygame.mouse.get_pos()
        BackB.Draw(pos)
        if BackB.Action:
            running = False
        pygame.display.flip()

    

#if __name__ == "__main__":
#    main()
