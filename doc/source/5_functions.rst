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

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/HTTCzLZw-ao>`_

The :class:`~fe_utils.function_spaces.Function` class provides a
simple implementation of function storage. The input is a
:class:`~fe_utils.function_spaces.FunctionSpace` which defines the
mesh and finite element to be employed, to which the
:class:`~fe_utils.function_spaces.Function` adds an array of degree of
freedom values, one for each node in the
:class:`~fe_utils.function_spaces.FunctionSpace`.

Interpolating values into finite element spaces
-----------------------------------------------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/WXiE8Yx_m0Q>`_

Suppose we have a function `g(x): \mathbb{R}^n \rightarrow \mathbb{R}`
which we wish to approximate as a function `f(x)` in some finite
element space `V`. In other words, we want to find the `f_i` such that:

.. math::
   :label:

   \sum_i f_i \phi_i(x) \approx g(x)

The simplest way to do this is to *interpolate* `g(x)` onto `V`. In
other words, we evaluate:

.. math::
   :label:

   f_i = n_i(g(x))

where `n_i` is the node associated with `\phi_i`. Since we are only
concerned with point evaluation nodes, this is equivalent to:

.. math::
   :label:

   f_i = g(x_i)

where `x_i` is the coordinate vector of the point defining the node
`n_i`. This looks straightforward, however the `x_i` are the *global*
node points, and so far we have only defined the node points in
*local* coordinates on the reference element. 

.. _coordinates:

Changing coordinates between reference and physical space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We'll refer to coordinates on the global mesh as being in *physical
space* while those on the reference element are in *local
space*. We'll use case to distinguish local and global objects, so
local coordinates will be written as `X` and global coordinates as
`x`. The key observation is that within each cell, the global
coordinates are the linear interpolation of the global coordinate
values at the cell vertices. In other words, if `\{\Psi_j\}` is the
local basis for the **linear** lagrange elements on the reference cell and
`\hat{x}_j` are the corresponding global vertex locations on a cell `c`
then:

.. math::
   :label: change

   x = \sum_j \hat{x}_j \Psi_j(X) \quad \forall x \in c.

Remember that we know the location of the nodes in local coordinates,
and we have the
:meth:`~fe_utils.finite_elements.FiniteElement.tabulate` method to
evaluate all the basis functions of an element at a known set of
points. So if we write:

.. math::
   :label: foo0

   A_{i,j} = \Psi_j(X_i)

where {X_i} are the node points of our finite element, then:

.. math::
   :label: foo1

   x = A\cdot \hat{x}

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

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/ZmUPyydAasY>`_

In the previous section we used the vertex coordinates of a cell to
find the node coordinates, and then we calculated
:class:`~fe_utils.function_spaces.Function` values at those
points. The coordinates are stored in a single long list associated
with the :class:`~fe_utils.mesh.Mesh`, and the
:class:`~fe_utils.function_spaces.Function` contains a single long
list of values. We need to use *indirect addressing* to access these
values. This is best illustrated using some Python code.

Suppose ``f`` is a :class:`~fe_utils.function_spaces.Function`.
For brevity, we write ``fs = f.function_space``, the
:class:`~fe_utils.function_spaces.FunctionSpace` associated with
``f``. Now, we first need a linear element and a corresponding
:class:`~fe_utils.function_spaces.FunctionSpace`::

  cg1 = fe_utils.LagrangeElement(fs.mesh.cell, 1)
  cg1fs = fe_utils.FunctionSpace(fs.mesh, cg1)

Then the vertex indices of cell number ``c`` in the correct order for the linear Lagrange element are::

  cg1fs.cell_nodes[c, :]

and therefore the set of coordinate vectors for the vertices of
element ``c`` are::

  fs.mesh.vertex_coords[cg1fs.cell_nodes[c, :], :]

That is, the ``cg1fs.cell_nodes`` array is used to look up the right
vertex coordinates. By a similar process we can access the values
associated with the nodes of element ``c``::

  f.values[fs.cell_nodes[c, :]]

A Python implementation of interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/Bb_9iRsTUgc>`_

Putting together the change of coordinates with the right indirect
addressing, we can provide the
:class:`~fe_utils.function_spaces.Function` class with a
:meth:`~fe_utils.function_spaces.Function.interpolate` method which
interpolates a user-provided function onto the
:class:`~fe_utils.function_spaces.Function`.

.. proof:exercise::
   
   Read and understand the
   :meth:`~fe_utils.function_spaces.Function.interpolate` method. Use
   ``plot_sin_function`` to investigate interpolating different
   functions onto finite element spaces at differering resolutions and
   polynomial degrees.

.. hint::

   There is no implementation work associated with this exercise, but
   the programming constructs used in
   :meth:`~fe_utils.function_spaces.Function.interpolate` will be
   needed when you implement integration.

.. _integration:

