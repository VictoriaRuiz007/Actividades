#region modulos
import re
#endregion


lista_compradores = []


#region opcion 1
def opc1():
    global nombre
    global tipo
    global codigo
    global comprador
    while True:
        try: 
            nombre = input("Ingrese el nombre al que desea dejar la entrada: ")
            if nombre.isalpha():
                print("Nombre ingresado correctamente")
                break
            else:
                raise ValueError
        except ValueError:
            print("Ingrese un nombre correcto")
            continue
    print("")
    
    while True:
        try:
            tipo = int(input("¿Qué tipo de entrada desea comprar?\n1. General($10.000)\n2. Vip($50.000)\nEntrada(1/2): "))
            if tipo in [1, 2]:
                print("Entrada elegida correctamente.")
                break
            else:
                raise ValueError
        except ValueError:
            print("Ingrese un tipo de entrada dentro de los presentados")
            continue
    print("")

    while True:
        try:
            codigo = input("Ingrese su código de confirmación. Este debe contener mínimo 6 carácteres, una mayúscula, un número y sin espacios: ")
            if len(codigo) < 6:
                raise ValueError("El código debe tener mas de 6 digitos")
            if not re.search(r"[A-Z]", codigo):
                raise ValueError("Su código debe contener al menos una mayúscula")
            if not re.search(r"[0-9]", codigo):
                raise ValueError("Su código debe contener al menos un número")
            if " " in codigo:
                raise ValueError("No pueden haber espacios en el codigo")
            else:
                print("Código guardado correctamente.")
                break
        except ValueError as e:
            print(e)
            continue
    comprador = f"Nombre: {nombre}, Entrada: {tipo}, Codigo: {codigo}"
    lista_compradores.append(comprador)

#endregion

#region opcion 2
def opc2():
    while True:
        busqueda = input("¿Qué usuario desea buscar?").lower
        if busqueda in [item.lower() for item in lista_compradores]:
            print("El usuario", busqueda, "ya existe.")
        else:
            print("El usuario no existe")
            break



#endregion

#region opcion 3
def opc3():
    while True:
        try:
            cancelar = input("Ingrese su usuario para cancelar la compra: ")
            if cancelar in lista_compradores:
                while True:
                    try:
                        contraseña_canc = input("Ingrese el código de confirmacion para cancelar: ")
                        if contraseña_canc == codigo:
                            print("Cancelación exitosa")
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Ingrese la contraseña correcta.")
                        continue
            else:
                raise ValueError
        except ValueError:
            print("Usuario no encontrado.")
            break



#endregion



print("Bienvenido al sistema de compra de entradas para el concierto de \"Noche de brujas\"")
print("")

while True:
    print(" M E N U ")
    print("1. Comprar entrada\n2. Consultar comprador\n3. Cancelar compra")
    try:
        opcion = int(input("Elija una opcion (1/3): "))
        if opcion == 1:
            opc1()
        elif opcion == 2:
            opc2()
        elif opcion == 3:
            opc3()
        else:
            raise ValueError
    except ValueError:
        print("Escoja una opción válida")
        continue








#realice un programa en python que permita generar un menu de gestión de entradas para el concierto de noche de brujas. 4 opciones principales:
#1) comprar entrada: se ingresa el nombre del comprador, tipo de entrada(general 10.000, vip 50.000) y codigo de confirmacion por separados. 
#   compra exitosa: nombre del comprador no debe repetirse, tipo de entrada general o vip, el codigo de confirmacion debe tener un minimo de 6 caracteres(una mayuscula,
#   una minuscula, un numero y sin espacios). entrada registrada exitosamente

#2) consultar comprador: el menu debe permitir buscar compradores por el nombre. si el comprador existe, deberia mostrar sus datos asociados: nombre, entrada y codigo
#   si no existe, comprador no existe


#3) cancelar compra: elimina un comprador con toda su informacion

#4) continuar o salir
#todas las opciones deben ser funciones separadas del codigo(main)
#
#
#
