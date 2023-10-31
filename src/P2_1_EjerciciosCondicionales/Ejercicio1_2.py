def chequear_clave(verified_pass: str, inserted_pass: str):
    if verified_pass.upper().replace(" ", "") == inserted_pass.upper().replace(" ", ""):
        return True
    else:
        return False


def verificar_login(acceso: bool):
    if acceso:
        print("Contraseña correcta, puedes entrar")
    else:
        print("Incorrecto!")


def introducir_clave():
    clave = input("Introduce tu contraseña: ")
    return clave


def main():
    password = "El.señor.de.los.PEPINILLOS"
    verificar_login(chequear_clave(password, introducir_clave()))


if __name__ == "__main__":
    main()
