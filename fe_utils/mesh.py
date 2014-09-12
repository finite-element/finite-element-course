import triangle
import numpy as np
import itertools


class Mesh(object):
    def __init__(self, vertices, elements, edges):
        self.vertices = vertices
        self.elements = elements
        self.edges = edges


class UnitSquareMesh(Mesh):
    def __init__(self, nx, ny):
        points = list((x, y) for x in np.arange(nx) for y in np.arange(ny))

        mesh = triangle.triangulate({"vertices": points})

        edges = np.unique(sorted(e)
                          for t in mesh["triangles"]
                          for e in itertools.combinations(t, 2))

        super(UnitSquareMesh, self).__init__(mesh["vertices"],
                                             mesh["triangles"],
                                             edges)
