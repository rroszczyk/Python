import unittest

class TestSum(unittest.TestCase):
    def test_sum3(self):
        assert sum([1, 1, 1]) == 3, "wyniki poprawny to 3"

    def test_sum1(self):
        assert sum([1, 2, 3]) == 6, "wyniki poprawny to 6"

    def test_sum2(self):
        assert sum([1, 1, 1]) == 6, "wyniki poprawny to 6"

if __name__ == "__main__":
    unittest.main()