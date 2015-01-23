.. default-role:: math

Functions in finite element spaces
==================================

Recall that the general form of a function in a finite element space is:

.. math::
   :label: function
   
   f(x) = \sum_i f_i \phi_i(x)

Where the `\phi_i(x)` are now the global basis functions achieved by
stitching together the local basis functions defined by the
:ref:`finite element <secfinitelement>`.

A python implementation of functions in finite element spaces
-------------------------------------------------------------

The :class:`~fe_utils.function_spaces.Function` class provides a
simple implementation of function storage. The input is a
:class:`~fe_utils.function_spaces.FunctionSpace` which defines the
mesh and finite element to be employed, to which the
:class:`~fe_utils.function_spaces.Function` adds an array of degree of
freedom values, one for each node in the
:class:`~fe_utils.function_spaces.FunctionSpace`.

Interpolating values into finite element spaces
-----------------------------------------------

Suppose we have a function `g(x): \mathbb{R}^n \rightarrow \mathbb{R}`
which we wish to approximate in as a function `f(x)` in some finite
element space `V`. In other words, we want to find the `f_i` such that:

.. math::

  \sum_i f_i \phi_i(x) \approx g(x)

The simplest way to do this is to *interpolate* `g(x)` onto `V`. In
other words, we evaluate:

.. math::

   f_i = n_i(g(x))

where `n_i` is the node associated with `\phi_i`. Since we are only
concerned with point evaluation nodes, this is equivalent to:

.. math::

   f_i = g(x_i)

where `x_i` is the coordinate vector of the point defining the node
`n_i`. This looks straightforward, however the `x_i` are the *global*
node points, and so far we have only defined the node points in
*local* coordinates on the reference element. 

Changing coordinates between reference and physical space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We'll refer to coordinates on the global mesh as being in *physical
space* while those on the reference element are in *local
space*. We'll use case to distinguish local and global objects, so
local coordinates will be written as `X` and global coordinates as
`x`. The key observation is that within each cell, the global
coordinates are the linear interpolation of the global coordinate
values at the cell vertices. In other words, if `\{\psi_j\}` is the
local basis for the **linear** lagrange elements on the reference cell and
`\hat{X}_j` are the corresponding global vertex locations on a cell `c`
then:

.. math::

   x = \sum_j \hat{x}_j \psi_j(X) \quad \forall x \in c.

Remember that we know the location of the nodes in local coordinates,
and we have the
:meth:`~fe_utils.finite_elements.FiniteElement.tabulate` method to
evaluate all the basis functions of an element at a known set of
points. So if we write:

.. math::

   M_{i,j} = \psi_j(X_i)

where {X_i} are the node points of our finite element, then:

.. math::

   x = M\cdot \hat{x}

Where `\hat{x}` is the `(\dim+1, \dim)` array whose rows are the current
element vertex coordinates, and `x` is the `(\textrm{nodes}, \dim)` array whose
rows are the global coordinates of the nodes in the current
element. We can then apply `g()` to each row of `x` in turn and record
the result as the :class:`~fe_utils.function_spaces.Function` value
for that node.

.. hint:: 

   The observant reader will notice that this algorithm is inefficient
   because the function values at nodes on the boundaries of elements
   are evaluated more than once. This can be avoided with a little
   tedious bookkeeping but we will not concern ourselves with that
   here.

Looking up cell coordinates and values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the previous section we used the vertex coordinates of a cell to
find the node coordinates, and then we calculated
:class:`~fe_utils.function_spaces.Function` values at those
points. The coordinates are stored in a single long list associated
with the :class:`~fe_utils.mesh.Mesh`, and the
:class:`~fe_utils.function_spaces.Function` contains a single long
list of values. We need to use *indirect addressing* to access these
values. This is best illustrated using some Python code.

Suppose ``f`` is a :class:`~fe_utils.function_spaces.Function` and,
for brevity, ``fs = f.function_space``, the
:class:`~fe_utils.function_spaces.FunctionSpace` associated with
``f``. Then the vertex indices of cell number ``c`` is::

  fs.mesh.cell_vertices[c, :]

and therefore the set of coordinate vectors for the vertices of
element ``c`` are::

  fs.mesh.vertex_coords[fs.mesh.cell_vertices[c, :], :]

That is, the ``cell_vertices`` array is used to look up the right
vertex coordinates. By a similar process we can access the values
associated with the nodes element c::

  f.values[fs.cell_nodes[c, :]]

A Python implementation of interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Putting together the change of coordinates with the right indirect
addressing, we can provide the
:class:`~fe_utils.function_spaces.Function` class with a
:meth:`~fe_utils.function_spaces.Function.interpolate` method which
interpolates a user-provided function onto the
:class:`~fe_utils.function_spaces.Function`.

.. exercise::
   
   Read and understand the
   :meth:`~fe_utils.function_spaces.Function.interpolate` method. Use
   ``test/plot_sin_function.py` to investigate interpolating different
   functions onto finite element spaces at differering resolutions and
   polynomial degrees.

.. hint::

   There is no implementation work associated with this exercise, but
   the programming constructs used in
   :meth:`~fe_utils.function_spaces.Function.interpolate` will be
   needed when you implement integration.
