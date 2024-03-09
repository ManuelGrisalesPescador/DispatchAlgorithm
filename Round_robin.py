from collections import deque

class Proceso:
    def __init__(self, nombre, tiempo_total, tiempo_llegada):
        self.nombre = nombre
        self.tiempo_total = tiempo_total
        self.tiempo_restante = tiempo_total
        self.tiempo_llegada = tiempo_llegada

def round_robin(procesos, Q):
    cola = deque()
    tiempo_actual = 0
    indice_proceso_actual = 0

    while True:
        # Agregar procesos a la cola de ejecución si han llegado durante la ejecución de otro proceso
        while indice_proceso_actual < len(procesos) and procesos[indice_proceso_actual].tiempo_llegada <= tiempo_actual:
            cola.append(procesos[indice_proceso_actual])
            indice_proceso_actual += 1

        if not cola:
            if indice_proceso_actual >= len(procesos):
                break
            else:
                tiempo_actual = procesos[indice_proceso_actual].tiempo_llegada
                continue

        proceso_actual = cola.popleft()
        print(f"Procesando {proceso_actual.nombre} desde el tiempo {tiempo_actual} hasta {tiempo_actual + min(Q, proceso_actual.tiempo_restante)}")
        tiempo_actual += min(Q, proceso_actual.tiempo_restante)
        proceso_actual.tiempo_restante -= Q

        # Verificar si hay procesos que han llegado durante la ejecución de este proceso
        while indice_proceso_actual < len(procesos) and procesos[indice_proceso_actual].tiempo_llegada <= tiempo_actual:
            cola.append(procesos[indice_proceso_actual])
            indice_proceso_actual += 1

        if proceso_actual.tiempo_restante > 0:
            cola.append(proceso_actual)
        else:
            print(f"{proceso_actual.nombre} ha terminado en el tiempo {tiempo_actual}")

# Procesos de ejemplo
proceso1 = Proceso("P1", 2, 0)
proceso2 = Proceso("P2", 4, 1)
proceso3 = Proceso("P3", 6, 2)
proceso4 = Proceso("P4", 10, 2)
proceso5 = Proceso("P5", 8, 3)
proceso6 = Proceso("P6", 4, 4)

# Quantum
Q = 2

# Ordenar procesos por tiempo de llegada
procesos = [proceso1, proceso2, proceso3, proceso4, proceso5, proceso6]
procesos.sort(key=lambda x: x.tiempo_llegada)

# Ejecutar algoritmo Round Robin
round_robin(procesos, Q)

#TODO: Calculo de Te y Ts