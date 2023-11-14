from Ejercicio2_10 import es_primo


def pedir_num():
    num = int(input("Introduce un numero: "))
    while num < 0:
        print("### ERROR ### - No puedes introducir numeros menores que 0")
        num = int(input("Introduce un numero: "))
    return num


def contar_primos():
    num = None
    primos = 0
    while num != 0:
        num = pedir_num()
        if es_primo(num) and num != 0:
            primos += 1
    return primos


def main():
    print("Has introducido", str(contar_primos()), "numeros primos")


if __name__ == "__main__":
    main()
