import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_22 import contar_par_impar_digitos


@pytest.mark.parametrize(
    "num, expected",
    [
        ("53516", (1, 4)),
        (34, (1, 1)),
        (0, (1, 0)),
        ("399", (0, 3)),
        ("12298924", (5, 3)),
        (932871, (2, 4)),
        ("000", (3, 0)),
        (000, (1, 0)),
        (1000, (3, 1))
    ]
)
def test_params_contar_par_impar_digitos(num, expected):
    assert contar_par_impar_digitos(num) == expected
