import pytest


class Calculadora:

    def __init__(self):
        pass

    def suma(self, num_a: int, num_b: int):
        return num_a + num_b

    def resta(self, num_a: int, num_b: int):
        return num_a - num_b

    def multiplicacion(self, num_a: int, num_b: int):
        return num_a * num_b

    def division(self, num_a: int, num_b: int):
        return num_a / num_b


def test_suma():
    calc = Calculadora()
    result = calc.suma(4, 2)
    assert result == 6, "La suma de 4 y 2 debe ser 6"


def test_resta():
    calc = Calculadora()
    result = calc.resta(10, 5)
    assert result == 5, "La resta de 10 - 5 debe ser 5"


def test_multiplicacion():
    calc = Calculadora()
    result = calc.multiplicacion(5, 5)
    assert result == 25, "La multiplicacion de 5 * 5 debe ser 25"


def test_division():
    calc = Calculadora()
    result = calc.division(100, 10)
    assert result == 10, "La division de 100 entre 10 debe ser 10"
