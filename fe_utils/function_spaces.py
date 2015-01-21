import numpy as np
from . import ReferenceTriangle, ReferenceInterval
from .finite_element import LagrangeElement, lagrange_points
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


class FunctionSpace(object):

    def __init__(self, mesh, element):
        """A finite element space.

        :param mesh: The :class:`~.mesh.Mesh` on which this space is built.
        :param element: The :class:`~.finite_elements.FiniteElement` of this space.

        Most of the implementation of this class is left as an :ref:`exercise
        <ex-function_space>`.
        """

        #: The :class:`~.mesh.Mesh` on which this space is built.
        self.mesh = mesh
        #: The :class:`~.finite_elements.FiniteElement` of this space.
        self.element = element

        raise NotImplementedError

        # Implement global numbering in order to produce the global
        # cell node list for this space.
        #: The global cell node list. This is a two-dimensional in which each row
        #: lists the global nodes incident to the corresponding cell.
        self.cell_nodes = None

        #: The total number of nodes in the function space.
        self.node_count = np.dot(element.nodes_per_entity, mesh.entity_counts)


class Function(object):
    def __init__(self, function_space, name=None):
        """A function in a finite element space. The main role of this object
        is to store the basis function coefficients associated with the nodes
        of the underlying function space.

        :param function_space: The :class:`FunctionSpace` in which
            this :class:`Function` lives.
        :param name: An optional label for this :class:`Function`
            which will be used in output and is useful for debugging.
        """

        #: The :class:`FunctionSpace` in which this :class:`Function` lives.
        self.function_space = function_space

        #: The (optional) name of this :class:`Function`
        self.name = name

        #: The basis function coefficient values for this :class:`Function`
        self.values = np.zeros(function_space.node_count)

    def interpolate(self, fn):
        """Interpolate a given Python function onto this finite element
        :class:`Function`.

        :param fn: A function ``fn(X)`` which takes a coordinate
          vector and returns a scalar value.

        """

        fs = self.function_space

        # Create a map from the vertices to the element nodes on the
        # reference cell.
        cg1 = LagrangeElement(fs.cell, 1)
        coord_map = cg1.tabulate(fs.element.nodes)

        for c in fs.mesh.entity_counts[-1]:
            # Interpolate the coordinates to the cell nodes.
            vertex_coords = fs.mesh.vertex_coords[fs.mesh.cell_vertices[c, :], :]
            node_coords = np.dot(coord_map, vertex_coords)

            self.values[fs.cell_nodes[c, :]] = [fn(x) for x in node_coords]

    def plot(self, subdivisions=None):
        """Plot the value of this :class:`Function`.

        :param subdivisions: The number of points in each direction to
          use in representing each element. The default is
          :math:`2d+1` where :math:`d` is the degree of the
          :class:`FunctionSpace`. Higher values produce prettier plots
          which render more slowly!

        """

        fs = self.function_space

        d = subdivisions or (2 * (fs.element.degree + 1) if fs.element.degree > 1 else 2)

        # Interpolation rule for element values.
        local_coords = lagrange_points(fs.element.cell, d)
        function_map = fs.element.tabulate(local_coords)

        # Interpolation rule for coordinates.
        cg1 = LagrangeElement(fs.cell, 1)
        coord_map = cg1.tabulate(fs.element.nodes)

        values = set()

        for c in fs.mesh.entity_counts[-1]:
            vertex_coords = fs.mesh.vertex_coords[fs.mesh.cell_vertices[c, :], :]
            x = np.dot(coord_map, vertex_coords)

            local_function_coefs = fs.values[fs.cell_nodes[c, :]]
            v = np.dot(function_map, local_function_coefs)

            values.update(zip(x, v))

        if fs.element.cell is ReferenceInterval:
            x, v = map(np.array, zip(*sorted(values)))

            fig = plt.figure()
            fig.add_subplot(111)

            plt.plot(x, v)

        else:
            x, v = map(np.array, zip(*values))

            fig = plt.figure()
            ax = fig.gca(projection='3d')

            ax.plot_trisurf(x[:, 0], x[:, 1], v, cmap=cm.RdBu, linewidth=0)

        plt.show()
