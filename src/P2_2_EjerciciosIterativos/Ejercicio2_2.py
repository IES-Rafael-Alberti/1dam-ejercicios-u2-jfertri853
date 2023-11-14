def pedir_edad():
    edad = input("Introduce tu edad: ")
    while not edad.isnumeric() or 1 > int(edad) or int(edad) > 125:
        edad = input("Introduce tu edad (0-125): ")
    return int(edad)


def contar_edad(edad):
    cadena = ""
    for i in range(1, edad + 1):
        if i == edad:
            cadena += str(i) + "."
        else:
            cadena += str(i) + " - "
    return cadena


def main():
    edad = pedir_edad()
    print(contar_edad(edad))


if __name__ == "__main__":
    main()
