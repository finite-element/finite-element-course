'''Test integration using the quadrature module.'''
import pytest
from fe_utils import gauss_quadrature, ReferenceTriangle, ReferenceInterval


# Test quadrature for polynomials of degree up to 8
@pytest.mark.parametrize('degree, quad_degree',
                         [(d, q)
                          for q in range(1, 8)
                          for d in range(q+1)])
def test_integrate_interval(degree, quad_degree):

    q = gauss_quadrature(ReferenceInterval, quad_degree)

    # Use x**n as test integrand.
    numeric = q.integrate(lambda x: x[0]**degree)
    analytic = 1./(degree+1)

    # Check that the answer is correct to 12 decimal places.
    assert round(numeric - analytic, 12) == 0


# Test quadrature for polynomials of degree up to 8
@pytest.mark.parametrize('dim, degree, quad_degree',
                         [(dim, d, q)
                          for dim in (0, 1)
                          for q in range(1, 8)
                          for d in range(q+1)])
def test_integrate_triangle(dim, degree, quad_degree):

    q = gauss_quadrature(ReferenceTriangle, quad_degree)

    # Use x[dim]**n as test integrand.
    numeric = q.integrate(lambda x: x[dim]**degree)
    analytic = 1./(degree+1) - 1./(degree+2)

    # Check that the answer is correct to 12 decimal places.
    assert round(numeric - analytic, 12) == 0


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
