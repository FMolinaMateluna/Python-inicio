def nueva_agenda():
    agenda = {}
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
# Confirmamos que el nombre no exista ya en la agenda
        if nombre in agenda:
            print("El nombre ya existe en la agenda. Por favor, inténtelo de nuevo.")
# Si no existe continuamos a colocar el numero y agregamos el contacto a la agenda.
            continue
        telefono = input("Ingrese el teléfono del contacto: ")
        agenda[nombre] = telefono
# Mediante un bucle preguntamos si quiere continuar o no.
        while True:
            nuevo_contacto = input("¿Desea agregar otro contacto? (SI/NO): ")
            if nuevo_contacto in ["SI", "NO"]:
                break
            else:
                print("Respuesta no válida. Por favor, responda 'SI' o 'NO'.")
#En el caso que no quiera continuar, el bucle termina para retornar la agenda
        if nuevo_contacto == "NO":
            break
    return agenda
#Lista ordenada de contactos nuevos
def lista_contactos(agenda):
    print("Agenda de contactos:")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre}, Teléfono: {telefono}")

# Creamos la agenda
agenda = nueva_agenda()

lista_contactos(agenda)