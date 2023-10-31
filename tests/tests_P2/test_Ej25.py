import pytest
from src.P2_2_EjerciciosIterativos.Ejercicio2_25 import modificar_frase
from src.P2_2_EjerciciosIterativos.Ejercicio2_25 import search_longest_word


@pytest.mark.parametrize(
    "frase, expected",
    [
        ("mi nombre es pedro.", ["mi", "nombre", "es", "pedro"]),
        ("murciélago", ["murciélago"]),
        ("", [""]),
        ("hola!     soy       juan", ["hola", "soy", "juan"]),
        ("¿dióxido de carbono?", ["dióxido", "de", "carbono"])
    ]
)
def test_params_modificar_frase(frase, expected):
    assert modificar_frase(frase) == expected


@pytest.mark.parametrize(
    "frase_enlistada, expected",
    [
        ([""], (None, 0)),
        (["dióxido", "de", "carbono"], ("dióxido", 7)),
        (["como", "te", "llamas?"], ("llamas?", 7)),
        (["hola", "joselu"], ("joselu", 6))
    ]
)
def test_params_search_longest_word(frase_enlistada, expected):
    assert search_longest_word(frase_enlistada) == expected
