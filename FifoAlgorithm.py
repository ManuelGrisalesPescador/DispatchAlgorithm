import pygame
import copy, sys, Button


WIDTH = 1000
HEIGHT = 600
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 20)
pygame.display.set_caption("FIFO Algorithm")

BackButton = pygame.image.load('Imgs/BackButton.png').convert_alpha()

def CalcFIFO(Process):
    OutTime = 0
    FisnishTime = 0

    InTimes = []
    Times = []

    for Proc in Process:
        InTimes.append(Proc.tiempo_llegada)
        Times.append(Proc.tiempo_total)

    Ts = []
    Tf = []

    TEspera = 0
    TSistema = 0

    for x in Times:
        FisnishTime += x
        Tf.append(FisnishTime)
        Ts.append(OutTime)
        OutTime += x
        
    FinalTimes = Tf
    StartTimes = Ts

    for Ts, InTime in zip(Ts,InTimes):
        TEspera += (Ts - InTime)

    TEspera = TEspera / len(Times)

    for Tf, InTime in zip(copy.copy(Tf), InTimes):
        TSistema += (Tf - InTime)

    TSistema = TSistema / len(InTimes)
    Gantt = []

    for Start, Final, n, Process in zip(StartTimes, FinalTimes, range(len(Process)), Process):
        Gantt.append((f"P{n+1}", Start, Final, Process.color))

    return Gantt, TEspera, TSistema


def DisplayFIFO(Gantt):
    bar_height = 30
    y_spacing = 10
    max_time = max([fin for _, _, fin, _ in Gantt])
    x_unit = (WIDTH - 300) / max_time

    # Dibujar ejes
    pygame.draw.line(screen, BLACK, (200, 100), (200, HEIGHT - 100), 2)
    pygame.draw.line(screen, BLACK, (200, HEIGHT - 100), (WIDTH - 100, HEIGHT - 100), 2)

    # Dibujar cuadrícula
    for x in range(0, max_time + 1):
        pygame.draw.line(screen, BLACK, (200 + x * x_unit, 100), (200 + x * x_unit, HEIGHT - 100), 1)
        text_n = font2.render(f"{x}", True, BLACK)
        screen.blit(text_n, (200 + x * x_unit, HEIGHT - 90))

    for proceso, inicio, fin, color in Gantt:
        Process = int(proceso[1])

        y = HEIGHT - ((bar_height + y_spacing) * (Process - 1)) - 130

        pygame.draw.rect(screen, color, (200 + inicio * x_unit, y, (fin - inicio) * x_unit, bar_height))
        text = font.render(proceso, True, BLACK)
        screen.blit(text, (150, y + bar_height // 2 - text.get_height() // 2))


def draw_info(tiempo_espera_promedio, tiempo_sistema_promedio):
    text_te = font.render(f"Te: {tiempo_espera_promedio:.2f}", True, BLACK)
    text_ts = font.render(f"Ts: {tiempo_sistema_promedio:.2f}", True, BLACK)
    screen.blit(text_te, (10, HEIGHT - 60))
    screen.blit(text_ts, (10, HEIGHT - 30))

def draw_legend(procesos):
    legend_y = 120
    for i in range(len(procesos)):
        proceso = procesos[i]
        pygame.draw.rect(screen, proceso.color, (WIDTH - 80, legend_y, 20, 20))
        text = font.render(proceso.nombre, True, BLACK)
        screen.blit(text, (WIDTH - 50, legend_y))
        legend_y += 30



def main(Process):
    BackB = Button.Button(50, 25, BackButton, screen, pygame)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill((255,255,255))
        

        pos = pygame.mouse.get_pos()
        BackB.Draw(pos)
        if BackB.Action:
            running = False


        Ans, Te, Ts = CalcFIFO(Process)
        DisplayFIFO(Ans)
        draw_legend(Process)
        draw_info(Te, Ts)

        pygame.display.flip()