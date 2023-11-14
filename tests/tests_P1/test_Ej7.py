import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_7 import calcular_porcentaje_renta
from src.P2_1_EjerciciosCondicionales.Ejercicio1_7 import calcular_impuestos


@pytest.mark.parametrize(
    "renta, expected",
    [
        (250.6, 0.05),
        (9999, 0.05),
        (10000, 0.15),
        (19999.999, 0.15),
        (20000, 0.2),
        (34999, 0.2),
        (35000, 0.3),
        (59999, 0.3),
        (60000, 0.45),
        (88900, 0.45),
        (4782748200, 0.45)
    ]
)
def test_params_calcular_porcentaje_renta(renta, expected):
    assert calcular_porcentaje_renta(renta) == expected


@pytest.mark.parametrize(
    "renta_anual, porcentaje, esperado",
    [
        (3489745, 0.45, 1570385.25),
        (4800, 0, 0),
        (72300, 0.5, 36150),
        (11399, 0.15, 1709.85),
        (34999, 0.2, 6999.8),
        (57341, 0.3, 17202.3),
        (121.483844, 0.05, 6.07)
    ]
)
def test_params_calcular_impuestos(renta_anual, porcentaje, esperado):
    assert calcular_impuestos(renta_anual, porcentaje) == esperado
