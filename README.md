# Hundir la Flota 🛳️

**Hundir la Flota** (también conocido como Battleship) es un juego de estrategia por turnos desarrollado en Python. En esta versión, se introduce una variación especial: ¡cada vez que disparas y das al agua, pierdes una vida! 

## Descripción del Juego

El objetivo del juego es hundir todos los barcos del oponente antes de quedarte sin vidas. Los jugadores deberán elegir coordenadas en el tablero para disparar y tratar de acertar en las posiciones de los barcos enemigos.

### Características
- **Tablero personalizable:** Define el tamaño del tablero.
- **Sistema de vidas:** Los jugadores pierden una vida por cada disparo que falle.
- **Colocación de barcos aleatoria:** La disposición de los barcos es distinta en cada partida.
- **Modo un jugador:** Enfréntate al ordenador.
- **Retroalimentación inmediata:** El juego indica si has dado en el blanco, hundido un barco o disparado al agua.

## Requisitos

- Python 3.8 o superior
- Librerías estándar de Python (no requiere instalaciones adicionales)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/VanessaLpzAg/Juego_Hundir_la_Flota.git
   

2. Ejecuta el script principal:
bash
Copiar
Editar
python main.py

## Cómo Jugar
Ejecuta el programa y sigue las instrucciones en pantalla.
Introduce las coordenadas del disparo en el formato correcto (por ejemplo: 3,5).
Intenta hundir todos los barcos antes de que se terminen tus vidas.

1. Reglas
Cada disparo al agua reduce tu número de vidas.
Hundir un barco no recupera vidas.
El juego termina cuando:
Hundes todos los barcos (¡Victoria! 🎉).
Pierdes todas tus vidas (¡Derrota! 😢).

2. Estructura del Proyecto
plaintext
Copiar
Editar
hundir-la-flota/
main.py         # Script principal del juego
utils.py        # Juego
README.md       # Documentación del proyecto

3. Personalización
Puedes modificar el tamaño del tablero, el número de barcos y las vidas iniciales desde el archivo utils.py. Busca las variables configurables al inicio del script:

python
Copiar
Editar
TAMANO_TABLERO = 10  # Cambiar tamaño del tablero
NUMERO_BARCOS = 5    # Cambiar número de barcos
VIDAS_INICIALES = 20 # Cambiar número de vidas iniciales

Este proyecto está licenciado bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

¡Disfruta jugando y tratando de hundir la flota enemiga! 🚢💥