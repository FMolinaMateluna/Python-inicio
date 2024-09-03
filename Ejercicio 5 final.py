"""Importamos random para poder elegir los numeros al azar para nuestra tupla, luego 
buscamos el mayor y menor de estos numeros y devolvemos todo."""
import random
def ganador_loteria():
    loteria = [random.randint(0, 100) for x in range(15)]
    loteria_tupla = tuple(loteria) #Convertimos la lista a tupla
    print ("Numeros sorteados", loteria_tupla)
#Buscamos mayor y menor de la tupla
    mayor_loteria = max(loteria_tupla)
    menor_loteria = min(loteria_tupla)
    print("El número mayor ganador es:", mayor_loteria)
    print("El número menor ganador es:", menor_loteria)
    return loteria_tupla
"""En esta funcion recibimos un numero del usuario y verificamos mediante el uso de try except 
para que identifique todo aquel valor que no es un numero o numero entero"""
def loteria_positivo():
    numero = input ("Introduzca aqui su numero entero positivo: ")
    try:
        numero = int(numero)
#Comprobamos mediante una condicional si es positivo
        if numero < 0:
                print("El número introducido no es positivo, vuelve a intentarlo.")
                return loteria_positivo()
#Para las excepciones utilizamos el mismo metodo
    except ValueError:
        try:
            decimal = float(numero) #Convertimos el numero a decimal
            if decimal != int(decimal): # Si el decimal es diferente al entero, es numero decimal
                print ("El numero es decimal, por favor ingresa un numero entero positivo")
                return loteria_positivo()
#Todo lo que no sea un caracter numero lo arroja como error
        except ValueError:
                print("El valor introducido no es un número, vuelve a intentarlo.")
                return loteria_positivo()
    return numero
"""En esta funcion vamos a comprobar si el usuario introdujo un numero igual al de la tupla, y
caso que haya una igualdad o mas se definira su premio"""
def definicion_ganador(loteria_tupla, numero):
#Constantes de premios
    PREMIO = 15
    EXTRA = 5
    if numero in loteria_tupla:
        repeticion = loteria_tupla.count(numero) #Identifica si el numero se encuentra
        if repeticion > 1: #Caso que este mas de una vez gana extra
            total_extra = ((repeticion * EXTRA) + PREMIO)
            print(f"Felicidades!!El numero {numero} es ganador y se encuentra repetido {repeticion} veces!¡Has ganado {total_extra}€!")
        else:
            print(f"Felicidades!!El numero {numero} es ganador! Tu premio es de {PREMIO}€!")
    else:
        print(f"Lo siento, El numero {numero} no se encuentra, no has ganado nada.")
#Funcion final para definir si el usuario sigue jugando o no
def final_juego():
        juego_nuevo = input("¿Desea volver a intentarlo?").upper()
        if juego_nuevo == "no":
            print ("Te deseamos suerte la proxima! Hasta luego.")
# Si el usuario quiere volver a jugar, llamamos a las funciones para que el juego vuelva a comenzar
        elif juego_nuevo == "si":
            numero = loteria_positivo()
            loteria_tupla = ganador_loteria()
            definicion_ganador(loteria_tupla,numero)
            final_juego()
        else:
            print ("No hemos logrado entender su respuesta. Repítala, por favor.")
            final_juego()
# Finalmente llamamos a todas las funciones para que el juego se lleve a cabo.
numero = loteria_positivo()
loteria_tupla = ganador_loteria()
definicion_ganador(loteria_tupla, numero)
final_juego()



