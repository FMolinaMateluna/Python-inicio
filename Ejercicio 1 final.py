'''La primera funcion la usamos para que el usuario introduzca su numero, y verificamos mediante
el uso de try except para que identifique todo aquel valor que no es un numero o numero entero'''
def numero_positivo():
    numero = input ("Introduzca aqui su numero entero positivo: ")
    try:
#Convertimos el numero ingresado a entero y comparamos con el numero real
        numero = int(numero)
#Si es entero, ahora comprobamos mediante una condicional si es positivo
        if numero < 0:
            print("El número introducido no es positivo, vuelve a intentarlo.")
            return numero_positivo()
#Para las excepciones utilizamos el mismo metodo
    except ValueError:
        try:
            decimal = float(numero) #Convertimos el numero a decimal
            if decimal != int(decimal): # Si el decimal es diferente al entero, es numero decimal
                print ("El numero es decimal, por favor ingresa un numero entero positivo")
                return numero_positivo()
#Todo lo que no sea un caracter numero lo arroja como error
        except ValueError:
            print("El valor introducido no es un número, vuelve a intentarlo.")
            return numero_positivo()
    return numero
'''En una nueva funcion utilizamos el numero obtenido de la funcion anterior para comprobar
si es primo o no'''
numero = numero_positivo()
def num_primo(numero):
#Todos los numero menores o igual a 1 no son primos
    if numero <= 1:
        return False
#Mediante un bucle identificamos si el numero tiene algun divisor
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
#Caso no cumpla ninguna de estas condiciones el numero es primo 
    return True
#Esta funcion final es para emitir el mensaje al usuario si el numero es o no primo
def resultado_primo(numero):
    if num_primo(numero):
        return f"El numero {numero} es primo."
    else:
        return f"El numero {numero} no es primo."
# Devolvemos el numero final 
print (resultado_primo(numero))