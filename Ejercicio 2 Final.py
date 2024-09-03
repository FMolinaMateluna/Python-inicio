#Creamos una funcion para calcular el numero de alumnos desaprobados
def no_aprobados(notas):
    desaprobados = sum(1 for nota in notas.values() if nota < 5)
    return desaprobados
#Agrupamos las notas de los alumnos en una variable por cada idioma haciendo uso de un diccionario
notas_latin = {"alumno1":8, "alumno2":7, "alumno3":10, "alumno4":4, "alumno5":9}
print("Los alumnos desaprobados en latín son:", no_aprobados(notas_latin))
notas_castellano = {"alumno1":8, "alumno2":6, "alumno3":7, "alumno4":4, "alumno5":8}
print("Los alumnos desaprobados en castellano son:", no_aprobados(notas_castellano))
notas_frances = {"alumno1":9, "alumno2":7, "alumno3":8, "alumno4":3, "alumno5":9}
print("Los alumnos desaprobados en francés son:", no_aprobados(notas_frances))
notas_ingles = {"alumno1":4, "alumno2":2, "alumno3":9, "alumno4":2, "alumno5":6}
print("Los alumnos desaprobados en inglés son:", no_aprobados(notas_ingles))
# Notas de los alumnos descriptas en diccionario
alumno_1 = {"Latin":8,"Castellano":8,"Frances":9,"Ingles":4}
alumno_2 = {"Latin":7,"Castellano":6,"Frances":7,"Ingles":2}
alumno_3 = {"Latin":10,"Castellano":7,"Frances":8,"Ingles":9}
alumno_4 = {"Latin":4,"Castellano":4,"Frances":3,"Ingles":2}
alumno_5 = {"Latin":9,"Castellano":8,"Frances":9,"Ingles":6}
''' Calculamos la media de las notas obtenidas por los alumnos mediante un bucle for, 
y con el resultado obtenido mediante una condicional calculamos que alumnos aprobaron 
y cuales no'''
total_clase = [alumno_1, alumno_2, alumno_3, alumno_4, alumno_5]
aprobados = []
desaprobados = []
for i, alum in enumerate(total_clase, start = 1):
    suma_notas = sum(alum.values())
    total_notas = len(alum)
    media = suma_notas / total_notas
    if media >= 5:
            aprobados.append(f"alumno_{i}")
    else:
            desaprobados.append(f"alumno_{i}")
    print(f"La nota promedio del alumno {i} es: {media}")
#Devolvemos los alumnos aprobados y desaprobados
print(f"Los alumnos aprobados son", "," .join(aprobados))
print(f"Los alumnos desaprobados son", "," .join(desaprobados))
    