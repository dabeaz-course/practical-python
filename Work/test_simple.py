import simple
import unittest

class TestAdd(unittest.TestCase):
	def test_simple(self):
		r = simple.add(2,2)
		self.assertEqual(r, 5)

	def test_str(self):
		r = simple.add('hello', 'world')
		self.assertEqual(r, 'helloworld')

if __name__ == '__main__':
	unittest.main()
