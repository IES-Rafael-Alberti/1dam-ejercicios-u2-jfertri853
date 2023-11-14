import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_3 import division


@pytest.mark.parametrize(
    "n1, n2, expected",
    [
        (5, 5, 1.0),
        (7, 3, 2.333),
        (4, 21, 0.19),
        (12.9645, 4, 3.241),
        (-6, -11, 0.545),
        (0, -3, -0.0),
        (0, 7, 0.0),
        (9, 0, None),
        (-3, 2, -1.5),
        (115.2, 5.78113, 19.927),
        (-353, 1.34, -263.433)
    ]
)
def test_params_division(n1, n2, expected):
    assert division(n1, n2) == expected
