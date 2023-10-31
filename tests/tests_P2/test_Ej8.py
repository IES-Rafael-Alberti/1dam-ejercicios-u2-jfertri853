import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_8 import piramide_impares


@pytest.mark.parametrize(
    "num, expected",
    [
        (4, "1 \n3 1 \n5 3 1 \n7 5 3 1 \n"),
        (1, "1 \n"),
        (9, "1 \n3 1 \n5 3 1 \n7 5 3 1 \n9 7 5 3 1 \n11 9 7 5 3 1 \n13 11 9 7 5 3 1 \n15 13 11 9 7 5 3 1 \n"
            "17 15 13 11 9 7 5 3 1 \n"),
        (2, "1 \n3 1 \n")
    ]
)
def test_params_piramide_impares(num, expected):
    assert piramide_impares(num) == expected
