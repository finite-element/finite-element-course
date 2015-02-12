'''Test integration of a function in a finite element space over a mesh.'''
import pytest
from fe_utils import UnitSquareMesh, UnitIntervalMesh, \
    FunctionSpace, LagrangeElement, Function


@pytest.fixture
def square():

    return UnitSquareMesh(2, 2)


@pytest.fixture
def interval():

    return UnitIntervalMesh(2)


@pytest.mark.parametrize('degree', range(1, 8))
def test_integrate_unit_interval(degree, interval):

    fe = LagrangeElement(interval.cell, degree)
    fs = FunctionSpace(interval, fe)

    f = Function(fs)

    f.interpolate(lambda x: x[0]**degree)

    numeric = f.integrate()

    analytic = 1./(degree + 1)

    assert round(numeric - analytic, 12) == 0, \
        "Integration error, analytic solution %g, your solution %g" % \
        (numeric, analytic)


if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
