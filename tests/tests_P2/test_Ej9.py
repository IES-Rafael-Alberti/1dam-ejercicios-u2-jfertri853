import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_9 import chequear_clave


@pytest.mark.parametrize(
    "clave_correcta, clave_intento, expected",
    [
        ("Abuelo", "abuelo", True),
        ("BETTERCALLSAUL", "better call saul", True),
        ("mickey mouse", "MICKEYMOUSE", True)
    ]
)
def test_params_chequear_clave(clave_correcta, clave_intento, expected):
    assert chequear_clave(clave_correcta, clave_intento) == expected
    