'''Test integration using the quadrature module.'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval
from fe_utils.finite_elements import lagrange_points
from scipy.special import comb
import numpy as np


# Test that the right type is returned.
@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_point_type(cell):

    assert isinstance(lagrange_points(cell, 1), np.ndarray), \
        "Return type of lagrange_points must be numpy array"


# Test that the right shape is returned in the 1D case.
def test_point_shape():

    assert lagrange_points(ReferenceInterval, 1).shape == (2, 1), \
        "In 1D, lagrange_points must return a list of 1-vectors, not a list of floats"


# Test number of points for polynomials of degree up to 8
@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_point_count(cell, degree):

    p = lagrange_points(cell, degree)

    assert p.shape[0] == np.round(comb(degree + cell.dim, cell.dim))


# Check that the average of the points is the circumcentre.
# This basic test follows by symmetry.
@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_point_average(cell, degree):

    p = lagrange_points(cell, degree)

    average = np.sum(p, 0) / p.shape[0]

    assert all(np.round(average - 1./(cell.dim + 1), 12) == 0)


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
