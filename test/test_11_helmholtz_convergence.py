'''Test that the sample helmholtz problem converges at approximately the right rate.'''
from __future__ import division
import pytest
from fe_utils.solvers.helmholtz import solve_helmholtz
import numpy as np


@pytest.mark.parametrize('degree', range(1, 4))
def test_convergence(degree):

    res = [2**i for i in range(4, 7)]

    error = [solve_helmholtz(degree, r)[1] for r in res]

    convergence_rate = np.array([np.log(error[i]/error[i+1])/np.log(res[i+1]/res[i])
                                 for i in range(len(res)-1)])

    print("Achieved convergence rates: %s" % convergence_rate)
    print("Expected: %s" % (degree + 1))

    assert (convergence_rate > 0.9 * (degree + 1)).all()


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
