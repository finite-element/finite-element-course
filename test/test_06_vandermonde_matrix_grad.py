'''Test the construction of the gradient Vandermonde matrix'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval
from fe_utils.finite_elements import vandermonde_matrix
import numpy as np
from scipy.special import comb


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(8)])
def test_vandermonde_matrix_grad_shape(cell, degree):

    points = np.ones((1, cell.dim))

    shape = vandermonde_matrix(cell, degree, points, grad=True).shape

    correct_shape = (1, round(comb(degree + cell.dim, cell.dim)), cell.dim)

    assert shape == correct_shape, \
        "vandermonde matrix should have returned an array of shape %s, not %s"\
        % (correct_shape, shape)


@pytest.mark.parametrize('degree', range(8))
def test_vandermonde_matrix_grad_values_1D(degree):

    points = np.array([[0], [1]])

    V = vandermonde_matrix(ReferenceInterval, degree, points, grad=True)

    V_t = np.array([[0] + ([1] if degree > 0 else []) + [0] * (V.shape[1]-2),
                    range(V.shape[1])]).reshape((2, V.shape[1], 1))

    print("Vandermonde matrix is:")
    print(V)
    print("Correct answer is:")
    print(V_t)

    assert (V == V_t).all()


@pytest.mark.parametrize('degree', range(8))
def test_vandermonde_matrix_grad_values_2D(degree):

    points = np.array([[0., 0.], [1., 0.], [0., 1.]])

    V = vandermonde_matrix(ReferenceTriangle, degree, points, grad=True)

    V_t = np.array([[[0, 0]] + ([[1, 0], [0, 1]] if degree > 0 else [])
                    + [[0, 0]] * (V.shape[1] - 3),
                    [[d, 0] if p == 0 else [0, 1] if p == 1 else [0, 0] for d in range(degree+1) for p in range(d+1)],
                    [[0, d] if p == d else [1, 0] if p == d - 1 else [0, 0] for d in range(degree+1) for p in range(d+1)]])

    print("Vandermonde matrix is:")
    print(V)
    print("Correct answer is:")
    print(V_t)

    assert (V == V_t).all()


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
