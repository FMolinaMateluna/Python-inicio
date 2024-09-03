import random
#Definimos el rango de numeros posibles al azar
def dados():
    return random.randint (1,6)
# Mostramos los numeros obtenidos por los jugadores  
def resultados ():
    dado_1 = dados()
    dado_2 = dados()
    print ("Resultados Jugador 1:", dado_1, "y", dado_2)
    dado_3 = dados()
    dado_4 = dados()
    print ("Resultados Jugador 2:", dado_3, "y", dado_4)
# Mediante una condicional comparamos los dados para saber que jugador gano la partida
    if dado_1 == dado_2 or dado_3 == dado_4:
        return 1
    elif dado_1 == dado_3 or dado_1 == dado_4:
        return 1
    elif dado_2 == dado_3 or dado_2 == dado_4:
        return 1
    else:
        return 2   
''' Creamos una funcion para el juego donde se repetira para 3 rondas, 
acumulando los resultados de cada una, y devolviendo quien gano en cada ronda'''
def jugar_partida():
    jugador_1 = 0
    jugador_2 = 0
    while jugador_1 < 3 and jugador_2 < 3:
        ganador_ronda = resultados()
        if ganador_ronda == 1:
            jugador_1 += 1
            print("Gana el Jugador 1")
        else:
            jugador_2 += 1
            print("Gana el Jugador 2")
#Definimos el ganador de toda la partida mediante una condicional
    if jugador_1 == 3:
        print("Felicidades ¡El Jugador 1 gano la partida!")
    else:
        print("Felicidades ¡El Jugador 2 gano la partida!")
# Mediante una funcion conseguimos saber si el juego continuara o no
def nueva_partida():
    otra_vez = input("¿Desea jugar otra partida?. Responda SI o NO").upper()
    if otra_vez == "SI":
        jugar_partida()
        nueva_partida ()
    elif otra_vez == "NO":
        print ("Gracias por jugar, hasta pronto!")
    else:
        print ("Respuesta no valida, intente de nuevo")
        nueva_partida()
#Llamamos a las funciones principales  
jugar_partida()
nueva_partida()