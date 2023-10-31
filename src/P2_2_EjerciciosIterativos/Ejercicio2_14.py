def bucle_sumatorio():
    sumatorio = 0
    num = None
    while num != 0:
        num = int(input("--> "))
        sumatorio += num
    return sumatorio


def main():
    print("La suma de los numeros ingresados es igual a", bucle_sumatorio())


if __name__ == "__main__":
    main()
