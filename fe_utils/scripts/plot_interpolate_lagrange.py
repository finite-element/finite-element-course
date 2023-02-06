#! /usr/bin/env python
from matplotlib import pyplot as plt
from argparse import ArgumentParser
from fe_utils.finite_elements import lagrange_points
from fe_utils import ReferenceTriangle, ReferenceInterval, LagrangeElement
from matplotlib import cm
import numpy as np
from math import *  # NOQA F403


def plot_interpolate_lagrange():
    parser = ArgumentParser(
        description="Plot a function interpolated onto the reference element."
    )
    parser.add_argument(
        "function", type=str, nargs=1,
        help='An expression in the coordinate vector x. The '
        'function should be a quoted string. E.g. "sin(x[0])".'
    )
    parser.add_argument("dimension", type=int, nargs=1, choices=(1, 2),
                        help="Dimension of reference cell.")
    parser.add_argument("degree", type=int, nargs=1,
                        help="Degree of basis functions.")

    args = parser.parse_args()
    dim = args.dimension[0]
    degree = args.degree[0]
    fn = eval('lambda x: ' + args.function[0])

    cells = (None, ReferenceInterval, ReferenceTriangle)

    fe = LagrangeElement(cells[dim], degree)
    coefs = fe.interpolate(fn)

    if dim == 1:
        x = np.linspace(0, 1, 100)
        x.shape = (100, 1)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        y = fe.tabulate(x)

        for c, y_ in zip(coefs, y.T):
            plt.plot(x, c * y_, "--")
        plt.plot(x, np.dot(y, coefs), 'k')

    if dim == 2:
        x = lagrange_points(ReferenceTriangle, 20)
        z = fe.tabulate(x)

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot_trisurf(x[:, 0], x[:, 1], np.dot(z, coefs), cmap=cm.RdBu,
                        linewidth=0)

    plt.show()
