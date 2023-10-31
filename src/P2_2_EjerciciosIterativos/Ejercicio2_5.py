# Tengo las variables en inglés para no poner palabras con Ñ como variables
def calcular_inversion(years, money, interest):
    counter = 0
    while counter < years:
        money *= 1 + interest
        counter += 1
        if counter <= 1:
            print("Su dinero tras", counter, "año:", str("{:.2f}".format(money)), "$")
        else:
            print("Su dinero tras", counter, "años:", str("{:.2f}".format(money)), "$")
    money = float(str("{:.2f}".format(money)))
    return money


def pedir_inversion():
    years = int(input("Introduce cuantos años va a invertir: "))
    while years < 1:
        years = int(input("Introduce cuantos años va a invertir (MINIMO=1): "))
    dinero = float(input("Introduce cuanto dinero va a invertir: "))
    while dinero < 0.01:
        dinero = float(input("Introduce cuanto dinero va a invertir (MINIMO=0.01$)"))
    dinero = float(str("{:.2f}".format(dinero)))
    interes = int(input("Introduce el tipo de interes en porcentaje: "))
    while 1 > interes < 100:
        interes = int(input("Introduce el tipo de interes en porcentaje (1-100): "))
    interes /= 100
    return years, dinero, interes


def main():
    info_inversion = pedir_inversion()
    dinero_final = calcular_inversion(info_inversion[0], info_inversion[1], info_inversion[2])
    print("Su inversion ha generado: " + str(dinero_final) + " $")


if __name__ == "__main__":
    main()
