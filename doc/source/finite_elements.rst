.. default-role:: math

Finite elements
===============

At the core of the finite element method is the representation of
finite-dimensional function spaces over elements. This concept was
formalised by Ciarlet CITE:

.. definition:: 

   A *finite element* is a triple `(K, P, N)` in
   which `K` is a cell, `P` is a space of functions
   `K\rightarrow\mathbb{R}^n` and `N`, the set of *nodes*,
   is a basis for `P^*`, the dual space to `P`.

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

Functions in this space have the form `ax + by + c`. So the
function space has three unknown parameters, and its basis (and dual
basis) will therefore have three members. In order to ensure the correct
continuity between elements, the dual basis we need to use is the
evaluation of the function at each of the cell vertices. That is:

.. math::

  n_0(f) = f\left((0,0)\right)

  n_1(f) = f\left((1,0)\right)

  n_2(f) = f\left((0,1)\right)

We know that `\phi_i` has the form `ax + by + c` so now we can
use the definition of the nodal basis to determine the unknown
coefficients:

.. math::
  
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

  \begin{bmatrix}
  0 & 0 & 1\\
  1 & 0 & 1\\
  0 & 1 & 1\\
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
