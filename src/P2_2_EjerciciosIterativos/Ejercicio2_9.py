from src.P2_1_EjerciciosCondicionales.Ejercicio1_2 import verificar_login
from src.P2_1_EjerciciosCondicionales.Ejercicio1_2 import introducir_clave


def chequear_clave(verified_pass: str, inserted_pass: str):
    while verified_pass.upper().replace(" ", "") != inserted_pass.upper().replace(" ", ""):
        print("### ERROR ### - La contraseña no coincide, prueba otra vez")
        inserted_pass = introducir_clave()
    return True


def main():
    password = "Better_Call SAUL!!!"
    clave = introducir_clave()
    verificar_login(chequear_clave(password, clave))


if __name__ == "__main__":
    main()
