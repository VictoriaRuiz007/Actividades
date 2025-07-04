import re

print("Almacenamiento de datos DUOC UC")

#nombre
def func_nombre():
    while True:
        try:
            nombre = input("Ingrese nombre de estudiante: ")
            if nombre.isalpha():
                print("Nombre ingresado correctamente")
                print("")
                break
            else:
                raise ValueError
        except ValueError:
            print("Nombre no válido, debe contener solamente carácteres.")
            continue

#apellido
def func_apellido():
    while True:
        try:
            apellido = input("Ingrese el apellido del estudiante: ")
            if apellido.isalpha():
                print("Apellido ingresado correctamente")
                print("")
                break
            else:
                raise ValueError
        except ValueError:
            print("Apellido no válido, debe contener solamente carácteres.")
            continue

#rut
def func_rut():
    while True: 
        try:
            rut = int(input("Ingrese el rut del alumno: "))
            if "-" in rut and rut.replace("-", "") and len.rut(8, 9):
                print("Rut ingresado correctamente.")
                print("")
                break
            elif not re.search(r"[0-9]", rut):
                raise ValueError("El rut solo debe contener números")
            elif re.search(r"[.]" or r"[""]", rut):
                raise ValueError("El rut no debe contener puntos ni espacios")
        except ValueError as e:
            print(e)

#





#duoc debe desarrollar un sistema para almacenar los datos de cada uno de sus estudiantes: nombre, apellido, rut, correo, carrera(ingenieria, analista, gastronomia).(power bi)
#ingenieria: desarrollo web, desarrollo movil, desarrollo de escritorio
#analista: analisis de datos, limpieza de datos, creacion de datos(dashboard)
#gastronomia: historia gastronomia, alimentos naturales y procesados, sopaipillas 2