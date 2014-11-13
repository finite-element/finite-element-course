Meshes
======

When employing the finite element method, we represent the domain on
which we wish to solve our PDE as a mesh. In order to work with
meshes, we need to have a somewhat more formal mathematical notion of
a mesh.

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

foo
