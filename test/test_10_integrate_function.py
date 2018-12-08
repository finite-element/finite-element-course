'''Test integration of a function in a finite element space over a mesh.'''
import pytest
from fe_utils import UnitSquareMesh, UnitIntervalMesh, \
    FunctionSpace, LagrangeElement, Function


@pytest.mark.parametrize('degree, mesh',
                         [(d, m)
                          for d in range(1, 8)
                          for m in (UnitIntervalMesh(2),
                                    UnitSquareMesh(2, 2))])
def test_integrate_result_type(degree, mesh):

    fe = LagrangeElement(mesh.cell, degree)
    fs = FunctionSpace(mesh, fe)

    f = Function(fs)

    i = f.integrate()

    assert isinstance(i, float), "Integrate must return a float, not a %s" % \
        str(type(i))


@pytest.mark.parametrize('degree, mesh',
                         [(d, m)
                          for d in range(1, 8)
                          for m in (UnitIntervalMesh(2),
                                    UnitSquareMesh(2, 2))])
def test_integrate_function(degree, mesh):

    fe = LagrangeElement(mesh.cell, degree)
    fs = FunctionSpace(mesh, fe)

    f = Function(fs)

    f.interpolate(lambda x: x[0]**degree)

    numeric = f.integrate()

    analytic = 1./(degree + 1)

    assert round(numeric - analytic, 12) == 0, \
        "Integration error, analytic solution %g, your solution %g" % \
        (analytic, numeric)


if __name__ == '__main__':
    import sys
    pytest.main(sys.argv)
