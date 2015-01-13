'''Test integration using the quadrature module.'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval
from fe_utils.finite_elements import lagrange_points
from scipy.misc import comb
import numpy as np


# Test number of points for polynomials of degree up to 8
@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_point_count(cell, degree):

    p = lagrange_points(cell, degree)

    assert p.shape[0] == comb(degree + cell.dim, cell.dim)


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
    import os
    pytest.main(os.path.abspath(__file__))
