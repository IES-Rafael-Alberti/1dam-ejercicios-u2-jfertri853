# ¿Se puede hacer sin cortar el flujo del bucle con un return antes de tiempo?
def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def pedir_num():
    num = input("Introduce un numero entero: ")
    while not num.isnumeric() or int(num) < 1:
        num = input("Introduce un numero entero(positivo): ")
    return int(num)


def main():
    numero = pedir_num()
    resultado = es_primo(numero)
    if resultado:
        print("EL numero", numero, "es primo")
    else:
        print("El numero", numero, "NO es primo")


if __name__ == "__main__":
    main()
