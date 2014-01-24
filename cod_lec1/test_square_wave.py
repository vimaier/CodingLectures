'''
Created on 24 Jan 2014

@author: vimaier
'''
import unittest

import numpy as np

import cod_lec1.square_wave as square_wave


class Test(unittest.TestCase):

    def test_square_wave(self):
        assumed_result = np.array(
            [-1.650777599717162E-14, -1.0032151693727007, 0.0, 1.0032151693727007, 1.650777599717162E-14]
              )

        num_points = 5
        list_of_t = np.linspace(-np.pi, np.pi, num_points)
        num_sine_osc = 99

        calculated_result = square_wave.calculate_square_wave_for(list_of_t, num_sine_osc)

        self.assertTrue((assumed_result == calculated_result).all(), "Results are not equal")

    def test_for_fail(self):
        wrong_result = np.zeros(10)
        num_points = 5
        list_of_t = np.linspace(-np.pi, np.pi, num_points)
        num_sine_osc = 99

        calculated_result = square_wave.calculate_square_wave_for(list_of_t, num_sine_osc)

        self.assertFalse((wrong_result == calculated_result), "Results are equal but they should not be equal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_square_wave']
    unittest.main()
