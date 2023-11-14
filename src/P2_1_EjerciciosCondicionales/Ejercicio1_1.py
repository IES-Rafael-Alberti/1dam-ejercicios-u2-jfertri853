def comprobar_edad(edad: int):
    if edad < 18:
        resultado = "menor"
    else:
        resultado = "mayor"
    return resultado


def pedir_edad():
    edad = input("Introduce tu edad: ")
    while not edad.isnumeric() or 1 > int(edad) or int(edad) > 125:
        edad = input("Introduce tu edad (1-125): ")
    return int(edad)


def main():
    print("eres", comprobar_edad(pedir_edad()), "de edad")


if __name__ == "__main__":
    main()
