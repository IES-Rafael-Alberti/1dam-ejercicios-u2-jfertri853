def crear_piramide(num):
    bloque = "*"
    piramide = ""
    for i in range(1, num + 1):
        piramide += (bloque * i) + "\n"
    return piramide


def pedir_num():
    num = input("Introduce un numero entero: ")
    while not num.isnumeric() or int(num) < 1:
        num = input("Introduce un numero entero(positivo): ")
    return int(num)


def main():
    keops = pedir_num()
    print(crear_piramide(keops))


if __name__ == "__main__":
    main()
