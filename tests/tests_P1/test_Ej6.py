import pytest
from src.P2_1_EjerciciosCondicionales.Ejercicio1_6 import asignacion_grupo


@pytest.mark.parametrize(
    "nombre, sexo, expected",
    [
        ("Anastasia", "F", "Grupo A"),
        ("blanca", "F", "Grupo A"),
        ("ELENA", "F", "Grupo A"),
        ("lAURA", "F", "Grupo A"),
        ("Oso", "M", "Grupo A"),
        ("pablo", "M", "Grupo A"),
        ("RAMON", "M", "Grupo A"),
        ("zAIRO", "M", "Grupo A"),
        ("Maria", "F", "Grupo B"),
        ("zaira", "F", "Grupo B"),
        ("PAM", "F", "Grupo B"),
        ("Nico", "M", "Grupo B"),
        ("alberto", "M", "Grupo B"),
        ("JOSE", "M", "Grupo B")
    ]
)
def test_params_asignacion_grupo(nombre, sexo, expected):
    assert asignacion_grupo(nombre, sexo) == expected
