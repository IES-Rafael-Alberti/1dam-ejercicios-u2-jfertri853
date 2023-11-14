import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_21 import precio_final


@pytest.mark.parametrize(
    "precio, expected",
    [
        (700, 700.0),
        (700, 700),
        (133.45, 133.45),
        (911.458, 911.46),
        (20.6729, 20.67),
        (10000, 9000),
        (1000, 1000),
        (1000.000001, 900.0),
        (1732.97, 1559.67),
        (3411.04, 3069.94)
    ]
)
def test_params_precio_final(precio, expected):
    assert precio_final(precio) == expected
