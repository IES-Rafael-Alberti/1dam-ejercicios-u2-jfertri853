def modificar_frase(frase: str):
    frase = frase.replace(",", "")
    frase = frase.replace(".", "")
    frase = frase.replace("?", "")
    frase = frase.replace("¿", "")
    frase = frase.replace("!", "")
    frase = frase.replace("¡", "")
    frase = frase.replace(":", "")
    frase = frase.replace(";", "")
    frase = frase.split(" ")
    for i in range(len(frase) - 1, 0, -1):
        if frase[i] == " " or frase[i] == "":
            frase.remove(frase[i])
    return frase


def search_longest_word(frase_enlistada):
    mayor = 0
    longest_word = None
    for i in frase_enlistada:
        longitud = len(i)
        if longitud > mayor:
            mayor = longitud
            longest_word = i
    return longest_word, mayor


def main():
    parrafo = input("Introduce una frase: ")
    parrafo = modificar_frase(parrafo)
    resultado = search_longest_word(parrafo)
    print("La palabra mas larga es", resultado[0], "con", resultado[1], "letras")


if __name__ == "__main__":
    main()
