def tributa(edad: int, ingresos: float):
    if edad > 16 and ingresos >= 1000:
        return True
    else:
        return False


def main():
    edad1 = int(input("Introduce tu edad: "))
    ingresos_mensuales1 = float(input("Introduce tus ingresos mensuales: "))
    print("Tributas:", tributa(edad1, ingresos_mensuales1))


if __name__ == "__main__":
    main()
