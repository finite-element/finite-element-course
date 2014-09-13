import triangle
import numpy as np
import itertools


class Mesh(object):
    """A one or two dimensional mesh composed of intervals or triangles
    respectively."""
    def __init__(self, vertices, element_vertices):
        """
        :param vertices: an vertex_count x dim array of the coordinates of 
          the vertices in the mesh.
        :param element_vertices: an element_count x (dim+1) array of the 
          indices of the vertices of which each element is made up.  
        """

        self.dim = vertices.shape(1)
        """The spatial dimension of the mesh. Immersed manifolds are not
        supported."""

        if self.dim not in (1, 2):
            raise ValueError("Only 1D and 2D meshes are supported")

        self.vertices = vertices
        """The coordinates of all the vertices in the mesh."""

        self.element_vertices = element_vertices
        """The indices of the vertices incident to element."""

        if self.dim == 2:
            self.edge_vertices = np.unique(tuple(sorted(e))
                                           for t in element_vertices
                                           for e in itertools.combinations(t, 2))
            """The indices of the vertices incident to edge (only for 2D
            meshes)."""

            # Invert self.edge_vertices so that it is possible to look up
            # the edge index given the vertex indices.
            edge_dict = {tuple(e): i
                         for i, e_ in enumerate(self.edge_vertices)
                         for e in (e_, reversed(e_))}

            # List the local vertex indices associated with
            # each local edge index.
            local_edge_vertices = np.array([[1, 2], [0, 2], [0, 1]])

            self.element_edges = np.fromiter(
                (edge_dict[tuple(t.take(local_edge_vertices[e]))]
                 for e in range(3)
                 for t in self.element_vertices),
                dtype=np.int32,
                count=self.element_vertices.size).reshape((-1, 3))
            """The indices of the edges incident to each element (only for 2D
            meshes)."""

    def adjacency(self, dim1, dim2):
        """Return the set of `dim2` entities adjacent to each `dim1`
        entity. For example if `dim1==2` and `dim2==1` then return the list of
        edges (1D entities) adjacent to each triangle (2D entity).

        This operation is only defined where `self.dim > dim1 > dim2`.

        This method is simply a more systematic way of accessing
        :attr:`edge_vertices`, :attr:`element_edges` and :attr:`element_vertices`.
        """

        if dim2 >= dim1:
            raise ValueError("""dim2 must be less than dim1.""")
        if dim2 < 0:
            raise ValueError("""dim2 cannot be negative.""")
        if dim1 > self.dim:
            raise ValueError("""dim1 cannot exceed the mesh dimension.""")

        if dim1 == 1:
            return self.edge_vertices
        elif dim1 == 2:
            if dim2 == 0:
                return self.element_vertices
            else:
                return self.element_edges


class UnitSquareMesh(Mesh):
    def __init__(self, nx, ny):
        points = list((x, y) for x in np.arange(nx) for y in np.arange(ny))

        mesh = triangle.triangulate({"vertices": points})

        super(UnitSquareMesh, self).__init__(mesh["vertices"],
                                             mesh["triangles"])
        
