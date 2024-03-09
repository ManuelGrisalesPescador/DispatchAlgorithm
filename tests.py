# Posible implementación de calculo de Te y Ts

from collections import deque

class Proceso:
    def __init__(self, nombre, tiempo_total, tiempo_llegada):
        self.nombre = nombre
        self.tiempo_total = tiempo_total
        self.tiempo_restante = tiempo_total
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_inicio_ejecucion = None
        self.tiempo_finalizacion = None

def round_robin(procesos, Q):
    cola = deque()
    pendientes = deque()

    tiempo_actual = 0
    indice_proceso_actual = 0
    tiempo_espera_total = 0
    tiempo_sistema_total = 0
    cola.append(procesos[indice_proceso_actual])
    indice_proceso_actual += 1

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
        print(f"Procesando {proceso_actual.nombre} desde el tiempo {tiempo_actual} hasta {tiempo_actual + min(Q, proceso_actual.tiempo_restante)}")
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
            print(f"{proceso_actual.nombre} ha terminado en el tiempo {tiempo_actual}")
            tiempo_espera_total += proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_total - proceso_actual.tiempo_llegada
            tiempo_sistema_total += proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada

    tiempo_espera_promedio = tiempo_espera_total / len(procesos)
    tiempo_sistema_promedio = tiempo_sistema_total / len(procesos)
    print(f"Tiempo de espera promedio: {tiempo_espera_promedio}")
    print(f"Tiempo de sistema promedio: {tiempo_sistema_promedio}")


# Procesos de ejemplo 1
# proceso1 = Proceso("P1", 2, 0)
# proceso2 = Proceso("P2", 4, 1)
# proceso3 = Proceso("P3", 6, 2)
# proceso4 = Proceso("P4", 10, 2)
# proceso5 = Proceso("P5", 8, 3)
# proceso6 = Proceso("P6", 4, 4)
    
# Procesos de ejemplo 2
proceso1 = Proceso("P1", 6, 0)
proceso2 = Proceso("P2", 4, 2)
proceso3 = Proceso("P3", 2, 4)

# procesos = [proceso1, proceso2, proceso3, proceso4, proceso5, proceso6] #1

procesos = [proceso1, proceso2, proceso3] # 2


# Quantum
Q = 2

# Ordenar procesos por tiempo de llegada
procesos.sort(key=lambda x: x.tiempo_llegada)

# Ejecutar algoritmo Round Robin
round_robin(procesos, Q)


#El ejemplo 1 planteado es el realizado en el taller en clase 05 marzo 2024 (Quizás el taller quedó mal)
# resultado esperado
#Tiempo de espera promedio: 10.666666666666666
#Tiempo de sistema promedio: 16.333333333333332

# Resultado obtenido
#Tiempo de espera promedio: 13.666666666666666
#Tiempo de sistema promedio: 19.333333333333332

#El ejemplo 2 planteado es el realizado en clase 27 de febrero 2024
# resultado esperado
# Tiempo de espera promedio: 3.3333333333333335
# Tiempo de sistema promedio: 7.333333333333333

# Resultado obtenido
# Tiempo de espera promedio: 3.3333333333333335
# Tiempo de sistema promedio: 7.333333333333333