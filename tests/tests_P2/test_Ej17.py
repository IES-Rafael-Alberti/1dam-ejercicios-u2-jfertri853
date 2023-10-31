import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_17 import sumatorio_digitos


@pytest.mark.parametrize(
    "num, expected",
    [
        ("13", 4),
        (13, 4),
        (398, 20),
        (1142, 8),
        (12, 3),
        ("0450", 9),
        (55922145, 33)
    ]
)
def test_params_sumatorio_digitos(num, expected):
    assert sumatorio_digitos(num) == expected
