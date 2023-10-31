import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_5 import calcular_inversion


@pytest.mark.parametrize(
    "years, money, interest, expected",
    [
        (3, 670, 0.04, 753.66),
        (1000, 0.01, 0.03, 68742402311.7),
        (15, 3569.32, 0.01, 4143.87),
        (8, 1200.0000, 0.35, 13238.88),
        (9, 999, 0.99, 488926.05),
        (11, 15.34, 0.5, 1326.87)
    ]
)
def test_params_calcular_inversion(years, money, interest, expected):
    assert calcular_inversion(years, money, interest) == expected
