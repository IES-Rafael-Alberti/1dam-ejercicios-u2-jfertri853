import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_20 import contar


@pytest.mark.parametrize(
    "frase, letra, expected",
    [
        ("Juan es flojo", "a", 2),
        ("azafata", "a", 0),
        ("science bitch!", "B", 8),
        ("HARRY POTTER Y LA PIEDRA DEL RIÑON", "y", 4),
        ("hello world", "z", None),
        ("buenas noches", " ", 6),
        ("buenas noches", "", None),
        ("hola\nbienvenido", "\n", 4),
        ("acaparar", "parar", None)
    ]
)
def test_params_contar(frase, letra, expected):
    assert contar(frase, letra) == expected
