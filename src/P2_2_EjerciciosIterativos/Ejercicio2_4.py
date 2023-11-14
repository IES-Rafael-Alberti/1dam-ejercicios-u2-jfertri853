def pedir_num():
    num = int(input("Introduce un numero: "))
    while num < 0:
        num = int(input("###Error### - Introduce un numero entero positivo: "))
    return num


def cadena_comas(num):
    cadena = ""
    for i in range(num, -1, -1):
        if i == 0:
            cadena += str(i) + "."
        else:
            cadena += str(i) + ", "
    return cadena


def main():
    numero = pedir_num()
    print(cadena_comas(numero))


if __name__ == "__main__":
    main()
