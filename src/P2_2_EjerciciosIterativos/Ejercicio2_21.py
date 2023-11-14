def introducir_monto():
    monto = None
    total = 0
    contador = 1
    while monto != 0:
        monto = float(input("Introduce el precio del monto numero " + str(contador) + ": "))
        if monto > 0:
            contador += 1
            total += monto
        elif monto < 0:
            print("### ERROR ### - Los montos no puede ser negativos")
    return total


def precio_final(precio):
    if precio > 1000:
        precio = precio * 0.9
    return float(str("{:.2f}".format(precio)))


def main():
    coste = introducir_monto()
    print("El coste final es de:", precio_final(coste), "$")


if __name__ == "__main__":
    main()
