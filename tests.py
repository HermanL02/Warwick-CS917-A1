import Skeleton.parta as parta
import unittest
import csv


class TestParta(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = []
        with open("cryptocompare_btc.csv", "r") as f:
            reader = csv.DictReader(f)
            cls.data = [r for r in reader]

    def test_highest_price(self):
        self.assertEqual(parta.highest_price(self.data, "01/01/2016", "31/01/2016", ), 462.92, 'Wrong')

    def test_highest_price2(self):
        self.assertEqual(parta.highest_price(self.data, "01/02/2016", "28/02/2016", ), 447.61, 'Wrong')

    def test_highest_price3(self):
        self.assertEqual(parta.highest_price(self.data, "01/12/2016", "31/12/2016", ), 982.57, 'Wrong')
    def test_lowest_price3(self):
        self.assertEqual(parta.lowest_price(self.data, "01/01/2016", "31/01/2016", ), 350.39, 'Wrong')

if __name__ == '__main__':
    TestParta.setUpClass()
