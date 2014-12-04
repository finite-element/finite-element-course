.. default-role:: math

Constructing finite elements
============================

At the core of the finite element method is the representation of
finite-dimensional function spaces over elements. This concept was
formalised by Ciarlet CITE:

.. definition:: 

   A *finite element* is a triple `(K, P, N)` in which `K` is a cell,
   `P` is a space of functions `K\rightarrow\mathbb{R}^n` and `N`, the
   set of *nodes*, is a basis for `P^*`, the `dual space
   <http://mathworld.wolfram.com/DualVectorSpace.html>`_ to `P`.

Note that this definition includes a basis for `P^*`, but not a
basis for `P`. It turns out to be most convenient to specify the set
of nodes for an element, and then derive an appropriate basis for
`P` from that. In particular:

.. definition:: 

   Let `N = \{n_j\}` be a basis for `P^*`.  A *nodal
   basis*, `\{\phi_i\}` for `P` is a basis for `P`
   with the property that `n_j(\phi_i) = \delta_{ij}`.


A worked example
----------------

To illustrate the construction of a nodal basis, let's consider the
linear polynomials on a triangle. We first need to define our
reference cell. The obvious choice is the triangle with vertices
`\{(0,0), (1,0), (0,1)\}` 

Functions in this space have the form `a + bx+ cy`. So the
function space has three unknown parameters, and its basis (and dual
basis) will therefore have three members. In order to ensure the correct
continuity between elements, the dual basis we need to use is the
evaluation of the function at each of the cell vertices. That is:

.. math::
  :label:

  n_0(f) = f\left((0,0)\right)

  n_1(f) = f\left((1,0)\right)

  n_2(f) = f\left((0,1)\right)

We know that `\phi_i` has the form `a + bx + cy` so now we can
use the definition of the nodal basis to determine the unknown
coefficients:

.. math::
  :label:

  \begin{pmatrix}
  n_0(\phi_i)\\
  n_1(\phi_i)\\
  n_2(\phi_i)
  \end{pmatrix}
  =
  \begin{pmatrix}
  \delta_{i,0}\\
  \delta_{i,1}\\
  \delta_{i,2}
  \end{pmatrix}

So for `\phi_0` we have:

.. math::
  :label: phimat

  \begin{bmatrix}
  1 & 0 & 0\\
  1 & 1 & 0\\
  1 & 0 & 1\\
  \end{bmatrix}
  \begin{bmatrix}
  a\\
  b\\
  c\\
  \end{bmatrix}
  = 
  \begin{bmatrix}
  1 \\
  0 \\
  0
  \end{bmatrix}

Which has solution `\phi_0 = 1 - x - y`. By a similar process,
we can establish that the full basis is given by:

.. math::
   :label:

   \phi_0 = 1 - x - y
   
   \phi_1 = x

   \phi_2 = y


Types of node
-------------

We have just encountered nodes given by the evaluation of the function
at a given point. Other forms of functional are also suitable for use
as finite element nodes. Examples include the integral of the function
of ver the cell or some sub-entity and the evaluation of the gradient
of the function at some point. For some vector-valued function spaces,
the nodes may be given by the evaluation of the components of the
function normal or tangent to the boundary of the cell at some point.

In this course we will only consider point evaluation nodes. The use of several other forms of node are covered in [CITE KIRBY 2005]


.. _sec-vandermonde:
Solving for basis functions
---------------------------

