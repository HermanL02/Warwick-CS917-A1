import partb as partb
import partc as partc
import unittest
import csv


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = []
        with open("../cryptocompare_btc.csv", "r") as f:
            reader = csv.DictReader(f)
            cls.data = [r for r in reader]

    def test_highest_price(self):
        self.assertEqual(462.92, partb.highest_price(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_highest_price2(self):
        self.assertEqual(447.61, partb.highest_price(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_highest_price3(self):
        self.assertEqual(982.57, partb.highest_price(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_lowest_price1(self):
        self.assertEqual(350.39, partb.lowest_price(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_lowest_price2(self):
        self.assertEqual(365.27, partb.lowest_price(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_lowest_price3(self):
        self.assertEqual(741.08, partb.lowest_price(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_max_volume1(self):
        self.assertEqual(268141.73, partb.max_volume(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_max_volume2(self):
        self.assertEqual(111626.76, partb.max_volume(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_max_volume3(self):
        self.assertEqual(102224.08, partb.max_volume(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_best_avg_price1(self):
        self.assertEqual(455.5523025617217, partb.best_avg_price(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_best_avg_price2(self):
        self.assertEqual(439.0143960593451, partb.best_avg_price(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_best_avg_price3(self):
        self.assertEqual(968.9494656981099, partb.best_avg_price(self.data, "01/122016", "31/12/2016"), 'Wrong')

    def test_moving_average1(self):
        self.assertEqual(411.89, partb.moving_average(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_moving_average2(self):
        self.assertEqual(402.73, partb.moving_average(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_moving_average3(self):
        self.assertEqual(824.83, partb.moving_average(self.data, "01/12/2016", "31/12/2016"), 'Wrong')


if __name__ == '__main__':
    Test.setUpClass()
