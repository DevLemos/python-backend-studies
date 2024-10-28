import unittest

def ehPalindromo(palavra):
    return palavra == palavra[::-1]

class TestePalindromo(unittest.TestCase):
    def test_palindromo_true(self):
        self.assertTrue(ehPalindromo("osso"))
        self.assertTrue(ehPalindromo("radar"))
        self.assertTrue(ehPalindromo("ana"))
    
    def test_palindromo_false(self):
        self.assertFalse(ehPalindromo("roma"))
        self.assertFalse(ehPalindromo("python"))
        self.assertFalse(ehPalindromo("cleber"))

if __name__ ==  '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



