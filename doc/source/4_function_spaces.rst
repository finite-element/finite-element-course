.. default-role:: math

Function spaces: associating data with meshes
=============================================

A finite element space over a mesh is constructed by associating a
finite element with each cell of the mesh. We will refer to the basis
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

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/JwUmZt2aknU>`_

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

This pattern holds more generally: for a `C_0` function space, the
number of nodes which must be associated with a local topological
entity of degree `d` is `\begin{pmatrix}p-1\\ d\end{pmatrix}`.

:numref:`figlagrange-nodes` illustrates the association of nodes with
reference entities for Lagrange elements on triangles. The numbering
of nodes will depend on how
:func:`~fe_utils.finite_elements.lagrange_points` is implemented. The
numbering used here is just one of the obvious choices.

.. _figlagrange-nodes:

.. figure:: lagrange_nodes.*
   :width: 70%

   Association of nodes with reference entities for the degree 1, 2,
   and 3 equispaced Lagrange elements on triangles. Black nodes are
   associated with vertices, red nodes with edges and blue nodes with
   the cell (face). The numbering of the nodes is arbitrary.
   
Implementing local numbering
----------------------------


.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/HswJShGI8X8>`_


Local numbering can be implemented by adding an additional data
structure to the :class:`~fe_utils.finite_elements.FiniteElement`
class. For each local entity this must record the local nodes
associated with that entity. This can be achieved using a dictionary
of dictionaries structure. For example employing the local numbering
of nodes employed in :numref:`figlagrange-nodes`, the ``entity_node``
dictionary for the degree three equispaced Lagrange element on a triangle is
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

.. only:: html

  The following animation illustrates the construction of the ``entity_node`` dictionary.
          
  .. container:: youtube

    .. youtube:: dTWoTjARi2w?modestbranding=1;controls=0;rel=0
       :width: 100%


.. proof:exercise::

   Extend the :meth:`__init__` method of
   :class:`~fe_utils.finite_elements.LagrangeElement` so that it
   passes the correct ``entity_node`` dictionary to the
   :class:`~fe_utils.finite_elements.FiniteElement` it creates.

   The ``test/test_08_entity_nodes.py`` script tests this functionality.

.. hint::

   You can either work out the right algorithm to generate
   ``entity_nodes`` with the right node indices, or you can modify
   :func:`~fe_utils.finite_elements.lagrange_points` so that it
   produces the nodes in entity order, thus making the construction of
   ``entity_nodes`` straightforward.

   You may find the
   :meth:`~fe_utils.reference_elements.ReferenceCell.point_in_entity`
   method of the :class:`~fe_utils.reference_elements.ReferenceCell`
   class useful.

Global numbering
----------------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/AgkunNycPWo>`_

Given a mesh and a finite element, the global numbering task is to
uniquely associate the appropriate number of global node numbers with
each global entity. One such numbering [#globalnumbering]_ is to
allocate global numbers in ascending entity dimension order, and
within each dimension in order of the index of each global topological
entity. The formula for the first global node associated with entity
`(d, i)` is then:

.. math::

   G(d, i) = \left(\sum_{\delta < d} N_\delta E_\delta\right) + iN_d

where `N_d` is the number of nodes which this finite element
associates with each entity of dimension `d`, and `E_d` is the number
of dimension `d` entities in the mesh. The full list of nodes
associated with entity `(d, i)` is therefore:

.. math::
   :label:

   [G(d, i), \ldots, G(d,i) + N_d - 1]

.. _cell-node:

The cell-node map
-----------------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/VHq3xJ-O9xc>`_


The primary use to which we wish to put the finite element spaces we
are constructing is, naturally, the solution of finite element
problems. The principle operation we will therefore need to support is
integration over the mesh of mathematical expressions involving
functions in finite element spaces. This will be accomplished by
integrating over each cell in turn, and then summing over all
cells. This means that a key operation we will need is to find the
nodes associated with a given cell.

It is usual in finite element software to explicitly store the map
from cells to adjacent nodes as a two-dimensional array with one row
corresponding to each cell, and with columns corresponding to the
local node numbers. The entries in this map will have the following values:

.. math::
   :label: eqcellnode

   M[c, e(\delta, \epsilon)] = [G(\delta, i), \ldots, G(\delta,i) + N_\delta - 1] \qquad\forall 0\leq\delta\leq\dim(c), \forall 0\leq\epsilon < \hat{E}_\delta

where:

.. math::
   :label:

   i = \operatorname{Adj}_{\dim(c), \delta}[c, \epsilon],

`e(\delta, \epsilon)` is the local entity-node list for this finite
element for the `(\delta, \epsilon)` local entity,
`\operatorname{Adj}` has the meaning given under :ref:`secadjacency`,
`\hat{E}_\delta` is the number of dimension `\delta` entities in each
cell, and `G` and `N` have the meanings given above. This algorithm
requires a trivial extension to adjacency:

.. math::
   :label:

   \operatorname{Adj}_{\dim(c),\dim(c)}[c, 0] = c

.. hint::
   
   In :eq:`eqcellnode`, notice that for each value of `\delta` and
   `\epsilon`, `e(\delta, \epsilon)` is a vector of indices, so the
   equation sets the value of zero, one, or more defined entries in row `c`
   of `M` for each `\delta` and `\epsilon`.
   
Implementing function spaces in Python
--------------------------------------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/cLVi-5DKZO8>`_


As noted above, a finite element space associates a mesh and a finite
element, and contains (in some form) a global numbering of the nodes. 

.. _ex-function-space:

.. proof:exercise::
   
   Implement the :meth:`__init__` method of
   :class:`fe_utils.function_spaces.FunctionSpace`. The key operation
   is to set
   :attr:`~fe_utils.function_spaces.FunctionSpace.cell_nodes` using
   :eq:`eqcellnode`.

   You can plot the numbering you have created with the
   ``plot_function_space_nodes`` script. As usual, run the
   script passing the ``-h`` option to discover the required
   arguments.

.. hint::

   Many of the terms in :eq:`eqcellnode` are implemented in the
   objects in :mod:`fe_utils`. For example:

   * `\operatorname{Adj}_{\dim(c), \delta}` is implemented by the
     :meth:`~fe_utils.mesh.Mesh.adjacency` method of the
     :class:`~fe_utils.mesh.Mesh`.

   * You have `e(\delta, \epsilon)` as
     :data:`~fe_utils.finite_elements.FiniteElement.entity_nodes`. Note
     that in this case you need separate square brackets for each
     index::

           element.entity_nodes[delta][epsilon]

.. hint::

   :attr:`~fe_utils.function_spaces.FunctionSpace.cell_nodes` needs to
   be integer-valued. If you choose to use :func:`numpy.zeros`
   to create a matrix which you then populate with values, you
   need to explicitly specify that you want a matrix of
   integers. This can be achieved by passing the ``dtype`` argument
   to :func:`numpy.zeros`. For example ``numpy.zeros((nrows, ncols), dtype=int)``.

.. rubric:: Footnotes

.. [#globalnumbering]  Many correct global numberings are possible,
                       that presented here is simple and correct, but not
                       optimal from the perspective of the memory
                       layout of the resulting data.
