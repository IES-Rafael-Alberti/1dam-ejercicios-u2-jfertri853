def contar_digitos(cadena: str):
    counter = 0
    for i in cadena:
        if i.isnumeric():
            counter += 1
    return counter


def introducir_lineas():
    libro = None
    lineas_completas = 0
    digit_counter = 0
    while libro != "*":
        libro = input("Libro: ")
        if libro != "/":
            digit_counter += contar_digitos(libro)
        else:
            print("Linea completa. Aparecen", digit_counter, "dígitos numéricos.")
            lineas_completas += 1
            digit_counter = 0
    return lineas_completas


def main():
    print("Se leyeron " + str(introducir_lineas()) + " líneas completas.")


if __name__ == "__main__":
    main()
