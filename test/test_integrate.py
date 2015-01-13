'''Test integration using the quadrature module.'''
import pytest
import numpy as np
from fe_utils import gauss_quadrature, ReferenceTriangle, ReferenceInterval

# Test quadrature for polynomials of degree up to 
@pytest.mark.parametrize('degree, quad_degree',
                         [(d, q) 
                          for q in range(1,8) 
                          for d in range(q+1)])
def test_integrate_interval(degree, quad_degree):

    q = gauss_quadrature(ReferenceInterval, quad_degree)

    # Use x**n as test integrand.
    numeric = q.integrate(lambda x: x[0]**degree)
    analytic = 1./(degree+1)

    # Check that the answer is correct to 12 decimal places.
    assert round(numeric - analytic, 12) == 0

# Test quadrature for polynomials of degree up to 
@pytest.mark.parametrize('degree, quad_degree',
                         [(d, q) 
                          for q in range(1,8) 
                          for d in range(q+1)])
def test_integrate_triangle(degree, quad_degree):

    q = gauss_quadrature(ReferenceTriangle, quad_degree)

    # Use x**n as test integrand.
    numeric = q.integrate(lambda x: x[0]**degree)
    analytic = 1./(degree+1) - 1./(degree+2)

    # Check that the answer is correct to 12 decimal places.
    assert round(numeric - analytic, 12) == 0
                         

if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
