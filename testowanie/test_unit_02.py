import unittest

class Calculator(object):
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Wystąpił błąd dzielenia przez zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def test_add(self):
        '''test funkcji dodawania'''
        self.calc = Calculator()
        result = self.calc.add(4, 7)
        expected = 11
        self.assertEqual(result, expected)
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(5, 5), 10)

    def test_sub(self):
        '''test funkcji odejmowania'''
        self.calc = Calculator()
        result = self.calc.sub(7, 3)
        expected = 4
        self.assertEqual(result, expected)

    @unittest.skip("Nie testujemy mnożenia")
    def test_mul(self):
        '''test funkcji mnożenia'''
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)

class TestCalculatorDiv(unittest.TestCase):
    def setUp(self):
        '''Konfiguracja środowiska testowego'''
        self.calc = Calculator()

    def test_div(self):
        '''test funkcji dzielenia'''
        result = self.calc.div(15, 6)
        expected = 2.5
        self.assertAlmostEqual(result, expected)

    def test_div_by_zero(self):
        '''test funkcji dzielenia przez zero'''
        self.assertRaises(ZeroDivisionError, self.calc.div, 10, 0)