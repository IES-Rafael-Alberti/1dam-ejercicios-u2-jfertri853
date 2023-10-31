def contar(frase: str, letra: str):
    posicion = None
    for i in range(0, len(frase)):
        if frase[i].upper() == letra.upper():
            posicion = i
            return posicion
        else:
            print("Posicion " + str(i) + ": NO se encuentra la letra " + letra + " -> " + frase[i])
    return posicion


def main():
    phrase = input("Frase: ")
    letter = input("Letra: ")
    position = contar(phrase, letter)
    if position is None:
        print("La letra (" + letter + ") no está en la frase: " + phrase)
    else:
        print("Se encontró la letra (" + letter + ") en la posicion " + str(position))


if __name__ == "__main__":
    main()
