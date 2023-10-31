def division(dividendo, divisor):
    if divisor == 0:
        print("### ERROR ### - el divisor no puede ser 0")
    else:
        return float("{:.3f}".format(dividendo / divisor))


def crear_division():
    dividendo = float(input("Introduce el dividendo: "))
    divisor = float(input("Introduce el divisor: "))
    return dividendo, divisor


def main():
    numeros_div = crear_division()
    print("Resultado:", division(numeros_div[0], numeros_div[1]))


if __name__ == "__main__":
    main()
