def mayor_ingresado():
    mayor = None
    num = None
    primera_vez = True
    while num != 0:
        num = int(input("--> "))
        if primera_vez and num != 0:
            mayor = num
            primera_vez = False
        if num == 0:
            print("Adios")
        elif num > mayor:
            mayor = num
    return mayor


def main():
    print("El numero mayor que has ingresado es el", mayor_ingresado())


if __name__ == "__main__":
    main()
