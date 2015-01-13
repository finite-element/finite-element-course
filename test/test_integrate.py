'''Test integration using the quadrature module.'''
import pytest
import numpy as np
from fe_utils import gauss_quadrature, ReferenceCell, ReferenceInterval

# Test quadrature for polynomials of degree up to 
@pytest.mark.parametrize('degree, quad_degree',
                         [(d, q) for q in range(1,2) for d in range(q+1)])
def test_integrate_interval(degree, quad_degree):

    q = gauss_quadrature(ReferenceInterval, quad_degree)

    # Use x**n as test integrand.
    numeric = q.integrate(lambda x: x[0]**degree)
    analytic = 1./(degree+1) - 1./(degree+2)

    # Check that the answer is correct to 12 DP.
    assert round(numeric - analytic, 12)) == 0
                         

if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
