def repetir10(palabra):
    return palabra * 10


def repetir10_saltos(palabra):
    return (palabra + "\n") * 10


def repetir10_bucle(palabra):
    cadena = ""
    for i in range(0, 10):
        cadena += palabra
    return cadena


def repetir10_bucle_saltos(palabra):
    cadena = ""
    for i in range(0, 10):
        cadena += palabra + "\n"
    return cadena


def main():
    print(repetir10(input("Introduce una palabra: ")))
    print(repetir10_saltos(input("Introduce una palabra: ")))
    print(repetir10_bucle(input("Introduce una palabra: ")))
    print(repetir10_bucle_saltos(input("Introduce una palabra: ")))


if __name__ == "__main__":
    main()
