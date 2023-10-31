import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_23 import contar_digitos


@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("1984", 4),
        ("fahrenheit 451", 3),
        ("Un mundo feliz", 0),
        ("20000 leguas de viaje submarino", 5),
        ("Veinte mil leguas de viaje submarino", 0),
        ("La metamorfosis", 0),
        ("Metro 2033", 4),
        ("El nombre de la rosa", 0)
    ]
)
def test_params_contar_digitos(cadena, expected):
    assert contar_digitos(cadena) == expected
