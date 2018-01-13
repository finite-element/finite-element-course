'''Test the creation of the basis function coefficients for lagrange elements.'''
import pytest
import numpy as np
from fe_utils import FiniteElement, ReferenceInterval, ReferenceTriangle
from fe_utils.finite_elements import vandermonde_matrix


@pytest.mark.parametrize('cell', (ReferenceInterval, ReferenceTriangle))
def test_init_finite_element(cell):

    nodes = cell.vertices

    fe = FiniteElement(cell, 1, nodes)

    v = vandermonde_matrix(cell, 1, nodes)

    assert (np.round(np.dot(fe.basis_coefs, v) - np.eye(cell.dim+1)) == 0).all()

if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
