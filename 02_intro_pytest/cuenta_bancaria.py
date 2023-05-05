import pytest


class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        print(f"saldo {self.saldo}")
        return self.saldo

    def teardown_method(self):
        pass


class TestCuentaBancaria:

    def setup_method(self):
        self.cuenta = CuentaBancaria('Luis', 100)

    def test_depositar(self):
        self.cuenta.depositar(80)
        assert self.cuenta.consultar_saldo() == 180, "El saldo debe ser 180 despues de depositar 80"

    def test_retirar(self):
        self.cuenta.retirar(50)
        assert self.cuenta.consultar_saldo() == 50, "El saldo debe de ser 50 despues de retirar 50"

    def test_retirar_insuficiente(self):
        with pytest.raises(ValueError) as exc_info:
            self.cuenta.retirar(1000)





        


