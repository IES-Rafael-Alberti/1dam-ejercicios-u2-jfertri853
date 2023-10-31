import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_11 import palabra_reversa_separada


@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("azul", "l u z a "),
        ("    pepito gri llo ", "o l l i r g o t i p e p "),
        ("r e c o n o c e r", "r e c o n o c e r "),
        ("radar", "r a d a r "),
        ("KCOHSOIB", "B I O S H O C K "),
        ("s e r p i e n t e ", "e t n e i p r e s "),
        ("amoR", "R o m a ")
    ]
)
def test_params_palabra_reversa_separada(palabra, expected):
    assert palabra_reversa_separada(palabra) == expected
