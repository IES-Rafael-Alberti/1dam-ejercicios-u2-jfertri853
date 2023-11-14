# He preferido llamar a una función dentro de otra antes que anidar bucles.
# ¿Es una buena práctica?
def tabla_multip(num_tabla: int):
    tabla = "Tabla del " + str(num_tabla) + ": "
    for i in range(1, 11):
        if i == 10:
            tabla += str(num_tabla * i) + "."
        else:
            tabla += str(num_tabla * i) + " - "
    return tabla


def imprimir_tablas_multip():
    for i in range(1, 11):
        print(tabla_multip(i))


def main():
    imprimir_tablas_multip()


if __name__ == "__main__":
    main()
    