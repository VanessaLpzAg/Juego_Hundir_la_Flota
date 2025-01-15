"""
Importar librería
"""
import numpy as np

import random


"""
Creamos el tablero en vacio de 10x10.
"""

def tablero(tamano=10):

    tablero= np.full((10,10), "_")

    return tablero


"""
CREAR BARCOS DE MANERA ALEATORIA.
"""

# Función para generar coordenadas aleatorias para los barcos, indicando ya que tablero es y que barcos son.
def generar_barcos():
    # Creamos un set para evitar solapamientos.
    tablero = set()
    
    # Creamos una lista vacia para ir alamcenando todos los barcos.
    barcos = []   

# Las diferentes esloras de los barcos, en el TABLERO.
    eslora = [2, 2, 2, 3, 3, 4] 

    for longitud in eslora:
        while True:
            # Seleccionar si el barco va horizontal o vertical
            orientacion = random.choice(['horizontal', 'vertical'])
            
            if orientacion == 'horizontal':
                # Seleccionamos coordenada (x, y) inicial aleatoria
                x = random.randint(0, 10 - longitud)  # Asegura que el barco cabe en el tablero.
                y = random.randint(0, 9)
                
                # Verificamos si hay espacio para colocar el barco en el tablero.
                posiciones = [(x + i, y) for i in range(longitud)] # Genera las posiciones del barco.

                if not any(pos in tablero for pos in posiciones):  # Recorre cada posicion generada y verifica si esta ya ocupada.
                    barcos.append(posiciones)   # Agrega las posiciones del barco a la lista barcos.
                    tablero.update(posiciones)  # Actualiza y marca las posiciones ocupadas.
                    break
            
            elif orientacion == 'vertical':
                # Seleccionamos coordenada (x, y) inicial aleatoria
                x = random.randint(0, 9)
                y = random.randint(0, 10 - longitud)  # Asegura que el barco cabe en el tablero
                
                # Verificamos si hay espacio para colocar el barco
                posiciones = [(x, y + i) for i in range(longitud)]  # Genera las posiciones del barco.

                if not any(pos in tablero for pos in posiciones):  # Recorre cada posicion generada y verifica si esta ya ocupada.
                    barcos.append(posiciones)  # Agrega las posiciones del barco a la lista barcos.
                    tablero.update(posiciones)  # Actualiza y marca las posiciones ocupadas.
                    break
    
    return barcos    # termina el ciclo actual, lo que indica que el barco ha sido colocado correctamente.   


"""
COLOCAR LOS BARCOS EN EL TABLERO (coloca una 'O' en las posiciones ocupadas por un barco).
"""
def colocar_barcos(barcos, tablero):
    # Recorrer las coordenadas de cada barco, para colocar una O en cada una de las coordenadas.
    for barco in barcos:
        for (x, y) in barco:        
        # Sustituir "_" por "O", para colocar el barco.
            if tablero[x, y] == "_":
                tablero[x, y] = "O"
                    
    return tablero

"""
GENERAR COORDENADAS ALEATORIAS PARA LOS DISPAROS.
"""
def generar_coordenadas_disparos(tablero):

    # Generar dentro del tablero.

    max_x = len(tablero) - 1            # Fila.
    max_y = len(tablero[0]) - 1         # Columna.

    # Generar coordenada aleatoria.

    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    return [(x, y)]

"""
DISPARAR EN EL TABLERO.
"""
vidas = 5               # Del jugador
vidas_ordenador = 5     # Del ordenador
turno = "jugador"       # Turno de quien juega


def disparar(casilla, tablero):

    # Usamos la variable global vidas
    global vidas 

    # Recorrer las coordenadas de la casilla introducida.
    for (x, y) in casilla:
        # Comprobar si hay acierto
        if tablero[x, y] == "O":
            tablero[x, y] = "X"
            print("TOCADO")
        # Comprobar si hay fallo y quitar una vida.
        elif tablero[x, y] == "_": 
            tablero[x, y] = "A"
            print("AGUA")
        # Contador de vidas, restando 1 vida cada vez que es agua.
            if vidas > 0:
                vidas -= 1
                print(f"Vidas restantes: {vidas}")
            if vidas <= 0:
                print("Te has quedado sin vidas")
           
    return tablero

"""
FUNCION PARA MOSTRAR LOS TABLEROS.
"""
# Imprimira el estado actual del tablero cada vez que se la llame.
def mostrar_tablero(tablero):
    for fila in tablero:
        # Mostrar las casillas con disparos (X o A) y dejar las casillas con barcos como barras bajas.
        print(" ".join([("_" if casilla == "O" else casilla) for casilla in fila]))