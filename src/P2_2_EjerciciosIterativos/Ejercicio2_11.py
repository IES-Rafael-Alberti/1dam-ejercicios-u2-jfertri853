# Por favor no testear con la cadena "arroz"
def palabra_reversa_separada(palabra: str):
    palabra = palabra.replace(" ", "")
    reverse = ""
    for i in range(len(palabra) - 1, -1, -1):
        reverse += palabra[i] + " "
    return reverse


def main():
    frase = input("Introduce una palabra o frase: ")
    print(palabra_reversa_separada(frase))


if __name__ == "__main__":
    main()
