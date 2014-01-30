'''
Created on 30.01.2014

@author: vimaier
'''
import unittest

import numpy as np
from cod_lec1.square_wave import calculate_square_wave_for

class Test(unittest.TestCase):


    def test_square_wave(self):
        assumed_results = np.array([-1.650777599717162E-14, -1.0032151693727007, 0.0, 1.0032151693727007, 1.650777599717162E-14])

        num_of_osc = 99
        num_of_points = 5
        list_of_t = np.linspace(-np.pi, np.pi, 5)

        calc_result = calculate_square_wave_for(list_of_t, num_of_osc)

        self.assertTrue(np.allclose(assumed_results, calc_result), "Calculated values are wrong")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_square_wave']
    unittest.main()