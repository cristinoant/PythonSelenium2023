class CuentaBancaria:

    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: int):
        self.saldo += cantidad

    def retirar(self, cantidad: int):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo


def test_consultar_saldo():
    mi_cuenta = CuentaBancaria("Antonio", 5000)
    resultado = mi_cuenta.consultar_saldo()
    assert resultado == 5000, "El saldo inicial deberia ser 5000"


def test_depositar():
    mi_cuenta = CuentaBancaria("Antonio", 5000)
    mi_cuenta.depositar(1000)
    resultado = mi_cuenta.consultar_saldo()
    assert resultado == 6000, "El saldo final deberia ser 6000"


def test_retirar():
    mi_cuenta = CuentaBancaria("Antonio", 5000)
    mi_cuenta.retirar(500)
    resultado = mi_cuenta.consultar_saldo()
    assert resultado == 4500, "El saldo final deberia ser 4500"