Integration
-----------

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/hvPR8CUwq3Q>`_


We now come to one of the fundamental operations in the finite element
method: integrating a :class:`~fe_utils.function_spaces.Function` over
the domain. The full finite element method actually requires the
integration of expressions of unknown test and trial functions, but we
will start with the more straightforward case of integrating a single,
known, :class:`~fe_utils.function_spaces.Function` over a domain
`\Omega`:

.. math::
   :label:

   \int_\Omega f \mathrm{d} x \quad f \in V

where `\mathrm{d}x` should be understood as being the volume measure
with the correct dimension for the domain and `V` is some finite
element space over `\Omega`. We can express this integral as a sum of
integrals over individual cells:

.. math::
   :label: integral_sum

   \int_\Omega f \mathrm{d} x = \sum_{c\in\Omega} \int_c f \mathrm{d} x.

So we have in fact reduced the integration problem to the problem of
integrating `f` over each cell. In :doc:`a previous part <1_quadrature>`
of the module we implemented quadrature rules which enable us to
integrate over specified reference cells. If we can express the
integral over some arbitrary cell `c` as an integral over a reference
cell `c_0` then we are done. In fact this simply requires us to employ
the change of variables formula for integration:

.. math::
   :label:

   \int_{c} f(x) \mathrm{d} x = \int_{c_0} f(X) |J|\mathrm{d} X

where `|J|` is the absolute value of the determinant of the Jacobian
matrix. `J` is given by:

.. math::
   :label: jacobian_def 

   J_{\alpha\beta} = \frac{\partial x_\alpha}{\partial X_\beta}.

.. hint::

   We will generally adopt the convention of using Greek letters to
   indicate indices in spatial dimensions, while we will use Roman
   letters in the sequence `i,j,\ldots` for basis function indices. We
   will continue to use `q` for the index over the quadrature points.

Evaluating :eq:`jacobian_def` depends on having an expression for `x` in
terms of `X`. Fortunately, :eq:`change` is exactly this expression,
and applying the usual rule for differentiating functions in finite
element spaces produces:

.. math::
   :label: jacobian

   J_{\alpha\beta} = \sum_j (\tilde{x}_j)_\alpha \nabla_\beta\Psi_j(X)

where `\{\Psi_j\}` is once again the degree 1 Lagrange basis and
`\{\tilde{x}_j\}` are the coordinates of the corresponding vertices of
cell `c`. The presence of `X` in :eq:`jacobian` implies that the
Jacobian varies spatially across the reference cell. However since
`\{\Psi_j\}` is the degree 1 Lagrange basis, the gradients of the
basis functions are constant over the cell and so it does not matter
at which point in the cell the Jacobian is evaluated. For example we
might choose to evaluate the Jacobian at the cell origin `X=0`.

.. hint::

   When using simplices with curved sides, and on all but the simplest
   quadrilateral or hexahedral meshes, the change of coordinates
   will not be affine. In that case, to preserve full accuracy it will be
   necessary to compute the Jacobian at every quadrature
   point. However, non-affine coordinate transforms are beyond the
   scope of this course.

Expressing the function in the finite element basis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/qKX3BGbbj58>`_

Let `\{\Phi_i(X)\}` be a **local** basis for `V` on the reference element
`c_0`. Then our integral becomes:

.. math::
   :label:

   \int_c f(x)\mathrm{d}x  = \int_{c_0} \sum_i F(M(c,i))\,\Phi_i(X)\, |J|\,\mathrm{d} X

where `F` is the vector of global coefficient values of `f`, and `M` is :ref:`the cell node map <cell-node>`.

Numerical quadrature
~~~~~~~~~~~~~~~~~~~~

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/5zby5uZUye0>`_

The actual evaluation of the integral will employ the quadrature rules
we discussed in :doc:`a previous section <1_quadrature>`. Let `\{X_q\},
\{w_q\}` be a quadrature rule of sufficient degree of precision that
the quadrature is exact. Then:

.. math::
   :label: integration

   \int_c f(x)\mathrm{d}x  = \sum_q \sum_i F(M(c,i))\,\Phi_i(X_q)\, |J|\,w_q

Implementing integration
~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   A video recording of this section is available `here <https://www.youtube.com/embed/XTUc2VcWKMU>`_


.. proof:exercise::

   Use :eq:`jacobian` to implement the
   :meth:`~fe_utils.mesh.Mesh.jacobian` method of
   :class:`~fe_utils.mesh.Mesh`. ``test/test_09_jacobian.py`` is
   available for you to test your results.

.. hint::

   The `\nabla_\beta\Psi_j(X)` factor in :eq:`jacobian` is the same
   for every cell in the mesh. You could make your implementation more
   efficient by precalculating this term in the :meth:`__init__`
   method of :class:`~fe_utils.mesh.Mesh`.

.. proof:exercise:: 

   Use :eq:`integral_sum` and :eq:`integration` to implement
   :meth:`~fe_utils.function_spaces.Function.integrate`.
   ``test/test_10_integrate_function.py`` may be used to test your
   implementation.

.. hint::

   Your method will need to:

   #. Construct a suitable :class:`~fe_utils.quadrature.QuadratureRule`.
   #. :meth:`~fe_utils.finite_elements.FiniteElement.tabulate` the
      basis functions at each quadrature point.
   #. Visit each cell in turn.
   #. Construct the :meth:`~fe_utils.mesh.Mesh.jacobian` for that cell
      and take the absolute value of its determinant (:data:`numpy.absolute`
      and :func:`numpy.linalg.det` will be useful here).
   #. Sum all of the arrays you have constructed over the correct
      indices to a contribution to the integral (:func:`numpy.einsum`
      may be useful for this).

.. hint::
   
   You might choose to read ahead before implementing
   :meth:`~fe_utils.function_spaces.Function.integrate`, since the
   :func:`~fe_utils.utils.errornorm` function is very similar and may provide a useful
   template for your work.
