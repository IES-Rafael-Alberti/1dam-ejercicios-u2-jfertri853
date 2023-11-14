import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_8 import calcular_plus
from src.P2_1_EjerciciosCondicionales.Ejercicio1_8 import rendimiento_empleado


@pytest.mark.parametrize(
    "puntuacion, expected",
    [
        (0.0, 0),
        (0.1, 240),
        (0.4, 960),
        (0.6, 1440),
        (0.9, 2160),
        (1.2, 2880),
        (0.542, 1300.8),
        (39, 93600)
    ]
)
def test_params_calcular_plus(puntuacion, expected):
    assert calcular_plus(puntuacion) == expected


@pytest.mark.parametrize(
    "puntuacion, expected",
    [
        (0.0, "Inaceptable"),
        (0.2, None),
        (0.4, "Aceptable"),
        (0.6, "Meritorio"),
        (0.9, "Meritorio"),
        (1.2, "Meritorio"),
        (0.542, None),
        (0.454, None),
        (0.654, "Meritorio"),
        (-0.4, None),
        (34, "Meritorio")
    ]
)
def test_params_rendimiento_empleado(puntuacion, expected):
    assert rendimiento_empleado(puntuacion) == expected
