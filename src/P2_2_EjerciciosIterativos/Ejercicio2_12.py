def contar_easy(frase: str, letra: str):
    frase = frase.upper()
    letra = letra.upper()
    return "La letra (" + letra + ") aparece " + str(frase.count(letra)) + " veces"


def contar(frase: str, letra: str):
    apariciones = 0
    for i in frase:
        if i.upper() == letra.upper():
            apariciones += 1
    return apariciones


def main():
    phrase = input("Frase: ")
    letter = input("Letra: ")
    print(contar_easy(phrase, letter))
    print("Tu letra aparece " + str(contar(phrase, letter)) + " veces en la frase (" + phrase + ")")


if __name__ == "__main__":
    main()
