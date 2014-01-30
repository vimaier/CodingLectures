'''
.. module: cod_lec1.square_wave
Created on 30.01.2014

<add a description>

.. moduleauthor:: vimaier 

'''

import sys

import numpy as np


#===================================================================================================
# main()-function
#===================================================================================================
def main():
    
    return 0


#===================================================================================================
# helper-functions
#===================================================================================================
def calculate_square_wave_for(list_of_t, num_of_osc):
    result = []

    for t in list_of_t:
        s = 0
        for k in xrange(1, num_of_osc+1):
            s += (4*np.sin((2*k-1)*t)) / ((2*k-1)*np.pi)
        result.append(s)

    return np.array(result)


#===================================================================================================
# main invocation
#===================================================================================================
if __name__ == "__main__":
    return_value = main()
    sys.exit(return_value)
