'''Test tabulation of basis functions.'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval, LagrangeElement
import numpy as np


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_tabulate_grad_shape(cell, degree):
    """Check that tabulating at the nodes produces the identity matrix."""
    fe = LagrangeElement(cell, degree)

    vals = fe.tabulate([[0] * cell.dim], grad=True)

    assert vals.shape == (1, fe.nodes.shape[0], cell.dim)


def test_tabulate_grad_1D():
    """Check that tabulating the gradient of a first degree element is correct."""
    fe = LagrangeElement(ReferenceInterval, 1)

    vals = fe.tabulate([[0]], grad=True)

    assert ((vals - np.array([[[-1], [1]]])).round(12) == 0).all()


def test_tabulate_grad_2D():
    """Check that tabulating the gradient of a first degree element is correct."""
    fe = LagrangeElement(ReferenceTriangle, 1)

    vals = fe.tabulate([[0, 0]], grad=True)

    assert ((vals - np.array([[[-1, -1], [1, 0], [0, 1]]])).round(12) == 0).all()


if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
