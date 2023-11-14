def asignacion_grupo(nombre, sexo):
    if (nombre[0].upper() < "M" and sexo == "F") or (nombre[0].upper() > "N" and sexo == "M"):
        return "Grupo A"
    else:
        return "Grupo B"


def rellenar_ficha_alumno():
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce una M si eres masculino y una F si eres femenino: ").upper()
    while sexo != "M" and sexo != "F":
        sexo = input("Introduce una M si eres masculino y una F si eres femenino: ").upper()
    return nombre, sexo


def main():
    ficha_alumno = rellenar_ficha_alumno()
    print("Perteneces al " + asignacion_grupo(ficha_alumno[0], ficha_alumno[1]))


if __name__ == "__main__":
    main()
