from Ejercicio2_17 import sumatorio_digitos
from src.P2_1_EjerciciosCondicionales.Ejercicio1_4 import par_impar


def pedir_num():
    num = int(input("Introduce un numero entero: "))
    while num < -1:
        print("### ERROR ### - Por favor introduce un numero entero mayor o igual que -1")
        int(input("--> "))
    return num


def cuantos_par():
    num = None
    contador_par = 0
    while num != -1:
        num = pedir_num()
        if num != -1:
            num = sumatorio_digitos(num)
            print("Sumatorio de digitos =", num)
            if par_impar(num) == "par":
                contador_par += 1
    return contador_par


def main():
    cantidad = cuantos_par()
    if cantidad != 1:
        print("Has introducido", cantidad, "sumatorios par")
    else:
        print("Has introducido", cantidad, "sumatorio par")


if __name__ == "__main__":
    main()
