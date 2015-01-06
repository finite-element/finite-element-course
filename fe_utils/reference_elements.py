import numpy as np

class ReferenceCell(object):

    def __init__(self, vertices, topology):
        """An object storing the geometry and topology of the reference cell.

        :param vertices: a list of coordinate vectors corresponding to
          the coordinates of the vertices of the cell.
        :param topology: a dictionary of dictionaries such that topology[d][i] 
          is the list of vertices incident to the `i`-th `d`-entity.
        """
        
        self.topology = topology
        
        self.vertices = np.array(vertices, dtype=np.double)

        """The geometric and topological dimension of the reference cell."""
        self.dim = self.vertices.shape[1]

        if self.dim != len(topology) - 1:
            raise ValueError("Dimension mismatch between vertices and topology.")

#: A :class:`ReferenceCell` storing the geometry and topology of the interval [0, 1].
ReferenceInterval = ReferenceCell(vertices=[[0.], [1.]],
                                  topology={0: {0: [0],
                                                1: [1]},
                                            1: {0: [0, 1]}}
                              )

#: A :class:`ReferenceCell` storing the geometry and topology of the triangle
#: with vertices [[0., 0.], [1., 0.], [0., 1.]].
ReferenceTriangle = ReferenceCell(vertices=[[0., 0.], [1., 0.], [0., 1.]],
                                  topology={0: {0: [0],
                                                1: [1],
                                                2: [2]},
                                            1: {0: [1, 2],
                                                1: [0, 2],
                                                2: [0, 1]},
                                            2: {0: [0, 1, 2]}}
                              )
