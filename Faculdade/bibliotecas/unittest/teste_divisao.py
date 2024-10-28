import unittest

def divisao(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

class TesteDivisao(unittest.TestCase):

    def test_divisao_normal(self):
        self.assertEqual(divisao(10,2), 5.0)
        self.assertEqual(divisao(9,3), 3)
        self.assertAlmostEqual(divisao(10,3), 3.333333333, places = 7)

    def test_excecao_parametro_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divisao(0,5)
        with self.assertRaises(ZeroDivisionError):
            divisao(9,0)
    
    def test_numeros_negativos(self):
        self.assertEqual(divisao(-10, 2), -5.0)
        self.assertEqual(divisao(10, -2), -5.0)
        self.assertEqual(divisao(-10, -2), 5.0)

if __name__ == '__main__':
    unittest.main()