from src.P2_1_EjerciciosCondicionales.Ejercicio1_9 import precio_entrada


def test_precio_entrada():
    assert precio_entrada(0) == 0
    assert precio_entrada(3) == 0
    assert precio_entrada(-8) == 0
    assert precio_entrada(4) == 5
    assert precio_entrada(5) == 5
    assert precio_entrada(17) == 5
    assert precio_entrada(18) == 10
    assert precio_entrada(21) == 10
    assert precio_entrada(17.95) == 5
    assert precio_entrada(3.99) == 0
