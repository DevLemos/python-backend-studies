import unittest

def potencia(base, expoente):
    if base == 0 and expoente == 0:
        raise ValueError("Indeterminação: 0 elevado a 0 não é definido.")
    return base ** expoente

class TestePotencia(unittest.TestCase):

    def test_potencia_normal(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(0, 5), 0)

    def test_potencia_com_negativos(self):
        self.assertEqual(potencia(-2, 3), -8)  # Base negativa, expoente ímpar
        self.assertEqual(potencia(-2, 2), 4)   # Base negativa, expoente par

    def test_potencia_indeterminada(self):
        with self.assertRaises(ValueError):
            potencia(0, 0)  # 0 ** 0 é indeterminado

if __name__ == '__main__':
    unittest.main()
