import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_10 import es_primo


@pytest.mark.parametrize(
    "num, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (11, True),
        (65, False),
        (89, True),
        (11311, True),
        (783, False)
    ]
)
def test_params_es_primo(num, expected):
    assert es_primo(num) == expected
