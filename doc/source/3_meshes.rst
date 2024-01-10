.. default-role:: math

Meshes
======

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495204015"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6965d603-79d9-43be-a9e6-ac9f00eb4b73>`__

When employing the finite element method, we represent the domain on
which we wish to solve our PDE as a mesh. In order to work with
meshes, we need to have a somewhat more formal mathematical notion of
a mesh. The mesh concepts we will employ here are loosely based on
those in :cite:`Logg2009`, and are typical of mesh representations for the
finite element method.

Mesh entities
-------------

Like a cell, a mesh is composed of *topological entities*, such as vertices,
edges, polygons and polyhedra. The distinction is that a mesh is made of
potentially many cells, and a commensurate number of lower-dimensional
entities.

.. proof:definition:: 

   The *(topological) dimension* of a mesh is the largest
   dimension among all of the topological entities in a mesh.

In this course we will not consider meshes of manifolds immersed in
higher dimensional spaces (for example the surface of a sphere
immersed in `\mathbb{R}^3`) so the topological dimension of the
mesh will always match the geometric dimension of space in which we
are working, so we will simply refer to the *dimension* of the mesh.

The numbering of mesh entities is similar to that of cell entities, except that
the indices range over all of the entities of that dimension in the mesh. For
example, entity `(0, 10)` is vertex number 10, and entity `(1, 10)` is edge 10.
:numref:`figmesh` shows an example mesh with the topological entities labelled.

.. _figmesh:

.. figure:: mesh.*
   :width: 80%

   A triangular mesh showing labelled topological entities: vertices
   (black), edges (red), and cells (blue).

Adjacency
---------

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495204218"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e524a811-b08b-4379-b821-ac9f00eb4b0e>`__

In order to implement the finite element method, we need to integrate
functions over cells, which means knowing which basis functions are
nonzero in a given cell. For the function spaces used in the finite
element method, these basis functions will be the ones whose nodes lie
on the topological entities adjacent to the cell. That is, the
vertices, edges and (in 3D) the faces making up the cell, as well as
the cell itself. One of the roles of the mesh is therefore to provide
a lookup facility for the lower-dimensional mesh entities adjacent to
a given cell.

.. proof:definition::

   Given a mesh `M`, then for each `\dim(M) \geq d_1 > d_2 \geq 0`
   the *adjacency* function
   `\operatorname{Adj}_{d_1,d_2}:\, \mathbb{N}\rightarrow \mathbb{N}^k` 
   is the function such that:

   .. math::

      \operatorname{Adj}_{d_1,d_2}(i) = (i_0, \ldots i_k)

   where `(d_1, i)` is a topological entity and `(d_2, i_0), \ldots, (d_2, i_k)`
   are the adjacent `d_2`-dimensional topological entities numbered in the
   corresponding reference cell order. If every cell in the mesh has the same
   topology then `k` will be fixed for each `(d_1, d_2)` pair. The
   correspondence between the orientation of the entity `(d_1, i)` and the
   reference cell of dimension `d_1` is established by specifying that the
   vertices are numbered in ascending order [#simplexnumbering]_. That is, for
   any entity `(d_1, i)`:
   
   .. math::

    (i_0, \ldots i_k) = \operatorname{Adj}_{d_1,0}(i) \quad \Longrightarrow \quad i_0 < \ldots <i_k

   A consequence of this convention is that the global orientation of
   all the entities making up a cell also matches their local
   orientation.
   
.. proof:example::

   In the mesh shown in :numref:`figmesh` we have:
   
   .. math::

      \operatorname{Adj}_{2,0}(3) = (1,5,8).

   In other words, vertices 1, 5 and 8 are adjacent to cell 3. Similarly:

   .. math::

      \operatorname{Adj}_{2,1}(3) = (11,5,9).
   
   Edges 11, 5, and 9 are local edges 0, 1, and 2 of cell 3.

Mesh geometry
-------------

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495204381"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=aa4f119b-c23e-487d-aa38-ac9f00eb4ae0>`__

The features of meshes we have so far considered are purely
topological: they deal with the adjacency relationships between
topological entities, but do not describe the locations of those
entities in space. Provided we restrict our attention to meshes in
which the element edges are straight (ie not curved), we can represent
the geometry of the mesh by simply recording the coordinates of the
vertices. The positions of the higher dimensional entities then just
interpolate the vertices of which they are composed. We will later
observe that this is equivalent to representing the geometry in a
vector-valued piecewise linear finite element space.


A mesh implementation in Python
-------------------------------

.. only:: html

    .. dropdown:: A video recording of the following material is available here.

        .. container:: vimeo

            .. raw:: html

                <iframe src="https://player.vimeo.com/video/495204532"
                frameborder="0" allow="autoplay; fullscreen"
                allowfullscreen></iframe>

        Imperial students can also `watch this video on Panopto <https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8cc7003a-5e13-4be3-b853-ac9f00eb4b40>`__

The :class:`~fe_utils.mesh.Mesh` class provides an implementation of
mesh objects in 1 and 2 dimensions. Given the list of vertices making
up each cell, it constructs the rest of the adjacency function. It
also records the coordinates of the vertices.

The :class:`~fe_utils.mesh.UnitSquareMesh` class creates a
:class:`~fe_utils.mesh.Mesh` object corresponding to a regular
triangular mesh of a unit square. Similarly, the
:class:`~fe_utils.mesh.UnitIntervalMesh` class performs the
corresponding (rather trivial) function for a unit one dimensional
mesh.

You can observe the numbering of mesh entities in these meshes using
the ``plot_mesh`` script. Run::

  plot_mesh -h

for usage instructions.


.. rubric:: Footnotes

.. [#simplexnumbering] The numbering convention adopted here is very
                       convenient, but only works for meshes composed
                       of simplices (vertices, intervals, triangles
                       and tetrahedra). A more complex convention
                       would be required to support quadrilateral
                       meshes.
