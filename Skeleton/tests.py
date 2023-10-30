import parta as parta
import partc as partc
import partd as partd
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
        self.assertEqual(462.92, parta.highest_price(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_highest_price2(self):
        self.assertEqual(447.61, parta.highest_price(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_highest_price3(self):
        self.assertEqual(982.57, parta.highest_price(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_lowest_price1(self):
        self.assertEqual(350.39, parta.lowest_price(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_lowest_price2(self):
        self.assertEqual(365.27, parta.lowest_price(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_lowest_price3(self):
        self.assertEqual(741.08, parta.lowest_price(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_max_volume1(self):
        self.assertEqual(268141.73, parta.max_volume(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_max_volume2(self):
        self.assertEqual(111626.76, parta.max_volume(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_max_volume3(self):
        self.assertEqual(102224.08, parta.max_volume(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_best_avg_price1(self):
        self.assertEqual(455.5523025617217, parta.best_avg_price(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_best_avg_price2(self):
        self.assertEqual(439.0143960593451, parta.best_avg_price(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_best_avg_price3(self):
        self.assertEqual(968.9494656981099, parta.best_avg_price(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_moving_average1(self):
        self.assertEqual(411.89, parta.moving_average(self.data, "01/01/2016", "31/01/2016"), 'Wrong')

    def test_moving_average2(self):
        self.assertEqual(402.73, parta.moving_average(self.data, "01/02/2016", "28/02/2016"), 'Wrong')

    def test_moving_average3(self):
        self.assertEqual(824.83, parta.moving_average(self.data, "01/12/2016", "31/12/2016"), 'Wrong')

    def test_crossover_method1(self):
        answer = [['01/06/2017'], ['28/05/2017']]
        self.assertEqual(answer, partc.crossover_method(self.data, "01/05/2017", "12/06/2017"), 'Wrong')

    def test_crossover_method2(self):
        answer = [['15/09/2018', '21/09/2018'], ['06/09/2018', '19/09/2018', '27/09/2018']]
        self.assertEqual(answer, partc.crossover_method(self.data, "05/09/2018", "27/09/2018"), 'Wrong')

    def test_crossover_method3(self):
        answer = [['06/11/2019'], ['04/11/2019', '08/11/2019']]
        self.assertEqual(answer, partc.crossover_method(self.data, "03/11/2019", "14/11/2019"), 'Wrong')

    def test_predict_next_average1(self):
        x = partd.Investment("04/05/2015", "27/05/2015", self.data)
        self.assertEqual(237.72045957687828, partd.predict_next_average(x), 'Wrong')

    def test_predict_next_average2(self):
        x = partd.Investment("01/02/2016", "28/02/2016", self.data)
        self.assertEqual(441.4238016565723, partd.predict_next_average(x), 'Wrong')

    def test_predict_next_average3(self):
        x = partd.Investment("08/12/2016", "11/12/2016", self.data)
        self.assertEqual(778.1930137752934, partd.predict_next_average(x), 'Wrong')

    def test_classify_trend1(self):
        x = partd.Investment("04/05/2015", "27/05/2015", self.data)
        self.assertEqual("other", partd.classify_trend(x), 'Wrong')

    def test_classify_trend2(self):
        x = partd.Investment("01/02/2016", "28/02/2016", self.data)
        self.assertEqual("increasing", partd.classify_trend(x), 'Wrong')

    def test_classify_trend3(self):
        x = partd.Investment("08/12/2016", "11/12/2016", self.data)
        self.assertEqual("increasing", partd.classify_trend(x), 'Wrong')


if __name__ == '__main__':
    Test.setUpClass()
