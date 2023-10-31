def bucle_sumatorio_positivo():
    sumatorio = 0
    num = None
    while num != 0:
        num = int(input("--> "))
        if num > 0:
            sumatorio += num
    return sumatorio


def main():
    print("La suma de los numeros positivos ingresados es igual a", bucle_sumatorio_positivo())


if __name__ == "__main__":
    main()
