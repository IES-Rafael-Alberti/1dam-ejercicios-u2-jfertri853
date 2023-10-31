import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_10 import crear_pizza
from src.P2_1_EjerciciosCondicionales.Ejercicio1_10 import sacar_lista_ingredientes


@pytest.mark.parametrize(
    "ingrediente, expected",
    [
        (None, ["tomate", "mozzarella", None]),
        (21, ["tomate", "mozzarella", 21]),
        ("Aguacate", ["tomate", "mozzarella", "Aguacate"]),
        ("pimiento", ["tomate", "mozzarella", "pimiento"]),
        (False, ["tomate", "mozzarella", False]),
        ("salmon", ["tomate", "mozzarella", "salmon"])
    ]
)
def test_params_crear_pizza(ingrediente, expected):
    assert crear_pizza(ingrediente) == expected


@pytest.mark.parametrize(
    "tipo, expected",
    [
        ("VEGETAL", ["pimiento", "tofu"]),
        ("CONCARNE", ["peperoni", "jamon", "salmon"]),
        ("vegetal", None),
        ("CON CARNE", None),
        ("VEGETARIANA", None)
    ]
)
def test_params_sacar_lista_ingredientes(tipo, expected):
    assert sacar_lista_ingredientes(tipo) == expected
