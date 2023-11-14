def piramide_impares(num):
    bloque = ""
    piramide = ""
    for i in range(1, num * 2, 2):
        bloque = str(i) + " " + bloque
        piramide += bloque + "\n"
    return piramide


def pedir_num():
    num = input("Introduce un numero entero: ")
    while not num.isnumeric() or int(num) < 1:
        num = input("Introduce un numero entero(positivo): ")
    return int(num)


def main():
    numero_bloques = pedir_num()
    print(piramide_impares(numero_bloques))


if __name__ == "__main__":
    main()
