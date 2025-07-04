print("Bienvenid@ al servicio de urgencia del Hospital Central de Santiago.\n A continuación, deberá ingresar sus datos e información del caso: ")

#rut y validacion
print("Ingrese su rut, sin puntos y con guión.")
try:
    rut = input("RUT del paciente: ")
    if "-" in rut and rut.replace("-", "").isdigit() and len.rut(8):
        print("Rut ingresado correctamente")
        
    else:
        raise ValueError
except ValueError:
    print("Ingrese el rut nuevamente.")


#nombre y apellido y validacion
print("")
try:
    nombre = input("Nombre del paciente: ")
    if nombre.isalpha():
        print("")
    else:
        raise ValueError
except ValueError:
    print("Nombre inválido.")

try:
    apellido = input("Apellido del paciente: ")
    if apellido.isalpha():
        print("")
    else:
        raise ValueError
except ValueError:
    print("Apellido inválido.")

print("Nombre y apellido ingresados correctamente.")


#lista patologías
print("")
print("A continuación, seleccione una patología numericamente: ")
print("1. Heridas punzopenetrantes\n2. Virus\n3.Hemorragis\n4. Reacciones alérgicas\5. Deshidratación")
try: 
    patologia = input("Patología: ")
    if patologia.isdigit():
        print("Ingreso exitoso.")
    elif patologia not in [1, 2, 3, 4, 5]:
        raise IndexError
    else:
        raise ValueError
except ValueError or IndexError:
    print("Ingrese un número correcto y dentro del rango (1/5).")








#el hospital central de santiago solicita ayuda para mejorar el ingreso a la sala de urgencias, requiere un software. datos a solicitar del paciente:
#1) rut, caracteristicas del campo, validar guión en el rut y que no exceda de 8 caracteres y validar el numero de identificacion
#2) nombre y apellido del paciente, validar caracteristicas del campo y tipo de variable
#3) lista de patologias: heridas punzo penetrante, virus, hemorragias, reacciones alergicas, deshidratacion
#4) direccion del paciente, validar ubicacion de residencia. lista de comunas de la localidad(si no pertenece, se rechaza al paciente si no pertenece a region metropolitana)