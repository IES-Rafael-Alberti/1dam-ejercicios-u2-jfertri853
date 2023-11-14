import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_7 import tabla_multip


@pytest.mark.parametrize(
    "num, expected",
    [
        (2, "Tabla del 2: 2 - 4 - 6 - 8 - 10 - 12 - 14 - 16 - 18 - 20."),
        (10, "Tabla del 10: 10 - 20 - 30 - 40 - 50 - 60 - 70 - 80 - 90 - 100."),
        (19, "Tabla del 19: 19 - 38 - 57 - 76 - 95 - 114 - 133 - 152 - 171 - 190."),
        (7, "Tabla del 7: 7 - 14 - 21 - 28 - 35 - 42 - 49 - 56 - 63 - 70."),
        (-4, "Tabla del -4: -4 - -8 - -12 - -16 - -20 - -24 - -28 - -32 - -36 - -40.")
    ]
)
def test_params_tabla_multip(num, expected):
    assert tabla_multip(num) == expected
