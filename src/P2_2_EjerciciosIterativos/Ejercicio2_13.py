def escribir_texto():
    texto = ""
    while texto.upper() != "SALIR":
        texto = input("--> ")
        if texto.upper() != "SALIR":
            print(texto)


def main():
    escribir_texto()


if __name__ == "__main__":
    main()
