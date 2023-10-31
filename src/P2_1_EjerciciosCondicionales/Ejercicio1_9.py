def precio_entrada(edad):
    edad = int(edad)
    if edad < 4:
        return 0
    elif edad in range(4, 18):
        return 5
    else:
        return 10


def pedir_edad():
    edad = input("Introduce tu edad: ")
    while not edad.isnumeric() or 0 > int(edad) or int(edad) > 125:
        edad = input("Introduce tu edad (0-125): ")
    return int(edad)


def main():
    edad1 = pedir_edad()
    precio1 = precio_entrada(edad1)
    print("Tu entrada cuesta " + str(precio1) + "€")


if __name__ == "__main__":
    main()
