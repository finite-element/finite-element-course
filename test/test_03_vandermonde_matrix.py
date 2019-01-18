'''Test the construction of the Vandermonde matrix'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval
from fe_utils.finite_elements import vandermonde_matrix
import numpy as np
from scipy.special import comb


@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_vandermond_matrix_type(cell):

    points = np.ones((4, cell.dim))

    v = vandermonde_matrix(cell, 2, points)

    assert isinstance(v, np.ndarray), \
        "vandermonde matrix must return a numpy array, not a %s" % type(v)


@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_vandermond_matrix_rank(cell):

    points = np.ones((4, cell.dim))

    v = vandermonde_matrix(cell, 2, points)

    assert len(v.shape) == 2, \
        "vandermonde matrix must return a rank 2 array, not rank %s" % len(v.shape)


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(8)])
def test_vandermonde_matrix_size(cell, degree):

    points = np.ones((1, cell.dim))

    shape = vandermonde_matrix(cell, degree, points).shape

    correct_shape = (1, np.round(comb(degree + cell.dim, cell.dim)))

    assert shape == correct_shape, \
        "vandermonde matrix should have returned an array of shape %s, not %s"\
        % (correct_shape, shape)


@pytest.mark.parametrize('degree', range(8))
def test_vandermonde_matrix_values_1D(degree):

    points = np.array([[0.], [1.], [2.]])

    V = vandermonde_matrix(ReferenceInterval, degree, points)

    V_t = np.array([[1] + [0] * (V.shape[1] - 1),
                    [1] * V.shape[1],
                    [2**d for d in range(V.shape[1])]])

    print("Vandermonde matrix is:")
    print(V)
    print("Correct answer is:")
    print(V_t)

    assert (V == V_t).all()


@pytest.mark.parametrize('degree', range(8))
def test_vandermonde_matrix_values_2D(degree):

    points = np.array([[0., 0.], [1., 1.], [1., 0.], [0., 1.]])

    V = vandermonde_matrix(ReferenceTriangle, degree, points)

    V_t = np.array([[1] + [0] * (V.shape[1] - 1),
                    [1] * V.shape[1],
                    [1 if p == 0 else 0 for d in range(degree+1) for p in range(d+1)],
                    [1 if p == d else 0 for d in range(degree+1) for p in range(d+1)]])

    print("Vandermonde matrix is:")
    print(V)
    print("Correct answer is:")
    print(V_t)

    assert (V == V_t).all()


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
