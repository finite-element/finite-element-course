'''Test the construction of the Vandermonde matrix'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval
from fe_utils.finite_elements import vandermonde_matrix
import numpy as np
from scipy.misc import comb


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(8)])
def test_vandermonde_matrix_size(cell, degree):

    points = np.ones((1, cell.dim))

    shape = vandermonde_matrix(cell, degree, points).shape

    assert shape == (1, int(comb(degree + cell.dim, cell.dim)))


@pytest.mark.parametrize('degree', range(8))
def test_vandermonde_matrix_values_1D(degree):

    points = np.array([[0], [1], [2]])

    V = vandermonde_matrix(ReferenceInterval, degree, points)

    V_t = np.array([[1] + [0] * (V.shape[1] - 1),
                    [1] * V.shape[1],
                    [2**d for d in range(V.shape[1])]])

    print "Vandermonde matrix is:"
    print V
    print "Correct answer is:"
    print V_t

    assert (V == V_t).all()


@pytest.mark.parametrize('degree', range(8))
def test_vandermonde_matrix_values_2D(degree):

    points = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])

    V = vandermonde_matrix(ReferenceTriangle, degree, points)

    V_t = np.array([[1] + [0] * (V.shape[1] - 1),
                    [1] * V.shape[1],
                    [1 if p == 0 else 0 for d in range(degree+1) for p in range(d+1)],
                    [1 if p == d else 0 for d in range(degree+1) for p in range(d+1)]])

    print "Vandermonde matrix is:"
    print V
    print "Correct answer is:"
    print V_t

    assert (V == V_t).all()


if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
