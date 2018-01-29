import unittest
from graph import *

class TestRailroad(unittest.TestCase):

	def SetUp(self):
		self.railroad = RailRoad()


	def test_build(self):
		string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
		attendu = {'A' :{'B':5, 'D': 5, 'E' : 7}, 'B': {'C':4 }, 'C' : {'D':8, 'E': 2 }, 'D' : {'C' : 8, 'E': 6}, 'E' : { 'B' : 3}}
		try :
			railroad.build(string)
		except :
			print("Method build of RailRoad doesn't run")
		self.assertEqual(railroad.graph,attendu)
		



if __name__ == '__main__':
    unittest.main()
	