#! /usr/bin/env python
from fe_utils import (UnitSquareMesh, LagrangeElement, ReferenceTriangle,
                      FunctionSpace, Function)
from math import sin, pi


def plot_sin_function():
    m = UnitSquareMesh(2, 2)
    fe = LagrangeElement(ReferenceTriangle, 4)
    fs = fs = FunctionSpace(m, fe)
    f = Function(fs)
    f.interpolate(lambda x: sin(2*pi*x[0])*sin(2*pi*x[1]))
    f.plot()
