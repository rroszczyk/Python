import unittest
from area import *
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)

    def test_type(self):
        self.assertRaises(TypeError, circle_area, 'napis')

    def test_value(self):
        self.assertRaises(ValueError, circle_area, -2)