lista_peliculas = []

#funcion volver



print("Editor menú Netflix")

while True:
    print("1. Añadir películas\n 2. Eliminar películas\n 3. Lista peliculas")
    try:
        opcion = int(input("Elija una opcion(1/2): "))
        if opcion == 1:
            while True:
                nombre = input("Nombre de la pelicula: ")
                print("Tipos de película:\n1.Acción\n2.Ciencia Ficción\n3.Terror\n4.Comedia")
                while True:
                    try:
                        tipo = input("Género: ")
                        if tipo.isalpha() and tipo.lower() in ["accion", "ciencia ficcion", "terror", "comedia"]:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Escoja un tipo correcto")
                        continue
                while True:
                    try:
                        duracion = int(input("Duracion de la pelicula: "))
                        if duracion > 0:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Ingrese una duracion valida")
                        continue

                volver = input("¿Desea ingresar otra pelicula?(Y/N): ")
                if volver in ["Y", "y"]:
                    pelicula = {"Nombre": nombre, "Tipo": tipo, "Duración": duracion}
                    lista_peliculas.append(pelicula)
                    continue
                elif volver in ["N", "n"]:
                    pelicula = {"Nombre": nombre, "Tipo": tipo, "Duración": duracion}
                    lista_peliculas.append(pelicula)
                    print("Peliculas exitosamente agregadas")
                    break

        elif opcion == 2:
            while True:
                for indice, pelicula in enumerate(lista_peliculas, start=1):
                    print(f"{indice}) {pelicula}")
                try:
                    borrar = int(input("Elija una pelicula para eliminar: "))
                    if borrar > 0 and borrar <= len(lista_peliculas):
                        borrar = lista_peliculas.pop(borrar - 1)
                        print("Pelicula eliminada correctamente")
                    else:
                        raise ValueError
                except ValueError:
                    print("Elija una pelicula válida")

                volver = input("¿Desea eliminar otra pelicula?(Y/N): ")
                if volver in ["Y", "y"]:
                    continue
                elif volver in ["N", "n"]:
                    break               

        elif opcion not in [1, 2]:
            raise ValueError
    except ValueError:
        print("Elija una opcion valida")






#la empresa netflix solicita mejorar su menu de seleccion. añadir titulo y luego opciones
#1) añadir peliculas -> 1) accion, 2) ciencia ficcion, 3) terror, 4) comedia, 5)salir menu
#2) tiempo duracion de pelicula, opcion para salir
