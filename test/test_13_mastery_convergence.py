'''Test that the sample poisson problem converges at approximately the right rate.'''
import pytest
from fe_utils.solvers.burgers import solve_burgers
import numpy as np


def test_convergence():

    res = [2**i for i in range(4, 7)]

    error = [solve_burgers(r)[1] for r in res]

    convergence_rate = np.array([np.log(error[i]/error[i+1])/np.log(res[i+1]/res[i])
                                 for i in range(len(res)-1)])

    print("Achieved convergence rates: %s" % convergence_rate)
    print("Expected: %s" % (2))

    assert (convergence_rate > 1.9).all()


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