The matrix in :eq:`phimat` is a *generalised Vandermonde* [#vandermonde]_
matrix . Given a list of points `(x_i,y_i) \in \mathbb{R}^2, 0\leq i< m`
the corresponding degree `n` generalised Vandermonde matrix is given by:

.. math::
    :label: Vandermonde

    \mathrm{V} = 
    \begin{bmatrix}
    1 & x_0 & y_0 & x_0^2 & x_0y_0 & y_0^2 & \ldots & x_0^n & x_0^{n-1}y_0 & \ldots & x_0y_0^{n-1} & y_0^n \\
    1 & x_1 & y_1 & x_1^2 & x_1y_1 & y_1^2 & \ldots & x_1^n & x_1^{n-1}y_1 & \ldots & x_1y_1^{n-1} & y_1^n \\
    \vdots \\
    1 & x_m & y_m & x_m^2 & x_my_m & y_m^2 & \ldots & x_m^n & x_m^{n-1}y_m & \ldots & x_my_m^{n-1} & y_m^n \\
    \end{bmatrix}

The equation for the complete set of basis function polynomial coefficients 
is then:

.. math::
   :label: vdm-equation

   \mathrm{V}\mathrm{C} = \mathrm{I}

where the `j`-th column of `C` contains the polynomial coefficients of
the basis function corresponding to the `j`-th node. For
:eq:`vdm-equation` to be well-posed, there must be a number of nodes
equal to the number of coefficients of a degree `n` polynomial. If
this is the case, then it follows immediately that:

.. math::
   :label:
   
   \mathrm{C} = \mathrm{V}^{-1}

The same process applies to the construction of basis functions for
elements in one or three dimensions, except that the Vandermonde
matrix must be modified to exclude powers of `y` (in one dimension) or
to include powers of `z`. 

.. note::

   The power series basis for polynomial spaces employed here becomes
   increasingly ill-conditioned at higher order, so it may be
   advantageous to employ a different basis in the construction of the
   Vandermonde matrix. See [CITE KIRBY2004] for an example.

The Lagrange element nodes
--------------------------

The number of coefficients of a degree `n` polynomial in `d`
dimensions is given by `\begin{pmatrix}n+d-1\\ d\end{pmatrix}`. The
simplest set of nodes which we can employ is simply to place these
nodes in a regular grid over the reference cell. Given the classical
relationship between binomial coefficients and `Pascal's triangle
<http://mathworld.wolfram.com/PascalsTriangle.html>`_ (and between
trinomial coefficients and Pascal's pyramid), it is unsurprising that
this produces the correct number of nodes.

The set of equally spaced points of degree `n` on the triangle is:

.. math::
   :label: lattice

   L_n = \left\{\left(\frac{i}{n}, \frac{j}{n}\right)\middle| 0 \leq i+j \leq n\right\}
  
The finite elements with this set of nodes are called the *equispaced
Lagrange* elements and are the most commonly used elements for
relatively low order computations. 

.. note::

   At higher order the equispaced Lagrange basis is poorly conditioned
   and creates unwanted oscillations in the solutions. However for
   this course Lagrange elements will be sufficient.


Implementing finite elements in python
--------------------------------------

.. _ex-lagrange-points:

.. exercise::
   
   Use :eq:`lattice` to implement
   :func:`~fe_utils.finite_elements.lagrange_points`. Make sure your
   algorithm also works for one-dimensional elements.

.. _ex-vandermonde:

.. exercise::

   Use :eq:`Vandermonde` to implement
   :func:`~fe_utils.finite_elements.vandermonde_matrix`. Think
   carefully about how to loop over each row to construct the correct
   powers of `x` and `y`. For the purposes of this exercise you should
   ignore the ``grad`` argument.

.. hint::

   You can use numpy array operations to construct whole columns of
   the matrix at once.

.. _ex-lagrange:

.. exercise::

   Implement the rest of the
   :class:`~fe_utils.finite_elements.FiniteElement` :meth:`__init__`
   method. You should construct a Vandermonde matrix for the nodes and
   invert it to create the basis function coeffs. Store these as
   ``self.basis_coeffs``.



Associating nodes with the mesh topology
----------------------------------------

In the worked example we asserted that evaluation at the vertices was
the correct set of nodes. Let's now establish that more rigorously. We
associate nodes with topological entitities of the cell: nodes may be
associated with the vertices, edges, or faces of the cell, or with the
interior of the cell itself. When we stitch together cells to form the
mesh, those nodes associated with topological entities on the boundary
of the cell will be shared by more than one cell. This enforces some
level of function continuity between cells since the function is
forced to take the nodal value in both cells.

Let's assume for the moment that we wish our finite element space to
have `C0` continuity over the mesh.

.. rubric:: Footnotes

.. [#vandermonde] A `Vandermonde
                  matrix <http://mathworld.wolfram.com/VandermondeMatrix.html>`_
                  is the one-dimensional case of the generalised Vandermonde matrix.
