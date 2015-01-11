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
