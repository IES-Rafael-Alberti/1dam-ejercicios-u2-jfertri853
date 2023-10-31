import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_6 import crear_piramide


@pytest.mark.parametrize(
    "num, expected",
    [
        (4, "*\n**\n***\n****\n"),
        (1, "*\n"),
        (7, "*\n**\n***\n****\n*****\n******\n*******\n"),
        (2, "*\n**\n")
    ]
)
def test_params_crear_piramide(num, expected):
    assert crear_piramide(num) == expected
