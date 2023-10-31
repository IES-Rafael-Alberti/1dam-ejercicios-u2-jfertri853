def mostrar_menu():
    print("1 - Introduzca una nota")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")
    opcion = int(input("Seleccione una opción => "))
    elegir_proceso(opcion)


def introducir_nota():
    nota = int(input("Introduce una nota (0-10): "))
    while nota < 0 or nota > 10:
        nota = int(input("Introduce una nota (0-10): "))
    return nota


def set_notas(nota):
    misNotas.append(nota)


def get_notas():
    print("Notas = ", end="")
    for nota in misNotas:
        print(str(nota), end=" - ")
    print()


def elegir_proceso(opcion):
    if opcion != 1 and opcion != 2 and opcion != 3:
        print("### ERROR ### - La opción ingresada no existe")
        mostrar_menu()
    else:
        match opcion:
            case 1:
                set_notas(introducir_nota())
                mostrar_menu()
            case 2:
                get_notas()
                mostrar_menu()
            case 3:
                print("Cerrando el programa...")


def main():
    mostrar_menu()


misNotas = []
if __name__ == "__main__":
    main()
