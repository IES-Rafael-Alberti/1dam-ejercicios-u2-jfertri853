def introducir_nums():
    num = None
    cadena = ""
    while num != 0:
        num = int(input("Introduce un numero: "))
        if num > 0:
            cadena += str(num)
    return cadena


def contar_par_impar_digitos(cadena_num):
    cadena_num = str(cadena_num)
    par = 0
    impar = 0
    for i in cadena_num:
        if int(i) % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar


def main():
    numeros = introducir_nums()
    cantidades = contar_par_impar_digitos(numeros)
    print("Has introducido " + str(cantidades[0]) + " numeros pares y " + str(cantidades[1]) + " impares")


if __name__ == "__main__":
    main()
