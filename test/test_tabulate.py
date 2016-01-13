'''Test tabulation of basis functions.'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval, LagrangeElement
import numpy as np


@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_tabulate_type(cell):
    fe = LagrangeElement(cell, 2)

    points = np.ones((4, cell.dim))

    t = fe.tabulate(points)

    assert isinstance(t, np.ndarray), \
        "tabulate must return a numpy array, not a %s" % type(t)


@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_tabulate_matrix_rank(cell):
    fe = LagrangeElement(cell, 2)

    points = np.ones((4, cell.dim))

    t = fe.tabulate(points)

    assert len(t.shape) == 2, \
        "tabulate must return a rank 2 array, not rank %s" % len(t.shape)


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(8)])
def test_tabulate_matrix_size(cell, degree):
    fe = LagrangeElement(cell, 2)

    points = np.ones((4, cell.dim))

    shape = fe.tabulate(points).shape

    correct_shape = (4, fe.nodes.shape[0])

    assert shape == correct_shape, \
        "tabulate should have returned an array of shape %s, not %s"\
        % (correct_shape, shape)


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_tabulate_at_nodes(cell, degree):
    """Check that tabulating at the nodes produces the identity matrix."""
    fe = LagrangeElement(cell, degree)

    assert (np.round(fe.tabulate(fe.nodes)-np.eye(len(fe.nodes)), 10) == 0).all()


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
