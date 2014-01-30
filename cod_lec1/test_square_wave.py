'''
Created on 30.01.2014

@author: vimaier
'''
import unittest

import numpy as np
import cod_lec1.square_wave as square_wave


class Test(unittest.TestCase):

    def test_square_wave(self):
        assumed_results = np.array([-1.650777599717162E-14, -1.0032151693727007, 0.0, 1.0032151693727007, 1.650777599717162E-14])

        num_of_osc = 99
        num_of_points = 5
        list_of_t = np.linspace(-np.pi, np.pi, num_of_points)

        calc_result = square_wave.calculate_square_wave_for(list_of_t, num_of_osc)

        self.assertTrue(np.allclose(assumed_results, calc_result), "Calculated values are wrong")

    def test_first_square_wave(self):
        assumed_results = np.array([-1.650777599717162E-14, -1.0032151693727007, 0.0, 1.0032151693727007, 1.650777599717162E-14])

        num_of_osc = 99
        num_of_points = 5
        list_of_t = np.linspace(-np.pi, np.pi, num_of_points)

        calc_result = square_wave.first_calculate_square_wave_for(list_of_t, num_of_osc)

        self.assertTrue(np.allclose(assumed_results, calc_result), "Calculated values are wrong")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_square_wave']
    unittest.main()
