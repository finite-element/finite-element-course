.. default-role:: math

Meshes
======

When employing the finite element method, we represent the domain on
which we wish to solve our PDE as a mesh. In order to work with
meshes, we need to have a somewhat more formal mathematical notion of
a mesh. The mesh concepts we will employ here are loosely based on
those in :cite:`Logg2009`, and are typical of mesh representations for the
finite element method.

Mesh entities
-------------

A mesh is composed of *topological entities*, such as vertices, edges,
polygons and polyhedra.

.. definition:: 

   The *(topological) dimension* of a mesh is the largest
   dimension among all of the topological entities in a mesh.

In this course we will not consider meshes of manifolds immersed in
higher dimensional spaces (for example the surface of a sphere
immersed in `\mathbb{R}^3`) so the topological dimension of the
mesh will always match the geometric dimension of space in which we
are working, so we will simply refer to the *dimension* of the mesh.

.. definition::

   A topological entity of *codimension* `n` is a topological
   entity of dimension `d-n` where `d` is the dimension of the
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
them. We will identify topological entities by an index pair `(d, i)`
where `i` is the index of the entity within the set of `d`-dimensional
entities. For example, entity `(0, 10)` is vertex number 10, and
entity `(1, 10)` is edge 10. :numref:`figmesh` shows an example
mesh with the topological entities labelled.

.. _figmesh:

.. figure:: mesh.svg
   :width: 80%

   A triangular mesh showing labelled topological entities: vertices
   (black), edges (red), and cells (blue).

Reference cell entities
-----------------------

The reference cells similarly have locally numbered topological
entities, these are shown in :numref:`figreferenceentities`. The
numbering is a matter of convention: that adopted here is that edges
share the number of the opposite vertex. The orientation of the edges
is also shown, this is always from the lower numbered vertex to the
higher numbered one.

.. _figreferenceentities:

.. figure:: entities.svg
   :width: 50%

   Local numbering and orientation of the reference entities.

Adjacency
---------

In order to implement the finite element method, we need to integrate
functions over cells, which means knowing which basis functions are
nonzero in a given cell. For the function spaces used in the finite
element method, these basis functions will be the ones whose nodes lie
on the topological entities adjacent to the cell. That is, the
vertices, edges and (in 3D) the faces making up the cell, as well as
the cell itself. One of the roles of the mesh is therefore to provide
a lookup facility for the lower-dimensional mesh entities adjacent to
a given cell.

