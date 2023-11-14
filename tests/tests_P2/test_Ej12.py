import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_12 import contar
from src.P2_2_EjerciciosIterativos.Ejercicio2_12 import contar_easy


@pytest.mark.parametrize(
    "frase, letra, expected",
    [
        ("anda para tu casa", "a", 6),
        ("hola que ase rayo laser", "ase", 0),
        ("buenas tardes Bartolo", "b", 2),
        ("mas estresado que doraemon en una aduana", "Q", 1),
        ("panza panza panza panza", " ", 3),
        ("hola", "x", 0),
        ("hola", "", 0)
    ]
)
def test_params_contar(frase, letra, expected):
    assert contar(frase, letra) == expected


@pytest.mark.parametrize(
    "frase, letra, expected",
    [
        ("anda para tu casa", "a", "La letra (A) aparece 6 veces"),
        ("hola que ase rayo laser", "ase", "La letra (ASE) aparece 2 veces"),
        ("cosecha propia de patacas", "P", "La letra (P) aparece 3 veces"),
        ("buenos dias", " ", "La letra ( ) aparece 1 veces"),
        ("buenas tardes", "y", "La letra (Y) aparece 0 veces"),
        ("hola", "", "La letra () aparece 5 veces")
    ]
)
def test_params_contar_easy(frase, letra, expected):
    assert contar_easy(frase, letra) == expected
