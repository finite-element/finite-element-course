#! /usr/bin/env python
from matplotlib import pyplot as plt
from argparse import ArgumentParser
from fe_utils.finite_elements import lagrange_points
from fe_utils import ReferenceTriangle, ReferenceInterval, LagrangeElement
from matplotlib import cm
import numpy as np


def plot_lagrange_basis_functions():
    parser = ArgumentParser(
        description="""Plot the nodes on the reference cell."""
    )
    parser.add_argument("dimension", type=int, nargs=1, choices=(1, 2),
                        help="Dimension of the reference cell.")
    parser.add_argument("degree", type=int, nargs=1,
                        help="Degree of polynomial basis.")
    args = parser.parse_args()
    dim = args.dimension[0]
    degree = args.degree[0]

    cells = (None, ReferenceInterval, ReferenceTriangle)

    fe = LagrangeElement(cells[dim], degree)

    if dim == 1:
        x = np.linspace(0, 1, 100)
        x.shape = (100, 1)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        y = fe.tabulate(x)

        for y_ in y.T:
            plt.plot(x, y_)

    if dim == 2:
        x = lagrange_points(ReferenceTriangle, 20)
        z = fe.tabulate(x)

        fig = plt.figure(figsize=(20, 4))
        ax = fig.gca(projection='3d')

        offsets = fe.nodes * fe.degree * 1.1

        for o, z_ in zip(offsets, z.T):
            ax.plot_trisurf(x[:, 0]+o[0], x[:, 1]+o[1], z_, cmap=cm.RdBu,
                            linewidth=0)

    plt.show()
