import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_3 import cadena_impar


@pytest.mark.parametrize(
    "num, expected",
    [
        (17, "1 - 3 - 5 - 7 - 9 - 11 - 13 - 15 - 17."),
        (4, "1 - 3."),
        (11.9, "1 - 3 - 5 - 7 - 9 - 11."),
        (6.9, "1 - 3 - 5."),
        (6.4, "1 - 3 - 5."),
        ("10", "1 - 3 - 5 - 7 - 9."),
        (2, "1."),
        (1, "1.")
    ]
)
def test_params_cadena_impar(num, expected):
    assert cadena_impar(num) == expected
