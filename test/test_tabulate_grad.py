'''Test tabulation of basis functions.'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval, LagrangeElement
import numpy as np


@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_tabulate_matrix_rank(cell):
    fe = LagrangeElement(cell, 2)

    points = np.ones((4, cell.dim))

    t = fe.tabulate(points, grad=True)

    assert len(t.shape) == 3, \
        "tabulate with grad=True must return a rank 3 array, not rank %s" % len(t.shape)


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_tabulate_grad_shape(cell, degree):
    """Check that tabulating at the nodes produces the identity matrix."""
    fe = LagrangeElement(cell, degree)

    vals = fe.tabulate(np.array([[0] * cell.dim]), grad=True)

    correct_shape = (1, fe.nodes.shape[0], cell.dim)

    assert vals.shape == correct_shape, \
        "tabulate should have returned an array of shape %s, not %s"\
        % (correct_shape, vals.shape)


def test_tabulate_grad_1D():
    """Check that tabulating the gradient of a first degree element is correct."""
    fe = LagrangeElement(ReferenceInterval, 1)

    vals = fe.tabulate(np.array([[0]]), grad=True)

    correct_answer = np.array([[[-1], [1]]], dtype=np.double)

    print("Your answer is:")
    print(vals)
    print("The correct answer is:")
    print(correct_answer)

    assert ((vals - correct_answer).round(12) == 0).all()


def test_tabulate_grad_2D():
    """Check that tabulating the gradient of a first degree element is correct."""
    fe = LagrangeElement(ReferenceTriangle, 1)

    vals = fe.tabulate(np.array([[0, 0]]), grad=True)

    # The order of this list depends on the order in which the nodes were defined.
    gradients = np.array([[-1., -1.] if (n == [0., 0.]).all() else n
                          for n in fe.nodes])

    print("Your answer is:")
    print(vals)
    print("The correct answer is:")
    print(gradients)

    assert ((vals - gradients).round() == 0).all()


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
