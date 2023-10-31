def par_impar(numero: int):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"


def main():
    num1 = int(input("Introduce un numero: "))
    print("el numero", num1, "es", par_impar(num1))


if __name__ == "__main__":
    main()
