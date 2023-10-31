import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_4 import cadena_comas


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, "0."),
        (14, "14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0."),
        (1, "1, 0."),
        (5, "5, 4, 3, 2, 1, 0.")
    ]
)
def test_params_cadena_comas(num, expected):
    assert cadena_comas(num) == expected
