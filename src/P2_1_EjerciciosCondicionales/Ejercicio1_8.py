def rendimiento_empleado(puntuacion):
    rendimiento = None
    if puntuacion == 0.0:
        rendimiento = "Inaceptable"
    elif puntuacion == 0.4:
        rendimiento = "Aceptable"
    elif puntuacion >= 0.6:
        rendimiento = "Meritorio"
    return rendimiento


def calcular_plus(puntuacion):
    return float("{:.2f}".format(puntuacion * 2400))


def pedir_puntuacion():
    puntuacion = float(input("Introduce la puntuacion del empleado: "))
    puntuacion = float("{:.1f}".format(puntuacion))
    while puntuacion < 0.0 or (puntuacion != 0.0 and puntuacion != 0.4 and puntuacion != 0.6) and puntuacion < 0.6:
        puntuacion = float(input("Introduce la puntuacion del empleado: "))
        puntuacion = float("{:.1f}".format(puntuacion))
    return puntuacion


def main():
    puntuacion_empleado = pedir_puntuacion()
    print(puntuacion_empleado)
    print("El rendimiento es", rendimiento_empleado(puntuacion_empleado))
    print("Se te pagaran", calcular_plus(puntuacion_empleado), "euros mas este mes")


if __name__ == "__main__":
    main()
