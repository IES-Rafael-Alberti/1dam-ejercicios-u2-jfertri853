import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_5 import tributa


@pytest.mark.parametrize(
    "age, income, expected",
    [
        (16, 23500, False),
        (17, 11255, True),
        (4, 12.34, False),
        (23, 999, False),
        (18, 1000, True),
        (41, 98230.53, True),
        (53, 328.11, False)
    ]
)
def test_params_tributa(age, income, expected):
    assert tributa(age, income) == expected
