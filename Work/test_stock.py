import unittest
import stock

class TestStock(unittest.TestCase):
	def test_create(self):
		s = stock.Stock('GOOG', 100, 490.1)
		self.assertEqual(s.name, 'GOOG')
		self.assertEqual(s.shares, 100)
		self.assertEqual(s.price, 490.1)
		self.assertEqual(s.cost, 49010.0)

	def test_bad_shares(self):
		s = stock.Stock('GOOG', 100, 490.10)
		with self.assertRaises(TypeError):
			s.shares = '100'

if __name__ == '__main__':
	unittest.main()
