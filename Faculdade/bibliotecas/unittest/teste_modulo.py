import unittest

def modulo(a, b):
    return a % b

class TesteModulo(unittest.TestCase):

    def test_modulo_normal(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(9, 2), 1)
        self.assertEqual(modulo(15, 5), 0)

    def test_modulo_com_negativos(self):
        self.assertEqual(modulo(-10, 3), 2)  
        self.assertEqual(modulo(10, -3), -2) 

if __name__ == '__main__':
    unittest.main()
