#! /usr/bin/env python
from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle, UnitSquareMesh, \
    ReferenceInterval, UnitIntervalMesh
from argparse import ArgumentParser
import numpy as np


def plot_mesh():
    parser = ArgumentParser(
        description="""Plot the topological entities in a regular mesh."""
    )
    parser.add_argument("dimension", type=int, nargs=1, choices=(1, 2),
                        help="Dimension of the domain.")
    parser.add_argument(
        "resolution", type=int, nargs=1,
        help="The number of cells in each direction of the mesh."
    )

    args = parser.parse_args()
    resolution = args.resolution[0]
    cell = (None, ReferenceInterval, ReferenceTriangle)[args.dimension[0]]

    if cell is ReferenceTriangle:
        mesh = UnitSquareMesh(resolution, resolution)
    else:
        mesh = UnitIntervalMesh(resolution)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if cell is ReferenceTriangle:
        for e in mesh.edge_vertices:
            plt.plot(mesh.vertex_coords[e, 0], mesh.vertex_coords[e, 1], 'k')
    else:
        for e in mesh.adjacency(1, 0):
            plt.plot(
                mesh.vertex_coords[e, 0], 0. * mesh.vertex_coords[e, 0], 'k'
            )

    colours = ["black", "red", "blue"]

    for i, x in enumerate(mesh.vertex_coords):
        x_ = x if cell.dim == 2 else (x[0], 0.)
        ax.annotate('(%s, %s)' % (0, i), xy=x_, xytext=(10, 1),
                    textcoords='offset points', color=colours[0])

    for d in range(1, mesh.dim + 1):
        adj = mesh.adjacency(d, 0)
        for i, e in enumerate(adj):
            x = np.mean(mesh.vertex_coords[e, :], axis=0)
            x_ = x if cell.dim == 2 else (x[0], 0.)
            ax.annotate('(%s, %s)' % (d, i), xy=x_, xytext=(10, 1),
                        textcoords='offset points', color=colours[d])

    if cell is ReferenceTriangle:
        ax.axis(np.add(ax.axis(), [-.1, .1, -.1, .1]))
    else:
        plt.plot(mesh.vertex_coords[:, 0], 0 * mesh.vertex_coords[:, 0], 'ko')

        ax.axis([-.1, 1.1, -.1, .1])

    plt.show()