.. definition::

   Given a mesh `M`, then for each `\dim(M) \geq d_1 > d_2 \geq 0`
   the *adjacency* function `\operatorname{Adj}_{d_1,d_2}:\,
   \mathbb{N}\rightarrow \mathbb{N}^k` is the function such that:

   .. math::

      \operatorname{Adj}_{d_1,d_2}(i) = (i_0, \ldots i_k)

   where `(d_1, i)` is a topological entity and `(d_2, i_0), \ldots,
   (d_2, i_k)` are the adjacent `d_2`-dimensional topological entities
   numbered in the corresponding reference cell order. If every cell
   in the mesh has the same topology then `k` will be fixed for each
   `(d_1, d_2)` pair. The correspondence between the orientation of
   the entity `(d_1, i)` and the reference cell of dimension `d_1` is
   established by specifying that the vertices are numbered in
   ascending order [#simplexnumbering]_. That is, for any entity `(d_1, i)`:
   
   .. math::

    (i_0, \ldots i_k) = \operatorname{Adj}_{d_1,0}(i) \quad \Longrightarrow \quad i_0 < \ldots <i_k

   A consequence of this convention is that the global orientation of
   all the entities making up a cell also matches their local
   orientation.
   
.. example::

   In the mesh shown in :numref:`figmesh` we have:
   
   .. math::

      \operatorname{Adj}_{2,0}(3) = (1,5,8).

   In other words, vertices 1, 5 and 8 are adjacent to cell 3. Similarly:

   .. math::

      \operatorname{Adj}_{2,1}(3) = (11,5,9).
   
   Edges 11, 5, and 9 are local edges 0, 1, and 2 of cell 3.


Function spaces: associating data with meshes
=============================================

A finite element space over a mesh is constructed by associating a
finite element with each cell of the mesh. Will refer to the basis
functions of this finite element space as *global* basis functions,
while those of the finite element itself we will refer to as *local*
basis functions. We can establish the relationship between the finite
element and each cell of the mesh by associating the nodes (and
therefore the local basis functions) of the finite element with the
topological entities of the mesh. This is a two stage process. First,
we associate the nodes of the finite element with the local
topological entities of the reference cell. This is often referred to
as *local numbering*. Then we associate the correct number of degrees
of freedom with each global mesh entity. This is the *global
numbering*.

Local numbering and continuity
------------------------------

Which nodes should be associated with which topological entities? The
answer to this question depends on the degree of continuity required
between adjacent cells. The nodes associated with topological entites
on the boundaries of cells (the vertices in one dimension, the
vertices and edges in two dimensions, and the vertices, edges and
faces in three dimensions) are shared between cells. The basis
functions associated with nodes on the cell boundary will therefore be
continuous between the cells which share that boundary.  

For the Lagrange element family, we require global `C_0`
continuity. This implies that the basis functions are continuous
everywhere. This has the following implications for the association of
basis functions with local topological entites:

vertices
  At the function vertices we can achieve continuity by requiring
  that there be a node associated with each mesh vertex. The basis
  function associated with that node will therefore be continuous. Since
  we have a nodal basis, all the other basis functions will vanish at
  the vertex so the global space will be continuous at this point.

edges
  Where the finite element space has at least 2 dimensions we need to
  ensure continuity along edges. The restriction of a degree `p`
  polynomial over a `d`-dimensional cell to an edge of that cell will
  be a one dimensional degree `p` polynomial. To fully specify this
  polynomial along an edge requires `p+1` nodes. However there will
  already be two nodes associated with the vertices of the edge, so
  `p-1` additional nodes will be associated with the edge. 

faces
  For three-dimensional (tetrahedral) elements, the basis
  functions must also be continuous across faces. This requires that
  sufficient nodes lie on the face to fully specify a two dimensional
  degree `p` polynomial. However the vertices and edges of the face
  already have nodes associated with them, so the number of nodes
  required to be associated with the face itself is actually the
  number required to represent a degree `p-2` polynomial in two
  dimensions: `\begin{pmatrix}p-1\\ 2\end{pmatrix}`.

:numref:`figlagrange-nodes` illustrates the association of nodes with
reference entities for Lagrange elements on triangles. The numbering
of nodes will depend on how
:func:`~fe_utils.finite_elements.lagrange_points` is implemented. The
numbering used here is just one of the obvious choices.

.. _figlagrange-nodes:

.. figure:: lagrange_nodes.svg
   :width: 70%

   Association of nodes with reference entities for the degree 1, 2,
   and 3 equispaced Lagrange elements on triangles. Black nodes are
   associated with vertices, red nodes with edges and blue nodes with
   the cell (face). The numbering of the nodes is arbitrary.

Implementing local numbering
----------------------------

Local numbering can be implemented by adding an additional data
structure to the :class:`~fe_utils.finite_elements.FiniteElement`
class. For each local entity this must record the local nodes
associated with that entity. This can be achieved using a dictionary
of dictionaries structure. For example employing the local numbering
of nodes employed in :numref:`figlagrange-nodes`, the ``entity_node``
list for the degree three equispaced Lagrange element on a triangle is
given by::

  entity_node = {0: {0: [0],
                     1: [3],
                     2: [9]},
                 1: {0: [6, 8],
                     1: [4, 7],
                     2: [1, 2]},
                 2: {0: [5]}}

Note that the order of the nodes in each list is important: it must
always consistently reflect the orientation of the relevant entity in
order that all the cells which share that entity consistently
interpret the nodes. In this case this has been achieved by listing
the nodes in order given by the direction of the orientation of each edge. 

.. exercise::

   Extend the :meth:`__init__` method of
   :class:`~fe_utils.finite_elements.LagrangeElement` so that it
   passes the correct ``entity_node`` dictionary to the
   :class:`~fe_utils.finite_elements.FiniteElement` it creates.

.. hint::

   You can either work out the right algorithm to generate
   ``entity_nodes`` with the right node indices, or you can modify
   :func:`~fe_utils.finite_elements.lagrange_points` so that it
   produces the nodes in entity order, thus making the construction of
   ``entity_nodes`` straightforward.


Mesh geometry
-------------

The features of meshes we have so far considered are purely
topological: they deal with the adjacency relationships between
topological entities, but do not describe the locations of those
entities in space.  

.. rubric:: Footnotes

.. [#simplexnumbering] The numbering convention adopted here is very
                       convenient, but only works for meshes composed
                       of simplices (vertices, intervals, triangles
                       and tetrahedra). A more complex convention
                       would be required to support quadrilateral
                       meshes.
