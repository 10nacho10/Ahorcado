# Representaremos las palabras como listas.
# Reglas:
# · Solo se puede jugar hasta 2 jugadores minimo.
# · El jugador 1 elije una palabra y los otros tienen que adivinar que
#   palabra es.
# · Los jugadores comienzan colocando letras para adivinar la palabra.
# · Si un jugador coloca una palabra, puede ganar si la misma coincide
#   con la colocada, pero si no es el caso el jugador pierde la partida.
# · Cada vez que un jugador coloque mal una letra ira apareciendo el
#   el dibujo del cuerpo de una persona, cuando este dibujo llegue a
#   completarse(es decir que este conformado por cabeza, tronco,
#   brazos y piernas), el jugador si antes de que se forme el mismo
#   no adivino la palabra perdera.
# ahorcado: Str -> Str
# Entrega un string que es la palabra y devuelve si el jugador acerto
# o perdio.
def ahorcado():
    """Se gana cuando se adivino la palabra del jugador 1."""
    palabra = []
    lugares = []
    print(" ______________________________________________________")
    print("|                         __________                   |")
    print("|                         |         |                  |")
    print("|                         |        / \                 |")
    print("|                         |        \_/                 |")
    print("|                         |         |                  |")
    print("|                         |      ---|---               |")
    print("|                         |         |                  |")
    print("|                         |         |                  |")
    print("|                         |        / \                 |")
    print("|                         |       /   \                |")
    print("|                     ____|____                        |")
    print("|                                                      |")
    print("|               * Inserte J para jugar.                |")
    print("|                                                      |")
    print("|               * Inserte R para ver las reglas.       |")
    print("|                                                      |")
    print("|               * Inserte S para salir                 |")
    print("|______________________________________________________|")
    opcion = input(" Ingrese alguna opcion: ").upper
    if opcion == "S":
        exit()
    elif opcion == "R":
        print(" Reglas: ")
        print(" · Solo se puede jugar hasta 2 jugadores minimo.")
        print(" · El jugador 1 elije una palabra y los otros tienen que adivinar que \n  palabra es.")
        print(" · Los jugadores comienzan colocando letras para adivinar la palabra.")
        print(" · Si un jugador coloca una palabra, puede ganar si la misma coincide \n  con la colocada, pero si no es el caso el jugador pierde la partida.")
        print(" · Cada vez que un jugador coloque mal una letra ira apareciendo el \n  el dibujo del cuerpo de una persona, cuando este dibujo llegue a \n  el dibujo del cuerpo de una persona, cuando este dibujo llegue a \n  completarse(es decir que este conformado por cabeza, tronco, \n  brazos y piernas), el jugador si antes de que se forme el mismo \n  no adivino la palabra perdera.")
        return ahorcado()
    elif opcion == "J":
        terminar = 0
        palabra += input(" Jugador 1 ingrese su palabra: ")
        while n != len(palabra):
            lugares += 
        while terminar != 1:
            

        
    return ahorcado()
