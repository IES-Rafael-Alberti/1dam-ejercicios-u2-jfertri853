import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_2 import chequear_clave


@pytest.mark.parametrize(
    "input_clave, input_intento, esperado",
    [
        ("134b-f", "patata", False),
        ("flamenco", "flamenco", True),
        ("pata ta", "patata", True),
        ("FRESA", "fresa", True),
        ("kotlin", "KOTLIN", True),
        ("python3.11", "PYTHON 3.11", True),
        ("java8", "gava8", False)
    ]
)
def test_params_chequear_clave(input_clave, input_intento, esperado):
    assert chequear_clave(input_clave, input_intento) == esperado
