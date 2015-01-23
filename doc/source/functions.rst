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
---------------------------------------------------------

We'll refer to coordinates on the global mesh as being in *physical
space* while those on the reference element are in *local
space*. We'll use case to distinguish local and global objects, so
local coordinates will be written as `X` and global coordinates as
`x`. The key observation is that within each cell, the global
coordinates are the linear interpolation of the global coordinate
values at the cell vertices. In other words, if `\{\psi_i\}` is the
local basis for the linear lagrange elements on the reference cell and
`X_i` are the corresponding global vertex locations on a cell `c`
then:

.. math::

   X = \sum_i X_i \psi_i(x) \quad \forall x \in c.


