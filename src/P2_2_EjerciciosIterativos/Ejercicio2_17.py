def sumatorio_digitos(num):
    num = str(num)
    sumatorio = 0
    for i in num:
        sumatorio += int(i)
    return sumatorio


def main():
    numero = int(input("Introduce un numero entero: "))
    print("El sumatorio de los digitos es", sumatorio_digitos(numero))


if __name__ == "__main__":
    main()
