import unittest
from graph import *

class RailroadTest(unittest.TestCase):

	def setUp(self):
		string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
		self.railroad = RailRoad()
		self.railroad.build(string)


	def test_distance(self):

		# Test 1:
		self.assertEqual(self.railroad.distance('A-B-C'),9)

		# Test 2:
		self.assertEqual(self.railroad.distance('A-D'),5)

		# Test 3:
		self.assertEqual(self.railroad.distance('A-D-C'),13)

		# Test 4:
		self.assertEqual(self.railroad.distance('A-E-B-C-D'),22)

		# Test 5:
		self.assertEqual(self.railroad.distance('A-E-D'),'NO SUCH ROUTE')




if __name__ == '__main__':
    unittest.main()
	