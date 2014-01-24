'''
.. module: cod_lec1.square_wave
Created on 24 Jan 2014

Calculates the square wave.
Solves equation sum_{k=1:inf}( 4(2k-1)t / ((2k-1)PI) ) for given t's and number of k's.

.. moduleauthor:: vimaier

'''

import sys

import numpy as np
import matplotlib.pyplot


#===================================================================================================
# main()-function
#===================================================================================================
def main():
    num_points = 201
    list_of_t = np.linspace(-np.pi, np.pi, num_points)
    num_sine_osc = 99

    result_for_given_t = calculate_square_wave_for(list_of_t, num_sine_osc)

    matplotlib.pyplot.plot(list_of_t, result_for_given_t)
    matplotlib.pyplot.show()

    return 0


#===================================================================================================
# helper-functions
#===================================================================================================
def calculate_square_wave_for(list_of_t, num_sine_osc):
    result = np.zeros(len(list_of_t))
    k = np.arange(1, num_sine_osc + 1)
    two_k_minus_one = 2*k - 1

    for i, t in enumerate(list_of_t):
        result[i] = np.sum(np.sin( two_k_minus_one*t ) / (two_k_minus_one) )

    return 4/np.pi * result


#===================================================================================================
# main invocation
#===================================================================================================
if __name__ == "__main__":
    return_value = main()
    sys.exit(return_value)
