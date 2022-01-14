'''Test jacobian formation.'''
import pytest
from fe_utils import UnitIntervalMesh, UnitSquareMesh, LagrangeElement, \
    FunctionSpace, Function
import numpy as np


def test_jacobian_type_1d():

    m = UnitIntervalMesh(2)

    J = m.jacobian(1)

    assert isinstance(J, np.ndarray), \
        "Jacobian must be a numpy array, not a %s" % type(J)


def test_jacobian_type_2d():

    m = UnitSquareMesh(2, 2)

    J = m.jacobian(1)

    assert isinstance(J, np.ndarray), \
        "Jacobian must be a numpy array, not a %s" % type(J)


def test_jacobian_shape_1d():

    m = UnitIntervalMesh(2)

    J = m.jacobian(1)

    assert J.shape == (1, 1), \
        "Jacobian must have shape (1, 1), not %s" % str(J.shape)


def test_jacobian_shape_2d():

    m = UnitSquareMesh(2, 2)

    J = m.jacobian(1)

    assert J.shape == (2, 2), \
        "Jacobian must have shape (2, 2), not %s" % str(J.shape)


def test_jacobian_1d():

    m = UnitIntervalMesh(2)

    assert (np.abs(np.linalg.det(m.jacobian(1))) - .5).round(12) == 0


def test_jacobian_2d():

    m = UnitSquareMesh(2, 2)

    assert (np.abs(np.linalg.det(m.jacobian(1))) - .25).round(12) == 0


def test_gradient_2d():
    """Ensure the Jacobian produces the correct gradient."""
    m = UnitSquareMesh(2, 2)
    fe = LagrangeElement(m.cell, 1)
    fs = FunctionSpace(m, fe)
    f = Function(fs)
    f.interpolate(lambda x: x[0])

    for c in range(m.entity_counts[-1]):
        df = (f.values[fs.cell_nodes[0]]
              @ fe.tabulate(((0.333, 0.333),), grad=True)[0]
              @ np.linalg.inv(m.jacobian(0)))

        if not np.allclose(df, [1., 0]):
            df_T = (f.values[fs.cell_nodes[0]]
                    @ fe.tabulate(((0.333, 0.333),), grad=True)[0]
                    @ np.linalg.inv(m.jacobian(0).T))
            if np.allclose(df_T, [1., 0]):
                assert np.allclose(df, [1., 0]), \
                    "Jacobian produces incorrect gradients." \
                    " You may have computed the transposed Jacobian."
            else:
                assert np.allclose(df, [1., 0]), \
                    "Jacobian produces incorrect gradients."


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
