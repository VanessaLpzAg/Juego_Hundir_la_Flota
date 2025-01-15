
import random
from utils import *


"""
INICIALIZAMOS LOS TABLEROS.
"""
tablero_ordenador = tablero()

tablero_jugador = tablero()


"""
GENERAMOS LOS BARCOS.
"""
barcos_ordenador = generar_barcos()

barcos_jugador = generar_barcos()

"""
COLOCAMOS LOS BARCOS.
"""
tablero_ordenador = colocar_barcos(barcos_ordenador, tablero_ordenador)

tablero_jugador = colocar_barcos(barcos_jugador, tablero_jugador)

"""
MOSTRAR LOS TABLEROS INICIALES.
"""
print("Tablero del Jugador (con barcos ocultos):")
mostrar_tablero(tablero_jugador)

print("\nTablero del Ordenador (con barcos ocultos):")
mostrar_tablero(tablero_ordenador)

"""
VARIABLES PARA EL JUEGO.
"""
vidas = 5               # Del jugador
vidas_ordenador = 5     # Del ordenador
turno = "jugador"       # Turno de quien juega

"""
BUCLE PRINCIPAL DEL JUEGO.
"""
while vidas > 0 and vidas_ordenador > 0:

        if turno == "jugador":
        # Turno del jugador: disparar.
            print("\nTurno del Jugador")
            entrada_usuario = input("Jugador, introduzca sus coordenadas (x,y): ")                          

            try:
                casilla_jugador = [tuple(map(int, coordenada.split(','))) for coordenada in entrada_usuario.split()]
                print(f"Disparo del jugador: {casilla_jugador}")            
                tablero_ordenador = disparar(casilla_jugador, tablero_ordenador)
                # Mostrar tablero del ordenador pero sin barcos, para saber donde impactan los disparos.
                print("\nTablero del Ordenador despues de tus disparos")
                mostrar_tablero(tablero_ordenador)
                # Cambiar al turno del ordenador
                turno = "ordenador"  
    
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar coordenadas en el formato correcto (x,y).")
                entrada_usuario = input("")

            # Verificar si el jugador ha quedado sin vidas.
            if vidas <= 0:
                print("Fin del juego. ¡EL ORDENADOR HA GANADO!")
                # Termina el bucle si el jugador se queda sin vidas
                break
            
    
        else:        
             
        # Turno del ordenador: disparar
            print("\nTurno del Ordenador")
            bombas_pc = generar_coordenadas_disparos(tablero_jugador)
            print(f"Disparo del ordenador: {bombas_pc}")
            tablero_jugador = disparar(bombas_pc, tablero_jugador)
            # Mostrar tablero del jugador pero sin barcos, para saber donde impactan los disparos del ordenador.
            print("\nTablero del Jugador despues del disparo del ordenador")
            mostrar_tablero(tablero_jugador)
            # Cambiar al turno del jugador
            turno = "jugador"

            # Verificar si el ordenador ha quedado sin vidas
            if vidas_ordenador <= 0:
                print("Fin del juego. ¡HAS GANADO!")
                # Termina el bucle si el ordenador se queda sin vidas
                break  
            

else:
    if vidas <= 0 or vidas_ordenador <= 0:
        print("Fin del juego")












