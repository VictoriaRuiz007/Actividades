#menus
servicio = ""
ubicacion = ""

def menu_servicios():
    print("Servicios:\n\n 1. Servicio de frenos y engrasado\n 2. Lavado\n 3. Pintura\n 4. Especial(Todo)")
    global servicio
    try:
        servicio = input("Escoja su servicio: ")
        if servicio.isdigit and servicio in [1, 2, 3, 4]:
            print("Servicio agendado.")
        else:
            raise ValueError("Ingresa un servicio válido") 
    except ValueError:
        print("")


def menu_ubicaciones():
    print("Ubicaciones:\n\n 1. Concepción\n 2. Puente Alto\n 3. Muelle Barón\n 4. Muelle Vergara ")
    global ubicacion
    try:
        ubicacion = input("Escoja su ubicación: ")
        if ubicacion.isdigit and ubicacion in [1, 2, 3, 4]:
            print("Ubicación seleccionada.")
        else:
            raise ValueError("Ingresa una ubicacion válida.")
    except ValueError:
        print("")

print("Bienvenid@ a la aplicación de Rock.")
print("")

#usuario
try:
    rut = input("Ingrese su rut: ")
    if rut.isdigit() and len(rut) <= 9:
        print("Rut ingresado correctamente.")
    else:
        raise ValueError
except ValueError:
    print("Ingrese un rut correcto.")

try:
    nombre = input("Ingrese su nombre: ")
    if nombre.isalpha():
        print("Mucho gusto, ", nombre)
    else:
        raise ValueError
except ValueError:
    print("Ingrese un nombre válido.")
                
#menu principal
while True:
    print("")


    #bucle menu
    while True:
        try:
            print("Menú\n\n 1. Servicios\n 2. Ubicaciones\n 3. Resumen")
            opcion = input("Escoja una opción numéricamente(1/2/3): ")

            if opcion == "1":
                menu_servicios()
                print("")
                try:
                    volver = input("¿Desea volver al menú? S/N")
                    if volver in ["Y", "y"]:
                        break
                    elif volver in ["N", "n"]:
                        continue
                    else:
                        raise ValueError
                except ValueError:
                    print("Escoja una opción válida")

            elif opcion == "2":
                menu_ubicaciones()
                print("")
                try:
                    volver = input("¿Desea volver al menú? S/N")
                    if volver in ["Y", "y"]:
                        break
                    elif volver in ["N", "n"]:
                        continue
                    else:
                        raise ValueError
                except ValueError:
                    print("Escoja una opción válida")

            elif opcion == "3":
                print("Usuario: ", nombre, "\nSu pedido actual es de un servicio de: ", servicio, "\nEn el sector de: ", ubicacion)
                try:
                    volver = input("¿Desea volver al menú? S/N")
                    if volver in ["Y", "y"]:
                        break
                    elif volver in ["N", "n"]:
                        continue
                    else:
                        raise ValueError
                except ValueError:
                    print("Escoja una opción válida")

            elif opcion not in [1, 2, 3]:
                raise ValueError
        
        except ValueError:
            print("Ingrese una opción válida.")

#finalización





#la gran cadena de autoservicio rock requiere realizar 
#su nueva aplicacion para gestionar un menu de entradas 
#para realizar las distintas compras a nivel nacional
#el menu debe tener 5 opciones. 
#1) ingresar usuario(rut, nombre)
#2) servicio de frenos, engrasado 
#3) lavado 
#4) pintura 
#5) especial(todo)
#menu 2: ubicaciones: 
#1) concepcion, 
#2) pte alto, 
#3) muelle varon
#4) muelle vergara, 
#5) continuar o salir