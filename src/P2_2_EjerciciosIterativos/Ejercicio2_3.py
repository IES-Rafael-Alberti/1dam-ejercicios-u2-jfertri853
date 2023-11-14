def pedir_num():
    num = int(input("Introduce un numero: "))
    while num <= 0:
        print("El numero no puede ser negativo o 0")
        num = int(input("Introduce un numero positivo mayor que 0"))
    return num


def cadena_impar(num):
    cadena = ""
    num = int(num)
    for i in range(1, num + 1, 2):
        if i == num or i == num - 1:
            cadena += str(i) + "."
        else:
            cadena += str(i) + " - "
    return cadena


def main():
    numero = pedir_num()
    print(cadena_impar(numero))


if __name__ == "__main__":
    main()
