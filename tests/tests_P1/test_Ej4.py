from src.P2_1_EjerciciosCondicionales.Ejercicio1_4 import par_impar


def test_par_impar():
    assert par_impar(0) == "par"
    assert par_impar(4) == "par"
    assert par_impar(3188) == "par"
    assert par_impar(-2) == "par"
    assert par_impar(1) == "impar"
    assert par_impar(245) == "impar"
    assert par_impar(-77) == "impar"
    assert par_impar(-389) == "impar"
