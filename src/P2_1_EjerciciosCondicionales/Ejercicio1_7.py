def calcular_porcentaje_renta(renta_anual):
    if renta_anual < 10000:
        return 0.05
    elif renta_anual < 20000:
        return 0.15
    elif renta_anual < 35000:
        return 0.2
    elif renta_anual < 60000:
        return 0.3
    else:
        return 0.45


def calcular_impuestos(renta_anual, porcentaje_renta):
    return float("{:.2f}".format(renta_anual * porcentaje_renta))


def pedir_renta_anual():
    renta = float(input("Introduce tu renta anual: "))
    while renta < 0:
        renta = float(input("Introduce tu renta anual (no puede ser negativa): "))
    return renta


def main():
    renta = pedir_renta_anual()
    porcentaje = calcular_porcentaje_renta(renta)
    impuestos = calcular_impuestos(renta, porcentaje)
    print("Tienes que pagar " + str(impuestos) + " euros")


if __name__ == "__main__":
    main()
