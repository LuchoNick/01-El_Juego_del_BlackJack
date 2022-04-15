"""
Reglas específicas:
Para simplificar un poco el juego original, planteamos las reglas que deberán seguir en el desarrollo del presente TP1
(sin considerar las reglas completas del juego en un casino real):

Para el presente Trabajo Práctico se pide simular una única mano con un jugador contra el crupier.
Se debe determinar el ganador de la mano considerando quien haya alcanzado un puntaje más cercano a 21 sin pasarse.
A cada jugador se le pueden dar hasta 3 cartas, la tercera carta sólo dependerá del puntaje alcanzado con las dos anteriores y no es opcional para el usuario.
El AS vale 11 mientras no se pase de 21 y 1 en caso contrario tanto para el croupier como para el jugador.
Como es una sola jugada podemos considerar posible que se obtenga la misma carta en la jugada (tanto el mismo jugador, como el croupier).
No se considera el Blackjack o 21 natural
No hay apuestas en juego.
==================================================================================================================================================================
Requerimiento:
Se pide desarrollar un programa en Python que cumpla las siguientes consignas:

Simular la partida generando en forma aleatoria los valores de las cartas obtenidas por ambos participantes (número o figura y palo),
mostrando en cada caso la carta y el puntaje parcial que obtiene con la misma.
Determinar quién ha obtenido el mayor puntaje, el jugador o el croupier. Considerar que pueden empatar.
Determinar si el palo de la primera carta del jugador es el mismo que el obtenido por el croupier en su primera carta.
Si además de coincidir en el palo es el mismo número (tomando en consideración que las cartas se pueden repetir) o figura mostrar un mensaje adicional.
Determinar si salió al menos una figura.
"""


input("Hola que tal:")




