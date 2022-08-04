# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
from railroad.network import RailroadNetwork

class TestRailroad(unittest.TestCase):


    def setUp(self):
        self.railroad = RailroadNetwork()


    def test_build(self):
        string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
        expected = {'A' :{'B':5, 'D': 5, 'E' : 7}, 'B': {'C':4 },
                    'C' : {'D':8, 'E': 2 }, 'D' : {'C' : 8, 'E': 6},
                    'E' : { 'B' : 3}}
        try :
            self.railroad.build(string)
        except :
            print("Could not build the railroad network.")
        self.assertEqual(self.railroad.graph, expected)




if __name__ == '__main__':
    unittest.main()
    