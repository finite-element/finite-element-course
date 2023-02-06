#! /usr/bin/env python
from matplotlib import pyplot as plt
from fe_utils import ReferenceTriangle, ReferenceInterval, \
    LagrangeElement, UnitSquareMesh, UnitIntervalMesh, FunctionSpace
from argparse import ArgumentParser
import numpy as np


def plot_function_space_nodes():
    parser = ArgumentParser(
        description="""Plot the nodes on the equispaced Lagrange function space
of the specified degree on a regular mesh."""
        )
    parser.add_argument("dimension", type=int, nargs=1, choices=(1, 2),
                        help="Dimension of the domain.")
    parser.add_argument(
        "resolution", type=int, nargs=1,
        help="The number of cells in each direction on the mesh."
    )
    parser.add_argument(
        "degree", type=int, nargs=1,
        help="The degree of the polynomial basis for the function space."
    )

    args = parser.parse_args()
    resolution = args.resolution[0]
    degree = args.degree[0]
    cell = (None, ReferenceInterval, ReferenceTriangle)[args.dimension[0]]

    fe = LagrangeElement(cell, degree)
    if cell is ReferenceTriangle:
        mesh = UnitSquareMesh(resolution, resolution)
    else:
        mesh = UnitIntervalMesh(resolution)
    fs = FunctionSpace(mesh, fe)

    nodes = np.empty((fs.node_count, cell.dim))
    cg1 = LagrangeElement(cell, 1)
    cg1fs = FunctionSpace(mesh, cg1)
    coord_map = cg1.tabulate(fe.nodes)
    for c in range(mesh.entity_counts[-1]):
        # Interpolate the coordinates to the cell nodes.
        vertex_coords = mesh.vertex_coords[cg1fs.cell_nodes[c, :], :]
        lcoords = np.dot(coord_map, vertex_coords)

        # Insert the resulting cells into the global set.
        nodes[fs.cell_nodes[c, :].astype(int), :] = lcoords

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if cell is ReferenceTriangle:
        for e in mesh.edge_vertices:
            plt.plot(mesh.vertex_coords[e, 0], mesh.vertex_coords[e, 1], 'k')

        plt.plot(nodes[:, 0], nodes[:, 1], 'bo')

        for i, x in enumerate(nodes):
            ax.annotate(str(i), xy=x, xytext=(10, 1),
                        textcoords='offset points')

        ax.axis([-.1, 1.1, -.1, 1.1])
    else:
        for e in mesh.cell_vertices:
            plt.plot(mesh.vertex_coords[e, 0], 0 * mesh.vertex_coords[e, 0],
                     'k')

        plt.plot(nodes[:, 0], 0 * nodes[:, 0], 'bo')
        plt.plot(mesh.vertex_coords[:, 0], 0 * mesh.vertex_coords[:, 0], 'ko')

        for i, x in enumerate(nodes):
            ax.annotate(str(i), xy=(x[0], 0), xytext=(10, 1),
                        textcoords='offset points')

        ax.axis([-.1, 1.1, -.1, .1])

    plt.show()
