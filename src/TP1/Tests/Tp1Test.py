import unittest
from TP1.Tp1 import *


class TestTp1(unittest.TestCase):
    tp1 = Tp1()

    def test_tp1(self):
        print("\n")
        print("Math pi: {}" .format(self.tp1.mathpi()))
        print("Gauss-Leggendre float pi: {}" .format(self.tp1.gauss_legendre_float(1000)))
        print("Gauss-Leggendre decimal pi: {}" .format(self.tp1.gauss_legendre_decimal(1000)))
        print("Spigot Pi Digits: {}" .format(list(self.tp1.pi_digits(100))))

if __name__ == '__main__':
    unittest.main()