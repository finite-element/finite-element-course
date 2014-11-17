Meshes
======

When employing the finite element method, we represent the domain on
which we wish to solve our PDE as a mesh. In order to work with
meshes, we need to have a somewhat more formal mathematical notion of
a mesh. The mesh concepts we will employ here are loosely based on
those in Logg2009, and are typical of mesh representations for the
finite element method.

A mesh is composed of *topological entities*, such as vertices, edges,
polygons and polyhedra.

.. definition:: 

   The *(topological) dimension* of a mesh is the largest
   dimension among all of the topological entities in a mesh.

In this course we will not consider meshes of manifolds immersed in
higher dimensional spaces (for example the surface of a sphere
immersed in :math:`\mathbb{R}^3`) so the topological dimension of the
mesh will always match the geometric dimension of space in which we
are working, so we will simply refer to the *dimension* of the mesh.

.. definition::

   A topological entity of *codimension* :math:`n` is a topological
   entity of dimension :math:`d-n` where `d` is the dimension of the
   mesh.

Armed with these definitions we are able to define names for
topological entities of various dimension and codimension:

=========== ========= ===========
entity name dimension codimension
=========== ========= ===========
vertex      0
edge        1
face        2
facet                 1
cell                  0
=========== ========= ===========

The cells of a mesh can be polygons or polyhedra of any shape, however
in this course we will restrict ourselves to meshes whose cells are
intervals or triangles. The only other two-dimensional cells
frequently employed are quadrilaterals.

The topological entities of each dimension will be given unique
numbers in order that degrees of freedom can later be associated with
them. We will identify topological entities by an index pair
:math:`(d, i)` where :math:`i` is the index of the entity within the
set of :math:`d`-dimensional entities.

In order to implement the finite element method, we need to integrate
functions over cells, which means knowing which basis functions are
nonzero in a given cell. For the function spaces used in the finite
element method, these basis functions will be the ones whose nodes lie
on the topological entities adjacent to the cell. That is, the
vertices, edges and (in 3D) the faces making up the cell, as well as
the cell itself. One of the roles of the mesh is therefore to provide
a lookup facility for the lower-dimensional mesh entities adjacent to
a given cell.

Mesh geometry
-------------

The features of meshes we have so far considered are purely
topological: they deal with the adjacency relationships between
topological entities, but do not describe the locations of those
entities in space. 
