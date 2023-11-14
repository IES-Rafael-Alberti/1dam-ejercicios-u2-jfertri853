from src.P2_1_EjerciciosCondicionales.Ejercicio1_1 import comprobar_edad


def test_comprobar_edad():
    assert comprobar_edad(0) == "menor"
    assert comprobar_edad(-5) == "menor"
    assert comprobar_edad(-23) == "menor"
    assert comprobar_edad(5) == "menor"
    assert comprobar_edad(17) == "menor"
    assert comprobar_edad(18) == "mayor"
    assert comprobar_edad(20) == "mayor"
    assert comprobar_edad(359) == "mayor"
