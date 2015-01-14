'''Test tabulation of basis functions.'''
import pytest
from fe_utils import ReferenceTriangle, ReferenceInterval, LagrangeElement
import numpy as np


@pytest.mark.parametrize('cell, degree',
                         [(c, d)
                          for c in (ReferenceInterval, ReferenceTriangle)
                          for d in range(1, 8)])
def test_tabulate_at_nodes(cell, degree):
    """Check that tabulating at the nodes produces the identity matrix."""
    fe = LagrangeElement(cell, degree)

    assert (np.round(fe.tabulate(fe.nodes)-np.eye(len(fe.nodes)), 10) == 0).all()


if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
