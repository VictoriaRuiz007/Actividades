print ("Contactos. Puedes almacenar un máximo de 20 contactos: ")

lista_contactos = []


#guardado contactos
while True:
    nombre = input("Nombre contacto: ")
    apellido = input("Apellido contacto: ")
    direccion = input("Direccion contacto: ")
    cumpleaños = input("Cumpleaños contacto: ")

    while True:
        nota = input("Ingrese una nota(max. 50 caracteres): ")
        if len(nota) > 50:
            print("La nota no puede superar los 50 caracteres")
        else:
            break

    contacto = f"Nombre: {nombre}\n, Apellido: {apellido}\n, Direccion: {direccion}\n, Cumpleaños: {cumpleaños}\n, Nota: {nota}\n\n\n"
   
    lista_contactos.append(contacto)

    salir = input("¿Desea agregar otro contacto?, Y/N: ").strip().lower()
    try:
        if salir in ["Y", "y"]:
            continue
        elif salir in ["N", "n"]:
            break

    except ValueError:
        print("Ingresa una eleccion valida entre y/n")

print("Contactos agregados correctamente.")


#contactos a txt e impresion
with open("contactos.txt", "w") as archivo:
    archivo.writelines(lista_contactos)

with open("contactos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contactos: ")
    print(contenido)















#samsung solicita para realizar su directorio agenda-contacto. la app debe almacenar nombre, apellido, direccion, fecha de cumpleaños y una nota de max 50 caracteres.
#la lista debe poder editar, guardar, eliminar(crud) 
#usar .txt y lista