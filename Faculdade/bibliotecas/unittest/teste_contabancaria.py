import unittest

class contaBancaria:
    def __init__(self,saldo = 50):
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
    
class TesteContaBancaria(unittest.TestCase):
    def test_deposito(self):
        conta = contaBancaria()
        conta.depositar(400)
        self.assertEqual(conta.saldo, 450)
    
    def test_saque(self):
        conta = contaBancaria()
        conta.sacar(50)
        self.assertEqual(conta.saldo, 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


