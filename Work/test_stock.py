import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)

    def test_bad_shares(self):
        with self.assertRaises(TypeError):
            s = stock.Stock('GOOG', 100., 490.1)


if __name__ == '__main__':
    unittest.main()
