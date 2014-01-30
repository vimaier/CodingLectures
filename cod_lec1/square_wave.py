'''
.. module: cod_lec1.square_wave
Created on 30.01.2014

<add a description>

.. moduleauthor:: vimaier

'''

import sys

import numpy as np
import timeit


#===================================================================================================
# main()-function
#===================================================================================================
def main():
    measure_time_between_old_and_improved_version()
    return 0


#===================================================================================================
# helper-functions
#===================================================================================================
def calculate_square_wave_for(list_of_t, num_of_osc):
    result = np.zeros(len(list_of_t))
    k = np.arange(1, num_of_osc + 1)
    two_k_minus_one = 2*k - 1 

    for i, t in enumerate(list_of_t):
        result[i] = np.sum((np.sin(two_k_minus_one*t)) / two_k_minus_one)       

    return (4/np.pi) * result


def first_calculate_square_wave_for(list_of_t, num_of_osc):
    result = []

    for t in list_of_t:
        s = 0
        for k in xrange(1, num_of_osc + 1):
            s += (4*np.sin((2*k-1)*t)) / ((2*k-1)*np.pi)
        result.append(s)

    return np.array(result)


def measure_time_between_old_and_improved_version():
    setup = """
import numpy as np

from __main__ import calculate_square_wave_for
from __main__ import first_calculate_square_wave_for

num_of_osc = 99
num_of_points = 5
list_of_t = np.linspace(-np.pi, np.pi, num_of_points)
"""

    print "Start..."
    num_of_iterations = 10000
    print "First version:", timeit.timeit("first_calculate_square_wave_for(list_of_t, num_of_osc)",
                                            setup, number=num_of_iterations)
    print "Improved version:", timeit.timeit("calculate_square_wave_for(list_of_t, num_of_osc)",
                                            setup, number=num_of_iterations)
    print "Finished..."


#===================================================================================================
# main invocation
#===================================================================================================
if __name__ == "__main__":
    return_value = main()
    sys.exit(return_value)
