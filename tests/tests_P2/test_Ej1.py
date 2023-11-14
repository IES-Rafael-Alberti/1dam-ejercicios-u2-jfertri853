import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_1 import repetir10
from src.P2_2_EjerciciosIterativos.Ejercicio2_1 import repetir10_saltos
from src.P2_2_EjerciciosIterativos.Ejercicio2_1 import repetir10_bucle
from src.P2_2_EjerciciosIterativos.Ejercicio2_1 import repetir10_bucle_saltos


@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("2", "2222222222"),
        ("hola ", "hola hola hola hola hola hola hola hola hola hola "),
        ("True.", "True.True.True.True.True.True.True.True.True.True."),
        ("kiwi\n", "kiwi\nkiwi\nkiwi\nkiwi\nkiwi\nkiwi\nkiwi\nkiwi\nkiwi\nkiwi\n")
    ]
)
def test_params_repetir10(palabra, expected):
    assert repetir10(palabra) == expected


@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("mango", "mango\nmango\nmango\nmango\nmango\nmango\nmango\nmango\nmango\nmango\n"),
        ("78", "78\n78\n78\n78\n78\n78\n78\n78\n78\n78\n"),
        ("A B\n", "A B\n\nA B\n\nA B\n\nA B\n\nA B\n\nA B\n\nA B\n\nA B\n\nA B\n\nA B\n\n")
    ]
)
def test_params_repetir10_saltos(palabra, expected):
    assert repetir10_saltos(palabra) == expected


@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("mango ", "mango mango mango mango mango mango mango mango mango mango "),
        ("FAL - SE", "FAL - SEFAL - SEFAL - SEFAL - SEFAL - SEFAL - SEFAL - SEFAL - SEFAL - SEFAL - SE"),
        ("191", "191191191191191191191191191191")
    ]
)
def test_params_repetir10_bucle(palabra, expected):
    assert repetir10_bucle(palabra) == expected


@pytest.mark.parametrize(
    "palabra, expected",
    [
        (" mango", " mango\n mango\n mango\n mango\n mango\n mango\n mango\n mango\n mango\n mango\n"),
        ("22", "22\n22\n22\n22\n22\n22\n22\n22\n22\n22\n"),
        ("c a t", "c a t\nc a t\nc a t\nc a t\nc a t\nc a t\nc a t\nc a t\nc a t\nc a t\n")
    ]
)
def test_params_repetir10_bucle_saltos(palabra, expected):
    assert repetir10_bucle_saltos(palabra) == expected
