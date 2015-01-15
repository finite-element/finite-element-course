import numpy as np


class ReferenceCell(object):

    def __init__(self, vertices, topology, name):
        """An object storing the geometry and topology of the reference cell.

        :param vertices: a list of coordinate vectors corresponding to
          the coordinates of the vertices of the cell.
        :param topology: a dictionary of dictionaries such that topology[d][i]
          is the list of vertices incident to the `i`-th `d`-entity.
        """

        #: The vertices making up each topological entity of the reference cell.
        self.topology = topology

        #: The list of coordinate veritices of the reference cell.
        self.vertices = np.array(vertices, dtype=np.double)

        self.name = name

        #: The geometric and topological dimension of the reference cell.
        self.dim = self.vertices.shape[1]

        if self.dim != len(topology) - 1:
            raise ValueError("Dimension mismatch between vertices and topology.")

        #: The number of entities of each dimension.
        self.entity_counts = np.array([len(d) for d in topology.values()])

    def point_in_entity(self, x, e):
        """ Return true if the point x lies on the entity e.

        :param x: The coordinate vector of the point.
        :param e: The (d, i) pair describing the entity.
        """

        vertices = self.topology[e[0]][e[1]]

        # Offset from first vertex.
        dx = np.subtract(x, self.vertices[vertices[0]])

        # Project onto space spanned by remaining vertices.
        for v in vertices[1:]:
            dv = np.subtract(self.vertices[v], self.vertices[vertices[0]])
            dx -= dv * np.dot(dx, dv) / np.dot(dv, dv)

        return (np.round(dx, 12) == 0).all()

    def __repr__(self):

        return self.name

#: A :class:`ReferenceCell` storing the geometry and topology of the interval [0, 1].
ReferenceInterval = ReferenceCell(vertices=[[0.], [1.]],
                                  topology={0: {0: [0],
                                                1: [1]},
                                            1: {0: [0, 1]}},
                                  name="ReferenceInterval")

#: A :class:`ReferenceCell` storing the geometry and topology of the triangle
#: with vertices [[0., 0.], [1., 0.], [0., 1.]].
ReferenceTriangle = ReferenceCell(vertices=[[0., 0.], [1., 0.], [0., 1.]],
                                  topology={0: {0: [0],
                                                1: [1],
                                                2: [2]},
                                            1: {0: [1, 2],
                                                1: [0, 2],
                                                2: [0, 1]},
                                            2: {0: [0, 1, 2]}},
                                  name="ReferenceTriangle")
